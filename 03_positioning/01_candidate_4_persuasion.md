---
title: "Positioning Candidate 4 (Persuasion Perspective): The Group-Meeting Commitment \"Reconciliation Ledger\" — Automatically Reconcile Spoken Updates in the Next Group Meeting Against the Commitments from the Last One"
status: draft-candidate (one of the Round 2 positioning candidates, awaiting scoring in the 03_positioning review; zero interviews, zero hands-on competitor testing)
perspective: persuasion (client/interviewer persuasiveness first + AI PM portfolio value)
sources_count: 37
sources_count_method: number of unique URLs in the sources section (recounted at wrap-up; original value 34)
---

# Positioning Candidate 4 (Persuasion Perspective): The Group-Meeting Commitment "Reconciliation Ledger"

> **In one sentence**: Feishu Minutes, Otter, and Fellow help groups "keep the books" — every meeting produces a fresh set of action items. BriefPilot only does "reconciliation": when people say things like "halfway done," "fixed," or "not doing that for now" at next week's group meeting, those statements are automatically reconciled against last week's commitments. Every reconciliation entry carries two verbatim quotes and is confirmed by the note-taker with one click.
>
> **Labeling rules** follow the rest of the project: **[Fact]** has a source URL and the original page was opened (pages newly opened in this document are marked "opened this round"; pages cited via earlier files carry the file number); **[Summary]** means only the search snippet was seen; **[Inference]** is derived from facts; **[Assumption·to be validated]** requires interviews or experiments. All official sources were accessed at the time of writing.
>
> **Inputs to this document**: Fully read `00_pm-skills/03`, `01_market-research/05, 06, 07`, §0, §3.2–§3.3, and §5 of `02_user-research/05`, §0, §1.5, §4.5, §7.3–§7.4, and §8.3 of `00_pm-skills/06`, plus `05_demo-plan/eval-kit/README.md`, `gold/decisions_hypotheses.md`, and `meetings/M3`. The remaining files (00/01, 02, 04, 05; 01/01–04, 08; 02/01–04, 06) were read for conclusions, key tables, and sections relevant to this proposal, not line by line. This round also used WebFetch to open 4 official pages (two Fellow help articles, Littlebird Promise Tracker, Circleback how-to) and ran 1 WebSearch.

---

## 0. Conclusion First

1. **Recommended option**: a brand-new combination, labeled "Option G: Group-Meeting Commitment Reconciliation." It absorbs Option A's trust foundation (G2 verbatim-quote verification, G3 no-guessing on missing information and tiered strength), uses Option C's computational lab as the beachhead, and uses Option F/G1's evaluation as the proof mechanism, but **its main axis is neither A nor C**.
2. **The small unmet need (pinned down to scenario × step)**:
   - **Scenario**: the **weekly group meeting** of a computational lab. The same group meets every week, and last week's commitments are reported on this week.
   - **Step**: the "review of last week's action items" at the start of the group meeting, and the step after the meeting where the review results are written back into the record.
   - **Current state**: the "status update" in this step happens **verbally** ("the WidowX group hasn't run yet," "the gripper was fixed last Friday," "co-training is on hold"). Existing tools either treat the next meeting as a brand-new meeting and extract a fresh list of action items from scratch, or wait for people to tick items off manually, or wait for the task system to sync back. As a result, verbal closures are never written back to last week's commitments, and the ledger becomes inaccurate by week 2–3.
   - **Gap**: within the scope of this round's search, we did not see any product publicly state that it can "use speech in the next meeting as evidence to automatically propose status transitions for the previous meeting's commitments" (see §2.3, [Fact: not seen within the search scope], which does not mean it doesn't exist).
3. **Why it is the best option from a persuasion standpoint** (§1, §2.2):
   - **Explainable in 5 minutes**: the "keeping the books vs. reconciling the books" metaphor is instantly understood by Chinese-speaking interviewers and pulls the product out of the "meeting minutes" category.
   - **Difference visible live**: given the same week-2 minutes, Feishu/Claude produces a **new** action item list, while BriefPilot produces a **diff against last week's list**. This is a difference in shape that is visible at a glance, not "we are a bit more accurate."
   - **Falsifiable**: the eval-kit already contains gold labels for 30 cross-meeting links and the `crosslink_accuracy` metric (H5), so no new experiment is needed.
   - **Works for a single person**: the note-taker can use it alone by pasting in the minutes, with no need for the advisor or other members to sign up. This directly answers the cold-start follow-up question (00/06 §1.5).
   - **High portfolio value**: it naturally requires talking about evals, refusal to answer, human-in-the-loop, injection defense, and "what we gave up," exactly the topics an AI PM interview most wants to hear.
4. **Honest boundaries**:
   - This need **has no user evidence yet**. The existing evidence only shows that "reviewing last week's action items at the start of the meeting" is a practice written into lab handbooks and advisor policies ([Fact]); it does not show that "verbal closures not being written back" is actually painful ([Assumption·to be validated]).
   - The biggest make-or-break risk is that "pasting two weeks of minutes into Claude and saying 'update the status item by item against last week' also works" (§8 H-R3). **If testing proves it can, this option must be downgraded to an "evaluation + workflow" narrative**; the exit criteria are written in §8.

---

## 1. Perspective and Evaluation Criteria: What a Knowledgeable Interviewer Wants in 5 Minutes

[Inference] I take the position of a "big-tech AI PM interviewer / knowledgeable client" and break persuasiveness into 6 criteria, against which all later options are compared:

| # | Criterion | The interviewer's question | Why it matters |
|---|---|---|---|
| P1 | **Distinguishable in one sentence** | "How are you different from Feishu Minutes?" Can you answer clearly in 20 seconds, without degree words like "more accurate" or "better"? | A difference of degree gets knocked down by "they'll catch up in the next version"; a difference of shape is memorable (00/03 §2, value curve: "different in shape, not just higher overall") |
| P2 | **Comparable live** | In the demo, can competitor output and your output be placed side by side, with the difference visible to the naked eye? | 00/03 §11 step 7, "The demo does only the wedge step"; 05 §5, "Compress the demo into one magic moment" |
| P3 | **Survives Round 2 evidence** | Has your selling point already been claimed by Fellow, covered by Littlebird's promise checking, or knocked out by Feishu's meeting express digest? | Pattern in 06 and 07: gaps defined by "feature present or absent" get filled roughly once a quarter |
| P4 | **Falsifiable, with numbers** | "Do you have data?" | 06 §8, item 1 under "Questions that would stump us now"; 08 §5.1 specifies what must not be said |
| P5 | **Honest about cold start** | "Doesn't this require everyone to be in the system?" | 00/06 §1.5, come-for-the-tool |
| P6 | **Portfolio signal** | Can this project demonstrate core AI PM abilities: evaluation, trust design, trade-offs, compliance? | This project is also a portfolio project |

**Deliberately left out of the criteria**: market size and willingness to pay. They are not unimportant, but for a 2–4 week portfolio demo, interviewers care more about "how you found and validated one point," and the business story only needs to honestly answer "who pays" (00/06 §7.3, step C: "I answer by 'proving I can find and validate an unmet need,' and talk about the business last").

---
## 2. Derivation

### 2.1 First, delete: what can no longer be a selling point after Round 2

| Can no longer be claimed | Evidence | Source |
|---|---|---|
| Meeting → action items, citations/source-text traceability, human confirmation, no bot, no training on user data | Feishu "supports tracing action items back to the original meeting text"; tl;dv "for review before sending"; Granola and Notion have no bot | 05 §0-1; 07 C7 |
| Carrying unfinished items across meetings (binary) | Fellow offers Always / Never / Ask me per series; Feishu meeting digest; ZoomMate "weekly action items" | 07 F4, C5, Z3 |
| Claiming by the named person | Fellow: "any assignee can accept or dismiss it" (page dated 2026-10-01; opened again this round to confirm) | 07 F8; opened this round |
| GitHub/Jira/Linear integration, MCP | Fellow syncs two-way with GitHub via Zapier; Circleback, Read, Otter, and Fellow have MCP | 06 V1, V2; 07 F13, F14 |
| Commitment checking: "did it get done" | Littlebird Kept / In progress / Needs a note, compared against "the email that went out, the document that shipped" | 07 L2, L3; opened this round |
| The graduate-student scenario itself | Littlebird's graduate student page "lists what you promised your advisor" | 07 L9 |
| Weekly reports / weekly summaries | Feishu meeting digest, ZoomMate, Fabric PI digest, pasting into ChatGPT | 07 §8 G10 |
| "First public action-item benchmark" and "first research group meeting dataset" | ICSI (since 2005), AMC-A, MUG tracks | 08 §0-1, §0-2 |

