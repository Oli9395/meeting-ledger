#!/usr/bin/env python3
# ---
# title: Transition gold generation script (transitions.gold.jsonl draft)
# status: v1 draft generator: the output is a draft "drafted by the model, pending labeling by owner A + independent labeling by a second person B", not human gold
# ---
"""Generate the gold/recon/transitions.gold.jsonl draft from gold/M*.gold.jsonl.

Usage (from the eval-kit directory):
  python3 -I tools/build_transitions_gold.py            # write gold/recon/transitions.gold.jsonl
  python3 -I tools/build_transitions_gold.py --stdout   # print only

Rules (consistent with 04_prd/01_PRD_v2.md §14.4):
1. Tracked items: entries in M1–M4 with type ∈ {action, question} (including tentative / suggestion).
   result, decision and hypothesis do not get transitions (PRD §14.4.1 R3, R4).
2. "Thread": if a new action / question in a later meeting has a cross_meeting_ref pointing to an older entry
   (claiming, restating, rescheduling, following up), it counts as the same thread and the transition is recorded on the thread root; the product is correct whether it attaches the transition to the root or to any member.
3. (root, meeting) pairs with a gold link get one of 4 labels from the LABELED table; the table is derived entry by entry from the PRD §14.4.3 mapping.
4. All other (root, each later meeting) pairs are not_mentioned until the thread closes; after closure (fulfilled / abandoned) they are no longer tracked.
5. Safety net: if a not_mentioned candidate's character-bigram similarity with any utterance in that meeting is ≥ the threshold, it is relabeled needs_adjudication
   (excluded from scoring, pending human adjudication), to avoid treating "a mention in different words" as not mentioned.
6. Second pass: 1 stale_number row and 3 constraint_check rows (these depend on gold/runs_synthetic.csv, a trap we planted ourselves).
"""
import glob
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # don't leave __pycache__ behind in eval-kit
_spec = importlib.util.spec_from_file_location("score", os.path.join(HERE, "score.py"))
score = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(score)

MEETINGS = ["M1", "M2", "M3", "M4", "M5"]
SIM_THRESHOLD = 0.50

# child entry -> thread root (action / question child entries only)
THREAD = {"M2-02": "M1-04", "M2-09": "M1-13", "M2-18": "M1-12", "M3-04": "M2-05", "M3-25": "M2-19",
          "M3-27": "M2-17", "M4-04": "M3-26", "M4-13": "M1-15", "M3-07": "M2-20"}

