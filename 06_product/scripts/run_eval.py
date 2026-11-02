#!/usr/bin/env python3
"""Run the 5 evaluation meetings in order through the real pipeline with a real model, then hand the results to eval-kit for scoring.

  python scripts/run_eval.py --name v1 [--extract-prompt extract_v1] [--reconcile-prompt reconcile_v1] [--record]

Chaining rule: after each meeting, confirm all drafts and all transition proposals, simulating a user who trusts the system.
Gold ids in pred are mapped mechanically by character similarity, with no manual step.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "..", "05_demo-plan", "eval-kit")
sys.path.insert(0, ROOT)
ap = argparse.ArgumentParser()
ap.add_argument("--name", required=True)
ap.add_argument("--extract-prompt", default="extract_v1")
ap.add_argument("--reconcile-prompt", default="reconcile_v1")
ap.add_argument("--meetings", default="M1,M2,M3,M4,M5")
args = ap.parse_args()
OUT = os.path.join(ROOT, "eval_runs", args.name)
os.makedirs(OUT, exist_ok=True)
os.environ["BP_DB"] = os.path.join(tempfile.mkdtemp(), "eval.db")
os.environ["BP_EXTRACT_PROMPT"] = args.extract_prompt
os.environ["BP_RECONCILE_PROMPT"] = args.reconcile_prompt

from app import db, llm, main, parse, pipeline, verify  # noqa: E402

DATES = {"M1": ("2026-10-06", "one_on_one"), "M2": ("2026-10-08", "group"), "M3": ("2026-10-15", "group"), "M4": ("2026-10-22", "group"), "M5": ("2026-10-26", "partner")}
MEMBERS = ["周岚", "陈思远", "王博", "李沐晴", "Daniel Ong", "Priya Nair", "Marcus Tan"]
GOLD = {m: [json.loads(x) for x in open(os.path.join(KIT, "gold", f"{m}.gold.jsonl"), encoding="utf8") if x.strip() and not x.startswith("#")] for m in DATES}
GOLD = {m: [g for g in rows if not g.get("_meta") and g.get("id")] for m, rows in GOLD.items()}


class Recording:
    def __init__(self, inner):
        self.inner, self.name, self.meeting, self.rec = inner, inner.name, None, {}

    def complete(self, step, system, user, schema):
        r = self.inner.complete(step, system, user, schema)
        self.rec.setdefault(f"{step}:{self.meeting}", r.data)
        print(f"   {step} {r.ms / 1000:.0f}s in={r.input_tokens} out={r.output_tokens} ${r.cost_usd}", flush=True)
        return r


def map_gold(quote, meeting):
    best, top = None, 0
    for g in GOLD[meeting]:
        s = max(verify.similarity(quote, g["text_span"]), verify.similarity(g["text_span"], quote))
        if s > top:
            best, top = g, s
    return best["id"] if best and top >= 0.5 else None


prov = Recording(llm.get_provider())
db.init()
with db.tx() as c:
    lid = c.execute("INSERT INTO ledgers(token,name,members_json,tag,created_at) VALUES('eval','eval',?,?,?)", (json.dumps(MEMBERS, ensure_ascii=False), "eval", db.now())).lastrowid
preds, tpreds, times, seq = [], [], {}, 0
for code in args.meetings.split(","):
    seq += 1
    d, kind = DATES[code]
    text = open(os.path.join(KIT, "meetings", "plain", f"{code}.txt"), encoding="utf8").read()
    with db.tx() as c:
        mid = c.execute("INSERT INTO meetings(ledger_id,seq,code,date,kind,source,status,created_at) VALUES(?,?,?,?,?,'text','processing',?)", (lid, seq, code, d, kind, db.now())).lastrowid
        pipeline.store_utterances(c, lid, mid, code, parse.parse_text(text))
    print(code, flush=True)
    prov.meeting = code
    pipeline.process(mid, prov)
    with db.tx() as c:
        m = dict(c.execute("SELECT * FROM meetings WHERE id=?", (mid,)).fetchone())
        if m["status"] != "ready":
            sys.exit(f"{code} failed: {m['error']}")
        times[code] = m["ms_total"]
        utt = {u["id"]: dict(u) for u in c.execute("SELECT * FROM utterances WHERE meeting_id=?", (mid,))}
        for n, i in enumerate(c.execute("SELECT * FROM items WHERE meeting_id=?", (mid,)).fetchall(), 1):
            t = {"commitment": "action", "decision": "decision", "result": "result", "question": "question"}[i["kind"]]
            preds.append({"id": f"P{code}{n:02d}", "meeting_id": code, "text_span": i["quote"], "owner": i["owner_value"] if i["owner_state"] == "given" else None,
                          "due": i["due_date"], "due_raw": i["due_raw"], "strength": i["strength"], "type": t, "evidence_timestamp": utt[i["utterance_id"]]["ts"],
                          "cross_meeting_ref": None, "status": None, "source_section": i["kind"]})
        for p in c.execute("SELECT p.*, i.quote iq, i.code ic, im.code im FROM proposals p JOIN items i ON i.id=p.item_id JOIN meetings im ON im.id=i.meeting_id WHERE p.meeting_id=? AND p.proposed_by='model'", (mid,)).fetchall():
            ev = json.loads(p["evidence_json"])
            gid = map_gold(p["iq"], p["im"])
            tpreds.append({"kind": "transition", "from": gid or f"UNMAPPED:{p['ic']}", "at_meeting": code, "transition": p["transition"], "flags": [],
                           "item_quote": p["iq"], "item_meeting": p["im"], "closing_quotes": [{"quote": e["quote"], "meeting_id": code} for e in ev], "note": p["note"]})
            # Write cross-meeting links back onto this meeting's new items, for the layer 1 crosslink metric
            for pr in preds:
                if pr["meeting_id"] == code and gid and any(verify.similarity(e["quote"], pr["text_span"]) >= 0.5 for e in ev) and not pr["cross_meeting_ref"]:
                    pr["cross_meeting_ref"] = gid
        # Simulate a user who trusts the system
        c.execute("UPDATE items SET review='confirmed' WHERE meeting_id=? AND review='pending'", (mid,))
        for p in c.execute("SELECT * FROM proposals WHERE meeting_id=? AND decision='pending'", (mid,)).fetchall():
            main.apply_decision(c, dict(p), "confirmed")
        print(f"  items={sum(x['meeting_id'] == code for x in preds)} rejected={len(json.loads(m['rejected_json']))} retries={m['retries']} total={m['ms_total'] / 1000:.0f}s", flush=True)

with open(os.path.join(OUT, "pred.jsonl"), "w", encoding="utf8") as f:
    f.writelines(json.dumps(p, ensure_ascii=False) + "\n" for p in preds)
with open(os.path.join(OUT, "transitions_pred.jsonl"), "w", encoding="utf8") as f:
    f.writelines(json.dumps(p, ensure_ascii=False) + "\n" for p in tpreds)
tdir = os.path.join(OUT, "text")
os.makedirs(tdir, exist_ok=True)
for code in args.meetings.split(","):
    open(os.path.join(tdir, f"{code}.txt"), "w", encoding="utf8").write(open(os.path.join(KIT, "meetings", "plain", f"{code}.txt"), encoding="utf8").read())
with open(os.path.join(OUT, "run_info.json"), "w", encoding="utf8") as f:
    json.dump({"extract_prompt": args.extract_prompt, "reconcile_prompt": args.reconcile_prompt, "model": llm.MODEL, "effort": llm.EFFORT, "provider": prov.name, "ms_total": times}, f, ensure_ascii=False, indent=1)
py = sys.executable
subprocess.run([py, "-I", "score.py", "--pred", os.path.join(OUT, "pred.jsonl"), "--emit-mapping", os.path.join(OUT, "mapping.csv")], cwd=KIT)
subprocess.run([py, "-I", "score.py", "--pred", os.path.join(OUT, "pred.jsonl"), "--map", os.path.join(OUT, "mapping.csv"), "--pred-text-dir", tdir, "--json", os.path.join(OUT, "metrics.json")], cwd=KIT)
subprocess.run([py, "-I", "score_recon.py", "--pred", os.path.join(OUT, "transitions_pred.jsonl"), "--json", os.path.join(OUT, "recon_metrics.json")], cwd=KIT)
