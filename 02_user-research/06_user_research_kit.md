---
title: "User Research 06: User Research Execution Package (Interview Guides / 2-Week Diary Study / Recruitment / Ethics / Analysis Templates)"
status: "ready-to-execute v1.1 (final revision: §4.4 adds D13, D14, D15, F4; §1.2 adds a 'corresponding positioning hypothesis' column and a decision tree based on the final positioning; hypothesis IDs in this document now carry the prefix U-H. All 'research findings' fields are empty, pending execution by the user)"
sources_count: 21
---

# User Research 06: User Research Execution Package — Interviews, Diary Study, and Recruitment You Can Start Tomorrow

> **What problem this document solves**
> The first-round integrity review (`01_market-research/06_research_integrity_review.md`) lists "zero first-hand user evidence" as a P0: an interviewer only needs to ask, "How many people have you interviewed? How many commitments per week do your users miss?", and the current answer is "0 people, no data." This document produces no findings. It produces only **tools that can be executed immediately**: what to validate, whom to find, how to ask, how to record, how to judge, and when to be done.
>
> **Labeling conventions** (used across the whole project):
> - **[Fact]** The original page was opened; URL and access date attached.
> - **[Summary]** Only the search-result summary was seen; the original page was not opened.
> - **[Inference]** Derived from facts; the source does not state it directly.
> - **[Assumption · to be validated]** A judgment or expectation set by this document, which must be confirmed or refuted by the results of execution.
> - **To be verified**: the page could not be opened, or sources contradict each other.
>
> **Search notes for this round**: WebSearch was available this round, with 3 searches run in total. WebFetch opened 10 official pages of the target university's IRB and 1 Mom Test book excerpt. The PDPC page opened but its body text did not render, and the Singapore statutes site returned 403; both are marked "to be verified". The methodology sources (Torres, NN/g, the Four Forces, YC) reuse the conclusions already checked in `00_pm-skills/02`; they were not reopened this round and are flagged separately.
>
> **Hard rule**: this document and the subsequent `07_研究发现` (research findings) **must not contain any interview, interviewee quote, or data that did not actually happen**. All template fields stay blank until real execution.

---

## 0. One-Page Overview (Conclusion First)

