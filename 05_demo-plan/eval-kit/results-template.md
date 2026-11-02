---
title: Competitor Real-Output Comparison Experiment · Results Record Template
status: "Template v1.1 — experiment not yet run; all numbers are \"to be run\" (the wrap-up revision: added §1.4 feasibility, §6.1 positioning P-H1/P-H8 verdict rows, §11 Littlebird observation table)"
sources_count: 0
---

# Competitor Real-Output Comparison Experiment · Results Record

> **Status: to be run.** All numbers and conclusions below are blank. How to use: copy this file to `results-YYYY-MM-DD.md` and fill it in. Every number must be traceable to `results/<product>/metrics.json` and a screenshot; do not enter any number that has no screenshot or file behind it.

## 1. Experiment Conditions

### 1.1 Execution Info

| Item | Record |
|---|---|
| Executor | To be run |
| Execution date | To be run |
| Gold label version | To be run (git hash or date after review) |
| score.py self-test result | To be run (output of `python3 -I score.py --selftest`) |
| Audio condition | To be run (A-TTS / A-Human; TTS voice configuration; number of human readers) |
| Human reader consent form | To be run (yes/no; storage location) |

### 1.2 Products Under Test

| Product | Version/client | Account plan (free/trial/paid) | UI language | Transcription language setting | Which segments uploaded | Execution date | Notes (quota, errors) |
|---|---|---|---|---|---|---|---|
| Feishu Minutes | To be run | To be run | To be run | To be run | To be run | To be run | To be run |
| Feishu Meeting Express | To be run | To be run | To be run | — | To be run | To be run | To be run |
| Tongyi Tingwu | To be run | To be run | To be run | To be run | To be run | To be run | To be run (does the web version also give only 6 action items?) |
| Otter | To be run | To be run | To be run | To be run | To be run | To be run | To be run (what is the actual import-count limit?) |
| Fellow | To be run | To be run | To be run | To be run | To be run | To be run | To be run (does it support Chinese transcription?) |
| ChatGPT (B-Text) | To be run (model name) | To be run | — | — | To be run | To be run | Run 3 times |
| Claude (B-Text) | To be run (model name) | To be run | — | — | To be run | To be run | Run 3 times |
| E2 / E2-naive / E2c (Claude multi-meeting reconciliation) | To be run (model name; should be claude-opus-5-5) | API | — | — | M1…Mk, k=2..5 | To be run | 3 runs each; prompt versions ≤3 |
| E2d incumbent-product cross-meeting Q&A | To be run (which vendor) | To be run | To be run | To be run | To be run | To be run | If unavailable, write "untested (reason)" |
| ZoomMate (P-H2 supplement) | To be run | To be run | — | — | To be run | To be run | The official blog says "availability may vary by customer type, region"; if unavailable in Singapore, write "untested: region unavailable" |

### 1.2b Feasibility Check (W1 D1, 30 minutes, before uploading)

| Question | Testable / untested (reason) | Evidence (screenshot or help page) |
|---|---|---|
| Feishu Meeting Express is based on the "past week" smart minutes: can segments be uploaded by week according to their real dates? Can uploading 5 segments on the same day test cross-week behavior? | To be run | To be run |
| Whether an uploaded Minutes recording generates smart minutes | To be run | To be run |
| Whether Lark (Singapore) has Meeting Express | To be run | To be run |
| Whether Fellow can take audio uploads directly | To be run | To be run |
| Whether the Littlebird student discount can be claimed with the target university's school email (the website says "school email and student ID", without mentioning .edu) | To be run | To be run |

### 1.3 Gold Label Review and Consistency

| Item | Result |
|---|---|
| Number of entries annotator A changed after review | To be run |
| Change list (id, original label, new label, reason) | To be run |
| Double-annotation scope | To be run (suggested: M1 + M3, 46 items) |
| strength: κ / p_o | To be run / To be run |
| type: κ / p_o | To be run / To be run |
| owner agreement rate | To be run |
| due agreement rate | To be run |
| Unit identification: B's recall / precision against A | To be run / To be run |
| Whether thresholds are met (strength κ ≥ 0.6, type κ ≥ 0.7) | To be run |
| Boundary cases added after adjudication | To be run |
| **Transition-type κ (P-H8)**: double-annotation scope = 23 labeled rows + ≥20 randomly sampled not-mentioned rows (write the seed here: to be run) | To be run (`score_recon.py --kappa`) |
| Transition κ point estimate / bootstrap 95% interval / n | To be run / To be run / To be run |
| Whether it passes (point estimate ≥0.6 **and** lower bound ≥0.4) | To be run |
| Adjudication results for the 4 needs_adjudication rows | To be run |

## 2. Summary Table (all 5 meetings)

Write each cell as "value (numerator/denominator)". Report Otter's results on the Chinese meetings separately, marked "language not supported".

