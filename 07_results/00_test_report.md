---
title: "Meeting Ledger: Product Test Results"
status: Version 1
---

# Meeting Ledger: Product Test Results

**In one sentence**: The product is built and runs locally, and all 8 AI-played personas completed the full flow. **The number of real users is 0**. These results show that the product works and that quality is improving; they do not prove real demand.

## Evidence Levels

| Evidence | What it can prove | What it cannot prove |
|---|---|---|
| Unit and API tests (22 passing) | The code logic is correct | Model quality |
| Evaluation set (5 synthetic meetings, 135 gold labels, run with a real model) | Relative changes in extraction and reconciliation quality | Absolute accuracy: the gold labels were drafted by AI and have not been manually reviewed |
| Persona tests (AI-played, real browser operating the real product) | The product runs end to end, real bugs were found, behavior across different meeting formats | Real demand, retention, payment, real time saved |
| Real users | **None yet** | — |

## 1. Evaluation Set Results (3 prompt versions, claude-opus-5-5)

| Metric | v1 | v2 | v3 (shipped) |
|---|---|---|---|
| Item recall | 129/135 (95.6%) | 120/135 (88.9%) | **130/135 (96.3%)** |
| Action item recall | 67/70 | 61/70 | **68/70** |
| Precision (extra items not manually reviewed are counted as errors) | 129/170 (75.9%) | 120/138 (87.0%) | 130/164 (79.3%) |
| Fabrication rate | 0/170 | 0/138 | **0/164** |
| Wrong owner filled in | 1/57 | 0/52 | **0/58** |
| Owner left blank | 5/57 | 3/52 | 3/58 |
| Wrong due date filled in | 1/31 | 0/29 | **0/31** |
| No guessing when missing (dates) | 36/36 | 32/32 | 37/37 |
| Reconciliation type accuracy, full set | **21/23** | 18/23 | 17/23 |
| Reconciliation type accuracy, test set M4–M5 | **6/8** | 5/8 | 5/8 |
| False-green rate: unfinished judged as done | 0/11 | 0/11 | 0/11 |
| Not mentioned judged as done | 2/75 | 2/75 | 3/75 |
| Verbatim quote rate | 113/113 | 80/80 | 88/88 |
| Whether injection was executed | No | No | No |

**Key points**:
- To reduce noise, v2 tightened too much and recall dropped; v3 loosened based on development-set errors, and its extraction is the best of the three versions.
- **Reconciliation accuracy for v3 is lower than for v1**. Part of this is caused by quotes not matching the gold labels after drafts were merged (3 such examples seen so far), but there was no item-by-item manual adjudication, so not all of it can be attributed to scoring. This is a known issue.
- The test set has only 8 rows in the denominator, so the numbers fluctuate a lot.

## 1a. English Prompts (run `v3_en`)

The open-source version uses English prompts, so the same 5 meetings and gold labels were run once more with them. The meetings are mostly Chinese with some English, and they were not translated, because the gold labels must match them verbatim.

| Metric | v3 (Chinese prompts) | v3_en (English prompts, current) |
|---|---|---|
| Item recall | 130/135 | **131/135** |
| Action item recall | 68/70 | 68/70 |
| Precision (unreviewed extra items count as wrong) | 130/164 (79.3%) | 131/183 (71.6%) |
| Fabricated items | 0/164 | 0/183 |
| Wrong owner | 0/58 | 0/57 |
| Omitted owner | 3/58 | 3/57 |
| Wrong due date | 0/31 | 0/31 |
| Reconciliation type accuracy, full set | 17/23 | 21/23 |
| Reconciliation type accuracy, test set M4–M5 | 5/8 | 7/8 |
| False green: not finished but judged done | 0/11 | 0/11 |
| Not mentioned but judged done | 3/75 | 1/75 |
| Verbatim quote rate | 88/88 | 93/93 |
| Injection executed | No | No |

- **Precision fell.** The English prompts produced more extra items that users would have to dismiss.
- **The reconciliation gain is not proven.** This is one run, the denominator is small, and model output varies between runs. It should not be attributed to the translation without repeated runs.
- **Later sections predate this run.** The persona tests used the Chinese interface and Chinese prompts. They were not repeated on the English version.
- **English meetings are not scored.** The English sample ledger was produced by the same pipeline with no rejected items or retries, but it has no gold labels.

## 2. Persona Tests (8 personas, 2 rounds, 42 meetings in total)

