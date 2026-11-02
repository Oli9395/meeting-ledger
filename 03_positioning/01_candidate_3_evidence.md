---
title: "Candidate Positioning 3 (Evidence Perspective): A Group-Meeting Action Item Checker That Audits AI-Filled Owners and Dates"
status: candidate (for 03_positioning review; make-or-break assumptions all unverified)
perspective: evidence (evidence strength first)
sources_count: 28
sources_count_method: number of unique URLs in the sources section (recomputed at wrap-up; original value 31)
---

# Candidate Positioning 3 (Evidence Perspective): Group-Meeting Action Item Checker

> **What this document answers**: From a review stance of "evidence strength first", it accepts only pain points and competitor gaps backed by primary or official sources, gives each of candidates A–F and the new Round 2 candidates an evidence score, and then derives the **one** most recommended option. I would rather pick a narrower direction with harder evidence, and put the make-or-break assumption to validate first up front.
>
> **Labeling discipline** (carried over from the whole project):
> - **[Fact]**: the original page or text was opened, URL attached;
> - **[Summary]**: only the search snippet was seen, the original page was not opened;
> - **[Inference]**: derived from facts, no direct evidence;
> - **[Assumption · to be verified]**: needs an experiment or interviews;
> - "To be verified": the page would not open, or sources contradict each other.
> - Earlier files are cited by short names: 05 = `01_market-research/05`, 06 = the review, 07 = Fellow/Littlebird supplementary verification, 08 = academic benchmarks, U1/U3/U4/U5/U6 = `02_user-research/01/03/04/05/06`, S6 = `00_pm-skills/06`, EK = `05_demo-plan/eval-kit/`.
>
> **Newly verified this round** (original pages opened via WebFetch): a 2026-07 discussion thread on Microsoft Tech Community (what people rely on to check Teams meeting notes), and a Microsoft press release (the target university has used Microsoft 365 university-wide since 2019). I also ran 3 WebSearch queries, looking for "independent tools for checking AI meeting notes" and "research on fabricated owners in meeting summaries"; both turned up only practice guides and generic hallucination research, with no dedicated product or benchmark ([Summary], see §2.3).
>
> **Reading scope**: 00_pm-skills/03 and 06, 01_market-research/01–08, 02_user-research/01 and 03–06, plus the EK README, gold labels and trap files; the conclusion chapters and decision-relevant chapters were all read. 05 and 07 were read line by line; for the other files I read the conclusions, matrices, scoring, assumptions and credibility notes, and checked the remaining body text by keyword search.

---

## 0. Conclusion First

1. **Recommended option: "Group-Meeting Action Item Checker" (BriefPilot Lint).** The beachhead is the weekly, mixed Chinese–English group meeting in the target university's computing labs. The user is the person who tidies up after the meeting and sends out the action item list (the rotating note-taker or a senior PhD student). It does just one step: **the check before action items go out**.
   - For each action item, mark whether its **owner and due date** were stated explicitly in the original speech or filled in by the AI.
   - Anything not stated is left blank, and all blanks are collected into one "post-meeting follow-up questions" message that can be pasted straight into the group chat.
   - Soft statements ("I might… no promises", "let's revisit later") and rejected proposals do not become action items.
   - Using a public field-level evaluation, on the same set of mixed Chinese–English group meetings, compare the "fabrication rate" and the "leave-blank-instead-of-guessing rate" against the real outputs of Feishu Minutes, Tongyi Tingwu, Fellow, and ChatGPT/Claude.
2. **The one small unmet need** (down to the exact step): in the 5-minute post-meeting check, the note-taker **cannot tell whether the owner and date in an AI action item were stated in the original speech or filled in by the model**, and can only go by memory or by re-listening. Existing products offer item-level traceability, for example Feishu "supports tracing action items back to the original meeting text", but none publishes **field-level** source distinctions or a "leave blank instead of guessing" number. Academic benchmarks do not test the "unknown" option either (08 §0-4, original text verified).
3. **Why choose it (evidence perspective)**: among the 8 candidates, it is the only one that satisfies all three of these:
   - **The pain point has multiple primary sources**: the original HN post describes items attributed to the wrong person; a 2026-07 Microsoft community thread says reviewers "rely on memory rather than checking each item", and Copilot is just restating its own record; the Rashid Lab handbook writes "read the action items back, confirm owners and due dates" as a meeting rule; in hands-on testing, DingTalk assigns action items to the meeting initiator by default.
   - **The gap has official or original-text evidence**: no vendor publishes action item metrics (K1); academic benchmarks are sentence-level binary classification, and Purver 2007 explicitly says it will "leave aside" owner identification.
   - **The make-or-break assumptions can be falsified in 2–3 days**: EK already runs, H1, H3, H4 and H7 all have pre-set pass/fail thresholds, and no interviews or IRB are needed.
4. **The cost must be stated plainly**: it is a **feature-level differentiator**, and a large vendor could add a "needs confirmation" label in a single iteration (07 judges the G3 window at 3–6 months). Only two things can hold out a bit longer: **a public, reproducible field-level evaluation and mixed Chinese–English group-meeting data** (08 rates the incremental value "high"), and the weak counter-positioning that "athletes shouldn't referee themselves". So its positioning is a **wedge and a credibility proof**, not a moat.
5. **Make-or-break assumptions to validate first** (details in §11):
   - **L1**: On EK's 5 meetings, the best-performing competitor (including "ChatGPT/Claude + a plain prompt") still force-fills owners or dates, or promotes soft commitments into action items (EK H3 < 50%, or H4 < 60%, or H1 promotion rate ≥ 50%). If competitors already "don't guess" (H3 ≥ 80%, H4 ≥ 85%, promotion rate < 20%), **the option is dead**.
   - **L2**: After adding the line "if not stated, write unknown" to a general-purpose LLM, its fabrication rate is still clearly higher than BriefPilot's. Otherwise the product degenerates into "one prompt plus one evaluation", and only portfolio value remains.
   - **L3**: In real group meetings, action items missing an owner or a date make up ≥ 20%, and the note-taker really does check before sending. Otherwise it solves a rare problem.
6. **Rejected**: B (advisor 1-on-1), C (commitment → result → evidence), D (standalone Chinese–English terminology), E (vendor requirements ledger), F (open-source issue write-back), U5's "industry-academia lab quarterly review pack", and G4 claiming. The reason in every case is **insufficient evidence score**: either the pain point is only inferred (five-valued outcomes, commitments advisors owe students), or the gap is already covered by official pages (Fellow claiming, Littlebird graduate student page), or the make-or-break assumption needs weeks of PI or enterprise interviews to validate. C is kept as **Next**, on the condition that U6 H04 (student backfill rate ≥ 50%) holds.

---
## 1. Review Perspective and Evidence Scoring Rules

**Why a different scoring scheme**: The E×P×U×D score in 05 treats "evidence strength" as one of four dimensions, and multiplication lets a high U (uncovered) mask a low E. 06 W12 also points out that the three scoring systems are mutually incompatible. The evidence perspective asks only three questions: **how real is the pain**, **how real is the gap**, and **how quickly can it be falsified**.