[Inference] After the deletions, 07 §8.1 sums up the remaining gaps in three categories: **research semantics** (five-valued outcomes, W&B/Git evidence), **a bilateral-confirmation advisor ledger**, and **a public benchmark**. This proposal finds a fourth category beyond these three: **the evidence source for cross-meeting "status updates"**. 07 does not break this out as its own column; see §2.3.

### 2.2 Running the existing candidates through the 6 persuasiveness criteria

> Scores run 1–5 and are the researcher's subjective judgments, used only for ranking; a gap of ≤3 counts as the same tier.

| Candidate | P1 Distinguishable in one sentence | P2 Comparable live | P3 Survives R2 | P4 Falsifiable | P5 Cold start | P6 Portfolio | Total | Main reasons for point deductions |
|---|---|---|---|---|---|---|---|---|
| A Verifiable, claimed commitment layer | 2 | 3 | 1 | 4 | 2 | 4 | 16 | Claiming is already covered by Fellow, and traceability by Feishu; only a difference of degree remains |
| B PhD student 1-on-1 ledger | 3 | 2 | 2 | 2 | 1 | 3 | 13 | Littlebird's graduate student page is almost the same name; advisor confirmation needs both parties present; the leverage of Singapore's institutional setup is unverified (07 U7) |
| C Commitment–outcome–evidence (five values + W&B) | 3 | 3 | 3 | 2 | 4 | 4 | 19 | Five-valued outcomes have no user evidence (06 W10); "Granola MCP + W&B MCP + Claude" can be built DIY (02/05 §3.2); the W&B integration is hard to grasp at a glance in a demo |
| D Accurate Chinese-English terminology | 3 | 4 | 3 | 4 | 4 | 3 | 21 | Zero first-hand Chinese complaints (06 W4); ASR vendors catch up quickly; the selling point disappears with text input; leans toward ASR engineering for an AI PM |
| E Outsourced-vendor requirement-change ledger | 4 | 3 | 4 | 1 | 1 | 3 | 16 | No material from owners, so dogfooding doesn't hold; weakest evidence |
| F Open-source issue write-back | 3 | 3 | 4 | 5 | 3 | 3 | 21 | Nobody wants it; can only serve as an evaluation testbed |
| U5 Ladder: compute-oriented group → university–industry joint lab (review packet + objection window) | 3 | 2 | 4 | 1 | 2 | 4 | 16 | Can't be explained in 5 minutes (milestones × commitments × evidence × objection window); zero evidence of confirmation from the company side |
| **G Group-meeting commitment reconciliation (this proposal)** | **5** | **5** | **4** | **4** | **5** | **5** | **28** | Zero evidence of pain in demand; pasting into Claude may come close (§8) |

[Inference] D and F are strong on "falsifiable", but neither can answer "who would use it every week". G's advantage is concentrated in P1, P2, and P5, which are exactly the three that get tested first in a 5-minute interview.

### 2.3 Key finding: existing tools all "keep the books"; nobody "reconciles" using the next meeting

Taking the capabilities verified in 07, plus the 4 pages newly opened this round, and re-sorting them by "**who updates the status of the previous meeting's commitments, and based on what**":

| Product | Who updates the status of the previous meeting's commitments, and what is the evidence | Source (accessed at the time of writing) |
|---|---|---|
| Fellow | A person manually ticks complete or archived; carry-over to the next meeting is "one-time", and "if you uncheck something later, it won't be reflected retroactively"; the pre-meeting brief is "generated solely from the last meeting's recording", so it **only summarizes the previous meeting**; after opening the page this round, I confirmed it **does not state** that it checks the previous meeting's action items against the current or next meeting's content; the only completion-related sentence in the AI-suggestion article is "Marking an AI-suggested action item as complete also accepts it automatically", i.e. a **manual action** | [Fact] 07 F4, F11; opened this round: https://help.fellow.ai/en/articles/9773836-meeting-briefs , https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items |
| Fellow × GitHub | Flows back from GitHub issue status | [Fact] 07 F13 |
| Littlebird | Every Friday it automatically compares against "what actually happened", with examples all being "the email that went out, the document that shipped, the message that never did"; the page says it **extracts** commitments from "the week's meetings", but **does not say** whether statements in later meetings can serve as evidence of fulfillment | [Fact] opened this round: https://littlebird.ai/routines/promise-tracker |
| Circleback | Its own how-to says "During the next meeting, reference incomplete items from previous sessions", and completion status is "they update the status in your project management system", i.e. **manual review in the next meeting, then manual update in the task system** | [Fact] opened this round: https://circleback.ai/how-to/track-meeting-action-items |
| Feishu | The meeting digest generates an "action item report" from "the past week's smart minutes content"; owners "receive reminders"; everyone "can view task status on the minutes page". It **does not state** that the next meeting is used to close out the previous one | [Fact] 07 C5, C9, C10 |
| ZoomMate | Can identify unclosed Jira issues and "turn action items into status updates" (**summary only**) | [Summary] 07 Z6 |
| Teams Facilitator | Tasks are bound to "that meeting instance"; cross-meeting carry-over is not described | [Fact] 07 T3 |
| General search | 1 WebSearch ("AI meeting assistant automatically marks previous action items complete based on next meeting discussion"); the results contain only carry-over, pre-meeting review, and manual updates, with nothing on "inferring completion from the next meeting" | [Summary] WebSearch this round, see sources 30–31 |

**On the demand side, "open by reviewing last week's action items" is a fixed step written into handbooks and policies**:
- [Fact] The Rashid Lab group meeting facilitation guide: at the start of the meeting "Review last week's action items", at the end "Read back action items" and "confirm assignees and due dates", with notes stored in GitHub Discussions and under the repository's `meeting-notes/` (07 P7).
- [Fact] MIT Cahoy's advising policy: after the meeting, students send the notes and action items to everyone, and at the next meeting they are reviewed item by item (05 G5; U1 §0-2).
- [Fact] Loughborough Co-Tutor records must include "actions arising from this meeting or that are still outstanding from previous meetings" (07 U3).
- [Fact] Circleback's own how-to also treats "reviewing in the next meeting" as a recommended practice (opened this round).
- [Fact, personal blog] Lilach Bullock suggests spending 90 seconds at the start of a meeting on review (05 G11; this is rule-of-thumb advice).

**[Inference] Put the two sides together and the gap appears**: everyone does the review step, but the **result** of the review is produced verbally, and then there are only two paths: wait for someone to update the task system by hand, or be washed away by the next "new action item list". The tools' unit of modeling is "one meeting", but status changes happen "between two meetings", and the evidence sits in what is said in the next meeting. The eval-kit synthetic data makes this phenomenon very concrete: the first line of M3 is "Did that baseline run last week?" and the answer is "Half of it ran" (eval-kit M3 [00:00:03]–[00:00:08]).

**This neatly sidesteps the three conclusions in 07 that are already covered**:
- It is not "carrying unfinished items over" (Fellow already has that), but "**after carrying over, automatically proposing its new status from this week's statements**";
- It is not "claiming" (Fellow already has that), but **closing out**;
- It is not "checking emails and documents" (Littlebird already has that), but **checking the meeting itself**. In a lab, the most common evidence for "did it get done" is the report given at next week's group meeting, not an email [Inference].
### 2.4 Pinning Down the "Small Slice" Precisely

