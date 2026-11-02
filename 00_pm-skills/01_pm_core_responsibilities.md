---
title: "Core PM Responsibilities and Cautions: A Master Checklist (for BriefPilot v2)"
status: draft
sources_count: 34
sources_count_method: Number of unique URLs in the sources section (recalculated at wrap-up; original value 27)
evidence_note: This is a first-round file. The body does not consistently distinguish [Fact] from [Summary], and sources do not record individual access dates (all treated as at the time of writing). Any item marked [Fact] whose body has no "opened the original page" record should be treated as [Summary·to be verified] before it is cited (added in the wrap-up revision).
---

# Core PM Responsibilities and Cautions: A Master Checklist (for BriefPilot v2)

> **How to read this document**
> - This file is the "PM skills foundation" for the BriefPilot v2 differentiation project. Its purpose is not to list theory, but to translate widely accepted PM principles into **actions that can be executed on this project right away**.
> - Every item carries an evidence level: **[Fact]** = has a verifiable source; **[Inference]** = reasonable inference based on facts; **[Assumption]** = still to be validated; **[To be verified]** = found in search but the original page could not be opened, or only secondary sources exist.
> - An honest statement about sources: several key Lenny's Newsletter articles ("How to know if you're doing a good job as a PM", "14 habits of highly effective PMs", "What makes a great PM") are paywalled, and this round **could not read the full text**; only their public summaries or free portions are cited. **No reliable public material was found** on ByteDance's product-track competency model. The views from *Yu Jun's Product Methodology* come from secondary interpretations (Everyone Is a Product Manager, 36Kr), not from the book itself. All of these are flagged individually in the text.
> - Research was completed. The web search quota for this round has been used up, so a few items (see "To be verified") are left for the next round.

---

## 0. First, answer a "why": why should BriefPilot v2 build PM method first instead of going straight to differentiation?

**[Inference]** The problem with the previous BriefPilot version (S0) was not that it was "poorly built" but that the **order was reversed**: the solution "RAG + action items + human confirmation" came first, and users and problems were sought afterward. The PRD itself honestly labels all users and pain points as HYPOTHETICAL, and `docs/research/findings.md` is still "not yet started" (see the earlier v1 docs (not included), the README and PRD §1.4 and §2). This is exactly a combination of the classic mistakes discussed below: **solution-first thinking**, **writing a PRD without validation**, and **feature-parity thinking ("if others have it, I must have it too")**.

When an interviewer or client asks, "Feishu Minutes, Otter, and Fireflies already do this, so why are you building it?", they are essentially asking about two of the four risks: **value risk and viability risk** (Cagan's definitions, see §2.1). Only by getting the method right can differentiation research avoid becoming, once again, "finding reasons for an existing solution."

---

## I. Mindset & Principles

### 1.1 A PM is accountable for outcomes, not outputs

- **[Fact]** In the SVPG article *Product vs. Feature Teams*, Marty Cagan divides teams into three kinds: delivery teams (measured on output), feature teams (given a "feature roadmap", measured on output), and product teams (empowered, given "problems to solve", measured on outcome). In a feature team, the PM is "mainly project manager, and partly (unskilled) designer", and value and feasibility are the responsibility of the executive who requested the work; in a product team, the PM is "explicitly responsible for ensuring value and viability". Source: https://svpg.com/product-vs-feature-teams/
- **[Fact]** The core argument of Melissa Perri's *Escaping the Build Trap* (O'Reilly, 2018): when an organization measures success by "how many features were shipped" rather than "what results were produced", it falls into the build trap. She distinguishes outputs (features, releases, velocity) from outcomes (the results of solving customer problems), and notes that "outputs are necessary to produce outcomes, but outputs alone do not guarantee value". Sources (secondary summaries; the original book page returned 403 and could not be opened): https://evansamek.substack.com/p/escaping-the-build-trap-by-melissa ; https://www.bennadel.com/blog/3967-escaping-the-build-trap-how-effective-product-management-creates-real-value-by-melissa-perri.htm
- **Why it matters**: If output is the goal, "building a meeting-to-tasks demo" counts as success in itself, and the interviewer's question can never be answered. If outcome is the goal, you must answer "who, in what scenario, saved how much time or made how many fewer mistakes."
- **Applying it to BriefPilot**: The success definition for v2 cannot be "the demo runs end to end"; it must be a measurable user outcome, for example "after a real meeting, the target user produces accepted action items within X minutes, with an acceptance rate ≥ Y%" (specific numbers to be set once 02_user-research provides a baseline). The S0 PRD already set "number of tasks confirmed as completed", rather than token volume, as the North Star metric (see the decision table in `docs/portfolio-case-study.md`). That direction is right, and v2 should keep and refine it.
### 1.2 Fall in love with the problem first, then with the solution (anti solution-first)

