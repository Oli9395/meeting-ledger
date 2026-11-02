"""Processing pipeline: transcribe → extract → validate → reconcile → validate → not mentioned. The model only proposes, code decides, humans confirm."""
import json
import os
import time
from datetime import date

from . import asr, db, schemas, verify
from .dates import anchor
from .llm import LLMError, ReplayProvider, get_provider
from .parse import Utterance

HERE = os.path.dirname(__file__)
EXTRACT_V = os.environ.get("BP_EXTRACT_PROMPT", "extract_v3_en")
RECONCILE_V = os.environ.get("BP_RECONCILE_PROMPT", "reconcile_v2_en")
OPEN_KINDS = ("commitment", "question")


def prompt(name: str) -> str:
    with open(os.path.join(HERE, "prompts", name + ".txt"), encoding="utf8") as f:
        return f.read()


def sample_recordings() -> dict:
    p = os.path.join(HERE, "..", "samples", "recordings.json")
    with open(p, encoding="utf8") as f:
        return json.load(f)


def render_utts(utts: list[dict]) -> str:
    return "\n".join(f"{u['id']} | {u['ts'] or ''} | {u['speaker'] or ''} | {u['text']}" for u in utts)


def store_utterances(c, ledger_id, meeting_id, code, utts: list[Utterance]):
    for u in utts:
        c.execute("INSERT INTO utterances(id,ledger_id,meeting_id,seq,ts,speaker,text) VALUES(?,?,?,?,?,?,?)",
                  (f"{code}-U{u.seq:03d}", ledger_id, meeting_id, u.seq, u.ts, u.speaker, u.text))


def call(provider, c_args, step, attempt, system, user, schema, version):
    ledger_id, meeting_id = c_args
    t = time.time()
    try:
        r = provider.complete(step, system, user, schema)
    except LLMError as e:
        with db.tx() as c:
            c.execute("INSERT INTO llm_calls(ledger_id,meeting_id,step,attempt,provider,prompt_version,ms,ok,error,created_at) VALUES(?,?,?,?,?,?,?,0,?,?)",
                      (ledger_id, meeting_id, step, attempt, provider.name, version, int((time.time() - t) * 1000), str(e), db.now()))
        raise
    with db.tx() as c:
        c.execute("INSERT INTO llm_calls(ledger_id,meeting_id,step,attempt,provider,model,prompt_version,input_tokens,output_tokens,cost_usd,ms,ok,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,1,?)",
                  (ledger_id, meeting_id, step, attempt, r.provider, r.model, version, r.input_tokens, r.output_tokens, r.cost_usd, r.ms, db.now()))
    return r.data


def validate_items(raw_items, utts_by_id, banned, members, mdate):
    good, bad = [], []
    for it in raw_items:
        reason = verify.check_quote(it.get("quote", ""), it.get("utterance_id", ""), utts_by_id, banned)
        if reason:
            bad.append({"step": "extract", "quote": it.get("quote"), "utterance_id": it.get("utterance_id"), "reason": reason})
            continue
        u = utts_by_id[it["utterance_id"]]
        order = sorted(utts_by_id.values(), key=lambda x: x["seq"])
        pos = next(n for n, x in enumerate(order) if x["id"] == it["utterance_id"])
        # The 3 utterances before and after are used to check who "you" refers to
        window = order[max(0, pos - 3):pos + 4]
        two_people = {x["speaker"] for x in order if x["speaker"]}
        if len(two_people) == 2:
            window = [x for x in order if x["speaker"]][:50]
        owner = verify.check_owner(it["owner"], it["quote"], u["speaker"], members, window)
        due_raw = verify.check_due_raw((it.get("due") or {}).get("due_raw"), it["quote"], u["text"])
        due_state, due_date = anchor(due_raw, mdate)
        good.append({**it, "kind": it["kind"].lower(), "strength": it["strength"].lower(), "owner": owner,
                     "due_raw": due_raw, "due_state": due_state, "due_date": due_date})
    return good, bad


