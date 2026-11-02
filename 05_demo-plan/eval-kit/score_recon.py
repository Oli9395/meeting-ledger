#!/usr/bin/env python3
# ---
# title: BriefPilot eval-kit layer 2 scoring script: cross-meeting reconciliation (4 transition types, false-green rate, quote verbatim rate, not mentioned, second-beat checks)
# status: v1 (selftest A–F pass; gold is still a model-drafted draft, see _meta in gold/recon/transitions.gold.jsonl)
# ---
"""score_recon.py -- standard library only. score.py (layer 1) is left unchanged; this script only reuses its utility functions.

Usage (from the eval-kit directory):
  python3 -I score_recon.py --selftest
  # Score (`from` in pred can be a gold id directly, or your own id mapped with --map)
  python3 -I score_recon.py --pred results/x/transitions_pred.jsonl [--map results/x/recon_mapping.csv] \
      [--with-runs] --json results/x/recon_metrics.json
  # Convert DIY (expert prompt) JSON output into pred and suggest a mapping for human review
  python3 -I score_recon.py --from-diy results/diy_expert/raw --emit-pred results/diy_expert/transitions_pred.jsonl \
      --emit-mapping results/diy_expert/recon_mapping.csv
  # E2c: apply the same verbatim filter as this system to DIY output
  python3 -I score_recon.py --verbatim-filter results/diy_expert/transitions_pred.jsonl results/diy_expert_c/transitions_pred.jsonl
  # Paired comparison (McNemar exact test + pre-registered win margin k)
  python3 -I score_recon.py --compare A.jsonl B.jsonl --k 4 [--map-a a.csv --map-b b.csv] [--with-runs]
  # Inter-annotator agreement (transition type), bootstrap 95% CI
  python3 -I score_recon.py --blank > blank_transitions.jsonl
  python3 -I score_recon.py --kappa annotatorA.jsonl annotatorB.jsonl

Canonical names (matching the canonical name table in 04_prd/01_PRD_v2.md §13.4; aliases are normalized on read):
  fulfilled | partial_or_rescheduled | abandoned | not_mentioned
"""
import argparse
import csv
import glob
import importlib.util
import json
import math
import os
import random
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True  # Do not leave __pycache__ in eval-kit
_spec = importlib.util.spec_from_file_location("score", os.path.join(HERE, "score.py"))
score = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(score)

GOLD_PATH = os.path.join(HERE, "gold", "recon", "transitions.gold.jsonl")
CANON = ["fulfilled", "partial_or_rescheduled", "abandoned", "not_mentioned"]
ALIASES = {
    "fulfilled": "fulfilled", "done": "fulfilled", "kept": "fulfilled", "兑现": "fulfilled", "已兑现": "fulfilled",
    "partial_or_rescheduled": "partial_or_rescheduled", "partial": "partial_or_rescheduled",
    "rescheduled": "partial_or_rescheduled", "in_progress": "partial_or_rescheduled", "部分或改期": "partial_or_rescheduled",
    "部分": "partial_or_rescheduled", "改期": "partial_or_rescheduled",
    "abandoned": "abandoned", "dropped": "abandoned", "放弃": "abandoned",
    "not_mentioned": "not_mentioned", "unmentioned": "not_mentioned", "无人提及": "not_mentioned", "未提及": "not_mentioned",
}
FLAG_ALIASES = {"condition_mismatch": "condition_mismatch", "fulfilled_condition_mismatch": "condition_mismatch",
                "条件不符": "condition_mismatch", "run_evidence_not_found": "run_evidence_not_found"}
DEV, TEST = ("M2", "M3"), ("M4", "M5")
LINE = re.compile(r"^\[(\d\d:\d\d:\d\d)\] (.+?)：(.*)$")
MATCH_THRESHOLD = 0.35


def canon(label):
    if label is None:
        return None
    k = unicodedata.normalize("NFKC", str(label)).strip().casefold()
    if k not in ALIASES:
        sys.exit(f"[error] Unknown transition label: {label!r} (canonical names: {CANON})")
    return ALIASES[k]


def canon_flags(flags):
    return sorted({FLAG_ALIASES.get(str(f).strip().casefold(), str(f)) for f in (flags or [])})


def load_gold(path=GOLD_PATH):
    rows = score.read_jsonl(path)
    return [r for r in rows if not r.get("_meta")]