- **[Fact]** In *The Product Kata* (2015-07-22), Perri looks back on her failed Seller Portal: "We really didn't understand their needs from the short time we spent interviewing them." The six steps of the Product Kata she proposes: set a direction → **understand the current condition (the most frequently skipped step)** → set a target condition → list obstacles → run small experiments ("A step with no measurements can't tell you if you are improving", ideally with steps no longer than a week) → record what you learned and return to the target. Source: https://melissaperri.com/blog/2015/07/22/the-product-kata
- **[Fact]** Su Jie's *Everyone Is a Product Manager* distinguishes "user needs" (what users think they need, often expressed in the form of a solution) from "product needs" (the real need found through analysis), and has a dedicated section titled "Listen carefully, but don't do as they say". Source (secondary): https://www.woshipm.com/pmd/4477209.html ; https://www.36kr.com/p/990643702555271
- **Why it matters**: The S0 version's "RAG + citations + confirmation gate" is an elegant solution, but it was fixed before any interview took place. No matter how elegant a solution is, it cannot answer "why would users replace Feishu Minutes?"
- **Applying it to BriefPilot**: The v2 process explicitly states that until at least 5 interviews in `02_user-research` are complete and a "current-state baseline" has been written, the `04_prd` directory **must not contain any feature descriptions**. The Product Kata's "understand the current condition" is put into practice as: record how target users currently handle meeting → action items (which tools they use, how long it takes, where errors occur), rather than asking directly "would you want AI to generate action items for you?"

### 1.3 User value = new experience − old experience − switching cost

- **[Fact]** This is Yu Jun's most widely circulated formula; several commentaries use Bullet Messenger vs. WeChat as an example: even if the new experience has an advantage, high switching costs such as the social graph can make the user value negative. Some authors criticize the formula for mixing variables of different dimensions and being hard to quantify, and use an ROI comparison instead. Source (secondary): https://www.woshipm.com/pd/6300702.html ; https://www.woshipm.com/pd/3402762.html
- **[To be verified]** The publisher/year of the original book *Yu Jun's Product Methodology* and its original wording could not be checked in this round (search quota exhausted); marked as to be verified.
- **Why it matters**: This formula is directly the mathematical form of the interviewer's question. Feishu Minutes is already built into Feishu, and Otter/Fireflies connect to Zoom/Teams in one click: **the old experience is already good, and the switching cost is close to zero**. For user value to be positive, BriefPilot has to focus on a niche segment where **the old experience is clearly poor and existing tools won't fill the gap for structural reasons**.
- **Applying it to BriefPilot**: In `01_market-research`, write one line per candidate segment: "what the old experience is, what the switching cost is". Screening criterion: only segments with "a large old-experience gap + low switching cost (e.g., target users have no unified meeting tool to begin with)" advance to the next round. Research labs are one of the candidates (group meetings often use Zoom/in person, there is no mandatory IM platform, and minutes are handwritten by students), but this is only an **[Assumption]** and needs to be confirmed through interviews.

### 1.4 Deep user knowledge + technical possibility is what distinguishes a PM from other roles

- **[Fact]** In *Product Manager vs. Product Owner*, Cagan writes: "Deep customer knowledge is what informs the decisions", and "it's essential that the product person has the direct customer interaction"; combining customer understanding with "the ability to solve customer problems with technology" is what makes a strong PM. Source: https://svpg.com/product-manager-vs-product-owner/
- **[Fact]** Yu Jun (secondary quotation): "Users are not natural persons, but collections of needs"; users have five attributes: heterogeneity, situational context, malleability, self-interest, and bounded rationality; "every proactive user action is a transaction with the world", and transaction costs fall into three categories: search/measurement, price-seeking/decision, and implementation/assurance. Source: https://www.woshipm.com/pd/3402762.html
- **Why it matters**: The project owner is a member of a research lab at the target university and is also working on a VLA survey, so has **first-hand experience** of "how research groups hold meetings, track tasks, and find literature evidence". This is a natural advantage for the direct customer interaction Cagan describes. But "being your own user" is also the most common source of bias (n=1).
- **Applying it to BriefPilot**: Write up your own experience as the **first interview record** (respondent_id = R0), then find at least 5 lab members or users from other segments who are **not yourself**. Using Yu Jun's "users are collections of needs" perspective, break "lab members" down into: advisor, PhD student, master's student, RA. Their needs within the same group meeting clearly differ (**[Inference]**).

### 1.5 Skepticism and sample size (Yu Jun's three simplified methodologies)

- **[To be verified / secondary]** A reposted article claims that Yu Jun simplified his methodology into three points: "balance of product interests, user sample size, and skepticism". Source: https://www.woshipm.com/pmd/381195.html (repost, original source not stated)
- **Applying it to BriefPilot**: Any differentiation conclusion must state its "sample size n and recruitment channel"; conclusions without n are always labeled [Assumption].

### 1.6 Lenny: the PM's job is "marshaling team resources to identify and solve the most impactful customer problems"

