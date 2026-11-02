#!/usr/bin/env python3
"""Summarize persona tests: in-product metrics come from the database; scoring comes from expectations each persona wrote in advance."""
import glob
import json
import os
import sqlite3
from statistics import median

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = sqlite3.connect(os.path.join(ROOT, "data", "persona.db"))
db.row_factory = sqlite3.Row
OUT = {}


def per_round(tag, r1_counts=None):
    res = {}
    ledgers = [dict(r) for r in db.execute("SELECT * FROM ledgers WHERE tag=? AND name LIKE 'p%'", (tag,))]
    rows = {"all": [], "same": [], "new": []}
    for l in ledgers:
        pid = l["name"].split()[0]
        ms = [dict(m) for m in db.execute("SELECT * FROM meetings WHERE ledger_id=? AND status='ready' ORDER BY seq", (l["id"],))]
        n_same = (r1_counts or {}).get(pid, len(ms))
        for m in ms:
            items = [dict(i) for i in db.execute("SELECT * FROM items WHERE meeting_id=? AND kind='commitment' AND manual=0", (m["id"],))]
            props = [dict(p) for p in db.execute("SELECT * FROM proposals WHERE meeting_id=? AND proposed_by='model'", (m["id"],))]
            group = "same" if m["seq"] <= n_same else "new"
            for key in ("all", group):
                rows[key].append((m, items, props))
    for key, val in rows.items():
        drafts = [i for _, its, _ in val for i in its if i["review"] != "merged"]
        dec = [i for i in drafts if i["review"] != "pending"]
        ok = [i for i in dec if i["review"] == "confirmed"]
        noedit = [i for i in ok if not i["edited"]]
        props = [p for _, _, ps in val for p in ps if p["decision"] in ("confirmed", "dismissed")]
        res[key] = {"meetings": len(val), "drafts_decided": len(dec), "confirmed": len(ok), "rejected": len(dec) - len(ok), "accepted_no_edit": len(noedit),
                    "accepted_no_edit_pct": round(100 * len(noedit) / len(dec), 1) if dec else None,
                    "edited": sum(1 for i in ok if i["edited"]), "no_owner_ai": sum(1 for i in drafts if i["ai_owner"] is None),
                    "proposals_decided": len(props), "proposals_confirmed": sum(p["decision"] == "confirmed" for p in props),
                    "median_pipeline_s": round(median([m["ms_total"] for m, _, _ in val if m["ms_total"]]) / 1000, 1) if val else None}
    return res


def personas(rnd):
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "persona_tests", rnd, "*", "result.json"))):
        r = json.load(open(f, encoding="utf8"))
        out[r["persona"]] = r
    return out


p1, p2 = personas("r1"), personas("r2")
r1_counts = {}
for l in db.execute("SELECT name,id FROM ledgers WHERE tag='r1' AND name LIKE 'p%'"):
    r1_counts[l["name"].split()[0]] = db.execute("SELECT COUNT(*) FROM meetings WHERE ledger_id=? AND status='ready'", (l["id"],)).fetchone()[0]
OUT["r1_db"] = per_round("r1")
OUT["r2_db"] = per_round("r2", r1_counts)


def s(d, k):
    return sum((x.get(k) or 0) if not isinstance(x.get(k), list) else len(x[k]) for x in d.values())


for name, d in (("r1", p1), ("r2", p2)):
    OUT[name + "_persona"] = {k: s(d, k) for k in ("expected_tasks", "found_correct", "false_tasks", "owner_wrong", "due_wrong", "edited", "transitions_expected", "transitions_correct")}
    OUT[name + "_persona"]["completed"] = sum(bool(x.get("completed_flow")) for x in d.values())
    OUT[name + "_persona"]["sean_ellis"] = {v: sum(x.get("sean_ellis") == v for x in d.values()) for v in ("very", "somewhat", "not")}
OUT["r2_new_meeting"] = {k: sum((x.get("new_meeting") or {}).get(k) or 0 for x in p2.values()) for k in ("expected_tasks", "found_correct", "false_tasks", "owner_wrong", "due_wrong", "transitions_expected", "transitions_correct")}
OUT["per_persona"] = {k: {"r1": {f: p1[k].get(f) if not isinstance(p1[k].get(f), list) else len(p1[k][f]) for f in ("expected_tasks", "found_correct", "false_tasks", "owner_wrong", "due_wrong", "edited", "transitions_correct", "transitions_expected", "sean_ellis")},
                          "r2": {f: p2[k].get(f) if not isinstance(p2[k].get(f), list) else len(p2[k][f]) for f in ("expected_tasks", "found_correct", "false_tasks", "owner_wrong", "due_wrong", "edited", "transitions_correct", "transitions_expected", "sean_ellis")},
                          "new": p2[k].get("new_meeting")} for k in p1 if k in p2}
OUT["security"] = {k: p2["p7_skeptic"].get(k) for k in ("injection_executed", "xss_triggered", "false_fulfilled")}
json.dump(OUT, open(os.path.join(ROOT, "persona_tests", "summary.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in OUT.items() if k != "per_persona"}, ensure_ascii=False, indent=0))
for k, v in OUT["per_persona"].items():
    print(k, v["r1"], "\n   ", v["r2"], "\n   new", v["new"])