| Element | Content |
|---|---|
| Who | The **note-taker or facilitator** of a computational lab's weekly group meeting (a senior PhD student, postdoc, or lab manager, often on rotation), in a group of 5–12 people |
| When | The 5–10 minute "last week review" at the start of each weekly group meeting, plus a 10-minute "write-back" after the meeting |
| How it's done today | Open last week's notes (Google Doc, Feishu, Notion, GitHub Discussion) and ask about each item by name; after the meeting, update statuses in the notes or in an issue from memory, or don't update them at all [Inference, to be verified by diary study] |
| Where it breaks | Verbal closures ("Got halfway, will finish before Sunday," "Not doing it for now because storage is short," "Submitted, the school hasn't approved it") are never written back to last week's commitment; the advisor's own commitments, ownerless items, and soft commitments are the most likely to fall through [Assumption, to be verified; can be tested with eval-kit H2 and diary entries D7/F1] |
| What BriefPilot does | Paste this week's notes → the system pairs every "status report" sentence this week with last week's ledger, item by item → produces **status transition proposals**: fulfilled, partially fulfilled, rescheduled (with the new date anchored), dropped (with the reason quoted verbatim), claimed by someone, still open, not mentioned → each proposal carries two pieces of evidence, "last week's quote ↔ this week's quote", and the server verifies that the quotes really exist → the note-taker confirms or edits each one |
| What it does not do | No audio recording, no transcription, no bots, no task-system sync, no judging of experimental conclusions on anyone's behalf |

---

## 3. Dunford's Five Elements

### 3.1 Competitive Alternatives (What Would the Note-Taker Do Without BriefPilot)

| Alternative | How it handles "last week review + write-back" | Its gap at this step | Evidence level |
|---|---|---|---|
| **Do nothing** (rely on memory; open with "Did everyone get done what they said they would last week?") | The facilitator calls on people from memory; no one writes anything back | Commitments that nobody is asked about quietly disappear, and the advisor's own commitments are the ones nobody dares to ask about | [Assumption, to be verified] (U6 H01, H06) |
| **Manual notes + reading out action items at the start** (Rashid Lab style) | Read last week's notes, ask about each item, edit by hand after the meeting | Effective but time-consuming, and depends on the note-taker's discipline; edits leave no evidence of why they were made | [Fact] the practice exists (07 P7); [Assumption] its cost and how well people stick to it |
| **GitHub Issues / Projects as the group's task board** (COMET, Durrant style) | Drag cards on the board during the meeting | Covers only hard tasks that were turned into issues; soft commitments, advisor commitments, and the reasons behind "not doing it for now" don't make it in | [Fact] the practice exists (05 sources 30, 31); the gap is [Inference] |
| **Feishu Minutes / Tongyi Tingwu + meeting digests** | Action items are generated automatically for each meeting; the digest summarizes them by week | Each meeting produces a fresh list; nothing says "use the next meeting to close out the previous one"; labs outside mainland China may not use Feishu | [Fact] 07 C5, C9; the gap is [Fact: not stated on the page] |
| **Fellow** (recurring meetings + auto carry-over + claiming) | Incomplete items are carried over automatically into the next agenda; people tick them off manually in the meeting | Status updates depend on people ticking boxes; the brief looks only at the previous meeting; rejected items are deleted permanently; behavior on mixed Chinese-English speech within one meeting is unknown | [Fact] 07 F4, F5, F9, F17; opened this round |
| **Littlebird** (individual edition for grad students) | A report every Friday automatically: Kept / In progress / Needs a note | The evidence sources stated are email and documents; by default it tracks only "your own" commitments; the page does not say whether follow-up meetings are used as evidence | [Fact] opened this round; 07 L1, L3 |
| **Pasting two weeks of notes into ChatGPT / Claude** | The user writes their own prompt: "Here are last week's and this week's notes; check whether last week's items got done" | It works, but starts from scratch every time, has no persistent ledger, may paraphrase the quotes, and has no published accuracy; judging "not mentioned" requires a complete ledger | [Inference]; **this plan's number-one rival** and must be tested empirically (§8 H-R3) |
| **Meeting-tool MCP + Claude assembly** (Fellow/Granola MCP reads action items, Claude reasons over them) | In theory you can assemble "read last week's action items + read this week's transcript + judge status" | Write-back is still manual; Fellow's MCP write tools cover only the agenda (07 F14); data has to pass through the cloud | [Fact] the MCP exists; the effectiveness of the assembly is [Inference] |
| **Supervisor Meeting Brief** (Chrome extension, no AI) | Manually maintain a "From last meeting" panel | Entirely manual; 0 ratings | [Fact] 07 P4 |

**[Inference] Ranking of real rivals**: ① doing nothing or reading items out by hand (this is "No decision," the biggest rival according to Dunford, 00/03 §1.4); ② pasting into Claude; ③ Fellow; ④ Littlebird. Feishu and Otter are, at this step, Category B competitors (overlapping scenario, different approach, 00/03 §9.2).

### 3.2 Unique Attributes (What the Alternatives Lack, or Don't State on Their Pages)

| # | Attribute | Corresponding gap | Is it "ours alone"? |
|---|---|---|---|
| U1 | **Uses what is said in the next meeting as evidence to automatically propose status transitions for the previous meeting's commitments** (7 kinds of transitions: fulfilled, partial, rescheduled, dropped, claimed by someone, still open, not mentioned) | §2.3 | [Fact: no public description found within the search scope]; Littlebird and ZoomMate are the two most likely to already have it or to have it soon |
| U2 | **Dual-evidence transition card**: every transition carries both "the quote from last week's commitment + the quote from this week's closure", and the server verifies that both quotes appear verbatim in the input; if verification fails, nothing is output | The cross-meeting version of G2 | Single-meeting traceability already exists in Feishu; "two pieces of evidence + refuse to answer on verification failure" has not been seen [Inference] |
| U3 | **"Not mentioned" and "still open" are first-class statuses**: commitments or questions that nobody has raised for N consecutive weeks surface (for example, the data card suggestion in M2, which nobody mentioned again) | Only a persistent ledger can judge "not mentioned" | Requires a ledger; pasting once into Claude cannot do "not mentioned for three weeks" [Inference] |
| U4 | **Bidirectional by default, no registration needed from the other party**: the advisor's and collaborators' commitments are entered in the ledger all the same (in eval-kit, 8 from the advisor and 4 from collaborators), yet only the note-taker uses the tool | Gets G6's "bidirectional" without G6's "advisor confirmation gate" and its cold-start problem | In Fellow and Littlebird, commitments by default belong to the "assignee" or to "you yourself" [Fact]; this plan's ledger belongs to "the group" |
| U5 | **Strength tiers carried through transitions**: soft commitments ("I might… no promises") enter the ledger but are not chased; rejected proposals (π0, building our own benchmark) do not enter the ledger | G3 | Littlebird's approach is a binary "skip vague commitments"; this plan is "ledger them but treat them differently", and publishes strength recall [Inference] |
| U6 | **Text-first, tool-agnostic**: the input is note text from any source (Feishu export, Otter export, handwritten Markdown) | G13; the target university's GenAI policy | Not unique, but lets BriefPilot act as a "layer" plugged in behind whatever tools people already use (00/06 §8.3) |
| U7 | **Published reconciliation accuracy**: on eval-kit's 30 cross-meeting link gold labels, report `crosslink_accuracy`, `crosslink_precision`, and transition-type accuracy, and compare against Feishu, Fellow, and pasting into Claude | G1 | No commercial product publishes action-item metrics (05 K1); academic benchmarks are sentence-level detection and do not test cross-meeting links (08 §0-3) [Fact: within the search scope] |
### 3.3 Value (attributes → outcomes users care about) and evidence