- **[Fact]** In *How AI will impact product management* (2024-04-09, free portion), Lenny Rachitsky defines the PM's job: "deliver business impact by marshaling the resources of your team to identify and solve the most impactful customer problems". Source: https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management
- **[To be verified]** Lenny's "How to know if you're doing a good job as a product manager" (2021-06-29, subtitle "The three things you need to get right") and "14 habits of highly effective product managers" are both paywalled, so the specifics of the three things could not be read in this round, and **this document does not cite their contents**. Source page: https://www.lennysnewsletter.com/p/doing-a-good-job-product-manager
- **Applying it to BriefPilot**: Even a one-person project should spell out its "team resources": the user themself (PM + researcher), AI coding tools (engineering), and interviewees (users). This avoids the PM doing everything personally and losing sight of the core duty of "identifying the most impactful problems".

---
## 2. Discovery

### 2.1 The four big risks: value, usability, feasibility, business viability

- **[Fact]** Cagan (SVPG, *The Four Big Risks*):
  - Value risk: "whether customers will buy it or users will choose to use it"
  - Usability risk: "whether users can figure out how to use it"
  - Feasibility risk: "whether our engineers can build what we need with the time, skills and technology we have"
  - Business viability risk: "whether this solution also works for the various aspects of our business"
  - The PM owns value and viability; the designer owns usability; the engineering lead owns feasibility. Cagan says value risk is usually the hardest; strong teams "tackle big risks early, especially value and business risk". Source: https://svpg.com/four-big-risks/
- **Why it matters**: In S0, BriefPilot put almost all of its effort into feasibility (RAG, citation checking, state machine, ADRs) and usability (flow charts, wireframes), and barely touched the hardest risks, value and viability (who pays? why not just use Feishu?). This is exactly where the interviewer's questions landed.
- **Applying it to BriefPilot**: In v2, every candidate segment gets a "four-risk table", and the rule is that **value risk must be tested before any technical design**. For the research-lab hypothesis, the minimal value-risk test could be: take a real group-meeting recording transcript (anonymized), manually produce "action items with literature citations", show them to 3 group members, and observe whether they are willing to keep using them next week (a Cagan-style prototype-based test, **[Inference]**).

### 2.2 Continuous discovery: weekly user contact, organized with an opportunity-solution tree

- **[Fact]** Teresa Torres (Product Talk): good teams "engage with customers at least weekly"; there are two core weekly activities, customer interviews (to discover opportunities) and assumption testing (to evaluate solutions); the opportunity solution tree (OST) is structured as Outcome → Opportunities → Solutions → Experiments; "Product discovery is a decision-making process". Source: https://www.producttalk.org/2021/08/product-discovery/
- **[Fact]** Cagan's Customer Discovery Program recommends finding **6** reference customers from the same segment for a B2B product. Source: https://svpg.com/charter-customer-programs/ (confirmed this round only via search snippets; the page was not opened; marked **[To be verified]**)
- **Why it matters**: Differentiation is not produced by a one-off study; it "grows" out of continuous contact. Running one round of 10 interviews and then writing a PRD behind closed doors is still project-style research.
- **Applying it to BriefPilot**: Starting this week, fix "at least 1 user contact per week" (this can be a 15-minute informal interview after a group meeting), recorded in `02_user-research/weekly-touchpoints.md` (**not adopted**: this file was never created; it was replaced by the diary study in `02_user-research/06_user_research_kit.md` §4 and `05_demo-plan/eval-kit/templates/h7_dogfood_log.md`; note added at wrap-up). Use the OST to hang "candidate differentiators" at the opportunity level rather than the solution level. Goal: find 6 "reference users" willing to keep trying the product (if the segment is research labs, span 2-3 different research groups, to avoid relying only on our own group).

### 2.3 Avoiding bias in interviews: The Mom Test

- **[Fact/secondhand]** Rob Fitzpatrick's *The Mom Test* has three rules: talk about their life rather than your idea; ask about specific past events rather than generic habits or predictions; talk less and listen more. Three kinds of bad data: compliments, fluff, and ideas. Sources: https://www.shortform.com/blog/what-is-the-mom-test/ ; https://www.ybrikman.com/blog/2023/03/29/the-mom-test/
- **Why it matters**: When the user interviews colleagues from the same lab, the other person is very likely to say out of politeness, "Sounds good, I'd use it."
- **Applying it to BriefPilot**: In v2, go through the interview guide (S0 already has `docs/research/interview-guide.md`) question by question against the Mom Test: delete every question of the "do you think this feature is useful?" kind and replace it with "After the last group meeting, how did you note down what you needed to do? How long did it take? Have you ever missed something? What were the consequences?"

### 2.4 The Y model: from user needs, probing to user goals, and back to product features

- **[Fact/secondhand]** Several articles in the Everyone Is a Product Manager community (人人都是产品经理) describe the Y model as: 1 user need (surface request) → 2 underlying goal/motivation → 3 actionable product feature, with 4 being the deeper human need; the core technique is to keep asking "why". Sources: https://www.woshipm.com/pd/6122327.html ; https://www.woshipm.com/pd/3762064.html
- **[To be verified]** Whether the Y model was proposed by Su Jie could not be confirmed in this round of searching, so only the model itself is cited.
- **Applying it to BriefPilot**: Every interview quote must go through the "1→2" conversion before it enters the requirements pool. For example, a user says "I want meetings to generate tasks automatically" (1); follow-up questions may reveal "I'm afraid I'll forget to do it before my advisor asks next week" (2), which means the product feature may be "reminders and an evidence chain" rather than "task generation".