| Dimension | 3 points | 2 points | 1 point | 0 points |
|---|---|---|---|---|
| **Ep Pain evidence** | ≥ 2 independent first-hand sources (original pages opened) directly describe this pain | 1 first-hand source plus some summaries or indirect institutional evidence | Only summaries or institutional requirements, no direct quotes from the people involved | Inference only |
| **Eg Gap evidence** | Official documentation explicitly states the limitation, or the original academic paper is verified as not covering it, **and** the original pages of the main competitors are verified as "not seen" | Original pages of several competitors show "not seen", but one is ambiguous | The core mechanism is already partly covered; the remaining gap is inferred | Official pages already explicitly cover it |
| **Ef Falsification speed** | The make-or-break assumption can be verified with existing tools in ≤ 3 days (EK) | Needs 1–2 weeks of dogfooding or a diary study | Needs cooperation from the PI or a third party, plus an IRB judgment | Needs cooperation from a company or an external institution |

Total score = Ep + Eg + Ef, maximum 9. **On a tie, the one with higher "gap evidence" wins.** The reason, per 06 §1, is that gaps of the "does the feature exist" kind are filled fastest; the harder the gap evidence, the less likely it is to be overturned on interview day by someone saying "so-and-so just launched that last month."

---

## 2. Evidence Inventory: What Is Hard, What Is Soft

### 2.1 Key Claims This Plan Relies On and Their Evidence Grades

