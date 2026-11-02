---
title: Supplementary PM Skills — Cold Start, Growth and Retention, Stakeholders, Compliance and Ethics, Product Teardowns, Willingness to Pay, Interview Cases, Build/Buy/Integrate, Roadmaps and Retrospectives (Including a Full-Process PM Checklist)
status: draft
sources_count: 47
---

# Supplementary PM Skills: Cold Start, Growth and Retention, Stakeholders, Compliance and Ethics, Product Teardowns, Willingness to Pay, Interview Cases, Build/Buy/Integrate, Roadmaps and Retrospectives

> **Why this file exists**
> The first-round integrity review (`01_market-research/06_research_integrity_review.md` §5, §9 P2 item 10) ran a keyword count and found that `00_pm-skills/01–05` had zero or near-zero coverage of these topics: cold start and network effects, PLG and retention, stakeholders, PDPA and IRB, product teardowns, willingness-to-pay measurement, interview cases, and build vs buy. These topics are not "icing on the cake"; they directly determine whether you can handle an interviewer's follow-up questions:
> - G4 (the named person claims the item themselves), G6 (the advisor confirmation gate), and G17 (the PI's group-wide dashboard) in options A/B/C **all require several people to be in the system at the same time**. Without a cold-start framework, you cannot answer "why would the first person use it?"
> - The biggest weakness of option C (computational research groups) is willingness to pay. Without a measurement method, all you can say is "I think so."
> - The project owner does research at the target university: **recording real group meetings, interviewing classmates, and pasting transcripts into cloud-hosted LLMs**. Every one of these steps may touch the university's IRB, its research data policy, and its generative AI policy. The facts newly found in this round (§4.4, §4.5) will in turn change the product design.
>
> **Evidence labels** (carried over from round one, with [Summary] added following the review's recommendation)
> - **[Fact]**: This round opened the original page with WebFetch; the URL and access date are at the end of the document.
> - **[Summary]**: Only a search-result snippet or a secondary overview was seen; the original page was not opened (or could not be opened). Downgrade by one level when citing.
> - **[Inference]**: The author's reasoning based on facts; it can be challenged.
> - **[Assumption · to be validated]**: A proposition that needs to be validated through user research or experiments.
> - **To be verified**: The source could not be opened, or sources conflict.
>
> **Legal disclaimer**: Chapter 4 is a PM-perspective compliance "risk map." It helps you know whom to ask and what to ask. **It is not legal advice.** Before any real launch or formal research, the written replies of the university IRB, the university's legal/IT offices, and a practicing lawyer prevail.

---

## 0. One-page conclusions (start here)

1. **[Inference] The cold-start solution is "useful to one person first, then grow into many."** What Chris Dixon's "come for the tool, stay for the network" (§1.2) means for BriefPilot: the v2 demo must have value that **holds up for a single user**, for example a doctoral student's own "commitment–outcome ledger." The named person claiming an item (G4), advisor confirmation (G6), and the group-wide dashboard (G17) are the "network layer" and belong in Next/Later, not in Now.
2. **[Inference] The atomic network is "one research group," and the hard side is the PI/advisor.** In the Slack example in Andrew Chen's original text, a company of fewer than ten people can sustain chat activity (§1.1, [Fact]). A research group is of similar size. But whether this network can start turning depends on whether the advisor is willing to look and willing to confirm (H-C in round-one 05).
3. **[Inference] Activation should be split into three steps, setup, aha, and habit, and retention should be counted by "group-meeting week."** Elena Verna points out that the most common B2B mistake is treating setup as the aha (§2.2, [Fact]). For BriefPilot, "importing one set of minutes" is only setup; "jumping back to the original sentence within 3 seconds after the meeting, or being reminded before the next group meeting to fill in the outcome" may be the aha ([Assumption · to be validated]).
4. **[Fact] There is indeed a "individuals use it first, the school buys later" path in the education market, but the evidence is scattered.** On 2025-03-14, UCLA announced a campus-wide Overleaf license, "eliminating the need for individual purchases by students and departments"; Overleaf's website describes its growth path as "From research groups to departments to the entire campus" (§2.4).
5. **[Fact] The university's rules impose three hard constraints on v2:**
   - Interviews and surveys **that count as "research"** (designed to develop or contribute to generalizable knowledge) require prior IRB approval from the university; even if the study can go through the Exempt route, an application must still be submitted (§4.4).
   - The university owns research data produced by on-campus research (§4.5).
   - The university's generative AI policy states, "Any confidential or sensitive information, and/or personal data must not be uploaded to any external GenAI," unless a set of conditions is met (§4.5).

   **[Inference]** The third point means that feeding real group-meeting transcripts to a cloud-hosted LLM is itself a compliance issue. This in turn supports G13 (text first), G19 (data never leaves the device), and "the demo uses only synthetic data or de-identified data collected with consent."
6. **[Fact] Recording-consent rules vary by jurisdiction.**
   - US federal law is one-party consent; the DMLP lists 10 states that require all-party consent, including California, Florida, Illinois, Pennsylvania, and Washington (§4.2).
   - China's Personal Information Protection Law requires "personal information processors" to obtain fully informed, voluntary, and explicit consent and to give prior notice (Articles 13, 14, and 17), but it does not apply when a natural person processes personal information for personal or household affairs (Article 72) (§4.3).
   - Singapore has no general recording-consent law; the PDPA binds organizations (§4.1, [Summary]).
7. **[Inference] Willingness to pay: the sample is too small for survey methods to be usable.** Gabor-Granger recommends at least 100 complete responses per segment (SurveyMonkey, §6.3, [Fact]). A research-group setting cannot reach that volume. A workable approach is Ramanujam's three-question WTP conversation (§6.1), plus asking PIs or corporate funders for "pre-sale commitments" (§6.5).
8. **[Inference] Build/Buy/Integrate: buy or integrate transcription, storage, and the task system; build only the "commitment semantics, verification, claiming, and evaluation set."** Round one already verified that integration is not a moat (Fellow↔GitHub, Granola via Zapier, Otter/Circleback/Read with MCP). So building integrations yourself has no differentiating value and is only a cost.
9. **[Inference] The main line of the interview narrative**: tell "why build this" as a product sense question.
   - Organize it with CIRCLES: first the alternatives and the gap, then why one particular group of people cares so much, and finally the trade-offs and the Won't items.
   - Tell v2 as a 5-minute AI product teardown: open with the most interesting insight rather than walking through features in order (Institute of AI PM, §5.2, §7.5).

---
## 1. Cold Start and Network Effects

### 1.1 Core Concepts

| Concept | Definition | Evidence level |
|---|---|---|
| **Cold Start Problem** | Network-type products have too few people early on, so the experience is actually worse ("anti-network effects"), which means even fewer people come | [Summary] (several book-review summaries; the Lenny excerpt gives no formal definition) |
| **Atomic network** | "the smallest network needed that can stand on its own"; the network needs "enough density and stability to break through early anti-network effects" | [Fact] Book excerpt published in Lenny's Newsletter |
| **Differences in atomic-network size** | Slack: a company with fewer than ten people can sustain chat, and the threshold is "the team of people around you"; Zoom is also a case where the minimum size is very low; a credit card must "launch in an entire city"; Uber early on focused on "5pm at the Caltrain station at 5th and King St."; Workday needs several hundred people at once, and is better suited to top-down sales | [Fact] Same as above |
| **Hard side** | In a multi-sided network, the side that has fewer people but creates most of the value, and must be won first; examples in the summaries include Uber drivers, Airbnb hosts, LinkedIn employers | [Summary] (book reviews and summaries; original wording not checked) |
| **The three forces of network effects** | Chen redefines network effects as acquisition effects, engagement effects, and economic effects | [Summary] |
| **Single-player mode / "come for the tool, stay for the network"** | "initially attract users with a single-player tool and then, over time, get them to participate in a network"; examples: Delicious started as cloud bookmarks (a single-player tool) and later became a tag-discovery network; Instagram's initial hook was filters | [Fact] Chris Dixon, original post of 2015-01-31 |
| **Slack's 2,000 messages** | Butterfield said that about 93% of teams that have sent roughly 2,000 messages are still using it | [Summary] (only reader excerpts on Goodreads were seen; the original book was not checked, **to be verified**) |

**Why this matters for BriefPilot**: Of the six options in round one, 05, three core differentiators are "multi-person" features: G4 claiming by the named person, G6 advisor confirmation, G17 PI whole-group board. Claiming requires the named person to be in the system too, and confirmation requires the advisor to be there as well. This is exactly the standard form of the cold start: **when the first user opens the product, nobody else is in the system, so the value of these features is zero**. [Inference]

### 1.2 Authoritative Sources (ordered by credibility)
1. Andrew Chen, *The Cold Start Problem* (Harper Business, 2021); Lenny's Newsletter excerpt "The Atomic Network" [Fact].
2. Chris Dixon, "Come for the tool, stay for the network" (cdixon.org, 2015-01-31) [Fact].
3. Assorted book reviews and summaries (Antoine Buteau, Frog Capital, Goodreads reader notes) [Summary], used only to locate concepts, not to quote figures directly.

### 1.3 Steps (applicable to any multi-person collaboration product)
1. **Write down the network's "edges"**: between whom does value arise? BriefPilot's edge is "the person who makes a commitment ↔ the person the commitment is made to", for example "student ↔ advisor" and "group member ↔ group member".
2. **Find the hard side**: which side is smaller, harder to recruit, and worth more? [Inference] In a research group the hard side is the **PI/advisor**: few in number, with expensive time, but one sentence from them, "I'll look at this", can get the whole group using it.
3. **Define the atomic network**: what is the smallest unit that can sustain itself? [Inference] **One recurring group meeting of one research group**, roughly 5–12 people plus one PI. This size is close to the "fewer than ten people" threshold Chen gives for Slack, but that is an analogy, not evidence.
4. **Design the single-player mode**: when the network is at zero, what can the first user get on their own? It must be written as one sentence: "Even if no colleague uses it, I would use it, because…".
5. **Design a natural "single-player → multi-player" spillover**: the single-player output must be visible to others, for example exporting a weekly report with original-sentence citations to send to the advisor. That gives the network-layer invitation a reason, rather than "please sign up too".
6. **Take on only one atomic network at a time**: first get to "everyone is using it" in one group, then replicate to adjacent groups (bowling pins, see 03 §3); don't scatter across five groups at once.
7. **Define the signal that "the network is alive"**: for example, over 4 consecutive group meetings, ≥50% of named people claimed items themselves ([Assumption · to be validated]; the threshold must be fixed in advance, see 05 §5.1).

### 1.4 Common Mistakes
- **Building multi-person features on day one**: claiming, boards, and notifications are all built, but when the first user opens the product there isn't a single colleague. [Inference]
- **Treating "pulling people in" as the cold-start plan**: relying on the advisor to push it, with no single-player value. [Inference] Chen's Workday example shows that top-down sales is another reasonable path, but only if there is a budget holder and a decision-maker. In a lab that person is the PI, and the PI is not yet a target user of v2.
- **Defining the atomic network too broadly**: for example, as "all computational labs at the target university". [Inference]
- **Ignoring the hard side's incentives**: confirming one item costs the advisor an extra 30 seconds, so what do they get in return? Without an answer, G6 will die. [Inference]

### 1.5 How to Use This in BriefPilot v2
- **[Inference] Single-player mode candidate (recommended for the Now-phase demo)**: "My Group-Meeting Commitment Ledger".
  - The student pastes in post-meeting minutes (text first, G13) and gets "what I promised / what others promised me". Each item can be traced back to the original sentence in 3 seconds (G2), and missing fields show "to be confirmed" (G3).
  - Before the next group meeting, the system automatically lists "results awaiting backfill" (the single-player version of G5).
  - **No dependence on any colleague signing up**.
- **[Inference] Spillover point**: one-click export of "this week's commitments and results" as Markdown, which can be pasted directly into group-meeting slides or a weekly report (G10). What the advisor sees is a weekly report with original-sentence citations, not a sign-up invitation.
- **[Inference] Network layer (Next/Later)**: the advisor clicks "confirm" in the weekly report (G6), named people claim items (G4), PI whole-group board (G17). Each of these should be opened only after the single-player mode has shown retention evidence.
- **[Assumption · to be validated] H-CS1**: At least 3 PhD students, with no colleague using it, spontaneously use the single-player ledger for 3 consecutive group meetings. If this does not hold, single-player value is insufficient and the network layer is moot. Return to 02 §5 step 1 and find the problem again.
- **Interview talking points**: when an interviewer asks "Your claiming feature requires everyone to be in the system; what about the cold start?", answering "I use Dixon's come-for-the-tool: phase one is only the single-player ledger… the network layer waits until single-player retention reaches the threshold" is much stronger than answering "we'll promote it".

---
## 2. PLG and Retention

### 2.1 Core Concepts

| Concept | Definition | Evidence level |
|---|---|---|
| **PLG (Product-led growth)** | A growth model in which the product itself is the main driver of acquisition, conversion, and expansion. OpenView says it coined the term in 2016 | [Summary] (excerpt from a Sacra interview with OpenView partner Blake Bartlett; the original OpenView page contained no definition text when opened in this round) |
| **Bottom-up adoption** | A shift from "selling to executives who hold the budget" to "selling to end users", and the shift is gradual ("more like a dimmer switch") | [Summary] (Pendo blog paraphrasing OpenView's Kyle Poyar) |
| **Three-stage activation: setup → aha → habit** | Setup is a necessary prerequisite action; aha is the first experience of value; habit is getting the aha repeatedly until it becomes routine | [Summary] (several practitioners' paraphrases of the Reforge framework; the original Reforge course page was not opened) |
| **B2B activation must be measured per account/team** | "Setup, aha, and/or habit loop have to incorporate distribution within the account"; "a large number of individual users doesn't guarantee successful bottom-up selling"; a common mistake is to "mistakenly want to count setup as their value delivery, or aha moment"; "The aha moment should be measurable in a quantitative way." | [Fact] Elena Verna's original article |
| **A flattening retention curve = a PMF signal for some segment** | Balfour: if the retention curve flattens somewhere, you have most likely found PMF for some market or segment | [Summary] (secondhand paraphrase) |
| **"Good retention" benchmarks** | Lenny (2020-06-09) gives **6-month user retention**: Consumer SaaS ~40% GOOD / ~70% GREAT; SMB/mid-market SaaS ~60% / ~80%; Enterprise SaaS ~70% (the headline says ~75%) / ~90%. For bottom-up SaaS he gives only 12-month net revenue retention: ~100% / ~120%. The original warns: "startups rarely increase retention significantly" | [Fact] Lenny's original article. Note that the enterprise SaaS figures contradict themselves within the article, and the data is from 2020 |

### 2.2 Authoritative Sources
1. Elena Verna, "Hey B2B, I bet you are measuring activation wrong" [Fact].
2. Lenny Rachitsky, "What is good retention?" (2020-06-09) [Fact].
3. Reforge's retention and activation framework (Brian Balfour, Casey Winters, et al.) [Summary]: the original course is paid and was not opened in this round. In 2026 there were reports that Reforge was acquired by Miro, [Summary], **to be verified**.
4. OpenView's PLG definition [Summary].

### 2.3 Procedure
1. **Write down the unit of value first**: the group meets once a week, so the natural retention cycle is the "group meeting week", not daily activity. [Inference] Measuring a periodic group-meeting product by daily active users is a common mistake.
2. **Define three measurable events for setup / aha / habit** (these are only BriefPilot [Assumption · to be validated] and must be calibrated against real traces):
   - setup: the first time the user pastes meeting notes and generates a commitment list.
   - aha (candidate 1): within 24 hours after the meeting, the user opens the original-sentence quote of a commitment and leaves it unchanged, or edits the fields and then confirms.
   - aha (candidate 2): before the next group meeting, the user sees the "pending fill-in" list and fills in the result for at least 1 item.
   - habit: for 3 consecutive group-meeting weeks, the user completes "paste → confirm → fill in before the next meeting".
3. **Correlation calibration**: once there is data from ≥10 users, check which aha candidate has the strongest relationship with still being active in week 4, and settle on that one. [Inference] With a sample this small, only direction can be read, not significance.
4. **Plot the weekly cohort retention curve**: the x-axis is the nth group meeting, the y-axis is the share of users still active. Watch whether the curve flattens, rather than the absolute values.
5. **B2B dimension**: track both "individual retention" and "research group retention" (≥2 people in the group still using it). Verna's warning is that many individual users does not mean the team will buy.
6. **Bottom-up path in the education market**: individual free → research group (PI funds) → college or university-wide license. The decision-maker and the payer differ at every level; see §3.
7. **Fix thresholds in advance** (reusing the template in 05 §5.1), for example: "week-4 group-meeting retention ≥50% (n≥6) before entering network-layer development". [Assumption · to be validated]

### 2.4 Bottom-up Procurement in Education: Facts Found in This Round
- **[Fact]** UCLA DTS 2025-03-14: "UCLA now offers a campus-wide Overleaf license, eliminating the need for individual purchases by students and departments." / "Previously, students and departments had to buy separate Overleaf licenses." This is a direct example of "individuals/departments pay first, the university consolidates procurement later".
- **[Fact]** Overleaf's university page says "From research groups to departments to the entire campus", and tiers by size: Standard is for "research groups, or small departments", and Commons AI is for "entire department or campus".
- **[Fact]** Notion offers individual students and educators a free Education Plan (single-person workspace), verified with a school email and re-verified every year; the page opened in this round has **no** campus-wide education plan, only a "student organizations" plan.
- **[Summary]** Several universities (Virginia, Michigan State, Edinburgh, UNSW) procure Overleaf centrally and directly. In other words, "individuals first, then the university" is not the only path, and **this round found no systematic data showing that "individuals first, then the university" generally holds**.
- **[Inference]** For BriefPilot, even if university-level procurement comes later, the upfront hurdles are university IT, data policy, and IRB (§4). This is much harder than for Overleaf, because meeting content contains personal data and unpublished research.
### 2.5 Common mistakes
- Treating setup as the aha moment (Verna). [Fact]
- Measuring a periodic product by daily active users or session count. [Inference]
- Reporting "67% retention" at n=3. You must attach n and the time window (01 §5.3). [Inference]
- Forcing consumer or enterprise benchmarks onto research groups: Lenny himself says these numbers are a starting point for judgment, not a passing bar. [Fact]
- Looking only at individual retention and not team retention, and wrongly concluding that bottom-up adoption has been established. [Fact, Verna]

### 2.6 How to apply this in BriefPilot v2
- **[Inference] The North Star stays the same, with an activation funnel added**: the North Star remains "the number of action items confirmed by the user and completed before the deadline" (01 §5.1), with a three-level activation funnel in front of it (setup → aha → habit). In the demo phase, report only the headcount at each funnel level, not percentages.
- **[Assumption · to be validated] H-PLG1**: Counted in "group meeting weeks", single-user ledger retention in week 4 is ≥50% (n≥6, across ≥2 research groups).
- **[Inference] Interview answer to "How do you measure week-one retention?"**: "I don't measure daily active users. I look at cohorts by group meeting week, and I split activation into three events: setup, aha, and habit. And aha isn't 'import succeeded'; it's 'the user filled in the results before the next meeting.'"

---
## 3. Stakeholder Map

### 3.1 Core concepts
- **Power-Interest Grid / Mendelow's Matrix**: Usually attributed to Aubrey Mendelow (1991). The two axes are power and interest, divided into four quadrants that correspond to four strategies:
  - High power × high interest: manage closely (key players).
  - High power × low interest: keep satisfied.
  - Low power × high interest: keep informed.
  - Low power × low interest: monitor.

  Secondary sources also warn that binary axes oversimplify, and that stakeholders' positions change over time and need to be reviewed regularly. [Summary] (Summarized from multiple secondary textbooks; Mendelow's original paper not verified)
- **RACI**: Responsible (does the work), Accountable (ultimately answerable), Consulted (asked for input beforehand), Informed (notified afterward). The core rule is "each task has exactly one A". [Summary] (Multiple secondary sources agree; the original CIO.com page returned 403, **to be verified**)
- **DACI (Atlassian Team Playbook)**: Used for "making a decision", not for "doing a task". [Fact]
  - Driver: "The person responsible for corralling stakeholders, collating all the necessary information… getting a decision made by the agreed date."
  - Approver: "The one person (yes: one!) who makes the decision."
  - Contributors: "they have a voice, but not a vote."
  - Informed: "People whose work may be affected by the decision."
  - Steps: prepare the DACI document → assign the Driver → assign the Approver and Contributors → assign the Informed → draft an action plan → gather input and decide → organize action items → share the outcome.
- **[Inference] How to choose**: RACI governs "execution", DACI governs "decisions". Solo projects most often get stuck on decisions, for example "choose option A or C", so DACI is more useful.

### 3.2 Steps
1. **List everyone**: users, payers, approvers, people who will be affected, and people who can veto.
2. **Write one row per person**: what they want, what they fear, where their power comes from, and their current attitude toward the project.
3. **Place them in the Power-Interest Grid**, and set a communication frequency and format for each quadrant.
4. **Run DACI on key decisions** and record them in the decision log (01 §6.4).
5. **Review every two weeks**: when positions change, the strategy must change with them.

### 3.3 BriefPilot v2 stakeholder map ([Inference], to be corrected by user research)

| Stakeholder | Wants | Fears | Power | Interest | Strategy | Communication |
|---|---|---|---|---|---|---|
| **Client / interviewer** | Evidence: why build this at all, whether there are users, where the moat is | Empty talk, fabricated data, "the features are better" style answers | High (decides the offer) | Medium | Keep satisfied → manage closely during the interview | One-page PR-FAQ + 5-minute demo + evidence grading table |
| **Advisor / PI** | Efficient group meetings, students moving forward on schedule, papers that are traceable; does not want to spend extra time | Recording leaks, leaks of unpublished results, students "performing" through the tool, IRB and data violations | **High** (decides whether it can be used in the group and whether to provide funding) | Medium→High (depends on value) | Manage closely (also the hard side of the network, §1.3) | Verbal check first → one-page explainer (data destination, no-recording option) → written consent |
| **Group members / peers (users)** | Fewer missed items, fewer follow-up questions, being able to recover the "why" when writing papers | Being monitored, being seen by the advisor as "not done", extra workload | Medium (they decide whether to use it) | High | Keep informed + co-create | Interviews, diary study, trial feedback group |
| **University IT / data governance** | Compliance, data kept within controlled bounds | Unapproved cloud services, personal data leaving the country | High (can ban it) | Low | Keep satisfied | Formal inquiry email: data classification, list of permitted tools |
| **University IRB / school-level ERC** | Subject protection, informed consent, data security | Unapproved research interviews or recordings | High (prior approval for research) | Low | Keep satisfied (ask clearly up front) | Email irb@university.example to request a written determination (§4.4) |
| **Corporate funder (if pursuing the university-industry joint lab direction)** | Transparent milestones, auditable deliverables | IP and confidentiality agreement risks | High (the paying party) | Medium | Manage closely (only where options C+E intersect) | Through the PI, no direct contact |
| **Competitors / platforms (Feishu, Fellow, Otter, etc.)** | Not relevant | Not relevant | Medium (APIs, MCP, and terms may change) | Low | Monitor | Track changelogs and terms |
### 3.4 RACI: Division of Labor for This Project's 2–4 Week Demo (Even a Solo Project Needs One)

| Item | R | A | C | I |
|---|---|---|---|---|
| Choose the wedge approach (A/C combination, etc.) | Project owner | Project owner | Advisor, 2–3 group members | Client/interviewer (afterward) |
| Trial in the group / observe group meetings | Project owner | **Advisor** | Group members, IRB (if it counts as research) | Whole group |
| Interviews and diary study | Project owner | Project owner (if it counts as research, PI and IRB approval are prerequisites) | IRB / ERC | Interviewees |
| Run the model on real data | Project owner | **Advisor + data owner** | University IT | Group members |
| External demo presentation | Project owner | Project owner | Advisor (whether unpublished group content is involved) | Client/interviewer |

> **[Inference] Key point**: For anything that touches "the group's real data," A is not you. Writing A down clearly is itself a way to show in an interview that you understand stakeholders.

### 3.5 Key Points for Communicating with Three Kinds of People
- **Client/interviewer**: Conclusion first, evidence after. Every number comes with n, a time window, and a measurement method (01 §5.3); proactively state "the parts I haven't validated yet" (03 §10.4).
- **Advisor**:
  - [Inference] Ask about pain points first; don't push the tool first (Mom Test, 02 §3.1): "After the last group meeting, how do you usually follow up on what was decided?"
  - When presenting the proposal, the first sentence covers where the data goes and "it works without recording."
  - Ask for one small commitment, for example "let me try the text-only version after the next two group meetings," rather than "have the whole group use it."
- **IT/IRB**: Written, specific, with attachments. State clearly what data is collected, where it is stored, who can access it, how long it is retained, and whether it is sent to an external model. Ask in their terminology, for example "does this count as research?"

### 3.6 Common Mistakes
- Treating only "users" as stakeholders and ignoring the people who can veto with a single vote (IT, IRB, advisor). [Inference]
- One task with two A's, or "everyone is jointly responsible." [Summary]
- Treating the advisor as a "distribution channel" rather than a person with their own interests and concerns. [Inference]
- Waiting until the demo is finished to ask IT/IRB, only to find the data source cannot be used and the demo evidence is invalidated. [Inference]

---

## 4. Compliance: PDPA, Recording Consent, University IRB, Unpublished Data

> Reminder: the following is a PM's risk map, not legal advice.

### 4.1 Singapore PDPA
- **[Summary] The PDPA only binds "organisations"**: The main provisions of the PDPA do not apply to individuals acting in a personal or domestic capacity, nor to public agencies (Linklaters summary; the relevant PDPC FAQ page was collapsed when opened this round and the original text was not seen, **to be verified**). When an employee acts in the course of employment, the compliance obligations fall on the employing organisation (secondary summary).
- **[Summary] Main obligations**: The obligations listed by the PDPC include consent (sections 13–17, withdrawable, see section 16), purpose limitation (section 18; catch-all wording such as "for any other purposes that the organisation deems fit" is generally not considered reasonable), notification (section 20, informing of purposes at or before collection, use, or disclosure), accountability, protection, retention limitation, transfer limitation, data breach notification, and so on. The body text of the official PDPC page did not load this round; the above comes from search summaries and a summary of the 2017 PDPC guidelines. The PDPA has since been amended, so **defer to the current PDPC pages, to be verified**.
- **[To be verified] Penalty amounts**: The official page was not opened this round, so **no figures are given**.
- **[To be verified] Research exception**: The wording "Research exception" was seen on only one low-credibility website, with no details.
- **[Inference] Implications for BriefPilot**:
  - The project owner keeping their own notes is close to acting in a "personal capacity."
  - Once BriefPilot, as a product (even a demo), collects other people's statements, names, and commitments, **the party operating it may be treated as an "organisation"** and bear obligations such as consent, notification, and purpose limitation.
  - Doing it within the target university in a research capacity also falls under the university's policies (§4.4, §4.5).

### 4.2 Recording Consent: Singapore, China, United States

| Jurisdiction | Key points of the rule | Evidence level | Implications for the product [Inference] |
|---|---|---|---|
| **Singapore** | There is no general recording-consent law or wiretapping law; a participant recording a conversation they are present in generally does not constitute a crime; the risk lies in later use (breach of confidentiality, etc.); when an organisation records in a business context, the PDPA requires consent and prior notification | [Summary] (commercial legal information sites such as singaporelegaladvice.com and recordinglaw.com; no statutory text or original PDPC source seen) | The legal bar is low, but **the university's policies and the trust bar within the group are high**; the product defaults to "pre-meeting notice + optional no-recording" |
| **Mainland China: civil evidence** | Article 106 of the Interpretation of the Civil Procedure Law: "Evidence formed or obtained by means that seriously infringe others' lawful rights and interests, violate prohibitions in law, or seriously violate public order and good morals shall not be used as a basis for finding the facts of a case"; in practice, a conversation secretly recorded by a participant is usually not excluded merely for lack of consent | [Fact] Quoted from the original in China Justice Observer (2019-11-23); law firm articles [Summary] | This is a question of "whether it can be used as evidence," and **does not mean a product may handle recordings without consent** |
| **Mainland China: personal information** | PIPL Article 13: legal bases for processing personal information; the first is "obtaining the individual's consent," with 6 others including contract and statutory duties; Article 14: "such consent shall be given voluntarily and explicitly by the individual on a fully informed basis"; Article 17: before processing, the processor must inform the individual of its name and contact information, the purpose and method of processing, the types of information, the retention period, how to exercise rights, etc.; Article 28: sensitive personal information includes "biometric identification," etc.; Article 72: "this Law does not apply where a natural person processes personal information for personal or family affairs" | [Fact] Full legal text published by the Cyberspace Administration of China | The product operator is a "personal information processor" and needs to give notice and obtain consent. If voiceprints are used for speaker identification, it **may** fall under "biometric identification" sensitive information, requiring stricter handling (separate consent, etc.). Article 29 was not opened this round, **to be verified** |
| **United States** | Federal law (18 U.S.C. 2511(2)(d)) is one-party consent: "Federal law permits recording telephone calls and in-person conversations with the consent of at least one of the parties"; the all-party-consent states listed by DMLP are California, Connecticut, Florida, Illinois, Maryland, Massachusetts (prohibits secret recording), Montana, New Hampshire, Pennsylvania, Washington; when it is unclear which state's law applies to a cross-state call, it is advisable to obtain everyone's consent | [Fact] DMLP page. **Conflict**: the page says "eleven states" but lists only 10; the Illinois entry notes that its law was ruled unconstitutional in 2014, and later amendments were not checked this round, **to be verified** | If even one participant is in an all-party-consent state, design for all-party consent: meeting-entry notice, explicit consent, ability to opt out |

- **[Fact, verified in round one] Granola was named in a class action on 2026-07-30 (3:26-cv-07926-EMC).** The complaint was not reopened this round, so the allegations are not described here. [Inference] It shows that the legal risk of the "no bot, silent transcription" class of design in US all-party-consent states is real, not theoretical.
- **[Inference] Product design conclusions (strictest of the three jurisdictions)**:
  - Text-first by default (G13), no recording.
  - If recording: explicit notice before the meeting, a recording status visible to everyone, and anyone may request that it stop or be deleted.
  - The retention period for personal data in transcripts and action items is configurable.
  - No voiceprint profiling.
### 4.3 Supplement for the China Scenario
- **[Inference]** If the product later targets teams in China (part of Option D), then beyond Articles 13, 14 and 17, cross-border transfer of personal information (from Article 38 onward; the relevant provisions were not opened this round, **to be verified**) also needs attention.
- Verified in round one: Feishu has "enterprise information recognition" (colleague names, project names) and can recognize mixed Chinese-English text. So when targeting teams in China, there is less room for differentiation on both compliance and features.

### 4.4 University IRB / Ethics Approval: Do User Interviews and Diary Studies Need IRB Approval?
**Official rules of the target university ([Fact], opened at the time of writing):**
- "All [university] research conducted by [university] staff and students involving the use of human subjects" must obtain IRB approval before it begins.
- Definition of "Research": "a systematic investigation, including research development, testing, and evaluation; designed to develop or contribute to generalizable knowledge".
- Activities explicitly listed as requiring approval include: "observational studies", "interviews and focus group discussions", "surveys and questionnaires", "any secondary use of data (containing personal identifiers) that are not in the public domain".
- When unsure: "contact [the university IRB] (irb@university.example) for clarifications".
- Student rules:
  - Research postgraduates (PhD, M.A./M.Sc. by research) "submit your ethics applications to [the university IRB] via your supervisor".
  - Coursework-based research (FYP, URECA, etc.) goes through the school ethics committee (SERC).
  - SERC only reviews projects that meet all four conditions: they fit the definition of "Research"; they fall outside the scope of HBRA; their risk level is Exempt or Expedited under SBER ("SERC does not review Full Board studies"); and they are not part of a faculty study already under review by the university IRB.
  - CITI certification is required; when personal data is collected, "informed consent from your participant is a must".
  - Observation explicitly includes "image recordings, audio recordings, visual observations".
  - Data must be encrypted and access-restricted; "No publishing of personal data in the public domain"; data is handled by classification under the university's data governance policy.
- **Exempt does not mean no application is needed**: research with less than minimal risk can be designated Exempt, but "Researchers are still required to apply to [the university IRB] and obtain formal approval for Exempt-status". Among the six Exempt categories, Category 2 is "Anonymous educational tests, surveys, interviews, or public observations". It requires participants to be anonymous or effectively de-identified, and they usually cannot be a vulnerable population.
- **[Summary] Non-academic surveys**: Search summaries show that the university's guidance states that "if the intent of the survey is not 'research', [university IRB] or SERC ethics approval is not required". Non-academic surveys (such as post-event questionnaires or service questionnaires of student organizations) generally need no approval, but should follow the Annex A guidelines. **This passage was not seen in the original text of the two pages opened this round, to be verified.**

**[Inference] Decision tree for BriefPilot v2** (the written IRB reply is final):
1. What is the purpose of the interviews and diary study?
   - Only to make product decisions (not published, not written into a paper, no claim of generalizable knowledge): may count as "not research". **But it is still conducted within the target university, by a student of the target university, with fellow students of the target university.**
   - Results will be written into a paper, thesis, or public report, or presented as "research findings": most likely counts as research and **requires IRB approval in advance**.
2. Do the portfolio and interview presentations count as "contribute to generalizable knowledge"? **Uncertain**. This is exactly the question to ask in an email to irb@university.example.
3. Will audio or video be recorded, and will identifiable information be collected? If so, even under Exempt a formal application is required, and Category 2 requires anonymity. Audio recordings are inherently identifiable, so this **most likely does not qualify for Exempt Category 2** and would need the Expedited route ([Inference], to be confirmed by the IRB).
4. Safe practice (recommended regardless of the determination):
   - Email irb@university.example to request a written determination, attaching a one-page research description.
   - Complete CITI certification first.
   - Do not record interviews and take notes only, or record only with local storage and delete afterward.
   - Use an informed consent form.
   - Until a determination is obtained, do only "own dogfooding + synthetic data".

### 4.5 Protection of Unpublished Data (University Research Data Policy + University Generative AI Policy)
- **[Fact] University Research Data Policy**:
  - "The University owns all research data produced by research projects conducted at or under the auspices of [the university]"; the PI and designated researchers have only non-commercial rights to use and publish the data.
  - Retention is "10 years after publication or after the completion of the project, whichever is later".
  - Data must be stored in "facilities, equipment, devices or virtual resources where the University has full access and control".
  - Before sharing externally, it is advisable to sign a research collaboration agreement or an NDA first.
  - The page shows no effective or revision date for the policy.
- **[Fact] University policy on the use of generative AI in research** (published 2023-07-04, reviewed 2025-11-07):
  - "Researchers must prioritise and safeguard the privacy and confidentiality of research data".
  - "Any confidential or sensitive information, and/or personal data must not be uploaded to any external GenAI". Exceptions must satisfy a set of conditions at the same time, including "The data is not retained in or by the GenAI", the activity being lawful and permitted by policy, access being limited to authorized research members, and (where applicable) coverage by the data owner's written permission or a research collaboration agreement.
  - Researchers are responsible for leaks.
  - Use of GenAI must be disclosed with the tool's full name, version, purpose and manner of use; "Not citing or acknowledging the use of GenAI could be considered plagiarism".
  - The policy does not directly name "unpublished manuscripts or grant applications"; if the rules of the submitting venue or funder are stricter, follow the stricter ones.
- **[Summary] Data classification**: The university library and other units have published a Research Data Classification and Handling Guide (accessible only to university/NIE staff). A 2020 university slide deck listed levels such as Unclassified/Open, Restricted, Confidential and Highly Confidential, which may be outdated, **to be verified**.

**[Inference] Direct implications of this section for the product and demo (one of the most important new findings in this document):**
1. **Group meeting content most likely counts as university research data**: unpublished experimental results, hypotheses and run links all do. Sending real group meeting transcripts to an external cloud LLM requires meeting all the exception conditions of the GenAI policy. Among them, "not retained" depends on the data retention terms of the API used, which must be verified one by one.
2. This pushes the **product form of Option C** toward the following combination:
   - text-first, with the user pasting content actively (G13);
   - able to run locally or connect to a model approved by the university (G19);
   - by default, raw transcripts are not uploaded; only commitment summaries confirmed by the user are uploaded (optional).
3. **Demo data strategy**: In the Now phase, use only synthetic group meetings (fictional topics and names) plus the project owner's own notes. Only after obtaining the supervisor's written permission and an IRB determination should de-identified real data be used. The demo opening must state "the data is ___" (Template D in 05 already includes this).
4. **[Inference] This is also a differentiation rationale worth presenting**: Feishu, Otter and Fireflies are all cloud products; "research groups with institution-level constraints on unpublished data" are a population structurally shut out by these rules, which fits the definition of "user differentiation". **But guard against over-interpretation**: the university may have approved enterprise-grade tools, a point covered in 06 Review P1 item 5 and still to be verified.
### 4.6 Steps (compliance pre-checklist)
1. List all data the demo and the research will touch: whose it is, what type, where it is stored, where it is sent.
2. Using the §4.4 decision tree, email the IRB and get a written determination.
3. Using §4.5, confirm: will real data be sent to an external model? If so, which exception conditions are met, and who approves in writing?
4. Design the consent process: pre-meeting notice text, informed consent form, and how to opt out and request deletion.
5. Set product defaults to the strictest of the three jurisdictions (§4.2).
6. Write the above into the "Data and Compliance" section of the PRD and the internal FAQ of the PR-FAQ.

### 4.7 Common mistakes
- Assuming "it's just product research, not research" means there is no need to ask the IRB. The IRB decides, not the researcher. [Inference]
- Assuming Exempt means "no application needed". The target university states that an application is still required. [Fact]
- Pasting real group meeting transcripts directly into an external GenAI tool for a demo. [Fact] This conflicts directly with the target university's GenAI policy unless an exception condition is met.
- Looking only at Singapore law and ignoring where participants are located (US all-party consent states) and platform terms. [Inference]
- Showing screenshots in an interview that contain real group members' names and unpublished results. [Inference]

---
## 5. Product Teardown Method: User → Scenario → Flow → Feature → Data → Business

### 5.1 Core concepts
- **Purpose of a teardown**: not only to see what a product "does", but to understand "how it does it" and "why it does it that way". [Summary] (practitioner articles such as LogRocket)
- **Common consensus structure**: problem first → user journey → experience and friction → business model → competitor comparison → actionable recommendations. [Summary]
- **Five-layer framework for AI product teardowns** (Institute of AI PM) [Fact]:
  - User Experience Layer: interaction model, how confidence is expressed, how errors are handled.
  - AI Architecture Layer: infer the architecture category from product behavior, and determine where the model's role ends and traditional software begins.
  - Data Strategy Layer: what data would make the product better, and whether the feedback loop compounds.
  - Metrics Layer: the primary success metric, metrics that pull against each other, and tradeoffs the team may have made.
  - Business Model Layer: pricing, unit economics, sources of competitive advantage.

  It also warns: "If your teardown framework is 'describe what I see,' it produces zero transfer."; in interviews, you should "present the teardown in under 5 minutes, leading with the most interesting insight".
- **Practices in the Chinese-language community**:
  - Scenario splitting should be "completely classified" along a single dimension, with each scenario described as "When I...".
  - A user's stated "feature request" is often just the solution they thought of; ask follow-up questions to find where they are really stuck.
  - Don't tear down only surface features, or you end up with a "fake product" that ignores differences in users and positioning.

  [Summary] (summaries from woshipm and 36kr)

### 5.2 The six-layer teardown template in this document (synthesized from the sources above, [Inference])
The six layers given in the task, "user, scenario, flow, feature, data, business", map onto the AI PM five layers:

| Layer | Question to answer | Evidence source | Corresponding AI PM five layer |
|---|---|---|---|
| **1 User** | Who is it built for? Who pays? Who approves? Who is explicitly not served? | Official pricing page, case study pages, job postings | Business |
| **2 Scenario** | In what context and at what frequency is it used? What are the alternatives (including "do nothing")? | Help center, reviews, own trial | UX |
| **3 Flow** | For every step from trigger to completion, where is a human needed? Where does it stop? | Walk through it fully yourself, take screenshots, time it | UX |
| **4 Feature** | Which Kano category does each feature belong to (01 §3.1)? Which are basic? | Feature pages, changelog | UX + Architecture |
| **5 Data** | What goes in, what comes out, where is it stored, is it used for training, is the feedback loop closed? How are errors exposed to the user? | Privacy policy, security whitepaper, trial observation | Architecture + Data + Metrics |
| **6 Business** | How does it charge? What is the unit of value (seat, minute, meeting)? Where is the moat (03 §4 7 Powers)? | Pricing page, financial reports and news | Business |
| **+ Conclusion** | What does it **structurally not do**? What is the small piece that I can do? | Synthesis | — |

### 5.3 Steps
1. **Problem first**: write one sentence, "who this product solves what for", before the teardown, and compare against it afterward.
2. **Walk through the key flow yourself** (not by watching a promo video), taking a screenshot and timing each step, and recording friction points.
3. **Fill in the table layer by layer across the six layers**, labeling each cell [Fact]/[Summary]/[Inference], with a URL and date.
4. **Find the "places where it stops"**: at which step does the flow hand the work back to a human? This is often the gap.
5. **Write "what it structurally does not do"**: derive it from its business model and users, for example "sold per seat to enterprise IT, so it won't localize for students with no budget".
6. **Write 3 actionable conclusions**: what to copy, what to avoid, what to differentiate on.
7. **Compress into a 5-minute spoken version**: open with the most interesting insight.

### 5.4 Common mistakes
- Making only a feature presence/absence matrix (the counterexample to 02 §5 step 6). [Inference]
- Listing "what I saw" without a "why" (the Institute's zero transfer warning). [Fact]
- Saying "it doesn't have X" from impression. This was already proven wrong in round one: Fellow has two-way GitHub sync, Feishu has meeting express delivery (会议速递), and Granola can connect to Linear/Jira via Zapier. [Fact, verified in round one]
- Tearing down a "fake product": ignoring that the other product's target users differ from yours. [Summary]

### 5.5 How to use it in BriefPilot v2: example, teardown of Fellow (fill in only the facts verified in round one; mark the rest as to-do)

| Layer | Content | Grade |
|---|---|---|
| User | Managers and their team meetings (1-on-1s, recurring meetings) | [Inference], needs verification against Fellow's official site |
| Scenario | Continuity of items between recurring meetings: before a meeting, "surface outstanding action items from previous sessions" | [Fact, round one 05 §0] |
| Flow | Meeting → action items → track whether unfinished → resurface before the next relevant meeting; two-way sync with GitHub | [Fact, round one] |
| Feature | Carrying items across meetings is already an **expected/basic** feature, not a blank space; the action item page **shows no "assignee confirmation/claiming"** | [Fact, round one]; "not seen" does not mean "does not exist", so a trial is needed to confirm (06 P0 item 2) |
| Data | Action item extraction accuracy: officially only "human-level accuracy" is stated, **no vendor-published accuracy** | [Fact, round one] |
| Business | Pricing and unit of measurement | **To do** |
| Structurally won't do | [Inference] As a product for enterprise managers, it is unlikely to rebuild its object model for the "advisor–student" relationship and "commitment–experiment result–run link". **But if Fellow ships a 1-on-1 academic template, it can approach option B**, so B's moat is thin | [Inference] |

> **[Inference] Other products to tear down with the same template**: Feishu Minutes (meeting express delivery, enterprise information recognition), Granola (PLG path, and what the 2026-07 lawsuit implies for "silent transcription"), Littlebird (Team plan; three states Kept/In progress/Needs a note; skipping "vague maybes", which directly overlaps with G3 "commitment-strength tiers" and needs a head-on comparison), and the DIY path of "ChatGPT/Claude + pasting minutes" (the 06 review considers it the biggest substitute).

---
## 6. Willingness-to-Pay Measurement

### 6.1 Core Concepts and Method Comparison

| Method | How it works | When it applies | Limitations | Evidence level |
|---|---|---|---|---|
| **WTP conversation (Ramanujam & Tacke, *Monetizing Innovation*, 2016)** | Ask three questions early: "What do you think could be an acceptable price?" / "What do you think would be an expensive price?" / "What do you think would be a prohibitively expensive price?"; segment by willingness to pay rather than demographics ("Segment on willingness to pay, not demographics"); classify features as Leaders / Fillers / Killers; reverse the order: "start with market and price, then design, and then build" | Early stage, small sample, qualitative | What people say is not what they do; needs a follow-up commitment test | [Fact, secondary]: Yevgeniy Brikman's book review was opened and read in full; the original book was not read |
| **Van Westendorp price sensitivity** | Four questions: too cheap (quality doubts) / a bargain / getting expensive / too expensive (would not consider). Plot cumulative curves; their intersections give the acceptable price range, the optimal price point, and the indifference price point | New product launches, repositioning; respondents understand the category | Does not ask about purchase likelihood directly (a purchase-intent question can be added); **data is of low value when respondents are unfamiliar with the category** | [Fact] SurveyMonkey (2021-05-07). Tools do not define "optimal price point" and "indifference price point" identically |
| **Gabor-Granger** | Present a product description, then ask "would you buy this at this price?" at ascending price steps (5 steps with even spacing recommended); compute the cumulative share willing to buy at each price → demand curve → revenue index, and take the peak | Familiar category, a single product with fixed features | Ignores competitors; works poorly for new categories; an overly attractive product description inflates WTP; the revenue index is only a proxy; **at least 100 complete responses per segment** | [Fact] SurveyMonkey (2026-08-26) |
| **Fake door / painted door** | Place a fake entry point inside an existing product and measure clicks | An existing user base | Ethically, users must be told the truth promptly; you cannot charge for something that does not exist | See 05 §4.1 (Amplitude et al., round one) |
| **Pre-sale / commitment currency** | Three kinds of commitment: time, reputation, money (The Mom Test, 02 §4); a prepaid deposit, a letter of intent, writing the product into a funding budget | A clearly identifiable payer | Personal relationships contaminate the signal | See 02 §4 (round one) |

### 6.2 Steps
1. **First distinguish the "user" from the "payer"**: In a research group, the user is the student, while the payer may be the PI's grant, the school, or a corporate funder. [Inference] Ask the wrong person and the WTP data is noise.
2. **Add a three-question WTP conversation at the end of the interview** (asked of the payer), not at the beginning.
3. **Combine Leaders / Fillers / Killers with Kano**: Leaders usually correspond to the core of attractive or expected features; Killers are features that make people not buy when present. For example, "auto-join and record meetings" could be a Killer in research settings ([Assumption, to be validated]).
4. **Use Van Westendorp only when the sample is large enough** (tens of people or more, and a familiar category); Gabor-Granger needs ≥100 responses per segment, so **v2 will not run it**.
5. **Verify what people say with behavior**: For a PI who says they are "willing to pay," make a specific, small, time-bound commitment request, e.g. "If the 4-week trial reaches X, this semester you will pay Y from the tool budget."
6. **Record refusals**: The reasons for refusing (no budget, the school already has a tool, data cannot leave campus) are more informative than "willing to pay."

### 6.3 Common Mistakes
- Asking students "how much would you pay per month." They are not the payer, so the answer is meaningless. [Inference]
- Running Van Westendorp with n=8 and then reporting "optimal price S$X." [Inference] The method itself requires respondents to understand the category, and the sample is far too small.
- Writing a product description that is too attractive and inflates WTP (flagged by SurveyMonkey). [Fact]
- Treating "interested" as "willing to pay" (false evidence, 02 §4). [Inference]
- Running a fake door without disclosing the truth, or charging for something that does not exist. [Fact, 05]

### 6.4 How to Use This in BriefPilot v2
- **[Inference] Reality check**: Willingness to pay for Plan C was flagged in round-one 05 as a fatal weakness ("low willingness to pay"). v2 does not need to prove it "can make money," but it does need to show it knows who would pay and how to validate that; this is the passing bar when an interviewer presses on the "business story."
- **[Assumption, to be validated] Three potential payers**, with 2–3 WTP conversations each:
  - The PI's research grant: ask "What software does the group currently pay for? Who approves it?"
  - Corporate funders of university-industry joint labs, reached indirectly through the PI (the C×E cross-segment raised in 06 review §4).
  - School or university IT: ask "Which meeting or note-taking tools are currently approved? What is the procurement process?"
- **[Inference] Pre-sale commitment**: Ask the 1–2 most enthusiastic PIs: "If group retention in week 4 of the 4-week trial is ≥50%, would you write it into next semester's tool budget or recommend it to neighboring groups?" Even a reputation commitment alone (a recommendation) is stronger than "sounds good."
- **[Inference] No fake door**: In a circle of acquaintances, clicks on a fake entry point carry no information (consistent with the reasoning for "no landing page" in 05 §4.1).

### 6.5 Special Caution on Pre-sales
- **[Inference]** Collecting money from PIs as a student at the target university involves university rules, intellectual property (the university owns research data, §4.5), and conflicts of interest. **v2 collects only "intent," not money**, and will say so honestly in interviews.

---
## 7. PM Interview Case Frameworks and How to Present an AI PM Portfolio

### 7.1 CIRCLES (product design questions)
- **[Fact]** Product School's seven steps (attributed to Lewis Lin):
  1. Comprehend the Situation
  2. Identify the Customer
  3. Report Customer Needs
  4. Cut (via prioritization)
  5. List Solutions
  6. Evaluate Trade-offs
  7. Summarize Recommendations

  Lin suggests clarifying the goal first during the Comprehend step, for example whether an update is meant to drive revenue or stickiness.
- **[Summary/Conflict]** Sources disagree on provenance: Product School says "Developed by Lewis Lin, author of Decode and Conquer"; another source says it first appeared in the 2017 book *The Product Manager Interview*; Blinkist expands the acronym in a completely different way, which is most likely wrong. **Treat *Decode and Conquer* as the reference; the edition still needs to be verified.**
- **[Inference] Limitation**: CIRCLES is an interview structure, not a real discovery process. Real work should go back to the 8 steps in 02. What interviewers fear most is a "memorized framework", so hide the framework inside the content and fill the blanks with real evidence.

### 7.2 Question types and answer essentials

| Question type | Typical prompt | Answer skeleton | Key points / source |
|---|---|---|---|
| **Product design** | "Design a meeting assistant for a research lab" | CIRCLES; first clarify goals, users, and constraints | At Identify, always segment users (students, PI, IT); at Cut, state clearly whom you gave up on [Inference] |
| **Product improvement** | "How would you improve Feishu Minutes?" | First define what "improvement" means as a metric → segment user groups → find where the workflow stalls (the §5 breakdown) → 2–3 options → trade-offs → pick one + metrics | Don't say "add AI"; argue from facts verified in the first round, for example that it already has meeting briefings and enterprise information recognition [Inference] |
| **Metrics** | "Define a north-star metric for X" / "A metric dropped 20%, what do you do?" | North star + input metrics + guardrails (counter metrics); for a metric drop, first clarify the definition, then slice by region, new vs. returning users, platform, etc., and build a hypothesis tree | [Summary] Exponent: the most common PM interview question is "Define the north-star metric/success metrics for X"; guardrails ensure that pushing one goal doesn't harm other priorities; a typical follow-up is "The north star rose but a guardrail fell. Do you ship?" |
| **AI product sense** | "You invented a memory machine. How do you take it to market?" (an OpenAI question, compiled by aced.io) | First interrogate the technology (capability boundaries, failure modes), then cover strategy, a specific user segment, the root problem, three distinct solutions, and an MVP that states what was cut | [Fact] aced.io: "Start by interrogating the technology before you design anything." |
| **AI technical** | "Users complain that Gemini is confident but wrong. How do you fix it?" | Separate training-time causes from inference-time causes → RAG, citations, confidence thresholds + human fallback, an eval set that tracks hallucination rate; when choosing among RAG, fine-tuning, and prompting, take a position first, then state "what would change my mind" | [Fact] aced.io; consistent with 04 §2 domains A/B |
| **Strategy** | "What if a big company enters the space?" | Distinguish competitor types: "A big company entering your space is a distribution threat", while an AI-native startup is a product-architecture threat | [Fact] aced.io; connects to 03 §10 |
| **Behavioral** | "Tell me about a time you did something against your values" (an Anthropic question, compiled by aced.io) | Don't recite STAR; tell a real experience + precise numbers + how you verified it + what you would change now | [Fact] aced.io: generic STAR at Meta, Netflix, and OpenAI "reads as rehearsed" |
| **"Why build this product"** | "Feishu Minutes, Otter, and Fireflies already do this. Why are you still building it?" | The five-step script in 03 §10.2: acknowledge the substitutes → point to the step none of them cover → which group cares most (evidence) → why big companies won't build it first → the seed of a moat and what you gave up | See §7.3 |

> Note: The "company X question" entries in the aced.io compilation are secondhand write-ups and **do not represent those companies' official question banks**. [Summary]

### 7.3 Answering "Why build BriefPilot v2" with CIRCLES (sample skeleton, [Inference]; fill blanks with real evidence)
- **C**: "First, confirming the goal: is it to prove there is a commercial opportunity, or to prove I can find and validate an unmet need? I'll answer for the latter and cover the business side at the end."
- **I**: "The users are PhD students in computational research groups; the hard side is the PI, and the approvers are the university IT and the IRB (§3). I am not serving enterprise IT procurement."
- **R**:
  - "I interviewed __ people and ran a diary study with __ people × 2 weeks. Each person generates __ commitments per week, and __% were not recorded within 48 hours."
  - "The strongest need is not 'generating tasks' but that 'after the work is done, the result and its evidence get disconnected' (G5)."
  - If there is no data yet, say: "This is a hypothesis, and the validation plan is..."
- **C(ut)**:
  - "By the Kano model, transcription, summaries, and cross-meeting carry-over are already basic features (Fellow and others have them), so I cut them."
  - "What remains is the commitment–result–evidence backfill and the 3-second check of the original sentence."
- **L**: Three options, for example a single-user ledger, a mentor confirmation gate, and a PI dashboard.
- **E**: "The mentor confirmation gate has the highest value, but it needs multiple people in the system at once, so the cold start is hardest (§1); the single-user ledger is worth less but can stand on its own."
- **S**: "Build the single-user ledger first and push the network layer to Next. The success bar is retention ≥50% at the 4th group-meeting week (n≥6). There is also a compliance precondition: real data does not leave campus and does not pass through external GenAI (§4.5)."
### 7.4 How to Present an AI PM Portfolio in Interviews
- **[Fact, see 05 §6.1]** The Institute of AI PM's seven-part structure: Problem → Why AI → Your role → Approach → What you built → Results → Learnings. AI-specific elements include model choice, data strategy, **evaluation**, staged rollout, feedback loops, and responsible-AI trade-offs. It should be readable in under 5 minutes.
- **[Fact]** Teardown-style presentation: under 5 minutes, opening with the most interesting insight (Institute, §5.1).
- **[Inference] The 5-minute pitch for BriefPilot v2**:
  1. **Opening insight (30 seconds)**: "Meeting tools have already made 'generating tasks' a commodity feature. What research groups actually lose is 'the outcome and evidence after the work is done'. And at the target university, real group-meeting content is itself subject to research-data and GenAI policies, so cloud tools structurally cannot get in."
  2. **Evidence (60 seconds)**: the competitor error-analysis numbers (06 P0 item 1, **can only be presented once done**) plus the interview and diary numbers.
  3. **Why AI (30 seconds)**: why not rules or templates. The answer: extracting commitments from free text, matching them back to the original sentence, and judging their strength all require language understanding; also explain why the product does "not guess when a field is missing".
  4. **Demo magic moment (90 seconds)**: the single-user ledger's "pre-meeting backfill" plus 3-second verification of the original sentence (05 template D).
  5. **Evaluation and trade-offs (60 seconds)**: evaluation set size, pass rate, main failure modes, refusal rate (04 §4 Q1/Q7).
  6. **Honest boundaries (30 seconds)**: what is unvalidated, what was dropped, and the compliance preconditions.
- **[Inference] Three questions that will definitely be asked, so prepare in advance**:
  - "Why not just paste the minutes into ChatGPT?" → needs data from a controlled comparison experiment (06 P0).
  - "Doesn't Fellow or Littlebird already do this?" → the §5.5 teardown.
  - "Who pays?" → §6.4.

### 7.5 Common Mistakes
- Reciting frameworks and using framework names in place of content. [Inference]
- Answering a metrics question with a single metric and no guardrails. [Summary, Exponent]
- Starting to design for an AI question without first asking about technical boundaries (aced.io). [Fact]
- Writing estimated numbers in a portfolio without labeling them "estimates" (05 §6.1). [Fact]
- Treating a demo as validation (05 §4.1: "Demo ≠ validation"). [Fact]

---
## 8. Build vs Buy vs Integrate

### 8.1 Core Concepts
- **Core vs Context (Geoffrey Moore)**: core is the work that creates differentiation and makes customers willing to pay more; context is work that must be done but does not create differentiation. The common corollary is "build the core, buy the context", with a hybrid option in between: "buy a platform and build the differentiating part on top of it". [Summary]: secondary sources agree; the sources disagree on the bibliographic origin, with some citing *Crossing the Chasm* and others *Dealing with Darwin* (2005), **to be verified**.
- **Commonly used decision dimensions**: differentiation (first and foremost), product fit, total cost of ownership (TCO, including maintenance), time to launch, team capability, compliance. Another view is that the real cost of building is "what that engineer could otherwise have shipped on the core". [Summary]
- **[Inference] New variables in the AI era**:
  - Platform dependence: API terms, pricing, model retirement.
  - Where data goes: directly tied to the target university's GenAI policy (§4.5).
  - MCP and workflow platforms push the cost of "integration" toward zero, so integration itself is not a moat (verified in round 1: Fellow↔GitHub two-way sync, Granola connects to GitHub/Linear/Jira via Zapier, Circleback/Read/Otter already have MCP).

### 8.2 Steps (Decision Table)
1. Break the product into components.
2. For each component, ask four questions:
   - Is it core or context? (If you remove it, would users still choose you?)
   - How mature and how costly is buying or integrating?
   - What are the data and compliance constraints?
   - How costly is it to switch vendors?
3. For each component, choose one of Build / Buy / Integrate / Not now, and write one sentence of rationale.
4. Write the decision up as an ADR with a "review date" (01 §5.2).

### 8.3 Applying It to BriefPilot v2 ([Inference]; decision table for the Now phase, 2–4 weeks)

| Component | core / context | Decision | Rationale |
|---|---|---|---|
| Speech transcription (ASR) | context | **Not now (text first)**; later integrate a local open-source ASR or user-supplied transcripts | Competitors all have it; accuracy on mixed Chinese-English speech is the subject of option D, not the core of option C; the target university's data constraints put a compliance bar on cloud ASR |
| Meeting recording and join-meeting bot | context | **Do not build** | Legal risk of recording consent (§4.2); round 1 already verified that "no bot" is not a differentiator |
| LLM inference | context (the model) / core (prompts, validation, refusal logic) | **Buy (API)** for the synthetic-data demo; reserve an interface for a local or university-approved model on the real-data path | The model itself is not a differentiator; but whether real data can be sent externally is constrained by §4.5, so it must be built as a swappable provider (S0 already has a mock/real provider design) |
| Commitment-extraction schema + strength tiers + no guessing on missing fields | **core** | **Build** | G2/G3; this is the differentiation itself |
| Original-sentence verification (server-side validation of citation pointers) | **core** | **Build (reuse the S0 design)** | 04 §4 Q7 |
| Outcome backfill (five-valued outcome + run/commit link) | **core** | **Build** | G5; the research object model |
| Evaluation set + competitor error analysis | **core (the means of proof and the seed of a moat)** | **Build** | G1/G21; no vendor publishes accuracy figures (verified in round 1) |
| Task system, GitHub Issues, calendar | context | **Integrate (Later)**; Now only exports Markdown | Integration is not a moat; least effort in the Now phase |
| User accounts, multi-user sync | context (single-user phase) → network layer comes first | **Not now**; use a hosted service in Next | Not needed in single-user mode (§1.5) |
| Upstream meeting data (MCP from Otter/Circleback/Read, Feishu export) | context | **Integrate (Next, optional)** | Lets users use BriefPilot on top of existing tools, as a "commitment layer" rather than a replacement (the "layer" positioning of option A) [Inference] |

- **[Inference] The alternative "stitch it together with MCP on Fellow or Granola" must be answered head-on**:
  - You can stitch together "meeting → action item → ticket".
  - What you cannot stitch together is the schema layer: commitment strength, no guessing on missing fields, outcome backfill, and original-sentence verification.
  - Also impossible to stitch together is where the data goes: a cloud toolchain cannot satisfy "real group-meeting data does not leave the university" under the target university's GenAI policy.
  - If testing shows that these two points can in fact be stitched together, building in-house should be abandoned in favor of an "evaluation and workflow solution on top of existing tools". This is the honest exit condition.
### 8.4 Common Mistakes
- Building an integration yourself and treating it as differentiation. [Fact, verified in round one: integrations are not a moat]
- Comparing only API prices, without counting maintenance costs and platform risk. [Summary]
- Buying an off-the-shelf solution for the core, for example using a product's action item extraction directly, so that the differentiation gets outsourced too. [Inference]
- Not writing down a review date, so the decision is never revisited (01 §5.2). [Fact, Cutler]

---

## 9. Product Roadmap and Release Planning (Now-Next-Later), Retrospectives (pre-mortem / post-mortem)

### 9.1 Now-Next-Later
- **[Fact] Janna Bastow (ProdPad)**:
  - She invented Now-Next-Later because she did not want delivery driven by deadlines. The earliest 2012 version was called Current/Near Term/Future.
  - "I dropped the dates and drew three columns: Now, Next, and Later."; "No Gantt chart, no false precision, no buffer time baked into invented deadlines."
  - Granularity of the three columns:
    - Now: what is being worked on.
    - Next: broken down more coarsely, with less detail.
    - Later: "hazy; they're big boulder blocks that you can see in the distance but don't need to break down yet".
  - The advice is to "prioritize problems, not ideas", so the team works toward outcomes.
- **[Inference] Why it fits BriefPilot**: one person, 2–4 weeks, many unvalidated assumptions. A date-driven roadmap only produces "false precision". The eight stages S1–S8 in S0 are exactly this kind of waterfall (01 §8, item 6).

**BriefPilot v2 roadmap draft ([Inference]; each item is written as "problem to solve + exit criteria", not as a feature list)**

| Column | Problem to solve | Deliverables | Condition for moving to the next column (fixed in advance) |
|---|---|---|---|
| **Now (Weeks 1–2)** | Where exactly do competitors go wrong on real group meeting samples? Does my solo-user value hold up? What data can I use within compliance limits? | ① Competitor error analysis (30–100 synthetic commitments, 06 P0 item 1) ② Written inquiries to the IRB and IT (§4.6) ③ Concierge: manually build a "commitment–outcome ledger" for 3 group meetings (05 §4.1) ④ 6–8 Mom Test interviews (if the IRB determines they are allowed) | Competitors show a reproducible high failure rate on ≥1 field; ≥3 people ask to continue after the concierge |
| **Now (Weeks 3–4)** | Can the solo ledger's magic moment be reproduced reliably in a demo? | Solo ledger demo (text input, verification against the original sentence, no guessing on missing fields, pre-meeting backfill) + evaluation set v1 + 5-minute demo script | Evaluation pass rate reaches a pre-set threshold; H-CS1 and H-PLG1 start collecting data |
| **Next (1–3 months, depending on results)** | Can the network layer start to turn? Are advisors willing to confirm? | "Advisor confirmation" (G6) in the exported weekly report, claiming by named people (G4); optional MCP upstream integration | Solo-user week-4 retention ≥50% (n≥6); ≥1 PI gives a reputational or budget commitment |
| **Later** | Can it expand to adjacent groups or segments? Who pays? | PI whole-group dashboard (G17), university–industry joint lab edition (C×E), local ASR + glossary (part of Option D's capabilities) | A payer has expressed intent (§6.4); the compliance path is clear |
| **Won't (explicitly not doing this round)** | — | Meeting-joining bot, automatic recording, sentiment analysis, voiceprint recognition, automatic external sending | — |

### 9.2 Pre-mortem
- **[Fact, partial]** Gary Klein, "Performing a Project Premortem", *HBR* 2007-09: team members "assume that the project they are planning has just failed", then write down the likely reasons for the failure (the HBR page showed only the beginning of the abstract; the full text has not been read).
- **[Summary/Conflict] The 30% figure**: Klein cites research by Mitchell, Russo, and Pennington (1989), saying prospective hindsight "increases the ability to correctly identify reasons for future outcomes by 30%". Secondary commentary points out that the original study measured an increase of about 30% in the **number of reasons generated** and did not assess the quality of those reasons. **When citing it, say only "about 30% more reasons were thought of".**
- **Steps**:
  1. Set the scenario: "It is now 2026-12-01, and the BriefPilot v2 demo has failed."
  2. Everyone writes down the reasons for failure independently. Working solo, write them yourself, then ask the advisor or classmates to write 3 each.
  3. Merge and rank.
  4. For each of the top 5 reasons, write one preventive action and one early signal.
  5. Put them into the roadmap's "exit criteria".
- **[Inference] Pre-written pre-mortem for BriefPilot v2** (for use in the first meeting):

| Possible reason for failure | Early signal | Preventive action |
|---|---|---|
| An interviewer says "I'd just paste it into ChatGPT" and the differentiation collapses | The comparison experiment keeps being postponed | Run the competitor + DIY comparison in Week 1 of Now |
| No access to real data; the demo has only synthetic data and is weakly persuasive | IRB and advisor replies are slow | Send the emails in Week 1; have real group members review whether the synthetic data "looks right" |
| Solo-user value does not hold; nobody uses it 3 times in a row | Nobody asks to continue after the concierge | Go back to Step 1 of 02 §5; do not force the network layer |
| Two weeks of coding with zero user contact | Weekly user-contact time < 1/3 of coding time (01 §4.2) | Fixed weekly interview slot |
| After hands-on testing, Fellow or Littlebird turn out to already cover the core differentiation | During the trial, claiming or outcome backfill is found | Do 06 P0 item 2 first; prepare to switch to alternatives B/D, or shift to an "evaluation-driven" narrative |
| Compliance questions stump me on demo day | Cannot explain where the data goes | Write the §4.6 checklist into the PRD and PR-FAQ |
### 9.3 Post-mortem

- **[Fact] Google SRE**:
  - Definition: "A postmortem is a written record of an incident, its impact, the actions taken to mitigate or resolve it, the root cause(s), and the follow-up actions to prevent the incident from recurring."
  - Blameless: "focus on identifying the contributing causes of the incident without indicting any individual or team".
  - Triggers include user-visible degradation, any data loss, the need for manual intervention, resolution time exceeding a threshold, and monitoring failure; "any stakeholder may request a postmortem".
- **[Inference] Transferring this to product retrospectives**: An SRE postmortem is about an incident, whereas a product retrospective is about a **decision**, for example "why did we choose C in the first place" (Cutler's "No PM retrospectives", 01 §5.2).
- **Product retrospective template ([Inference])**:
  1. The original decision and its rationale, copied verbatim from the ADR.
  2. The metrics and thresholds expected at the time.
  3. Actual results: with n, time window, and measurement method.
  4. Contributing factors to the gap, blameless, looking only at systems and information.
  5. What was learned and which assumption was falsified.
  6. Follow-up actions, each with an owner and a date.
- **Suggested cadence**: Hold a retrospective at the end of each Now cycle (2 weeks); after the demo, run decision retrospectives on ADR-002 and ADR-003 (already required by 01 §5.2).

### 9.4 Common mistakes
- Writing the roadmap as a dated feature list (the practice Bastow argues against). [Fact]
- Breaking the Later column down too finely, which wastes time. [Fact, Bastow: "don't need to break down yet"]
- Using retrospectives to find someone to blame instead of finding system causes (SRE's blameless principle). [Fact]
- Reviewing only failures and not successes. A success can also be luck. [Inference]
- Writing a pre-mortem and never feeding it into the roadmap. [Inference]

---
## 10. End-to-end PM master checklist (Discovery → Definition → Delivery → Measurement → Growth)

> **How to use**
> - This checklist strings together the key points of `00_pm-skills/01–06` into one start-to-finish tick-box list. The parentheses give the source, e.g. "01 §2.1" means section 2.1 of file 01.
> - The standard for ticking an item is **"written evidence (a file path or link)"**, not "I feel it's done" (carried over from 04 §3).
> - Each stage ends with a "gate": if the gate is not passed, do not move on to the next stage.
> - Stage 0 is a prerequisite added in this document.

### Stage 0: Pre-start prerequisites (mindset + compliance + stakeholders)
- [ ] Write down the **outcome** this project is responsible for, not the output (01 §1.1)
- [ ] Commit to "fall in love with the problem first, then with the solution": freeze the list of solutions for now (01 §1.2)
- [ ] Stakeholder list + power-interest matrix (06 §3.3); for key decisions, use DACI to name a single Approver (06 §3.1)
- [ ] Use the decision tree to confirm whether interviews, diaries, and observation count as "research", and **email irb@university.example to get a written determination** (06 §4.4)
- [ ] Complete CITI certification; prepare the informed consent form and the pre-meeting disclosure text (06 §4.4, §4.6)
- [ ] Confirm whether real group meeting data may be sent to an external GenAI, which exception conditions apply, and who approves it in writing (06 §4.5)
- [ ] Get written advisor consent for observing or piloting within the group; confirm the data stays only in storage the target university controls (06 §3.4, §4.5)
- [ ] Recording is off by default; if recording is needed, design the consent flow around the strictest of the three jurisdictions' rules (06 §4.2)
- **Gate 0**: Until the IRB and the advisor have given their determinations, do only dogfooding + synthetic data.

### Stage 1: Discovery
- [ ] Four-risks table, **testing value risk and business viability risk first** (01 §2.1)
- [ ] Starting from your own schlep, list 10–20 candidate **problems** (not products) (02 §5 step 1)
- [ ] The OST root node is a measurable user behavior (02 §2.3, §5 step 2)
- [ ] Observe 2–3 real group meetings plus the 48 hours after each, capturing at least 3 "action item created → lost/survived" chains (02 §5 step 3)
- [ ] Rewrite the interview guide per the Mom Test, deleting every "do you think it's useful?" (01 §2.3, 02 §3.1)
- [ ] 6–10 interviews, spanning ≥2 research groups plus a control group; each interview must yield at least 1 past event, 1 workaround, and 1 commitment (02 §5 step 4)
- [ ] Y model: for every verbatim quote, probe from "need" to "goal" (01 §2.4)
- [ ] 2-week diary study: measure "commitment frequency × 48-hour omission rate" (02 §5 step 5; 06 review P0 item 3)
- [ ] Competitor review mining: ≥10 low-star reviews per competitor, coded by sub-step (02 §5 step 6, 05 template A)
- [ ] **Error analysis on real competitor outputs**: 30–100 items, including a "ChatGPT/Claude + pasted minutes" baseline (04 §4 Q2; 06 review P0 item 1)
- [ ] Break down Fellow, Feishu Minutes, Littlebird, and Granola with the six-layer template, and write down "what it structurally will not do" (06 §5)
- [ ] Genuine vs. false demand: frequency × intensity × commitment, discarding false evidence (02 §4)
- [ ] Importance × satisfaction + Kano, looking at differences across segments (02 §5 step 7, 01 §3.1)
- [ ] Commitment test: ≥5 people give a time commitment, ≥2 give a reputational commitment (02 §5 step 8)
- [ ] At least 1 user touchpoint per week, logged in weekly-touchpoints (01 §2.2)
- **Gate 1**: At least one opportunity must satisfy both conditions: there is user evidence (≥3/6 people independently recount specific events), and the competitor error analysis shows a reproducible failure mode (05 §5.2 H4).
### Stage 2: Definition (Positioning / PRD)
- [ ] User scenario grid + Dunford competitive alternatives analysis, including "do nothing" and DIY (03 §11 step 1)
- [ ] Strategy canvas / ERRC: decide what to eliminate (03 §2)
- [ ] Wedge assessment: build only one step of the workflow (03 §6)
- [ ] Dunford five-element canvas + Moore one-sentence positioning + 7 Powers self-check (03 §1, §3, §4)
- [ ] Differentiation type check: feature, user, experience, or business model; avoid feature-only differentiation (03 §8.5)
- [ ] One-page PR-FAQ with a concrete persona and concrete numbers (01 §3.2, 05 §3.2)
- [ ] Every PRD requirement carries an evidence ID; requirements without evidence go into the assumptions section (01 §3.2, 05 template C)
- [ ] The PRD has an AI-specific section: evaluation, refusal to answer, citation verification, cost of failure (05 §3.3, 04 §3)
- [ ] The PRD has a "Data and compliance" section (06 §4.6)
- [ ] "What we won't do / who we won't serve" and a Won't list (01 §3.3, 06 §9.1)
- [ ] Prioritization: in RICE, items without evidence get Confidence ≤50%; MoSCoW freezes the demo scope (01 §3.1)
- [ ] Cold-start design: a single-player mode exists; the opening conditions for the network layer are written down (06 §1.5)
- [ ] Build / Buy / Integrate decision table; build only the core (06 §8.3)
- [ ] Payer identification + WTP (willingness-to-pay) conversation plan (06 §6.2, §6.4)
- [ ] Answer the ten AI PM questions one by one (04 §4 Q1–Q10)
- [ ] Five-step "why build this anyway" pitch: 3-minute and 20-second versions (03 §10.2, §10.3)
- **Gate 2**: The internal FAQ of the PR-FAQ can answer "why build this anyway" and "who pays" with evidence. Anything it cannot answer must be marked as [Assumption] with a validation plan attached.

### Stage 3: Delivery (MVP / Demo)
- [ ] Now-Next-Later roadmap, where each item is a "problem + exit criterion" (06 §9.1)
- [ ] Pre-mortem: the top 5 failure causes have been folded into the roadmap (06 §9.2)
- [ ] Choose the MVP type by the biggest risk: concierge first, then a single magic-moment demo (05 §4.1)
- [ ] Weekly increments, with something to show users every week (01 §4.1)
- [ ] Weekly user-contact time ≥ 1/3 of coding time (01 §4.2)
- [ ] A workflow rather than an agent, using the simplest architecture (04 §3 I, §4 Q8)
- [ ] Eval set v1 comes from error analysis of real (or reviewed synthetic) traces; Pass/Fail + critique (04 §2 domain A)
- [ ] Citations are verified server-side; refuse to answer when evidence is insufficient; don't guess missing fields (04 §3 III, 05 §0)
- [ ] Actions are classified by reversibility, and high-risk ones go through a confirmation gate (04 §3 IV)
- [ ] Prompts are versioned + regression evals (04 §3 V)
- [ ] Cost / latency broken out by path, **numbers measured, not invented** (04 §4 Q10)
- [ ] The LLM provider is swappable: mock, API, local, or a university-approved model (06 §8.3)
- [ ] The demo uses only synthetic or consented, de-identified data, and states the data source up front (05 template D, 06 §4.5)
- [ ] Demo script: one magic moment + trust boundary + a plan for when the demo fails (05 §4.2–4.3)
- **Gate 3**: The demo's differentiating action can be written as one eval and has one number (04 §4 Q1).

### Stage 4: Measurement (Experiments / Retrospective)
- [ ] Every hypothesis is written as "We believe… We will know we are right when…", with thresholds fixed in advance (05 §5.1–5.2)
- [ ] North Star + leading indicators + trust metrics + guardrails (01 §5.1; 06 §7.2 metrics questions)
- [ ] Activation funnel setup → aha → habit, where aha is not the same as setup (06 §2.3)
- [ ] Retention as cohort curves by "group-meeting week", checking whether they flatten; look at both the individual level and the research-group level (06 §2.3)
- [ ] Every number comes with n, time window, and measurement method; do not report percentages when n is small (01 §5.3, 06 §2.5)
- [ ] Structured thumbs-down + user-correction triples flow back into the eval set (04 §3 VII, §4 Q5)
- [ ] Run error analysis every 2–4 weeks (04 §3 VIII)
- [ ] One blameless post-mortem per Now cycle; ADRs get their outcomes filled in when the review date arrives (06 §9.3, 01 §5.2)
- [ ] Results are compared against "supports, contradicts, mixed → action" and executed according to the pre-commitment (05 template E)
- **Gate 4**: At least one core hypothesis has a supported or contradicted conclusion, and the pre-committed action was taken (including abandoning it).

### Stage 5: Growth (Cold Start / Monetization / Storytelling)
- [ ] Define the atomic network (one research group) + incentive design for the hard side (the PI) (06 §1.3)
- [ ] Open the network layer (claiming, advisor confirmation, dashboard) only after single-player retention meets its target (06 §1.5, §9.1)
- [ ] "Single-player → multi-player" overflow point: a weekly report export with verbatim quoted sentences (06 §1.5)
- [ ] Attack one atomic network at a time, then expand to adjacent groups or segments following the bowling-pin strategy (03 §3; 06 §1.3)
- [ ] Education-market procurement path: individual → research group → school or university, with the decision-maker and compliance threshold at each level (06 §2.4, §3.3)
- [ ] WTP conversations with ≥2–3 payers; collect intent, not money (06 §6.4–6.5)
- [ ] Where the first 10 users come from: list and channels (the GTM gap in 06 review §5)
- [ ] Portfolio case study in seven sections, with facts, assumptions, and estimates written separately (05 §6)
- [ ] Interview preparation: CIRCLES framework, metrics questions, AI technical questions, "why did you build this", a 5-minute decomposed storytelling (06 §7)
- [ ] Handle the three must-ask questions: DIY ChatGPT, Fellow/Littlebird, who pays (06 §7.4)
- **Gate 5**: Within 5 minutes, you can explain with evidence: who it is for, why current tools are not enough, what I proved, what I gave up, and what to validate next.
### Cross-cutting: PM common-mistake self-check (stop as soon as any one appears)
- [ ] Starting with a solution, then looking for a problem (01 §8 #1)
- [ ] Writing a PRD without validation (01 §8 #2)
- [ ] Feature-parity thinking (01 §8 #3)
- [ ] Caring only about feasibility and usability (01 §8 #4)
- [ ] Big-batch delivery or waterfall (01 §8 #6)
- [ ] Using n=1 (yourself) to represent users (01 §8 #8)
- [ ] Writing the rubric before looking at the data (01 §8 #9)
- [ ] Treating setup as the aha moment (06 §2.5)
- [ ] Building multi-user features on day one (06 §1.4)
- [ ] Sending real data to an external GenAI without permission (06 §4.7)
- [ ] Asking a non-payer "how much would you pay?" (06 §6.3)
- [ ] Treating self-built integrations as a moat (06 §8.4)
- [ ] Writing the roadmap as a dated feature list (06 §9.4)

---

## 11. Source list (all accessed at the time of writing)

**Cold start and network effects**
1. [Fact] Andrew Chen book excerpt "The Atomic Network", Lenny's Newsletter: https://www.lennysnewsletter.com/p/atomic-network
2. [Fact] Chris Dixon, "Come for the tool, stay for the network" (2015-01-31): https://cdixon.org/2015/01/31/come-for-the-tool-stay-for-the-network
3. [Summary] Antoine Buteau, *The Cold Start Problem* book summary: https://www.antoinebuteau.com/the-cold-start-problem-book-summary/
4. [Summary] Frog Capital book review: https://frogcapital.com/think-frog/the-cold-start-problem-by-andrew-chen/
5. [Summary, to be verified] Goodreads reader notes (Slack 2,000 messages / 93%): https://www.goodreads.com/notes/56962799-the-cold-start-problem/84411704-mikko-ikola/435bc888-c6a7-45f1-83c2-6c66617e1ab2

**PLG and retention**
6. [Fact] Elena Verna, "Hey B2B, I bet you are measuring activation wrong": https://www.elenaverna.com/p/hey-b2b-i-bet-you-are-measuring-activation
7. [Fact] Lenny Rachitsky, "What is good retention?" (2020-06-09): https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29
8. [Summary] Sacra interview with OpenView partner Blake Bartlett (PLG definition): https://sacra.com/research/blake-bartlett-openview-future-product-led-growth
9. [Summary] Pendo, "Product-led growth and the age of the end user": https://www.pendo.io/pendo-blog/product-led-growth-and-the-age-of-the-end-user/
10. [Summary] CleverTap's paraphrase of Brian Balfour's views on retention: https://clevertap.com/blog/brian-balfour-reforge-retention-matters/
11. [Summary] Practitioner's paraphrase of the Reforge activation framework (setup/aha/habit): https://www.june.so/blog/activation-playbook
12. [Fact] UCLA DTS (2025-03-14) campus-wide Overleaf license: https://dts.ucla.edu/news/overleaf-scheduled-enhancement-monday-47
13. [Fact] Overleaf for Universities: https://www.overleaf.com/for/universities
14. [Fact] Notion for Education: https://www.notion.com/product/notion-for-education
15. [Summary] University of Virginia Library's centralized Overleaf procurement: https://library.virginia.edu/data/research-software/overleaf

**Stakeholders**
16. [Fact] Atlassian Team Playbook, DACI: https://www.atlassian.com/team-playbook/plays/daci
17. [Summary] Mendelow power-interest matrix (LogRocket): https://blog.logrocket.com/product-management/stakeholder-matrix
18. [Summary] Mendelow's Matrix (LearnSignal): https://www.learnsignal.com/blog/mendelows-matrix/
19. [To be verified, 403] CIO.com, RACI: https://www.cio.com/article/287088/project-management-what-is-raci-and-how-does-it-improve-clarity.html

**Compliance**
20. [Fact] Target university IRB, "Do I Need IRB Approval": (university page; link removed)
21. [Fact] Target university IRB, "Students conducting human subjects research": (university page; link removed)
22. [Fact] Target university IRB, "Exempt Review": (university page; link removed)
23. [Fact] Target university Research Data Policy: (university page; link removed)
24. [Fact] Target university Policy on the Use of Generative AI in Research (published 2023-07-04, reviewed 2025-11-07): (university page; link removed)
25. [Summary] Target university Research Data Classification and Handling Guide (staff access only): (university page; link removed)
26. [Summary] PDPC Advisory Guidelines on Key Concepts (2017 revised edition): https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/overview-of-dp-provisions---ch-10-(270717).pdf
27. [To be verified, body text not loaded] PDPC Data Protection Obligations: https://www.pdpc.gov.sg/Overview-of-PDPA/The-Legislation/Personal-Data-Protection-Act/Data-Protection-Obligations
28. [Summary] Linklaters, "Data Protected – Singapore" (excluding personal or domestic capacity): https://www.linklaters.com/en/insights/data-protected/data-protected---singapore
29. [Summary] SingaporeLegalAdvice, "Can an organisation record a conversation without consent?": https://singaporelegaladvice.com/can-an-organisation-record-a-conversation-without-consent/
30. [Summary] RecordingLaw, Singapore: https://www.recordinglaw.com/singapore/recording-laws/
31. [Fact] Full text of the Personal Information Protection Law of the People's Republic of China (published by the Cyberspace Administration of China): http://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
32. [Fact] China Justice Observer, "Can Secret Recordings Be Used as Evidence in Chinese Courts?" (2019-11-23): https://www.chinajusticeobserver.com/a/can-secret-recordings-be-used-as-evidence-in-chinese-courts
33. [Fact] Digital Media Law Project, "Recording Phone Calls and Conversations": https://www.dmlp.org/legal-guide/recording-phone-calls-and-conversations

**Product teardowns**
34. [Fact] Institute of AI PM, AI PM Product Teardowns: https://www.institutepm.com/knowledge-hub/ai-pm-product-teardowns
35. [Summary] LogRocket, Product teardown process: https://blog.logrocket.com/product-management/product-teardown-process-tools/
36. [Summary] Everyone Is a Product Manager (scenario breakdown): https://www.woshipm.com/pmd/734280.html

**Willingness to pay**
37. [Fact] SurveyMonkey, Van Westendorp (2021-05-07): https://www.surveymonkey.com/learn/market-research/van-westendorp-price-sensitivity-meter/
38. [Fact] SurveyMonkey, Gabor-Granger (2026-08-26): https://www.surveymonkey.com/learn/gabor-granger/
39. [Fact, secondhand book review] Yevgeniy Brikman, review of "Monetizing Innovation": https://www.ybrikman.com/blog/2023/04/01/monetizing-innovation/

**Interviews**
40. [Fact] Product School, CIRCLES: https://productschool.com/blog/skills/circles-framework-guide
41. [Fact, compilation] aced.io (formerly Exponent) AI PM interview questions: https://www.aced.io/blog/ai-product-manager-interview-questions
42. [Summary] Exponent/aced metrics-question course (partly paid): https://www.tryexponent.com/courses/pm/analytical/how-to-answer-metrics-questions

**Roadmaps and retrospectives**
43. [Fact] Janna Bastow, ProdPad, "I invented the Now-Next-Later roadmap": https://www.prodpad.com/blog/invented-now-next-later-roadmap/
44. [Fact] Google SRE Book, "Postmortem Culture": https://sre.google/sre-book/postmortem-culture/
45. [Fact, abstract section only] Gary Klein, "Performing a Project Premortem", HBR 2007-09: https://hbr.org/2007/09/performing-a-project-premortem
46. [Summary] The pre-mortem "30%" claim and its critiques (secondhand): https://resources.rework.com/libraries/project-management/pre-mortem

**Build vs buy**
47. [Summary] Practitioner overview of the Core vs Context framework: https://www.codestringers.com/articles/build-vs-buy-software-decision-framework

**Facts carried over from the first round, already verified (not reopened this round)**: Fellow↔GitHub two-way sync, cross-meeting carry-over, and no ownership claiming seen on the action item page; Granola connects to GitHub/Linear/Jira via Zapier; Circleback/Read/Otter have MCP; Littlebird's Team plan and its three states; Feishu meeting digest and enterprise information recognition; no vendor publishes accuracy figures; the Granola class-action lawsuit of 2026-07-30 (3:26-cv-07926-EMC). For sources, see the source lists in `01_market-research/05_gap_synthesis_opportunities.md` and `01_market-research/06_research_integrity_review.md`.
---

## 12. Confidence Notes for the Conclusions in This Document

- **Most reliable ([Fact], official original pages)**: the three university IRB pages, the university research data policy, the university GenAI policy, the text of the PIPL (Personal Information Protection Law), the DMLP list of states with recording-consent laws, Atlassian DACI, Google SRE postmortem, ProdPad Now-Next-Later, Lenny's retention benchmarks, Elena Verna on activation, Chris Dixon's original piece, the Chen book excerpt, the two SurveyMonkey pricing-method articles, and the UCLA/Overleaf/Notion education pages.
- **Medium ([Summary])**: the specific Singapore rules on recording and the PDPA (mainly from commercial legal information sites and law-firm summaries; the body text of the official PDPC pages did not load this round), the Reforge framework, the OpenView PLG definition, Mendelow/RACI, the source of Core vs Context, and the 30% figure for pre-mortems.
- **Explicit conflicts and items to verify**:
  - The DMLP says "eleven states" but lists only 10; Illinois's current status has not been checked.
  - Lenny's enterprise SaaS benchmark: 70% and 75% both appear in the text.
  - The first source of CIRCLES (*Decode and Conquer* or the 2017 book).
  - Slack's 2,000 messages / 93%.
  - PDPA penalties and the research exception.
  - The original wording of the university's "non-academic surveys need no approval" rule.
  - PIPL Articles 29 and 38.
  - Reforge being acquired by Miro.
- **[Inference] judgments most in need of challenge**:
  1. "Group meeting content most likely counts as university research data and is subject to the GenAI policy." This needs confirmation from the university IT office or IRB, **and also a check on whether the university already has an approved enterprise-grade AI or meeting tool**; if it does, the argument that "cloud tools structurally can't get in" has to be weakened.
  2. "Atomic network = one research group, hard side = the PI." This comes from analogy and has no user evidence.
  3. The candidate events for activation and the aha moment, and thresholds such as 50%. All of these are [Assumption · to be validated]; the thresholds need to be fixed after discussion with the advisor or peers, before the first experiment.
- **Not covered in this document; suggested for the next round**: A/B testing and SQL metric breakdown (listed in §5 of the 06 review, but outside the scope of this task), GTM and the initial user list, and accessibility.
