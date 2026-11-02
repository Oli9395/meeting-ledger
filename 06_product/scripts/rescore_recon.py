#!/usr/bin/env python3
"""Map old items from migrated predictions back to gold using the layer 1 score.py mapping (item → gold id), then compute layer 2 scores. Does not call a model."""
import csv
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "..", "05_demo-plan", "eval-kit")
for v in sys.argv[1:]:
    d = os.path.join(ROOT, "eval_runs", v)
    mp = {r["pred_id"]: r["gold_id"] for r in csv.DictReader(open(os.path.join(d, "mapping.csv"), encoding="utf8"))}
    pred = {}
    for x in open(os.path.join(d, "pred.jsonl"), encoding="utf8"):
        p = json.loads(x)
        pred[(p["meeting_id"], p["text_span"])] = mp.get(p["id"]) or None
    rows, un = [], 0
    for x in open(os.path.join(d, "transitions_pred.jsonl"), encoding="utf8"):
        p = json.loads(x)
        gid = pred.get((p["item_meeting"], p["item_quote"]))
        p["from"] = gid or p["from"]
        un += not gid
        rows.append(p)
    out = os.path.join(d, "transitions_pred_mapped.jsonl")
    with open(out, "w", encoding="utf8") as f:
        f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    subprocess.run([sys.executable, "-I", "score_recon.py", "--pred", out, "--json", os.path.join(d, "recon_metrics.json")], cwd=KIT, capture_output=True)
    r = json.load(open(os.path.join(d, "recon_metrics.json")))
    print(v, "predictions", len(rows), "unmatched gold items", un)
    for s in ("all", "dev", "test"):
        print("  ", s, {k: f"{r[s][k].get('num')}/{r[s][k].get('den')}" for k in ("fgr_mentioned", "fgr_unmentioned", "transition_accuracy", "mention_recall", "unmentioned_recall")})