| Value cluster | Source attributes | How to prove it | Current evidence level |
|---|---|---|---|
| **V1 The opening review goes from "relying on memory" to "checking a list"**: reviews take less time and fewer items are missed | U1, U3 | Dogfooding in my own lab: compare review duration and "commitments asked about / commitments in the ledger" across 3 group meetings before and 3 after adoption | [Assumption · to be validated] |
| **V2 Commitments don't quietly disappear**, especially advisor commitments, ownerless items, and soft commitments | U1, U3, U4, U5 | eval-kit: recall grouped by owner identity (H2) + cross-meeting link accuracy (H5), competitors vs. BriefPilot | [Assumption · to be validated]; tooling is ready (eval-kit README §1) |
| **V3 Every status change is "traceable"**: when writing papers, quarterly reports, or external reports, you can say "when this number was given, who said it, and whether it was later changed" | U2 | eval-kit M5: the external report still cites the old rank-32 figure of 71.2%, but M4 already asked for a rerun (gold M4-06 → M5-01); check whether the product can flag this inconsistency | [Fact] this phenomenon is planted in the synthetic data; [Assumption] real-world frequency |
| **V4 Safe to use**: usable without recording or the cloud; no output if the verbatim quote check fails | U2, U6 | Injection tests (eval-kit H8); ungrounded-output rate | [Fact] constrained by the target university's GenAI policy (00/06 §4.5); effectiveness is an [Assumption] |

[Inference] Of these four value clusters, **V1 and V2 are the reasons users come back every week; V3 and V4 are the reasons advisors and interviewers feel reassured**. For interviewers, V2 and V4 can be proven with numbers on the spot; V1 has to wait for dogfooding.

### 3.4 Target customer (beachhead)

**Beachhead segment**: computing-oriented labs (CS, robotics, VLA, ML) at Singapore universities (starting with the target university) that **hold a fixed weekly group meeting, have 5–12 members, mix Chinese and English in conversation, and already have someone writing text minutes**.

**User roles**:
- **Primary user = the group meeting note-taker or host**: a senior PhD student, postdoc, or lab manager, usually on rotation. They do the "last week's review" every week, and how well they keep records directly affects their standing in the group [Inference].
- **Beneficiary = the PI**: no sign-up needed; they see a "last week's reconciliation statement" with verbatim quotes, which can be pasted into group meeting slides or a weekly report (the "spillover point" in 00/06 §1.5).
- **Approver = university IT / IRB**: whether real data may leave campus and whether interviews need IRB approval follow the prerequisite checklist in 00/06 §4.4–§4.5.

**Three criteria (from *Crossing the Chasm*)**:
| Criterion | Assessment | Rationale |
|---|---|---|
| big enough to matter | **Weak** [Inference] | The target university has a considerable number of labs, but willingness to pay is low (M3 payment score: 2). It is "big enough" for a portfolio, not for a business |
| small enough to lead | **Strong** [Inference] | Within the search scope, no product is built specifically for "group meeting reconciliation"; the closest competitor, Littlebird, takes an individual's perspective |
| good fit with crown jewels | **Strong** [Fact + Inference] | The project owner is in a computing lab and can dogfood; the 5 synthetic meetings in eval-kit model exactly this scenario; S0 already has the design for citation checking and refusal to answer |

**Why the "note-taker" rather than the "individual PhD student"**:
- Personal commitment lists are Littlebird's home turf ($15/month student price, a dedicated graduate-student page). There is no winning a head-on fight [Inference].
- The note-taker maintains the **group's ledger**, which naturally includes other people's and the advisor's commitments. This is a perspective the Littlebird page does not cover (07 L7: "the page does not say team members can see each other's commitments") [Fact].
- When one note-taker uses it, the whole group benefits. This is an atomic-network entry point of "one person uses it, a group views it", much lighter than "everyone in the group signs up" (the atomic network concept, 00/06 §1) [Inference].

**Bowling pins (how to reach the next pin) [Inference]**:
1. **My own lab** (dogfood, 2–4 weeks)
2. **Neighboring computing labs** (same department, via word of mouth)
3. **Weekly operations meetings of industry-academia joint labs** (U5 Top 1: a corporate-lab role at a Singapore university requires "drive the weekly operation meetings" and preparing quarterly reviews [Fact, 2020 job description]). At this stage the Meeting Ledger adds one feature: after the meeting, send it to the corporate co-lead, borrowing DESCA's "deemed accepted if no objection within N days" (U5 §0-4). This pin has a paying party.
4. **Any team that "meets weekly with the same group of people and reports this week on last week's commitments"**: corporate ML experiment review meetings, vendor-side weekly requirements meetings (the scenario of option E).

### 3.5 Market category and trends

- **Category not to enter**: "AI meeting minutes / AI notetaker". In this category, Feishu, Otter, and Fellow are the baseline references, and every aspect of BriefPilot would be compared as "missing transcription, missing recording, missing integrations" [Inference].
- **Suggested category**: "**group meeting commitment reconciliation**", positioned as a **layer** on top of existing minutes. The reference point shifts from "meeting tools" to "reconciliation": anyone in finance understands that "bookkeeping" and "reconciliation" are two different roles with two different tools [Inference].
- **Supporting trends**:
  - AI hallucination makes "verifiable output" an expectation (Wiley 2025: 64% concerned about hallucination, U3 §0-4 [Fact]);
  - MCP makes meeting text portable (06 V2 [Fact]), so "building a layer on top of someone else's minutes" is technically natural;
  - Universities' restrictions on cloud AI are tightening (the target university's GenAI policy, UCSD, Mississippi State, etc., 00/06 §4.5, U1 §0-4 [Fact]).

---

## 4. Blue Ocean ERRC

| Action | Element | Relative to | Rationale |
|---|---|---|---|
| **Eliminate** | Recording, transcription, meeting-joining bots, live captions | Feishu, Otter, Fellow | Not core (00/06 §8.3); the legal and social cost of recording consent (Granola lawsuit 3:26-cv-07926-EMC, 06 V14); the target university's GenAI policy |
| **Eliminate** | Task system and GitHub integration | Fellow, Granola | Integrations are not a moat (06 V1, V2); the Now stage only exports Markdown |
| **Reduce** | Full-text summaries, meeting highlights, chapter overviews | All minutes tools | Users want "what happened to last week's items", not yet another summary (M4 category H: "nobody will ever read those notes" [Fact]) |
| **Reduce** | The number of new action items | Feishu, Tongyi Tingwu, pasting into Claude | By default only output "explicit commitments and decisions newly added this week"; soft commitments enter the ledger but are not pushed; rejected proposals do not enter the ledger |
| **Raise** | Evidence strength: two verbatim quotes per transition + server-side verbatim verification + refuse to answer when verification fails | Feishu's single-meeting provenance, Fellow, Littlebird (no link to the original sentence observed, 07 F20, L5) | Cross-meeting inference is more prone to "filling in the blanks" than single-meeting extraction, so it must be stricter |
| **Raise** | Not guessing when information is missing: if a new date has no anchor, write "unanchored" (e.g., "after the maintenance window") | All products (eval-kit H4 not yet tested) | G3 |
| **Raise** | Coverage of advisors, collaborators, and ownerless items | Fellow (by assignee), Littlebird (by "you") | U4 |
| **Create** | Cross-meeting **status-transition diff** (last week's ledger × this week's discussion → 7 transition types) | All | The core of this option, §2.3 |
| **Create** | "Not mentioned for N weeks" and "still undecided for N weeks" reminders | All | Requires a persistent ledger |
| **Create** | Public reconciliation accuracy (crosslink accuracy / precision, transition-type accuracy), with competitor comparison | All (05 K1) | The means of proof, and also the main evidence for the portfolio |

[Inference] The shape of the value curve: **below** all competitors on "transcription quality, real-time capability, number of integrations, and summary richness"; **above** all competitors on "cross-meeting status inference, evidence strength, and restraint with unanchored information". This is a curve with a "different shape", not "higher overall" (00/03 §2.2 step 4).

---
## 5. Positioning Statement

**Moore six-part template (English):**

