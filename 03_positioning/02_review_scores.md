---
title: "03_positioning Review Scoring Record: 4 Candidate Positioning Options × 3 Judges"
status: final (review record; scores transcribed verbatim from the structured scoring supplied by the workflow; averages and sensitivity analysis computed in this document)
sources_count: 4
sources_note: 4 candidate option files, all internal to the project; this document introduces no new external facts
---

# Review Scoring Record: 4 Candidate Positioning Options × 3 Judges

> **What this file records**: A verbatim transcription of the three judges' scores for `01_候选方案_1–4`, plus the averages, a summary of each judge's "strongest objection", and an analysis of where the judges disagree. The reasoning behind the final positioning is in `03_final_positioning.md`; this file only records "what the judges said and how the scores are calculated".
>
> **Two things to be clear about first**:
> 1. **The judges are not real people.** The three judges are roles played by a model in the workflow (investor/client, big-tech AI PM, target user). Their scores and "quotes" are **simulated review feedback**, not user interviews and not market evidence. This document uses them as a "structured list of counterarguments". [Fact: judge IDs and scores come from the workflow input; Inference: their representativeness has not been verified]
> 2. **All four options are themselves based on zero interviews and zero hands-on competitor testing.** So the generally low "pain evidence" scores from the judges (3–6) are an honest reflection of the current state, not the judges being harsh.

---

## 1. Judge Identities

| Judge ID | Role played | What they care about | Scoring habits (inferred from scores) |
|---|---|---|---|
| **vc-client** | Investor / knowledgeable client. The one who asks, "Feishu Minutes, Otter and Fireflies already do this, so why are you building it?" | Whether the need is proven, whether DIY can replace it, whether it's "just one prompt" | Strictest: total scores of 4.6–5.65 across the four options; pain evidence scored 3–6, defensibility 2–5 |
| **bigtech-aipm** | AI PM at a big-tech company (Feishu or a similar meeting product), also an interviewer | "Could we add this in one sprint?", portfolio signal, whether the evaluation design is professional | Middle: 5.55–6.35; gives the highest portfolio-value scores (8–9) |
| **target-user** | A dual role for the target user: a PI supervising 8 PhD students plus a third-year PhD student | Would I use it, are the incentives right, where does the input come from, is this how group meetings actually go | Middle-to-high: 5.1–6.25; the only judge who ranks Option 1 first |

---

## 2. Scoring Dimensions and Total-Score Formula

Six dimensions, scored 1–10:

| Dimension | Code | Meaning |
|---|---|---|
| Pain evidence | pain | Whether there is first-hand or reliable evidence that the pain is real and frequent enough |
| Gap authenticity | gap | Whether the gap is truly unaddressed (rather than just "not mentioned on the official site") |
| Defensibility | def | How long it would take Feishu/Fellow/Littlebird/DIY to catch up |
| Demo feasibility | demo | Whether one person can build it end to end and test it in 2–4 weeks |
| Persuasiveness | pers | Whether a knowledgeable person can see the difference within 5 minutes |
| Portfolio value | port | How well it demonstrates core AI PM skills |

**Total-score formula**: The workflow did not supply weights. This document back-solved them from the 12 totals and found the only set of weights that **reproduces all of them exactly**:

> total = 0.20 × pain + 0.20 × gap + 0.15 × def + 0.15 × demo + 0.15 × pers + 0.15 × port

Example: vc-client on Option 1: 0.2×3 + 0.2×6 + 0.15×(3+6+6+7) = 0.6 + 1.2 + 3.3 = **5.1**, matching the given 5.1. The other 11 totals were each checked as well. [Inference: the weights are back-solved, not declared by the judges]

---

## 3. Master Score Table (per option × per dimension × per judge)

