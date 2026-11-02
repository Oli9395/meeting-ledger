import hmac
import json
import os
import secrets
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone

from fastapi import BackgroundTasks, FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import asr, db, metrics, pipeline, render
from .dates import anchor
from .llm import get_provider
from .parse import parse_text

HERE = os.path.dirname(__file__)
MAX_TEXT = 60000
MIN_TEXT = 20
MAX_AUDIO = 200 * 1024 * 1024
ADMIN_KEY = os.environ.get("BP_ADMIN_KEY", "")
MAX_DAY = int(os.environ.get("BP_MAX_MEETINGS_PER_DAY", "200"))
MAX_LEDGER_DAY = int(os.environ.get("BP_MAX_LEDGER_MEETINGS_PER_DAY", "10"))

app = FastAPI(title="Meeting Ledger", docs_url=None, redoc_url=None)
workers = ThreadPoolExecutor(max_workers=int(os.environ.get("BP_WORKERS", "4")))
db.init()


def recover():
    # Background tasks are lost when the service restarts, so meetings must not stay stuck in processing forever
    with db.tx() as c:
        c.execute("UPDATE meetings SET status='failed', error='The service restarted and processing was interrupted. Please submit again.' WHERE status='processing'")


@app.middleware("http")
async def security_headers(request: Request, call_next):
    r = await call_next(request)
    r.headers["Referrer-Policy"] = "no-referrer"
    r.headers["X-Content-Type-Options"] = "nosniff"
    r.headers["X-Frame-Options"] = "DENY"
    r.headers["Content-Security-Policy"] = "default-src 'self'; style-src 'self'; style-src-attr 'unsafe-inline'; script-src 'self'; img-src 'self' data:"
    return r


def ledger_or_404(c, token):
    row = c.execute("SELECT * FROM ledgers WHERE token=?", (token,)).fetchone()
    if not row:
        raise HTTPException(404, "Ledger not found or already deleted")
    return dict(row)


def err(status, msg):
    raise HTTPException(status, msg)