# (root, meeting) -> (type, closure gold, flags, note)
LABELED = {
    ("M1-04", "M2"): ("partial_or_rescheduled", ["M2-01", "M2-02"], [], "rank 16 完成、rank 64 未完成"),
    ("M1-04", "M3"): ("fulfilled", ["M3-08"], [], "经线程成员 M2-02 结案：rank 64 出来了"),
    ("M1-13", "M2"): ("partial_or_rescheduled", ["M2-09"], [], "无主事项被 Priya 认领（note=claimed）"),
    ("M1-13", "M3"): ("fulfilled", ["M3-18"], [], "经 M2-09 结案"),
    ("M1-12", "M2"): ("partial_or_rescheduled", ["M2-18"], [], "导师重申（note=restated）"),
    ("M1-12", "M3"): ("fulfilled", ["M3-23"], [], "交了，学院未批；'批'是另一件事"),
    ("M1-11", "M2"): ("fulfilled", ["M2-03"], [], "问题被决议解决"),
    ("M2-05", "M3"): ("partial_or_rescheduled", ["M3-01", "M3-02", "M3-04"], [], "Google robot 完成，WidowX 未跑，新日期'周日前'"),
    ("M2-05", "M4"): ("fulfilled", ["M4-01"], [], "经 M3-04 结案"),
    ("M2-19", "M3"): ("partial_or_rescheduled", ["M3-25"], [], "无主事项被指派（note=claimed）"),
    ("M2-19", "M4"): ("fulfilled", ["M4-03"], [], "经 M3-25 结案"),
    ("M2-17", "M3"): ("partial_or_rescheduled", ["M3-27"], [], "无锚点日期被锚定（note=rescheduled）"),
    ("M2-17", "M4"): ("fulfilled", ["M4-26"], [], "经 M3-27 结案"),
    ("M3-26", "M4"): ("partial_or_rescheduled", ["M4-04"], [], "被指派人打折扣（tentative）"),
    ("M1-15", "M4"): ("partial_or_rescheduled", ["M4-13"], [], "改期为模糊日期'11 月初'"),
    ("M2-20", "M3"): ("partial_or_rescheduled", ["M3-07"], [], "问题被重新提起仍未决（note=still_open）"),
    ("M1-10", "M3"): ("partial_or_rescheduled", ["M3-10"], [], "单 seed 初步结果，本人说不能算数"),
    ("M2-13", "M3"): ("fulfilled", ["M3-14"], [], ""),
    ("M2-11", "M3"): ("abandoned", ["M3-15"], [], "导师决议先不做（等 storage 扩容）"),
    ("M2-10", "M3"): ("fulfilled", ["M3-16"], [], "他人代述（speaker_is_owner=false）"),
    ("M3-03", "M4"): ("fulfilled", ["M4-02"], [], "软承诺被兑现"),
    ("M3-24", "M4"): ("fulfilled", ["M4-14"], [], ""),
    ("M3-13", "M4"): ("fulfilled", ["M4-08"], ["condition_mismatch"],
                      "口头兑现；合成 run 表 seed 3 的 lora_rank=16 违反 M3-09（自己埋的雷）"),
}
# (root, meeting) pairs known to need human adjudication: no gold link, but possibly mentioned semantically
ADJUDICATE = {
    ("M1-10", "M4"): "M3-13（补到 5 个 seed）是 M1-10 的后续但 gold 未链；M4-08 可能同时结案 M1-10",
}
EXCLUDED_LINKS = {"M4-12": "决议重申（R4）", "M5-01": "结果再引用（R3，旧数检查）",
                  "M5-02": "结果再引用（R3）", "M5-06": "结果再引用（R3）"}


def load_gold():
    gold = {}
    for p in sorted(glob.glob(os.path.join(HERE, "gold", "M*.gold.jsonl"))):
        for g in score.read_jsonl(p):
            gold[g["id"]] = g
    return gold


LINE = re.compile(r"^\[(\d\d:\d\d:\d\d)\] (.+?)：(.*)$")


def utterances(mid):
    path = os.path.join(HERE, "meetings", "plain", f"{mid}.txt")
    out = []
    for line in open(path, encoding="utf-8"):
        m = LINE.match(line.rstrip("\n"))
        if m:
            out.append(m.groups())
    return out