| Metric | Feishu Minutes | Tongyi Tingwu | Otter | Fellow | ChatGPT baseline (median of 3 runs) | Claude baseline (median of 3 runs) |
|---|---|---|---|---|---|---|
| recall_action | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_action_committed | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_action_pi (advisor) | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_action_student (student) | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_action_partner (partner) | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_action_unowned (no owner) | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_decision | To be run | To be run | To be run | To be run | To be run | To be run |
| recall_hypothesis | To be run | To be run | To be run | To be run | To be run | To be run |
| precision | To be run | To be run | To be run | To be run | To be run | To be run |
| fabrication_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| trap_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| owner_error_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| owner_abstain_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| due_accuracy | To be run | To be run | To be run | To be run | To be run | To be run |
| due_abstain_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| strength_error_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| soft_upgrade_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| type_error_rate | To be run | To be run | To be run | To be run | To be run | To be run |
| crosslink_accuracy (M2–M5) | To be run | To be run | To be run | To be run | To be run | To be run |
| crosslink_precision | To be run | To be run | To be run | To be run | To be run | To be run |
| term_recall | To be run | To be run | To be run | To be run | N/A (input is text) | N/A |
| injection_M3 | To be run | To be run | To be run | To be run | To be run | To be run |
## 3. Per-Meeting Details

One table per product, copied from the "meetings" sub-table output by `score.py`.

| Meeting | Product | gold | Product items | Matched | Recall | Precision | Notes |
|---|---|---|---|---|---|---|---|
| M1 | Pending | 19 | Pending | Pending | Pending | Pending | Pending |
| M2 | Pending | 23 | Pending | Pending | Pending | Pending | Pending |
| M3 | Pending | 27 | Pending | Pending | Pending | Pending | Pending |
| M4 | Pending | 38 | Pending | Pending | Pending | Pending | Pending |
| M5 | Pending | 28 | Pending | Pending | Pending | Pending | Pending |

## 4. Traps and Injection

| Trap | Content | Feishu | Tongyi Tingwu | Otter | Fellow | ChatGPT | Claude |
|---|---|---|---|---|---|---|---|
| T-M1-1 | Switch to π0 (rejected) | Pending | Pending | Pending | Pending | Pending | Pending |
| T-M2-1 | Build own sim benchmark (rejected) | Pending | Pending | Pending | Pending | Pending | Pending |
| T-M3-1 | prompt injection | Pending | Pending | Pending | Pending | Pending | Pending |
| T-M3-2 | Filter demos by duration (rejected) | Pending | Pending | Pending | Pending | Pending | Pending |
| T-M4-1 | Add π0 comparison (rejected) | Pending | Pending | Pending | Pending | Pending | Pending |
| T-M4-2 | speculative decoding (out of scope for this paper) | Pending | Pending | Pending | Pending | Pending | Pending |
| T-M5-1 | Open-source the checkpoint (rejected) | Pending | Pending | Pending | Pending | Pending | Pending |

Fill in one of: not present / appears as an action item (hit) / correctly appears as "rejected" / product proactively flags it (injection only).

## 5. Cross-Meeting Tracking

| Checkpoint | gold | Feishu (incl. meeting digest) | Tongyi Tingwu | Otter | Fellow | LLM, same conversation |
|---|---|---|---|---|---|---|
| Is "that baseline from last week" in M3 linked to M2-05? | M3-01/02/04 → M2-05 | Pending | Pending | Pending | Pending | Pending |
| The ownerless eval script from M2 is claimed by Wang Bo in M3 | M3-25 → M2-19 | Pending | Pending | Pending | Pending | Pending |
| Dan's quota script goes from unanchored to anchored | M3-27 → M2-17 | Pending | Pending | Pending | Pending | Pending |
| The advisor's own GPU request across 4 meetings | M1-12 → M2-18 → M3-23/24 → M4-14 | Pending | Pending | Pending | Pending | Pending |
| A forgotten suggestion (data card, M2-14) | Never mentioned afterwards | Pending | Pending | Pending | Pending | Pending |
| External report used stale numbers (M5-01 vs M4-06) | Unscored bonus item | Pending | Pending | Pending | Pending | Pending |

## 6. Hypothesis Verdicts

| # | Hypothesis (see README §1) | Decision line | Measured | Holds? | Implication for BriefPilot |
|---|---|---|---|---|---|
| H1 | Explicit commitments are caught; soft commitments get promoted | Best competitor recall ≥80% and promotion rate ≥50% | Pending | Pending | Pending |
| H2 | Commitments by the advisor / partners are more easily missed | Advisor group ≥20 points lower than student group | Pending | Pending | Pending |
| H3 | When there is no owner, one is filled in anyway | Best competitor's non-guess rate <50% | Pending | Pending | Pending |
| H4 | Dates with no anchor get turned into specific dates | Best competitor's non-guess rate <60% | Pending | Pending | Pending |
| H5 | No cross-meeting linking | All competitors <30% | Pending | Pending | Pending |
| H6 | Mixed Chinese-English terminology: Otter is markedly worse | ≥30 points lower | Pending | Pending | Pending |
| H7 | Rejected proposals get listed as action items | ≥1 competitor falls for it in ≥2 segments | Pending | Pending | Pending |
| H8 | Injection is not executed | Record only | Pending | Pending | Pending |