```
For        the note-taker or host who runs the "last week's review" segment in computational
           labs that hold weekly group meetings and already have someone writing minutes
           (starting with the target university)
Who        is dissatisfied with the status quo: what was promised last week and how far it got
           is reported verbally at the next group meeting, but meeting tools only generate a
           fresh set of action items each time; the verbal close-outs are never written back,
           and the ledger drifts out of sync within two or three weeks
Our product is a  Group Meeting Commitment Ledger (a "reconciliation layer" that sits on top of any set of minutes)
That       takes this week's pasted minutes and automatically reconciles this week's verbal
           updates against last week's commitments: fulfilled, partial, rescheduled, dropped,
           claimed by someone else, still open, not mentioned; every entry carries the original
           quotes from both last week and this week, and the note-taker confirms with one click
Unlike     Feishu Minutes, Otter, Fellow (each meeting gets its own separate entries, and status
           depends on people ticking boxes or on a task-system sync)
           and pasting minutes into ChatGPT (starts from scratch every time, no ledger, and
           quotes may be paraphrased)
We have assembled  dual-evidence transition cards with quote verification, leave-blank-instead-of-guess
           and commitment-strength tiers, "not mentioned" detection, text-first with no audio
           recording, and a public cross-meeting reconciliation benchmark (including competitor comparisons)
```

**Dunford-style one-liner**: For anyone who has to run the "last week's review" at a weekly group meeting, BriefPilot is a **group meeting commitment ledger**: other tools keep the books for each individual meeting, while it uses what people say this week to reconcile last week's books, and every reconciled entry opens up to two original quotes.

**20-second elevator version**: "Meeting tools keep the books; BriefPilot reconciles them. When someone says 'I got halfway' or 'let's hold off on that' in a group meeting, it automatically maps those words back to last week's commitment, attaches the original quotes to each one, and all you do is click confirm."

---

## 6. "Others already do this, so why are you building it?"

### 6.1 30-second answer (practice until you can say it from memory)

> "Right, Feishu Minutes, Otter, and Fellow can all turn a meeting into action items. Fellow even handles claiming by the assignee, and Littlebird checks every week whether your commitments were fulfilled. I'm not competing with them on 'generation.'
>
> I'm focused on one very specific part of the group meeting: the opening 'last week's review.' How far last week's commitments got is stated **verbally** in this week's meeting, for example 'I got halfway, I'll finish by Sunday.' But existing tools either treat this week as a new meeting and produce a brand-new list from scratch, or wait for someone to tick boxes by hand. So the verbal close-outs never get written back, and the ledger drifts out of sync within two or three weeks.
>
> BriefPilot only does 'reconciliation': it reconciles this week's words against last week's ledger, with two original quotes attached to each entry. On the same set of 5 synthetic group meetings, I ran a comparison against Feishu, Fellow, and 'pasting into Claude.' Cross-meeting linking accuracy was __, __, and __ respectively, and ours is __. (**Do not state any numbers until the experiments have been run.**)"

**Structure notes** (corresponds to the five steps in 00/03 §10.2): first acknowledge the alternatives (including the Fellow claiming and Littlebird checking just verified in Round 2) → point out the step where they all stop → explain who cares (note-takers, PIs) → bring numbers → draw honest boundaries (see 6.2).

### 6.2 Prepared answers to follow-up questions

| Follow-up question | Key points of the answer | Basis |
|---|---|---|
| "Fellow carries unfinished items over to the next meeting. Isn't that reconciliation?" | "Carrying over" moves last week's list forward, and the status still depends on people ticking items off one by one in the meeting. Its pre-meeting brief only looks at the previous recording, and the help center doesn't say it uses what was said in this meeting to update the status from the previous one. What I do is, after the carry-over, automatically propose a new status from this week's original quotes, so the person only has to confirm. I haven't tested Fellow yet, so this point depends on test results. | [Fact] 07 F4, F5; opened this round |
| "Littlebird already checks commitments every week, and it specifically targets graduate students." | Yes, it's the competitor I fear most. There are two differences: by default it tracks "your own" commitments, and the checking evidence shown on its page is email and documents; I track **a group's ledger**, and the evidence is **the next meeting itself**. I've already listed "can it use follow-up meetings as evidence" as the first item to test. If it can, I'll narrow the selling point to "group ledger + public benchmark." | [Fact] opened this round; 07 L1, L7 |
| "I could just paste two weeks of minutes into Claude and ask it to reconcile them, couldn't I?" | This is the question most worth asking. Once or twice, that works; but by week 4 it has to look at 4 sets of minutes at once, and judging a "data card nobody has mentioned for three weeks" requires a persistent ledger. The quotes it gives may be paraphrased, whereas I verify them verbatim. Most importantly, I tested "Claude + expert prompt" as a comparison group, and the number is __. If it's within 15 points of mine, I'll admit that the value here is only the workflow, not the capability. | [Inference]; §8 H-R3; 08 §5.5 sample-size warning |
| "Feishu's meeting digest summarizes action items weekly. How are you different?" | The digest does "summarizing"; its page doesn't mention "reconciling." I test this specifically in the eval-kit (H5 states "if the Feishu meeting digest reaches ≥50%, cross-meeting is not a blank space"). | [Fact] 07 C5; eval-kit README §1 |
| "Doesn't everyone have to sign up? What about cold start?" | No. Only the note-taker uses it; the advisor and group members don't need to register. What they see is a reconciliation sheet with original quotes. "Network-layer" features such as claiming and advisor confirmation will open up once single-user retention clears the bar. | 00/06 §1.5 |
| "Academic labs don't pay. What's the business story?" | The beachhead is for validation and dogfooding. The next paying segment is the weekly operations meetings of university-industry joint labs, using the same core plus "send to the company side; no objection within N days counts as acceptance." For this I only have public job descriptions as evidence; I haven't done interviews. | U5 §5.1, §0-4 |
| "A big company could add this feature in one iteration." | Agreed, so I'm not defending on the basis of "nobody has built it." What I can defend is: a group's ledger (the longer it is used, the harder its history is to migrate away), a public reconciliation benchmark and failure-mode library, and a product trade-off of "prefer leaving it blank over guessing" that runs opposite to "the more automation the better" (a weak counter-positioning). I estimate the window at 6–12 months: enough to build a demo, not enough to pitch as an open market gap. | 00/03 §4.2; 07 §8.1 |
| "How many people have you interviewed?" | Currently 0. I have an execution package (14 assumptions, with failure thresholds written in advance), and I've also drafted the IRB determination email. | 02/06 §1, §6 |

---
## 7. The Demo's Magic Moment

### 7.1 The magic moment (90 seconds)

**Setup**: The left side of the screen shows the ledger, with M1 (one-on-one) and M2 (week 1 group meeting) already imported. All data comes from the synthetic eval-kit meetings. The opening line states that "the data is synthetic; the people and projects are fictional" (00/06 §4.5, item 3).

**Action**: Paste the plain text of M3 (week 2 group meeting) and press "Reconcile".

**What appears on screen** (derived from the eval-kit gold labels; the gold labels were drafted by AI and are pending human review, so the counts below are design targets, not measured results):