def thread_index(gold):
    idx = {}
    for r in gold:
        if r["kind"] == "transition":
            for m in r["members"]:
                idx[m] = r["thread"]
    return idx


# ----------------------------------------------------------------- Verbatim check (same rule as product F04)
def vnorm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s or "")).strip()


_UTT = {}


def utterances(mid):
    if mid not in _UTT:
        path = os.path.join(HERE, "meetings", "plain", f"{mid}.txt")
        _UTT[mid] = [vnorm(m.group(3)) for m in (LINE.match(l.rstrip("\n")) for l in open(path, encoding="utf-8")) if m] \
            if os.path.exists(path) else []
    return _UTT[mid]


def is_verbatim(quote, mid=None):
    q = vnorm(quote)
    if not q:
        return False
    mids = [mid] if mid else ["M1", "M2", "M3", "M4", "M5"]
    return any(q in u for m in mids for u in utterances(m))


# ----------------------------------------------------------------- Read pred
def load_map(path):
    if not path:
        return {}
    out = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("gold_id"):
                out[row["pred_from"] if "pred_from" in row else row["pred_id"]] = row["gold_id"].strip()
    return out


def load_pred(path, mapping, tindex):
    preds = []
    for p in score.read_jsonl(path):
        kind = p.get("kind", "transition")
        if kind == "transition":
            src = p.get("from")
            gid = mapping.get(src, src)
            p = dict(p, kind=kind, transition=canon(p.get("transition")), flags=canon_flags(p.get("flags")),
                     gold_from=gid, thread=tindex.get(gid))
        preds.append(p)
    return preds


def index_preds(preds):
    """(thread, at_meeting) -> pred. When a key has several rows, keep the "greenest" one (fulfilled > partial > abandoned > not mentioned),
    so duplicate output cannot lead to underestimating the false-green rate."""
    rank = {"fulfilled": 0, "partial_or_rescheduled": 1, "abandoned": 2, "not_mentioned": 3}
    idx, extra = {}, []
    for p in preds:
        if p["kind"] != "transition":
            continue
        if p["thread"] is None:
            extra.append(p)
            continue
        k = (p["thread"], p["at_meeting"])
        if k not in idx or rank[p["transition"]] < rank[idx[k]["transition"]]:
            idx[k] = p
    return idx, extra


# ----------------------------------------------------------------- Scoring
def wilson_pair(num, den):
    return score.wilson(num, den)


def scored_rows(gold, with_runs):
    rows = [r for r in gold if r["kind"] == "transition" and r.get("label_status") != "needs_adjudication"
            and r.get("transition")]
    return rows


def row_outcome(g, p, with_runs):
    """Return (pred_label, correct, false_green, flags_ok). No prediction = implicit not_mentioned."""
    pl = p["transition"] if p else "not_mentioned"
    pf = p["flags"] if p else []
    gl = g["transition"]
    need_flag = with_runs and "condition_mismatch" in g.get("flags", [])
    if need_flag:
        correct = pl == gl and "condition_mismatch" in pf
        fg = pl == "fulfilled" and "condition_mismatch" not in pf
    else:
        correct = pl == gl
        fg = pl == "fulfilled" and gl != "fulfilled"
    return pl, correct, fg


