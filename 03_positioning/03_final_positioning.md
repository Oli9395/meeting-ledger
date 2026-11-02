---
title: "BriefPilot v2 Final Positioning: A Group Meeting Commitment Ledger, Reconciling Last Meeting's Commitments and Decisions Against What Is Said in the Next Meeting (and, Optionally, the Run Config)"
status: "decision-v1.1 (closing revision of at the time of writing, see §0.1; positioning is chosen, \"conditionally viable\": if any of P-H1, P-H2, P-H3, P-H8, P-H12 hits its abandonment line, downgrade per §11; zero interviews, zero hands-on competitor testing, zero code)"
sources_count: 34
sources_count_method: unique URLs in the sources section (recounted at closing; original value 39)
inputs: 03_positioning/01_candidate-proposals_1–4, 02_review-scoring-log, the earlier v1 docs (not included)/docs/PRD.md, 02_user-research/06, 05_demo-plan/eval-kit
---

# BriefPilot v2 Final Positioning: A Group Meeting Commitment Ledger

> **Labeling rules** (carried over from the whole project): **[Fact]** has a source URL and the original page was opened; **[Summary]** only a search snippet or secondhand account was seen; **[Inference]** derived from facts; **[Assumption · to be verified]** requires interviews or experiments. All official sources were accessed at the time of writing. "Not seen" means the page does not say so, which is not the same as the product not having it.
>
> **New verification done for this document** (4 WebFetch/WebSearch calls in total): ① the GitHub homepage of the open-source project Minutes (silverstein/minutes); ② its `minutes-x1-closeout` skill page; ③ a name-collision search (the "Closeout" meeting app); ④ the tally.so homepage (name-collision check for a candidate name). ① and ② are **competitor signals newly found in this round**, which none of the three reviewers or four candidate proposals mentioned; see §10.2. The remaining competitor facts carry over the conclusions already verified in `01_market-research/06, 07` and the four candidate proposals, and are not reopened here.
>
> **What this document is not**: it is not a conclusion that "demand has been proven." It is a decision to pick, among four zero-evidence candidates, using review scores and objections, the direction that is **most worth falsifying first**, and to fix the falsification order and abandonment lines in writing.

---

## 0. One-Sentence Conclusion

> **For graduate students in computational labs at the target university who must report progress at a weekly group meeting and whose group has a transcript export or a rotating verbatim minutes-taker: meeting tools each open a new ledger entry after every meeting and can also answer "what was said last time" when asked, but none of them will **proactively and in batch** use the next meeting's remarks to propose new statuses for the previous meeting's commitments and ask you to confirm. BriefPilot does only this one step, "reconciliation": it automatically maps "got halfway," "dropping it for now," and "fixed" back to last week's commitment, attaching two verbatim-checkable evidence snippets to each entry; items nobody has mentioned for several consecutive weeks are surfaced; and when connected to a run config, it can also flag "said to be fulfilled, but what ran is not what the meeting decided." Where no evidence is found, it writes "not found" and does not tick the box for you.**

| Element | Content |
|---|---|
| **Target user** | The **graduate student themself** in a computational (ML / robotics / VLA) lab at the target university, who each week must prepare "last week's progress" before the group meeting and follow up on commitments after it (usable by one person alone). The ledger is built per group; commitments from the advisor, collaborators, and ownerless items are logged all the same, but the advisor and group members do not need to register |
| **The small unmet need** | Stage: **after one group meeting and before the next**, the step of "status of last week's commitments." Most status changes are said **aloud** in the next meeting, and the **decisions** made in the meeting ("use rank 32 from now on," "unify LIBERO-Long to 5 seeds") are supposed to constrain later experiments. Existing tools produce a **new** list after each meeting, with status relying on manual ticking or task-system sync. Littlebird's context includes meetings, email, calendar, and screen; each week it extracts "the commitments you made" from this week's meetings and compares them against "what actually happened," but the page does not say it uses **later-meeting remarks** to determine status, and its graduate-student page mentions only advisor meetings, not multi-person group meetings. Fabric can capture a decision log from group meetings, but its page does not say it compares decisions against subsequent runs. No vendor publicly states that, in a **multi-person group meeting**, it automatically proposes statuses for the previous meeting's commitments from the next meeting's remarks, and none treats in-meeting decisions as deterministic check conditions against a later run config ([Fact: not seen within the search scope]; see §5.1, §10.2) |
| **Differentiation type** | **Both, with feature differentiation as the main one.** Feature: proactive batch proposal of cross-meeting status transitions + a decision × run check (evidence-snippet verification is the trust foundation). User: the weekly computational-lab group meeting is the premise that makes these features **meaningful** (the same people, meeting weekly, last week's items reported this week, artifacts living in runs), **but the user segment itself is not a moat**: Littlebird already has a graduate-student page, and Fabric already has an academic-lab page. Honestly, this is "feature differentiation plus a segment that makes the features hold," not a "user-differentiation moat" |

**20-second elevator version**: "Meeting tools keep the books; BriefPilot reconciles them. When the group meeting says 'got halfway' or 'dropping it for now,' it automatically maps that back to last week's commitment, attaching two evidence snippets to each entry; if the meeting decided 'use rank 32 everywhere,' it checks whether later runs actually followed it. Where it finds no evidence, it writes 'not found' and does not tick the box for you."

### 0.1 v1.1 Revision Notes (closing revision at the time of writing, based on the issue list in `05_demo-plan/04_consistency_check.md`)

| What changed | Why |
|---|---|
| Littlebird's evidence source changed to the official site's original text "your meetings, your inbox, your calendar, and what was on your screen," and it is noted that it "goes through the week's meetings, extracts the commitments you made"; the corresponding cell in the value curve changed to "?"; the differentiation moved to "multi-person group meetings + decision × run check" | The old version said "the evidence source is email and documents," which is inconsistent with 07 L3 and the official site (blocker) |
| The input premise changed to "the group has a transcript export or a rotating verbatim minutes-taker," with shorthand notes demoted to a secondary input; at the positioning level, "original words" is now called "evidence snippets" and graded by source (§4.1) | "Verbatim verification" holds only on verbatim transcripts (blocker) |
| P-H1 decision rule rewritten: added the E2c, E2-naive, and E2d conditions; the success line looks only at transition correctness and false-green rate, using the paired discordant count (McNemar) with a k fixed in advance; dev set and test set reported separately; both sides limited to ≤3 prompt iterations | The old rule had asymmetric AND/OR and could be fixed by a single verbatim-filter script (blocker) |
| Added Fabric (R11) and incumbents' cross-meeting Q&A (R12) as competing substitutes; ZoomMate promoted to [Fact] and ranked ahead of Littlebird | Omissions (major) |
| U5 demoted to a pass line; U3, U6, U7 reclassified as "trust foundation / portfolio assets"; §5.2 now opens by stating the increment boundary | 06 §3 already ruled that "cross-meeting binary tracking" is not a differentiator |
| Added P-H12, a zero-code concierge gate (W1–W2); P-H9 merged into P-H5's success line; P-H3 now uses synthetic data; P-H7 gained "group-member consent rate" | The demand side had no gate that could halt development |
| Hypothesis numbering unified with a P-H prefix (eval-kit uses E-H; 02/06 use U-H) | Three numbering schemes conflicted |
| Removed every sentence that cites "ranked first in scoring" as a reason for selection; the reason for selection is now "fastest to falsify, and the evaluation assets can be reused after failure" | The 0.23 average score gap from models role-playing as reviewers is within noise |

---
## 1. Decision Process Summary

| Step | Basis | Conclusion |
|---|---|---|
| 1. Look at average scores (**simulated judges, played by a model**) | `02_评审打分记录` §3.2 | Option 4 (6.05) > Option 1 (5.82) > Option 3 (5.48) > Option 2 (5.08). **Options 4 and 1 differ by only 0.23, which is within the noise of model scoring, so it is not used as a reason for selection** |
| 2. Look at each judge's winner | Same, §3.3 | 2 votes for Option 4 (vc-client, bigtech-aipm), 1 vote for Option 1 (target-user, 6.25 vs 6.15, "basically a tie") |
| 3. Look at score structure | Same, §5.2 | Option 4 wins on persuasiveness (8.0), portfolio value (8.67), and demo (8.0); Option 1 wins on whitespace authenticity (6.67 vs 4.67). **When the evidence dimension is weighted to 30%, the outcome flips** |
| 4. Look at objections | Same, §4 | The three judges' suggested fixes for Option 4 are almost identical: cut to 4 transition types, test multi-hop DIY, graft on Option 1's "condition mismatch" cell and "resolution as constraint", and graft on Option 3's field-level three-state labels and post-meeting follow-up questions. The fallback path of target-user's vote for Option 1 is also "Option 4, single-user version" |
| 5. Decision | There is only one reason for the choice: **it can be falsified fastest, and after a failure the evaluation assets (transition gold labels, DIY comparison, competitor outputs) can be reused** | **Use Option 4's cross-week reconciliation as the main axis, graft on Option 1's hard-evidence cell as the second beat, use Option 3 as the trust foundation and Option 2 as the trust boundary; change the user from "note-taker" to "the graduate student themself (starting as a single user)"**. Recorded as "Option G′" |

**[Inference] Why "merging" is not papering over differences**: Option 4 on its own would be taken down by "this is just a long-context prompt" (the top attack from all three judges); Option 1 on its own would be taken down by "too infrequent, and a W&B group-by shows it in 30 seconds". The two wounds do not overlap: Option 1's "resolution as constraint" is exactly what a DIY long-context prompt will not do on its own initiative (target-user's argument), and Option 4's cross-week ledger gives Option 1's low-frequency events a container that gets opened every week.

---

## 2. Why This One, and Why Not the Others

### 2.1 Why This One

> **v1.1 note**: The "Scoring basis" column in the table below comes from the opinions of **simulated judges (played by a model)**, not from real expert opinions. The score gaps are within noise, so **in the Q&A we do not give "ranked first by score" as a reason**. The real reasons for the choice are R3, "it can be falsified fastest", and "evaluation assets can be reused after a failure" (G15).

| Reason | Scoring basis | Evidence (grade) |
|---|---|---|
| **R1 It has a "shape difference"**: others hand you a new list; this hands you a diff against last week's list (note: the diff view is close in form to Fellow's carry-over of unfinished items, and the only difference is that "status is proposed automatically from the next meeting's speech") | Opinions of simulated judges (model-played): persuasiveness 8; vc persona: "lets someone who knows the field see the shape difference at a glance within 5 minutes" | Fellow surfaces all open items before each recurring meeting, but completion is ticked by a person, and the page does not say status is changed automatically from later speech; Circleback's own how-to says "review manually at the next meeting, then update manually in the task system" ([Fact], Option 4 §2.3, opened in this round) |
| **R2 The operator is a single person, but one-time informed consent from the whole group is needed** | Simulated judges: demo feasibility 8.0 | 00/06 §1.5 come-for-the-tool; Option 4 §3.4. **v1.1 correction**: the ledger records the whole group's speech, and PRD §16 requires informed consent from the whole group, so "the advisor doesn't need to register" does not mean "no coordination cost"; if consent cannot be obtained from the whole group, only the operator's own commitments are recorded (P-H7 observes the "member consent rate") |
| **R3 It can be falsified fastest (main reason)** | bigtech persona (model-played): "30 cross-meeting links mean it can be falsified very quickly" | eval-kit gold: 30 cross-meeting links; v1.1 has built `score_recon.py`, a draft of the transition gold labels, a synthetic run table, and the E2 comparison prompt ([Fact], in-project files). The actual cost is about 1.5–2 days, not half a day |
| **R4 The portfolio signal is complete**: evaluation, refusal to answer, human in the loop, trade-offs, and the division of labor "LLM extracts slots, code makes the judgment" | Simulated judges: portfolio value 8.67 | Option 4 §12; Option 1 U-2. This is a portfolio asset, not a difference in user value |
| **R5 Grafting on Option 1 fills in the weakest part, the whitespace** | Option 1's whitespace authenticity 6.67 (simulated scoring); all three simulated judges suggested grafting on its "condition mismatch" and "resolution as constraint" | Fellow only has complete / archived; the context of Littlebird's three states is "your meetings, your inbox, your calendar, and what was on your screen", the page does not say it uses later meeting speech to determine status, and its graduate-student page only mentions advisor meetings, not W&B or GitHub ([Fact], 07 L1–L3; promise-tracker and graduate-students pages reopened at the time of writing); Fabric has a decision log but its page does not mention runs, configs, or W&B ([Fact], 07 P1, reopened at the time of writing) |