def validate_proposals(raw, open_items, utts_by_id, banned, mdate):
    good, bad = [], []
    by_code = {i["code"]: i for i in open_items}
    for p in raw:
        it = by_code.get(p.get("ledger_id"))
        if not it:
            bad.append({"step": "reconcile", "ledger_id": p.get("ledger_id"), "reason": "Item is not in the ledger"})
            continue
        ev = p.get("closure_evidence") or []
        reason = None if 1 <= len(ev) <= 3 else "Closure evidence must be 1 to 3 quotes"
        for e in ev:
            reason = reason or verify.check_quote(e.get("quote", ""), e.get("utterance_id", ""), utts_by_id, banned)
            if not reason and p["transition"].lower() == "fulfilled" and verify.norm(e["quote"]).endswith("?"):
                reason = "A question cannot prove an item is done"
            if not reason and verify.norm(e["quote"]) == verify.norm(it["quote"] or ""):
                reason = "The closure quote cannot be the same as the commitment quote"
        if reason:
            bad.append({"step": "reconcile", "ledger_id": p["ledger_id"], "reason": reason, "quote": (ev[0].get("quote") if ev else None)})
            continue
        new_raw = verify.check_due_raw(p.get("new_due_raw"), *[utts_by_id[e["utterance_id"]]["text"] for e in ev])
        _, new_date = anchor(new_raw, mdate)
        good.append({**p, "transition": p["transition"].lower(), "new_due_raw": new_raw, "new_due_date": new_date})
    return good, bad


def retry_note(bad: list[dict]) -> str:
    lines = [f"- {b.get('ledger_id') or b.get('utterance_id')}: {b['reason']} (your quote: {b.get('quote')})" for b in bad[:15]]
    return "\n\n<previous_output_failed_checks>\nThe program discarded these items. Output only these items again, and copy each quote verbatim from the utterance:\n" + "\n".join(lines) + "\n</previous_output_failed_checks>"


def open_ledger_items(c, ledger_id, before_seq):
    rows = c.execute(f"""SELECT i.*, m.code AS m_code, m.date AS m_date, m.seq AS m_seq FROM items i LEFT JOIN meetings m ON m.id=i.meeting_id
        WHERE i.ledger_id=? AND i.kind IN ('commitment','question') AND i.review IN ('pending','confirmed') AND i.task_status IN ('todo','doing')
        AND (m.seq<? OR i.manual=1) ORDER BY m.seq, i.id""", (ledger_id, before_seq)).fetchall()
    return [dict(r) for r in rows]


def unmentioned_count(c, item: dict) -> int:
    rows = c.execute("""SELECT m.id, m.seq, (SELECT p.transition FROM proposals p WHERE p.item_id=? AND p.meeting_id=m.id AND p.decision!='dismissed'
          ORDER BY (p.transition='not_mentioned') LIMIT 1) AS tr
        FROM meetings m WHERE m.ledger_id=? AND m.seq>? AND m.status='ready' ORDER BY m.seq DESC""",
                     (item["id"], item["ledger_id"], item.get("m_seq") or 0)).fetchall()
    n = 0
    for r in rows:
        if r["tr"] == "not_mentioned":
            n += 1
        elif r["tr"] is None:
            continue
        else:
            break
    return n


def render_ledger(c, items) -> str:
    lines = []
    for i in items:
        lines.append(f"{i['code']} | {i.get('m_code') or 'manual'} {i.get('m_date') or ''} | {i['owner_state']}:{i['owner_value'] or ''} | {i['strength'] or ''} | "
                     f"Task: \"{i['title'] or ''}\" Quote \"{i['quote'] or ''}\" | Original due words: {i['due_raw'] or 'none'} | Consecutive meetings not mentioned: {unmentioned_count(c, i)}")
    return "\n".join(lines)


def set_stage(meeting_id, stage):
    with db.tx() as c:
        c.execute("UPDATE meetings SET stage=? WHERE id=?", (stage, meeting_id))