Option short names:
- **Option 1** (dogfood-feasibility): pre-meeting "experiment commitments × run reconciliation sheet" (condition-mismatch state)
- **Option 2** (defensibility): reconciliation of experiment commitments that never leave the lab
- **Option 3** (evidence): group-meeting action item checker, BriefPilot Lint (field-level sourcing + don't guess when missing)
- **Option 4** (persuasion): group-meeting commitment ledger (statements in the next meeting reconcile the commitments from the previous one)

### 3.1 Raw scores

| Option | Judge | pain | gap | def | demo | pers | port | **total** |
|---|---|---|---|---|---|---|---|---|
| Option 1 | vc-client | 3 | 6 | 3 | 6 | 6 | 7 | **5.10** |
| Option 1 | bigtech-aipm | 4 | 7 | 4 | 7 | 7 | 8 | **6.10** |
| Option 1 | target-user | 4 | 7 | 5 | 7 | 7 | 8 | **6.25** |
| Option 2 | vc-client | 3 | 5 | 5 | 4 | 5 | 6 | **4.60** |
| Option 2 | bigtech-aipm | 3 | 6 | 6 | 6 | 6 | 7 | **5.55** |
| Option 2 | target-user | 4 | 5 | 5 | 5 | 5 | 7 | **5.10** |
| Option 3 | vc-client | 6 | 4 | 2 | 8 | 5 | 7 | **5.30** |
| Option 3 | bigtech-aipm | 6 | 4 | 3 | 9 | 5 | 8 | **5.75** |
| Option 3 | target-user | 5 | 4 | 3 | 9 | 5 | 7 | **5.40** |
| Option 4 | vc-client | 4 | 4 | 3 | 8 | 8 | 8 | **5.65** |
| Option 4 | bigtech-aipm | 5 | 5 | 4 | 8 | 8 | 9 | **6.35** |
| Option 4 | target-user | 4 | 5 | 4 | 8 | 8 | 9 | **6.15** |
### 3.2 Average Scores (Arithmetic Mean of the Three Judges)

| Option | pain | gap | def | demo | pers | port | **Mean total** | Rank | Range of the three judges' totals |
|---|---|---|---|---|---|---|---|---|---|
| **Option 4 Meeting Ledger** | 4.33 | 4.67 | 3.67 | 8.00 | **8.00** | **8.67** | **6.05** | **1** | 0.70 |
| Option 1 run statement | 3.67 | **6.67** | 4.00 | 6.67 | 6.67 | 7.67 | 5.82 | 2 | **1.15** |
| Option 3 Lint | **5.67** | 4.00 | 2.67 | **8.67** | 5.00 | 7.33 | 5.48 | 3 | 0.45 |
| Option 2 Stays on campus | 3.33 | 5.33 | **5.33** | 5.00 | 5.33 | 6.67 | 5.08 | 4 | 0.95 |

(The highest value in each column is in bold.)

### 3.3 Each Judge's Winner

| Judge | Winner | Runner-up | Gap between 1st and 2nd | Conditions for the win |
|---|---|---|---|---|
| vc-client | Option 4 (5.65) | Option 3 (5.30) | 0.35 | **Conditional**: on day 1, run H-R3 (Claude vs. an expert prompt) and test H-R5 with the Littlebird student edition; if either hits the exit threshold, downgrade to an "evaluation + workflow" piece |
| bigtech-aipm | Option 4 (6.35) | Option 1 (6.10) | 0.25 | **Must be reworked**: the value must rest on a multi-week ledger (not single-hop reconciliation); graft on Option 1's "condition mismatch" evidence cell; in W1, test the multi-hop version of H-R3, Littlebird, and a 2-week diary with 3–5 people from the same group |
| target-user | Option 1 (6.25) | Option 4 (6.15) | 0.10 ("basically a tie") | **Three changes required**: make the lead feature "checking whether a run complies with decisions made in the meeting"; count real-world frequency in week 1; graft on Option 4's cross-week ledger, "bookkeeping vs. reconciliation", and "reported a stale number externally". If explicit-condition commitments turn out to be fewer than 1 per week, pivot to the **single-user version** of Option 4's Meeting Ledger |

**[Inference] How to read this**: Option 4 wins 2 votes to 1, but all three judges' winners are "conditional winners", and the fallback attached to target-user's vote for Option 1 happens to be "the single-user version of Option 4". So the three judges effectively converge on the same **hybrid**: Option 4's cross-week reconciliation backbone + Option 1's decision-constraint / condition-mismatch evidence cell + Option 3's field-level trust foundation + Option 2's trust boundary. The disagreement is over which one leads and which one is the second beat; see §5.

---

## 4. Summary of the Strongest Objections

### 4.1 By Option

| Option | vc-client's strongest objection | bigtech-aipm's strongest objection | target-user's strongest objection | **Core wound all three agree on** |
|---|---|---|---|---|
| **Option 1** | The pain point is imagined; the project owner is not a W&B user themself; grouping by config in W&B shows rank16 in 30 seconds; the only frequency evidence is about 19% in synthetic data; Claude + the W&B MCP could be assembled in an afternoon; the rank16 in the magic moment is a landmine planted by ourselves | "rank16 mixed into rank32" is a W&B problem, not a meeting problem; real verbal commitments rarely carry all their conditions, so most slots would be empty; dogfooding depends on other people and needs IRB approval; "this is an expected-config annotation W&B should add" | The PI does believe in the pain of "numbers with the wrong conditions ending up in the paper", but real group meetings say "run a few more seeds" or "try rank again", with the conditions hidden in the default config; third-year PhD students already group-by in W&B before the meeting; W&B itself is a cloud service, so "stays on campus" is only half achieved | **Frequency**: commitments with explicit conditions may be too rare; **DIY**: W&B has built-in group-by and an official MCP |
| **Option 2** | The whole defense rests on "staying on campus is a hard requirement", yet the counter-evidence (NUS ChatGPT Edu) is in our own files; local deployment is commodity (Meetily, anarlog, Ollama); local 8–14B models will fall well short of cloud quality; scope is greedy; "0 bytes outbound" is a gimmick | "Stays on campus" contradicts itself: the evidence source, W&B, is itself SaaS; the target university uses M365, and Copilot enterprise data protection has most likely been enabled for students and staff; policy is the compliance office's pain, not the students'; "3 seconds during the meeting" contradicts "paste after the meeting" | The PI likes hearing "stays on campus", but run metadata already lives on wandb.ai, so the counter feels like a stage prop; what gets projected in group meetings is slides, and nobody will open another tool during the meeting; scope is too large | **The main leg could be cut off by a single IT email**; **W&B being SaaS makes "stays on campus" self-contradictory** |
| **Option 3** | This is a system prompt plus a UI label, not a product; Feishu's "can be edited manually" field may simply be left blank; one of the hardest pieces of evidence is a post by a user named "AI-Transcript", who has a stake in the outcome; Rashid Lab reads it back at the end of the meeting and it's done in 30 seconds; the window is 3–6 months | This is a prompt; having Feishu add a gray "AI-inferred" label is a single feature request; everyone in the group meeting is present, and if something is filled in wrong, one message in the group chat the next day corrects it; it requires supplying both another tool's output and the transcript, which is high friction; "a good evaluation, not a good product" | Nobody in my group uses AI to generate action items and then posts them to the group chat, so the object to be checked doesn't exist; the linter is stateless, so there is no reason to come back every week; the pain point is the generic "AI makes things up", not a pain of the target university's group meetings | **"It's just a prompt"**; **stateless, no reason to return** |
| **Option 4** | "Bookkeeping vs. reconciliation" is nicely put, but the white space is thin: Littlebird may already treat later meetings as evidence and the pages simply don't say so; Claude's long context + an expert prompt may be able to do it; demand evidence is zero; status may show up first in group chats, issues, or W&B; there is no data on κ for the 7 transition types; the 30 gold labels were drafted by the AI itself, with the planted traps also placed by the AI | Probably not white space at all, just undocumented in help pages (Littlebird, ZoomMate's "turn action items into status updates", Feishu's meeting digest is one sprint away); single-hop reconciliation H-R3 could be ruled out in half a day, and what remains, the "persistent ledger", is CRUD, not AI; κ for the 7 transition types will most likely fail to reach 0.6 | PI: "I ask at the start of the meeting, the student answers on the spot, and I don't look at the ledger"; third-year PhD student: the one doing the work is the note-taker while the beneficiary is the PI, so incentives are misaligned; "nobody in my group writes written minutes, everyone just puts up slides"; a Claude Project would most likely tie | **DIY with long context may tie (H-R3)**; **zero evidence of demand**; **incentives and input prerequisites** |
### 4.2 Re-grouping by "Attack Type" (Across Options)

| Attack type | Options hit | Judges | Notes |
|---|---|---|---|
| **A. "This is just a prompt / DIY can piece it together"** | 1, 3, 4 (2 indirectly) | All three raised it | Claude long context, Claude + W&B MCP, a one-line "write UNKNOWN" prompt. **This is the number-one attack on every option** |
| **B. Zero evidence on the demand side / frequency unknown** | All | All three raised it | None of the four options has interviews; Option 1's 19% comes from synthetic data; Option 4 only proves that the "opening recap" is a ritual |
| **C. "Not on the official site ≠ not done"** | 4, 1, 3 | vc, bigtech, target | Littlebird, ZoomMate, Feishu meeting digest, Feishu "can be added manually" |
| **D. Setting your own exam** | 1, 4 (3 admits it) | vc, bigtech | The gold labels were drafted by AI; the rank16 run was built by the team itself |
| **E. Scenario and user mismatch** | 4, 2, 3 | Mainly target-user | Misaligned incentives (note-taker vs. PI); nobody writes written minutes; nobody opens another tool during the group meeting; nobody uses AI action items |
| **F. Compliance narrative doesn't hold** | 2 (1 also affected) | All three raised it | A Singapore university's ChatGPT Edu; W&B SaaS; nobody enforces the policy |
| **G. Same beachhead = self-projection** | All | bigtech | All four options land on group meetings of computational labs at the target university, which is exactly the project owner's own environment |

---

## 5. Analysis of Disagreements

### 5.1 The Option with the Biggest Disagreement: Option 1 (total-score range across the three judges: 1.15)

| Dimension | vc | bigtech | target | Source of disagreement [Inference] |
|---|---|---|---|---|
| pain | 3 | 4 | 4 | Minor disagreement: all think frequency is unconfirmed |
| gap | 6 | 7 | 7 | **Consensus**: the most real gap of the four options (6.67 average, highest overall) |
| def | 3 | 4 | 5 | target-user thinks "DIY won't proactively treat last time's decision as a constraint", so scores higher |
| demo | 6 | 7 | 7 | vc cares more that "the W&B leg depends on classmates + IRB" |
| pers | 6 | 7 | 7 | vc thinks "planting the mine yourself and then defusing it" weakens persuasiveness |

**Core disagreement**: vc-client sees Option 1 as "something a W&B user could do on their own in 30 seconds"; target-user takes the PI's perspective and sees a high-cost event: "numbers from mismatched conditions going into a paper or an industry report". **Both are right**: the event is costly, but may be infrequent. This is exactly what H-D1 (frequency) is meant to answer.

### 5.2 The Win/Loss Flip Between Option 4 and Option 1: It Depends on the Weights

| Weighting scheme | Option 4 | Option 1 | Winner |
|---|---|---|---|
| Workflow weights (pain/gap 20% each, the rest 15% each) | **6.05** | 5.82 | Option 4 |
| Equal weights (1/6 for each of the six dimensions) | **6.22** | 5.89 | Option 4 |
| **Evidence first** (pain/gap 30% each, the rest 10% each) | 5.53 | **5.60** | **Option 1** |
| Storytelling first (demo 20%, pers/port 25% each, the rest 10% each) | **7.03** | 6.35 | Option 4 |

(Computed in this document, based on the dimension averages in §3.2.)

**[Inference] Conclusion**: Option 4 wins on "can be explained clearly and demoed" (pers 8.0, port 8.67, demo 8.0); Option 1 wins on "a more real gap" (gap 6.67 vs. 4.67). **Once the weight on "whether the demand and the gap are real" is raised, the outcome flips.** vc-client's summary hits the mark: "It wins by being easy to explain, not by having its demand proven." This shows that picking any single option leaves an obvious weakness, and **merging is dictated by the structure of the scores, not a compromise.**

### 5.3 Five Specific Disagreements

| # | Disagreement | One side | Other side | Direction of this document's ruling (see `03_final_positioning.md`) |
|---|---|---|---|---|
| D1 | **Who is the protagonist**: the note-taker maintaining the group ledger, or each student keeping their own ledger | vc, bigtech: keep "group-level ledger, advisor and partner commitments are also recorded, advisors don't need to sign up" as the main differentiator from Littlebird | target-user: the note-taker does the work and the PI benefits, so incentives are misaligned; it should become a single-user mode | **Start single-user, group-level ledger**: the user is the student who is "preparing last week's progress before the meeting"; the ledger is built per group, and commitments from advisors and others are still recorded, with the option to view only "those related to me"; note-taker mode goes into Next |
| D2 | **Whether "condition mismatch" is the main thread or the second beat** | vc, bigtech: demote it to one kind of transition within reconciliation + the second beat of the demo | target-user: the protagonist should be replaced by "decision in the meeting → constraint check on subsequent runs" | **Compromise**: the main thread is cross-week reconciliation; "decision as constraint" is the second beat and also the main weapon for answering "this is just a prompt"; whether to promote it to the main thread is decided by the H-D1 frequency result |
| D3 | **How to test H-R3 (DIY baseline)** | vc: run it on day 1; downgrade if the gap is <10 points | bigtech: must test the M2→M5 multi-hop, not only single hops; target: the control group should be "a Claude Project holding all the minutes + an expert prompt", not a weak baseline | **Use the strongest control group and test multi-hop**; on day 1 first measure DIY's absolute score, and if it is already close to the gold-label ceiling, there is no need to wait for our own system to be finished |
| D4 | **Number of transition types** | All three agree: compress 7 types to 4 first | — | **Adopted**: fulfilled / partial or rescheduled / dropped / not mentioned; "fulfilled but conditions mismatch" is a sub-flag of "fulfilled" (appears only when there is run evidence) |
| D5 | **How much to say about "data never leaves campus"** | All three agree: demote from selling point to trust boundary, cover it in 10 seconds | bigtech keeps the "0 bytes outbound" counter as a detail; target-user thinks the counter looks like a stage prop | **No counter**; say just one sentence: "meeting text can optionally stay on the local machine; where run data lives depends on whether your group uses SaaS or self-hosting", and proactively raise the counterexample of a Singapore university's ChatGPT Edu |
### 5.4 Equally Important Points of Consensus, With No Disagreement

1. **All four proposals have zero first-hand evidence on the demand side** (all three reviewers pointed this out). A 2-week diary study with 3–5 people from the same group should start in Week 1.
2. **Test the cheapest, most lethal DIY baseline first**, with the abandonment line written down in advance (all three raised this).
3. **Until the gold labels reach the κ threshold with two independent annotators, do not cite any "we're better" number externally** (all three raised this).
4. **Proposal 3's field-level three-state design and the "post-meeting follow-up message" should be merged into the winner** (all three raised this; the target-user reviewer called the follow-up message "the only thing a PI might actually forward").
5. **Proposal 2's original text of the target university's GenAI policy, its RCA clause, and the D2 test are kept as the basis for Bottle 2 (university–industry joint lab)** (all three raised this).

### 5.5 Limitations of the Review Itself

- All three reviewers are model-played personas that share the same input files, so they **very likely share the same blind spots** (for example, none of them mentioned that the open-source local tool Minutes already links decisions across meetings to check whether they were upheld; this was newly discovered while writing this document, see `03_final_positioning.md` §10).
- Scores are integers, so total-score gaps of 0.1–0.35 fall within scoring noise. **The margin between Proposal 1 and Proposal 4 should not be treated as a significant difference.**
- No reviewer represents "users who are not in a computational lab at the target university," and the "self-projection" alarm raised by the bigtech reviewer was not rebutted within the review either.

---

## Appendix: Sources

This document only consolidates in-project material and introduces no new external facts:
1. `03_positioning/01_candidate_1_dogfood_feasibility.md`
2. `03_positioning/01_candidate_2_defensibility.md`
3. `03_positioning/01_candidate_3_evidence.md`
4. `03_positioning/01_candidate_4_persuasion.md`
5. Structured scores from the three reviewers (workflow input)