**What must be acknowledged at the same time**: its pain-point evidence scores only 4.33, and its whitespace authenticity only 4.67 (simulated scoring). The simulated judge (model-played vc-client) said: "It wins on being easy to explain, not on the need being confirmed." This positioning accepts that judgment, so the first thing in §11 is not writing code.

### 2.2 Why Not the Others (One by One)

| Candidate | Average score | Why it is not the main axis | What is kept |
|---|---|---|---|
| **Option 1 standing alone** (run reconciliation sheet) | 5.82 (2nd) | ① Frequency: the only number is roughly 19% from a rough keyword count in the synthetic gold ([Inference · rough count], admitted by Option 1 itself, not rechecked in this round); in real group meetings most verbal commitments do not come with their full conditions (target-user, bigtech); ② the owner is writing a survey paper and W&B usage is unknown, so dogfooding the W&B leg depends on classmates and an IRB pass (all three raised this); ③ the W&B runs table grouped by config already shows anomalous runs by itself, and Claude + the official W&B MCP (which has `compare_runs_tool`, [Fact]) can put it together in an afternoon (vc, bigtech). **Standing alone, the magic moment might trigger only once a month** | Resolution as constraint, the "fulfilled but condition mismatch" sub-flag, false-green rate as the primary metric, the LLM extracting slots only + deterministic code making the judgment, the H-D3 abandonment line, the "pure evaluation product" fallback |
| **Option 2** (stays on campus) | 5.08 (4th) | ① The main leg, "staying on campus is a threshold", has zero user evidence, and counter-evidence sits in its own file: NUS has opened ChatGPT Edu to the whole university ([Fact, media]); ② self-contradiction: if the evidence source W&B is SaaS, the run metadata is already in the cloud (all three raised this); ③ localization is already commonplace: Meetily has about 32.4k stars (rechecked at the time of writing), Anarlog about 9.7k stars (recorded in the first round, not rechecked in this round), and this round also found Minutes (MIT, local-first, about 1.6k stars); ④ "answer the PI within 3 seconds during the meeting" contradicts "paste text after the meeting", since group meetings project slides | A switchable provider (local Ollama / API) as a **trust boundary** rather than a selling point; the four conditions of the target university's GenAI research policy and the original text of the RCA clause; the D2 test; ICSI (CC BY 4.0) as a reproducible English foundation; the monthly competitor early-warning signal table |
| **Option 3** (BriefPilot Lint) | 5.48 (3rd) | ① "One system prompt plus one UI label" (vc, bigtech); ② stateless, so no reason to come back every week (target-user); ③ the pain point is the generic "AI makes things up", and one of the hardest pieces of evidence is a community post by a user named "AI-Transcript", who may have a stake (vc; admitted by Option 3 itself); ④ it admits a window of only 3–6 months | Field-level three states (given verbatim / vague in the source, keep the original wording / absent from the source, leave blank); post-meeting follow-up question messages; linter-style tool-agnostic input; L1/L2 evaluation and Wilson intervals; injected text treated as quoted content |
| **Option 4 original** (note-taker maintains the group ledger, 7 transition types) | 6.05 (1st) | Not rejected but **used after rework**: ① the user changes from "note-taker" to "the graduate student themself", fixing the incentive mismatch (target-user); ② 7 transition types cut to 4 (all three raised this); ③ H-R3 changed to multi-hop with a strong control group (bigtech, target-user); ④ a second beat, "resolution as constraint", is added, answering "what's left is just CRUD" (bigtech) | The main axis, double verbatim-quote verification, "not mentioned for N weeks", the "recording vs reconciling" framing, the M4→M5 beat of reporting stale numbers externally |
| First-round A–F (verifiable commitment layer, advisor 1-on-1, five-value evidence chain, Chinese-English terminology, vendor requirements ledger, open-source issue write-back) | Did not enter this round's review | Reasons are in §9/§12/§13 of the four candidate options, with consistent conclusions: A's claiming is covered by Fellow (AI-suggested items only, 07 F8), B is covered by Littlebird's graduate-student page (07 L9), C's five values have zero evidence (06 W10), D has no first-hand Chinese pain point (06 W4), E cannot be dogfooded, and nobody wants F | A's G2/G3 → trust foundation; C → second beat; D → terminology recall in evaluation; E → the 5th-bottle narrative; F → evaluation data source |

---
## 3. Which runner-up ideas were grafted in

| # | Idea | From | Where it goes | Which objection it answers |
|---|---|---|---|---|
| G1 | **Decision as constraint**: decisions made in the meeting (M2 "LIBERO-Long uses 5 seeds from now on", M3 "all later experiments use rank 32") automatically become check rules for later commitments and runs | Proposal 1 (U-3); the target-user feedback suggested promoting it to the lead feature | Now; second beat of the demo | "This is just a prompt": a DIY long-context setup will not proactively treat the previous meeting's decisions as constraints ([Assumption, to be validated]; tested as a separate item in P-H1) |
| G2 | **"Fulfilled but conditions don't match" sub-flag**: it was said aloud to be done, but the run config disagrees with the decision; evidence sources can be a W&B export CSV or a local config directory (**direct TensorBoard reading goes to v0.2**, consistent with PRD §9.4) | Proposal 1 (U-1, U-2); the target-user feedback added the input sources | Now (optional input); second beat of the demo | "A student saying they did it is only second-hand evidence" (target-user) |
| G3 | **False-green rate as the first metric**: the share of "not found" or "mismatch" items judged as "fulfilled"; "not found ≠ done" is a product discipline and is reported publicly | Proposal 1 | First line of the evaluation report | "Writing your own exam and grading it": report first the metric on which you are most likely to look bad |
| G4 | **The LLM only extracts slots; judgment is left to deterministic code** | Proposal 1 | Architecture | Reproducible and auditable; in interviews, it lets me explain "where an LLM belongs and where it doesn't" |
| G5 | **Field-level three states**: owner and date are each marked "stated verbatim / vague in the original (original wording kept) / not in the original (left blank)" | Proposal 3 (U1) | Now, on every row of the reconciliation sheet | The old PRD's `owner=null` and `relative_date_without_anchor` carry over directly |
| G6 | **Post-meeting follow-up message**: all "not in the original" and "no evidence found" items are gathered into a single follow-up draft (**private draft by default**; posting to the group is optional, since in a clearly hierarchical lab students may not dare to press the advisor in the group chat; tested in diary D15) | Proposal 3 (U2) | Now, as a by-product of the reconciliation result | target-user: "the only thing a PI might actually forward" |
| G7 | **Tool-agnostic input (linter mode)**: the input can be your own shorthand notes, slide notes, rotating-minutes, or a Feishu/Teams/Otter export; it only checks, never replaces | Proposal 3 (U5); the target-user feedback added slide notes and semi-structured shorthand like `@exp dataset=… seeds=…` | Now | "Nobody in our group writes written minutes" (target-user); lowers the cost of switching tools |
| G8 | **The full evaluation discipline**: L1 competitor testing → L2 strong-prompt baseline; Wilson 95% intervals; from v1.1, **paired discordant counts + a pre-fixed k** (n is too small, so percentage-point differences have no resolving power); untested cells are marked "untested"; no numbers reported until κ clears the threshold | Proposal 3; consensus of all three reviewers | Evaluation report | "Writing your own exam and grading it" |
| G9 | **Injected text is cited as meeting content, not executed as instructions** (eval-kit M3 [00:04:28]) | Proposals 3 and 4 | A 10-second security detail in the demo | — |
| G10 | **Switchable provider** (local Ollama / API) as the trust boundary; in week 1, ask the target university's IT whether there is an approved tool covering research data (D2); **proactively discuss the NUS ChatGPT Edu counterexample** | Proposal 2 | One FAQ entry; the demo does not include a "0 bytes outbound" counter | All three reviewers agreed that "data never leaves campus" cannot be the main selling point |
| G11 | **ICSI (CC BY 4.0, research-group weekly meetings) English subset** as a reproducible foundation; try a public W&B project for "semi-real" reconciliation (**whether a public project is usable remains to be verified**) | Proposals 2 and 3; target-user | Evaluation extension | "Synthetic gold labels are mines you buried yourself" |
| G12 | **The target university's GenAI research policy RCA clause + DESCA's "deemed accepted if no objection within N days"** | Proposals 2 and 4 | Reason for entering bottle 3 (university-industry joint labs) | Business story |
| G13 | **Monthly competitor early-warning signal table** (does Littlebird's grad-student page mention W&B/GitHub, does Fellow add an outcome field, does Feishu's meeting digest add "link external data sources"); this document adds three more: does Minutes add "automatic batch closeout"; does ZoomMate add "update the previous meeting's action item status based on the next meeting's remarks"; does Fabric add a W&B / code connector | Proposal 2 (D6) + this document | PRD risk monitoring | Window of opportunity |
| G14 | **A 2-week diary from 3–5 people in the same group**, asking four things once: where they first learned of a status, whether it was written back within 48 hours, how many conditional experiment commitments or decisions per week, and whether anything happened that they "didn't dare paste into ChatGPT" | bigtech (filling a shared gap) | P-H4, P-H5, P-H6, P-H10 in §11 | Zero evidence on the demand side |
| G15 | **Proposal 1's "pure evaluation product" fallback**: if DIY ties, present the evaluation set + DIY workflow as the deliverable, and say in interviews "I used data to disprove my own direction" | Proposals 1 and 4 | Abandonment action of §11 P-H1 | — |

**Deliberately not grafted**: Proposal 2's "0 bytes outbound" counter (target-user: "feels like a stage prop"); Proposal 1's "five-valued outcome" (zero evidence); the original 7 transition types of Proposal 4 (κ risk); Proposal 2's "answer the PI within 3 seconds during the meeting" scenario (contradicts the input method).

---

## 4. Product form: down to each step

### 4.1 Two touchpoints, one ledger

| Touchpoint | Timing | What the user does | What the system provides |
|---|---|---|---|
| **T1 Post-meeting reconciliation** (main axis) | Within 10 minutes after the group meeting ends | Paste this meeting's text. **Primary input**: a transcript export (Feishu / Teams / Zoom) or rotating verbatim minutes; **secondary input**: your own shorthand notes or slide notes (these can only provide "excerpt-level" evidence; see the table below) | **Proposed status transitions** against last week's (and earlier) ledger, each with "original wording of the commitment ↔ original wording in this report"; new commitments and decisions are entered into the ledger; fields that are "not in the original" are gathered into a single **post-meeting follow-up** |
| **T2 Pre-meeting reconciliation sheet** (second beat) | The evening before the next group meeting | Optional: import a run table (W&B CSV export / local config directory; TensorBoard goes to v0.2) | A one-page "progress since last week": the current status of every commitment, "not mentioned for N weeks", decision-constraint check results, "fulfilled but conditions don't match"; one-click export to Markdown to paste into slides |

**Evidence snippets are graded by source** (from v1.1, promoted from the labels in `04_prd/02` §8.3 to the positioning level; we no longer speak loosely of "original wording" externally):

| Grade | Source | What it can claim | What it cannot claim |
|---|---|---|---|
| **E1 Verbatim transcript snippet** | A transcript export with speaker and timestamp, or rotating verbatim minutes | "This is what X said, in minute N"; verbatim verification is meaningful | — |
| **E2 Excerpt snippet** | Your own shorthand notes, slide notes, non-verbatim minutes | "This is the line you wrote down"; verbatim verification only guarantees that "the model did not rewrite your notes" | Cannot say "this is someone's original wording" |
| **E3 No evidence** | Model inference, no snippet at all | No status is output; the item goes only into "not found / to follow up" | — |

**[Inference] An honest note on the input precondition**: to get E1, someone has to record and transcribe the meeting; and the transcription platforms (Feishu, Teams, Zoom) themselves hold the full history, so in theory they could do the same thing at any time. The foothold of this proposal is therefore not "they don't have the data", but "they don't proactively, in batch, propose transitions and ask for confirmation" (§5.2 boundary). The effect of the shorthand version is evaluated separately (the "shorthand version M3/M4" condition in P-H1); numbers from verbatim transcripts are not used to represent the shorthand scenario.
### 4.2 State Model: 4 Transition Types + 1 Sub-flag