def metrics(gold, preds, with_runs=False, split=None):
    idx, extra = index_preds(preds)
    rows = scored_rows(gold, with_runs)
    if split:
        rows = [r for r in rows if r["at_meeting"] in split]
    M = {}

    def put(key, label, num, den):
        M[key] = {"label": label, "num": num, "den": den, "value": (num / den if den else None)}

    mentioned = [r for r in rows if r["transition"] != "not_mentioned"]
    unm = [r for r in rows if r["transition"] == "not_mentioned"]
    out = {r["id"]: row_outcome(r, idx.get((r["thread"], r["at_meeting"])), with_runs) for r in rows}
    # False-green rate is split in two (first line of the report = fgr_mentioned)
    fgr_m_den = [r for r in mentioned if r["transition"] in ("partial_or_rescheduled", "abandoned")
                 or (with_runs and "condition_mismatch" in r.get("flags", []))]
    put("fgr_mentioned", "False-green rate: mentioned but not cleanly fulfilled (partial/abandoned/condition mismatch)",
        sum(out[r["id"]][2] for r in fgr_m_den), len(fgr_m_den))
    put("fgr_unmentioned", "False-green rate: not mentioned but judged fulfilled", sum(out[r["id"]][2] for r in unm), len(unm))
    put("transition_accuracy", "Transition type accuracy (mentioned rows)", sum(out[r["id"]][1] for r in mentioned), len(mentioned))
    put("transition_accuracy_all", "Transition type accuracy (all scorable rows, including not mentioned)", sum(out[r["id"]][1] for r in rows), len(rows))
    put("mention_recall", "Cross-meeting mention recall (mentioned rows with a prediction other than 'not mentioned')",
        sum(out[r["id"]][0] != "not_mentioned" for r in mentioned), len(mentioned))
    put("unmentioned_recall", "Not-mentioned recall", sum(out[r["id"]][0] == "not_mentioned" for r in unm), len(unm))
    pred_unm = [r for r in rows if out[r["id"]][0] == "not_mentioned"]
    put("unmentioned_precision", "Not-mentioned precision (rows predicted as not mentioned that are also not mentioned in gold)",
        sum(r["transition"] == "not_mentioned" for r in pred_unm), len(pred_unm))
    # Quote verbatim rate: only considers quotes written out in pred
    qs = []
    for p in preds:
        if p["kind"] != "transition" or (split and p.get("at_meeting") not in split):
            continue
        for q in p.get("closing_quotes") or []:
            qs.append(is_verbatim(q.get("quote"), q.get("meeting_id") or p.get("at_meeting")))
        if p.get("item_quote"):
            qs.append(is_verbatim(p["item_quote"], p.get("item_meeting")))
    put("quote_verbatim_rate", "Quote verbatim rate (DIY rewrite rate = 1 − this value)", sum(qs), len(qs))
    put("extra_predictions", "Predictions that match no tracked thread (count)", len([e for e in extra
        if not split or e.get("at_meeting") in split]), 0)
    # Second-beat checks
    if not split or "M5" in split:
        stale = [r for r in gold if r["kind"] == "stale_number"]
        hit = sum(1 for r in stale if any(p.get("kind") == "stale_number" and
                                          (p.get("result") == r["result_gold"] or p.get("cited_at") == r["cited_at"])
                                          for p in preds))
        put("stale_number_recall", "Stale-number check recall (n is very small, report counts only)", hit, len(stale))
    if with_runs and (not split or "M4" in split):
        ck = [r for r in gold if r["kind"] == "constraint_check"]
        got = {p.get("run_group"): p.get("result") for p in preds if p.get("kind") == "constraint_check"}
        mis = [r for r in ck if r["expected"] == "condition_mismatch"]
        put("constraint_flag_recall", "Decision constraint violation recall (synthetic planted cases)",
            sum(got.get(r["run_group"]) == "condition_mismatch" for r in mis), len(mis))
        ok = [r for r in ck if r["expected"] != "condition_mismatch"]
        put("constraint_false_alarms", "False alarms in the compliant control group (count)", sum(got.get(r["run_group"]) == "condition_mismatch" for r in ok), 0)
    return M, out


ORDER = ["fgr_mentioned", "fgr_unmentioned", "transition_accuracy", "transition_accuracy_all", "mention_recall",
         "unmentioned_recall", "unmentioned_precision", "quote_verbatim_rate", "extra_predictions",
         "stale_number_recall", "constraint_flag_recall", "constraint_false_alarms"]
COUNT_ONLY = {"extra_predictions", "constraint_false_alarms"}


def report(gold, preds, with_runs):
    lines = []
    for name, sp in (("Full set", None), ("Dev set M2–M3", DEV), ("Test set M4–M5", TEST)):
        M, _ = metrics(gold, preds, with_runs, sp)
        lines += [f"### {name}", "", "| Metric | key | Value | Numerator/denominator | 95% CI (Wilson) |", "|---|---|---|---|---|"]
        for k in ORDER:
            if k in M:
                m = M[k]
                if k in COUNT_ONLY:
                    lines.append(f"| {m['label']} | {k} | {m['num']} rows | - | - |")
                else:
                    lines.append(f"| {m['label']} | {k} | {score.fmt(m['value'])} | {m['num']}/{m['den']} | "
                                 f"{wilson_pair(m['num'], m['den'])} |")
        lines.append("")
    adj = [r["id"] for r in gold if r.get("label_status") == "needs_adjudication"]
    lines.append(f"Not scored (needs_adjudication, awaiting human adjudication): {len(adj)} rows {adj}")
    lines.append(f"Run table condition: {'imported (--with-runs)' if with_runs else 'not imported: condition_mismatch is scored from spoken transitions only'}")
    return "\n".join(lines)