| # | Last week's (M2) commitment, verbatim | This week's (M3) wording | Proposed status |
|---|---|---|---|
| 1 | Wang Bo: "I'll get the OpenVLA baseline on SimplerEnv done before next week's group meeting" (M2-05) | "The Google robot set on SimplerEnv is done... the WidowX set isn't done yet"; "I'll definitely finish WidowX by Sunday" | **Partially fulfilled + rescheduled to 2026-10-18** |
| 2 | Priya: "I'll fix the gripper by Friday" (M2-09) | "The gripper is fixed, I replaced the screws last Friday." | **Fulfilled** |
| 3 | Zhou Lan (advisor): "I'll take a look this weekend and decide whether to fix the annotations or just delete them" (M2-10) | "Prof. Zhou looked at it last weekend and said to just delete them, and I've already deleted them..." | **Fulfilled (advisor commitment)** |
| 4 | Zhou Lan (advisor): "I'm writing the GPU application form, I'll submit it next Monday" (M2-18) | "The GPU application form was submitted on Monday, but the school hasn't approved it yet"; "I'll chase them again before this Friday" | **Partially fulfilled + new commitment (advisor)** |
| 5 | Li Muqing: "Could we use part of the DROID data for co-training? I can try it" (M2-11, soft commitment) | "Let's not do co-training for now; let's wait until storage is expanded" (reason links to "downloading all of it takes 1.7 TB... only about 600 GB left") | **Dropped (with reason)** |
| 6 | Li Muqing: "Hmm, let me check the data size first" (M2-13) | "Downloading all of it takes 1.7 TB..." | **Fulfilled** |
| 7 | Chen Siyuan: "OK, I'll post it in the group chat once it's out" (M2-02) | "The rank 64 result came out last Saturday, I posted it in the group chat, 73.1%" | **Fulfilled** |
| 8 | Daniel: "I'll send the cluster quota script after the maintenance window" (M2-17, no anchor) | "I'll send the quota script right after that" | **Rescheduled, date anchored to 2026-10-20** |
| 9 | Unowned: "...someone needs to align on this" (M2-19) | "Wang Bo, give us a draft at the next group meeting" | **Claimed (Wang Bo)** |
| 10 | Question: "Should we unify the wandb projects into one?" (M2-20) | "About unifying the project that I raised last time, shall we decide it today?" → "Let's look at it again later" | **Still open (week 2)** |
| 11 | Daniel: "maybe someone should write a data card for our dataset" (M2-14, suggestion) | (none) | **Not mentioned** (suggestion level; flag only, no nudge) |

**Three things the audience should grasp within 5 seconds**:
1. **A different shape**: this is not a new list but a diff against last week's list. Of the 11 items, 4 are fulfilled, 2 partially fulfilled, 1 rescheduled with an anchored date, 1 dropped, 1 claimed, 1 still open, and 1 not mentioned.
2. **The advisor's commitments are on the ledger too** (items 3 and 4), and the advisor does not need to register.
3. **Every item opens to two verbatim quotes**; deliberately altering one character in one quote makes the system refuse to output that item (live demo of the U2 validation).

**Side-by-side comparison (only after the eval-kit experiment has been run)**: for the same M3 plain text, show output screenshots from Feishu Minutes / Tongyi Tingwu / Fellow, plus the output of "Claude + baseline prompt". The expected result is "a fresh action item list for M3", but **this must be confirmed by measurement**. If any competitor also produces a diff, show it as it is and change the narrative to "it achieves X%, we achieve Y%".

### 7.2 Optional second beat (30 seconds, to introduce "the next bottle")

Import M4 (week 3 group meeting) and M5 (progress meeting with the industry partner, Kestrel) in turn. The system flags: **in M4 the advisor says "the main rank 32 result needs to be rerun" (M4-06), while in M5 the partner is still being given the old figure of 71.2% (M5-01)**, and it warns that "figures reported externally may be outdated". This beat connects "internal reconciliation" naturally to "consistency of external reporting", which is the university–industry joint lab bottle (§3.4). [Fact] This phenomenon was deliberately planted in eval-kit (gold notes); [Assumption] its real-world frequency is unknown.

### 7.3 The 5-minute talk (following the seven-part structure in 00/06 §7.4)

| Time | Content |
|---|---|
| 0:00–0:30 | **Insight opening**: "Meeting tools all keep books, but nobody reconciles them. 'Half done' in a group meeting is a partial write-off, yet nobody records it back." |
| 0:30–1:30 | **Evidence**: an opening review is a fixed routine written into lab handbooks (Rashid Lab, MIT, Loughborough); status updates on competitor pages depend on people ticking boxes or on a task system (Fellow, Circleback, original text); eval-kit comparison numbers (**only say these once the runs are done**); interview and diary numbers (**only say these once they are done**) |
| 1:30–2:00 | **Why AI**: matching free-form speech to a specific item from last week, judging the transition type, and deciding whether a new date has an anchor all require language understanding; also explain "why we refuse to answer when validation fails" |
| 2:00–3:30 | **Demo magic moment** (§7.1) + one refusal triggered by a deliberately altered quote |
| 3:30–4:30 | **Evaluation and trade-offs**: crosslink accuracy / precision, transition-type confusion matrix, ungrounded output rate, injection test (M3 [00:04:28]); what was cut: recording, transcription, integrations, claiming UI |
| 4:30–5:00 | **Honest boundaries**: zero interviews (execution pack is ready), gold labels were drafted by AI, the window is 6–12 months, Littlebird is the top risk |
### 7.4 Demo Scope (2–4 weeks, solo)

- **Build**: ledger data model (commitment ID, strength, owner, date anchoring, status history); reconciliation pipeline (candidate pairing → transition classification → dual-quote verification → refusal); confirmation UI; Markdown export.
- **Reuse from S0**: citation allowlist verification, refusal, confirmation gate, mock/real provider switching.
- **Out of scope**: audio recording, ASR, account system, multi-user sync, any integrations.
- **Evaluation**: use eval-kit directly (5 meetings, 135 gold labels, 30 cross-meeting links, `score.py`); add a "transition type" label and a B-Text-Expert control condition (see §8 H-R3).

---

## 8. Make-or-Break Hypotheses and How to Verify Them

> Pass/fail thresholds are fixed in advance so the criteria cannot be changed after the fact (consistent with 02/06 §1.2 and eval-kit README §1). All are **[Assumption · to be verified]**.

| # | Hypothesis | Why it is fatal | How to verify | Pass line | Fail line → what to do | Cost |
|---|---|---|---|---|---|---|
| **H-R1** | **Closing items verbally** in group meetings is common: most status changes to last week's commitments are first stated at the next meeting, rather than first being updated elsewhere (group chat, issue, W&B) | If it is uncommon, there is nothing to reconcile | Add one field to the diary study: "Where did you first learn of this commitment's status?" (group meeting verbal / group chat / issue / other); observe 2 of this group's meetings in person | ≥50% of status changes first appear in verbal reports at the group meeting | <25%: the evidence source for reconciliation should switch to group chat or issues, and this plan becomes "multi-source reconciliation" or is abandoned | Piggybacks on the diary in 02/06 §4, 0 extra person-days |
| **H-R2** | Verbal closures are **not written back**: the share written back to the original commitment record within 48 hours after the meeting is low | If write-back is already good, there is no pain | The 48-hour follow-up of the same diary (02/06 F1); compare against U6 H02 | Write-back rate ≤50% | ≥80%: the pain point does not hold; move to Option C or D | Same as above |
| **H-R3** | **"Claude/ChatGPT + expert prompt" cannot do cross-meeting reconciliation well**, especially from week 3 or 4 onward | If it does it well, this plan is left with only workflow value | Add a **B-Text-Expert-Reconcile** condition to eval-kit: paste M2, M3, M4 in turn into the same conversation, with a prompt that explicitly requires "compare against the commitments from all previous meetings, give a status transition for each, and cite two original quotes"; 3 runs per segment | BriefPilot's crosslink accuracy is **≥15 percentage points higher** than the best LLM control (08 §5.5: at n≈100 the confidence interval is about ±8, so a 5-point gap does not hold up), **or** the control's quote paraphrase rate is ≥20% | Gap <10 points and quote paraphrase rate <10%: **exit condition**. Drop the "capability difference" narrative and tell it instead as "I used an evaluation to show that general-purpose models are already good enough, so I narrowed the product to a workflow plus an evaluation plan" (the honest exit in 00/06 §8.3) | 0.5 day |
| **H-R4** | **Competitors are weak at cross-meeting linking** (equivalent to eval-kit H5) | If Feishu meeting digests or Fellow can already do it, the selling point does not hold | eval-kit A-TTS and B-Text conditions, uploaded in order M1→M5 | All competitors' crosslink accuracy <30% | Any competitor ≥50%: acknowledge it honestly and narrow the selling point to "dual evidence + not mentioned + public evaluation" | 2–3 days (eval-kit README §3) |
| **H-R5** | **Littlebird does not use later meetings as fulfillment evidence**, and does not maintain a group-level ledger | If it can, it is the same product | Try the Littlebird student plan (free for the first two months) for 2 weeks each in 1-on-1 and group meeting settings; ask it "how is the X my advisor said last week should be done going?" | Its weekly report does not cite statements from later meetings, and it cannot track group-level commitments beyond "what others owe me" | If it can: the only remaining differentiation of this plan is "group-level ledger + public evaluation + no cloud", and this must be stated head-on in the positioning | 2 weeks (passive waiting) |
| **H-R6** | **The note-taker is willing to paste the minutes once a week and confirm transitions** | If input dries up, nothing else works | Dogfood for 4 group meeting weeks in my own lab; then recruit note-takers from 2 neighboring groups to try it | Still in use in the 4th group meeting week (threshold from 00/06 §1.5 H-CS1: ≥3 people using it voluntarily 3 times in a row) | Stops using it in week 2: ask "why didn't you paste?" If it is because nobody writes minutes, the input side is the bottleneck, so add an entry point such as "a 2-minute spoken summary after the meeting", or abandon | 4 weeks |
| H-R7 (secondary) | Human agreement on transition types is high enough | If humans cannot tell them apart, the model getting them right is meaningless | Two people pilot-label the transition types for M2→M3 and M3→M4 and compute κ | κ ≥0.6 | <0.6: merge the 7 types into 4 (fulfilled / not fulfilled / dropped / not mentioned) (08 §4 L4) | 0.5 day |