def build():
    gold = load_gold()
    rows = []
    roots = [g for g in gold.values()
             if g["meeting_id"] in MEETINGS[:-1] and g["type"] in ("action", "question") and g["id"] not in THREAD]
    # Sanity check: links covered by LABELED + excluded links = all links in gold
    linked = {g["id"] for g in gold.values() if g.get("cross_meeting_ref")}
    covered = {c for v in LABELED.values() for c in v[1]} | set(EXCLUDED_LINKS)
    missing = linked - covered
    if missing:
        sys.exit(f"[Error] These gold links are not covered by the transition table: {sorted(missing)}")
    n_links_used = len([c for v in LABELED.values() for c in v[1] if c in linked])
    for g in sorted(roots, key=lambda x: (MEETINGS.index(x["meeting_id"]), x["id"])):
        start = MEETINGS.index(g["meeting_id"]) + 1
        members = [g["id"]] + [c for c, r in THREAD.items() if r == g["id"]]
        for mid in MEETINGS[start:]:
            key = (g["id"], mid)
            base = {"thread": g["id"], "members": members, "at_meeting": mid,
                    "item_meeting": g["meeting_id"], "item_text": g["text_span"], "item_strength": g["strength"],
                    "item_type": g["type"], "item_owner": g["owner"], "split": "dev" if mid in ("M2", "M3") else "test"}
            if key in LABELED:
                t, closure, flags, note = LABELED[key]
                rows.append(dict(id=f"TR-{mid}-{g['id']}", kind="transition", transition=t, closure_gold=closure,
                                 flags=flags, requires_runs=bool(flags), label_status="draft_from_gold_links",
                                 notes=note, **base))
                if t in ("fulfilled", "abandoned"):
                    break
                continue
            if key in ADJUDICATE:
                rows.append(dict(id=f"TR-{mid}-{g['id']}", kind="transition", transition=None, closure_gold=[],
                                 flags=[], requires_runs=False, label_status="needs_adjudication",
                                 notes=ADJUDICATE[key], **base))
                continue
            best, best_u = 0.0, None
            for ts, sp, tx in utterances(mid):
                s = score.similarity(g["text_span"], tx)
                if s > best:
                    best, best_u = s, f"[{ts}] {sp}：{tx[:60]}"
            if best >= SIM_THRESHOLD:
                rows.append(dict(id=f"TR-{mid}-{g['id']}", kind="transition", transition=None, closure_gold=[],
                                 flags=[], requires_runs=False, label_status="needs_adjudication",
                                 notes=f"安全网：与本场发言相似度 {best:.2f}，可能被提及：{best_u}", **base))
            else:
                rows.append(dict(id=f"TR-{mid}-{g['id']}", kind="transition", transition="not_mentioned",
                                 closure_gold=[], flags=[], requires_runs=False, label_status="auto_not_mentioned",
                                 notes=f"本场最高相似度 {best:.2f}", **base))
    rows.append({"id": "FL-M5-M1-01", "kind": "stale_number", "result_gold": "M1-01", "invalidated_by": "M4-06",
                 "cited_at": "M5-01", "at_meeting": "M5", "split": "test", "label_status": "draft_from_gold_links",
                 "notes": "M4 要求 rank 32 主结果重跑，M5 对合作方仍报 71.2%；不依赖 run 表"})
    for cid, run_group, expect, note in [
        ("CK-M4-M3-13-chunk5", "chunk5", "condition_mismatch", "seed 3 的 lora_rank=16，违反 M3-09（自己埋的雷）"),
        ("CK-M4-ablation", "chunk_ablation", "ok", "chunk_size 4/16，rank 32，守规对照组，不应误报"),
        ("CK-M4-widowx", "widowx_baseline", "not_applicable", "零样本 baseline 没有 lora_rank 列，约束不适用，不应判不符"),
    ]:
        rows.append({"id": cid, "kind": "constraint_check", "constraint_gold": "M3-09", "run_group": run_group,
                     "expected": expect, "at_meeting": "M4", "split": "test", "requires_runs": True,
                     "label_status": "draft_synthetic", "notes": note})
    meta = {"_meta": True, "title": "迁移 gold 草稿（transitions.gold.jsonl）", "status": "draft——由 tools/build_transitions_gold.py 从 gold 链接生成；负责人 A 复核 + 第二人 B 独立标注前不得对外报数",
            "links_used": n_links_used, "links_excluded": EXCLUDED_LINKS}
    return meta, rows


def main():
    meta, rows = build()
    lines = ["# " + json.dumps(meta, ensure_ascii=False)] + [json.dumps(r, ensure_ascii=False) for r in rows]
    if "--stdout" in sys.argv:
        print("\n".join(lines))
    else:
        out = os.path.join(HERE, "gold", "recon", "transitions.gold.jsonl")
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        tr = [r for r in rows if r["kind"] == "transition"]
        from collections import Counter
        c = Counter((r["transition"] or "needs_adjudication") for r in tr)
        print(f"Wrote {out}: {len(tr)} transition rows {dict(c)}; used {meta['links_used']} gold links, "
              f"excluded {len(EXCLUDED_LINKS)}; 1 stale_number row; 3 constraint_check rows")


if __name__ == "__main__":
    main()