| Transition type | Meaning | Example in eval-kit (synthetic data) |
|---|---|---|
| **Fulfilled** | This meeting contains a direct quote showing the item is done | M2 Priya "I'll fix the gripper by Friday" → M3 "The gripper is fixed" |
| ↳ *Fulfilled but conditions don't match* (sub-flag, appears only when run evidence is available) | Verbally reported as done, but the run config is inconsistent with the original commitment or resolution | M3 resolution "all later experiments use rank 32" + M4 "chunking is now filled out to 5 seeds", while the synthetic run table has one seed with `lora_rank=16` (**this run table is built in W1; the trap is planted by ourselves, so it only demonstrates the mechanism and does not prove how often this happens**) |
| **Partial or rescheduled** | Part of it was done, or a new date was given (if the new date has no anchor, write "unanchored") | M2-05 SimplerEnv baseline → M3 "The Google robot set finished running... the WidowX set hasn't run yet" |
| **Dropped** | Explicitly not being done, with the reason quoted verbatim | M2 DROID co-training (soft commitment) → M3 "co-training is on hold for now, let's revisit once storage is expanded" |
| **Not mentioned** | No relevant quote in this meeting; accumulates over N consecutive weeks | M2-14 Daniel "maybe someone should write a data card" → never mentioned again |

"Claimed" and "still undecided" are not separate categories. They are shown as notes under "Partial or rescheduled" and as the status of question items. We will consider splitting them out once κ meets the target (adopting the unanimous recommendation of the three judges).

### 4.3 What We Don't Do

No audio recording, no transcription, no meeting bot sent into calls, no full-text summaries, no task-system sync, no write-back to W&B or GitHub, no claiming UI, no group-wide dashboard, no judging experiment conclusions for people (no "five-value results"), and no real-time use during the meeting.

---

## 5. April Dunford's Five Elements (Full Version)

### 5.1 Competitive Alternatives (What This Graduate Student Would Do Without BriefPilot)

| # | Alternative | How far it gets on "status of last week's commitments" | Gap | Evidence |
|---|---|---|---|---|
| R1 | **Do nothing**: the advisor asks at the meeting and the student answers on the spot | Zero cost; target-user playing the PI: "I ask at the start, the student answers on the spot, and I hear it" | Commitments that aren't asked about quietly disappear; the advisor's own commitments are the least likely to be asked about; nobody goes back to check resolutions | [Inference]; Dunford: "No decision" is the biggest competitor (00/03 §1.4) |
| R2 | **Manual reconciliation**: dig through group chat, shorthand notes, last week's slides, then open W&B to check configs | Most accurate | Time-consuming, depends on that night's attention; starts from scratch every week; "on what basis did you change the status" leaves no evidence | Rashid Lab "Review last week's action items"; MIT Cahoy next-time review ([Fact], 07 P7, U3 §3.1) |
| R3 | **W&B runs table grouped by config** | Shows at a glance which runs have inconsistent configs | Doesn't know what was promised or decided in the meeting | [Inference]; arguments from vc and bigtech |
| R4 | **ChatGPT / Claude long context**: put 4 weeks of minutes into a Claude Project and ask "compare against earlier commitments, give status transitions, and cite the original quotes" | **May work very well** (all three judges concluded this) | To be tested: multi-hop accuracy, whether original quotes get paraphrased, whether "not mentioned" can be found reliably, whether resolution constraints get checked proactively; uploading real group-meeting content to an external GenAI is subject to the target university's policy | [Inference]; the target university's GenAI research policy ([Fact]). **Top competitor, P-H1** |
| R5 | **DIY assembly**: Claude + Fellow/Granola/Minutes MCP + official W&B MCP | Technically can assemble most of it | Must write a prompt every time; no fixed slots or decision rules; no persistent ledger | W&B MCP `compare_runs_tool` ([Fact], plan 1 opened this round); Fellow MCP ([Fact], 07 F14); Minutes MCP ([Fact], opened this round) |
| R6 | **Littlebird (graduate student page, student price $15/month)** | Its context is "your meetings, your inbox, your calendar, and what was on your screen"; Promise tracker "goes through the week's meetings, extracts the commitments you made", then "checks each one against what actually happened: the email that went out, the document that shipped", producing three categories: kept / in progress / needs a rescue note; by default it only tracks your own commitments, "If you want to track what others owe you… just say so in the prompt"; Team plan has "Shared projects and routine templates" | The page **does not say** it uses statements in later meetings to determine status (the examples are all emails and documents); the graduate student page only mentions "advisor meetings" and **does not mention multi-person group meetings**; no mention of W&B, GitHub, or run configs | [Fact] reopened https://littlebird.ai/routines/promise-tracker , /for/graduate-students , /pricing; 07 L1–L10 |
| R7 | **Fellow** | Before each recurring meeting, surfaces all open items (Always / Never / Ask me); assignees accept / dismiss (**AI-suggested items only**); two-way GitHub sync via Zapier | Completion is ticked off by a person; the page doesn't say status is changed automatically from later statements; only complete / archived | [Fact] 07 F4, F5, F8, F11, F13 |
| R8 | **Feishu Minutes + Meeting Express (会议速递)** | Automatically produces action items for every meeting, traceable back to the source text; Meeting Express aggregates a week's action items; recognizes enterprise terms; mixed Chinese-English speech is recognized in the original language | The page says "aggregate", not "close out"; Singapore requires Lark, and feature parity is still to be verified | [Fact] 07 C5–C11 |
| R9 | **Minutes (open source, local-first) + closeout skill** | Meetings are stored as Markdown, with `action_items` (including status) and `decisions` in the YAML; an example links a February decision with a March reversal across meetings; the closeout skill matches **one** user-selected meeting conclusion to **one** existing collaboration thread, and the user picks the outcome, producing a draft | The page doesn't say it automatically tracks commitments across meetings or automatically marks old action items as done; closeout handles a single item, the user selects the outcome, and it depends on X1 | [Fact, checked verbatim; see `01_market-research/09` §1] opened this round, see §10.2 |
| R10 | **ZoomMate** (Zoom AI Companion) | Official blog: "you can quickly revisit previous discussions, unresolved action items, and open questions"; "A project team might automatically generate status updates and assign tasks based on decisions"; "either per-meeting or across a recurring series" | **Closer to this proposal than the earlier version of this positioning stated.** The page does not say "use the next meeting's statements to automatically propose the previous meeting's status and ask for confirmation", and does not mention run comparison; "availability may vary by customer type, region"; the half-sentence about Jira in 07 Z6 **does not appear** on this page, so it stays "to be verified" | [Fact] opened at the time of writing https://www.zoom.com/en/blog/zoommate-getting-started/ ; add ZoomMate to the P-H2 hands-on test, and if unavailable in the region, write "untested: unavailable in region" |
| R10b | Circleback | Manual review at the next meeting, then update the task system | — | [Fact] (plan 4 opened this round) |
| R11 | **Fabric (academic lab page)** | The agent "reads your supervisor meeting recording, extracts the action items, and creates tasks for each lab member with deadlines"; decision log "tracking analytical choices, methodological pivots, and design decisions as they're discussed in meetings and channels"; "pulls together a weekly lab digest… so the PI stays current" | The page doesn't say how task completion is tracked (only a generic Kanban); **no mention of runs, configs, W&B, or code** (connectors listed are only Google Drive, Dropbox, Notion, Gmail, Slack, and meeting tools); no named customers (07 P2) | [Fact] reopened https://fabric.so/teams/academic-labs ; 07 P1–P3 |
| R12 | **Cross-meeting Q&A in incumbent products**: Otter AI Chat, Granola folder Q&A, Circleback cross-meeting chat, Fireflies AskFred, Tongyi Tingwu multi-file Q&A (up to 50 files at a time, answers cite sources and timestamps) | Holds the full history; **when asked**, can answer "who promised what last week and how far along is it" | "Starts from zero every time, no ledger" is **not true** of them. The only difference: they are passive Q&A, and their pages don't say they would **proactively, in batch** propose transitions and ask for confirmation (**to be tested in E2d**) | `01_market-research/02` sections on each product; 07 C3 (Tingwu, 2024 media report, [Fact, media]) |

**[Inference] Actual ranking of opponents**: R1/R2 (do nothing or manual) > **R4 (Claude long context)** ≈ R12 (cross-meeting Q&A in incumbent products) > **R10 (ZoomMate)** > R6 (Littlebird) > R11 (Fabric) > R9/R5 (open source and DIY) > R7, R8. The **single-meeting minutes** of Feishu and Otter are Class B competitors at this step; their **cross-meeting Q&A** (R12) is Class A and must be tested hands-on (E2d).
### 5.2 Unique Attributes

> **Boundary (v1.1)**: Carrying over unfinished items, binary completion status, cross-meeting Q&A, and capturing meeting decisions are all **table stakes** (06 §3 already ruled that "cross-meeting binary tracking" and "a basic version of commitment-evidence comparison" are not differentiators; Fellow, Littlebird, Fabric, ZoomMate, and R12 each cover part of them). **The only increment of this proposal is one thing: automatically proposing 4 kinds of status from free-form speech in the next meeting and requiring confirmation** (U1), plus a second beat that depends on it (the deterministic comparison part of U2). U3–U7 are not differentiators in terms of user value; they are listed separately as "trust foundation / portfolio assets".

**Differentiators in user value (the increment)**