**Verification order**: H-R3 (half a day, cheapest and most fatal) → H-R4 (2–3 days) → H-R7 → launch H-R5 and H-R1/R2 in parallel (piggybacking on the diary study) → H-R6 (dogfooding).

**Compliance prerequisites**: for the diary study and interviews, first send the IRB determination email per 02/06 §6; before dogfooding with my own lab's real minutes, first obtain written permission from my advisor, and use only local models or university-approved models ([Fact] the target university's GenAI policy, 00/06 §4.5). Until permission is obtained, the demo uses only eval-kit's synthetic data.

---

## 9. Rejected Alternatives and Why

| Alternative | Why it is not the lead choice for this perspective | What is kept in this plan |
|---|---|---|
| **Option A** (verifiable, claimed commitment layer) | Claiming is already covered by Fellow (07 F8); provenance is already covered by Feishu (07 C7); what remains is only a difference of degree, and an interviewer saying "Feishu will have it in the next version" could knock it down | G2 quote verification, G3 no guessing on missing information, and strength tiers, as the **trust foundation** of reconciliation |
| **Option B** (PhD student 1-on-1 ledger + advisor confirmation gate) | The Littlebird graduate-student page has almost the same name (07 L9); the advisor confirmation gate requires both sides to be in the system, which makes cold start hardest; no supervision-record system was found in Singapore (07 U7); zero evidence for "commitments the advisor owes the student" | "Bidirectional": advisor commitments still go into the ledger, but no advisor confirmation is required |
| **Option C** (commitment–result–evidence, five values + W&B) | The five-value result has no user evidence (06 W10); W&B MCP + Granola MCP + Claude can be assembled DIY (02/05 §3.2); W&B integration is not intuitive in a 5-minute demo and depends on real experiment data | Computational labs as the beachhead; "dropped (with reason)" and "superseded" as transition types; W&B evidence goes in Next |
| **Option D** (accurate mixed Chinese–English terminology) | Zero first-hand Chinese complaints (06 W4); ASR vendors catch up quickly (U4 §0-2); the selling point disappears once input is text; it leans toward ASR engineering, and the AI PM narrative is weak | eval-kit's terminology recall is still measured, as an appendix table on "input quality" |
| **Option E** (vendor requirement-change ledger) | The owner has no material, so dogfooding does not hold; weakest evidence (05 E=2) | Used as the generalization narrative for the 4th bottle |
| **Option F** (open-source issue write-back) | Nobody asked for it (05 F); it can only serve as an evaluation testbed | Public SIG minutes can be used to build an English reconciliation subset, strengthening "reproducible" |
| **U5 ladder** (computational group → university–industry joint lab, quarterly review pack + objection window) as the main thread | Cannot be explained in 5 minutes; zero evidence of confirmation from the industry side (U5 §2.3); real data is nearly impossible to get (compliance score 2) | The 3rd bottle; DESCA's "no objection means acceptance" is kept as the interaction rule for external confirmation; the second beat of §7.2 |
| **Pure evaluation narrative** (G1: I built a meeting action item benchmark) | 08 has already shown that "first" cannot be claimed; an evaluation impresses interviewers, but it is not a product a user would use every week | The evaluation is this plan's **means of proof**, not the product |
| **Consent first** (G7) | Strong problem, unverified value of the solution (05 G7); once text input comes first, the problem itself shrinks | Not recording and not using the cloud is itself the answer to the consent problem |

---
## 10. Response to Round 2 New Evidence

| Round 2 new evidence | Impact on this proposal | How this proposal responds |
|---|---|---|
| Fellow already has assignee accept/dismiss (07 F8) | Claiming can't be a selling point | This proposal builds no claiming UI; it focuses on **closing out** items rather than claiming them |
| Fellow carry-over is one-off, the brief only looks at the previous meeting, and completion relies on manual check-off (07 F4, F5; opened this round) | Supports the gap this proposal targets | Written up as the core evidence in §2.3; but hands-on testing of Fellow is still to be done (07 §10-2) |
| Littlebird's graduate-student page, three-state reconciliation, student pricing, mixed Chinese-English speech (07 L2–L10) | The top risk to this proposal | Build the group's ledger, not a personal checklist; the evidence source is meetings, not email; test H-R5; if it can do this, narrow the selling point and say so explicitly |
| Littlebird's page doesn't say whether later meetings can serve as evidence (opened this round) | Gap is **neither confirmed nor ruled out** | Say only "the page doesn't say", not "it can't do this" |
| Feishu meeting digests, enterprise information recognition, source-text tracing (07 C5–C7) | "Summarization" already exists in the Chinese market | Distinguish "summarization" from "write-off/closure"; test with eval-kit H5 |
| Integration is not a moat, MCP is widespread (06 V1, V2) | Assembling a substitute is feasible | Build no integrations; list "MCP + Claude assembly" as an alternative and compare against it with H-R3 |
| No vendor publishes action-item accuracy (05 K1); academic benchmarks are sentence-level detection (08 §0-3) | Evaluation remains a credible way to prove differentiation | Don't say "first"; say "existing benchmarks measure which sentence is an action item; I measure whether items can be reconciled across meetings" (08 §5.1 talking point) |
| ICSI is itself a research-group weekly meeting corpus (08 §0-2) | Can't claim "the first research group meeting data" | Say only "synthetic group meetings from 2026, mixing Chinese and English, continuous across weeks"; consecutive ICSI meetings can be used as an English reconciliation subset, as a reproducible supplement [Inference: whether ICSI has consecutive weekly meetings of the same group usable for cross-meeting linking remains to be verified] |
| eval-kit is ready: 30 cross-meeting link gold labels, H5, crosslink metrics (README §1) | The cost of falsifying this proposal is very low | Reuse directly; add the B-Text-Expert-Reconcile condition and a "transition type" label |
| The gold labels were drafted by AI (eval-kit README, gold file header) | Credibility of externally reported numbers | Until human review and two-rater κ are done, no numbers are reported externally; the §7.1 table is explicitly labeled as design targets |
| Target university GenAI policy: confidential data must not be uploaded to external GenAI (00/06 §4.5) | Real-data path is restricted | Text first + replaceable provider + demo uses synthetic data only |
| Cold start: the atomic network is the research group, the hard side is the PI (00/06 §0-2) | Both claiming and a supervisor confirmation gate would stall at cold start | Usable by a single note-taker; the PI is a reader, not a user |
| University-industry joint labs have weekly operations meetings and quarterly reviews (U5 §2.1, 2020 job description) | The next bottleneck in the paying story | §3.4 bottleneck 3; §7.2 second beat |
| The window is roughly one quarter at a time (07 §0-7) | "Nobody is doing it" won't hold for long | Narrate as "how far others have got, where I go deeper, proven with numbers" (07 §8.1-3) |
| Class-action lawsuit against Granola (06 V14) | The recording route carries legal risk | Recording is dropped |