| Item | Content |
|---|---|
| Core question to answer | In computational research groups (Option C) and PhD student–advisor 1-on-1s (Option B), is "verbal commitment in a meeting → not recorded afterward → forgotten or disputed" a problem that is **weekly, costly, and not caught by existing tools**? Are advisors and students willing to pay a small cost for closing the loop? Is the enterprise ML team comparison group equally affected? |
| Method mix | ① Mom Test interviews, 12–16 people (three interview guides) ② 2-week event-triggered diary study, 5–6 people (including the project owner's own R0) ③ Commitment-currency test at the end of interviews ④ Week-2 "concierge" backfill test (validates Q4) |
| Pre-defined failure lines | The 14 hypotheses in §1, each with an evidence standard for "supported / not supported / gray zone". **Locked before execution and not changed during it**; any change must record the reason and date |
| Sample | PhD students 5, master's students 2, PIs 3, postdocs 1–2, enterprise ML comparison 3–4, joint university–industry lab 2 (§2.3) |
| Ethics | The target university's IRB requires that "research involving human subjects at the target university" be approved by the IRB before it begins, with interviews and surveys listed among the examples; but research "about products or methods rather than about people" and "non-academic research" generally do not need it. This project falls in a gray zone, so **before the first interview, email irb@university.example to request a determination** (§6) |
| Timeline | Week 1 (11/02–11/08): send the IRB determination email, start own R0 diary, interview 4 people; Week 2 (11/09–11/15): the diary study formally starts, interview 5–6 more people, run the concierge backfill test; Week 3 (11/16–11/22): diary wrap-up, exit interviews, complete analysis, make decisions against the failure lines (§8) |
| Outputs | `07_research_findings.md` (research findings; fill in following the §7.4 skeleton), and an updated opportunity–solution tree |

**[Inference] Why do this first instead of writing code**: the conclusion of the 05 gap synthesis is that all option rankings are "only an order worth validating first, not conclusions" (05 §0, item 6). If Q3 (frequency) and Q4 (whether advisors and students are willing to bear a cost) are refuted, the demos for Options B and C would be code written for a problem that does not exist. Taking the first 2 weeks of the 2–4 week demo budget and running this in parallel with demo data preparation and competitor error analysis (05 Q1) will not slow progress.

---

## 1. Research Goals and Hypothesis List (with Pre-Defined Failure Lines)

### 1.1 Research Goals

| ID | Goal | Corresponding 05 open question | What it decides |
|---|---|---|---|
| RG1 | Measure a first-hand baseline for "commitment frequency × 48-hour recording rate × post-hoc forgetting/dispute rate" | Q3 | Whether Options B and C are worth building; whether a real number can be cited in interviews |
| RG2 | Judge whether advisors and students are willing to pay the closing-the-loop cost (advisor weekly confirmation under 5 minutes, student backfill about 30 seconds) | Q4 | The make-or-break line for Options B and C |
| RG3 | Judge whether "advisor commitments to students" is a real pain point, and whether students selectively withhold information from advisors | Q5 | Whether Option B can be differentiated from Fellow and Littlebird; sharing-granularity design |
| RG4 | Judge whether recording and third-party cloud are hard thresholds or mere preferences | Q8 | Whether G7, G13, G19 (consent-first, text-first, local execution) are selling points |
| RG5 | Pin down the paying unit and payment path (per person or per group; individual, grant funds, or university; the funder of joint university–industry labs) | Q13 | Whether the business story is left with only "portfolio value" |
| RG6 | Use enterprise ML teams as a comparison: does the pain come from "R&D semantics" or "academic relationships" | 06 review §4 | The expansion path for Option C; whether to differentiate on "research" or on "R&D" |
| RG7 | Use Switch interviews to get the real reasons for having abandoned a meeting AI tool | 00/02 §2.2 | Whether differentiation lands on Push/Pull or on Anxiety/Habit |

**Not goals**: validating the BriefPilot interface; collecting votes on "which feature do you like"; selling to anyone.
### 1.2 Hypothesis List and Failure Lines

**How to read this table**:
- Each hypothesis first states a **behavioral metric** (something that can be counted), then a judgment line.
- The judgment lines are **[Assumption · to be validated]** set by this document, not thresholds given in the literature. They exist for one purpose only: to prevent "moving the goalposts" after execution.
- Interview samples are small (2–5 people per group), so always report **n/N** (e.g., "3 of 5 people"). **Do not report percentages and do not run statistical tests.** Diary study results are summarized by "person × week", reporting the median and range.
- The standard for "can describe a specific event" is: the person can give an approximate date (which week), which meeting, who was involved, and what happened afterward. Answers that only say "often" or "usually" do not count.

> **Numbering (v1.1)**: IDs in this table are always read as **U-H01…U-H14** (U = user research), to distinguish them from the **P-H** IDs in positioning and the **E-H** IDs in eval-kit. The rightmost column, "Corresponding positioning hypothesis", is new in v1.1.

| ID | Hypothesis ([Assumption · to be validated]) | Source | Evidence source | Pass line | Fail line | How to handle the gray zone | Decision consequence if it fails | Corresponding positioning hypothesis (v1.1) |
|---|---|---|---|---|---|---|---|---|
| **U-H01** | PhD and master's students have at least 1 experience per week of "being unable to recall the advisor's or the last group meeting's specific requirements, and having to check records or ask someone" | 05 Q3; U1 H1 | Diary field D10; interview PhD-Q7 | Among diary participants (excluding R0), **≥3/5** have a person-week median of ≥1 occurrence; in interviews, ≥3/7 students can describe a specific event from the past 2 weeks | In the diary, **≤1/5** have a person-week median of ≥1 occurrence, **and** in interviews ≤1/7 can describe a specific event | Anything else is the gray zone: extend the diary by 1 week, or add 2 students from outside this group | Plan B's "bring unclosed items back before the next meeting" is downgraded to a secondary feature | P-H4 (supporting: pre-meeting recall) |
| **U-H02** | The share of verbal commitments made in a meeting that are not written down anywhere (notes, group chat, documents, task tools) within 48 hours is ≥30% | 05 Q3; U1 §3.1; 00/02 §6 B6 | Diary D7 and 48-hour follow-up F1; live observation of 1–2 meetings of this group | Aggregate 48-hour **unrecorded rate ≥30%**, and at least 3 participants each at ≥20% | Aggregate unrecorded rate **<15%** | 15%–30%: check whether the unrecorded items are hard or soft commitments; if soft commitments are the majority, treat as "fails" | If it fails: "recording" is not the pain point; the pain can only be in "recorded but never closed" (see U-H04, U-H11) | P-H5 (adjacent metric to write-back rate) |
| **U-H03** | Losing a commitment has a perceptible cost (redoing experiments, missing a deadline, being criticized by the advisor, two people doing the same thing, an awkward group meeting) | 00/02 §6 A3 (Mom Test cost question) | Interviews PhD-Q8, PI-Q2; diary F2 | **≥4/8** students and postdocs can describe a specific cost event from the past 3 months and can state the cost (how many hours spent, how many days delayed) | **≤2/8** can describe one, or can only say "it's a bit of a hassle" | Can describe an event but cannot state a cost: record as a Hard Fact signal ("everyone's like this") and analyze separately | If it fails: the problem is "annoying", not "painful"; downgrade to a portfolio narrative and do not tell a commercial story | **P-H5** (cost events; former P-H9 merged in) |
| **U-H04** | Students are willing to spend about 30 seconds, when a commitment is "done", to fill in one sentence of result and one evidence link (run, commit, figure) | 05 Q4; U3 H-A, H-B | Week 2 manual fill-in test (§4.6): before the next meeting, the researcher manually sends "the N things you promised last time: reply with a one-line result and a link" | Fill-in rate (items filled in / items sent) **≥50%**, and ≥3 participants fill in at least 1 item | Fill-in rate **<30%**, or most people reply "I remember it myself" or "it's in W&B" | 30%–50%: check whether people reply with only the result and no link; replying with only the result suggests the "link" is superfluous design | Plan C's "result–evidence chain" does not hold; fall back to Plan A or B | P-H6 (fill in run link) |
| **U-H05** | PIs are willing to spend under 5 minutes per week confirming the commitment and decision drafts that students submit | 05 Q4; U3 H-C | Interview PI-Q4 (past behavior: what they did the last time they received a student's post-meeting summary); commitment test: ask PIs to confirm 2 manually prepared drafts within 2 weeks | ≥2/3 PIs **actually confirm** at least 1 draft within 2 weeks (replying "confirmed" or editing it also counts) | 0/3 actually confirm, or a PI explicitly says "let the students manage it themselves" | Only 1 PI confirms: find 2 more PIs from neighboring groups | Plan B's "advisor confirmation gate" does not hold; change to "student's private ledger + selective sharing" | Entry condition for Bottleneck 2 |
| **U-H06** | "The advisor's commitments to students" (granting access, introducing collaborators, revising drafts, writing recommendation letters) get delayed, and students are reluctant to chase them | 05 Q5; U1 H2 | Interviews PhD-Q5, PI-Q3 | ≥3/7 students can describe one instance in the past 3 months where the advisor agreed, delayed by 1 week or more, and the student did not chase or chased only after a long time; and ≥1/3 PIs admit to having done this themselves | ≤1/7 students can describe one | Student can describe one but says "a quick nudge fixes it, not awkward": low pain, treat as fails | Plan B's "two-way commitments" is no longer a differentiator | U5 (downgraded to baseline requirement); D15 social dynamics |
| **U-H07** | Students show the advisor fewer records than they keep privately (selective sharing) | 05 Q5; U1 §6.3 (c) | Interview PhD-Q15 (ask "what was the last thing you deliberately left out of the weekly report", not "would you be willing to") | ≥3/7 students describe a specific instance of "left it out" and the reason | ≤1/7 | — | This hypothesis **does not decide whether a plan lives or dies**; it only determines sharing granularity: if it holds, "student-owned, shared after confirmation"; if it fails, a group-wide dashboard is possible | Follow-up question: default to private drafts |
| **U-H08** | Recording and third-party cloud AI tools are a **barrier** in labs, not a preference | 05 Q8; U3 H-E | Interviews PhD-Q13, PI-Q9, ENT-Q7; check the target university's IT policy | ≥3 interviewees describe a specific instance of "wanted to record or use AI transcription and was refused by the advisor, group members, a collaborator, or policy"; or a written policy restriction from the target university is found | Most interviewees already use Otter, Feishu Minutes, or ChatGPT on group meeting content and cannot recall a single refusal | Some people are worried but there is no refusal event: record as "Anxiety", not a barrier | G7 and G19 are downgraded to "nice-to-have"; the demo does not invest more in privacy | **P-H10** |
| **U-H09** | Labs have a viable payment path: in the past 12 months a PI bought some SaaS with grant funds or a personal card and can clearly describe the process | 05 Q13; U1 H6 | Interview PI-Q8; university–industry joint lab member CL-Q3 | ≥2/3 PIs can describe one specific purchase (what was bought, who paid, what process, how long approval took) | All PIs only use tools the university has already procured and cannot describe a single self-initiated purchase | — | Commercial story shifts to university–industry joint labs or enterprise ML teams (see U-H13) | Commercial story (Bottleneck 3) |
| **U-H10** | Enterprise ML teams' pain points are **different from labs'**: their action items already go into Jira, Linear, or GitHub, and the loss mainly occurs in "experiment results and decision rationale", not in "who promised to do what" | 06 Review §4 control-group recommendation | Enterprise control interviews ENT-Q2, ENT-Q3, ENT-Q6 | ≥3/4 enterprise interviewees can describe the closed-loop process for action items in a task system, but cannot say where decision rationale is stored | Enterprise interviewees describe the same loss pattern as lab students (the same loss of "who promised") | — | **Both outcomes are useful**: if it holds, differentiation lies in "academic relationships" (Plan B direction); if it fails, differentiation lies in "R&D semantics" (Plan C can extend to enterprise ML, with a better commercial story) | Bottleneck 4; P-H10 control |
| **U-H11** | When writing papers or replying to reviewers, the frequency of decision lookback ("why did we set it up that way back then") is high enough | U3 H-D; 05 G12 | Interviews PhD-Q10, PostDoc same question (reviewing their last paper) | ≥3/6 interviewees with submission experience can describe **≥3 specific lookbacks** (scrolling chats, checking old slides, asking collaborators) during the writing or rebuttal of their last paper | ≤1/6, or all say "just ask a peer" | U3 originally set the threshold at "10 or more per paper"; this document lowers it to 3 specific events because recall underestimates; **this is a downward adjustment, recorded here** | G12 decision-lookback Q&A is removed from the demo | PRD US-16 (P2) |
| **U-H12** | The main reason interviewees abandoned meeting AI tools is anxiety (privacy, errors) or habit (group chat plus Excel), not insufficient features | 00/02 §2.2 Four Forces; 05 Plan A | Switch interviews PhD-Q12, ENT-Q4 | Among those who describe a specific abandonment event, more than half have Anxiety or Habit as the main reason | More than half have features as the main reason (inaccurate transcription, no Chinese support, no offline support) | Those who cannot describe an abandonment event are not counted in the denominator | If it fails: differentiation should go through features (Plan D, bilingual Chinese–English terminology), not trust design | — |
| **U-H13** | University–industry joint labs have a need for "milestones and deliverables confirmed by both sides" after funder meetings, and there is a paying party | 06 Review §4 new segment | University–industry joint lab interviews CL-Q1 to CL-Q4 | 2/2 interviewees describe a specific instance of "promised the funder a deliverable in a meeting, and afterwards the two sides understood it differently", and can say who manages the funds | 0/2 | Only 1 person found: mark as "signal, more samples needed" | If it holds: write it into `03_positioning` as the intersection of Plan C and Plan E | Entry condition for Bottleneck 3 |
| **U-H14** | Being named but not believing one actually agreed ("claiming" disputes) has genuinely happened in the past 3 months | 05 G4, Plan A | Interviews PhD-Q8, ENT-Q5 | Across all interviewees, ≥4 people describe a specific dispute | ≤1 person | — | Plan A's "named person claims" is downgraded | — (claiming is only an AI-suggested item; Fellow already has it) |

**[Inference] Decision Tree A: interpretation by the final positioning (`03_positioning/03_final_positioning.md` decision-v1.1) — new in v1.1, use first**:
1. **P-H12 concierge gate** (end of W2): 0/2 classmates willing to paste the manual reconciliation sheet into slides / weekly report → stop UI development and deliver only the evaluation work; no need to wait for diary results.
2. **P-H4** (D13): the share of status changes that first appear verbally in the group meeting is <25% → switch the main axis to "multi-source reconciliation" (add group chat export as input), or abandon the main axis; ≥50% → the main-axis premise holds.
3. **P-H5** (F4 + U-H03): write-back rate ≥80% **or** cost events ≤2/8 → the pain point does not hold (not writing back may be rational: nobody checks); in that case, if P-H6 holds, switch to "decision × run check" as the main axis, otherwise keep only the evaluation work. Write-back rate ≤50% **and** ≥4/8 describe a cost → holds.
4. **P-H6** (D14 + review of one's own notes): person-week median of commitments / decisions with explicit conditions <1, or real drift 0–1 times → delete the "condition mismatch" from the second beat; the stale-data check (F08b) is unaffected.
5. **P-H7** (trial, `eval-kit/templates/h7_dogfood_log.md`): 0 people with binary retention in week 2 → ask why; if "no text", add a 3-line shorthand entry point and retry for 2 weeks. Also look at **D15** and "where follow-up questions are sent": if most people "don't dare ask the advisor follow-ups in the group chat", keep follow-ups as private drafts and do not build any "one-click send to group".
6. **P-H10** (U-H08 + the target university's IT reply): decides FAQ wording and which model dogfood uses.

**[Inference] Decision Tree B (the old version for the first-round Plans A–F, kept on file; where it conflicts with Decision Tree A, A prevails)**:
1. **Both U-H01 and U-H02 fail** → the core premise of Plans B and C disappears → return to 05 §4, prioritize Plan A (horizontal "verifiable commitment layer") or Plan D, and in interviews honestly say "I ran a 2-week diary and found that labs don't actually lose commitments" (which is itself a good story).
2. **U-H01 or U-H02 holds, U-H04 fails** → students are unwilling to fill in → change Plan C's "result–evidence chain" to "automatically find evidence from Git and W&B" (higher cost), or switch to Plan B.
3. **U-H01 or U-H02 holds, U-H05 fails** → Plan B drops the "advisor confirmation gate" and becomes a student private ledger.
4. **U-H10 fails (enterprises hurt just as much)** → Plan C's narrative changes from "research" to "R&D teams", strengthening the commercial story.
5. **U-H08 holds** → G7, G13, G19 move into the demo's P0; if it fails → still build text input (because it is easier engineering-wise), but do not pitch it as a selling point.

---
## 2. Recruitment Plan

### 2.1 Target Population and Screening Principles

- **Behavior first, not job title**: Recruit only people who "actually attended at least one group meeting or one-on-one in the past 2 weeks."
- **Recruitment copy mentions neither AI nor the product**. It says only "studying how things get followed up after a research team's meeting." The original research plan already pointed out that mentioning AI makes people interested in AI more willing to participate, which overestimates acceptance (the earlier v1 docs (not included), §4).
- **Control self-projection bias**: Interviewees from the project owner's own group make up no more than 40% of the academic sample. At least 1 comes from a non-computational lab (for example, a wet lab) as a boundary sample (the mitigation in U1 §14).
- **Power relations**: Do not recruit students in the project owner's own group through PI instructions. Interview content from the own-group PI and own-group students is not disclosed to each other (§6.4).

### 2.2 Channels

| Channel | Reachable population | Approach | Label |
|---|---|---|---|
| Own group (the computational lab of the project owner) | PhD students, master's students, postdocs, PIs | Invite in person or by private message; do not single people out publicly in the group chat | [Fact] project owner's background |
| Adjacent groups (same school, same floor, or sharing a GPU cluster) | PhD students, PIs | Ask own-group peers for referrals (snowballing); at the end of each interview ask "who else should I talk to?" | [Inference] |
| Target-university industry joint labs | Student researchers, research engineers, project PIs | The university's official industry collaboration page lists joint labs with multiple companies (e.g., the Rolls-Royce and Alibaba joint labs); start with joint labs in the same school and go through personal introductions | [Summary] (university page; link removed), search snippet from at the time of writing, original page not opened; for the NRF corporate lab programme see https://www.nrf.gov.sg/programmes/corp-labs/, also [Summary] |
| Corporate ML teams (comparison group) | ML engineers, research scientists, and ML team leads at companies in Singapore or China | LinkedIn alumni, graduated senior labmates, internship colleagues | [Inference] |
| Academic community (backup) | PhD students from other universities | Use only if the sample within the target university is insufficient | [Inference] |

### 2.3 Sample Size and Quotas

| Segment | Interview target | Own-group cap | Diary study | Quota requirements |
|---|---:|---:|---:|---|
| S1 PhD students | 5 | 2 | 3 | At least 1 in year 1–2 and 1 in year 3 or above; at least 1 from a non-computational lab |
| S2 Master's students (research-track preferred) | 2 | 1 | 1 | Research-track preferred; coursework-track students doing FYP-style projects may serve as boundary samples |
| S3 PIs | 3 | 1 | 0 | At least 1 PI from outside the own group |
| S4 Postdocs / researchers | 1–2 | 1 | 0–1 | Experience supervising students or collaborating across groups |
| S5 Corporate ML teams (comparison) | 3–4 | — | 0 | At least 1 team lead; at least 2 different companies |
| S6 Industry joint lab members | 2 | — | 0 | At least 1 person who has attended a funder meeting |
| R0 Project owner | — (not counted in interviews) | — | 1 | Data **reported separately**, not merged into the aggregate |
| **Total** | **16–18 (minimum 12)** | | **5–6** | |

**Stopping rule** (carried over from §3.2 of the original research plan, rewritten by segment): After 8 interviews in the academic segments (S1–S4), if 2 consecutive interviews yield no new themes (measured by the number of new codes in the affinity diagram, §7.2), recruitment may stop. The same applies to the corporate segment after 3 interviews. After each interview, record the "number of new codes" as evidence of saturation.

### 2.4 Recruitment Scripts

**(a) Chinese-language private message (peers, adjacent groups; translated here)**

> Hi ___, I'm doing a small study to understand **how people follow up on what was agreed in a research group meeting or a one-on-one with their advisor, after the meeting**. I'm not selling anything, and you don't need to use any tool. We'd just talk about what you actually did after your last one or two meetings.
> It takes about 40 minutes, online or in person, and you pick the time. I won't ask about the details of your research, and your name won't appear in any record. As a thank-you, I'll buy you a coffee (or a S$__ gift card).
> If convenient, you can first spend 2 minutes filling in this short questionnaire: [link]. Thanks!

**(b) English DM / email (labmates, adjacent labs, corporate lab)**

> Hi ___, I'm running a small study on **how research teams follow up on what was agreed in lab meetings and 1:1s**. I'm not selling anything and you won't need to try any tool. I'd just like to hear how you actually handled the last one or two meetings.
> About 40 minutes, online or in person, at your convenience. I won't ask about your research content, and your name won't appear in any notes. As a thank-you, coffee is on me (or a S$__ gift card).
> If you're open to it, here's a 2-minute screener: [link]. Thanks!

**(c) Email to PIs (English, formal)**

> Subject: 30-minute conversation on how your group follows up after lab meetings
>
> Dear Prof. ___,
> I'm ___, a PhD student in ___ (supervised by Prof. ___). Alongside my research, I'm doing a small, independent study on how research groups keep track of what is agreed in lab meetings and 1:1s, and what happens to those items afterwards.
> Would you be willing to share 30 minutes for a conversation about the last few meetings in your group? I won't ask about unpublished research content, and nothing will be attributed to you or your group. Participation is entirely voluntary.
> If it suits you, I can come to your office or meet online at any time that works for you.
> Best regards, ___

**(d) Corporate ML teams (Chinese or English, LinkedIn)**

> Hi ___, I'm a PhD student at the target university studying how ML teams track decisions and follow-ups from experiment reviews and team syncs. Would you have 30–40 minutes for a conversation about your last few team meetings? No product pitch, nothing confidential, and no company names in my notes. Happy to share a summary of what I learn across teams.

**[Inference] Script design notes**:
- The promise "I won't ask about the details of your research" is there because labs are sensitive about unpublished results (U1 §6.3 (b)).
- The value exchange for companies is an "anonymous cross-team summary," which in itself is a low-cost reputational return.
- The gift card amount is left blank. Whether compensation is allowed, and how much, depends on the IRB determination (§6).
### 2.5 Screening Questionnaire (2 minutes, 8 questions)

> Tool suggestion: Microsoft Forms or Google Forms. Whether a university account at the target university can use Microsoft Forms, and where the data would be stored: **to be verified**. The questionnaire **does not collect names**; it collects only one contact method for scheduling, which is deleted after the study ends.

| # | Question (CN / EN) | Options | Screening logic |
|---|---|---|---|
| S1 | Your current role | PhD student / Research master's student / Coursework master's student / Postdoc or researcher / PI or faculty / Industry ML engineer or researcher / Industry ML team lead / Other | Assigned to S1–S6; "Other" goes to manual judgment |
| S2 | In the past 2 weeks, how many of these meetings did you attend? (group meetings, 1-on-1s with your advisor or supervisor, project or experiment sync meetings, meetings with funders or clients) | 0 / 1 / 2–3 / 4–6 / 7+ | **0 → exclude** |
| S3 | Date of the most recent one | Date | More than 14 days ago → exclude (recall becomes unreliable) |
| S4 | After that meeting, where did the agreed items end up? (multiple choice) | Paper notes / Notes on phone or computer / Group chats such as WeChat, Telegram, Slack / Shared document / Task tools (Jira, Notion, GitHub, etc.) / Auto-generated by a meeting AI tool / Not recorded / Don't remember | Not used to screen people; used for quota balancing (both the "not recorded" and "AI tool" ends need participants) |
| S5 | Meeting note or transcription tools used in the past 6 months | Feishu Minutes / Tencent Meeting minutes / Otter / Fireflies / Granola / Notion AI / Built-in Teams or Zoom features / Other / Never used any | Quota: at least 2 people who "used one and then stopped" (material for Switch interviews) |
| S6 | Main meeting language | Chinese / English / Mixed Chinese and English / Other | Recorded, not used to screen people |
| S7 | Are you involved in this project, or in a direct reporting line with the researcher? | Yes / No | Involved in design or development → exclude; reporting-line relationship → may be included, but flag it and analyze separately |
| S8 | You are willing to take part in: a 40-minute interview / a 2-week post-meeting log (2 minutes after each meeting) / both / neither | —— | Those who choose the log enter the log candidate pool |
| — | Contact (for scheduling only) | Free text | Deleted after the study ends |

---

## 3. Mom Test Interview Guide

### 3.1 General Interview Rules (moderator self-check list; read once before each interview)

Source: the three Mom Test rules: "talk about their life, not your idea"; "ask about specific past events, not generalities or opinions about the future"; "talk less, listen more". The three kinds of "fluff" are generalities ("I usually"), future promises ("I would"), and hypotheticals ("I might"). Compliments are "fool's gold". The book recommends taking notes with pen and paper and capturing exact words where possible, because typing during the conversation comes across as rude. **[Fact]** https://mtlynch.io/book-reports/the-mom-test/ (Mom Test book notes, opened at the time of writing)

Torres's story-based interviewing centers on the prompt "Tell me about the last time you…", on the grounds that people answer direct questions poorly when they are removed from the context. **[Fact, cited from `00_pm-skills/02` §2.3, not reopened this round]** https://www.producttalk.org/best-customer-interview-questions/

| Rule | In practice |
|---|---|
| Don't mention the product | For the first 80% of the time, the words "AI", "tool", or "BriefPilot" do not appear. Describe it briefly only at the commitment-test stage (§5) |
| Anchor on one specific meeting | Right at the start, pick "the most recent group meeting or 1-on-1", and bring every later question back to that meeting |
| Look at the real artifact | Ask the participant to **open on the spot** the notes, group chat, or document from after that meeting (look at structure only; no screenshots, no photos, no copying content) |
| Talk ratio | Moderator talking time ≤ 30%. Self-assess after the interview and record it in the note template |
| Don't correct, don't explain | When you hear "it would be great if a tool could…", don't engage; just ask "When was the last time you most needed it?" |
| Duration | Students 40 minutes; PIs 30 minutes; industry 35 minutes |
| Recording | Audio may be recorded with consent (§6.5); also take handwritten notes of exact words. Marking convention: `"..."` exact words, `[Observation]` behavior seen, `[Interpretation]` the moderator's speculation |

### 3.2 Recognizing Bad Data and Redirect Scripts

| Signal heard | Type of bad data | Redirect script |
|---|---|---|
| "I usually…", "We normally…", "I never forget" | Generalization (fluff) | "Can you walk me through how you did it last time? Which day's meeting was it?" |
| "If I had this, I'd definitely use it" | Future promise (fluff) | "The last time you needed it, what did you actually do?" |
| "Maybe", "It should be useful" | Hypothetical (fluff) | "In the past month, was there a time you really wished you had this? What happened?" |
| "That's a great idea", "I'll definitely try it once you build it" | Compliment | Don't thank them and don't dwell on it; ask directly: "What do you use to get by now? When did you start using that workaround?" |
| "It would be great if it could sync to Notion automatically" | Feature request | "Why Notion? What happened the last time you synced manually? How long did it take?" |
| "Everyone's like this, that's just how research is" | Not bad data; it is a **Hard Fact signal** (the user has resigned themselves to it) | Note the exact words and follow up: "When was the last time you got burned by that?" |
| The participant is from your own group or is the PI, and is clearly going along with you | Relationship bias | Mark `[relationship bias]` in the notes and analyze separately; if needed, ask a same-group participant to swap for a different interviewee |
| The moderator says "So you feel that… right?" | Leading question | Change to "What happened after that?" or "Then what happened?" |
| The participant can only describe a process and cannot recount any single event | No evidence of pain | Don't dig forcefully. Record "could not recount a specific event"; this is itself a data point (counted in the denominators of U-H01 and U-H03) |
### 3.3 Critical Incident Interview Method: "What happened after the last group meeting"

> Method source: the Critical Incident Technique (Flanagan 1954, published in *Psychological Bulletin*). In this round I tried to open the original APA PsycNet page (https://psycnet.apa.org/doi/10.1037/h0061470 ), but the page did not load its main text, so **the citation details remain to be verified**. The timeline table below is an operational version adapted by this document from the "last time" principle of The Mom Test and Torres, and is an **[Inference]**.

**How to use it**: Use it in the core section of all three interview guides (about 15 minutes). The moderator takes a sheet of paper, draws a horizontal timeline, and fills it in together with the interviewee.

| Time point | What to ask | What to look at | What to record |
|---|---|---|---|
| T0 in the meeting | "In that meeting, who agreed to do what? Don't look at your notes yet. Tell me from memory." | — | Number of commitments recalled from memory = A |
| T0 in the meeting (cross-check) | "Now open your notes or the group chat from that meeting. How many are there?" | Notes, group chat, documents | Number of commitments in the records = B; in memory but not in the records = C; in the records but not in memory = D |
| T+2 hours | "In the two hours after the meeting ended, what did you do that was related to it?" | Group chat timestamps | Did anyone send a post-meeting summary? Who sent it? |
| T+24 hours | "What about the next day?" | — | Did anyone start on any commitment? What tool did they use? |
| T+48 hours | "By the third day, where were these items written down?" | — | Number of items written down within 48 hours |
| T+1 week | "A week later, what happened to each of these items?" | — | Done / In progress / Not done / Replaced / Forgotten |
| The night before the next meeting | "Before the next meeting, how do you prepare the 'what was arranged last time' part? What did you look through? How long did it take?" | What they looked through | Preparation time (self-reported, in minutes) |
| At the next meeting | "Did anyone in the meeting mention 'what was said last time' while people remembered it differently?" | — | Forgetting or dispute incidents, recorded one by one |

**Output metrics** (one row per interviewee, entered into §7.1): A, B, C, D, number of items recorded within 48 hours, preparation time before the next meeting, number of forgetting or dispute incidents. These are all **retrospectives of a single incident**, with a small sample and recall bias, so they serve only as a supplement to the diary study and must not be treated as frequency estimates.

### 3.4 Guide A: PhD / Master's Student Version (17 questions, 40 minutes)

> Opening (not counted in the question total): introduce yourself, read out the key points of informed consent (§6.5), and confirm whether recording is agreed. "There are no right or wrong answers today. I want to understand what really happens, including the parts that don't go smoothly. I won't ask about the specifics of your research."

| # | Main question | Follow-up | What I'm listening for (not read aloud) | Related hypothesis |
|---|---|---|---|---|
| PhD-Q1 | When was your most recent 1-on-1 with your advisor, or group meeting? What kind of meeting was it? How many people? How long did it last? | Was it online or in person? What language was used? | Anchor on one specific meeting; every later question comes back to it | — |
| PhD-Q2 | How did you prepare before that meeting? What did you look through? How long did it take? | Was there a part where you had to recall "what my advisor asked me to do last time"? How did you remember it? | The preparation cost of the "previous arrangements" section (U1 §3.3) | U-H01 |
| PhD-Q3 | (Enter the §3.3 timeline) In that meeting, who agreed to do what? Tell me from memory first. | Now open your notes or group chat and check? | The gap between memory and records (A, B, C, D) | U-H02 |
| PhD-Q4 | Within 48 hours after the meeting, where were these items written down? Who wrote them? | Did anyone send a post-meeting summary? Did you reply? | Existing workarounds; whose job the post-meeting summary is | U-H02 |
| PhD-Q5 | In that meeting, did your advisor promise you anything? (Granting access, an introduction, reviewing a draft, buying equipment) | What happened afterwards? How long did it take? Did you follow up? How? If not, why not? | Two-way commitments; whether "feeling awkward about chasing" is real | U-H06 |
| PhD-Q6 | Going back one more meeting (the one before last), do you remember what you agreed to? What is its status now? | How do you know its status? | Continuity across meetings; memory decay | U-H01, U-H02 |
| PhD-Q7 | In the past two weeks, was there a time you couldn't remember a specific request from your advisor or a group meeting? What were you doing at the time? | How did you finally figure it out? What did you look through, and whom did you ask? How long did it take? | Frequency and cost (real incidents, not "often") | U-H01 |
| PhD-Q8 | In the past three months, has anything gone wrong because of inconsistent understanding of "who agreed to do what"? Tell me about the most recent one. | What were the consequences? How much extra time did it cost? Did you change your approach afterwards? Was there a case where "someone else said you agreed to it, but you didn't think so"? | Cost incidents; disputes over who claimed what | U-H03, U-H14 |
| PhD-Q9 | The last time you finished an experiment you had agreed to in a meeting, how did you tell your advisor the result? | Where are the results, runs, commits, and figures stored? When your advisor asked about it at the next meeting, how did you find it? | How the result-to-evidence chain breaks today | U-H04 |
| PhD-Q10 | When was the last time you were writing a paper or replying to reviewer comments and needed to recall "why we set it up this way back then"? | Roughly how many times in total? How did you find it? Were there cases where you couldn't? What did you do when you couldn't find it? | Frequency of decision look-backs | U-H11 |
| PhD-Q11 | When did you start using your current method for recording meeting key points? What happened that led to it? | What did you use before? Why did you switch? | Push and Habit in the Four Forces | U-H12 |
| PhD-Q12 | Have you ever tried a meeting-notes or AI note-taking tool and then stopped using it? Tell me about the last time you used it. | Why did you start using it? What worried you along the way? What finally made you stop? What do you use instead? | The Four Forces timeline of a Switch interview: Push, Pull, Anxiety, Habit | U-H12 |
| PhD-Q13 | The last time you (or anyone in your group) wanted to record or use AI to transcribe a group meeting, what happened? | What did the advisor say? What did the group members say? Did anyone mention university rules? | Whether recording is a barrier or a preference (ask about events, not attitudes) | U-H08 |
| PhD-Q14 | When did you last write a weekly report or supervision record? How did you write it? How long did it take? Who read it? | Where did you pull the material from while writing? | The weekly report as a ready-made "output slot" (U1 §2) | U-H01 |
| PhD-Q15 | How does the weekly report or record you show your advisor differ from what you note privately? What type of thing did you deliberately leave out last time? (No need to give specifics) | Why did you leave it out? | Selective sharing; **sensitive question, skip it if the person hesitates** | U-H07 |
| PhD-Q16 | In this whole matter we've been discussing (meeting, recording, following up, reporting), which step is the hardest or most annoying? Why? | What have you tried to solve it? | Migicovsky's "hardest part"; users' self-rated priorities | All |
| PhD-Q17 | Is there anything I should have asked but didn't? Who else do you think I should talk to? | (After getting a name) Could you introduce me? | Snowball sampling; the first step of a reputation commitment | — |

> The interview ends by moving into the §5 commitment-currency test (about 3 minutes).
### 3.5 Outline B: PI Version (15 questions, 30 minutes)

> PIs have little time. Priority: B-Q1, Q2, Q3, Q4, Q8, and Q9 are must-asks; trim the rest as time allows. Never bring up any student's interview content in front of a PI.

| # | Main question | Follow-ups | What I'm listening for | Related hypotheses |
|---|---|---|---|---|
| PI-Q1 | When was your most recent group meeting or 1-on-1 with a student? In the day or two after it, what did you do that was related to that meeting? | Is there a record? Where is it kept? | Anchor event; the PI's own record-keeping habits | — |
| PI-Q2 | For the tasks you assigned to students at the last meeting, how do you know now whether they've done them? When was the last time you found that a student hadn't done something, or had done it off-target? | How did you find out? Was it found late? What was the cost? | Cost events from the PI's perspective | U-H03 |
| PI-Q3 | For things you yourself promised students in a meeting, such as granting access, introducing a collaborator, or reviewing a draft, what was the most recent one you let slip? How did you remember it? | Did the student remind you, or did you remember on your own? | PI-side evidence of two-way commitments | U-H06 |
| PI-Q4 | The last time a student sent you a post-meeting summary or weekly report, what did you do? How long did it take? Did you reply? | What do you usually do (pull back to the specific instance): what about the time before that? Were there any you didn't read? | **Behavioral evidence**: the PI's actual cost and willingness to confirm | U-H05 |
| PI-Q5 | When was the last time you needed to recall "why a student's experiment from a few months ago was stopped" or "why this approach was chosen back then"? | How did you find it? Ask the student? Dig through email? | Decision retrospection on the PI side | U-H11 |
| PI-Q6 | The last time you prepared a grant or project report, how did you compile the year's progress? How long did it take? Where did you get the material? | Was anything impossible to find, so that you had to ask a student? | The "archaeology" cost | U-H11, U-H09 |
| PI-Q7 | When a new student joins, how do you let them know the decisions the group made earlier and the detours it has taken? How did you do it the last time? | Has a newcomer ever repeated an old member's mistake? | Current state of organizational memory | U-H11 |
| PI-Q8 | Over the past year, what software or subscriptions have you bought for the group? Who paid? What process did it go through? Roughly how long did approval take? | Was there anything you wanted to buy but couldn't? Where did it get stuck? Was it bought per person or per group? | Payment path and paying unit (ask about past purchases, not "how much would you pay") | U-H09 |
| PI-Q9 | What requirements do the university, funders, or collaborators have for meeting recordings and AI transcription? When was the last time you ran into a problem in this area? | Have you ever refused to let a student record? Why? | First-hand evidence of policy barriers | U-H08 |
| PI-Q10 | Have you ever tried to get the whole group onto one tool for tracking progress, such as Notion, Trello, Feishu, or Slack? How did it turn out? | At what moment did you feel "this can't be pushed through"? | Resistance to group-wide adoption (Duke case: members don't update) | U-H05, U-H12 |
| PI-Q11 | If a student's post-meeting summary doesn't match your memory, how did you handle it the last time? | Whose version counts? | "Who has to confirm for it to count as consensus" | U-H05, U-H14 |
| PI-Q12 | (Extra question for PIs on university–industry joint projects) The last time you held a progress meeting with an industry funder, how did both sides confirm deliverables afterward? | Was there ever a mismatch in understanding after the fact? | Mutual confirmation needs in university–industry joint labs | U-H13 |
| PI-Q13 | In managing students' progress, what is the hardest part? Why? | What have you tried for it? | The hardest part | All |
| PI-Q14 | Is there anything I should have asked but didn't? Which other professors or students do you think I should talk to? | — | Snowballing; reputation commitment | — |
| PI-Q15 | (Move on to the §5 commitment test) | — | — | U-H05, U-H09 |

### 3.6 Outline C: Enterprise ML Team Comparison Version (15 questions, 35 minutes)

> The purpose is not to find new customers but to run a comparison: both are "R&D-type meetings", so where do commitments get lost in enterprise teams, and where do they not?

| # | Main question | Follow-ups | What I'm listening for | Related hypotheses |
|---|---|---|---|---|
| ENT-Q1 | When was your most recent team sync or experiment review? How many people? How long? | Online or in person? What language? | Anchor event | — |
| ENT-Q2 | For the things agreed on in that meeting, where did they go afterward? Who entered them? How long after? | Could you open Jira, Linear, or GitHub and show me the structure? (Not the content) | Whether the enterprise already has a closed-loop process | U-H10 |
| ENT-Q3 | The last time an experiment-type task was "done", how was it closed? What was attached when closing it? | Where are the results and conclusions written? Could you still find them three months later? | Whether the result–evidence chain is equally broken in the enterprise | U-H10, U-H04 |
| ENT-Q4 | Do you currently use an AI meeting tool? Is it company-approved? The last time you checked AI-generated action items, what did you change? | Is there a tool you tried and then abandoned? Tell me about the last time before you gave up on it | Switch interview; real errors in AI action items | U-H12 |
| ENT-Q5 | In the past three months, has there been a dispute over "who promised it" or "who is responsible"? Tell me about the most recent one. | How was it resolved? What was the cost? | Frequency of ownership disputes in the enterprise | U-H14, U-H03 |
| ENT-Q6 | When was the last time you needed to answer "why did we choose this model, this hyperparameter, this data split back then"? | Where did you find the answer? What do you do when you can't find it? | Decision retrospection: does the enterprise hurt here too | U-H10, U-H11 |
| ENT-Q7 | What are the company's rules on recording meetings and sending meeting content to external AI services? When was the last time you were blocked by them or avoided something because of them? | Who set the rules? | Enterprise-side comparison for the privacy barrier | U-H08 |
| ENT-Q8 | The last time the team adopted a new tool, how was it decided, who paid, and how long did the process take? | Was it bought per person or per team? Roughly what price range? (Fine not to ask for specific numbers) | Comparison of payment paths | U-H09 |
| ENT-Q9 | For cross-team or client meetings, how are post-meeting commitments confirmed? How did you do it the last time? | Has the other side ever disowned something afterward? | Cross-organization confirmation (lead for Option E) | U-H13 |
| ENT-Q10 | Last week, when you wrote a weekly report or reported to your manager, where did you pull the material together from? How long did it take? | —— | Comparison of the output slot | U-H01 |
| ENT-Q11 | Comparing your experience running group meetings during your PhD or master's with team meetings now, how does post-meeting follow-up differ? (If they have that experience) | What specific incident made you feel it was different? | Direct comparison (must be traced to a specific incident) | U-H10 |
| ENT-Q12 | When a newcomer joins, how do you let them know the team's past technical decisions? How did you do it the last time? | —— | Comparison of organizational memory | U-H11 |
| ENT-Q13 | In the "meeting–follow-up–reporting" cycle, what is the hardest part? Why? | What have you tried for it? | The hardest part | All |
| ENT-Q14 | Is there anything I should have asked but didn't? Who else should I talk to? | —— | Snowballing | — |
| ENT-Q15 | (Move on to the §5 commitment test) | —— | —— | — |
### 3.7 Joint Lab Add-on Module (insert into the PhD or PI guide, 4 questions)

| # | Main question | Follow-up | Related hypothesis |
|---|---|---|---|
| CL-Q1 | When was the last meeting you attended with an industry funder? What deliverables or milestones did both sides agree on at that meeting? | Who wrote the minutes afterward? Were they sent to the other side for confirmation? | U-H13 |
| CL-Q2 | In the past six months, has there been a time when the funder and your team understood "what we agreed last time" differently? Tell me about it. | Whose record was used in the end? What was the cost? | U-H13, U-H14 |
| CL-Q3 | When the joint lab buys software or services, where does the money come from? What process did the last purchase go through? | Does the funder require a particular reporting format? | U-H09, U-H13 |
| CL-Q4 | What requirements does the funder have for meeting recordings and cross-border data transfer? What happened the last time you ran into them? | — | U-H08 |

### 3.8 Rewrite Comparison for Old Guide Q4 / Q6

The review pointed out that Q4 and Q6 of the old guide (`briefpilot/docs/research/interview-guide.md`) are hypothetical questions that, under the Mom Test, produce "noise" (`00_pm-skills/02` §3.1). Q5 and Q8 have the same problem.

| Old question | What's wrong | New phrasing (already merged into the three guides above) |
|---|---|---|
| Q4 "If an AI gives you an answer, what evidence would you need before you are willing to use it?" | Hypothetical + future | "When was the last time you used an answer from an AI or a colleague and later found it was wrong? What happened? What did you change afterward?" (merged into PhD-Q12, ENT-Q4) |
| Q5 "Which actions must you confirm yourself? Which would you let the tool do automatically?" | Asks about attitudes and the future | "What was the last time an AI or a colleague did something for you that you felt it shouldn't have?"; "The last time you checked AI-generated action items, what did you change?" (ENT-Q4) |
| Q6 "For more accurate answers with an audit trail, how much longer are you willing to wait?" | Purely hypothetical | **Deleted**. Latency tolerance will instead be measured in the demo usability test; it is not asked during interviews |
| Q8 "If you could improve only one step today, which would you pick?" | Makes the user do your design for you | "What is the hardest part of this whole thing? Why? What have you tried for it?" (PhD-Q16, PI-Q13, ENT-Q13) |
| Closing question 2 "If there were a tool like this… what is your first reaction?" | Invites flattery | Replaced by the §5 commitment test: don't ask "what do you think?", instead ask the person to commit time, reputation, or money |

---

## 4. 2-Week Diary Study Plan

### 4.1 Why a diary study is necessary

NN/g defines a diary study as one in which participants record entries themselves, at the time of an event or as soon as possible afterward, over a period of a few days to a month or more. It suits studying habits and frequency, change over time, and cross-tool usage. There are three ways to trigger entries: event-triggered, fixed-interval, and signal-triggered (the researcher sends reminders). The costs are complex planning, easy attrition, and the need for higher incentives. **[Fact, cited from `00_pm-skills/02` §3.4, not reopened this round]** https://www.nngroup.com/articles/diary-studies/

**[Inference]** Whether a commitment "was written down within 48 hours" is a phenomenon only visible across days. A one-off interview relies on recall and will systematically undercount omissions (because a commitment that was forgotten cannot be recalled). So the primary evidence for U-H01 and U-H02 must come from the diary; interviews serve only as a supplement.

### 4.2 Design parameters

| Parameter | Setting | Rationale |
|---|---|---|
| Duration | 14 days (Monday of week 2 to Sunday of week 3) | Covers at least 2 weekly group meetings and 2 one-on-ones |
| Participants | 5–6 people: R0 (the project owner, starting early in week 1) + 3 PhD students + 1 master's student + 0–1 postdoc | Both 05 §0 and step 5 of 00/02 recommend 3–5 people; recruit 1 extra to allow for attrition |
| Trigger method | **Event-triggered** (one form after each meeting) + **signal-triggered** (a reminder every evening at 21:00: "Did you have a meeting today?") + **48-hour follow-up** (pushed automatically) | Mixing the three methods reduces missed entries |
| What is recorded | Only "counts + categories"; **the specific content of commitments is not recorded** | Minimizes privacy exposure; also keeps each entry under 2 minutes |
| Tools | Microsoft Forms or Google Forms (whether the university account can be used and where the data is stored: to be verified); reminders via the participant's own usual Telegram, WhatsApp, or WeChat | No new app to install, lowering the barrier |
| Pre-briefing | 15 minutes: explain "what counts as a commitment" (the definition in §4.3) and practice filling in the form together on a hypothetical meeting | Aligns the counting convention |
| Exit interview | 15 minutes: review the participant's own data and probe the details of 2–3 "forgotten or disputed" events | Turns counts into stories |

### 4.3 Counting convention for "one commitment" (read verbatim during the pre-briefing)

> One commitment = one thing that **a specific person** in the meeting (including you, your advisor, or group members) **said aloud** they would do, whether or not there is a deadline.
> - Counts: "I'll rerun the baseline this week", "I'll open the dataset permissions for you", "I'll look at your draft before the next group meeting", "I'll try swapping the loss" (soft commitments also count; tick "soft" separately).
> - Does not count: pure discussion ("maybe we could try X" but nobody says they will do it), and things already finished on the spot during the meeting.
> - If unsure: count it, and also count it once in the "soft commitments" number.

**[Inference]** The distinction between soft and hard commitments will affect how U-H02 is interpreted (see the gray-zone rule in §1.2 U-H02). Whether different people apply the counting convention consistently is itself the subject of 05 Q10; see the calibration approach in §4.7.

### 4.4 Form fields

**Form 1: 2-minute post-meeting form (filled in after each meeting)**

| Field | Question | Type | Required | Maps to |
|---|---|---|---|---|
| D1 | Participant ID (R0–R6) | Dropdown | Yes | — |
| D2 | Meeting date and start time | Date-time | Yes | — |
| D3 | Meeting type | Single choice: group meeting / one-on-one with advisor / sub-project or experiment alignment meeting / collaborator meeting / funder or industry meeting / journal club / other | Yes | Stratified analysis |
| D4 | Duration | Single choice: <30 minutes / 30–60 / 60–120 / >120 | Yes | — |
| D5 | Format | Single choice: in person / online / hybrid | Yes | U-H08 |
| D6 | Main language | Single choice: Chinese / English / mixed Chinese-English / other | Yes | Option D lead |
| D7 | Total number of commitments you heard | Number | Yes | **U-H02 denominator** |
| D7a | Of which, your own commitments | Number | Yes | — |
| D7b | Of which, commitments made by your advisor or supervisor to you (or to group members) | Number | Yes | U-H06 |
| D7c | Of which, "soft commitments" ("I'll try", "if I have time") | Number | Yes | U-H02 gray zone |
| D8 | Did anyone in the meeting mention "what was said last time" but need to check the records, or did people remember it differently? | Single choice: no / yes, checked the records and found it / yes, couldn't find it / yes, people remembered it differently | Yes | **U-H01** |
| D9 | Where are these commitments recorded now (after the meeting)? | Multiple choice: not recorded / paper notes / personal digital notes / group chat / shared document / task tool / auto-generated by a meeting AI tool / someone else recorded them, I don't know where | Yes | Tool distribution |
| D10 | Before this meeting, was there anything from "the last arrangement" that you needed to recall but couldn't? | Single choice: no / yes, solved by checking records (about how many minutes: __) / yes, solved by asking someone / yes, not resolved | Yes | **U-H01** |
| D11 | Was this meeting recorded or transcribed by AI? | Single choice: yes / no, because it didn't occur to us / no, because it wasn't permitted or convenient / don't know | Yes | U-H08 |
| D12 | One sentence: the most annoying thing about follow-up after this meeting (optional; **do not write specific research content or names**) | Short text | No | Qualitative material |
| **D13** | How many "earlier commitments" had their status updated verbally in this meeting? Of those, how many did you learn about **for the first time** (not seen beforehand in the group chat / issues / W&B)? | Two numbers | Yes | **P-H4** (positioning §11) |
| **D14** | How many experiment commitments or decisions in this meeting came with **explicit conditions** (dataset / seed / hyperparameters / version)? | Number | Yes | **P-H6** |
| **D15** | If you wanted to follow up on something your advisor promised in this meeting, would you ask in the group chat? (Single choice: yes / only privately to the advisor / only privately to a labmate / would not ask / no such situation this time) | Single choice | Yes | **P-H7 social dynamics**; decides whether post-meeting follow-up should be a private draft only |

**Form 2: 48-hour follow-up (30 seconds, pushed automatically 48 hours after the meeting)**

| Field | Question | Type |
|---|---|---|
| F0 | The corresponding meeting (date and type filled in automatically) | Hidden field or dropdown |
| F1 | Of the D7 commitments from that meeting, how many are now **written down anywhere** (written by anyone counts)? | Number |
| F1a | Of those, how many are your own commitments that were written down? | Number |
| F2 | So far, has any commitment been forgotten, duplicated, or understood differently in terms of "who is responsible"? | Single choice: no / yes, forgotten (how many: __) / yes, duplicated / yes, disputed owner |
| F3 | Did anyone send a post-meeting summary? | Single choice: no / yes, I sent it / yes, someone else sent it |
| **F4** | Of the statuses updated verbally in the last meeting, how many have now been written back to the original record (minutes, issue, task sheet)? (__ items, out of __ verbal updates) | Two numbers (**P-H5** write-back rate) |

**Form 3: Weekly review on Sunday evening (3 minutes, 2 times in total)**

| Field | Question |
|---|---|
| W1 | This week, did you pay a cost because a commitment from a meeting was forgotten or misunderstood? (Single choice: no / yes → describe the type of cost in one sentence: rerunning experiments / delay / criticism / awkwardness / other, and roughly how many hours it took) |
| W2 | This week, how many minutes did you spend writing a weekly report or supervision record? How many places did you piece the material together from? |
| W3 | This week, was there anything you wanted to chase your advisor or colleagues about but didn't? (Single choice: no / yes, how many: __) |
| W4 | This week, how many meetings did you forget to fill in? (An honest estimate, used for data quality) |
### 4.5 Reminder Mechanism

| Timing | Channel | Content |
|---|---|---|
| After each meeting (during the pre-study briefing, participants tell the researcher when their regular meetings are held) | The instant messenger the participant normally uses | "Just finished the ___ meeting, right? 2-minute form: [link]" |
| Every evening at 21:00 | Same as above | "Any meetings today that you haven't logged yet? If not, just ignore this message." |
| 48 hours after a meeting | Same as above (the researcher sends it manually, based on the submission time of Form 1, or uses the form tool's scheduled push) | "A 30-second follow-up on the meeting two days ago: [link]" |
| Every Sunday at 20:00 | Same as above | Weekly review form |
| 2 consecutive days with no submission | Private message | "Were there no meetings these two days, or did things get busy and slip your mind? Either is fine, just let me know." |

**[Inference]** Err on the side of slightly more frequent reminders, because NN/g points out that attrition is the main risk in diary studies; but every reminder should give the recipient an "ignore it if not" exit, so it doesn't become a burden.

### 4.6 Week-2 Manual Backfill Test (validates U-H04, U-H05)

This is a "concierge" test: no code is written; the researcher manually simulates one key action of the product and observes real behavior. **[Inference]**

1. In week 2, one day before each diary participant's next meeting, the researcher sends a private message:
   > "At the last meeting (date), you noted N commitments of your own. Before the next meeting, could you reply with one line for each: **what the outcome was** (done / not done / result supports it / result contradicts it / replaced), and **one link or file name** (a run, commit, or figure is fine)? It's completely fine if you'd rather not reply."
   Note: the researcher does not know the actual content of the commitments, so the message gives only the count and asks the participant to match them up themselves. This is harder than the real product would be, so the results will be conservative.
2. Record: number of messages sent, number of items backfilled, number of backfilled items that include a link, response time, and reasons for declining or not replying (asked in the exit interview).
3. PI side: with the consent of 1 student, organize that student's backfilled results into a 3–5 line draft (containing only what the student agreed to share) and send it to that student's PI: "Here are ___'s commitments and outcomes this week. Anything to change? Just reply 'confirmed'." Record whether the PI replies, how quickly, and whether they make changes. **Written consent from the student must be obtained first, and the PI must also have taken part in an interview and be aware of this.**

### 4.7 Data Analysis Methods

| Metric | Definition | How reported |
|---|---|---|
| Commitment frequency | ΣD7 per person per week | One number per person; report the median and range; R0 listed separately |
| 48-hour logging rate | ΣF1 / ΣD7 (computed per person, then take the median; also give the pooled value) | Compare against the 30% / 15% lines of U-H02 |
| Logging rate of own commitments | ΣF1a / ΣD7a | Distinguishes "someone else logged it" from "I logged it" |
| Recall-failure frequency | Number of times D10 is answered "yes" / person / week | Compare against U-H01's "≥1 per week" |
| Forgotten / disputed rate | Number of meetings where F2 is "yes" / total meetings | Supplements U-H03 and U-H14 |
| Share of commitments from superiors | ΣD7b / ΣD7 | Background for U-H06 |
| Share of soft commitments | ΣD7c / ΣD7 | Gray area for U-H02 |
| Tool distribution | Number of times each D9 option appears | Profile of existing makeshift workarounds |
| Stratified by meeting type | The metrics above grouped by D3 | Judge whether "group meeting" and "1-on-1" are two different product problems (the inference in U1 §2) |
| Backfill rate | Items backfilled / items sent; link rate | U-H04 |
| Data quality | Form 1 submissions / (submissions + number of missed entries self-reported in W4); 48-hour follow-up completion rate | If quality is below 70%, downgrade the conclusion by one level |

**Counting calibration**: In group meetings of the group the owner (R0) belongs to, pick 1–2 meetings and have the owner (R0) and another diary participant each fill in Form 1 independently. Compare their D7 and D7c and record the differences. If the two people's commitment counts for the same meeting differ by more than 50%, the counting criteria are not aligned, the pre-study briefing needs to be redone, and this should be noted in the report. **[Inference]** This is also a very small-scale pre-test of 05 Q10 (whether commitment strength can be labeled consistently), but 2 meetings are far too few to compute Cohen's Kappa, so it must not be written up as a conclusion.

**Analysis discipline**:
- With a sample of 5–6 people, do not run significance tests or report confidence intervals; report only descriptive statistics and each person's raw numbers.
- R0's data (the owner's own) is listed separately and not merged into the pooled figures, to avoid self-confirmation bias.
- Diary numbers are **self-reported**; in the exit interview, pick 2–3 specific events to cross-check, and note in the report any that cannot be verified.

### 4.8 Incentives

| Item | Setting [Assumption, to be validated] |
|---|---|
| Form | Tiered by completion: complete the pre-study briefing + at least 80% of meetings logged each week + exit interview → full amount; complete half → half amount |
| Amount | Left blank; depends on the IRB determination and personal budget. Principle: incentives for a diary study should be higher than for a single interview (NN/g notes that diary studies require higher incentives) |
| Non-monetary reward | After the study, give each participant a summary of **their own** two weeks of meeting data (how many meetings, how many commitments, how many noted down). This is useful to the participant and is also a value exchange |
| Not done | Do not use "free use of the product in the future" as an incentive, to avoid turning participants into people with expectations about the product |

---

## 5. Commitment Currency Test (last 3 minutes of the interview)

### 5.1 Why "ask" at the end

The Mom Test divides commitment into three currencies: **time** (scheduling a next meeting with a clear goal, sitting down to give feedback on wireframes, trying it out for a meaningful period), **reputation** (introducing peers or decision-makers, public endorsement or case study), and **money** (letter of intent, pre-order, deposit). **[Fact]** https://mtlynch.io/book-reports/the-mom-test/ (opened at the time of writing). The pass line given in step 8 of `00_pm-skills/02` is: ≥5 people give a time commitment and ≥2 people give a reputation commitment.

**[Inference]** Being turned down is also valid data. Every interview must ask for at least one kind of commitment and record the result; "didn't ask" is recorded as "not requested" in the log and counts as an execution error by the moderator.

### 5.2 Commitment Ladder and Scripts

First describe what is to be built in **one sentence** (it appears only here, with no feature details):

> 中文："我在考虑做一个很小的东西：会后把每个人说过要做的事列出来，下次会前提醒回填结果。现在还没做出来。"
> EN: "I'm considering building something small: after a meeting, it lists what each person said they'd do, and before the next meeting it asks for the outcome. Nothing is built yet."

Then make requests **from low to high**, one level at a time; if the person declines, stop at that level:

| Level | Currency | Script for students / postdocs | Script for PIs | Script for industry |
|---|---|---|---|---|
| L1 | Time (low) | "Next week I'll manually put together your group meeting's commitments on paper or in a spreadsheet. Would you be willing to spend 10 minutes checking whether it's right?" | "I can send you a draft of the commitments of one student who has agreed. Would you be willing to spend 2 minutes confirming it?" | "Once I've made a draft version, can I book 20 minutes to show it to you?" |
| L2 | Time (high) | "Would you be willing to take part in a 2-minute post-meeting log for the next 2 weeks?" (diary study) | "In two weeks, could I book another 15 minutes to show you the anonymized results for the whole group?" | "Would you be willing to try it once at your team's next real team sync?" |
| L3 | Reputation | "Could you introduce me to another student in your group, or to your advisor?" | "Could you introduce a colleague who you think would have opinions on this?"; "If it turns out to be useful after the trial, would you be willing to let the students in your group try it once?" | "Could you introduce me to your team lead, or to someone on another team, so I can talk to them?" |
| L4 | Money (PIs, university-industry joint labs, and companies only) | Do not ask students for a monetary commitment | "If the pilot proves useful, would you be willing to go through the funding process to trial it for a semester for the group? Can you tell me who would need to sign off on that process?" | "If it's useful, does your team have a budget for trying new tools? Who approves it?" |

**Ethical boundary on monetary commitments**: With no product and no IRB determination, **do not collect any real payment**. L4 records only "whether the person is willing to name the approver, and whether they are willing to bring this into the approval process." This is a proxy indicator for a monetary commitment; the report must state it honestly as a "proxy indicator" and must not describe it as "obtained a prepayment." **[Inference]**
### 5.3 Record Sheet

| Field | Description |
|---|---|
| respondent_id | P01… |
| Group | S1–S6 |
| L1 request / outcome | Not requested / Declined / Accepted / Accepted and fulfilled (filled in later) |
| L2 request / outcome | Same as above |
| L3 request / outcome | Same as above; if accepted, record how many people were introduced (no names) |
| L4 request / outcome | Same as above; if accepted, record "named an approver role / willing to bring it into the workflow" |
| Verbatim reason for declining | Record word for word |
| Fulfillment check date | Within 7 days of the commitment, check whether it was actually fulfilled (whether the introduction happened, whether the draft was actually viewed) |

**Scoring**: Each respondent is scored at their "highest fulfilled level" (L0 = no commitment, or verbal approval only; L1–L4 as above). **Only fulfilled commitments count toward the score.** A commitment made verbally but not fulfilled is recorded as "verbal" and listed separately. The summary reports the number of respondents at each level, not an average score.

---

## 6. Ethics and Compliance

### 6.1 Target University IRB Rules (official pages, accessed at the time of writing)

| Rule | Key points from the source text | Label and source |
|---|---|---|
| Scope | Research involving human subjects conducted by the target university's faculty, staff and students "must be reviewed and approved by the [university's] Institutional Review Board ([university] IRB) before they are conducted". Research is defined as a systematic investigation designed to develop or contribute to "generalizable knowledge"; examples include observational studies, **interviews and focus groups**, **questionnaires**, and secondary use of non-public data containing personal identifiers | [Fact] (university page; link removed) |
| Not under IRB jurisdiction | The page lists three categories: (1) research that is "about what" rather than "about whom": "the focus of a study is only on products, methods, policies, procedures and organizations"; (2) service evaluations and audits, where "such evaluations and audits does not require IRB approval"; (3) academic and journalistic activities (oral history, biography, etc.). When in doubt, contact IRB staff "to obtain a decision from IRB" | [Fact] (university page; link removed) |
| Student research | Students in research degrees (PhD, research master's) submit to the university IRB through their supervisor; coursework projects (FYP, URECA, etc.) submit to the school's Ethics Review Committee (ERC); "Generally, non-academic studies on humans do not require ethics approval", with post-event surveys and project feedback given as examples; **if you intend to publish or present results in a journal or at a conference, contact the IRB before starting** | [Fact] (university page; link removed) |
| Exempt review also requires an application | "Researchers are still required to apply to [the university IRB] and obtain formal approval for Exempt-status"; exempt status is determined by IRB members, not by the researcher | [Fact] (university page; link removed) |
| Exempt Category 2 (anonymous surveys, interviews) | Requires that the information obtained cannot identify subjects directly or through linked identifiers; **recording information in a way that can identify subjects (for example, identifiable audio recordings) does not qualify for exemption**; intrusive questions that may cause emotional distress, and situations where a disclosure could harm subjects' employment or reputation, also do not qualify | [Fact] (university page; link removed) |
| No retroactive approval | The RNR category page states that the IRB cannot grant retrospective approval, so submission before the research begins is recommended | [Fact] (university page; link removed) (Note: RNR itself applies only to secondary research on non-identifiable data and does not apply to this project's interviews) |
| Training | "CITI certification is required for all domains in [the university] IRB, before the review of your ethics application can proceed" | [Fact] (university page; link removed) |
| Submission system and timeline | Submit through the Ethics Review Management Portal (ERMP); the deadline for exempt and expedited review is 8 a.m. every Monday, and for full-board review the 15th of each month | [Fact] (university page; link removed) |
| Form templates | Forms are "accessible through [the university] intranet" and require login, so the official informed-consent template could not be viewed in this round | [Fact] Stated on the page; template content **to be verified**. (university page; link removed) |
| Contact | irb@university.example | [Fact] Same as the do-i-need-irb-approval page above |
### 6.2 Does This Project Need IRB Review? Assessment and Recommendation

**[Inference] This project falls in a gray area, with reasons on both sides:**

- Supporting "not needed": the research purpose is requirements discovery for a product demo, and the questions center on "post-meeting workflows and tools" (closer to "about products and methods, not about people"). It is a non-academic activity, and the results will be used for a portfolio and job interviews, not for journals or conferences.
- Supporting "needed": (1) the project owner is a research PhD student at the target university, and the interviewees are colleagues and students there; (2) interviews will be audio-recorded, and the recordings are identifiable; (3) some questions touch on the advisor–student relationship (PhD-Q5, Q15), and a leak could affect interviewees' reputation or their relationship with their advisor, which is exactly the situation excluded from exemption category 2; (4) if the results are later written up as a paper for venues such as CHI or CSCW, IRB approval **cannot be obtained retroactively**.

**Recommended order of execution**:
1. **On Monday of Week 1**, email irb@university.example to request a determination (template in §6.3), and inform your own advisor at the same time.
2. While waiting for a reply, **only conduct interviews that are not audio-recorded and do not involve the sensitive advisor–student questions (PhD-Q5, Q15)**, and interview only students outside your own group and industry interviewees, with all notes anonymized.
3. If the IRB determines that the activity is "not under its jurisdiction": keep the email as evidence and continue under the rules in §6.4–6.6.
4. If the IRB requires an application: first complete CITI training, then submit through ERMP via your advisor. If the interviews include identifiable audio recordings, they most likely will not qualify for exemption category 2 and would need expedited review. In the meantime, change the study to "R0's own diary + competitor error analysis only", with no contact with human subjects.
5. **Regardless of the determination**, follow IRB-level standards (informed consent, anonymization, minimization, deletion deadlines), because what this project is about is precisely "trustworthy, consent-first" design.

**Other items to verify**:
- **Singapore PDPA**: this round, the official PDPC page (https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act/data-protection-obligations ) was opened, but its body text did not render; the statute text site (sso.agc.gov.sg) returned 403. The specific provisions of the PDPA obligations (consent, purpose limitation, notification, retention limitation, cross-border transfer, etc.) and the conditions for applying the "research exception" are **to be verified**. The approach in §6.5–6.6 of this document is designed around the general principles of "consent + stating the purpose + minimization + time-limited deletion", and is an **[Inference]**, not legal advice.
- **The target university's IT policy on AI meeting tools and third-party cloud services** (05 Q8): this round's search found no official page from the university, so this is **to be verified**. Consider asking about it in the IRB determination email, or asking the school's IT office.

### 6.3 IRB Determination Request Email Template (English)

> Subject: Request for determination – non-academic user interviews for a product prototype
>
> Dear University IRB Secretariat,
> I am ___, a PhD student in ___ (supervisor: Prof. ___). Separately from my thesis research, I am building a software prototype for my personal portfolio and would like to conduct about 15 informal interviews (30–40 minutes) and a 2-week self-report log with about 5 participants. Participants would be university students, staff and some industry professionals.
> The questions focus on how teams follow up on items agreed in meetings and which tools they use (i.e., the process and tools, not the participants themselves). No sensitive personal data will be collected. With consent, interviews may be audio-recorded for note-taking; recordings will be deleted within 30 days and notes will be de-identified. Results will be used to guide the prototype design and may be summarised (anonymously) in a portfolio or job interview. There is no plan to publish in journals or conferences.
> Could you please advise whether this activity falls under "Not Under IRB", or whether I should submit an application (and under which review category)? I would also appreciate any guidance on the university's policy on audio recording and third-party AI transcription services in this context.
> Thank you very much.
> Best regards, ___

### 6.4 Power Dynamics and Voluntariness

- Do not recruit students by having the PI post instructions in a group chat; the PI should not know whether a given student participates (unless the student says so).
- Interviews with the PI of your own group do not involve any specific student; the content of interviews with students in your own group is not disclosed to the PI. This includes aggregated information such as "someone mentioned that the advisor delays", which is also not reported to the PI when the in-group sample is fewer than 3 people (with so few people, it could be traced back to a specific person).
- The PI confirmation test in §4.6 must satisfy all of the following: the student's written consent, the PI having attended the interview and being informed, and the draft containing only content the student agreed to share.
- If an interviewee is a direct supervisor or direct report of the project owner (screening question S7), list them separately in the analysis and note this in the report.
### 6.5 Informed Consent Form Template (Bilingual)

> If the IRB requires a formal application, use the official template on the university intranet instead (§6.1, to be verified). The following is the simplified version to be used when the study is determined to be "outside IRB jurisdiction."

```
Participant Information and Consent

Study title:
How research and R&D teams follow up after meetings

Researcher: ___ (PhD student, the target university, ___), Contact: ___
(If applicable) IRB determination or approval ref: ___

1. Purpose
To understand how teams record and follow up on what was agreed in meetings. Results will inform the design of a software prototype. This is not a sales conversation.

2. What you will do
□ One 30–40 minute interview
□ A ~2-minute form after each meeting for two weeks, plus a 3-minute weekly review
We only ask about process and tools, not your research content. Please do not share unpublished results, confidential information, or other people's personal data.

3. Voluntary participation
Participation is voluntary. You may skip any question or withdraw at any time without giving a reason and without any consequence. On withdrawal, your data will be deleted (except anonymised aggregate counts already produced).

4. Audio recording (optional)
□ I agree to audio recording   □ I do not agree
Recordings are used only for note-taking, stored on the researcher's encrypted device, never uploaded to any cloud AI service, and deleted after transcription and no later than 30 days after the interview.

5. How data are handled
- Notes use a code (e.g., P03) instead of your name; your lab or company is not recorded. The code key is stored separately, encrypted, and deleted at the end of the study.
- De-identified notes may be analysed with the help of AI tools; only text with names, affiliations and research content removed will be used.
- De-identified notes will be deleted by ___ (date).

6. How results are used
Results will be used in anonymised, aggregated form for prototype design, a personal portfolio and job interviews. Your exact words will only be quoted with your further permission.
□ I agree to be quoted anonymously   □ I do not agree

7. Risks and benefits
Risks are minimal. Some questions touch on working with your supervisor or manager; you may skip them. Thank-you: ___ (coffee / gift card / a summary of your own two-week meeting data).

8. Contact
Questions: contact the researcher at ___. (If IRB-reviewed) For questions about your rights as a participant: the university IRB, irb@university.example.

I have read the above and agree to take part.
Participant code: ____   Date: ____
(Verbal consent: recorded by researcher with time ___)
```
### 6.6 Recording and Data Retention Rules

| Data | Storage location | Who can access | Retention period | Notes |
|---|---|---|---|---|
| Recordings | An encrypted folder on the researcher's own computer (e.g., a local disk with macOS FileVault enabled), not synced to any cloud drive | Researcher only | Deleted immediately after transcription is complete, and no later than 30 days after the interview | **Never uploaded to any cloud transcription or AI service.** If transcription is needed, use a locally run speech recognition model [Inference] |
| Transcripts and interview notes | Local project folder `02_user-research/raw/` (added to `.gitignore`, never committed to any repository) | Researcher only | After de-identification, retained until the project ends (date left blank) | De-identification: replace personal names with roles ("advisor", "labmate A"); remove identifiable parts of affiliations, project titles, and model names |
| ID–name mapping table | Separate encrypted file, stored apart from the notes | Researcher only | Deleted when the research ends | — |
| Screening questionnaire and diary forms | The platform hosting the form tool (whether the platform under the target university account stores data within Singapore: to be verified) | Researcher only | Raw form data and contact details are deleted after the de-identified CSV is exported | Forms do not collect names |
| Analysis outputs (affinity diagram, summary tables, `07_research_findings.md`) | Project folder | May be shown publicly | Long term | Contain only anonymous summaries and anonymous quotes the respondent has consented to |

**Boundaries for AI-assisted analysis**: **De-identified** notes may be given to an AI tool for preliminary categorization, but: (1) recordings and raw transcripts are never shared; (2) this has been disclosed in Article 5 of the informed consent form; (3) every categorization produced by the AI must be checked item by item by the researcher, and the AI must not generate any "verbatim respondent quote". **[Inference]**

---

## 7. Analysis Templates (all blank, pending execution)

### 7.1 Single-Interview Notes Template

> File name: `02_user-research/raw/P__-interview-notes.md` (not committed to the repository); the de-identified version goes in `02_user-research/notes/P__.md`.

```
---
respondent_id: P__            # pending
segment: S_                   # S1 PhD / S2 Master's / S3 PI / S4 Postdoc / S5 Industry ML / S6 University-industry joint lab
same_lab_as_researcher: yes/no  # pending
reporting_relation: none/superior/subordinate # pending
recruit_channel:              # pending
date:                         # pending
duration_min:                 # pending
recording_consent: yes/no       # pending
quote_consent: yes/no           # pending
interviewer_talk_ratio_self_estimate: __%   # pending (target ≤30%)
---

## Anchor Event
- Meeting date / type / number of attendees / format / language: (pending)

## §3.3 Timeline (key events)
| Time point | What happened | Tool used | Verbatim quote | [Observation] | [Interpretation] |
|---|---|---|---|---|---|
| T0 in the meeting | | | | | |
| T+2h | | | | | |
| T+24h | | | | | |
| T+48h | | | | | |
| T+1 week | | | | | |
| Night before the next meeting | | | | | |
| At the next meeting | | | | | |

- A: commitments recalled from memory: (pending)  B: commitments in records: (pending)  C: remembered but not recorded: (pending)  D: recorded but not remembered: (pending)
- Number of items written down within 48 hours: (pending)
- Preparation time before the next meeting (self-reported, minutes): (pending)

## Specific Events (one block per event)
### Event 1
- Time (roughly which week):
- Context:
- What happened:
- Cost (time / delay / relationship / other):
- Workaround at the time:
- Verbatim quote:
- Corresponding hypothesis: H__

## Four Forces (if there is an event of abandoning a tool)
- Push:  - Pull:  - Anxiety:  - Habit:

## Bad-Data Flags
- Count and location of generalizations / future statements / hypotheticals / flattery / feature requests: (pending)
- Whether relationship bias is present: (pending)

## Hypothesis Direction (one-sentence reason each)
| U-H01 | U-H02 | U-H03 | U-H04 | U-H05 | U-H06 | U-H07 | U-H08 | U-H09 | U-H10 | U-H11 | U-H12 | U-H13 | U-H14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| supports/opposes/irrelevant | | | | | | | | | | | | | |

## Commitment Currency (§5.3)
- L1:  L2:  L3:  L4:  Verbatim refusal:

## Three Most Surprising Findings (write within 30 minutes after the interview)
1.
2.
3.

## Adjustments Needed to the Interview Guide
-
```

### 7.2 Affinity Diagram Coding Table

**Approach** [Inference]: After each interview, split the notes into "one observation per card" (a verbatim quote or a behavior). First sort cards using the **preset codes** below (deductive); create new codes for those that don't fit (inductive). After each interview, record the number of new codes added as the basis for judging saturation (§2.3 stopping rule).

**Preset codebook**:

| Code | Definition | Type of included example (not real data) | Corresponding hypothesis |
|---|---|---|---|
| REC-NONE | The commitment was not written down anywhere after the meeting | Describes "nobody took notes after the meeting" | U-H02 |
| REC-OTHER | It was recorded, but by someone else, and the person doesn't know where | Describes "my senior labmate took notes but never shared them" | U-H02 |
| RECALL-FAIL | Cannot remember the previous arrangements before a meeting | Describes scrolling through chat history to find "what was said last time" | U-H01 |
| COST-REDO | Redoing work because a commitment was lost | Describes rerunning an experiment | U-H03 |
| COST-DELAY | Delay caused by a lost commitment | —— | U-H03 |
| COST-REL | Relational or emotional cost (being criticized, embarrassment, hesitating to follow up) | —— | U-H03, U-H06 |
| UP-PROMISE | Commitments made by an advisor or superior to a subordinate | —— | U-H06 |
| NOT-CHASE | Wanted to follow up on something but didn't | —— | U-H06 |
| SELECT-SHARE | Selectively withholding from a superior | —— | U-H07 |
| OUTCOME-LINK | Where results and evidence are stored and how they are found | —— | U-H04 |
| DECISION-WHY | Tracing back "why was it set up this way" | —— | U-H11 |
| CONFIRM-PI | A PI's act of confirming a student's records | —— | U-H05 |
| OWNER-DISPUTE | Disagreement over "who is responsible" | —— | U-H14 |
| REC-BAN | Recording or an AI tool was refused or prohibited | —— | U-H08 |
| PRIV-ANX | Worry about privacy or leakage (with no refusal event) | —— | U-H08, U-H12 |
| TOOL-QUIT | An event of abandoning a tool | —— | U-H12 |
| HABIT | Existing workarounds and where they came from | —— | U-H12 |
| PAY-PATH | Past purchase events and approval processes | —— | U-H09 |
| SPONSOR | Confirmation with a funder or client | —— | U-H13 |
| REPORT-SLOT | Existing outputs such as weekly reports and supervision records | —— | U-H01 |
| HARD-FACT | Resigned expressions such as "everyone does it this way" | —— | All (Sequoia archetype judgment) |
| NEW-* | Newly derived inductive codes | —— | —— |

**Coding log** (one row per card, pending execution):

| card_id | respondent_id | segment | Verbatim quote or behavior | Code | Specific event (yes/no) | Event timing (weeks ago) | Corresponding hypothesis | Supports/opposes |
|---|---|---|---|---|---|---|---|---|
| (pending) | | | | | | | | |

**Summary table** (one row per code, pending execution):

| Code | Number of people mentioning n/N | Of whom with a specific event | Academic group n/N | Industry group n/N | Most representative anonymous quote (consent required) |
|---|---|---|---|---|---|
| (pending) | | | | | |
### 7.3 Opportunity–Solution Tree (OST) Update Method

Torres's OST has four layers: desired outcome → opportunities (unmet needs, pain points, desires) → solutions → assumption tests. The test for telling an opportunity from a solution is "can it be addressed in more than one way?"; opportunities must come from user stories. **[Fact, quoted from `00_pm-skills/02` §2.3, not reopened in this round]** https://www.producttalk.org/2016/08/opportunity-solution-tree/

**Root node (unchanged)**: the number of commitments per week that the target team "confirms and closes out."

**Update rules** [Inference]:
1. **Add an opportunity node** only when at least 2 interviewees (or at least 2 people in the diaries) give **specific events** that support it. An opportunity backed by only 1 person goes into the "candidate opportunities" area and does not go on the tree.
2. **Write opportunities in the user's language**, e.g., "My advisor promised to open up the permissions and it dragged on for two weeks; I felt awkward chasing," not "needs a two-way commitment feature."
3. **Annotate each opportunity node** with: supporter count n/N (academic and industry groups counted separately), cost type, linked assumption, and evidence card IDs.
4. **Delete or downgrade**: if an assumption in §1.2 falls into the "rejection line," gray out the corresponding opportunity node and note the date and evidence; solutions hanging under it (solutions A–F in 05 §4) are downgraded accordingly.
5. **Solution layer** only hangs the solutions already in 05 §4 and the G-numbered items; no new solutions are added during the research period, to avoid "researching and designing at the same time."
6. **Version log**: update once a week on Sunday, and record at the end of `07_research_findings.md` "which nodes were added / deleted / downgraded this week, and on what basis."

**OST text skeleton (to be executed)**:

```
Desired outcome: number of commitments per week the target team confirms and closes out
├── Opportunity O1: (to be executed, in user language) [support n/N | cost | H__ | card ID]
│   ├── Solution: (05 §4 solution _ / G__)
│   │   └── Assumption test: (to be executed)
├── Opportunity O2: (to be executed)
└── Candidate opportunities (supported by 1 person only): (to be executed)
```

### 7.4 "Research Findings" Report Skeleton (written to `02_user-research/07_research_findings.md`, all to be executed)

```
---
title: User Research 07: Research Findings (Round 1 Interviews + 2-Week Diary Study)
status: to be executed
sample: interviews __ people (S1 __ / S2 __ / S3 __ / S4 __ / S5 __ / S6 __); diary __ people × 14 days; R0 listed separately
---

## 0. One-Sentence Conclusion (to be executed)
## 1. Method and Sample (to be executed)
   - Recruitment channels, quota completion, unfilled quotas and reasons
   - IRB determination result and date
   - Bias notes: share from our own group, number of relationship-biased participants, how R0 data is handled
## 2. Hypothesis Verdict Table (to be executed)
   | ID | Support line | Rejection line | Actual evidence (n/N or value) | Verdict: supported / rejected / gray zone | Evidence card ID |
## 3. Diary Study Numbers (to be executed)
   - Commitment frequency (median, range)
   - 48-hour logging rate (per-person median, pooled)
   - Recall-failure frequency, forgotten/disputed rate, share of commitments from superiors, share of soft commitments
   - Stratified by meeting type
   - Data quality (completion rate, self-reported missed entries)
   - Counting-convention calibration results
## 4. Manual Backfill Test Results (U-H04, U-H05) (to be executed)
## 5. Main Themes (Affinity Diagram) (to be executed)
   - For each theme: definition, supporter count, academic vs. industry comparison, representative anonymous quotes (consent required)
## 6. Commitment Currency Statistics (to be executed)
   | Level | Number who requested | Number who accepted | Number fulfilled |
## 7. Surprises and Overturned Presuppositions (to be executed)
## 8. Impact on 05 Solutions A–F (per the §1.2 decision tree) (to be executed)
## 9. Opportunity–Solution Tree (Updated) (to be executed)
## 10. Interview Answer Template, Fill-in (00/02 §6 G) (to be executed)
   "In __ interviews and a 2-week diary study with __ people, I found..."
## 11. Limitations and Next Steps (to be executed)
## Appendix: OST Version Log (to be executed)
```

---

## 8. Execution Timeline (One-Page Version)

> Start: (Monday). Today (Sunday), is for reading through this file and preparing the forms. Research runs in parallel with the demo's competitor error analysis (05 Q1) and takes about 2–3 hours per day.

| Date | Research task | Output / completion marker |
|---|---|---|
| **Day 0, 11/01 (Sun)** | Read this file; build the screening questionnaire and Forms 1, 2, 3 in the form tool; print the §3.3 timeline sheet | 4 form links working |
| **Week 1** | | |
| 11/02 (Mon) | ① Send the IRB determination email (§6.3), cc or inform the advisor ② **R0 diary starts** (the project owner personally, running Forms 1/2/3 for a week first, which also tests the forms) ③ Send the first batch of recruitment DMs: 3 PhD students from adjacent groups, 2 industry ML practitioners, 1 student from our own group | Email sent; first R0 entry; recruitment sent to 6 people |
| 11/03 (Tue) | Interview **#1** (PhD student from an adjacent group, not recorded, skip PhD-Q5 and Q15 until the IRB replies) | Notes template filled in; three surprises written down within 30 minutes |
| 11/04 (Wed) | Interview **#2** (industry ML comparison); revise questions in the guide that were misunderstood in #1 | Interview guide v1.1 |
| 11/05 (Thu) | Interview **#3** (PhD or master's student from an adjacent group); send 2–3 PI emails; recruit 4–5 diary participants | PI invitations sent |
| 11/06 (Fri) | Interview **#4** (industry ML comparison or university–industry joint lab); book Week 2 interviews | 4 people done in Week 1 |
| 11/07 (Sat) | First round of affinity-diagram coding; record the number of new codes; review R0's week of data and check the forms for ambiguity | Codebook v1; forms finalized |
| 11/08 (Sun) | Pre-briefing for diary participants (15 minutes online, can be merged into 1–2 sessions); update OST v1 | 4–5 diary participants confirmed |
| **Week 2** | | |
| 11/09 (Mon) | **Diary study officially starts** (14 days, through 11/22); decide whether to start recording and sensitive questions based on the IRB reply | First batch of form submissions |
| 11/10–11/13 | Interviews **#5–#9**: 2–3 PIs, 1 PhD student from our own group, 1 postdoc, 1 industry ML practitioner, 1 university–industry joint lab member (fill quota gaps) | 9 interviews cumulative |
| 11/11–11/14 | **Manual backfill test** (§4.6): send the backfill request to each diary participant 1 day before their next meeting; after one student agrees, send a confirmation draft to their PI | Initial values for backfill rate and PI confirmation |
| 11/12 | Counting-convention calibration: R0 and 1 diary participant record the same group meeting of our own group simultaneously | Calibration discrepancy log |
| 11/14–11/15 | Commitment fulfillment check (were the L1–L3 commitments of Week 1 interviewees fulfilled?); second round of affinity-diagram coding; saturation check; OST v2 | Codebook v2; fulfillment table updated |
| **Week 3** | | |
| 11/16–11/19 | Interviews **#10–#16** (fill quotas: master's students, non-computational labs, a 2nd university–industry joint lab member, 3rd–4th industry practitioners); may end early if the stopping rule is met | 12–16 interviews |
| 11/20–11/22 | Wrap up the diary study; 15-minute exit interview with each participant (verify 2–3 events); distribute incentives and personal data summaries | Diary data exported (de-identified) |
| 11/23 (Mon) | Compute metrics per §4.7; judge each hypothesis per §1.2; apply the decision tree | Hypothesis verdict table |
| 11/24–11/25 | Write `07_research_findings.md` (§7.4 skeleton); update the OST; carry conclusions into `03_positioning` | Research findings report v1 |

**Minimum deliverable version** (if time is compressed to 2 weeks): 8 interviews (5 academic + 3 industry) + 4 diary participants × 10 days + 1 round of manual backfill testing. With less than this, the report must state "evidence is insufficient to judge U-H01/U-H02" and must not draw a conclusion. **[Inference]**

**Risks and responses**:

| Risk | Response |
|---|---|
| IRB is slow to reply | In Week 1, only do interviews that are unrecorded, contain no sensitive questions, and are not with our own group; if there is still no reply in Week 2, follow up by phone or ask the advisor to inquire |
| Can't book PIs | Switch to a 15-minute version (PI-Q1, Q2, Q4, Q8, Q9 + commitment test); or catch them in gaps before and after the PI's office hours |
| Diary attrition | Recruit 1 extra person; DM anyone with no submission for 2 consecutive days; give incentives based on completion |
| Too many participants from our own group (self-projection) | Our own group ≤40% is a hard cap; stop recruiting from our own group once exceeded |
| Many interviewees "can't recall a specific event" | This is data, not failure. Record it as "couldn't recall," count it in the denominator; if 3 consecutive people can't recall, check whether the opening failed to anchor on one specific meeting |

---
## Source List (all accessed at the time of writing)

**Official pages opened in this round**
1. (University) IRB, Do I Need IRB Approval — (university page; link removed) [Fact]
2. (University) IRB homepage — (university page; link removed) [Fact]
3. (University) IRB, Not Under IRB — (university page; link removed) [Fact]
4. (University) IRB, Exempt Review — (university page; link removed) [Fact]
5. (University) IRB, Exempt Category 2 — (university page; link removed) [Fact]
6. (University) IRB, Review Not Required (RNR) Category — (university page; link removed) [Fact]
7. (University) IRB, Minimum Training Requirements — (university page; link removed) [Fact]
8. (University) IRB, Students Conducting Human Subjects Research — (university page; link removed) [Fact]
9. (University) IRB, Forms (forms are on the intranet; template contents to be verified) — (university page; link removed) [Fact]
10. (University) IRB, Submission Timeline — (university page; link removed) [Fact]
11. mtlynch.io, The Mom Test book report — https://mtlynch.io/book-reports/the-mom-test/ [Fact]

**Only search snippets seen, or page opened with no body text**
12. A Singapore university, Industry Partnerships (list of university–industry joint labs) — (university page; link removed) [Summary]
13. NRF Corporate Laboratories — https://www.nrf.gov.sg/programmes/corp-labs/ [Summary]
14. PDPC, Data Protection Obligations (page opened but body text did not render) — https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act/data-protection-obligations To be verified
15. Singapore Statutes Online, PDPA 2012 (403) — https://sso.agc.gov.sg/Act/PDPA2012 To be verified
16. Flanagan (1954), The Critical Incident Technique, *Psychological Bulletin* (page did not load) — https://psycnet.apa.org/doi/10.1037/h0061470 To be verified

**Cited from `00_pm-skills/02` (verified in round one, not reopened in this round)**
17. Teresa Torres, Best Customer Interview Questions — https://www.producttalk.org/best-customer-interview-questions/
18. Teresa Torres, Opportunity Solution Tree — https://www.producttalk.org/2016/08/opportunity-solution-tree/
19. NN/g, Diary Studies — https://www.nngroup.com/articles/diary-studies/
20. Bob Moesta / Chris Spiek, The Four Forces — https://jobstobedone.org/the-four-forces/
21. YC Startup School Week 1 Recap (Eric Migicovsky: "What's the hardest part?") — https://www.ycombinator.com/blog/startup-school-week-1-recap-kevin-hale-and-eric-migicovsky

**Internal project files**
- `00_pm-skills/02_product_discovery_methods.md` (Mom Test, JTBD, Four Forces, OST, steps 3–8, pain-point list)
- `01_market-research/05_gap_synthesis_opportunities.md` (Q3, Q4, Q5, Q8, Q13; options A–F)
- `01_market-research/06_research_integrity_review.md` (P0: zero interviews; recommendations on a control group and new segments)
- `02_user-research/01_segment_academic_labs.md` (H1–H6, meeting landscape, risks)
- `02_user-research/03_research_commitment_tracking_specifics.md` (H-A to H-E)
- the earlier v1 docs (not included): the old interview guide and research plan (old outline and stopping rules)

---
## Credibility Notes for This Document

| Content | Credibility | Notes |
|---|---|---|
| The target university's IRB rules (§6.1) | **High** | 10 official pages were opened on the day; however, the page contents were paraphrased by the WebFetch summarization model, with key sentences preserved in the original English; it is advisable to re-read the details of the Exemption Category 2 and RNR pages by hand before execution |
| "This project falls in a gray area and should first request a determination" (§6.2) | **Medium** | An inference from the official rules, not an IRB determination; **the written reply from irb@university.example takes precedence** |
| PDPA and the target university's IT policy | **Low (to be verified)** | The full text was not obtained in this round |
| Mom Test rules and commitment currency | **High** | The book-excerpt page was opened and checked on the day |
| Methodology (Torres, NN/g, Four Forces, YC) | **Medium-high** | Checked in the first round; not reopened in this round |
| Hypothesis decision thresholds (§1.2) | **[Assumption · to be validated]** | Set in this document to prevent moving the goalposts after the fact; not thresholds from the literature. U-H11 was lowered relative to the original U3 threshold, as explained in the table |
| Interview guide, diary fields, commitment-test scripts, schedule | **[Inference]** | Method design, not piloted; the first 2 interviews in Week 1 are the pilot, and adjustments are expected |
| Any research findings | **None** | This document contains no real interview or diary data; all findings fields are empty, pending execution |
