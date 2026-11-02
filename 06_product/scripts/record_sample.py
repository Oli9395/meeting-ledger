#!/usr/bin/env python3
"""Run the live pipeline on samples/M1-M3 and save raw model output as replay data for the sample ledger.

  BP_PROVIDER=claude_cli python scripts/record_sample.py   # or set ANTHROPIC_API_KEY
"""
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ["BP_DB"] = os.path.join(tempfile.mkdtemp(), "record.db")

from app import db, llm, main, parse, pipeline  # noqa: E402


class Recording:
    def __init__(self, inner):
        self.inner, self.name, self.meeting, self.rec = inner, inner.name, None, {}

    def complete(self, step, system, user, schema):
        r = self.inner.complete(step, system, user, schema)
        self.rec.setdefault(f"{step}:{self.meeting}", r.data)
        print(f"  {step} {r.ms / 1000:.0f}s", flush=True)
        return r


prov = Recording(llm.get_provider())
db.init()
with db.tx() as c:
    lid = c.execute("INSERT INTO ledgers(token,name,members_json,tag,created_at) VALUES('rec','rec',?,?,?)",
                    (json.dumps(main.SAMPLE_MEMBERS, ensure_ascii=False), "record", db.now())).lastrowid
for n, (code, d, title, kind) in enumerate(main.SAMPLE, 1):
    with open(os.path.join(ROOT, "samples", f"{code}.txt"), encoding="utf8") as f:
        text = f.read()
    with db.tx() as c:
        mid = c.execute("INSERT INTO meetings(ledger_id,seq,code,date,title,kind,source,status,created_at) VALUES(?,?,?,?,?,?,'text','processing',?)",
                        (lid, n, code, d, title, kind, db.now())).lastrowid
        pipeline.store_utterances(c, lid, mid, code, parse.parse_text(text))
    print(code, flush=True)
    prov.meeting = code
    pipeline.process(mid, prov)
    with db.tx() as c:
        m = dict(c.execute("SELECT * FROM meetings WHERE id=?", (mid,)).fetchone())
        if m["status"] != "ready":
            sys.exit(f"{code} failed: {m['error']}")
        print(f"  items={c.execute('SELECT COUNT(*) FROM items WHERE meeting_id=?', (mid,)).fetchone()[0]} rejected={len(json.loads(m['rejected_json']))} retries={m['retries']}")
        c.execute("UPDATE items SET review='confirmed' WHERE meeting_id=? AND review='pending'", (mid,))
        for p in c.execute("SELECT * FROM proposals WHERE meeting_id=? AND decision='pending'", (mid,)).fetchall():
            main.apply_decision(c, dict(p), "confirmed")
with open(os.path.join(ROOT, "samples", "recordings.json"), "w", encoding="utf8") as f:
    json.dump(prov.rec, f, ensure_ascii=False)
print("saved", sorted(prov.rec))