def process(meeting_id: int, provider=None, audio_path: str | None = None):
    t0 = time.time()
    try:
        _process(meeting_id, provider, audio_path, t0)
    except (LLMError, ValueError, json.JSONDecodeError) as e:
        with db.tx() as c:
            c.execute("UPDATE meetings SET status='failed', error=?, finished_at=?, ms_total=? WHERE id=?",
                      (str(e)[:500], db.now(), int((time.time() - t0) * 1000), meeting_id))
    except Exception as e:  # Background thread: any unexpected error must reach the page, so a meeting never stays stuck in processing
        with db.tx() as c:
            c.execute("UPDATE meetings SET status='failed', error=?, finished_at=?, ms_total=? WHERE id=?",
                      (f"Internal error: {type(e).__name__}: {str(e)[:300]}", db.now(), int((time.time() - t0) * 1000), meeting_id))
        raise
    finally:
        if audio_path and os.path.exists(audio_path):
            os.remove(audio_path)  # Delete the audio immediately after transcription


def _process(meeting_id, provider, audio_path, t0):
    with db.tx() as c:
        m = dict(c.execute("SELECT m.*, l.members_json, l.terms_json, l.is_sample FROM meetings m JOIN ledgers l ON l.id=m.ledger_id WHERE m.id=?", (meeting_id,)).fetchone())
    ledger_id, code, members = m["ledger_id"], m["code"], json.loads(m["members_json"])
    mdate = date.fromisoformat(m["date"])
    if m["is_sample"]:
        provider = ReplayProvider(sample_recordings(), meeting_code=code)
    if audio_path:
        set_stage(meeting_id, "transcribing")
        ts = time.time()
        utts = asr.transcribe(audio_path, "参会人：" + "、".join(members) + "。术语：" + "、".join(json.loads(m["terms_json"])))
        if not utts:
            raise ValueError("No speech was detected in the audio")
        with db.tx() as c:
            store_utterances(c, ledger_id, meeting_id, code, utts)
            c.execute("UPDATE meetings SET ms_transcribe=? WHERE id=?", (int((time.time() - ts) * 1000), meeting_id))
    provider = provider or get_provider()
    if provider is None:
        raise ValueError("The service has no model configured (ANTHROPIC_API_KEY is missing), so only the sample ledger is available for now")
    with db.tx() as c:
        utts = [dict(r) for r in c.execute("SELECT * FROM utterances WHERE ledger_id=? AND meeting_id=? ORDER BY seq", (ledger_id, meeting_id))]
    by_id = {u["id"]: u for u in utts}
    meeting_block = f'<meeting id="{code}" date="{m["date"]}" kind="{m["kind"]}">\n{render_utts(utts)}\n</meeting>'
    members_block = f"<members>{'、'.join(members)}</members>\n"

    # Extract: looks at this meeting only
    set_stage(meeting_id, "extracting")
    ts = time.time()
    sys_x, user_x = prompt(EXTRACT_V), members_block + meeting_block
    raw = call(provider, (ledger_id, meeting_id), "extract", 1, sys_x, user_x, schemas.EXTRACT, EXTRACT_V)
    injections = [i for i in raw.get("suspected_instructions", []) if i.get("utterance_id") in by_id]
    banned = {i["utterance_id"] for i in injections}
    items, rejected = validate_items(raw.get("items", []), by_id, banned, members, mdate)
    retries = 0
    if rejected and not m["is_sample"]:
        retries += 1
        again = call(provider, (ledger_id, meeting_id), "extract", 2, sys_x, user_x + retry_note(rejected), schemas.EXTRACT, EXTRACT_V)
        fixed, rejected = validate_items(again.get("items", []), by_id, banned, members, mdate)
        seen = {verify.norm(i["quote"]) for i in items}
        items += [i for i in fixed if verify.norm(i["quote"]) not in seen]
    ms_x = int((time.time() - ts) * 1000)

    # Reconcile: looks at the whole ledger
    with db.tx() as c:
        open_items = open_ledger_items(c, ledger_id, m["seq"])
        ledger_block = render_ledger(c, open_items)
    props, ms_r, suspicious = [], None, 0
    if open_items:
        set_stage(meeting_id, "reconciling")
        ts = time.time()
        sys_r, user_r = prompt(RECONCILE_V), f"<ledger>\n{ledger_block}\n</ledger>\n{meeting_block}"
        raw = call(provider, (ledger_id, meeting_id), "reconcile", 1, sys_r, user_r, schemas.RECONCILE, RECONCILE_V)
        props, bad = validate_proposals(raw.get("proposals", []), open_items, by_id, banned, mdate)
        if bad and not m["is_sample"]:
            retries += 1
            again = call(provider, (ledger_id, meeting_id), "reconcile", 2, sys_r, user_r + retry_note(bad), schemas.RECONCILE, RECONCILE_V)
            fixed, bad = validate_proposals(again.get("proposals", []), open_items, by_id, banned, mdate)
            got = {(p["ledger_id"]) for p in props}
            props += [p for p in fixed if p["ledger_id"] not in got]
        rejected += bad
        suspicious = int(verify.batch_suspicious(props))
        ms_r = int((time.time() - ts) * 1000)

    # Write to the ledger
    with db.tx() as c:
        now = db.now()
        old_owner = {i["code"]: i["owner_value"] if i["owner_state"] == "given" else None for i in open_items}
        evidence = [(e["utterance_id"], verify.norm(e["quote"]), old_owner.get(p["ledger_id"])) for p in props for e in p["closure_evidence"]]
        for n, it in enumerate(items, 1):
            ow = it["owner"]
            review = "pending" if it["kind"] == "commitment" else "confirmed"
            # If the same sentence was already used to reconcile an earlier item, don't create a duplicate task
            # It must be the same passage of text, not just the same utterance: one transcript segment often contains new tasks
            qn = verify.norm(it["quote"])
            if it["kind"] == "commitment" and any(
                    uid == it["utterance_id"] and (qn in q or q in qn or verify.similarity(qn, q) >= 0.7)
                    # Assigning work to someone new (e.g. "have a teammate write the test cases") is a new task, not progress on the old item
                    and (not ow["value"] or ow["value"] == oo)
                    for uid, q, oo in evidence):
                review = "merged"
            c.execute("""INSERT INTO items(ledger_id,meeting_id,code,kind,strength,title,quote,utterance_id,owner_state,owner_value,owner_basis,due_state,due_raw,due_date,
                ai_owner,ai_due_date,slots_json,review,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                      (ledger_id, meeting_id, f"I-{code}-{n:02d}", it["kind"], it["strength"], (it.get("title") or "").strip()[:80] or None, it["quote"].strip(), it["utterance_id"], ow["state"], ow["value"], ow["basis"],
                       it["due_state"], it["due_raw"], it["due_date"], ow["value"], it["due_date"], json.dumps(it.get("slots", []), ensure_ascii=False), review, now))
        hit, code_to_item = set(), {i["code"]: i for i in open_items}
        for p in props:
            it = code_to_item[p["ledger_id"]]
            hit.add(it["id"])
            flags = ["multiple_items"] if any(k in (p.get("note") or "") for k in ("may match multiple", "可能对应多条")) else []
            c.execute("""INSERT INTO proposals(ledger_id,item_id,meeting_id,transition,evidence_json,new_due_raw,new_due_date,note,flags_json,proposed_by,created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (ledger_id, it["id"], meeting_id, p["transition"], json.dumps(p["closure_evidence"], ensure_ascii=False),
                                                  p["new_due_raw"], p["new_due_date"], p.get("note"), json.dumps(flags), "model", now))
        for it in open_items:
            if it["id"] in hit:
                continue
            pm = verify.possible_mention(it["quote"] or it["title"] or "", utts)
            flags = [{"possible_mention": pm}] if pm else []
            c.execute("""INSERT INTO proposals(ledger_id,item_id,meeting_id,transition,flags_json,decision,proposed_by,created_at)
                VALUES(?,?,?,?,?,?,?,?)""", (ledger_id, it["id"], meeting_id, "not_mentioned", json.dumps(flags, ensure_ascii=False), "auto", "code", now))
        c.execute("""UPDATE meetings SET status='ready', stage=NULL, finished_at=?, ms_extract=?, ms_reconcile=?, ms_total=?, retries=?, rejected_json=?, injections_json=?, suspicious=? WHERE id=?""",
                  (now, ms_x, ms_r, int((time.time() - t0) * 1000), retries, json.dumps(rejected, ensure_ascii=False), json.dumps(injections, ensure_ascii=False), suspicious, meeting_id))
        db.event(c, ledger_id, "meeting_ready", json.dumps({"code": code, "items": len(items), "proposals": len(props), "rejected": len(rejected)}))
