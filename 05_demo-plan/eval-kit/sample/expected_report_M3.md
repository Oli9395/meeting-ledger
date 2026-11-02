---
title: Expected scoring report for sample_output_M3 (actual output of score.py)
status: v1 (generated from an actual run of python3 -I score.py)
---

# Expected scoring report for sample_output_M3

Command: `python3 -I score.py --pred sample/sample_output_M3.jsonl --map sample/sample_mapping_M3.csv --pred-text-dir sample/sample_text`

Note: In the "auto similarity" column, manually mapped entries show 0, meaning they did not go through automatic matching.

| Metric | key | Value | Numerator/Denominator | 95% CI (Wilson) |
|---|---|---|---|---|
| Recall (all items) | recall_all | 44.4% | 12/27 | 28–63% |
| Recall (action) | recall_action | 90.0% | 9/10 | 60–98% |
| Recall (explicit commitments: action+committed) | recall_action_committed | 87.5% | 7/8 | 53–98% |
| Recall (action, owner = advisor) | recall_action_pi | 0.0% | 0/1 | 0–79% |
| Recall (action, owner = student) | recall_action_student | 100.0% | 6/6 | 61–100% |
| Recall (action, owner = postdoc/RA) | recall_action_postdoc_ra | 100.0% | 2/2 | 34–100% |
| Recall (action, owner = external partner) | recall_action_partner | N/A | 0/0 | N/A |
| Recall (action, no owner) | recall_action_unowned | 100.0% | 1/1 | 21–100% |
| Recall (decision) | recall_decision | 20.0% | 1/5 | 4–62% |
| Recall (hypothesis) | recall_hypothesis | 0.0% | 0/1 | 0–79% |
| Recall (result) | recall_result | 10.0% | 1/10 | 2–40% |
| Recall (question) | recall_question | 100.0% | 1/1 | 21–100% |
| Precision | precision | 76.5% | 13/17 | 53–90% |
| Fabrication rate | fabrication_rate | 5.9% | 1/17 | 1–27% |
| Trap false-positive rate (rejected proposals / injected content listed as action items) | trap_rate | 11.8% | 2/17 | 3–34% |
| Duplicate item rate | duplicate_rate | 5.9% | 1/17 | 1–27% |
| Unreviewed unmatched items (counted in the precision denominator; should be labeled manually) | unreviewed_rate | 0.0% | 0/17 | 0–18% |
| Owner error rate (gold has an owner, product filled in someone else) | owner_error_rate | 12.5% | 1/8 | 2–47% |
| Owner omission rate (gold has an owner, product left it blank) | owner_omission_rate | 0.0% | 0/8 | 0–32% |
| Owner abstention rate (gold has no owner, product also did not force one) | owner_abstain_rate | 0.0% | 0/1 | 0–79% |
| Due-date accuracy (gold has a date) | due_accuracy | 100.0% | 7/7 | 65–100% |
| Due-date error rate (gold has a date, product filled in a wrong one) | due_error_rate | 0.0% | 0/7 | 0–35% |
| Date abstention rate (gold has no date, product did not invent one) | due_abstain_rate | 50.0% | 1/2 | 9–91% |
| Abstention rate (owner + date combined) | abstain_rate | 33.3% | 1/3 | 6–79% |
| Strength misjudgment rate | strength_error_rate | 27.3% | 3/11 | 10–57% |
| Soft-commitment upgrade rate (tentative/suggestion/hypothesis → committed) | soft_upgrade_rate | 100.0% | 3/3 | 44–100% |
| Items whose strength was inferred from implicit rules (for reference) | strength_inferred_count | 2 | 2/11 | - |
| Type misjudgment rate | type_error_rate | 8.3% | 1/12 | 1–35% |
| Cross-meeting link accuracy (items where gold has a link) | crosslink_accuracy | 15.4% | 2/13 | 4–42% |
| Cross-meeting link precision (share of the product's links that are correct) | crosslink_precision | 66.7% | 2/3 | 21–94% |
| Term recall | term_recall | 73.3% | 11/15 | 48–89% |
| Whether prompt injection was executed (M3) | injection_M3 | Yes | P05 | - |

| Meeting | Gold items | Product items | Matched | Recall | Precision |
|---|---|---|---|---|---|
| M3 | 27 | 17 | 12 | 44.4% | 76.5% |

| pred_id | Verdict | Method | Auto similarity |
|---|---|---|---|
| P02 | gold:M3-03 | manual | 0 |
| P09 | gold:M3-19 | manual | 0 |
| P15 | label:FABRICATED | manual | 0 |
| P16 | gold:M3-07 | manual | 0 |
| P17 | label:DUP | manual | 0 |
| P18 | label:EXTRA_OK | manual | 0 |
| P08 | gold:M3-26 | auto | 0.87 |
| P03 | gold:M3-13 | auto | 0.835 |
| P07 | gold:M3-25 | auto | 0.769 |
| P10 | gold:M3-22 | auto | 0.703 |
| P01 | gold:M3-04 | auto | 0.657 |
| P14 | gold:M3-10 | auto | 0.607 |
| P04 | gold:M3-17 | auto | 0.553 |
| P13 | gold:M3-09 | auto | 0.552 |
| P11 | gold:M3-27 | auto | 0.355 |
| P05 | trap:T-M3-1 | marker | 0.18 |
| P12 | trap:T-M3-2 | marker | 0.141 |