class NewLedger(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    members: list[str] = []
    tag: str | None = Field(default=None, max_length=40)


@app.post("/api/ledgers")
def create_ledger(b: NewLedger):
    token = secrets.token_urlsafe(16)
    with db.tx() as c:
        cur = c.execute("INSERT INTO ledgers(token,name,members_json,tag,created_at) VALUES(?,?,?,?,?)",
                        (token, b.name.strip(), json.dumps(clean_members(b.members), ensure_ascii=False), b.tag, db.now()))
        db.event(c, cur.lastrowid, "ledger_created")
    return {"token": token}


def clean_members(ms):
    out = []
    for m in ms:
        m = (m or "").strip()[:40]
        if m and m not in out:
            out.append(m)
    return out[:50]


SAMPLE = [("M1", "2026-10-06", "Advisor 1-on-1", "one_on_one"), ("M2", "2026-10-08", "Group meeting, week 1", "group"), ("M3", "2026-10-15", "Group meeting, week 2", "group")]
SAMPLE_MEMBERS = ["Zhou Lan", "Chen Siyuan", "Wang Bo", "Li Muqing", "Daniel Ong", "Priya Nair"]


@app.post("/api/sample")
def create_sample():
    """Sample ledger: a fictional group that replays recorded real model output without calling the model. The first two meetings are already confirmed; the third is left for the visitor to confirm."""
    token = secrets.token_urlsafe(16)
    with db.tx() as c:
        lid = c.execute("INSERT INTO ledgers(token,name,members_json,is_sample,created_at) VALUES(?,?,?,1,?)",
                        (token, "Sample: Robot Learning Group (fictional)", json.dumps(SAMPLE_MEMBERS, ensure_ascii=False), db.now())).lastrowid
    for n, (code, d, title, kind) in enumerate(SAMPLE, 1):
        with open(os.path.join(HERE, "..", "samples", f"{code}.txt"), encoding="utf8") as f:
            text = f.read()
        with db.tx() as c:
            mid = c.execute("INSERT INTO meetings(ledger_id,seq,code,date,title,kind,source,status,created_at) VALUES(?,?,?,?,?,?,'text','processing',?)",
                            (lid, n, code, d, title, kind, db.now())).lastrowid
            pipeline.store_utterances(c, lid, mid, code, parse_text(text))
        pipeline.process(mid)
        if n < len(SAMPLE):
            with db.tx() as c:
                c.execute("UPDATE items SET review='confirmed', decided_at=? WHERE meeting_id=? AND review='pending'", (db.now(), mid))
                for p in c.execute("SELECT * FROM proposals WHERE meeting_id=? AND decision='pending'", (mid,)).fetchall():
                    apply_decision(c, dict(p), "confirmed")
    return {"token": token}


def public_ledger(c, l):
    meetings = [public_meeting(dict(m)) for m in c.execute("SELECT * FROM meetings WHERE ledger_id=? ORDER BY seq", (l["id"],))]
    counts = {r["task_status"]: r["n"] for r in c.execute(
        "SELECT task_status, COUNT(*) n FROM items WHERE ledger_id=? AND kind='commitment' AND review='confirmed' GROUP BY task_status", (l["id"],))}
    return {"name": l["name"], "members": json.loads(l["members_json"]), "terms": json.loads(l.get("terms_json") or "[]"), "is_sample": bool(l["is_sample"]), "meetings": meetings, "counts": counts,
            "asr": asr.available(), "model_ready": provider_ready()}


_provider_ok = None


def provider_ready() -> bool:
    global _provider_ok
    if _provider_ok is None:
        _provider_ok = get_provider() is not None
    return _provider_ok


def public_meeting(m):
    m.pop("ledger_id", None)
    return {**m, "rejected": json.loads(m.pop("rejected_json")), "injections": json.loads(m.pop("injections_json"))}


@app.get("/api/l/{token}")
def get_ledger(token: str):
    with db.tx() as c:
        return public_ledger(c, ledger_or_404(c, token))


class Members(BaseModel):
    members: list[str]
    terms: list[str] = []


@app.post("/api/l/{token}/members")
def set_members(token: str, b: Members):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        c.execute("UPDATE ledgers SET members_json=?, terms_json=? WHERE id=?", (json.dumps(clean_members(b.members), ensure_ascii=False), json.dumps(clean_members(b.terms), ensure_ascii=False), l["id"]))
    return {"ok": True}


@app.delete("/api/l/{token}")
def delete_ledger(token: str):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        c.execute("DELETE FROM ledgers WHERE id=?", (l["id"],))
    return {"ok": True}


@app.post("/api/l/{token}/meetings")
async def create_meeting(token: str, meeting_date: str = Form(...), title: str = Form(""), kind: str = Form("group"),
                         text: str = Form(""), file: UploadFile | None = File(None)):
    try:
        d = date.fromisoformat(meeting_date)
    except ValueError:
        err(400, "Invalid meeting date format. Please use YYYY-MM-DD")
    if kind not in ("group", "one_on_one", "partner", "other"):
        err(400, "Invalid meeting type")
    with db.tx() as c:  # Check the date order first so the error message is accurate
        l = ledger_or_404(c, token)
        last_d = c.execute("SELECT MAX(date) d FROM meetings WHERE ledger_id=? AND status!='failed'", (l["id"],)).fetchone()["d"]
    if last_d and d.isoformat() < last_d:
        err(400, f"The meeting date can't be earlier than the previous meeting ({last_d}). Meetings must be reconciled in chronological order")
    utts, audio_path = None, None
    if file is not None and file.filename:
        name = file.filename.lower()
        data = await file.read(MAX_AUDIO + 1)
        if len(data) > MAX_AUDIO:
            err(413, "File is too large. The limit is 200 MB")
        if name.endswith((".txt", ".md")):
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                err(400, "Text files must be UTF-8 encoded")
        else:
            if not asr.available():
                err(503, "Speech transcription isn't enabled on this deployment. Please paste the text instead")
            fd, audio_path = tempfile.mkstemp(suffix=os.path.splitext(name)[1] or ".bin")
            with os.fdopen(fd, "wb") as f:
                f.write(data)
    if audio_path is None:
        text = text.strip()
        if len(text) < MIN_TEXT:
            err(400, "The content is too short. Please paste the full meeting text")
        if len(text) > MAX_TEXT:
            err(400, f"The content is too long. The limit is {MAX_TEXT} characters, so please submit it in parts")
        utts = parse_text(text)
        if not utts:
            err(400, "No utterances could be parsed")
    with db.tx() as c:
        l = ledger_or_404(c, token)
        today = datetime.now(timezone.utc).date().isoformat()
        if not l["is_sample"]:
            if c.execute("SELECT COUNT(*) FROM meetings WHERE created_at>=?", (today,)).fetchone()[0] >= MAX_DAY:
                err(429, "Today's total processing quota has been used up. Please try again tomorrow")
            if c.execute("SELECT COUNT(*) FROM meetings WHERE ledger_id=? AND created_at>=?", (l["id"], today)).fetchone()[0] >= MAX_LEDGER_DAY:
                err(429, "This ledger has had too many submissions today. Please try again tomorrow")
            if not audio_path and not provider_ready():
                err(503, "The service has no model configured, so only the sample ledger is available for now")
        last = c.execute("SELECT MAX(seq) s, MAX(date) d FROM meetings WHERE ledger_id=? AND status!='failed'", (l["id"],)).fetchone()
        if last["d"] and d.isoformat() < last["d"]:
            err(400, f"The meeting date can't be earlier than the previous meeting ({last['d']}). Meetings must be reconciled in chronological order")
        if c.execute("SELECT 1 FROM meetings WHERE ledger_id=? AND status='processing'", (l["id"],)).fetchone():
            err(409, "The previous meeting is still processing. Please wait for it to finish")
        seq = (c.execute("SELECT MAX(seq) s FROM meetings WHERE ledger_id=?", (l["id"],)).fetchone()["s"] or 0) + 1
        code = f"M{seq}"
        mid = c.execute("INSERT INTO meetings(ledger_id,seq,code,date,title,kind,source,status,stage,created_at) VALUES(?,?,?,?,?,?,?,'processing','queued',?)",
                        (l["id"], seq, code, d.isoformat(), title.strip()[:120] or None, kind, "audio" if audio_path else "text", db.now())).lastrowid
        if utts:
            pipeline.store_utterances(c, l["id"], mid, code, utts)
        db.event(c, l["id"], "meeting_submitted", json.dumps({"source": "audio" if audio_path else "text"}))
    workers.submit(pipeline.process, mid, None, audio_path)
    return {"code": code}


def meeting_detail(c, l, code):
    m = c.execute("SELECT * FROM meetings WHERE ledger_id=? AND code=?", (l["id"], code)).fetchone()
    if not m:
        err(404, "Meeting not found")
    m = dict(m)
    utts = [dict(u) for u in c.execute("SELECT id,seq,ts,speaker,text FROM utterances WHERE ledger_id=? AND meeting_id=? ORDER BY seq", (l["id"], m["id"]))]
    spk = {u["id"]: u["speaker"] for u in utts}
    items = [{**dict(i), "speaker": spk.get(i["utterance_id"]), "slots": json.loads(i["slots_json"])}
             for i in c.execute("SELECT * FROM items WHERE ledger_id=? AND meeting_id=? ORDER BY id", (l["id"], m["id"]))]
    props = []
    for p in c.execute("""SELECT p.*, i.code AS item_code, i.quote AS item_quote, i.title AS item_title, i.owner_state, i.owner_value, i.due_raw AS item_due_raw, i.due_date AS item_due_date,
            i.utterance_id AS item_utterance_id, i.strength AS item_strength, i.kind AS item_kind, im.code AS item_meeting, im.date AS item_meeting_date, im.seq AS m_seq, i.ledger_id, i.id AS iid
            FROM proposals p JOIN items i ON i.id=p.item_id LEFT JOIN meetings im ON im.id=i.meeting_id
            WHERE p.ledger_id=? AND p.meeting_id=? ORDER BY p.id""", (l["id"], m["id"])):
        d = dict(p)
        d["evidence"] = json.loads(d["evidence_json"])
        d["flags"] = json.loads(d["flags_json"])
        d["unmentioned"] = pipeline.unmentioned_count(c, {"id": d["iid"], "ledger_id": d["ledger_id"], "m_seq": d["m_seq"]})
        props.append(d)
    return m, utts, items, props


@app.get("/api/l/{token}/meetings/{code}")
def get_meeting(token: str, code: str):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        m, utts, items, props = meeting_detail(c, l, code)
        return {"meeting": public_meeting(dict(m)), "utterances": utts, "items": items, "proposals": props}


class ItemPatch(BaseModel):
    title: str | None = Field(default=None, max_length=300)
    owner: str | None = Field(default=None, max_length=60)
    due_date: str | None = None


def touch_item(c, lid, iid):
    i = c.execute("SELECT * FROM items WHERE id=? AND ledger_id=?", (iid, lid)).fetchone()
    if not i:
        err(404, "Item not found")
    return dict(i)


def audit(c, lid, action, target, before, after):
    c.execute("INSERT INTO audit_log(ledger_id,action,target,before_json,after_json,created_at) VALUES(?,?,?,?,?,?)",
              (lid, action, target, json.dumps(before, ensure_ascii=False, default=str), json.dumps(after, ensure_ascii=False, default=str), db.now()))


@app.patch("/api/l/{token}/items/{iid}")
def patch_item(token: str, iid: int, b: ItemPatch):
    fields = b.model_fields_set
    with db.tx() as c:
        l = ledger_or_404(c, token)
        i = touch_item(c, l["id"], iid)
        before = {k: i[k] for k in ("title", "owner_value", "owner_state", "due_date", "due_state")}
        sets, args, changed = [], [], False
        if "title" in fields and (b.title or None) != i["title"]:
            sets.append("title=?"); args.append(b.title or None); changed = True
        if "owner" in fields:
            o = (b.owner or "").strip() or None
            if o != i["owner_value"]:
                sets += ["owner_value=?", "owner_state=?", "owner_basis=?"]
                args += [o, "given" if o else "absent", "user"]
                changed = True
        if "due_date" in fields:
            nd = b.due_date or None
            if nd:
                try:
                    date.fromisoformat(nd)
                except ValueError:
                    err(400, "Invalid date format")
            if nd != i["due_date"]:
                sets += ["due_date=?", "due_state=?"]
                args += [nd, "given" if nd else ("vague" if i["due_raw"] else "absent")]
                changed = True
        if changed:
            sets += ["edited=1", "updated_at=?"]
            args += [db.now(), iid]
            c.execute(f"UPDATE items SET {','.join(sets)} WHERE id=?", args)
            audit(c, l["id"], "item_edited", str(iid), before, b.model_dump(exclude_unset=True))
        return dict(touch_item(c, l["id"], iid))


class Review(BaseModel):
    action: str


@app.post("/api/l/{token}/items/{iid}/review")
def review_item(token: str, iid: int, b: Review):
    if b.action not in ("confirm", "reject", "reopen"):
        err(400, "Invalid action")
    with db.tx() as c:
        l = ledger_or_404(c, token)
        i = touch_item(c, l["id"], iid)
        new = {"confirm": "confirmed", "reject": "rejected", "reopen": "pending"}[b.action]
        c.execute("UPDATE items SET review=?, decided_at=?, updated_at=? WHERE id=?", (new, db.now(), db.now(), iid))
        audit(c, l["id"], "item_" + b.action, str(iid), {"review": i["review"]}, {"review": new})
        db.event(c, l["id"], "draft_" + b.action, json.dumps({"edited": i["edited"]}))
        return dict(touch_item(c, l["id"], iid))


class TaskStatus(BaseModel):
    task_status: str


@app.post("/api/l/{token}/items/{iid}/status")
def set_status(token: str, iid: int, b: TaskStatus):
    if b.task_status not in ("todo", "doing", "done", "dropped"):
        err(400, "Invalid status")
    with db.tx() as c:
        l = ledger_or_404(c, token)
        i = touch_item(c, l["id"], iid)
        if i["review"] != "confirmed":
            err(409, "A draft must be confirmed before it can become a task")
        c.execute("UPDATE items SET task_status=?, updated_at=? WHERE id=?", (b.task_status, db.now(), iid))
        audit(c, l["id"], "task_status", str(iid), {"task_status": i["task_status"]}, {"task_status": b.task_status})
    return {"ok": True}


class NewTask(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    owner: str | None = None
    due_date: str | None = None


@app.post("/api/l/{token}/tasks")
def add_task(token: str, b: NewTask):
    if b.due_date:
        try:
            date.fromisoformat(b.due_date)
        except ValueError:
            err(400, "Invalid date format")
    with db.tx() as c:
        l = ledger_or_404(c, token)
        n = c.execute("SELECT COUNT(*) FROM items WHERE ledger_id=? AND manual=1", (l["id"],)).fetchone()[0] + 1
        cur = c.execute("""INSERT INTO items(ledger_id,code,kind,title,owner_state,owner_value,owner_basis,due_state,due_date,review,manual,created_at,decided_at)
            VALUES(?,?,'commitment',?,?,?,'user',?,?,'confirmed',1,?,?)""",
                        (l["id"], f"I-T-{n:02d}", b.title.strip(), "given" if b.owner else "absent", b.owner or None, "given" if b.due_date else "absent", b.due_date, db.now(), db.now()))
        return {"id": cur.lastrowid}


@app.get("/api/l/{token}/tasks")
def list_tasks(token: str):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        rows = c.execute("""SELECT i.*, m.code m_code, m.date m_date, m.title m_title FROM items i LEFT JOIN meetings m ON m.id=i.meeting_id
            WHERE i.ledger_id=? AND i.kind='commitment' AND i.review='confirmed' ORDER BY i.task_status='done', i.due_date IS NULL, i.due_date, i.id""", (l["id"],)).fetchall()
        tasks = []
        for r in rows:
            d = dict(r)
            d["m_seq"] = None
            if d["meeting_id"]:
                d["m_seq"] = c.execute("SELECT seq FROM meetings WHERE id=?", (d["meeting_id"],)).fetchone()[0]
            d["unmentioned"] = pipeline.unmentioned_count(c, d) if d["task_status"] in ("todo", "doing") else 0
            tasks.append(d)
        return {"tasks": tasks}


def apply_decision(c, p, decision):
    now = db.now()
    item = dict(c.execute("SELECT * FROM items WHERE id=?", (p["item_id"],)).fetchone())
    if p["decision"] == "confirmed" and decision != "confirmed":
        # Undo: restore the state from before the transition
        before = c.execute("SELECT before_json FROM audit_log WHERE action='proposal_confirmed' AND target=? ORDER BY id DESC LIMIT 1", (str(p["id"]),)).fetchone()
        if before:
            b = json.loads(before["before_json"])
            c.execute("UPDATE items SET task_status=?, due_date=?, due_raw=?, due_state=?, updated_at=? WHERE id=?",
                      (b["task_status"], b["due_date"], b["due_raw"], b["due_state"], now, item["id"]))
    if decision == "confirmed":
        snap = {k: item[k] for k in ("task_status", "due_date", "due_raw", "due_state")}
        new_status = {"fulfilled": "done", "abandoned": "dropped", "partial_or_rescheduled": "doing"}[p["transition"]]
        due_raw, due_date, due_state = item["due_raw"], item["due_date"], item["due_state"]
        if p["transition"] == "partial_or_rescheduled" and p["new_due_raw"]:
            # If the new time can't be resolved to a date, keep the existing date rather than clearing what the user entered
            due_raw = p["new_due_raw"]
            if p["new_due_date"]:
                due_date, due_state = p["new_due_date"], "given"
            elif not due_date:
                due_state = "vague"
        c.execute("UPDATE items SET task_status=?, due_raw=?, due_date=?, due_state=?, updated_at=? WHERE id=?",
                  (new_status, due_raw, due_date, due_state, now, item["id"]))
        # The task board only holds confirmed drafts; confirming a reconciliation is itself a human confirmation of the item
        if item["review"] == "pending":
            c.execute("UPDATE items SET review='confirmed', decided_at=? WHERE id=?", (now, item["id"]))
        audit(c, p["ledger_id"], "proposal_confirmed", str(p["id"]), snap, {"task_status": new_status})
    c.execute("UPDATE proposals SET decision=?, decided_at=? WHERE id=?", (decision, now, p["id"]))


class Decide(BaseModel):
    decision: str
    transition: str | None = None  # The user can override the verdict, e.g. "actually only part of it was done"


@app.post("/api/l/{token}/proposals/{pid}/decide")
def decide(token: str, pid: int, b: Decide):
    if b.decision not in ("confirmed", "dismissed", "pending"):
        err(400, "Invalid action")
    with db.tx() as c:
        l = ledger_or_404(c, token)
        p = c.execute("SELECT * FROM proposals WHERE id=? AND ledger_id=?", (pid, l["id"])).fetchone()
        if not p:
            err(404, "Proposal not found")
        if p["proposed_by"] != "model":
            err(409, "Not-mentioned items don't need confirmation")
        p = dict(p)
        if b.transition:
            if b.transition not in ("fulfilled", "partial_or_rescheduled", "abandoned"):
                err(400, "Invalid status")
            if p["decision"] == "confirmed":
                apply_decision(c, p, "pending")
                p["decision"] = "pending"
            c.execute("UPDATE proposals SET transition=?, flags_json=? WHERE id=?", (b.transition, json.dumps(json.loads(p["flags_json"]) + ["changed_by_user"]), pid))
            p["transition"] = b.transition
            db.event(c, l["id"], "proposal_retyped", json.dumps({"to": b.transition}))
        apply_decision(c, p, b.decision)
        db.event(c, l["id"], "proposal_" + b.decision)
    return {"ok": True}


@app.get("/api/l/{token}/followup/{code}")
def followup(token: str, code: str):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        m, _, items, _ = meeting_detail(c, l, code)
        # Only the latest meeting shows follow-ups: progress on older items is already in later meetings
        latest = c.execute("SELECT MAX(seq) FROM meetings WHERE ledger_id=? AND status='ready'", (l["id"],)).fetchone()[0]
    return {"text": render.followups(items, m["date"]) if m["seq"] == latest else ""}


@app.get("/api/l/{token}/tasks.csv")
def export_csv(token: str):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        rows = c.execute("""SELECT i.*, m.date m_date FROM items i LEFT JOIN meetings m ON m.id=i.meeting_id
            WHERE i.ledger_id=? AND i.kind='commitment' AND i.review='confirmed' ORDER BY i.id""", (l["id"],)).fetchall()
        db.event(c, l["id"], "exported", json.dumps({"format": "csv"}))
    return Response(render.tasks_csv(rows), media_type="text/csv; charset=utf-8", headers={"Content-Disposition": 'attachment; filename="tasks.csv"'})


@app.get("/api/l/{token}/export/{code}.md", response_class=PlainTextResponse)
def export_md(token: str, code: str):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        m, utts, items, props = meeting_detail(c, l, code)
        tasks = []
        db.event(c, l["id"], "exported", json.dumps({"code": code}))
    return render.minutes_md(m, utts, items, props, tasks)


class Feedback(BaseModel):
    target_type: str = Field(max_length=20)
    target_id: str = Field(default="", max_length=40)
    rating: str = Field(default="", max_length=10)
    reason: str = Field(default="", max_length=60)
    comment: str = Field(default="", max_length=2000)


@app.post("/api/l/{token}/feedback")
def add_feedback(token: str, b: Feedback):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        c.execute("INSERT INTO feedback(ledger_id,target_type,target_id,rating,reason,comment,created_at) VALUES(?,?,?,?,?,?,?)",
                  (l["id"], b.target_type, b.target_id, b.rating, b.reason, b.comment, db.now()))
    return {"ok": True}


class Survey(BaseModel):
    sean_ellis: str = Field(pattern="^(very|somewhat|not)$")
    value_text: str = Field(default="", max_length=2000)
    missing: str = Field(default="", max_length=2000)


@app.post("/api/l/{token}/survey")
def add_survey(token: str, b: Survey):
    with db.tx() as c:
        l = ledger_or_404(c, token)
        c.execute("INSERT INTO surveys(ledger_id,sean_ellis,value_text,missing,created_at) VALUES(?,?,?,?,?)",
                  (l["id"], b.sean_ellis, b.value_text, b.missing, db.now()))
    return {"ok": True}


@app.get("/api/admin/metrics")
def admin_metrics(key: str = "", tag: str | None = None):
    if not ADMIN_KEY or not hmac.compare_digest(key, ADMIN_KEY):
        err(403, "Incorrect admin key")
    return metrics.compute(tag)


@app.get("/api/health")
def health():
    return {"ok": True, "asr": asr.available(), "model_ready": provider_ready()}


@app.exception_handler(HTTPException)
async def http_error(_, e: HTTPException):
    return JSONResponse({"error": e.detail}, status_code=e.status_code)


recover()
STATIC = os.path.join(HERE, "static")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
@app.get("/privacy")
@app.get("/l/{token}")
@app.get("/l/{token}/{rest:path}")
def spa(token: str = "", rest: str = ""):
    return FileResponse(os.path.join(STATIC, "index.html"))