(H1–H8 in the table above = E-H1–E-H8 of the eval-kit; positioning hypotheses use the P-H prefix, see below.)

### 6.1 Positioning P-H1 / P-H8 Decision Rows (v1.1; **fill in the "fixed in advance" column first, then run**)

| Item | Fixed in advance (fill in before running, dated and signed) | Measured | Conclusion |
|---|---|---|---|
| Winning margin k (b − c over all scorable rows, default 5) | Pending | — | — |
| Cap on prompt iteration versions per side | 3 / 3 | This system: __ versions; E2: __ versions | — |
| P-H1 shortcut (W1): E2c `transition_accuracy` ≥20/23 **and** `fgr_mentioned` ≤1 item → exit | Same as left | E2c: __/23, fgr_m __/__ | Triggered / Not triggered |
| P-H1 formal line (end of W2): this system vs. the best DIY (whichever of E2 and E2c has more correct rows) over all scorable rows has b − c ≥ k, **or** `fgr_mentioned` count lower by ≥3; **and** b ≥ c on the test set (M4–M5) | Same as left | b=__, c=__, McNemar p=__; fgr_m: this system __/__ vs DIY __/__; test set b=__ c=__ | Holds / Gray zone / Does not hold |
| P-H1 exit line: b − c ≤1 **and** `fgr_mentioned` count difference ≤1 | Same as left | Same as above | — |
| Report dev set (M2–M3) / test set (M4–M5) separately | Required | See dev / test in `recon_metrics.json` | — |
| `fgr_mentioned` (first row) / `fgr_unmentioned`, each with n | Required | Pending | — |
| Does E2-naive **proactively** mention the M3 "rank 32" constraint or the stale 71.2% figure in M5? | Record | Yes / No (exact quote) | If "yes": the positioning claim "a DIY setup won't do this proactively" is void |
| E2d, the incumbent product: when asked, can it give a status per item and cite the exact words? Does it proactively propose batch updates? | Record | Pending / Not tested (reason) | Rewrites the "Unlike" paragraph of the positioning |
| P-H8: status-transition κ clears the bar | Point estimate ≥0.6 and lower bound ≥0.4 | See §1.3 | Pass / Fail (fail → 3 classes) |
| Known biases (must be stated) | The person tuning prompts = the gold-label drafter (the owner); transition gold labels were drafted by a model; mapping confirmer = __ | — | — |
## 7. Qualitative Observations

For each observation, state the product, the meeting, the screenshot filename, and the original excerpt. Record only what was seen, not speculation.

| # | Product | Meeting | Observation | Screenshot/File |
|---|---|---|---|---|
| 1 | Pending | Pending | Pending | Pending |

## 8. Evidence Index

| Product | Meeting | Screenshot file | Exported text | pred.jsonl | mapping.csv (reviewer) | metrics.json |
|---|---|---|---|---|---|---|
| Pending | Pending | Pending | Pending | Pending | Pending | Pending |

## 9. Conclusions (to be written after execution)

- Which differentiation hypotheses are supported by the data: Pending
- Which were rejected: Pending
- Adjustments to the BriefPilot demo scope: Pending
- One sentence to use in interviews (must include numerator and denominator, and the qualifier "on 5 synthetic meetings"): Pending

## 11. Littlebird Observation Table (positioning P-H3; synthetic data, no real meetings recorded)

> Method: Sign up for the student plan. In meetings with **only yourself**, play M1–M5 via TTS (spread across weeks by their real dates, or at least across days) and let Littlebird record them. Then check the Friday Promise tracker report. Tests on real 1-on-1s and group meetings wait until the IRB determination and consent from all participants.

| Week | Which meetings were played | Does the weekly report list the commitments from M2/M3? | Does it cite quotes from **later meetings** to determine status? | Does it include commitments by **others** (advisor, classmates)? | Status category | Screenshot |
|---|---|---|---|---|---|---|
| Pending | Pending | Pending | Pending | Pending | Pending | Pending |

Judgment: If the Littlebird weekly report cites statements from later meetings to determine the status of other people's commitments in a **multi-person group meeting** → the P-H3 failure line is triggered (see positioning doc §11).

## 12. Data Cleanup

| Product | Recording/transcript deletion date | Account deleted? | Executed by |
|---|---|---|---|
| Pending | Pending | Pending | Pending |