Personas: a third-year PhD student, a PI on a phone, a note-taker, the lead of an English-speaking ML team, a founder with only recordings, a PM at an outsourced vendor, a postdoc who picks out mistakes, and an undergraduate in a WeChat group. Each persona first wrote their own meetings and expected tasks, then operated the product.

**Before/after comparison on the same set of meetings** (scored by the personas against the expectations they wrote in advance):

| Metric | Round 1 | Round 2 |
|---|---|---|
| Completed the full flow | 8/8 | 8/8 |
| Expected tasks found | 83/91 | 85/91 |
| Extra or duplicate drafts | 23 | **7** |
| Wrong owner | 22 | **2** |
| Wrong due date | 12 | **4** |
| Manual edits | 41 | **9** |
| Reconciliation judged correct | 51/56 | 50/56 |

**Objective records in the product database**:

| Metric | Round 1 | Round 2, same meetings | Round 2, new meetings |
|---|---|---|---|
| Drafts accepted without edits | 40/97 (41.2%) | **70/83 (84.3%)** | 29/35 (82.9%) |
| Reconciliation proposals confirmed | 48/57 (84.2%) | 49/52 (94.2%) | 37/38 (97.4%) |
| Median processing time | 51 seconds | 62 seconds | 51 seconds |

**Held-out sample** (meetings newly written in round 2, not seen while fixing bugs, scored by the personas): tasks 33/40, extra 1, wrong owner 3, wrong due date 1, reconciliation 40/44. Missed tasks were concentrated in "follow-up actions with a new time being assigned to reconciliation cards". Some of this was fixed at the end, and after the fix only one round of regression was run; not everything was retested.

**Security**: 3 kinds of prompt injection were not executed, XSS did not trigger, vague statements like "everything from last week is done" did not cause false fulfillment, cross-ledger access was denied, and links became invalid after deletion. The CSV formula injection found in round 2 has been fixed.

**"Would be very disappointed if it were unavailable"**: 0/8 → 1/8. This is an answer from AI-played personas and has no reference value; it only shows that this question has been wired into the product.

### Issues Found in Testing and Fixed (Excerpt)

| Issue | Found by | Result |
|---|---|---|
| Reconciliation cards displayed as `[object HTMLDivElement]` | Browser smoke test | Fixed |
| Two-line "name time" format from Feishu and WeChat parsed wrongly, leaving all owners empty | Third-year PhD student, undergraduate | Fixed |
| Advisor saying "你把…" ("you take…") was not recognized as an owner, requiring manual entry every week | PI | Fixed, and cross-checked by the validator |
| Nicknames (小王, 芳姐) did not match the member list | Note-taker | Fixed; no guessing when two people share a surname |
| Task names were whole sentences of verbatim speech | 4 personas | Fixed: added short titles, kept the verbatim quote |
| New tasks in recording scenarios were swallowed by reconciliation | Founder | Fixed |
| Exported minutes included rejected content | ML lead, vendor PM | Fixed |
| Corrupted audio error exposed server path | Founder | Fixed |
| CSV formula injection | Postdoc who picks out mistakes | Fixed |
| "Next week, maybe" was guessed as a specific date | Vendor PM, founder | Fixed: marked "time unclear" |
### Data Notes

- A mid-round report during Round 1 cited "32% directly adopted, 38% rejected." That figure counted drafts the system had merged automatically as rejections, which was wrong. It has been corrected here.
- In Round 2, some meetings show 6 to 18 minutes. This was caused by the computer going to sleep (the call time jumped, and the system log records deep sleep). For this reason the median is used here.
- In Round 2 the persona knew about the Round 1 problems, so its scoring may be somewhat lenient. The adoption rates in the database also come from the persona's actions, so they likewise do not equal real user behavior.
- The undergraduate persona pointed out during its retest that Round 1 should have 7 items rather than 8. The table keeps the originally submitted value, 83.
- After Round 2, 5 more fixes were made. These fixes were verified only by unit tests and one round of real-model regression; the 8 personas did not retest them.

## 3. Cost and Speed

Each meeting takes two model calls, costing about US$0.15 in equivalent cost as reported by Claude Code (Round 2: 25 meetings, US$3.49 total, claude-opus-5-5, effort=high). The median transcription time for a 1–3 minute recording is about 15 seconds. These figures come from the local development environment and need to be measured in production.

## 5. Files

- Product code and how to run it: `06_product/`; start with `06_product/README.md`
- UI screenshots: `06_product/docs/screenshots/`
- Raw evaluation results: `06_product/eval_runs/`
- Raw persona records: `06_product/persona_tests/` (`summary.json` is the summary)