| # | Attribute | Is it "only we have it"? |
|---|---|---|
| U1 | **In a multi-person group meeting, using what is said in the next meeting as evidence, proactively and in batch propose status transitions for commitments from the previous meeting (and earlier)** (4 kinds) and require confirmation | [Fact: not found in public documentation within the search scope]. Closest: ZoomMate (can "revisit… unresolved action items" and generate status updates from decisions; does not state that it automatically proposes transitions), Minutes closeout (single item, the user picks the outcome), Littlebird (each week extracts your commitments from that week's meetings, then checks them against email and documents; does not state that it uses later meetings to decide; the graduate-student page only mentions advisor meetings), R12 cross-meeting Q&A (passive) |
| U2 | **Deterministic comparison of decisions × run config**: decisions made in the meeting become check conditions for subsequent runs; when a verbal fulfillment does not match the run config, flag it as "fulfilled but conditions mismatch" | **Capturing decisions already exists** (Fabric decision log, Minutes `decisions`, ZoomMate generating tasks from decisions); **deterministic comparison of decisions × run config not found** [Inference: not found within the search scope; for how far experiment-tracking tools go at this step, see `01_market-research/09`] |

**Trust foundation / portfolio assets (not differentiators in user value, but they make U1 trustworthy and verifiable)**

| # | Attribute | Notes |
|---|---|---|
| U3 | **Verbatim verification of evidence snippets**: each transition carries both "the original commitment wording + the original closing wording"; the server verifies them verbatim, and if verification fails, nothing is output | Feishu already provides item-level traceability within a single meeting; "two pieces of evidence + refuse to answer on verification failure" not found [Inference] |
| U4 | **"Not mentioned for N meetings" is a first-class status** and requires a persistent ledger | A single paste cannot do "not mentioned for three consecutive meetings" [Inference, tested in P-H1]; however, R12, an incumbent product, holds history and may be able to answer when asked (tested in E2d) |
| U5 | **Group-level ledger** (v1.1 **downgraded to table stakes**): advisors, collaborators, and ownerless items are all recorded | Littlebird's website says "track what others owe you… just say so in the prompt", and its Team plan can share projects; Fellow works by assignee. The operator is a single person, but it needs one-time informed consent from the whole group (§2.1 R2) |
| U6 | **Field-level three-state + post-meeting follow-up questions** | Field-level provenance not found; follow-up messages not found (Proposal 3 §6.2). A single prompt can approximate it (tested in P-H11) |
| U7 | **Public evaluation** (portfolio asset): cross-meeting reconciliation accuracy, false-green rate, verbatim-quote rate, including a Claude long-context strong baseline, Wilson intervals, and two-rater κ | Vendors publish no action-item accuracy ([Fact: not found within the search scope], 05 K1); academic benchmarks are sentence-level (08) |

**Table stakes that do not count as unique attributes**: citations, human confirmation, carrying over unfinished items, binary completion status, cross-meeting Q&A, capturing decisions, claiming (AI-suggested items only, Fellow), group-level ledger, no bot, runs locally, GitHub integration.

### 5.3 Value (attribute → outcome users care about) and Evidence

| Value | For whom | From | Evidence today | Numbers to obtain |
|---|---|---|---|---|
| **V1 Get a "last week's progress" reconciliation page 10 minutes before the group meeting**, without digging through group chats, notes, and W&B to piece it together | Students | U1, U4, U6 | Zero first-hand data. (v1.1 removes an old citation: the Zhihu post "What to report when the group meeting has no progress" is about "having no progress to report"; it is related to "needing a reconciliation page" but does **not support** it) | Preparation time before and after dogfooding, 2 times each (self-reported); P-H7 |
| **V2 Commitments don't quietly disappear**: advisor commitments, ownerless items, soft commitments, suggestions nobody mentions | Students, PI | U1, U4, U5 | eval-kit has seeded samples (8 advisor items, 4 collaborator items); zero data on real frequency | eval-kit E-H2 (recall grouped by owner); diary D7b, F2 |
| **V3 Don't carry stale or condition-mismatched numbers into slides, papers, or external reports** | PI (cares most), students | U2, U3 | The PI played by the target-user persona: "My biggest fear is numbers with the wrong conditions ending up in a paper or in the quarterly report for the company" (**simulated opinion, not a user's own words**); Gundersen & Kjensmo 2018 (AAAI): only about 20%–30% of reproducibility variables are documented ([Summary]: follows the paraphrase in 02/03 §4.1; the attempt to open the AAAI page was blocked and the PDF on the author's homepage returned 404, so **page / table numbers remain to be verified**) | Number of real "condition drift" events in P-H6; the M4→M5 71.2% beat is synthetic only |
| **V4 Dare to use it, with quantifiable trust** | Students, PI, interviewers | U3, U7 | The target university's GenAI research policy ([Fact]); Wiley 2025: 64% concerned about hallucination ([Fact]) | False-green rate, verbatim-quote rate, injection tests |

### 5.4 Target Customers (the people who care most about these values)

**Beachhead**: Graduate students in computational labs at the target university (ML / robotics / VLA) who meet the following 4 observable traits:
1. They have a regular weekly group meeting or advisor 1-on-1;
2. The meeting includes a "did that run from last week finish?" style review;
3. **The group has a transcript export or rotating verbatim minutes** (Feishu / Teams / Zoom export, or a rotating note-taker writes verbatim minutes). Their own notes and slide speaker notes are demoted to a **secondary input**, giving the E2 only excerpt-level evidence (§4.1), with effects evaluated separately (P-H1 notes-version condition). The target-user persona pointed out that many groups only put up slides; such groups are outside the beachhead, and P-H7 records the proportion with "no text";
4. Experiments run on W&B / TensorBoard + Git (affects the second beat only).

| Moore criterion | Judgment | Basis |
|---|---|---|
| Big enough to matter | **Weak**: enough for the portfolio and validation; not enough for a business | The number of computational labs at the target university was not found; no figure is invented |
| Small enough to lead | **Medium** (downgraded in v1.1; the old "strong" was circular reasoning) | Within the search scope there is no product dedicated to "group meeting reconciliation", but Littlebird (graduate-student page) and Fabric (academic lab page) already offer adjacent features in the same niche |
| Fit with crown jewels | **Medium** (downgraded) | The project owner is in this lab, understands VLA terminology, and has the eval-kit; **but the project owner is writing a survey and is not a heavy W&B user** (admitted in Proposal 1), so dogfooding the second beat will depend on classmates |

**Explicitly not served**: wet labs (evidence lives in ELNs and paper notebooks); people who need this tool to record and transcribe (leave transcription to the tools they already have); PIs who want a group-wide dashboard (Next); groups with no text input at all that are also unwilling to write 3 lines of notes.

**Self-projection alert** (bigtech): All four proposals sit inside the project owner's own environment. Countermeasures: at least 2 diary participants come from **outside this group**; keep the enterprise ML comparison interviews from 02/06 (P-H10); add the ICSI English subset to the evaluation.
### 5.5 Market category (and trends)

- **Do not place it in** "AI meeting notes / notetaker": in that category, Feishu, Otter, and Fellow are the reference points, and BriefPilot would be compared with each of them as "no transcription, no recording, no integrations."
- **Place it in** the "**group-meeting commitment reconciliation layer**" (commitment reconciliation layer): it sits on top of any meeting notes, and the reference point becomes "reconciliation." In Chinese, "bookkeeping" and "reconciliation" are two different jobs with two different tools, so the distinction is understood immediately [Inference]. For computational labs, it can also be pitched as "running CI on the group meeting": decisions are the tests, and runs are the things under test [Inference].
- **Trends**: ① AI hallucination has made "verifiable output" an expectation ([Fact] Wiley 2025); ② MCP makes meeting text portable ([Fact] 06 V2), so "building a layer on top of someone else's notes" is technically natural; ③ universities are tightening research-data rules (the target university's policy, rechecked 2025-11-07) while also procuring approved cloud tools (NUS ChatGPT Edu), and both forces need to be described honestly.

---

## 6. Positioning statements

### 6.1 Moore's six-part template

```
For        Graduate students in computational (ML/robotics/VLA) labs at the target university who report experiment progress at the weekly group meeting
Who        are dissatisfied with the status quo: who promised what last week, what was decided in the meeting, and how far each item has progressed are all stated orally at the next meeting;
           meeting tools generate only a fresh set of action items per meeting, status depends on people ticking boxes, nobody goes back to check decisions,
           and the night before the group meeting they can only dig through group chats, shorthand notes, and W&B to piece it together themselves
Our product is a  group-meeting commitment ledger (a "reconciliation layer" that sits on top of any meeting notes)
That       takes the meeting text pasted in for this week and reconciles this week's oral reports against earlier commitments (fulfilled / partial or rescheduled / dropped / not mentioned),
           attaching two verbatim-checkable evidence snippets to each entry; turns decisions made in the meeting into check conditions on subsequent runs, and flags "said it was done, but the run isn't the one that was agreed on";
           when no evidence can be found it writes "not found," leaves blank any owner and date the original words did not give, and compiles everything into one post-meeting follow-up message
Unlike     Feishu Minutes, Otter, Fellow, ZoomMate (each meeting gets its own separate ledger entry, with status ticked by people or synced from a task system;
           their cross-meeting Q&A can answer "what was said last week," but they do not proactively and in batch propose status transitions and ask for confirmation, pending E2d testing),
           Littlebird (each week it extracts your commitments from that week's meetings and checks them against email and documents; its page does not say it uses later meetings to judge them, and its graduate-student page mentions only advisor meetings),
           Fabric (captures group-meeting decision logs, but does not compare them against runs),
           and pasting the notes into ChatGPT/Claude (starts from scratch every time, with no ledger; whether it proactively takes the previous decision as a constraint is pending E2-naive testing)
We have assembled  a deterministic comparison of decision constraints against run configurations; a trust foundation (verbatim verification of evidence snippets with refusal to answer, field-level "don't guess" for missing values, a persistent ledger);
           and a public cross-meeting reconciliation benchmark (including a strong Claude long-context control, comparisons with incumbent products, and the false-green rate)
```

### 6.2 Dunford one-liner

For graduate students in computational labs who have to account for "did you finish that thing from last week?" at every group meeting, BriefPilot is a **group-meeting commitment ledger**: other tools keep the books for each individual meeting and can look up old entries when asked, whereas it proactively uses what everyone said this week (and your runs) to reconcile last week's ledger, every entry opens to two evidence snippets, and when things don't match it says so plainly.

### 6.3 "Others already do this, so why are you building it?" — the 30-second version

> "Right, Feishu, Otter, and Fellow can all turn meetings into action items; Otter and Granola can also answer questions across meetings; Fellow has assignee claiming for AI-suggested items; Littlebird checks your commitments every week; Fabric can capture group-meeting decision logs; and the open-source Minutes can also match meeting conclusions to an open matter awaiting resolution. I'm not competing with them on 'generation,' nor on 'whether it can answer.'
> I only do the step between group meetings: how last week's commitments were described orally this week, and whether the rules set in the meeting were followed afterwards. Existing tools produce a fresh list for each meeting, with status ticked by people, or they wait for you to ask. I proactively and in batch reconcile this week's remarks against last week's ledger, attaching two evidence snippets to each entry; if the meeting decided 'everyone uses rank 32,' I go and check the subsequent runs.
> The question most worth asking is 'Couldn't you just paste four weeks of notes into Claude's long context?' I treated that as the strongest control and tested it: across __ paired comparison rows, I was wrong on __ rows where it was right, it was wrong on __ rows where I was right, and it judged items that were mentioned but not finished as 'fulfilled' __ times versus my __ times. (**Until the numbers are in, none of this gets said; and if the pre-registered k isn't met, I will say 'I falsified my own capability hypothesis, and the project becomes a benchmark plus workflow.'**)"

---

## 7. ERRC grid (Blue Ocean four actions)

| Action | Element | Relative to | Rationale |
|---|---|---|---|
| **Eliminate** | Recording, transcription, meeting-joining bots, live captions | Feishu, Otter, Fellow, Littlebird | Not core; the legal and social cost of recording consent (Granola class action 3:26-cv-07926-EMC, [Fact] 06 V14); the target university's GenAI policy |
| **Eliminate** | Task system / GitHub write-back, claiming UI, whole-group board | Fellow, Granola | Integration is not a moat (Fellow syncs to GitHub via Zapier, and several have MCP, [Fact] 06 V1–V2); claiming already exists in Fellow (AI-suggested items only, 07 F8) |
| **Eliminate** | "Data never leaves campus" as a selling point, outbound-traffic counter | Option 2 | The NUS ChatGPT Edu counterexample; W&B SaaS is self-contradictory; local tools are already crowded |
| **Reduce** | Full-text summaries, meeting highlights | All notes tools | An anonymous HN comment, "nobody will ever read those notes" (quote verified as accurate, incidentally checked in 06), **is only an anecdote**; its converse applies equally to this proposal: "nobody reads the reconciliation statement," so P-H7 / P-H12 need to be tested |
| **Reduce** | Number of new action items: soft commitments are entered but not pushed, and rejected proposals are not entered | Feishu, Tingwu, Claude | eval-kit pitfalls: π0, self-built benchmark |
| **Reduce** | Degree of automation: only propose transitions, never auto-close | Fireflies, Krisp "automatically assigns" ([Fact] 05 K4) | Weak counter-positioning |
| **Raise** | Evidence strength: dual verbatim-verified quotes + refuse to answer when verification fails | Feishu (item level), Fellow, Littlebird (no link to the original sentence seen, 07 F20, L5) | Cross-meeting inference is more prone to "filling in the blanks" than single-meeting extraction |
| **Raise** | Don't guess when missing: field-level three states, vague dates keep the original wording | All products (eval-kit E-H3/E-H4 untested) | Carries over `missing_owner` and `relative_date_without_anchor` from the old PRD |
| **Raise** | Coverage of advisors, collaborators, and ownerless items (a baseline requirement, not a differentiator) | Fellow (by assignee), Littlebird (defaults to "you," though you can prompt it to chase "what others owe you") | U5 (downgraded to baseline in v1.1) |
| **Create** | Cross-meeting **status-transition diff** (4 categories) | All | Main axis |
| **Create** | **Decision as constraint** + "fulfilled but conditions don't match" | All | The second beat; answers "it's just a prompt" |
| **Create** | "Not mentioned for N weeks" reminder + post-meeting follow-up message | All | Requires a persistent ledger |
| **Create** | Public reconciliation benchmark: crosslink accuracy, false-green rate, verbatim-quote rate, including a strong DIY control | All (05 K1) | The means of proof, and also the main evidence in the portfolio |

---
## 8. Strategic Positioning Map (Value Curve)

**Scale**: 3 = strong, 2 = medium, 1 = weak, 0 = none; "not seen" = not stated on the official page (does not mean absent); "?" = not verified. **Everything is based on official documentation and inference; no product was tested hands-on.** The BriefPilot column is a **design target**, not a measured result.

| Competitive factor | Feishu Minutes + Meeting Express | Otter | Fellow | Littlebird | ChatGPT/Claude with pasted minutes | **BriefPilot v2** | Basis |
|---|---|---|---|---|---|---|---|
| Recording, transcription, joining meetings | 3 | 3 | 3 | 2 | 1 | **0** | 07; ChatGPT Record is macOS only ([Summary] 07 A1) |
| Single-meeting summary and action item generation | 3 | 3 | 3 | 2 | 2 | **1** | 07 |
| Number of integrations | 3 | 3 | 3 | 2 | 2 (MCP) | **0** | 06 V1–V2 |
| Usability with mixed Chinese-English speech | 3 | 0 (lists only English, Spanish, French) | 1 (lists "Chinese"; mixed speech not mentioned) | 2 (Multilingual mode) | 2 [Inference] | **2** (target, untested) | 07 C11, F17, L10; eval-kit §2.2 |
| Item-level source traceability | 3 | ? | 1 (no link to the original sentence seen) | 1 (not seen) | 1 (may paraphrase) | **3** (dual verbatim-quote check) | 07 C7, F20, L5 |
| Carrying over unfinished items | 2 (weekly roll-up) | ? | 3 | 2 (three-state weekly report) | 1 (manual) | **3** | 07 C5, F4, L2 |
| **Automatically proposing the status of the previous meeting's items from what is said in the next meeting** | Not seen (may answer when asked? to be tested) | Not seen (AI Chat may answer when asked, pending E2d) | 0 (manual check-off) | **?** (extracts commitments from "this week's meetings" and checks them against email / documents; whether later meetings are used to decide status is not stated) | 2 (can do it, but from scratch each time, pending P-H1) | **3** | §5.1; P-H1, P-H3 |
| **Decision → constraint check / condition mismatch** | Not seen | Not seen | Not seen | Not seen | 1 (DIY, can be assembled with the W&B MCP) | **2** (second beat; frequency pending P-H6) | Plan 1 §3.2 |
| **"Not mentioned for N meetings"** | Not seen | Not seen | 1 (unfinished items keep being carried over) | ? | 0–1 | **3** | Requires a ledger |
| Field-level "don't guess when missing" | 1–2 ("can be added manually"; whether it leaves a field blank or fills it first is to be tested) | ? | 2 (takes effect only after accept) | 2 (skips vague maybes) | ? (depends on the prompt) | **3** | 07 C8, F8, L4; eval-kit E-H3/E-H4 |
| Recording commitments by advisors / partners / ownerless commitments | 2 | 2 [Inference] | 1 (by assignee) | 2 (can track "what others owe you") | 2 | **2** (passing line, lowered in v1.1) | 07 L1; Plan 2 §13 |
| Public accuracy figures | 0 | 0 | 0 ("human-level accuracy" with no number) | 0 | 0 | **3** (target) | 05 K1; 06 V7 |
| Data can stay on the local machine | 1 (private deployment goes to large customers, [Inference]) | 0 | 0 | 0 | 0 | **2** (provider is switchable; run data depends on SaaS vs. self-hosted) | Plan 2 §6.2 |
| Student pricing | Free tier ([Summary]) | ? | No education pricing | $15/month student price | Free or already paid | **Free (demo)** | 07 F18, L8 |

**[Inference] Shape of the curve**: BriefPilot is deliberately **below** all competitors on three factors (recording/transcription, single-meeting generation, integrations), and **above** competitors on six (cross-meeting status inference, decision constraints, not mentioned, evidence strength, don't guess when missing, public numbers). **The most dangerous column is "ChatGPT/Claude with pasted minutes"**: it already scores 2 on "automatically proposing status." If P-H1 shows it close to 3, this plan's curve is left with only two bumps: "ledger + evaluation."

---

## 9. Wedge and Expansion Path

```mermaid
flowchart LR
    W0["Wedge: the project owner's group<br/>2–3 students running experiments<br/>Single-user T1 post-meeting reconciliation"] --> W1["Bottle 1: adjacent computational groups<br/>Same department, shared GPU cluster<br/>Word of mouth + public evaluation"]
    W1 --> W2["Bottle 2: group-level mode<br/>Rotating note-taker maintains the group ledger<br/>PI reads the reconciliation sheet"]
    W2 --> W3["Bottle 3: university-industry joint labs<br/>Weekly operations meeting + consistency of external reporting<br/>RCA clauses, N-day no-objection"]
    W3 --> W4["Bottle 4: enterprise ML experiment review meetings<br/>Same W&B/Git toolchain"]
    W4 --> W5["Bottle 5: any team where the same people meet weekly<br/>e.g. vendor-side requirements weekly meetings"]
```

| Stage | Segment | Why adjacent | New whole product | Entry conditions (written down in advance) | Evidence level |
|---|---|---|---|---|---|
| **Wedge** | The project owner's group, 2–3 students, single-user mode | The project owner can reach them; the eval-kit is exactly this scenario | T1 post-meeting reconciliation + post-meeting follow-up questions | P-H1, P-H2, P-H8, P-H12 in §11 have not hit their abandonment lines; the IRB determination email has been answered, and **one-time informed consent from the whole group** is in place (if it cannot be obtained, record only the user's own commitments) | [Inference] |
| **Bottle 1** | Adjacent computational groups | Same group meeting structure, same toolchain | T2 pre-meeting reconciliation sheet + run table import | ≥2 of the wedge users voluntarily use it for 3 consecutive group meetings (P-H7) | [Inference] |
| **Bottle 2** | Group-level mode (rotating note-taker) | Same ledger, different operator | Multi-user read-only view, "export to PI" | Bottle 1 week-4 retention ≥50% (n≥6, 00/06 §9.1); 02/06 U-H05 (PI willing to read it weekly) is at least in the gray zone | [Assumption] |
| **Bottle 3** | University-industry joint labs (Hyundai-A\*STAR joint lab, AUMOVIO joint lab, etc.) | Same experiment commitments; **consistency of external reporting** (eval-kit M4 "the rank-32 main result needs to be rerun" → M5 still reports 71.2% to the partner); there is a paying party | A check before external reporting for "cited numbers that are pending rerun / outdated"; DESCA-style "draft → N-day objection window → default acceptance" | 02/06 U-H13: among 2 university-industry lab interviewees, ≥1 describes "promised the funder a deliverable, and afterwards the two sides understood it differently"; it has been established whether the RCA clauses restrict GenAI use | [Fact] job description (2020), original RCA clause text; [Assumption] demand |
| **Bottle 4** | Enterprise ML teams | Same W&B/Git | Private deployment notes | **See 02/06 U-H10**: if enterprise action items are already closed out in Jira/Linear and what gets lost is "the rationale for decisions," sell only "decision as constraint"; if they lose "who promised what" just as labs do, enter with the whole product | [Assumption] |
| **Bottle 5** | Vendor-side requirements weekly meetings, etc. | Same "last week's commitments, reported this week" | Requirements change ledger (the Plan E scenario) | ≥3 reachable vendor-side PM interviews | [Assumption] |

**Why the wedge is "single-user" rather than "note-taker"**: target-user research points out that the note-taker does the work while the PI benefits, so incentives are misaligned. In single-user mode, the person who does the work and the person who benefits are the same student: after the meeting he pastes the text once, and before the next meeting he gets a one-page "last week's progress" that can go straight into his slides. The group-level view is kept in the **data model** (the ledger is built per group), not in the **operator**.

---
## 10. Defensibility Analysis (What Can Be Copied, and How Fast)

### 10.1 Item by item: who can copy it, and how fast

| Component | Who is most likely to copy it | Estimated time [Inference] | Basis | What remains after copying |
|---|---|---|---|---|
| Cross-meeting status transition proposals (4 types) | **Users themselves with Claude's long context** (possible today); Littlebird; Feishu meeting digests; the Minutes community | DIY: **0 days** (P-H1 determines how well it works); Littlebird / Feishu: 1–3 months (one feature iteration) | 07 §0-7: vendors fill "feature present/absent" gaps about once a quarter; Minutes already has a closeout prototype | Ledger, evaluation |
| Dual verbatim-quote verification + refusal to answer | Any vendor | 2–6 weeks | Feishu already has item-level provenance | — |
| Field-level three states + post-meeting follow-up questions | Feishu (one step beyond "can be added manually"); a single prompt | 1 sprint; Plan 3 estimates a 3–6 month window | 07 C8 | — |
| Decision-as-constraint + condition mismatch | W&B itself (an "expected config" annotation); Littlebird connecting a W&B data source; DIY + W&B MCP | DIY: one afternoon (ad hoc assembly); vendors: 1–2 quarters (**small demand, most likely they won't build it**) | W&B `compare_runs_tool` ([Fact]) | Slot schema and judgment rules |
| Runs locally | Already saturated by open source | **The window is already closed** | Meetily (about 32.4k stars), Anarlog, Minutes ([Fact]) | None |
| History of the group's multi-week ledger | Cannot copy away **existing users' history**, but new users can switch at any time | Exists only after sustained use; zero Now | 7 Powers: nascent switching costs | Switching tools means losing "who said what in which week" |
| Public evaluation + failure-mode library + user-correction feedback loop | Technically anyone can build it; **incumbent vendors lack the motivation to publish** (publishing competitors is free advertising for them, and publishing their own UNKNOWN rate is admitting "it can fail to know") | 6–12 months; assumes continuous updates and two annotators | Plan 2 §6.3, Plan 3 §12 | A source of credibility, not a moat |

**[Inference] Overall judgment**:
1. **Not a single Power has taken shape yet.** There are three seeds: weak counter-positioning ("no evidence, no checkmark" runs against the "fully automatic" narrative), switching costs (ledger history), and process power (evaluation and the failure-mode library).
2. **The window is most likely to be closed not by Feishu or Otter, but by "users themselves + Claude's long context" and Littlebird.** The former exists today and is tested by P-H1; the latter is tested by P-H3.
3. **Window: 1–3 months at the feature layer, 6–12 months for evaluation and the ledger.** That is enough for a 2–4 week portfolio demo; **it is not enough for a "market gap" claim**. So externally, say only "I found a specific link in the workflow and validated (or falsified) it with numbers," not "nobody is building in this market."

### 10.2 New finding this round: Minutes (open source, local-first)

| Fact | Source ([Fact]: opened twice; the second time, during final revision, verbatim quotes were required, and the key sentences were checked: the tagline, MIT, 1.6k stars, "Capture, transcription, and storage run locally", the `action_items`/`decisions` fields, "spans two meetings a month apart", the closeout's "Turn one clear meeting outcome into a proposed closeout for one existing X1 coordination thread", "Ask the user to choose the X1 outcome", "The accountable participant must review and commit in X1", "doesn't prove settlement") |
|---|---|
| Minutes' tagline is "Your conversations. Your memory. Ready for the AI you use.", MIT license; capture, transcription, and storage run locally, but when a cloud AI is chosen, the authorized meeting content is sent to that provider; about 1.6k stars on GitHub | https://github.com/silverstein/minutes |
| Meetings are stored as Markdown; the YAML frontmatter has `action_items` (assignee, task, due, status) and `decisions`; the example answers "did it stick?", linking a February launch decision and a March reversal across two meetings | Same as above |
| The page **does not say** that it automatically tracks commitments across meetings, or automatically marks old action items as done | Same as above |
| `minutes-x1-closeout` skill: matches **one** `explicit` or `strong` meeting decision/commitment to **one** existing X1 coordination thread, with the outcome **chosen by the user** (resolved / escalated_elsewhere / deferred / no_longer_relevant), generates a draft, "The accountable participant must review and commit in X1"; and states "Meeting language that money was sent… doesn't prove settlement" | https://tessl.io/registry/skills/github/silverstein/minutes/minutes-x1-closeout |

**[Inference] Impact on this positioning**:
- **Weakens**: the **concept** of "using meeting statements to close out existing work" has already been built by someone, though only for a single item, with the user choosing the outcome, and dependent on X1. U1's distinctiveness must narrow to "**automatic, batch** proposal of transitions + multi-week not mentioned + decision constraints + public evaluation."
- **Corroborates**: its four outcomes (resolved / deferred / no_longer_relevant / escalated) are highly isomorphic with this plan's 4 transition types; its principle that "saying in a meeting that money was sent doesn't mean it is settled" is this plan's "saying it was fulfilled out loud ≠ evidence." This suggests the state model was not devised in isolation [Inference].
- **Adds a new DIY route**: Claude Code + Minutes MCP. Fold it into the P-H1 control group.
- **None of the three judges or four candidate plans found it**, which shows the project's competitor scan still has long-tail blind spots; scan GitHub and the MCP directory once more the week before the interview.

---
## 11. Make-or-Break Hypothesis List

**Rule**: Thresholds are fixed in advance. After a run, the only thing filled in is "holds / does not hold / gray zone"; the line is never moved (consistent with 02/06 §1.2 and eval-kit README §1). A **Make-or-break** entry marked "Kill" triggers the stop action as soon as the abandonment line is hit; one marked "Downgrade" only downgrades a single component. All entries are **[Assumption · to be validated]**.

**Numbering (v1.1)**: This table uses **P-H** throughout (positioning); eval-kit hypotheses are written **E-H**, and the 02/06 user-research package uses **U-H**. Mapping: P-H1 = E-H9; P-H2 ≈ E-H5; P-H11 ≈ E-H3/E-H4; the diary fields for P-H4/P-H5/P-H6 are in 02/06 §4.4 (D13, D14, F4), and the cost event for P-H5 = U-H03.

| # | Hypothesis | Make-or-break | Validation method | Success line | Failure line → stop action | Concrete experiment | Cost |
|---|---|---|---|---|---|---|---|
| **P-H1** | **Claude/ChatGPT long context + a prompt cannot do multi-hop reconciliation well** (especially from the 3rd and 4th meetings onward, items mentioned but only half done, and items whose conditions no longer match) | **Kill** | eval-kit layer 2 (`score_recon.py`), with these conditions: **E2** expert prompt (requires 4 categories, two verbatim quotes, not mentioned, and checking decision constraints); **E2-naive** plain prompt (no mention of constraints, verbatim quotes, or not mentioned; tests "proactivity"); **E2c** = E2 output + the same verbatim filter as this system; **E2d** cross-meeting Q&A in an incumbent product (pick one that allows uploads); **shorthand version of M3/M4**: someone other than the owner rewrites M3 and M4 as shorthand following real note-taking habits, then both this system and E2 are run again on the shorthand, reported separately. Same model `claude-opus-5-5`, 3 runs per setting. **Prompt iteration on both sides is capped at ≤3 versions, and only on the development set (M2–M3)**. DIY output is JSON, organized by script (`templates/expert_reconcile_prompt.md`) | **W1 shortcut** (DIY only): if **E2c** has `transition_accuracy` ≥20/23 **and** `fgr_mentioned` ≤1 item → there is no room left for a gap, and the failure line triggers directly. **Formal line** (end of W2): across all scorable rows (23 mentioned rows + 75 not-mentioned rows; needs_adjudication excluded), the paired discordant count of this system versus the "best DIY" (whichever of E2 and E2c has more correct rows) satisfies **b − c ≥ k** (k is written into `results-template.md` §6.1 in advance, default 5), **or** the `fgr_mentioned` count is lower by ≥3; **and** b ≥ c on the test set (M4–M5). The exact McNemar p is reported regardless, but significance is not a success condition (n is too small) | **b − c ≤1 and `fgr_mentioned` count difference ≤1** → **exit**: the "capability gap" narrative is void, and the work becomes "cross-meeting reconciliation eval set + DIY workflow recipe + failure-mode table". Between the two lines = gray zone: continue, but the demo does not claim "more accurate". **Side readings**: if E2-naive proactively mentions the M3 "rank 32" constraint or the stale number in M5 → "DIY won't do it proactively" is void; if E2c matches this system → "rewrite rate" no longer counts as a difference; if E2d, when asked, gives the status of each item with verbatim quotes → the Unlike section keeps only "proactive, batch + requires confirmation" | `score_recon.py` (`--compare --k`, `--verbatim-filter`, `--from-diy`); `gold/recon/transitions.gold.jsonl` (draft); `templates/expert_reconcile_prompt.md`; `results-template.md` §6.1 | **About 1.5–2 days** (including drafting and reviewing the transition gold labels, 3 DIY runs, and mapping confirmation; the earlier estimate of 0.5–1 day was an underestimate) |
| **P-H2** | **Competitors are weak at cross-meeting linking** (= eval-kit E-H5) | **Kill** (downgrade to narrowing) | eval-kit A-TTS: Feishu Minutes (first spend 30 minutes verifying whether the meeting digest can be tested weekly), Tongyi Tingwu; **ZoomMate** (if unavailable in the region, write "not tested: unavailable in region"); B-Text: ChatGPT and Claude baseline prompts. Whether Fellow can accept audio uploads is yet to be verified; if not, write "not tested (reason)" | `crosslink_accuracy` <30% for all tested competitors | Any competitor ≥50% → the main-axis selling point is void; narrow to "decision × run check + N meetings not mentioned + public evaluation", and state plainly in the positioning how much that competitor achieves | eval-kit README §1 E-H5, §3 step 1b, `results-template.md` §1.2b | 2–3 days (**from W2**, test only one first: whichever of Feishu or ZoomMate is available) |
| **P-H3** | **Littlebird does not use later-meeting remarks to determine the status of other people's commitments in multi-person group meetings**; Minutes does not do automatic batch reconciliation | **Kill** (downgrade to narrowing) | **Synthetic data**: first verify whether the student price accepts a university school email (the official site says "school email and student ID"); sign up for the student plan, and in meetings with **only yourself**, play M1–M5 weekly via TTS, let Littlebird record them, and read the Friday Promise tracker report. Real 1-on-1 and group-meeting tests wait until IRB determination and consent from all members. Minutes: install locally and see whether it can propose statuses on M1–M5 without the user selecting item by item | The weekly report does not cite later-meeting remarks to determine status, or only tracks "your" commitments; **added**: whether the weekly report cites **others'** remarks in group meetings — if it does not, the hypothesis holds; Minutes can only handle single items, with the user choosing the outcome | If either can do it → the differentiation is reduced to "decision × run check + public evaluation + mixed Chinese-English group-meeting scenario", the Unlike section is rewritten, and the 30-second answer names and acknowledges it | `results-template.md` §11 observation table; Plan 2 D6 early-warning signal table (re-check on the 1st of each month) | 2 weeks (passive waiting) |
| **P-H4** | **Verbal remarks are where status first appears** | **Kill** | 2-week diary item **D13** (02/06 §4.4 form 1): in this meeting, how many "earlier commitments" had their status updated verbally? How many of those did you learn of for the first time? Plus on-site note-taking observation of 2 group meetings in this lab (no audio recording) | In aggregate, ≥50% of status changes first appear verbally in the group meeting | <25% → the evidence source should switch to group chat / issues, this plan becomes "multi-source reconciliation", or the main axis is abandoned | 02/06 §4.4 D13; U-H02 on-site observation method | Layered onto the diary |
| **P-H5** | **Verbal closures are not written back, and not writing back has cost people something** | **Kill** | 48-hour follow-up **F4** (02/06 §4.4 form 2): "Of the statuses updated verbally at the last meeting, how many have now been written back to the original record?"; interviews PhD-Q8, PI-Q2; diary weekly review W1, follow-up F2 | Write-back rate ≤50% **and** ≥4/8 of students and postdocs can describe a specific cost event from the past 3 months (rerun, stale number in slides, being questioned by the advisor) and state its cost | Write-back rate ≥80%, **or** cost events ≤2/8 → the pain point does not hold (not writing back may be rational: nobody checks); if P-H6 holds, switch to "decision constraints" as the main axis; otherwise keep only the evaluation work | 02/06 §4.4 F4 + U-H03 | Layered onto interviews and diary |
| **P-H6** | **Experiment commitments or decisions with explicit conditions occur at least 1 per week**, and "condition drift" has actually happened | Downgrade (affects only the second beat) | ① 3 students who run experiments review **their own** shorthand or slides from the past 4 weeks (ask IRB first); ② diary **D14**: number of experiment commitments or decisions with explicit conditions in this meeting | Median per person-week ≥1, **and** cumulative real drift events across 3 people × 4 weeks ≥2 | Median <1, **or** 0–1 drift events → remove "condition mismatch" from the demo's second beat and move it to a footnote. **The stale-number check (F08b) is unaffected**, since it does not depend on the run table | Plan 1 H-D1; 02/06 §4.4 D14, §4.6 | 1–2 weeks (waiting on IRB) |
| **P-H7** | **A single user will use it weekly**: graduate students are willing to paste text once after a meeting and view a reconciliation sheet once before the next, they have text to paste, **and the whole group's consent can be obtained** | **Kill** | The W3 version goes to 2–3 students (at least 1 outside this lab) for 4 group-meeting weeks; `eval-kit/templates/h7_dogfood_log.md` records: reconciliation within 24 h, export before the next group meeting (system timestamp), "whether reminded" (**ticked by the participant themselves**), preparation time, **member consent rate**, and **where the post-meeting follow-up, once copied, was sent** | ≥2 people with binary retention (reconciliation within 24 h and export before the meeting) for 3 consecutive group meetings | 0 people in week 2 → ask "why not paste"; if the reason is "no text", add "2-minute spoken dictation of 3 lines of shorthand after the meeting" and retry for 2 weeks; if still ineffective, stop productization. If whole-group consent cannot be obtained → record only one's own commitments, and document this limitation | Plan 4 H-R6; reuse of 02/06 diary participants | 4 weeks |
| **P-H8** | **Human annotation agreement on the 4 transition categories is high enough** | **Kill** (prerequisite for any external number) | Two people independently annotate **all 23 labeled (thread, meeting) rows** (covering 26 of the 30 cross-meeting links) + a random sample of ≥20 not-mentioned rows; `score_recon.py --kappa` reports Cohen's κ and the bootstrap 95% interval; also double-annotate the strength and type of M1 and M3 per annotation-guide **§7** | Transition κ point estimate ≥0.6 **and** bootstrap lower bound ≥0.4; strength κ ≥0.6, type κ ≥0.7 | Line not met → merge into 3 categories (fulfilled / not fulfilled / not mentioned), **report only crosslink externally, not type accuracy**; until κ is met, make no external "we are better" claim | eval-kit `annotation-guide.md` §7; `score_recon.py --blank / --kappa` | 1 day |
| **P-H9** | (v1.1 **merged into the success line of P-H5**; no longer listed separately as "Downgrade") | — | — | — | — | — | — |
| **P-H10** | **"Never leaves the machine" is a hard requirement rather than a preference**; whether the target university has an approved cloud model | Downgrade (affects FAQ wording, **and also determines which model to use for dogfooding**) | In week 1, email the university IT / research integrity office; confirm whether this group uses W&B SaaS or self-hosted; diary D11 + interviews | No approved tool, **or** ≥3 interviewees describe a specific "refused / afraid to paste" incident | The university already has an approved tool → dogfood with the model from the approved tools that is in the same family as the demo; the FAQ changes to "compatible with university-approved models", and all "stays on campus" wording is removed | 02/06 U-H08; Plan 2 D2 | 1 week |
| **P-H11** | **Field-level three-state output adds value** | Downgrade (affects only whether G5 is a selling point or a baseline requirement) | eval-kit B-Text strengthened prompt; A-TTS competitors | The best comparison has `owner_abstain_rate` <50% or `due_abstain_rate` <60% (= the holding lines of E-H3 and E-H4), and a gap of ≥15 points | Competitors already "don't guess" → three-state output is downgraded to a baseline requirement and is not discussed in the demo | eval-kit E-H3, E-H4 | Same batch as P-H1 and P-H2 |
| **P-H12** | **(New in v1.1; a demand-side stop gate) People are willing to use reconciliation results**: classmates who receive a manually produced reconciliation sheet are willing to paste it into their own slides or weekly reports | **Kill** (W2 exit criterion) | **Zero-code concierge**: the project owner manually produces 2 reconciliation sheets each for 2 classmates (at least 1 outside this lab) (W1–W2; synthetic format + shorthand voluntarily provided by the classmates themselves; until IRB replies, use only the classmates' own commitments) | ≥1 of 2 people pastes one into slides or a weekly report at least once (self-reported by ticking) | **0/2 willing to paste → stop UI development and deliver only the evaluation work** (written into the W2 exit criterion) | `eval-kit/templates/h7_dogfood_log.md` §1 | About 1 hour each × 4 |
### 11.1 Weeks 1–2 Execution Order (v1.1 reduced-load version)

| Day | What to do | Output |
|---|---|---|
| W1 D1 morning | Send the IRB determination email (02/06 §6.3 template), and ask the target university's IT in the same email (P-H10); verify whether the Littlebird student price can be used with a university email (P-H3) | Email |
| W1 D1 | Review the transition gold draft (`gold/recon/transitions.gold.jsonl`, drafted by the model; the 4 needs_adjudication rows are adjudicated by the owner); write the winning count k into `results-template.md` §6.1 and sign with the date | Annotation A, k |
| W1 D1–D2 | Run the **P-H1 shortcut**: E2 × 3 runs → organize with the `--from-diy` script → E2c verbatim filter → scoring; E2-naive × 3 runs | E2 / E2c / E2-naive scores. If the failure line is triggered → switch to the "evaluation artifact" route the same day |
| W1 D2–D3 | Find 1 classmate to independently annotate the 23 rows + sample ≥20 not-mentioned rows (P-H8) | κ and bootstrap interval |
| W1 D3–D5 | Recruit 3–5 people for the diary study (at least 2 from outside this group); the form includes D13, D14, D15, F4; start the **P-H12 concierge** round 1 | Diary study started, concierge log |
| End of W1 | Decision meeting: P-H1 shortcut, whether P-H8 passes the line | One-page decision record |
| W2 | P-H2 tests only one vendor (Feishu or ZoomMate, whichever is available; first do a 30-minute feasibility check); P-H3 synthetic data begins; concierge round 2; **write the P-H12 gate into the W2 exit criteria** | `results-YYYY-MM-DD.md` |

**Why not write code first**: The three simulated judges (played by a model) unanimously held that the demand side is zero, and the most fatal attack (P-H1) can be tested in 1.5–2 days; the demand side gets stopped at the W2 P-H12 concierge gate. Spend the first week testing the cheapest and most fatal items; if they fail, the loss is smallest, and the evaluation assets left behind (annotations, DIY baseline, competitor outputs) can all be reused.

---

## 12. Point-by-Point Responses to the Judges' Strongest Objections

Status: **Addressed** (a concrete change or experiment exists) / **Partially addressed** (hedged but not eliminated) / **Cannot be addressed** (explicitly acknowledged).

### 12.1 Against the main axis (Option 4)

| # | Objection | Judge | Response | Status |
|---|---|---|---|---|
| O1 | "Claude long context + an expert prompt may be able to do this; H-R3 is killed in half a day, and what remains of the ledger is CRUD, not AI" | All three | Accepted. P-H1 uses the **strongest control group** (a Claude Project holding all the minutes + an expert prompt), tests **multi-hop** (M2→M5), and adds "resolution constraints," an item DIY won't proactively do. On day 1 we first test the DIY absolute score; if it is already close to the ceiling, we exit that same day. **If we exit, I concede that "the ledger is CRUD"**, and the artifact becomes an evaluation + workflow | Addressed (by falsification) |
| O2 | "Littlebird may already use later meetings as evidence, the page just doesn't say so" | All three | Accepted that "the page doesn't say so ≠ it doesn't do it"; moreover, the official site already says it "goes through the week's meetings". P-H3 tests this with synthetic data. The main differentiation is staked on "**multi-person group meetings** + the resolution × run check" (v1.1 no longer stakes on the "group-level ledger"; U5 has been downgraded to a passing bar). This round also newly found Minutes closeout, and U1 has been narrowed to "automatic, batch" | Partially addressed: cannot be ruled out before testing |
| O3 | "The demand side is zero: it only proved that the 'opening recap' is a ritual, not that 'verbal closure not written back' ever hurt anyone" | vc, bigtech | **Cannot be addressed; explicitly acknowledged.** There are currently zero interviews and zero diaries. P-H4, P-H5, and P-H9 are layered onto the 2-week diary study to test this, with failure lines fixed in advance | Cannot be addressed (pending experiment) |
| O4 | "Status changes may happen first in group chats, issues, or W&B" | vc, bigtech | Accepted. P-H4 specifically tests "where did you first learn of it"; if <25%, switch to "multi-source reconciliation" or give up. The run evidence in the second beat also partly covers the W&B case | Partially addressed |
| O5 | "The 7 transition types will most likely not reach κ 0.6" | All three | Accepted; already compressed to 4 types; if P-H8 fails, merge further to 3 types and do not report type accuracy | Addressed |
| O6 | "The 30 gold items are AI-drafted with self-planted markers, so you are setting and taking your own exam" | vc, bigtech | Accepted. ① P-H8 uses two annotators (vc requires at least completing the M2→M3 batch first); ② the ICSI English subset (CC BY 4.0); ③ try a public W&B project for semi-real reconciliation (**availability to be verified**); ④ gold labels, annotation guidelines, and prompts are all public; ⑤ report first the false-green rate, where we are most likely to look bad. **But this cannot be fully eliminated**: real group meeting data cannot be used before IRB and advisor consent | Partially addressed |
| O7 | "At the opening I ask one question, the student answers on the spot, and I don't look at the ledger" (PI) | target-user | Partially accepted: the PI is not the user. The user is the student preparing a report, who receives the pre-meeting reconciliation page and the post-meeting follow-ups. What would truly alarm a PI is "reporting stale numbers externally" and "not mentioned for N weeks"; these two beats are moved to the front of the demo. **But I cannot refute the claim that "the PI doesn't care about the ledger"**; 02/06 U-H05 will test whether PIs are willing to spend 5 minutes a week looking at it | Partially addressed |
| O8 | "The note-taker does the work and the PI benefits, so incentives are misaligned" | target-user | Accepted. The user is changed to the graduate student themselves (starting with a single user); the group level appears only in the data model; the note-taker mode is moved to Bottle 2 | Addressed |
| O9 | "Nobody in our group writes text minutes; everyone just puts up slides" | target-user | Partially accepted: inputs are expanded to slide notes, one's own 3-line shorthand, and semi-structured shorthand like `@exp dataset=… seeds=…`. **But if a group doesn't even have shorthand, this plan has no input**; this is specifically recorded among the failure reasons for P-H7 | Partially addressed |
| O10 | "Feishu meeting digests are only one sprint away from a 'progress on last time's action items' card; ZoomMate already writes that it turns action items into status updates" | bigtech | Accepted. The window estimate has been lowered to 1–3 months at the feature level (§10). The ZoomMate blog has been opened ([Fact], R10) and is closer to this plan than the old version stated; P-H2 adds ZoomMate to the real tests (if unavailable in the region, record it as "untested") | Partially addressed |
### 12.2 On the grafted Option 1 components

| # | Objection | Judge | Response | Status |
|---|---|---|---|---|
| O11 | "In W&B you can group by config and see rank16 in 30 seconds" | vc, bigtech, target | Partially accepted: a diligent student really can. What group-by doesn't know is "what was decided in the meeting"; this proposal's increment is linking decisions to runs. **Precisely because its standalone value is limited, it serves only as the second beat, not as the main axis** | Partially addressed |
| O12 | "The only frequency evidence is about 19% in synthetic data; real commitments mostly don't carry the full set of conditions" | all three | Accepted. P-H6 uses frequencies from real notes: if there are <1 per week or 0–1 drift events, the second beat is cut. The lead changes from "the condition slots of a single commitment" to "decision as constraint", because decisions are more explicit and cover more ground (suggestion from target-user) | Addressed (by falsification) |
| O13 | "The owner is not a W&B user, dogfooding depends on classmates, and it needs IRB approval" | all three | **Acknowledged.** The main axis (T1 post-meeting reconciliation) can be used by the owner personally (they attend the group meeting); the second beat relies on classmates, and the IRB email is sent on day 1; until consent is obtained, the demo uses only synthetic data | Partially addressed |
| O14 | "The rank16 in the magic moment is a landmine you planted yourself" | vc | **Acknowledged.** The demo states plainly: "this run table is one I built; it demonstrates the mechanism, not the frequency"; frequency cites only the real counts from P-H6 | Addressed (by disclosure) |
| O15 | "Claude + W&B MCP can be put together in an afternoon" | vc, bigtech | Accepted. DIY variant ① of P-H1 is exactly this; if the gap is <10 points, we exit | Addressed (by falsification) |

### 12.3 On the grafted Option 2 and Option 3 components

| # | Objection | Judge | Response | Status |
|---|---|---|---|---|
| O16 | "'Nothing leaves campus' is self-contradictory: W&B itself is SaaS; NUS has already rolled out ChatGPT Edu; '0 bytes egress' is a gimmick" | all three | Fully accepted. The counter and the "nothing leaves campus" selling point are deleted; the FAQ says only "meeting text can be processed on the local machine only; where run data lives depends on whether your group uses SaaS or self-hosting"; the NUS counterexample is raised proactively; P-H10 affects only the wording | Addressed |
| O17 | "Local 8–14B models lose accuracy on mixed Chinese-English extraction" | vc, bigtech | Accepted. Local mode is an option, not the default; D4 of Option 2 is no longer a make-or-break assumption | Addressed |
| O18 | "Field-level three-state is one system prompt plus one UI label" | vc, bigtech | Agreed, so it is only the trust foundation. P-H11 tests whether it is a selling point or merely table stakes | Addressed |
| O19 | "One of the hardest pieces of pain-point evidence comes from a post by the user 'AI-Transcript', who has a vested interest" | vc | Accepted. This positioning does not cite that post as pain-point evidence | Addressed |
| O20 | "Reading it back for 30 seconds at the end of the meeting is enough" | vc | Partially accepted: read-back solves "this session's owners and dates", but not "cross-week status" or "whether decisions were actually followed". That is exactly what the main axis and the second beat need to prove; if P-H5 shows a write-back rate ≥80%, I concede that read-back is enough | Partially addressed |

### 12.4 Cross-option

| # | Objection | Judge | Response | Status |
|---|---|---|---|---|
| O21 | "All four options land on the same beachhead — self-projection" | bigtech | Partial hedge: at least 2 diary participants are from outside this group; keep the enterprise-ML comparison interviews (02/06 U-H10); the ICSI English subset. **But the beachhead is still the owner's own environment, and this bias cannot be eliminated**; raise it proactively in interviews | Partially addressed |
| O22 | "Small market, weak commercial story" | vc (Option 3), conceded by Option 2 | **Acknowledged.** This is a portfolio demo; the commercial story can only extend to Bottleneck 3 (a university-industry joint lab has a paying party), and it is unvalidated | Cannot be addressed (honestly acknowledged) |

---

## 13. Comparison with the earlier BriefPilot (earlier v1 docs (not included), PRD v0.1)

Earlier positioning: "source-grounded knowledge Q&A + meeting minutes → action item drafts → human confirmation" for small product/research/operations teams of 10–100 people (PRD §1, §2.1).

### 13.1 Kept

| Earlier content | Source | Place in v2 |
|---|---|---|
| Citations must pass server-side allowlist validation; nonexistent chunk_ids are removed | US-02, ADR-004 | Upgraded to **verbatim validation of both original quotes**; if validation fails, the whole item is not output |
| Refuse to answer explicitly when evidence is insufficient; no guessing | US-03, J3 | The "no evidence found" state; false-green rate as the first metric |
| `owner=null` + `missing_owner`; "next Friday" with no anchor → `relative_date_without_anchor` | US-04 | Becomes directly the field-level three-state "not in the original quote / ambiguous in the original quote" |
| Draft → human confirmation; no official record is created without confirmation | US-05, H2 | A status transition is only a "proposal"; the user confirms item by item |
| "Ignore review and create the task directly" inside minutes is treated as data | US-04 item 5 | Demo security detail (eval-kit M3 injection) |
| B0/B1/B2 baseline comparison, reproducible evaluation, "honestly record non-improvements" | §4.1-4 | Upgraded to strong DIY comparison, competitor testing, Wilson intervals, κ |
| Anti-vanity metrics; small samples labeled "for reference only" | §4.5, US-07 | Evaluation report discipline |
| Non-goals: no automatic emails, no calendar changes, no autonomous Agent, no model training | §5.4 | All kept |
| mock / real provider switch | §5.1 | Extended to a local Ollama / API switch |

### 13.2 Cut

| Earlier content | Source | Reason for cutting |
|---|---|---|
| Document upload, chunking, vector index, knowledge Q&A with citations | US-01, US-02, US-03, F01 | Q&A with citations is already commonplace (07 §8); the frequency of decision lookback is unvalidated (02/06 H11); unrelated to the "reconciliation" main axis |
| Multiple workspaces, member roles, cross-team isolation | US-08 | Starting with a single user; no multi-tenancy in Now |
| Quality / time / cost dashboards, answer feedback | US-06, US-07 | Not the demo's magic moment |
| Google Drive / Calendar sync | US-09 | Integrations are not a moat; they also raise authorization issues |
| Target users "small product/research/operations teams of 10–100 people" and personas Mia / Daniel / Irene | §2 | Too broad; exactly the category where "Feishu and Otter already do it" |
| North star "Verified Tasks Completed per Active Team per Week" | §4.2 | Takes Q&A + tasks as its unit, which doesn't suit reconciliation |
### 13.3 Additions

| Addition | Description |
|---|---|
| Cross-meeting **commitment ledger** data model | Commitment ID, strength, owner (three-state), date (three-state), status history, two verbatim quotes |
| **4 types of transition proposals** + not mentioned for N weeks | Main axis |
| **Decision-as-constraint** + run-table import (CSV / local config; TensorBoard in v0.2) + deterministic comparison | Second beat |
| **Post-meeting follow-up message** | Side output |
| Tool-agnostic input (shorthand notes, slide notes, exports from other tools) | Lowers the cost of switching tools |
| New target users: graduate students in computational labs; mixed Chinese-English speech | §5.4 |
| New metrics | North-star candidate: **reconciliation transitions confirmed per active user per week** (counting only those with two verified verbatim quotes). Guardrails: false-green rate, verbatim-quote rate, number of unconfirmed status changes = 0 |
| New evaluation | Crosslink accuracy / precision, 4-type transition accuracy, false-green rate, not-mentioned recall, decision-constraint recall, strong DIY baseline |
| Monthly competitor early-warning signal table | Littlebird, Fellow, Feishu meeting digest, Minutes |

**[Inference] One-line comparison**: v1 was "a more trustworthy general-purpose assistant", with trustworthiness as the selling point. v2 demotes trustworthiness to a foundation and makes the single step of "cross-meeting reconciliation" the selling point. Most of v1's engineering design (validation, refusal to answer, confirmation gate) can be reused. What gets cut are the two heaviest parts: RAG Q&A and multi-tenancy.

---

## 14. Name

### 14.1 Whether to keep the name BriefPilot

| Dimension | Judgment |
|---|---|
| For keeping | Continuity of the project narrative: the repositioning from v1 to v2 is itself worth explaining |
| Against keeping | "Brief" suggests summaries and briefings, whereas v2 deliberately **reduces** summaries; "Pilot" suggests autopilot, whereas v2's selling point is "we don't tick the box for you". The name runs directly opposite to two actions in the ERRC table [Inference] |

### 14.2 New name candidates (all **without trademark or domain searches**; only 1 web search and 1 duplicate-name check were done)

| Candidate | Rationale | Risk |
|---|---|---|
| **① Meeting Ledger (the Chinese name 组会对账本; working English name Recon)** | The Chinese name is the category name, so interviewers immediately grasp "bookkeeping vs. reconciliation"; Recon is short for reconciliation | In English, "recon" also means "reconnaissance" and is a common word, so the chance of a name clash is high (not searched); the Chinese name is descriptive rather than brand-like |
| **② Closeout** | Emphasizes "closing out" rather than "claiming", which maps to the boundary between this proposal and Fellow; one search found no meeting app with the same name ([Summary]) | Minutes already has a skill called `minutes-x1-closeout` ([Fact], opened this round) with the same concept, so we may be seen as a follower; it is also a generic word |
| **③ LabLedger (group-meeting ledger)** | Clear niche; computational labs see at once who it is for | "Ledger" leans toward "bookkeeping" rather than "reconciliation", the opposite of the core metaphor; locks us into the lab segment, so a rename is needed when entering pins 3–5 |

**Abandoned candidate**: Tally (semantically the most accurate, as in "the numbers tally"), but tally.so is already a well-known form product ([Fact], homepage opened this round), so it is not recommended.

### 14.3 Recommendation

**At the project level, keep "BriefPilot v2" as the codename** (preserves continuity and makes it easy to explain "why v1 → v2 changed direction"). **For the external product name, use "Meeting Ledger" (组会对账本)**, with the demo title reading "BriefPilot v2 · Meeting Ledger". Leave the English name undecided for now. Once the P-H1 and P-H2 results are in and the direction is settled, run trademark and duplicate-name searches and choose between Recon and Closeout (choose Recon if Minutes' closeout skill gains mindshare).

**[Inference] Rationale**: In an interview setting, the Chinese name "对账本" (reconciliation ledger) does the positioning work directly (changing the frame of reference) and needs less explanation than any English brand word. An English name has no value if the direction is falsified, so spending time on it now is wasteful.

---

## 15. Source list (all accessed at the time of writing)

**Newly opened this round (WebFetch / WebSearch)**
1. Minutes (silverstein/minutes) GitHub — https://github.com/silverstein/minutes [Fact, checked verbatim]
2. Minutes `minutes-x1-closeout` skill page (Tessl registry) — https://tessl.io/registry/skills/github/silverstein/minutes/minutes-x1-closeout [Fact, checked verbatim]
3. WebSearch: "Closeout" app meeting action items — no meeting app with the same name found [Summary]
4. Tally homepage — https://tally.so [Fact: no-code form product]

**Cited from the four candidate proposals and 01_market-research/06, 07 (opened by the earlier agent)**
5. Fellow AI-Suggested Action Items — https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items
6. Fellow Meeting Briefs — https://help.fellow.ai/en/articles/9773836-meeting-briefs
7. Fellow Carry incomplete items forward — https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward
8. Fellow Action item page — https://help.fellow.ai/en/articles/4144380-action-item-page
9. Fellow × GitHub — https://fellow.ai/integrations/github
10. Fellow MCP server — https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server
11. Fellow Supported languages — https://help.fellow.ai/en/articles/8514401-supported-languages-for-ai-note-taker
12. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
13. Littlebird Graduate students — https://littlebird.ai/for/graduate-students
14. Littlebird Pricing — https://littlebird.ai/pricing ; Teams — https://littlebird.ai/teams
15. Littlebird Multilingual — https://littlebird.ai/use-cases/knowledge-and-education
16. Circleback, How to track meeting action items — https://circleback.ai/how-to/track-meeting-action-items
17. Feishu intelligent meeting minutes — https://www.feishu.cn/content/article/7577317993749269689
18. Feishu AI breakdown of action items — https://www.feishu.cn/content/article/7600354912756681687
19. Zoom AI assistant — https://www.zoom.com/en/products/ai-assistant/ ; ZoomMate getting started ([Fact], opened at the time of writing, verbatim quote in R10) — https://www.zoom.com/en/blog/zoommate-getting-started/
20. Otter supported languages — https://otter.ai/mp3-to-text
21. W&B official MCP server — https://github.com/wandb/wandb-mcp-server
22. Meetily — https://github.com/Zackriya-Solutions/meeting-minutes
23. Rashid Lab meeting leader guide — https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html
24. MIT Cahoy advising policy — https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf
25. The target university's Position on the Use of GAI in Research — (university page; link removed)
26. NUS ChatGPT Edu coverage (media) — https://www.edtechinnovationhub.com/news/the-national-university-of-singapore-brings-chatgpt-edu-and-codex-to-all-students-faculty-and-staff
27. Granola class-action coverage (3:26-cv-07926-EMC) — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
28. Gundersen & Kjensmo, AAAI 2018 — https://mlanthology.org/aaai/2018/gundersen2018aaai-state ([Summary]: the original AAAI page was blocked and the PDF on the author's homepage returned 404; page and table numbers still to be verified)
29. Wiley ExplanAItions 2025 — https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx
30. ICSI Corpus (CC BY 4.0) — https://groups.inf.ed.ac.uk/ami/icsi/
31. Hacker News discussion ("nobody will ever read those notes", a single anonymous comment, anecdotal level) — https://news.ycombinator.com/item?id=48823024
32. DESCA Horizon Europe v2.1 — https://www.desca-agreement.eu/assets/helmholtz_gemeinschaft/user_upload/Brussels_Office/DESCA/2026/20260228_DESCA_HorizonEurope_.2.1_with_elucidations_final.pdf

**Added in the v1.1 closing revision (accessed at the time of writing)**
34. Littlebird Promise Tracker (reopened; verbatim: "your meetings, your inbox, your calendar, and what was on your screen" and "goes through the week's meetings, extracts the commitments you made") — https://littlebird.ai/routines/promise-tracker
35. Littlebird Graduate students (reopened: only mentions advisor meetings, not lab / group meetings) — https://littlebird.ai/for/graduate-students
36. Littlebird Pricing (reopened: student pricing says "Apply in the app with your school email and student ID", with no mention of .edu) — https://littlebird.ai/pricing
37. Fabric Academic labs (reopened) — https://fabric.so/teams/academic-labs
38. Minutes GitHub (reopened, checked verbatim) — https://github.com/silverstein/minutes ; closeout skill — https://tessl.io/registry/skills/github/silverstein/minutes/minutes-x1-closeout
39. Meetily GitHub (stars rechecked: about 32.4k) — https://github.com/Zackriya-Solutions/meeting-minutes

**Methodology**
33. April Dunford's *Obviously Awesome* (summary), Blue Ocean ERRC, Moore's beachhead, 7 Powers — see the source list in `00_pm-skills/03`

**Files within the project**: `03_positioning/01_candidate-proposals_1–4`, `02_scoring-review-log`; the earlier v1 docs (not included); `02_user-research/06`; `05_demo-plan/eval-kit/` (README, scoring.md, gold/decisions_hypotheses.md, meetings/plain/M1–M5).

---
## 16. Confidence Notes for This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| Choose Option 4 as the main thread + Option 1 as the second beat + Option 3 as the foundation | **Medium** | The rationale is "fastest to falsify, and the evaluation assets can be reused if it fails"; the repair suggestions from the simulated judges (played by a model) converge. **Not chosen because it scored first**: the total-score gap of 0.23 is within noise |
| "Using the next meeting's discussion to proactively, in batch, propose status updates for the previous meeting" in multi-person group meetings was not found within the search scope | **Medium-low** | Minutes closeout already has a single-item version where the user picks the outcome; the ZoomMate blog already mentions "revisit… unresolved action items" and generating status updates from decisions; Littlebird pulls commitments from the week's meetings every week; R12, an incumbent product, can answer passively; the long tail of products has not been fully scanned; **zero hands-on testing** |
| The need genuinely exists (P-H4, P-H5, P-H9) | **Assumption** | Zero interviews, zero diaries |
| DIY long-context cannot do multi-hop reconciliation well (P-H1) | **Assumption; the one most likely to be overturned** | All three judges tend to think DIY would come close |
| "A decision is a constraint" is something DIY won't do proactively | **Assumption** | The target user's argument; untested |
| Competitor scores on the strategic positioning map | **Low to medium** | All drawn from official documentation and inference, zero hands-on testing; the "not found" cells are the most likely to be wrong |
| Window of opportunity: 1–3 months (features) / 6–12 months (evaluation and ledger) | **Inference** | Carries over the observations on catch-up speed from 07 §0-7 |
| Name suggestions | **Low** | No trademark or domain search done |

**The most important reminder**: this positioning was chosen because it is the one that can be **explained most clearly and falsified fastest**, not because its underlying need has been confirmed. In Week 1, write no code; first run P-H1 (the Day 1 shortcut), P-H8, and P-H2, and kick off P-H3 and the diaries. If P-H1 hits the abandonment threshold, §5–§9 of this document are all void, and the deliverable becomes "a cross-meeting reconciliation evaluation + a DIY workflow", which is also a legitimate AI PM conclusion.