# ----------------------------------------------------------------- Paired comparison
def binom_two_sided(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def compare(gold, pa, pb, k, with_runs, split=None):
    _, oa = metrics(gold, pa, with_runs, split)
    _, ob = metrics(gold, pb, with_runs, split)
    ids = sorted(oa)
    b = [i for i in ids if oa[i][1] and not ob[i][1]]
    c = [i for i in ids if ob[i][1] and not oa[i][1]]
    fga = sum(oa[i][2] for i in ids)
    fgb = sum(ob[i][2] for i in ids)
    p = binom_two_sided(len(b), len(c))
    verdict = "A 胜（b − c ≥ k）" if len(b) - len(c) >= k else ("B 胜（c − b ≥ k）" if len(c) - len(b) >= k else "未分胜负")
    return {"n_rows": len(ids), "b_A_right_B_wrong": len(b), "c_B_right_A_wrong": len(c), "mcnemar_exact_p": p,
            "k": k, "verdict": verdict, "false_green_A": fga, "false_green_B": fgb, "b_ids": b, "c_ids": c}


# ----------------------------------------------------------------- Kappa (transition type) + bootstrap
def kappa_boot(xs, ys, n_boot=2000, seed=20261101):
    k, po = score.cohen_kappa(xs, ys)
    rng = random.Random(seed)
    n = len(xs)
    ks = []
    for _ in range(n_boot):
        ids = [rng.randrange(n) for _ in range(n)]
        kb, _ = score.cohen_kappa([xs[i] for i in ids], [ys[i] for i in ids])
        if kb is not None:
            ks.append(kb)
    ks.sort()
    lo = ks[int(0.025 * len(ks))] if ks else None
    hi = ks[min(len(ks) - 1, int(0.975 * len(ks)))] if ks else None
    return k, po, lo, hi


def kappa_cmd(pa, pb):
    A = {r["id"]: r for r in score.read_jsonl(pa) if not r.get("_meta")}
    B = {r["id"]: r for r in score.read_jsonl(pb) if not r.get("_meta")}
    ids = sorted(i for i in set(A) & set(B) if A[i].get("transition") and B[i].get("transition"))
    xs = [canon(A[i]["transition"]) for i in ids]
    ys = [canon(B[i]["transition"]) for i in ids]
    k, po, lo, hi = kappa_boot(xs, ys)
    passed = k is not None and k >= 0.6 and lo is not None and lo >= 0.4
    print(f"Rows labeled by both annotators: {len(ids)} (including {sum(1 for x in xs if x == 'not_mentioned')} sampled not-mentioned rows)")
    print("| Field | Cohen's κ | bootstrap 95% CI | Observed agreement | n | Pass (point estimate ≥0.6 and lower bound ≥0.4) |")
    print("|---|---|---|---|---|---|")
    f = (lambda v: "N/A" if v is None else f"{v:.3f}")
    print(f"| transition | {f(k)} | {f(lo)}–{f(hi)} | {f(po)} | {len(ids)} | {'yes' if passed else 'no'} |")
    # Merged 3-class version
    m3 = {"fulfilled": "fulfilled", "partial_or_rescheduled": "not_fulfilled", "abandoned": "not_fulfilled",
          "not_mentioned": "not_mentioned"}
    k3, po3, lo3, hi3 = kappa_boot([m3[x] for x in xs], [m3[y] for y in ys])
    print(f"| transition_3c | {f(k3)} | {f(lo3)}–{f(hi3)} | {f(po3)} | {len(ids)} | - |")
    return {"kappa": k, "po": po, "ci": [lo, hi], "n": len(ids), "pass": passed, "kappa_3c": k3}


def blank_cmd():
    for r in load_gold():
        if r["kind"] != "transition":
            continue
        keep = {k: r[k] for k in ("id", "thread", "at_meeting", "item_meeting", "item_text", "item_owner")}
        keep.update({"transition": None, "closure_gold": [], "notes": ""})
        print(json.dumps(keep, ensure_ascii=False))


# ----------------------------------------------------------------- DIY output → pred
def from_diy(raw_dir, out_pred, out_map):
    """Each file Mk.json under raw_dir = DIY JSON output with Mk as the "current meeting" (format in templates/expert_reconcile_prompt.md)."""
    gold_items = {}
    for p in sorted(glob.glob(os.path.join(HERE, "gold", "M*.gold.jsonl"))):
        for g in score.read_jsonl(p):
            gold_items[g["id"]] = g
    preds, maprows = [], []
    for path in sorted(glob.glob(os.path.join(raw_dir, "M*.json"))):
        mk = os.path.basename(path).split(".")[0].split("_")[0]
        data = score.read_json(path)
        items = data.get("reconciliation", data) if isinstance(data, dict) else data
        for n, it in enumerate(items, 1):
            pid = f"DIY-{mk}-{n:03d}"
            im = it.get("item_meeting")
            cands = [g for g in gold_items.values() if (not im or g["meeting_id"] == im)]
            best = max(((score.similarity(it.get("item_quote", ""), g["text_span"]), g["id"]) for g in cands),
                       default=(0.0, None))
            maprows.append([pid, best[1] if best[0] >= MATCH_THRESHOLD else "",
                            f"auto {best[0]:.2f}" + (" (needs human review)" if best[0] < MATCH_THRESHOLD + 0.15 else "")])
            cq = it.get("closing_quote")
            preds.append({"id": pid, "kind": "transition", "from": pid, "at_meeting": mk,
                          "transition": it.get("status"), "item_quote": it.get("item_quote"), "item_meeting": im,
                          "closing_quotes": [{"quote": cq, "meeting_id": mk}] if cq else [],
                          "flags": it.get("flags", [])})
        issues = data.get("constraint_issues", []) if isinstance(data, dict) else []
        for n, s in enumerate(issues, 1):
            kind = "stale_number" if s.get("kind") == "stale_number" else "constraint_issue"
            cands = [g for g in gold_items.values() if g["meeting_id"] == mk]
            best = max(((score.similarity(s.get("issue_quote", ""), g["text_span"]), g["id"]) for g in cands),
                       default=(0.0, None))
            preds.append({"id": f"DIY-{mk}-S{n:02d}", "kind": kind, "at_meeting": mk,
                          "cited_at": best[1] if best[0] >= MATCH_THRESHOLD else None,
                          "quote": s.get("issue_quote"), "decision_quote": s.get("decision_quote")})
    os.makedirs(os.path.dirname(os.path.abspath(out_pred)), exist_ok=True)
    with open(out_pred, "w", encoding="utf-8") as f:
        for p in preds:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    with open(out_map, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pred_id", "gold_id", "note"])
        w.writerows(maprows)
    print(f"Wrote {out_pred} ({len(preds)} rows) and {out_map} (review gold_id line by line, then pass it back with --map)")


def verbatim_filter(src, dst):
    kept, dropped = [], 0
    for p in score.read_jsonl(src):
        if p.get("kind", "transition") == "transition":
            qs = [(q.get("quote"), q.get("meeting_id") or p.get("at_meeting")) for q in p.get("closing_quotes") or []]
            if p.get("item_quote"):
                qs.append((p["item_quote"], p.get("item_meeting")))
            if any(not is_verbatim(q, m) for q, m in qs):
                dropped += 1
                continue
        kept.append(p)
    os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        for p in kept:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"Verbatim filter: kept {len(kept)} rows, dropped {dropped} rows (same normalization as product F04: NFKC + whitespace folding) → {dst}")


# ----------------------------------------------------------------- Selftest
def gold_as_pred(gold, with_flags=True):
    out = []
    for r in gold:
        if r["kind"] == "transition" and r.get("transition") and r.get("label_status") != "needs_adjudication":
            quotes = []
            out.append({"id": "P-" + r["id"], "kind": "transition", "from": r["thread"], "at_meeting": r["at_meeting"],
                        "transition": r["transition"], "closing_quotes": quotes,
                        "flags": r.get("flags", []) if with_flags else []})
        elif r["kind"] == "stale_number":
            out.append({"id": "P-" + r["id"], "kind": "stale_number", "result": r["result_gold"], "cited_at": r["cited_at"]})
        elif r["kind"] == "constraint_check":
            out.append({"id": "P-" + r["id"], "kind": "constraint_check", "run_group": r["run_group"], "result": r["expected"]})
    return out


def selftest():
    gold = load_gold()
    ti = thread_index(gold)
    ok = True

    def prep(rows):
        return [dict(p, transition=canon(p.get("transition")), flags=canon_flags(p.get("flags")),
                     gold_from=p.get("from"), thread=ti.get(p.get("from"))) if p["kind"] == "transition" else p
                for p in rows]

    # A) gold vs. gold
    GA = prep(gold_as_pred(gold))
    M, _ = metrics(gold, GA, with_runs=True)
    for k in ("transition_accuracy", "transition_accuracy_all", "mention_recall", "unmentioned_recall",
              "unmentioned_precision", "stale_number_recall", "constraint_flag_recall"):
        if M[k]["value"] != 1.0:
            print(f"[selftest A] {k} = {M[k]}"); ok = False
    for k in ("fgr_mentioned", "fgr_unmentioned"):
        if M[k]["num"] != 0:
            print(f"[selftest A] {k} = {M[k]}"); ok = False
    if M["constraint_false_alarms"]["num"] != 0:
        print("[selftest A] constraint_false_alarms != 0"); ok = False
    print(f"selftest A (gold vs. gold, {M['transition_accuracy_all']['den']} scorable rows): {'passed' if ok else 'failed'}")

    # B) Hand-computed perturbations: 4 changes, with each expected value hard-coded
    okB = True
    P = [dict(p) for p in gold_as_pred(gold)]
    by = {p["id"]: p for p in P}
    by["P-TR-M3-M2-05"]["transition"] = "fulfilled"          # partial → fulfilled: fgr_mentioned +1, accuracy −1
    P.remove(by["P-TR-M3-M2-11"])                             # abandoned row missing → implicit not mentioned: accuracy −1, mention_recall −1, not a false green
    first_nm = next(p for p in P if p["transition"] == "not_mentioned")
    first_nm["transition"] = "fulfilled"                      # not mentioned → fulfilled: fgr_unmentioned +1
    by["P-TR-M4-M3-13"]["flags"] = []                         # condition mismatch missed with a run table: fgr_mentioned +1, accuracy −1
    by["P-TR-M3-M2-10"]["closing_quotes"] = [
        {"quote": "周老师上周末看完说直接删，我已经删了", "meeting_id": "M3"},   # verbatim
        {"quote": "周老师看完后说删掉，我已删除", "meeting_id": "M3"}]          # rewritten
    MB, _ = metrics(gold, prep(P), with_runs=True)
    n_m = MB["transition_accuracy"]["den"]
    n_all = MB["transition_accuracy_all"]["den"]
    n_unm = MB["fgr_unmentioned"]["den"]
    expect = {"fgr_mentioned": (2, MB["fgr_mentioned"]["den"]), "fgr_unmentioned": (1, n_unm),
              "transition_accuracy": (n_m - 3, n_m), "transition_accuracy_all": (n_all - 4, n_all),
              "mention_recall": (n_m - 1, n_m), "unmentioned_recall": (n_unm - 1, n_unm),
              "quote_verbatim_rate": (1, 2)}
    # fgr_mentioned denominator = number of partial + abandoned + condition mismatch rows
    exp_den = sum(1 for r in scored_rows(gold, True) if r["transition"] in ("partial_or_rescheduled", "abandoned")
                  or "condition_mismatch" in r.get("flags", []))
    if MB["fgr_mentioned"]["den"] != exp_den:
        print(f"[selftest B] fgr_mentioned denominator {MB['fgr_mentioned']['den']} != {exp_den}"); okB = False
    for k, (num, den) in expect.items():
        if (MB[k]["num"], MB[k]["den"]) != (num, den):
            print(f"[selftest B] {k}: got {MB[k]['num']}/{MB[k]['den']}, expected {num}/{den}"); okB = False
    # unmentioned_precision: predicted not mentioned = original nm − 1 + the 1 missing abandoned row; of those, gold nm = n_unm − 1
    if (MB["unmentioned_precision"]["num"], MB["unmentioned_precision"]["den"]) != (n_unm - 1, n_unm):
        print(f"[selftest B] unmentioned_precision {MB['unmentioned_precision']}"); okB = False
    print(f"selftest B (4 hand-computed perturbations + 1 rewritten quote): {'passed' if okB else 'failed'}")

    # C) Paired comparison: A=gold, B=perturbed version → b=4 (A right, B wrong), c=0
    cmp_ = compare(gold, GA, prep(P), k=4, with_runs=True)
    okC = cmp_["b_A_right_B_wrong"] == 4 and cmp_["c_B_right_A_wrong"] == 0 and abs(cmp_["mcnemar_exact_p"] - 0.125) < 1e-12
    okC = okC and abs(binom_two_sided(8, 2) - 112 / 1024) < 1e-12 and cmp_["verdict"].startswith("A 胜")
    print(f"selftest C (McNemar exact test b=4,c=0 → p=0.125; b=8,c=2 → p=112/1024): {'passed' if okC else f'failed {cmp_}'}")

    # D) κ + bootstrap: reuse the hand-computed value from score.py and check that the interval contains the point estimate
    xs, ys = list("aabbccaabb"), list("aabbcaabbb")
    k, po, lo, hi = kappa_boot(xs, ys, n_boot=500)
    okD = abs(k - 21 / 31) < 1e-9 and lo <= k <= hi
    print(f"selftest D (κ=21/31, bootstrap interval {lo:.2f}–{hi:.2f} contains the point estimate): {'passed' if okD else 'failed'}")

    # E) Verbatim: the verbatim version of a sentence passes; changing one character fails
    okE = is_verbatim("The gripper is fixed, I replaced the screws last Friday.", "M3") and \
        not is_verbatim("The gripper is fixed, I replaced the screw last Friday.", "M3")
    print(f"selftest E (verbatim check: changing one character fails): {'passed' if okE else 'failed'}")

    # F) Aliases: dropped / unmentioned / 兑现 all resolve to canonical names
    okF = canon("dropped") == "abandoned" and canon("unmentioned") == "not_mentioned" and canon("兑现") == "fulfilled"
    print(f"selftest F (canonical names ↔ aliases): {'passed' if okF else 'failed'}")
    return ok and okB and okC and okD and okE and okF


def main():
    ap = argparse.ArgumentParser(description="BriefPilot eval-kit layer 2: cross-meeting reconciliation scoring (standard library)")
    ap.add_argument("--gold", default=GOLD_PATH)
    ap.add_argument("--pred")
    ap.add_argument("--map")
    ap.add_argument("--with-runs", action="store_true", help="The system under test imported a run table: condition mismatch rows must carry condition_mismatch")
    ap.add_argument("--json")
    ap.add_argument("--from-diy", metavar="RAW_DIR")
    ap.add_argument("--emit-pred")
    ap.add_argument("--emit-mapping")
    ap.add_argument("--verbatim-filter", nargs=2, metavar=("SRC", "DST"))
    ap.add_argument("--compare", nargs=2, metavar=("A", "B"))
    ap.add_argument("--map-a")
    ap.add_argument("--map-b")
    ap.add_argument("--k", type=int, help="Pre-registered win margin (write it into the results file before running)")
    ap.add_argument("--kappa", nargs=2, metavar=("A", "B"))
    ap.add_argument("--blank", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    if a.blank:
        blank_cmd(); return
    if a.kappa:
        kappa_cmd(*a.kappa); return
    if a.from_diy:
        if not (a.emit_pred and a.emit_mapping):
            sys.exit("--from-diy requires both --emit-pred and --emit-mapping")
        from_diy(a.from_diy, a.emit_pred, a.emit_mapping); return
    if a.verbatim_filter:
        verbatim_filter(*a.verbatim_filter); return
    gold = load_gold(a.gold)
    ti = thread_index(gold)
    if a.compare:
        if a.k is None:
            sys.exit("--compare requires --k (the pre-registered win margin)")
        pa = load_pred(a.compare[0], load_map(a.map_a), ti)
        pb = load_pred(a.compare[1], load_map(a.map_b), ti)
        res = {name: compare(gold, pa, pb, a.k, a.with_runs, sp)
               for name, sp in (("all", None), ("dev", DEV), ("test", TEST))}
        for name, r in res.items():
            print(f"[{name}] n={r['n_rows']} b(A right, B wrong)={r['b_A_right_B_wrong']} c(B right, A wrong)={r['c_B_right_A_wrong']} "
                  f"McNemar p={r['mcnemar_exact_p']:.4f} k={r['k']} → {r['verdict']}; false green A={r['false_green_A']} B={r['false_green_B']}")
        if a.json:
            json.dump(res, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return
    if not a.pred:
        ap.print_help(); return
    preds = load_pred(a.pred, load_map(a.map), ti)
    print(report(gold, preds, a.with_runs))
    if a.json:
        out = {name: metrics(gold, preds, a.with_runs, sp)[0] for name, sp in (("all", None), ("dev", DEV), ("test", TEST))}
        json.dump(out, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