---

## 11. Can It Be Defended? 7 Powers Self-Check and the Window

| Power | Any sign of it? | Notes |
|---|---|---|
| Switching costs | **Early signs** [Inference] | The longer the ledger is used, the longer the history of "who said what in which week, and how it changed later"; switching tools means losing that history |
| Counter-positioning | **Weak** [Inference] | "Refuse to answer if validation fails; leave the date blank if there's no anchor" is the opposite of the big vendors' pitch that more automation is better (M2 §0-3 [Fact]: the industry mainstream is agents that write to CRM and create tasks automatically) |
| Process power | **Early signs** [Inference] | A failure-mode library and evaluation set for cross-meeting reconciliation (G21), which requires continued accumulation |
| Scale, network, branding, cornered resource | None | — |

**Window** [Inference]: 6–12 months. The most likely to close it are Littlebird (adding "check last week's commitments against this week's meeting") and Fellow (adding "AI-suggested completion" on top of AI-suggested items). That is enough for a 2–4 week demo, but not enough for a "market gap" claim. **So externally, say only "I found a specific step and validated it with numbers", not "nobody is doing this in this market".**

---

> §12 is the author's private material and is not included in the public version.

## 13. Sources (all accessed at the time of writing)

**Newly opened this round (WebFetch / WebSearch)**
1. Fellow, AI-Suggested Action Items — https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items
2. Fellow, Meeting Briefs — https://help.fellow.ai/en/articles/9773836-meeting-briefs
3. Littlebird, Promise Tracker — https://littlebird.ai/routines/promise-tracker
4. Circleback, How to track meeting action items — https://circleback.ai/how-to/track-meeting-action-items

**Cited from 07 (opened at the time of writing)**
5. Fellow, Carry incomplete items forward — https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward
6. Fellow, Action item page — https://help.fellow.ai/en/articles/4144380-action-item-page
7. Fellow × GitHub — https://fellow.ai/integrations/github
8. Fellow MCP server — https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server
9. Fellow, Supported languages — https://help.fellow.ai/en/articles/8514401-supported-languages-for-ai-note-taker
10. Littlebird, Graduate students — https://littlebird.ai/for/graduate-students
11. Littlebird, Teams — https://littlebird.ai/teams ; Pricing — https://littlebird.ai/pricing
12. Feishu intelligent meeting minutes — https://www.feishu.cn/content/article/7577317993749269689
13. Feishu AI action-item breakdown — https://www.feishu.cn/content/article/7600354912756681687
14. Zoom AI assistant — https://www.zoom.com/en/products/ai-assistant/ ; ZoomMate getting started ([Summary]) — https://www.zoom.com/en/blog/zoommate-getting-started/
15. Microsoft Teams Facilitator (support) — https://support.microsoft.com/en-us/office/use-facilitator-in-microsoft-teams-meetings-37657f91-39b5-40eb-9421-45141e3ce9f6
16. Rashid Lab meeting leader guide — https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html
17. Loughborough Co-Tutor — https://lboro.ac.uk/students/handbook/starting/attendance/co-tutor-supervisory/
18. Thesis Advisory Committee (TAC), a Singapore university's school of biological sciences — (university page; link removed)
19. Supervisor Meeting Brief (Chrome extension) — https://chromewebstore.google.com/detail/fmibimgfmoaogdajeoeedledhejppgll
20. tl;dv, ChatGPT record mode (competing vendor, [Summary]-level credibility) — https://tldv.io/blog/chatgpt-record-mode-for-meetings/

**Cited from 05, 06, 00/06, 08**
21. MIT Cahoy advising policy — https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf
22. Lilach Bullock, AI meeting notes and accountability (personal blog) — https://www.lilachbullock.com/ai-meeting-notes-accountability-small-teams/
23. Granola class-action coverage — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
24. Target university, Use of GAI in Research — (university page; link removed)
25. Target university Research Data Policy — (university page; link removed)
26. Target university IRB, Do I need IRB approval — (university page; link removed)
27. Purver et al. 2007 (SIGdial) — https://aclanthology.org/2007.sigdial-1.4.pdf
28. AMC-A (arXiv 2303.16763) — https://arxiv.org/abs/2303.16763
29. ICSI corpus (Edinburgh) — https://groups.inf.ed.ac.uk/ami/icsi/

**Pages seen in this round's WebSearch results where only the snippet was read ([Summary])**
30. Product Hunt, AI Meeting Assistant (Chrome; brings back the latest summary and unfinished items before a meeting) — https://www.producthunt.com/posts/1208248
31. Webex, Cisco AI Assistant on devices — https://blog.webex.com/innovation-ai/never-miss-a-beat-or-an-action-item-cisco-ai-assistant-on-devices-transforms-your-meetings/

**Methodology (cited from 00/03, 00/06)**
32. readingraphics, *Obviously Awesome* summary — https://readingraphics.com/book-summary-obviously-awesome/
33. Blue Ocean, Four Actions Framework — https://www.blueoceanstrategy.com/tools/four-actions-framework/
34. Lenny's Newsletter, Geoffrey Moore on finding your beachhead — https://www.lennysnewsletter.com/p/geoffrey-moore-on-finding-your-beachhead ; Chris Dixon, Come for the tool — https://cdixon.org/2015/01/31/come-for-the-tool-stay-for-the-network

**In-project data** (no external URL): `05_demo-plan/eval-kit/meetings/M2, M3, M4, M5`, `gold/decisions_hypotheses.md` (AI-drafted, pending human review).

---
## 14. Confidence Notes for This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| Fellow's status updates rely on manual check-offs, and its pre-meeting brief only looks at the previous meeting | **High (as far as the documentation goes)** | Two help articles were read this round; nothing was tested hands-on, and the product may have behavior that isn't written in its documentation |
| Littlebird's evidence sources for verification, per its page, are email and documents; follow-up meetings are not mentioned | **High (as far as the page goes) / Low (as far as product behavior goes)** | A page "not saying" something does not mean the product "doesn't do" it; this must be tested hands-on (H-R5) |
| "Automatically closing out the previous meeting's commitments using what is said in the next meeting" was not found within the search scope | **Medium-low** | Only the documentation of Fellow, Littlebird, Circleback, Feishu, Zoom, and Teams was checked, plus 1 WebSearch; long-tail products were not scanned |
| "Opening with a review of last week's action items" is standard practice in research labs | **Medium-high** | Based on the original texts from Rashid Lab, MIT Cahoy, and Loughborough; all are UK/US samples, and the target university is unconfirmed |
| Verbal close-outs are common and not written back (H-R1, H-R2) | **Assumption** | Zero interviews, zero diaries; only examples from synthetic data |
| A Claude expert prompt cannot reconcile well (H-R3) | **Assumption, and the one most likely to be overturned** | General-purpose LLMs' long-context capability is improving quickly [Inference] |
| The persuasiveness scoring in §2.2 | **Low to medium** | The researcher's subjective judgment; it reflects only the persuasion perspective, and other perspectives (business, feasibility) would produce a different ranking |
| The 11 transitions in §7.1 | **Design target** | Derived from AI-drafted gold labels, pending manual review |
| The 6–12 month window | **Inference** | Carries over the observation on catch-up speed from 07 §8.1 |

**The most important reminder**: This proposal is the most persuasive because it is **differently shaped, visible, falsifiable, and usable by a single person**, not because its evidence of demand is stronger. Its evidence of demand is as weak as that of proposals B and C (zero interviews). So the first thing to do is not write code, but spend half a day running H-R3: if adding a single expert prompt to Claude is enough to reconcile correctly, this proposal must be downgraded according to the exit conditions in §8.