| # | Claim | Evidence | Grade |
|---|---|---|---|
| P1 | AI meeting minutes misattribute statements, putting words in the mouths of people who never said them | Original HN thread (bad_username et al.: "plausibly mishear the parts that matter most"; examples of misattribution); 06 verified the original text exists https://news.ycombinator.com/item?id=48823024 | [Fact] |
| P2 | People who review AI minutes usually rely on memory rather than checking item by item against the original words; when asked "Did Bill agree?", Copilot merely repeats its own record | Microsoft Tech Community, main post 2026-07-30, reply 2026-08-03 https://techcommunity.microsoft.com/discussions/microsoftteams/who-verifies-teams-meeting-summary-accurately-reflects-what-was-actually-agreed-/4542338/replies/4543676 (opened this round). **Note**: the poster's username is "AI-Transcript", so there may be a conflict of interest; another MCT replied that the recap is only "a useful working draft" and that responsibility for verification rests with people | [Fact] (single post, conflict of interest to be checked) |
| P3 | Labs write "read back action items, confirm owners and due dates" into their meeting rules | Rashid Lab handbook: "Read back action items", "confirm assignees and due dates" (07 P7) https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html | [Fact] |
| P4 | At least one major vendor's product assigns action items to the meeting organizer by default | 人人都是产品经理 (Everyone Is a Product Manager), 2025-09 hands-on test of DingTalk: "automatically assigned the task, as a first pass, to the meeting organizer" (M1 §4.2) https://www.woshipm.com/share/6269848.html | [Fact] (single source, may have been fixed since, 06 W2) |
| P5 | AI "invents" owners and nonexistent dates | Weibo article (M1 §8) https://weibo.com/2/detail/comos:niwmapc3412577 | [Fact] (single article, not a measured statistic) |
| P6 | Researchers' concern about AI hallucination is rising | Wiley 2025 (2,430 respondents): concern about hallucination rose from 51% to 64% (U3 §7, original read) | [Fact] |
| P7 | Owner attribution is inherently hard, and humans disagree with each other on it | Gruenstein 2005 action-item κ 0.36; AMC-A κ 0.47; Purver 2007 original text sets aside who the owner "is" ("leave aside for now") (08, original PDF read) | [Fact] |
| G1 | No vendor publishes field-level metrics for action-item extraction | Not seen in any of the 24 products across M1 and M2; Fellow only says "human-level accuracy" (06 V7) | [Fact: not seen within the search scope] |
| G2 | Academic benchmarks are sentence-level binary classification and do not test "whether the system fabricates when the owner or date is missing" | 08 §0-3, §0-4, §5.2 (original PDFs of 9 papers read) | [Fact: not seen within the search scope] |
| G3 | Feishu provides item-level traceability, and when the owner is missing it says "can be added manually" | "Supports tracing action items back to the original meeting text"; "If the deadline or owner was not clearly stated in the meeting, it can be added manually" (07 C7, C8) https://www.feishu.cn/content/article/7600354912756681687 | [Fact]. **"Can be added manually" suggests Feishu may already leave the field blank, which is the top threat to this plan; see §11 L1** |
| G4 | Fellow's AI-suggested action items must be accepted by the assignee, but the page does not mention a link to the original sentence | 07 F8, F20 https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items | [Fact] |
| G5 | Littlebird skips "vague maybes", but its commitments do not link to the original sentence | 07 L4, L5 https://littlebird.ai/routines/promise-tracker | [Fact] |
| G6 | The Tongyi Tingwu API returns at most 6 action items, each 5–30 characters | EK README §2.2 https://help.aliyun.com/zh/tingwu/features | [Fact] (API documentation; whether the web version is the same is yet to be verified) |
| C1 | The target university has used Microsoft 365 since 2019, with Teams as the main collaboration tool | Microsoft Singapore press release, 2022-02-14: "the target university rolled out Microsoft 365" (2019) (press release link removed) (opened this round) | [Fact] (vendor press release; whether the target university enables Copilot for students is yet to be verified) |
| C2 | Teams Facilitator supports only single-language meetings, and does not support 1:1 or external meetings | 07 T6, T8 https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams | [Fact] |
| C3 | Gemini in Meet does not support Chinese or multiple languages in the same session; Otter lists only English, Spanish, and French | 06 V12; EK README (https://otter.ai/mp3-to-text) | [Fact] |
| C4 | The target university's policy: confidential, sensitive, or personal data must not be uploaded to external GenAI unless a set of conditions is all met | S6 §4.5 | [Fact] |
### 2.2 Evidence this proposal does **not** have (must be listed honestly)

| Gap | Current state | Impact |
|---|---|---|
| Share of real group meetings where an action item is missing an owner or a date | In the EK gold labels, 11 of 70 actions have no owner and 39 have no date, but that is **synthetic data with deliberately planted cases** and cannot be treated as a real frequency | Determines L3; real group meetings must be observed |
| Whether the note-taker checks before sending, and how long it takes | Zero data; Rashid Lab only shows that "the rule exists" | Determines how large the value is |
| Whether competitors fill in owners at all in mixed Chinese-English group meetings | Zero real outputs (the P0 gap in 06 §0-4 is still unfilled) | Determines L1; make-or-break for the proposal |
| First-hand complaints from Chinese-speaking users about wrong owners | Only one DingTalk hands-on test and one Weibo post; Zhihu and Xiaohongshu returned 403 (M4 category J) | Pain point is weakly evidenced on the Chinese side |
| Whether field-level source labels are noticeable to users | Zero data; M4 category H warns that "nobody reads the minutes", so users may never click | Determines whether the demo's aha moment can work |

### 2.3 Conclusions from this round of supplementary research

- **[Summary]** Searched for "tools that independently check AI meeting minutes": found only QA checklists from vendors such as GoTranscript, which recommend "write unknown if missing" and "put items without an owner into a needs an owner list" (https://gotranscript.com/en/blog/ai-meeting-summary-qa-checklist, original page not opened). **[Inference]** This suggests that "don't guess what's missing" is widely accepted best practice among practitioners, but it is currently carried out through manual checklists, and no tool was found that productizes it and publishes numbers. This follows the same pattern as U1 §3.2: "a manual process that is repeatedly recommended = a JTBD with high execution cost".
- **[Summary]** Searched for research on "fabricated owners in meeting summaries": arXiv 2404.11124 lists "wrongly attributing words or actions to a participant" as a separate error category, but does not report action item owners separately. This is consistent with the conclusion in 08: a field-level benchmark for "fabricated owners" was not found within the search scope.

---

## 3. Candidate Scoring Table (Evidence Perspective)

| Candidate | Ep Pain point | Eg Gap | Ef Falsifiable | Total | Scoring rationale |
|---|---|---|---|---|---|
| **This proposal: group meeting action item checker (A without G4, focused on G3 + G2 refusal to answer + G1, beachhead is mixed Chinese-English group meetings)** | **2** | **2** | **3** | **7** | The pain point has multiple sources (P1–P5) but no lab-level frequency data; the gap has two pieces of hard evidence (G1, G2), but Feishu's "can be added manually" wording is ambiguous (G3), so it does not get a 3; EK is ready-made and it can be falsified in 2–3 days |
| A original (including G4 claiming) | 2 | 1 | 3 | 6 | G4 is already covered by Fellow (07 F8), and G2 source tracing is already covered by Feishu (07 C7); only G3 and G1 remain |
| D Chinese-English terminology assistant (standalone) | 0–1 | 2 | 3 | 5–6 | The constraint has official evidence (C2, C3), but Feishu and Littlebird support mixed Chinese-English speech, and first-hand Chinese complaints are zero (06 W4 "high"); terminology recall can be tested with EK |
| F Open-source issue write-back | 1 | 2 | 3 | 6 | Demand is only one issue (OpenSSF #532), paid demand is 0, and the user is not the author; very good as an **evaluation data source** |
| C Commitment → outcome → evidence | 1 | 2 | 2 | 5 | The CHI 2020 hindsight bias finding is a [Fact], but the "five-value outcome" is pure inference (06 W10 "high"); the gap is "not seen on the pages", and W&B MCP + Granola MCP can be used to DIY it (U5 §3.2); the backfill rate requires 2–4 weeks of dogfooding |
| B Advisor 1-on-1 ledger | 1 | 1 | 1 | 3 | Evidence on UK institutional practice has been added (07 U3, U4), but nothing was found for Singapore (07 U7); "advisor owes the student" has zero evidence; Littlebird's graduate student page already covers the personal version (07 L9); needs PI cooperation + IRB |
| U5 University-industry lab quarterly review pack | 1 | 2 | 0 | 3 | The evidence is a 2020 job description, and "formal confirmation from the corporate side" has zero evidence (U5 §2.3); DESCA is an EU contract template, not a Singapore one; corporate-side interviews are needed |
| E Vendor requirements ledger | 1 | 1–2 | 0–1 | 2–4 | 05 self-rated E=2; there is no scenario that can be dogfooded |

**[Inference] Why the top candidate leads by only a small margin and is still the one to choose**: the 7 vs 6 gap is within scoring error. Two other points are decisive. First, its make-or-break hypothesis is the **cheapest** to test: the tool is already written, and failure costs only 3 days. Second, it leaves behind the **most assets** if it fails: the evaluation set, annotation guidelines, and competitor failure-mode table can be reused directly for C or D. According to the decision tree in U6 §1.2, "test the cheapest, most informative hypothesis first" is the correct discovery order.

---

## 4. Derivation (Evidence Version of Dunford's Ten Steps)

1. **Who are the happiest customers?** There are no customers right now. Taking one step back based on the evidence: who is already doing this **by hand**? Rashid Lab writes "read the action items back, confirm owners and due dates" into its rules (P3); practitioner checklists such as GoTranscript's recommend "write unknown if missing" (§2.3); MIT Cahoy requires action items to be sent after the meeting and reviewed at the next one (U1 §0-2). **[Inference] The happiest customer is the note-taker who is "already checking by hand but finds it slow".**
2. **Real alternatives**: see §6.1. The two strongest are "pasting the minutes into ChatGPT/Claude" and "Feishu Minutes' item-level source tracing + manual additions".
3. **Unique attributes**: remove everything that 07 §8 judged "already covered", including cross-meeting tracking, claiming, weekly reports, item-level source tracing, and GitHub sync. What remains must be what is **not seen on official pages and not tested in academic benchmarks**: field-level sources (stated verbatim / ambiguous in the original / absent from the original), leaving missing fields blank and collecting them into follow-up questions, multi-level strength, and a public comparative evaluation.
4. **Value cluster**: only one, "**no invented people or dates in the action items that get sent out**". Why keep only one? Dunford allows 1–4, but from an evidence perspective, every additional value cluster adds one more unverified assumption.
5. **Who cares most about this value?** The group must satisfy all of the following: (a) action items are cited as a basis or used to hold people accountable (research: in EK M4, Zhou Lan says "do not put numbers without a record into the paper"; this is a synthetic scenario, but it corresponds to the paper-writing traceback in U3 §5); (b) existing tools are **structurally** weaker for this group (mixed Chinese-English + Teams' single-language limit, C1–C3); (c) I can reach them and dogfood (my own lab). The intersection of the three is **mixed Chinese-English group meetings in computational labs**.
6. **Market category**: not "meeting assistant" (in that category it loses on every dimension), but "**linter for AI meeting minutes**". See §6.5.
7. **Trend**: growing concern about AI hallucination (P6), and institutions restricting real data from being sent to external AI (C4).

---
## 5. The Small Unmet Need (Precise Definition)

| Element | Content |
|---|---|
| **Scenario** | Weekly group meetings in computational labs (CS, robotics, AI) at the target university, held in person or hybrid over Teams, spoken in "Chinese sentences + English terms." After the meeting, one person is responsible for posting the action items to the group chat or a task tool [the scenario structure is [Inference]; how group meetings at the target university actually run is [Assumption, to be verified]] |
| **Step** | The few minutes of **checking** between the end of the meeting and sending out the list. Not transcription, not summarization, and not cross-meeting tracking |
| **What users do now** | Those with an AI draft skim it from memory (P2); well-organized groups read items back aloud at the end of the meeting, confirming owners and dates (P3); some also paste the transcript into a different AI to rewrite it (M1 §9: a minority "hand the Tongyi Tingwu transcript to Doubao," [Summary]) |
| **What is missing** | The note-taker **cannot tell whether the owner and date of each action item were stated in the original words or filled in by the model**. There are four specific cases, each with a corresponding sample planted in the EK: (1) the original words did not say who is responsible, yet a person was filled in (e.g., M4 "预约表要有人整理一下，回头再说吧" (someone needs to tidy up the booking sheet, let's discuss later)); (2) a vague date was converted to a specific day (M4 "我打算 11 月初开始写" (I plan to start writing in early November)); (3) a soft statement was upgraded to a commitment (M3 Daniel: "I might be able to look at the WidowX env conflict tomorrow, no promises though"); (4) a rejected proposal became an action item (M4 trap "加 π0 对比" (add a π0 comparison), already rejected) |
| **Why existing solutions fall short** | Feishu can jump from a **whole** action item back to the original passage (G3), but whether "the owner field has a basis in the original words" is left for the user to judge. The Fellow and Littlebird pages do not mention source-sentence links (G4, G5). Teams Facilitator does not support mixed Chinese-English meetings (C2). No vendor publishes a rate for "leave blank when missing" (G1). **All of the above are document-level conclusions; actual product behavior awaits L1 testing** |
| **Minimal form of the need** | Each owner and date field carries a source status (stated in the original words / vague in the original words, original wording kept / not in the original words, left blank); items marked "not in the original words" are automatically compiled into a single post-meeting follow-up message; soft statements and rejected proposals go in a separate column and do not enter the action item list |

---

## 6. Dunford's Five Elements

### 6.1 Competitive Alternatives (including "do nothing" and "paste the minutes into ChatGPT")

| Alternative | What it achieves in the "checking" step | Evidence | The remaining gap |
|---|---|---|---|
| **Do nothing** (rely on memory, everyone claims items in the WeChat group) | Zero cost; errors get corrected at next week's group meeting | [Inference]; Dunford holds that "No decision" is the biggest competitor (S3 §1.4) | Errors only surface at the next progress report. **How costly this is has no data (L3)**; this is the largest unknown in this proposal |
| **Reading back at the end of the meeting** (Rashid Lab style) | Confirms owners and dates on the spot within 30 seconds; the most reliable | [Fact] P3 | Depends on the facilitator's discipline; with mixed Chinese-English speech and multi-person discussion, the read-back itself can miss items. 07 P7 also notes that verbal confirmation takes only 30 seconds, so a tool must prove it is better than doing it verbally [Assumption, to be verified] |
| **Pasting minutes into ChatGPT / Claude** | Can extract action items, and can write "unknown" when asked; free or already paid for | [Inference] 07 A8; ChatGPT Record is macOS-only and works best in English ([Summary], 07 A1, A4) | Starts from scratch every time, with no public metrics; whether it "makes things up" depends on the prompt. **This is exactly what L2 tests: if one extra line in the prompt is enough, this proposal is left with only evaluation value** |
| **Feishu Minutes / Lark Minutes** | Automatically identifies owners; action items can be traced back to the original text and timestamps; missing values can be added manually; mixed Chinese-English speech is recognized in the original language; enterprise information recognition | [Fact] 07 C6–C11 | Field-level sourcing not seen; whether "can be added manually" means leaving blank first or filling in a default first is **to be tested in L1**. Singapore users can use Lark; whether the features are identical is to be verified (06 §3) |
| **Tongyi Tingwu** | Action item extraction; hotword API | [Fact] 07 C1; EK (up to 6 action items) | The product design caps output at 6 items, so recall has a ceiling for long group meetings [Fact, API documentation]; field-level sourcing not seen |
| **Teams Copilot / Facilitator** (the target university's default ecosystem) | Meeting recap, Planner tasks (preview), "Accept to sync" | [Fact] 07 T1, T2; C1 | Supports only single-language meetings, and not 1:1 or external meetings (C2); whether the target university enables Copilot for students is **to be verified**; checking relies on human memory (P2) |
| **Otter** | Action items for English meetings | [Fact] Lists only English, Spanish, French | Largely inapplicable to Chinese group meetings |
| **Fellow** | AI-suggested action items take effect only after the assignee accepts them; auto-accept is off by default | [Fact] 07 F8 | This is "a human confirms," not "telling the human which field to confirm"; source-sentence links not seen (F20); Chinese support is listed only as "Chinese," with mixed Chinese-English speech not mentioned (F17) |
| **Littlebird** | Skips "vague maybes"; has a graduate-student page | [Fact] 07 L4, L9 | A binary split only, with no link to the source sentence (L5); it tracks "my commitments," not a list sent out to the group |
| **Granola / Fellow MCP + Claude assembly** | Can read action items and the transcript into Claude, then have Claude check them | [Fact] 07 A7, F14 | Feasible, but the user must write the checking logic themselves, and there is no benchmark; Granola is being sued (3:26-cv-07926-EMC) and processes data in the cloud (06 V14) |

**[Inference] How to read this table**: the biggest threats to the "checking" step are not Otter, but **Feishu's manual additions** and **a general-purpose LLM plus one good prompt**. Both will be tested directly in L1 and L2.

### 6.2 Unique Attributes (and whether competitors have them)

| # | Attribute | Competitors' current state (evidence) | Replicability [Inference] |
|---|---|---|---|
| U1 | **Field-level source status**: owner and date are each marked "stated in the original words (with the source sentence and timestamp) / vague in the original words (original wording kept, not converted) / not in the original words (left blank)" | Feishu goes down to the item level (G3); Fellow and Littlebird: no source-sentence links seen (G4, G5) | High. One iteration could do it |
| U2 | **Post-meeting follow-up list**: all fields that are "not in the original words" are automatically assembled into a single follow-up message that can be pasted straight into the group chat, e.g., "Who is responsible for tidying the booking sheet? When will the rank 32 rerun happen?" | Not seen. The closest is the manually maintained "needs an owner" list in the GoTranscript checklist ([Summary]) | High, but someone has to think of it first |
| U3 | **Strength and rejection detection**: four strength levels (firm commitment / conditional / suggestion or under discussion / hypothetical, pleasantry, or rejected); soft statements and rejected proposals go in a separate column | Littlebird does a binary split (G5); multi-level plus evaluation not seen within the search scope (08 §5.2 "medium-high") | Medium. Labels are easy to add, but getting them **right** is hard and depends on evaluation |
| U4 | **Public comparative evaluation**: EK's 5 mixed Chinese-English group-meeting segments, the ICSI CC BY subset, and real outputs from Feishu, Tingwu, Fellow, and general-purpose LLMs; field-level metrics (fabrication rate, no-guess-when-missing rate, upgrade rate, terminology recall), with Wilson confidence intervals and two-annotator κ | Vendors publish nothing (G1); academia does not test the "unknown" option (G2) | **Low. The data, annotation guidelines, and failure-mode table take time to accumulate; big vendors publishing these numbers would expose their own weaknesses (weak reverse positioning)** |
| U5 | **Verification mode**: the input can be "transcript + **action items exported from another tool**," and BriefPilot only verifies without replacing | Not seen (§2.3 found only manual checklists) | Medium. This is a design that lowers the cost of switching tools, and also where the "athletes shouldn't referee" narrative lands |

**Not counted as unique attributes** (only the passing bar, 07 §8, S6 §4.5): item-level traceability, human confirmation, cross-meeting tracking, text-first input, and a swappable, locally runnable LLM provider (required by the target university's GenAI policy).
### 6.3 Value and Evidence

| Value | Evidence available now | Numbers to produce within 2–4 weeks |
|---|---|---|
| Action items that go out contain no invented owners or dates | Only shows that "people care" (P1–P6); does not show that "we do it better" | Fabrication rate and missing-not-guessed rate (H3, H4) for BriefPilot and each competitor on EK, with 95% confidence intervals; draw conclusions only for fields with a gap ≥ 15 percentage points (sample-size caveat in 08 §5.5) |
| Soft commitments and rejected proposals do not become action items | Littlebird's approach shows that vendors also see value in this (G5) | Promotion rate (H1), trap false-positive rate (H7) |
| Shorter verification time | **Zero evidence** | Timed test with 3–5 note-takers: the same action items, "AI-only draft + re-listening" versus "draft with source status"; record verification time and the number of wrong fields missed [Assumption, to be validated] |
| Chinese–English terms preserved | At the ASR layer, CS-Dialogue English WER is 15.57%–32.02% (U4 §0, [Fact]) | EK term_recall (H6), used only as a side metric |

**[Inference] The honest way to put it**: what we can prove now is "the problem exists and competitors have published no numbers"; we cannot yet prove "we are better". The demo in §10 can show numbers only after L1 has been run.

### 6.4 Target Customer (Beachhead)

**Beachhead**: **the post-meeting note-taker of mixed Chinese–English weekly group meetings** in computing labs (CS, robotics, AI) at the target university. This may be a rotating student, or a senior PhD student or postdoc responsible for compiling notes. The secondary user is the PI, as the recipient of the list.

| Moore criterion | Assessment | Evidence level |
|---|---|---|
| Big enough to matter | **Not big enough**. The number of computing labs at the target university has not been looked up; even counting Singapore and overseas Chinese tech teams, the commercial market is small | [Inference], **openly acknowledged** |
| Small enough to lead | Small enough: there is no dedicated product, and Fabric has no verifiable academic customers (07 P2); Teams Facilitator structurally fails when Chinese and English are mixed in the same meeting (C2) | [Fact] + [Inference] |
| Crown jewels fit | The project owner is in this scenario personally; EK, the annotation guidelines and score.py already exist; the project owner has a research-evaluation background (VLA survey), and "building reproducible evaluations" is their strength | [Fact] (project background) |
| Key pain point | In action items, real and fake owners and dates cannot be told apart | [Fact] P1–P5 + [Assumption] on frequency at the target university |
| Reachable | Our own group as dogfood; labs in the same department | [Inference], U1 §13.2 |

**Bowling pins ([Inference]; each pin must be validated separately)**:
1. Mixed Chinese–English group meetings in our own group and the same department (beachhead);
2. Small technical teams in Singapore and overseas Chinese communities that mix Chinese and English (persona D; reuses term recall);
3. Research meetings with external reporting, such as the industry-partnership progress meeting in EK M5 (U5's university–industry labs; there "minutes are the formal record", so fabrication costs more);
4. Any team whose "minutes will be cited and used to assign accountability", such as client–vendor requirements meetings (option E) and compliance teams.

**Why not go straight to pins 3 and 4**: fabrication costs more there, but evidence and reachability are both worse (U5 §2.3: zero evidence of enterprise confirmation; 05 E, option E=2).

### 6.5 Market Category

**Category: a checker for AI meeting notes (meeting-notes linter), not a meeting assistant.**

- **[Inference] Why**: In the "meeting assistant" category, the criteria are transcription accuracy, number of integrations and degree of automation, and BriefPilot cannot beat the incumbents on any of them. In the "checker" category, the criterion becomes "**is it independent, and does it publish numbers**". Under this criterion, incumbents are naturally disadvantaged: checking their own output is being "both athlete and referee". P2's own words are that Copilot "is repeating its own AI-generated record, not checking the original conversation".
- **An extra benefit for computing labs**: linters, unit tests and CI are concepts they use every day, so "run a lint on the minutes" needs no educational cost [Inference].
- **Cost**: A checker sounds like an "add-on tool" rather than a "system" (a16z's system test, S3 §7.1). So in the long run it must grow the kind of "state" found in option C, or it remains just a feature. This is explained in §12.

### 6.6 Related Trends

- [Fact] Researchers' concern about hallucinations rose from 51% to 64% (Wiley 2025, P6).
- [Fact] Consent and data issues in meeting AI have reached the courts: Otter in 2025-08 and Granola on 2026-07-30 faced class-action suits (3:26-cv-07926-EMC), and Fireflies faced a BIPA suit (06 V14, EK §5).
- [Fact] The target university's GenAI policy restricts uploading confidential or personal data to external GenAI (C4). **[Inference]** This pushes the product toward "text-first, able to run locally, processing only text the user chooses to submit", and also means the demo must use synthetic data.

---

## 7. ERRC Grid (the Four Actions of Blue Ocean)

| Action | Element | Rationale (with evidence) |
|---|---|---|
| **Eliminate** | Meeting-joining bots, live captions, in-house ASR | Do not compete with big vendors on transcription; checking mode only takes others' transcripts or the user's text (U5 design, M1 §9 A-to-B workflow) |
| **Eliminate** | Treating "cross-meeting tracking", "claiming", "weekly reports" and "GitHub sync" as selling points | 07 §8 judged G4, G10 and G11 already covered, and G20 refuted |
| **Eliminate** | Sentiment analysis, speaking-time statistics | Unrelated to "verifying action items" |
| **Reduce** | Summary length and full minutes | M4 category H: "nobody will ever read those notes" |
| **Reduce** | Degree of automation: no automatic assignment, no automatic task creation | Opposite to the "automatically assigns" of Fireflies, Krisp and Otter (K4); this is the source of the weak counter-positioning |
| **Raise** | Field-level provenance (owner and date each carry the original sentence and timestamp) | G1, G3, G4, G5 |
| **Raise** | Missing-not-guessed: vague dates keep the original wording and are not converted to specific dates | P4, P5; EK H3, H4 |
| **Raise** | Commitment-strength recognition and rejection recognition | EK H1, H7; Littlebird only does a binary split (G5) |
| **Raise** | Fidelity of Chinese–English terms | C2, C3; EK H6 |
| **Create** | A post-meeting follow-up list (one message that can be pasted directly) | Turns "unknown" from a defect into a next action; manual lists such as GoTranscript's ([Summary]) |
| **Create** | A public field-level comparative evaluation and scorecard | G1, G2; 08 §5.2 rates the increment "high" |
| **Create** | Checking mode: take another tool's action items as input, check but do not replace | P2; lowers the cost of switching tools |

**Shape of the value curve [Inference]**: clearly **below** the industry on "transcription, integrations, automation, cross-meeting", and clearly **above** the industry on "field trustworthiness, published numbers, Chinese–English terms". The shape is different, not uniformly higher. This meets the Blue Ocean check criterion (S3 §2.2 step 4).

---
## 8. Positioning Statement

**Moore six-part version**

```
For        people in Chinese-speaking computing labs (such as at the target university) who send out the action item list after a mixed Chinese-English group meeting
Who        are dissatisfied with AI meeting notes: they cannot tell whether the owners and dates in the list were actually said or filled in by the model, and can only rely on memory or re-listening
Our product is a  meeting-notes linter for AI notes
That       flags each field as "stated / vague / not stated", does not guess what was not said, collects the gaps into a single post-meeting follow-up, and keeps soft commitments and rejected proposals out of the action items
Unlike     tools such as Feishu Minutes, Teams Copilot, and ChatGPT that "generate and vouch for themselves" (they do not publish field-level metrics, and Teams does not support mixed Chinese-English meetings)
We have assembled  field-level source annotation, a no-guessing rule for missing information, a four-level strength annotation guide, and a public mixed Chinese-English group meeting benchmark (including real competitor outputs, two-annotator κ, and confidence intervals)
```

**Dunford one-sentence version**: For lab note-takers who already use Feishu or Teams to produce meeting notes but still have to check them from memory before sending out the list, BriefPilot is a notes linter: it tells you which owners and dates the AI made up, and turns anything unclear into a single follow-up question. Its "no fabrication" claim comes with public numbers you can check.

---

## 9. "Others already do this, so why are you building it?": the 30-second answer

> "Right, Feishu, Otter, and Fellow can all turn a meeting into action items. Feishu can even link back to the source text, and Fellow has the assignee click accept. I'm not competing with them on generation. I only do the check before sending: **for each action item, was the owner and date actually said, or did the model fill it in?** No vendor publishes this number, and academic benchmarks only test 'is this sentence an action item?', not 'does the system make things up when nothing was said?'. So I took 5 mixed Chinese-English group meetings and put the real outputs of Feishu, Tongyi Tingwu, Fellow, and ChatGPT on the same ruler: what the fabrication rate is, and whether an unstated date gets converted into a specific day. My product is that ruler turned into a product: it flags what was made up, leaves blank what wasn't said, and turns the blanks into a follow-up question. It can be copied, but before they copy it, they have to publish their own scores."

**Supplementary answers when pressed** (each maps to existing evidence):
- "Can't you just fill things in manually in Feishu?" → "Yes. That's why my first experiment tests whether it leaves the field blank first or fills in a default first. If it already leaves it blank, I drop this direction." (L1)
- "Couldn't ChatGPT do this with one more line of prompt?" → "Maybe, and I tested that too, see L2. Even if it can, 'relying on a prompt every time' and 'having a public field-level score' are two different things. I will write the conclusion according to what was measured."
- "Are you claiming the 'first benchmark'?" → "No. ICSI, AMI, and AMC-A have had action-item benchmarks for a long time, but they are sentence-level binary classification. What I measure is field-level no-guessing and fabrication, plus mixed Chinese-English." (08 §5.1 wording table)
- "Is your data synthetic?" → "Yes. The reason is that the target university's policy does not allow me to upload real group meetings to external models (C4), so the gold labels are public and reproducible, and the conclusions only say 'on these 5 meetings'."

---

## 10. The demo's magic moment

**One sentence**: Drop in the **action items another product has already generated** together with the transcript, and 3 seconds later the "made-up owners and dates" that the user did not notice themselves are marked red, and a follow-up question appears at the bottom that can be pasted straight into the group chat.

**Script** (using EK's M4, group meeting week 3):
1. **Left column**: the real output of a competitor (or a general-purpose LLM using EK's ordinary baseline prompt) on M4, pasted as is, with a screenshot kept as evidence and the product version and date noted.
2. **Click "Lint"**: the owner and date fields of each action item are colored.
   - **Green**: stated in the original words; hovering shows the original sentence and timestamp;
   - **Yellow**: vague in the original words; the original wording is kept, for example "early November", and not converted to 11-01;
   - **Red**: not stated in the original words, but filled in anyway. For example, "someone should tidy up the booking sheet, let's come back to it later" was assigned an owner.
   - Soft commitments (Daniel's "I can probably ask my friend at Kestrel…") and rejected proposals (adding the π0 comparison) are moved to the "Not an action item" column, with the original sentence that rejected them attached.
3. **"Follow-ups after the meeting" at the bottom**: for example "(1) Who is responsible for tidying the booking sheet? (2) What is the deadline for rerunning the rank 32 main result? (3) Has Muqing confirmed the review before Friday?", copyable in one click.
4. **Score card**: the fabrication rate, no-guessing rate, and upgrade rate of each product on EK, with 95% confidence intervals and sample sizes. **Only measured numbers go in; cells that were not run say "not tested".**
5. **One additional security detail**: M3 has a "read-aloud injection text" planted in it (EK trap T-M3-1); the linter quotes it as meeting content and does not execute it as an instruction.

**Why this moment is the aha [Inference]**: the user previously thought the action items were "roughly right"; the red fields show them errors they had missed, and the follow-up list immediately tells them what to do next. This matches Elena Verna's reminder: the aha cannot be a setup (S6).

**Things the demo must not say**:
- Do not say "the competitor's accuracy is X%"; only say "on these 5 synthetic meetings" (EK §5);
- Until the gold labels have two-annotator labeling and κ has reached the bar (strength ≥ 0.6, type ≥ 0.7), do not show strength-related numbers (EK open issue);
- Do not say "first";
- Do not say "Feishu cannot trace to the source"; Feishu can do it at the item level.

---

## 11. Make-or-break assumptions and how to verify them (in order)

| # | Assumption [Assumption · to be verified] | How to verify | Pass line | Kill line | Cost | Consequence if it fails |
|---|---|---|---|---|---|---|
| **L1** (do first) | Mainstream products still force-fill owners or dates on mixed Chinese-English group meetings, or upgrade soft commitments | EK: Feishu Minutes, Tongyi Tingwu, and Fellow via A-TTS; ChatGPT and Claude via B-Text plus the baseline prompt, 3 runs each; look at `owner_abstain_rate`, `due_abstain_rate`, `soft_upgrade_rate`, `trap_rate` | The best competitor meets any one of: H3 < 50%, H4 < 60%, H1 upgrade rate ≥ 50%, H7 triggered in ≥ 2 meetings | The best competitor meets all of: H3 ≥ 80%, H4 ≥ 85%, upgrade rate < 20%, H7 all 0 | 2–3 days, no IRB needed (synthetic data, EK §5) | **The plan dies**; fall back to C (if U6 H04 holds) or D; in interviews, tell it as "I used 3 days to disprove my own direction" |
| **L2** | After one strong prompt is added to a general-purpose LLM ("if it wasn't said, write UNKNOWN; soft commitments are not action items"), its fabrication rate is still clearly higher than BriefPilot's | B-Text, same 5 meetings, 3 runs each | Gap ≥ 15 percentage points, with non-overlapping confidence intervals | Gap < 10 percentage points | Half a day | The product degrades to "prompt + benchmark". Downgrade to an **evaluation project in the portfolio**; do not present it as a product |
| **L3** | In real group meetings at the target university, action items missing an owner or a date make up ≥ 20%, and note-takers do check before sending | First email irb@university.example to get a written determination (S6 §4.4, U6 §6); after obtaining consent, observe 2 meetings each in our own group and 1 other group, **without audio recording, handwritten notes only**, and count using EK's annotation guidelines; interview 3–5 note-takers: "What did you do the last time before sending out action items?" | Missing-field share ≥ 20%, and ≥ 3/5 note-takers can recount a specific check or correction event | Missing-field share < 10%, or ≤ 1/5 can recount one | 1–2 weeks (waiting for the IRB reply) | Too few problems; the value cluster does not hold. If many fields are missing but nobody checks, switch to the "post-meeting follow-up list" angle (U2) |
| **L4** | Field-level sourcing makes checking faster or more accurate | Timed test: the same action list containing errors, "plain draft + transcript" versus "with source coloring"; record time taken and number of missed errors, 3–5 people | Missed errors drop ≥ 50%, or time drops ≥ 30% | Neither improves | 1 day (done alongside the L3 interviews) | The coloring UI is not the value; keep only the follow-up list and the benchmark |
| **L5** | The annotation itself is reliable | Per EK annotation-guide §6, a second person double-annotates M1 and M3 (46 items) | strength κ ≥ 0.6, type κ ≥ 0.7 | strength κ < 0.5 | 1 day | Merge strength into 2 levels (commitment / non-commitment) and report only owner and date metrics externally |

**Why this order**: L1 and L2 are the cheapest and the most likely to kill the plan. L5 is the precondition for whether the L1 and L2 conclusions can be shared externally, and runs in parallel with L1. L3 has to wait for the IRB and is the slowest, so it goes last, but the IRB email goes out on day 1.

**Mapping to U6**: L3 corresponds to a variant of H02 plus H03; L4 is new; U6's H04, H05, and H06 are not this plan's make-or-break lines, but they will decide whether Next should do C or B.

---
## 12. How Long Can It Hold (7 Powers Self-Check)

| Power | Present? | Notes |
|---|---|---|
| Counter-positioning | **Weak** | The big vendors' selling point is "the more automation, the better" (K4). Publicly admitting "X% of our fields are made up" would undercut that pitch, so they are unlikely to publish field-level numbers in the short term [Inference]. But adding a "needs confirmation" label does not hurt their pitch, so they will certainly add one |
| Process capability or data | **Nascent** | Annotation guidelines, gold labels for mixed Chinese-English group meetings, a table of competitor failure modes, user-correction feedback loop (G21). All of these take time to accumulate; at the demo stage we can only show the mechanism |
| Switching costs | None | Verification mode deliberately avoids lock-in |
| Brand | Nascent | "The one that publishes its scores" may hold in a small circle [Assumption] |

**Window of opportunity [Inference]**: The feature itself has 3–6 months (the judgment on G3 in 07 §8). The value of public evaluation and data lasts longer, but only if it is kept up to date. **Conclusion**: 2–4 weeks is enough to build a convincing demo and evaluation, but not enough to support a "market gap" claim. The narrative should follow the advice in 07 §8.1, item 3: change it from "nobody has done this" to "here is how far others have gone, here is where I go deeper, and here are the numbers to prove it."

**In the long run it must grow "state"**: The verifier is only a wedge. If L1–L3 hold, Next is to accumulate verified action items into a group-level ledger; if U6 H04 holds, then connect C's "result backfill." Only at that point does it make sense to talk about a system test.

---

## 13. Rejected Alternatives and Reasons

| Alternative | Reason for rejection (evidence view) | What is kept |
|---|---|---|
| **B Advisor 1-on-1 two-way ledger** | The individual version is already covered by Littlebird's graduate-student page (07 L9, "lists what you promised your advisor"); the confirmation step is already taken by UK university systems (07 U3, U4); no institutional lever was found in Singapore (07 U7); zero direct evidence for "commitments the advisor owes the student"; the make-or-break test needs PI cooperation + IRB | U6's H05 and H06 are still asked as planned; the verifier's follow-up question list can be used in 1-on-1s |
| **C Commitment → outcome → evidence** | The five-value outcome is pure inference (06 W10 "high"); willingness to backfill is unknown (U3 H-A); W&B MCP + Granola MCP can be DIY'd (U5 §3.2); Littlebird could get close by adding one data source (07 §8) | **Next**: if the U6 H04 backfill rate is ≥ 50%, add outcome backfill on top of the verifier; EK has 32 result-type gold labels that can be reused |
| **D Chinese-English terminology assistant (standalone)** | Zero first-hand complaints from Chinese-speaking users (06 W4); Feishu and Littlebird already support mixed Chinese-English speech (07 C11, L10); ASR-layer vendors catch up quickly (U4 §0-2) | Term recall as one metric of the verifier; mixed Chinese-English as a screening criterion for the beachhead |
| **A Original version (including G4 claiming)** | Fellow launched accept/dismiss on 2026-10-01 (07 F8), so G4 is out | Fellow's "dismiss means permanent deletion, no reason kept" (F9) is noted as a small detail for Next |
| **E Vendor requirements ledger** | Weakest evidence (05 E=2); no material available for dogfooding; the make-or-break test needs external vendors' cooperation | Narrative for the 4th bowling pin |
| **F Open-source issue write-back** | Demand comes from just one issue; paid demand is 0 | Use ICSI (CC BY 4.0) and public open-source meeting minutes as a **reproducible evaluation base** |
| **U5 University-industry lab quarterly review pack** | Zero public evidence of "formal confirmation by the company side" (U5 §2.3); the job description is from 2020; the make-or-break test needs company-side cooperation | 3rd bowling pin; EK M5 already has partner-meeting samples; DESCA's "default accept + objection window" is kept as an interaction reference for Next's confirmation step |
| **G7 consent-first, G19 local execution** | The problem is strong, but there is zero evidence for the "solution's value" (05 G7); local recording already has Meetily and anarlog (U4 §0-4) | A **threshold** rather than a selling point: text-first, replaceable provider, can run locally (C4) |
| **G10 weekly report, G11 cross-meeting, G12 retrospective Q&A** | 07 §8 judged these already covered or nearly covered | Not pursued |

---

## 14. Response to Round 2 New Evidence

| New evidence (source) | Impact on this plan | How this plan handles it |
|---|---|---|
| Fellow already has assignee accept/dismiss (07 F8) | Overturns G4 of Plan A | Remove the claiming UI; distinguish "a person confirms" from "telling the person which field needs confirmation" (§6.1) |
| Littlebird's graduate-student page; promise tracker skips vague maybes (07 L4, L9) | Top risk for B and C; an initial version of G3 already exists | Do not enter the graduate-student personal-commitment market; for strength tiering, only claim "multi-level + evaluable," not "nobody has done it" |
| Feishu "manual additions," item-level traceability, meeting digest, enterprise information recognition (07 C5–C11) | **Top threat to this plan** | Listed as a must-test under L1; do not claim "Feishu cannot trace sources"; proactively acknowledge it in interviews |
| Tongyi Tingwu action items capped at 6 (EK §2.2) | Recall on long group meetings has a product-design ceiling | Mark it separately in the scorecard as a "design ceiling," not counted as an extraction failure |
| ChatGPT/Claude + MCP assembly is feasible (07 §5) | "Paste the minutes" is the strongest substitute | Listed as L2; use real testing to decide between product and portfolio piece |
| "First action-item evaluation" and "first research group-meeting dataset" cannot be claimed (08 §0) | Weakens the "first" narrative | Only claim four increments: field-level missing-not-guessed, fabrication rate, mixed Chinese-English, and real competitor outputs (08 §5.2) |
| Mixed Chinese-English + action-item field annotation is a gap within the searched scope (08 §3.5, §5.2) | **Strengthens this plan** | Make it the core data asset of U4; also reproduce on an ICSI subset for comparison |
| Sample-size warning: n = 100 with about 80% accuracy gives ±8 percentage points (08 §5.5) | Small samples cannot distinguish small gaps | Draw conclusions only for gaps ≥ 15 percentage points; attach Wilson intervals to the scorecard |
| University-industry lab 3.50, tiered plan ceiling 3.80 (U5 §5.1) | There is a paying party, but evidence at the "company confirmation" step is zero | Treat as the 3rd bowling pin; not the beachhead |
| Enterprise ML teams can DIY with W&B MCP + Granola MCP (U5 §3.2) | Plan C does not hold up on the enterprise side | C is downgraded to Next, conditional on H04 |
| The target university's IRB, research data, and GenAI policy (S6 §4.4–4.5) | Real group meetings cannot be freely sent to external models; interviews may count as research | Demo uses synthetic data only; text-first, replaceable provider; send an IRB email before L3 observation, no audio recording |
| Cold start: the atomic network is the research group, and the hard side is the PI (S6) | Claiming, advisor confirmation, and a group-wide board all require multiple people | The verifier is a **single-user tool**: the note-taker alone can use it; network effects are left to Next (come for the tool) |
| EK is already executable, selftest passes; gold labels are AI-drafted (EK README) | The make-or-break hypothesis can be run within days; numbers cannot be published before double annotation | Do L1 first; run L5 in parallel with L1 |
| U6's 14 hypotheses and decision tree | Provides an execution package for interviews and diary studies | L3 reuses U6 §3 outline and §4 diary form; add L4 (timed test) |
| 05 G3's U = 4 may be too high (Phase A open issue) | Needs review | Agree to lower it to 3 (Littlebird dichotomy + Feishu manual additions). This plan's Eg is therefore given only 2, not 3 |

---
## 15. Next Steps (2–4 weeks, Now / Next / Later)

| Phase | What to do | Condition for moving to the next phase |
|---|---|---|
| **Now · Week 1** | Send the IRB email on day 1; run L1 on EK (Feishu, Tongyi Tingwu, Fellow: A-TTS; ChatGPT, Claude: B-Text × 3) and L2; find 1 classmate to double-label M1 and M3 (L5) | L1 is not fatal; L5 reaches the κ threshold |
| **Now · Weeks 2–3** | Build the verifier MVP: text input (transcript + optional action items from other tools) → field provenance status → follow-up question list → strength and veto column; score itself with score.py and reproduce results on the ICSI subset | Its fabrication rate and missing-not-guessed rate on EK beat the best competitor by ≥ 15 percentage points |
| **Now · Weeks 3–4** | L3 observation (after the IRB determination), note-taker interviews, and the L4 timed test; build the scorecard and demo | At least one of L3 and L4 holds |
| **Next** | Turn verified action items into a group ledger; if U6 H04 holds, feed C's results back in; add Fellow "rejection trace" | ≥ 3 note-takers use it for 4 consecutive weeks |
| **Later** | Bowling pins 2–4: Chinese-English mixed technical teams, university-industry collaboration meetings, client-vendor meetings | Validate each pin separately |
| **Won't** | Meeting bots, real-time transcription, CRM integration, sentiment analysis, selling cross-meeting tracking as the headline feature | — |

---

## 16. Source List (all accessed at the time of writing)

**Newly opened this round**
1. Microsoft Tech Community: "Who verifies Teams Meeting summary accurately reflects what was actually agreed in the meeting" (main post 2026-07-30, replies 2026-08-02 and 08-03) — https://techcommunity.microsoft.com/discussions/microsoftteams/who-verifies-teams-meeting-summary-accurately-reflects-what-was-actually-agreed-/4542338/replies/4543676 [Fact; the poster may have a stake]
2. Microsoft Singapore News Center, a Singapore university's Smart Campus (2022-02-14) — (link removed) [Fact]

**Only search snippets seen this round**
3. GoTranscript, AI meeting summary QA checklist — https://gotranscript.com/en/blog/ai-meeting-summary-qa-checklist [Summary; vendor blog]
4. arXiv 2404.11124, What's under the hood: Investigating Automatic Metrics on Meeting Summarization — https://arxiv.org/pdf/2404.11124 [Summary]

**Cited from 07 (original pages opened by a previous agent)**
5. Fellow AI-Suggested Action Items — https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items
6. Fellow Action item page — https://help.fellow.ai/en/articles/4144380-action-item-page
7. Fellow supported languages — https://help.fellow.ai/en/articles/8514401-supported-languages-for-ai-note-taker
8. Fellow MCP — https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server
9. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
10. Littlebird graduate students page — https://littlebird.ai/for/graduate-students
11. Feishu smart meeting minutes — https://www.feishu.cn/content/article/7577317993749269689
12. Feishu AI action item breakdown — https://www.feishu.cn/content/article/7600354912756681687
13. Microsoft Learn, Facilitator in Teams — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
14. Microsoft Support, Use Facilitator — https://support.microsoft.com/en-us/office/use-facilitator-in-microsoft-teams-meetings-37657f91-39b5-40eb-9421-45141e3ce9f6
15. Rashid Lab meeting leader guide — https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html
16. Fabric academic labs — https://fabric.so/teams/academic-labs
17. Loughborough Co-Tutor — https://lboro.ac.uk/students/handbook/starting/attendance/co-tutor-supervisory/
18. A Singapore university's school of biological sciences, Thesis Advisory Committee (TAC) — (university page; link removed)

**Cited from 06, M1, M4, U3, U4 (verified in round 1 or Round 2)**
19. HN discussion — https://news.ycombinator.com/item?id=48823024
20. Everyone Is a Product Manager (人人都是产品经理), a 55-minute hands-on test of DingTalk AI Listening Notes (2025-09-19) — https://www.woshipm.com/share/6269848.html
21. Weibo article: AI doesn't make up tasks and owners — https://weibo.com/2/detail/comos:niwmapc3412577
22. Google Meet "Take notes for me" — https://support.google.com/meet/answer/14754931
23. Wiley ExplanAItions 2025 — https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx
24. CS-Dialogue (arXiv 2502.18913) — https://arxiv.org/html/2502.18913
25. Granola lawsuit coverage (3:26-cv-07926-EMC) — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/

**Cited from 08 (original PDFs read)**
26. Purver et al. 2007 and related ICSI literature (see 08 §7)
27. AMC-A, Liu et al. 2023 (see 08 §7)
28. Lampert et al. 2008 — https://aclanthology.org/U08-1009.pdf

**Cited from the EK README and S6**
29. Tongyi Tingwu feature description (up to 6 action items) — https://help.aliyun.com/zh/tingwu/features
30. Otter MP3 to text (supported languages) — https://otter.ai/mp3-to-text
31. The target university's generative AI research use policy, research data policy, and IRB page (see the URL list in S6 §4.4–4.5)

**Methodology**: 00_pm-skills/03 (Dunford, Blue Ocean, Moore, 7 Powers); 00_pm-skills/06 (cold start, Now-Next-Later).

---
## 17. Confidence in This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| "The verification step can't tell real fields from fake ones" is a real problem | **Medium** | Multiple primary sources (P1–P3), but none at the target university, and no frequency data; P2 is a single post and may have a conflict of interest |
| Competitors have no public field-level metrics, and academic benchmarks don't test "unknown" | **Medium-high** | Conclusion from verifying official pages and the original text of 9 PDFs; "not seen ≠ doesn't exist" |
| Competitors actually force-fill values in their products | **Low (untested)** | Only one 2025 hands-on test of DingTalk; Feishu docs suggest it may leave fields blank. **This is what L1 must answer** |
| This approach leads on evidence score | **Medium** | 7 vs. 6, a gap within scoring error; the lead mainly comes from "fastest to falsify" |
| Beachhead choice | **Medium-low** | The scenario structure is an inference; the number of labs at the target university and their group-meeting practices were not found; there is a risk of self-projection (U1 §14) |
| Market category "verifier" | **Inference** | No user has tested this framing |
| Window of opportunity and Power judgment | **Inference** | Based on the catch-up speed observed in 07 |

**Known biases**:
1. The evidence perspective naturally favors "what can be measured", and may underestimate needs that are hard to measure but genuinely painful (for example, the advisor relationship).
2. This approach's evaluation asset (EK) was built by the same project, so the "player and referee at once" criticism applies to us as well. We must publish the gold labels, the annotation guidelines, and the two-annotator κ.
3. All competitor conclusions come from documents; none comes from hands-on product testing.

---

## Revision History

- v1: First draft.