---
## 3. Definition (From Problem to PRD)

### 3.1 Prioritization frameworks: RICE / ICE / Kano / MoSCoW — use them in the right context, and don't worship the scores

| Framework | Definition (fact) | Suitable context (inference) | How it is used in BriefPilot v2 |
|---|---|---|---|
| **RICE** | Per the original Intercom post: Reach = number of people/events affected in a given period (Intercom uses customers per quarter); Impact has five levels: 3/2/1/0.5/0.25; Confidence is 100%/80%/50%, with <50% called a "total moonshot"; Effort = total person-months across product + design + engineering, recorded as 0.5 if under one month; score = R×I×C÷E. Intercom explicitly says the score is "not a hard rule" and can be overridden by dependencies or sales needs. Source: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/ | Feature-level ranking, when some data is available | Used to rank features within the demo scope. **Pay special attention to Confidence**: any feature without interview evidence must not have Confidence above 50%, and is downgraded automatically |
| **ICE** | Impact/Confidence/Ease are scored and multiplied; originates from Sean Ellis's growth-experiment method (**[To be verified]**, the original page was not opened in this round) | Fast, coarse-grained ranking of experiments | Used to rank "validation experiments for differentiation hypotheses", not features |
| **Kano** | Proposed by Noriaki Kano in 1984; categories: must-be/threshold, performance/one-dimensional, attractive/delighter, and indifferent, plus reverse (not covered by this round's sources). Usage: classify internally first, then validate with users via a questionnaire. Source: https://www.productplan.com/glossary/kano-model/ | Deciding "what is table stakes, and what creates differentiation if built" | **This is the most useful framework for answering the interviewer's question**: "meeting-to-tasks" is already a must-be feature in 2026 (users complain if it is missing, and building it creates no differentiation). Differentiation must land in the attractive category. Use the Kano questionnaire (how would you feel if the feature were present / absent) to validate candidate delighters with target users |
| **MoSCoW** | Must/Should/Could/Won't; proposed by Dai Clegg in 1994 (most sources say at Oracle at the time, a few say British Airways, **sources conflict**), later widely adopted by DSDM. Source: https://en.wikipedia.org/wiki/MoSCoW_method | Scope negotiation within a fixed timebox | Used to freeze the demo scope: the Won't list matters as much as the Must list, and both go into `05_demo-plan` |

- **[Fact]** Sign #7 in John Cutler's feature-factory list is exactly "Obsessing about prioritization": spending lots of effort choosing what to build, and rarely checking whether the choice was right. Source: https://cutle.fish/blog/12-signs-youre-working-in-a-feature-factory
- **Why it matters**: Frameworks are communication tools, not oracles. Assigning RICE scores to a feature with no user data, as in S0, only dresses up an "assumption" as "data".

### 3.2 Validate before writing the PRD; a PRD is a decision record, not a wish list

- **[Fact]** Cagan's view of discovery: discovery is the work of deciding what to build before committing engineering, with the goal of reducing the four big risks before delivery; strong teams test 10-20 or more ideas per week, mostly based on prototypes. Sources (secondary summaries; the original book was not opened): https://www.shortform.com/blog/inspired-product-management/ ; https://svpg.com/four-big-risks/
- **[Fact]** Amazon Working Backwards / PR-FAQ: write the internal press release and FAQ before building the product; the book version requires the press release to be "less than one page". Sources (secondary): https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes ; https://www.modelthinkers.com/mental-model/amazons-working-backwards
- **Why it matters**: The S0 PRD has 36 evaluation cases and 4 ADRs, yet its user sections are entirely HYPOTHETICAL. This is a classic symptom of "the PRD was written before the research", and also Cutler's sign #9, "Culture of hand-offs" (front-loading work into documents so it is "ready for engineering").
- **Applying this to BriefPilot**:
  1. Before the v2 PRD, write a one-page PR-FAQ (`03_positioning/pr-faq.md`, to be added at the wrap-up, with content extracted from the Q&A notes (not included in this repository)). The press release must contain a **specific user persona and specific numbers**; if it cannot be written, discovery is not finished.
  2. Add an "Evidence ID" column after each requirement in the PRD (pointing to an interview record or experiment); items without evidence can only go in the "assumptions section".
  3. Keep S0's practice of a contingency plan for "how to change the PRD if validation fails" — this is one of the few things S0 got right.

### 3.3 Defining "what we won't do" and "who we won't serve"

- **[Fact]** S0 PRD §2.2 already explicitly excludes legal/medical use, sensitive PII, autonomous external actions, and audio/video teams.
- **[Inference]** v2's differentiation will make the "who we won't serve" list longer and sharper (for example, explicitly excluding enterprise IT procurement scenarios). This is a good thing: the narrower the positioning, the easier it is to prove value in the demo.

---
## 4. Delivery (Follow-through and Launch)

### 4.1 Small batches and continuous iteration, not big releases

- **[Fact]** Cutler's sign #10, "Large batches": even when working in sprints, features still ship as a single large release. Sign #8, "No tweaking": once something ships, the team moves straight to the next project without iterating on data. Source: https://cutle.fish/blog/12-signs-youre-working-in-a-feature-factory
- **[Fact]** Perri's Product Kata requires steps of no more than one week, and they must be measurable. Source: https://melissaperri.com/blog/2015/07/22/the-product-kata
- **Applied to BriefPilot**: The demo plan works at weekly granularity, with one increment per week that can be shown to users (even if it is only a hand-drawn prototype), rather than the eight-stage S1-S8 waterfall of the S0 handbook.

### 4.2 The PM's job during delivery: clear obstacles, make decisions, don't be a project manager stand-in

- **[Fact]** Cagan points out that PMs on feature teams degrade into "mostly project managers". Source: https://svpg.com/product-vs-feature-teams/
- **[Inference]** When a solo builder develops with AI coding tools, the biggest risk is spending all their time tweaking code (feasibility) and forgetting to keep talking to users (value).
- **Applied to BriefPilot**: Set a hard rule for yourself: weekly user-contact time ≥ 1/3 of coding time (**[Assumption]**; the ratio is adjustable).

### 4.3 Launch is an experiment: don't ship without measurement

- **[Fact]** Cutler's sign #1, "No measurement", and sign #3, "Success theater" (celebrating the release without discussing its impact). Source: same as above.
- **Applied to BriefPilot**: Every demo feature must have a "success metric + baseline + measurement method" written in advance in `05_demo-plan`. The S0 `docs/analytics/event-taxonomy.md` can be reused, but the events need to be re-trimmed around the new North Star.

---

## 5. Measurement

### 5.1 Outcome metrics first, output metrics second

- **[Fact]** Perri: outputs do not guarantee value. Torres: the top of the OST is the product outcome, which should be a leading indicator of the business outcome. Source: see §1.1 and §2.2.
- **Applied to BriefPilot** (**[Inference/to be validated]**, example metrics):
  - North Star: **number of action items confirmed by users and completed before their deadline** (direction already set in S0).
  - Leading indicators: draft acceptance rate, rate at which users fill in missing fields, time taken to produce action items after each meeting.
  - Trust metric: whether users keep using the product after a refusal to answer (the S0 E4 experiment).
  - Counter-metrics (guardrails): number of wrong-owner assignments, share of drafts that get deleted.

### 5.2 PM retrospectives: go back and check whether past decisions were fulfilled

- **[Fact]** Cutler's sign #6, "No PM retrospectives": the PM does not review whether their decisions delivered the expected benefit, and treats speed/output as the KPI. Source: same as above.
- **Applied to BriefPilot**: Add a "review date" field to every ADR; when it comes due, backfill "actual result vs. original rationale". S0's ADR-002 (human confirmation gate) and ADR-003 (RAG rather than fine-tuning) should both be reviewed after the demo.

### 5.3 Honesty about sample size and baselines

- **[Fact]** S0's `portfolio-case-study.md` already states that "estimated or demo values must not be filled in before the work is complete."
- **Applied to BriefPilot**: Continue this rule. Any number shown to interviewers must come with n, the time period, and the measurement method.

---

## 6. Communication (with Engineering, Design, Clients/Interviewers)

### 6.1 Give engineering "the problem to solve", not "the feature to build"

- **[Fact]** Cagan: product teams are given problems rather than features, "empowered to figure out the best way to solve the problems". Source: https://svpg.com/product-vs-feature-teams/
- **Applied to BriefPilot**: Prompts to AI coding tools should work the same way: first give the user problem, constraints, and success criteria, then have the tool propose solutions and explain the trade-offs, rather than handing it a feature list directly (the P0-P9 prompts in the S0 handbook lean toward the latter; v2 can rewrite them).

### 6.2 For clients/interviewers: answer "why build this at all" with "old experience vs. new experience vs. switching cost" and "Kano basic vs. delighter"

- **[Inference]** Combine §1.3 and §3.1 into a standard answer framework:
  1. Concede: turning meetings into tasks is a basic feature in 2026, and Feishu Minutes / Otter / Fireflies already cover mainstream office scenarios (for the detailed feature comparison see `01_market-research`; this file makes no assertions about it).
  2. Point out: in [target segment], the old experience is [specific description], and existing tools do not cover it because of [structural reason], backed by interview quotes and n.
  3. Prove: the demo validated that [delighter feature] had an acceptance rate of [number] among [n users].
  4. Acknowledge the boundary: this is not about replacing Feishu Minutes, but about going deep in the [segment] it does not cover.
- **Why it matters**: Interviewers don't want a feature comparison table; they want to see whether "you have a way of judging things that holds together on its own terms".

### 6.3 With design: a PM is not an unskilled designer

- **[Fact]** Cagan criticizes feature-team PMs as "partly (unskilled) designer". Source: same as above.
- **[Inference]** A solo project has no designer, so usability risk has to be addressed through "usability testing with 5 users" rather than considering the work done once you have drawn the wireframes yourself.
### 6.4 Written Communication: Decision Records + Evidence Grading

- **[Fact]** S0 already established rules for three kinds of wording: "fact / assumption / experiment goal" (`docs/portfolio-case-study.md`).
- **Applied to BriefPilot**: all v2 files continue to use the four evidence labels used in this document — [Fact] / [Inference] / [Assumption] / [To be verified] — and end with a list of sources.

### 6.5 Level-Based Competency Models: What Public Sources Can Tell Us

- **[Fact]** Google PM levels: numbering differs across sources and the sources conflict with each other (one version: APM L2/L3 → PM L4/L5 → Senior L6 → Group PM L7; another: L3 APM → L4 → L5 Senior → L6 Staff → L7 → L8). What they share: a move from "executing within a given scope" to "creating scope for the organization." Sources: https://www.aakashg.com/google-product-manager/ ; https://blog.tryexponent.com/product-manager-career-path/ (both third-party; Google has not published anything official)
- **[Fact]** Meta PM: IC4 is the entry level, IC5 is a common landing level for industry hires, IC6 leans toward lead. A 2020 Blind post describes IC4 as "one team, lots of oversight" and IC5 as "self directed." Sources: https://www.news.aakashg.com/p/meta-pm-job ; https://www.teamblind.com/post/leveling-facebook-pm-ic4-vs-ic5-5opxgxmv (anonymous forum; low credibility)
- **[Fact]** Tencent: a 2014 article on 人人都是产品经理 (Everyone Is a Product Manager) (author Blues, a former senior PM at Tencent) lists 18 competencies (learning ability, execution, communication, industry integration, mindset and EQ, technical literacy, project management, related knowledge, product planning/release management, professional design, market analysis, BD, data analysis, marketing, channels, user research, methodology building, knowledge transfer), and states that Tencent P3-1 ≈ Alibaba/Baidu P6. **Note**: the article describes itself as a synthesis of the standards of Tencent, YY, Alibaba and Baidu, and is **not an official Tencent framework**; the claim in a search snippet of "4 parts, 19 items, 5 grades, 15 levels" does not match the original article. Source: https://www.woshipm.com/pmd/88721.html
- **[To be verified]** ByteDance product-track competency model: no reliable public source found; only secondhand descriptions of the 10-level engineering track exist.
- **Inference for BriefPilot**: the common thread across these models is "scope from small to large + from executing to defining the problem." For career changers, what a demo must prove is not "I can build a feature" but "I can independently define a problem worth solving and validate it" — which is exactly the dividing line between L4/IC4 and L5/IC5.

---

## 7. AI-Era Additions

### 7.1 Evals Are the Core New Skill for AI PMs

- **[Fact]** Aman Khan (Director of Product at Arize AI), in Lenny's Newsletter, *Beyond vibe checks: A PM's complete guide to evals*: evals work like regression tests/benchmarks and define what "good" looks like; there are three types — human evals, code-based evals, and LLM-as-judge; common dimensions include hallucination (whether the output is grounded in the given context), toxicity, correctness, and retrieval relevance; he advises not to ship an AI product before it passes deliberately designed evals, and to start with open-source tools (Phoenix, Ragas). Source: https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete
- **[Fact]** Hamel Husain: do error analysis first (read logs/traces and annotate them), then write evals; "a common mistake is writing the scoring rubric before having read any traces"; he and Shreya Shankar report spending 60-80% of development time on error analysis and evaluation; use synthetic data when there are no real users. Sources: https://hamel.dev/notes/llm/ai-product-engineering/evals-error-analysis.html ; https://simonwillison.net/tags/hamel-husain/ ; https://www.chatprd.ai/how-i-ai/debugging-ai-writing-evals
- **[Fact]** Shankar et al., *Who Validates the Validators?* (arXiv 2404.12272, UIST 2024) propose "criteria drift": people need criteria to grade outputs, but the grading process itself changes the criteria; switching models can also cause drift. Source: https://arxiv.org/pdf/2404.12272
- **Why it matters**: S0 already has 36 eval cases and a B0/B1/B2 baseline design — this is the most valuable asset from S0. But they were written without any real traces, which by Husain's standard counts as "writing the rubric before looking at the data."
- **Applied to BriefPilot**:
  1. Before the demo, collect ≥ 20 real (anonymized) meeting transcripts or group meeting records, annotate failure modes by hand, then revise the eval set.
  2. Treat criteria drift as an expected phenomenon: version the eval set, and record the reason each time the criteria change.
  3. The PM and "engineering" (i.e., the user plus AI tools) look at the data together, rather than looking only at aggregate scores.

### 7.2 AI Will Hit the "Strategy/Analysis" Parts of PM Work First, Not "Communication/Execution"

- **[Fact]** Lenny (2024-04-09): AI has the greatest impact on "setting strategy and vision" (4/5), "setting goals" (4/5), "writing specs" (3/5), and "discovery" (3/5), and less impact on "roadmap" (2/5) and "product/design feedback" (2/5); the skills that become more valuable are product sense, communication, creativity, empathy, influence, and being the team's "glue." Source: https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management
- **[Inference]** For people moving into AI PM roles: using AI to draft a PRD is not a plus — interviewers assume you can. The plus is first-hand insight you bring back from users that AI cannot write.
### 7.3 Model choice and prompting are short-shelf-life skills; trade-off judgment is a long-shelf-life skill

- **[Fact / secondhand]** Several 2026 articles on AI PM skills argue that prompt engineering has become a baseline skill and that "which model to pick" is the skill with the shortest shelf life (measured in months). The long-term value lies in latency/cost/quality trade-offs, safety and trust UX, and human-AI interaction patterns. Sources: https://productside.com/top-ai-product-manager-skills-in-2026/ ; https://resumegeni.com/blog/ai-product-manager-resume (both are blog/SEO content; credibility is low to medium)
- **Applying this to BriefPilot**: the demo should focus on **user-reaction data** for trust-UX decisions such as the "human confirmation gate" and "refusal to answer", not on which model was used.

### 7.4 Uncertainty communication and trust design, specific to AI products

- **[Fact]** S0 ADR-002/004 already chose a human confirmation gate and server-side citation validation.
- **[Assumption H2/H3, from the S0 PRD]** "Draft + confirm" is more trustworthy than automatic execution; quality assurance drives early retention more than a complex agent does. **Still unvalidated.**
- **Applying this to BriefPilot**: v2 must validate H2/H3 with real users; otherwise they are just beliefs.

### 7.5 AI-era "rapid prototyping" changes the cost structure of discovery

- **[Inference]** Since AI coding sharply lowers prototype cost, the PM excuse "we don't have the resources to build a prototype" disappears. But this also means that "having built it" is no longer proof; "people actually use it" is. Cagan's "10-20 prototype tests per week" becomes feasible for the first time in a solo project.

---

## 8. PM Common-Mistakes Self-Check (against the current state of BriefPilot S0)

| # | Mistake | Source | Did S0 hit it? | v2 countermeasure |
|---|---|---|---|---|
| 1 | Solution-first: having a solution before finding the problem | Perri Product Kata; Su Jie | **Yes** | §1.2 sequencing rule |
| 2 | Writing the PRD without validation | Cagan four risks; Cutler #9 | **Yes** (findings.md is empty) | §3.2 evidence ID column |
| 3 | Feature-parity thinking (others have it, so we need it) | Yu Jun formula; Kano basic type | **Partly** (meeting-to-task conversion) | §3.1 Kano classification |
| 4 | Only caring about feasibility/usability, not value/viability | Cagan | **Yes** | §2.1 four-risk table |
| 5 | No metrics / success theater | Cutler #1 #3 | No (metrics are designed) | Keep, but metrics must be reset to follow the new positioning |
| 6 | Big-batch delivery | Cutler #10 | **Yes** (S1-S8 waterfall) | §4.1 weekly increments |
| 7 | No PM retrospective | Cutler #6 | Unknown (not yet carried out) | §5.2 ADR retrospective field |
| 8 | Using n=1 (oneself) to represent users | Mom Test; Yu Jun on sample size | **High risk** | §1.4 R0 + ≥5 other people |
| 9 | Writing the rubric before looking at data (AI-specific) | Husain | **Yes** (36 cases with no real traces) | §7.1 |
| 10 | Obsessing over priority scores | Cutler #7 | No | Keep avoiding |

---

## 9. Direct Inputs for the Remaining v2 Directories

- `01_market-research`: for each competitor, write "old experience / switching cost / what it structurally will not do"; use Kano to classify its features as basic / performance / delighter.
- `02_user-research`: rewrite the interview guide per the Mom Test; R0 = the user themself; target ≥ 5 interviews with other people, spanning ≥ 2 research groups (if segmented by lab); weekly contact log.
- `03_positioning`: a one-page PR-FAQ; the four-risk table; the standard answers in §6.2.
- `04_prd`: requirement items carry evidence IDs; assumptions get their own section; a Won't list.
- `05_demo-plan`: weekly increments; metrics + baseline for each feature; eval set v1 built from error analysis of real traces.

---

## Source List

**Primary / official sources**
1. Marty Cagan, *The Four Big Risks*, SVPG — https://svpg.com/four-big-risks/
2. Marty Cagan, *Product vs. Feature Teams*, SVPG — https://svpg.com/product-vs-feature-teams/
3. Marty Cagan, *Product Manager vs. Product Owner*, SVPG — https://svpg.com/product-manager-vs-product-owner/
4. Marty Cagan, *Charter Customer Programs*, SVPG — https://svpg.com/charter-customer-programs/ (search snippet only; to be verified)
5. John Cutler, *12 Signs You're Working in a Feature Factory* (2016-11-17) — https://cutle.fish/blog/12-signs-youre-working-in-a-feature-factory
6. Intercom, *RICE: Simple prioritization for product managers* — https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
7. Melissa Perri, *The Product Kata* (2015-07-22) — https://melissaperri.com/blog/2015/07/22/the-product-kata
8. Teresa Torres, *Product Discovery Basics*, Product Talk — https://www.producttalk.org/2021/08/product-discovery/
9. Lenny Rachitsky, *How AI will impact product management* (2024-04-09) — https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management
10. Lenny Rachitsky, *How to know if you're doing a good job as a product manager* (2021-06-29, paywalled, title only) — https://www.lennysnewsletter.com/p/doing-a-good-job-product-manager
11. Aman Khan (via Lenny's Newsletter), *Beyond vibe checks: A PM's complete guide to evals* — https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete
12. Hamel Husain, *Automating Error Analysis* — https://hamel.dev/notes/llm/ai-product-engineering/evals-error-analysis.html
13. Shreya Shankar et al., *Who Validates the Validators?* (arXiv 2404.12272) — https://arxiv.org/pdf/2404.12272
14. Wikipedia, *MoSCoW method* — https://en.wikipedia.org/wiki/MoSCoW_method
15. Amazon, *An insider look at Amazon's culture and processes* — https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes

**Secondary / interpretive sources**
16. ProductPlan, *Kano Model* — https://www.productplan.com/glossary/kano-model/
17. Evan Samek, book summary of Escaping the Build Trap — https://evansamek.substack.com/p/escaping-the-build-trap-by-melissa
18. Ben Nadel, book review of Escaping the Build Trap — https://www.bennadel.com/blog/3967-escaping-the-build-trap-how-effective-product-management-creates-real-value-by-melissa-perri.htm
19. Shortform, summary of *Inspired* — https://www.shortform.com/blog/inspired-product-management/
20. Shortform, summary of *The Mom Test* — https://www.shortform.com/blog/what-is-the-mom-test/
21. Everyone Is a Product Manager (人人都是产品经理): in-depth analysis of Yu Jun's product methodology — https://www.woshipm.com/pd/3402762.html
22. Everyone Is a Product Manager: User value = new experience − old experience − switching cost — https://www.woshipm.com/pd/6300702.html
23. Everyone Is a Product Manager: three points of Yu Jun's methodology (repost, original source not stated) — https://www.woshipm.com/pmd/381195.html
24. Everyone Is a Product Manager / 36Kr: Su Jie's *Everyone Is a Product Manager*, user needs vs. product needs — https://www.woshipm.com/pmd/4477209.html ; https://www.36kr.com/p/990643702555271
25. Everyone Is a Product Manager: the Y model — https://www.woshipm.com/pd/6122327.html
26. Everyone Is a Product Manager (Blues, 2014-06-09): the 18-item PM competency model — https://www.woshipm.com/pmd/88721.html
27. Aakash Gupta: Google PM levels / Meta PM levels — https://www.aakashg.com/google-product-manager/ ; https://www.news.aakashg.com/p/meta-pm-job ; additional: https://blog.tryexponent.com/product-manager-career-path/ ; https://www.teamblind.com/post/leveling-facebook-pm-ic4-vs-ic5-5opxgxmv ; https://simonwillison.net/tags/hamel-husain/ ; https://www.chatprd.ai/how-i-ai/debugging-ai-writing-evals ; https://productside.com/top-ai-product-manager-skills-in-2026/

---
## Confidence Notes for This Document

- **High confidence (verified by opening the original source directly)**: Cagan's four risks and three types of teams, Cutler's 12 symptoms, the Intercom RICE definition, Perri's Product Kata, Torres's continuous discovery, Lenny's 2024 article on AI's impact, Aman Khan's evals guide, Husain's error analysis, Shankar's criteria drift, and the origin of MoSCoW (the sources conflict on Oracle vs. BA).
- **Medium confidence (secondhand, but consistent across multiple sources)**: Perri's definition of the build trap, the three rules of The Mom Test, the Kano classification, Yu Jun's user value formula and user/transaction model, Su Jie's "user needs vs. product needs," and Amazon PR/FAQ.
- **Low confidence / needs verification**: specific items in Lenny's paid articles (not cited); the publication details and original wording of Yu Jun's book; the attribution of the Y model; the original source of ICE; the original text behind Cagan's "6 reference customers"; Google/Meta level numbering (sources conflict with each other); Tencent's capability model (unofficial, and the search snippet did not match the original text, which has been corrected); ByteDance's product-track capability model (no public material).
- **All "Applying this to BriefPilot" paragraphs in this document are [Inference] or [Assumption]**. They are suggestions for mapping public methodologies onto the project, not verified conclusions. Anything involving "research labs" is only a candidate segment and **does not constitute a presupposed conclusion**; whether it stays or goes will be decided by the interview evidence in `02_user-research`.
- The web search quota for this round has been used up, so the items above that need verification are left for the next round of follow-up checks.
