---
title: "Market Research 06: Research Completeness Review (Completeness Critic) — What Is Still Missing to Convince a Client or Interviewer"
status: draft
sources_count: 25
sources_count_method: "Number of unique URLs in the sources section (recalculated at wrap-up; original value 24)"
---

# Market Research 06: Research Completeness Review — What Is Still Missing to Convince a Client or Interviewer?

> **Reading notes**
> - This document reviews the 14 research files in the directory (`00_pm-skills/01–05`, `01_market-research/01–05`, `02_user-research/01–04`) in the role of the "most demanding reviewer," and answers one question: **if tomorrow you took this material in to answer "Feishu Minutes, Otter, and Fireflies already do this — why are you building it anyway?", where would you get stumped?**
> - Labels follow the project-wide rules: **[Fact]** has a source URL; **[Inference]** is derived from facts without direct evidence; **[Assumption]** is awaiting validation; **to be verified** means the original page could not be opened or sources contradict each other.
> - **How this round was verified, and its limits (must be stated up front)**:
>   1. The WebSearch quota for this round (200 searches shared across the whole round) was already used up before this agent started, so **not a single search could be run**. All new verification in this document was therefore done by using WebFetch to **open vendors' official pages directly** , 22 pages in total. The upside is a high evidence grade (all first-hand official pages); the downside is that it can only verify "pages at known URLs" and cannot do open-ended search. For exhaustive questions such as "does anyone on the market do X?", this document likewise cannot conclude "no one does."
>   2. The 14 files total roughly 700,000 bytes. This document **read `05_缺口综合` in full**; for the other 13 files it read the decision-relevant sections in full (conclusions, feature matrices, common weaknesses, scoring tables, uncovered items, and credibility notes) and used keyword search (`grep`) to locate and check the rest of the body, but **did not read them line by line**. Paragraph-by-paragraph fact-checking is outside the scope of this round.
>   3. Official pages are vendors' own claims. They can only prove that "the vendor claims to have it," not that "it works well."

---

## 0. Conclusions First

1. **[Fact, verified this round] At least 3 claims that were treated as "competitor gaps" have been overturned or substantially weakened by official pages, and can no longer be used in interviews or the PRD:**
   - **"No meeting tool integrates with GitHub Issues" (05 K11, M2 §7 #6) does not hold.** Fellow's official page states that it syncs with GitHub **in both directions**: a newly assigned action item from a meeting will "instantly opens an issue in a specified GitHub repository," and changes to an issue on GitHub flow back into Fellow as action items, "any addition or status change moves across systems in real time" (https://fellow.ai/integrations/github ). Granola also lists GitHub, Linear, Jira, and Asana via Zapier (https://www.granola.ai/integrations ). In addition, Circleback, Read, Otter, Fellow, and Granola all offer MCP or Claude access, so users can have an agent such as Claude Code push action items to any tool. **[Inference]** "Integration with engineering or research tools" can no longer serve as a differentiator; it is only a baseline feature.
   - **"Littlebird is personal-only" (M2 §0 item 6, 05 G17, and Option B) does not hold.** Littlebird's pricing page has a Team plan, "From $17" per seat per month, including admin controls and shared projects (https://littlebird.ai/pricing ). However, its commitment-tracking routine is still "tuned to yours," meaning it only tracks your own commitments (https://littlebird.ai/routines/promise-tracker ).
   - **"No product records completion evidence; there are only binary states" (05 K5) is weakened.** Littlebird's commitment tracking compares each commitment against what actually happened, for example "the email that went out, the document that shipped," and outputs three states: Kept, In progress, Needs a note. It also says "Vague maybes are skipped," i.e., it skips vague "maybes" (same URL). **This also means that "commitment strength tiering" (K3, which 05 originally recorded as "none seen") already exists in an early form**: it distinguishes explicit commitments from vague statements.
2. **[Fact, verified this round] One differentiator has actually been strengthened by official pages: mixed Chinese–English speech has officially acknowledged hard limits in international platform products.**
   - Google Meet "Take notes for me" has no Chinese among its supported languages, and "Multiple languages spoken in the same meeting aren't currently supported" (https://support.google.com/meet/answer/14754931 ).
   - Microsoft Teams Facilitator's AI notes "only support meetings where a single language is spoken" (https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams ).
   - Notion's speaker labeling is "available in English only" (https://www.notion.com/help/ai-meeting-notes ).
   - Chinese is not among the 16 languages Krisp lists (https://krisp.ai/pricing/ ).
   - **But Feishu states that "in discussions mixing Chinese and English, the transcript can be recognized in the original language,"** with input supporting Chinese, English, and Japanese (https://www.feishu.cn/content/article/7577317993749269689 ). **[Inference]** So this gap is not a "market void" but the intersection of "**teams that use an international toolchain such as Zoom/Teams/Meet and also speak mixed Chinese and English**," for example labs at Singapore universities. This presupposes confirming that they cannot or do not want to use Lark/Feishu, which is still to be verified.
3. **[Fact] Competitor coverage has two structural holes**:
   - **Fellow is the most direct rival for "recurring meetings + 1:1s + carrying action items across meetings + two-way GitHub sync," yet it was not included in M2's 15 in-depth analyses**; it is cited only sporadically in 05 and U2.
   - **Microsoft Teams Facilitator (Planner task-tracking preview, mobile capture of in-person discussions), ChatGPT's record mode, and the DIY alternative path of "general-purpose LLM + pasted minutes"** have not been analyzed systematically. The DIY alternative is exactly the one an interviewer is most likely to press on: "Can't I just paste the minutes into ChatGPT?"
4. **[Inference] The biggest weakness in persuasiveness of the existing material is not "not enough material" but "zero first-hand evidence."** Across the 14 files there is not a single real competitor output, not a single user interview, and not a single frequency data point. Every differentiation claim rests on "the official page doesn't say so" and "complaints from English-language tech communities." 05 itself acknowledges this (§6 Q1, Q3). For a client, "I compared 20 official websites" is far less convincing than "I ran the same group meeting recording through Feishu and Otter, and they missed 3 of 7 commitments."
5. **[Inference] After this round's verification, the most defensible differentiation space has narrowed further to two items, which need to be proven with first-hand evidence in the next round:**
   - **A. A "commitment → outcome → evidence" closed loop with research semantics**: outcomes need five-value semantics, and evidence should link to W&B runs, configs, and data versions, not just GitHub issue status. Note that Fellow's GitHub sync and Littlebird's evidence comparison each already cover half of this.
   - **B. Mixed Chinese–English speech and terminology accuracy under an international toolchain**: this needs measurable metrics such as terminology recall.
   - "Claiming by the person named" (G4) still does not appear on the Fellow page verified this round. It can be kept as a candidate, but only one vendor has been checked.

---
## 1. Verification Table for Key "Competitors Don't Do X" Claims (14 this round, all checked by opening the official pages)

> Verdicts: **Overturned** = the official page explicitly says the capability exists; **Weakened** = a close capability exists or coverage is partial; **Holds** = the official page explicitly says it is absent or limited; **To be verified** = the page doesn't mention it, so no conclusion can be drawn.

| # | Original claim (source) | Official wording verified this round | Verdict | Impact on differentiation |
|---|---|---|---|---|
| V1 | No meeting tool has GitHub Issues integration (05 K11; M2 §7 #6; G20) | Fellow: action items "instantly opens an issue in a specified GitHub repository", with two-way status sync (https://fellow.ai/integrations/github ); Granola: GitHub, Linear, Jira, Asana via Zapier (https://www.granola.ai/integrations ) | **Overturned** | Remove the "not covered" scores for K11 and G20; Option C can no longer claim "meeting tools don't connect to engineering tools" |
| V2 | Action-item integrations are CRM-centric, with dev tools missing (M2 §7 #6) | Circleback lists Linear, Claude Code, Cursor, Codex, MCP server, CLI (https://circleback.ai/integrations ); Read lists Jira, Linear, MCP, Claude, ChatGPT (https://www.read.ai/integrations ); Otter states "Connect Otter.ai meeting transcripts and action items to Claude via MCP" (https://otter.ai/integrations ) | **Overturned** | Once everything is exposed via MCP, "integration" itself is no longer a moat [Inference] |
| V3 | Littlebird is a personal tool with no team layer (M2 §0-6; 05 G17; Option B positioning line) | The Team plan is "From $17" per seat and includes shared projects and admin controls; the $15/month student price is confirmed (https://littlebird.ai/pricing ) | **Overturned (team billing tier) / Holds (commitment tracking is still a personal view)** | The positioning line for Option B and G17 should change to a team-shared **commitment ledger**, not a "team edition" |
| V4 | Task completion is only a binary state, with no evidence (05 K5) | Littlebird's promise tracker compares against "the email that went out, the document that shipped", with three states: Kept, In progress, Needs a note (https://littlebird.ai/routines/promise-tracker ) | **Weakened** | G5's uniqueness shrinks to "five-value research outcomes + experiment-artifact evidence"; the evidence source shifts from email and documents to W&B and Git |
| V5 | No product distinguishes commitment strength (05 K3, "none seen") | Littlebird: "Vague maybes are skipped unless you ask for them" (same page) | **Weakened** | G3 can only claim "strength tiers + evaluability", not "nobody does it" |
| V6 | Fellow only tracks open/closed (05 K5, verified before this round) | The page only shows "mark them complete" and "tracks whether items are still open"; it supports assignment during or after the meeting, reassignment, and multiple owners; **the page does not mention the assignee confirming or accepting** (https://fellow.ai/features/action-items ) | **Holds (as far as this page goes)** | G4 "owner self-claims" is still not seen on Fellow's page; but the two-way GitHub sync means engineering teams' "status" can already flow back automatically |
| V7 | No vendor publishes action-item extraction accuracy (05 K1; M1, M2) | Fellow only writes "human-level accuracy", with no figures (same URL as V6); Fabric gives no metrics at all (https://fabric.so/teams/academic-labs ); in academia, Golia & Kalita 2023 used AMI for action-item-driven summarization and report a BERTScore of 64.98, **not action-item accuracy** (https://arxiv.org/abs/2312.17581 ) | **Not overturned, but not exhaustive** (search was not possible this round) | K1 continues to hold, but academic benchmarks (AMI action-item annotations, meeting summarization datasets) still need to be checked, otherwise "I'm building the first public evaluation" may be refuted by academia |
| V8 | Notion speaker labeling supports English only and does not work offline (M1, M2) | "Speaker labeling is currently available in English only"; "AI Meeting Notes is not currently supported while offline"; transcription supports 16 languages including Chinese (https://www.notion.com/help/ai-meeting-notes ) | **Holds** | Supports Option D |
| V9 | Krisp on-device transcription supports English only (M2 §7 #4, #7; 05 K8) | The pricing page only says on-device belongs to **Enterprise** and **does not say "English only"**; **Chinese is not among** the 16 supported languages (https://krisp.ai/pricing/ ) | **Original wording to be verified; the stronger fact is that Krisp does not support Chinese at all** | Rewrite how K8 and K12 describe Krisp |
| V10 | Zoom AI Companion 3.0 claims to "track cross-meeting projects" (M2 §3.8; 05 Q15) | The official AI assistant page **does not** contain this sentence; it has "ZoomMate project agent to track progress, share updates, and manage tasks", My Notes covering "in-person", and Jira integration (https://www.zoom.com/en/products/ai-assistant/ ) | **To be verified (source of the original sentence) / Direction holds** | Zoom is moving toward a "project-level agent"; the window for G5 and G11 is narrowing [Inference] |
| V11 | Teams only "suggests" action items and does not track them (M2 matrix) | **New competitor Facilitator**: Planner task-tracking integration (public preview), "Mobile capture of ad-hoc discussions and action items"; but it does not support 1:1 chats or external meetings, and notes support only a single language (https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams ) | **Weakened (tracking) / Holds (cross-organization, multilingual)** | The M2 matrix needs Facilitator added; the "cross-organization + Chinese/English" limits are confirmed by official documentation |
| V12 | Gemini in Meet produces only one Doc and has limited language support (M2) | "Next steps" lists "actionable items and assigned tasks"; in-person meetings are supported; the language list **has no Chinese**; "Multiple languages spoken in the same meeting aren't currently supported" (https://support.google.com/meet/answer/14754931 ) | **Holds** | Supports Option D |
| V13 | Feishu has no cross-meeting tracking and unclear terminology capability (M1 matrix, whole row ○, §9 #6; 05 K12 "no product builds a glossary chain") | "Meeting Express" (会议速递) aggregates action items based on "the smart-minutes content of the most recent week"; "enterprise information recognition" can identify "uncommon characters in colleagues' names and project names"; mixed Chinese-English speech is recognized in the original language; **deadlines are not mentioned on the page** (https://www.feishu.cn/content/article/7577317993749269689 ) | **Weakened** | K12 should be changed to "has enterprise-level entity recognition, but no project-level glossary + public recall rate"; the M1 matrix entry "terminology / hot words ?" can become "◐ (enterprise information recognition)" |
| V14 | Granola processes in the cloud, trains by default, and has been sued (M2, U4, 05 G7) | "Transcription and AI summarization use cloud processing"; "Granola doesn't store the audio"; individual users participate in training by default and can opt out, while the enterprise edition is off by default (https://www.granola.ai/security ); the lawsuit was filed on 2026-07-30, case no. 3:26-cv-07926-EMC, alleging hidden-by-default recording and training-by-default (https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ ) | **Holds** | The factual basis for G7 and G19 is sound |

**Supplementary checks (not "doesn't do X" claims)**:
- The HN quotes "plausibly mishear the parts that matter most" (bad_username) and "nobody will ever read those notes" (smartmic) exist in the original (https://news.ycombinator.com/item?id=48823024 ).
- Fabric's marketing page confirms: it extracts action items from supervision-meeting recordings and creates tasks, a decision log "within 24 hours", a PI weekly digest, and "never used to train"; **no customer case studies and no academic-lab pricing** (https://fabric.so/teams/academic-labs ).
- The Tongyi Tingwu help center home page only confirms "action item" extraction and **does not mention hot words or cross-file Q&A** (https://help.aliyun.com/zh/tingwu/ ). M1's "multi-file Q&A (2024)" cannot be confirmed on this page; the specific documentation page remains to be verified.
- The UW CS PhD handbook page now returns a 301 redirect to an internal domain (internal.cs.washington.edu) and could not be opened this round. U1 §0 item 2 cites it as a "verbatim quote [Fact]" and **should be downgraded to "search snippet, to be verified"** (U3 is already labeled this way).

**Overall conclusion of this round's verification [Inference]**: Of the 14 items, 3 are overturned, 5 weakened, 4 hold, and 2 are to be verified. **The directional pattern is: every gap of the "does the feature exist" kind is being filled quickly (integrations, tracking, evidence comparison); every gap of the "constraint" kind (multilingual, cross-organization, local processing, consent) is instead confirmed as a limitation by official documentation.** This matches 05's judgment that "horizontal features are easy to copy, while constraints and niche semantics are copied slowly", but is more pessimistic than 05: the uniqueness of G5 (ranked in tier 4 in 05) and G20 (tier 9) both need to be revised downward.

---
## 2. Key Claims Used as Conclusions Despite Weak Sourcing

| # | Claim (file) | Current evidence | Problem | Severity |
|---|---|---|---|---|
| W1 | "Advisors can't remember what they said last time" is institutionally recognized (U1 §0-2, U3 §0-3, 05 G6) | UW CS handbook (search snippet; now behind a login); MIT Cahoy advising policy (original text read) | U1 labels it "verbatim quote [Fact]" while U3 labels it "to be verified": **the same evidence carries two different labels**. It is also the core basis for Option B | High |
| W2 | DingTalk assigns action items to the meeting organizer by default (M1 §4.2, 05 K2/G3) | One hands-on test on Everyone Is a Product Manager (人人都是产品经理), 2025-09 | Single source and possibly already fixed, yet it is the **only** hands-on evidence for the "big vendors silently fill in the gaps" argument | High |
| W3 | About 1/3 of AI action items are left untouched three weeks later (M4 §0-2, 05 G4) | Personal estimate by Lilach Bullock | Already marked "not a statistic" in the file, but still appears as an evidence entry in 05 G4; **must not go into the interview script** | Medium |
| W4 | Mixed Chinese-English speech and terminology are "high-frequency complaints" (M1 §9 #6) | One sentence from a DingTalk hands-on test, one from Sspai (少数派), one Juejin (掘金) article; **zero original posts from Zhihu or Xiaohongshu** (M4 category J, U4 self-assessment) | No frequency data supports "high-frequency"; this round's verification of official limitations (V8, V9, V11, V12) only proves "capability is limited", not "users are in pain" | High (make-or-break for Option D) |
| W5 | Student-side pain point ("forgetting things the advisor assigned verbally") | Notion templates selling well, one GradCafe post, Reddit attempts all failed (M4 §1) | M3 §8 itself says "student-side pain has only indirect evidence", yet Options B and C both take students as the primary user | High |
| W6 | Nature 2025: about half of PhD students meet their advisor for less than 1 hour per week | Secondhand PDF repost; U1 notes "the figures point in conflicting directions" | **M3 §8 labels it [Fact] and uses it for frequency scoring**, while U1 labels it "to be verified" | Medium |
| W7 | Teams recap action items are "suggestions, not authoritative assignments" (M4 C4, 05 G4) | Search snippet | A key comparison point for G4; this round's verification found that Facilitator already has Planner tracking, so the original claim may be outdated | Medium |
| W8 | UK supervision record systems work as "student writes, advisor confirms" (U3 §6.2, 05 G6) | Haplo page now redirects, LJMU PDF returns 404, content comes from search snippets | The main basis for Option B's "embed in existing institutional processes" is that **neither source can be opened** | Medium-high |
| W9 | Harvard bans AI meeting assistants (U1 §0-4, §6) | Search snippet; original page returns 403 | Used as the lead example of an "institutional restriction"; recommend leading with the UCSD and Mississippi State pages instead, which can be opened | Low-medium |
| W10 | "A research commitment has a five-valued outcome" (U3 §0-1, 05 G5) | Derived from the data model (U3 self-assessment: [Inference]) | The "opportunity description" in 05 G5 reads like a fact; Option C's magic moment depends on it | High |
| W11 | A 500-person survey: 34.7% are "always asked for consent" (U4, 05 G7) | Republished by Stacker; commissioned by a law firm | Interested party already flagged, but still used as one of the main pieces of evidence that "consent is a strong problem" | Low |
| W12 | Scoring in each file (E×P×U×D in 05, six-dimension weighting in U2, seven dimensions in M3) | Researcher's subjective scoring | The three scoring systems are **mutually incompatible**; U2's 3.70 and 05's E=2 give opposite signals for the same segment (see §5 C6) | Medium |

**[Inference] Pattern**: The weak evidence is concentrated in **the pain felt by students and advisors** and **the pain felt by Chinese-language users**. Those two categories are exactly the foundation of Options B, C, and D, the ones v2 most wants to bet on. Evidence on the competitor side is comparatively solid (mostly official pages). In other words, **what we can currently demonstrate with confidence is "what others have built", not "that my users are really in pain"**.

---

## 3. Competitor Coverage Gaps: Missed or Superficially Analyzed Targets

| Target | Why it must be added | Current status | Suggested action |
|---|---|---|---|
| **Fellow** | Recurring meetings, 1:1s, carrying action items across meetings, two-way GitHub sync, MCP; **the most direct rival to Options B and C** | Only cited in 05 and U2; M2 has no standalone analysis | Add to M2 §3 and analyze with the same template; sign up for a trial and test the 1:1 template and GitHub sync hands-on |
| **Microsoft Teams Facilitator** | Microsoft's official "meeting agent", with Planner tracking and mobile in-person capture | Does not appear at all | Add to the matrix, recording in particular the two limitations "single language" and "no support for external meetings" (favorable for D) |
| **ChatGPT record mode / Claude or ChatGPT + pasted minutes** | Interviewers are most likely to say "I can just use ChatGPT". This is the **biggest substitute**, and under the Dunford framework it should be listed as a "competitive alternative" | ChatGPT is only mentioned sporadically (e.g., S4); its help page returned 403 this round | Run a hands-on test: paste the same group meeting minutes into ChatGPT or Claude and record how it handles commitments, owners, and outcome semantics, as a control group |
| **MCP ecosystem** (Otter, Read, Circleback, Granola, and Fellow have all integrated it) | Users can assemble part of BriefPilot themselves with "meeting tool + Claude Code + GitHub MCP" | MCP is mentioned in only a few files and is not analyzed as a competing form | Answer head-on in the positioning document: "Why not Granola MCP + Claude assembled by the user?" |
| **Lark international edition** (available in Singapore) | What users in Singapore can actually use is Lark, not Feishu; it is the strongest rival in mixed Chinese-English scenarios | Listed as to-do in M1 §10 item 4, not done | Verify Lark Minutes' availability, languages, and pricing in Singapore |
| **Recording hardware such as Plaud** | Another way to solve in-person group meetings | Mentioned in U2 and U4, not in the matrix | Add a row |
| tactiq, Bluedot, MeetGeek, Jamie, Sembly | Long tail of small and mid-size vendors that may already offer "push by person" or "local" features | Search returned 0 or sporadic results | Low priority; at least skim the homepage of each official site |
| Doubao (豆包), Kimi recording minutes | Free alternatives for students in China | To-do in M1 §10 item 4 | Follow up on verification |
| Academic benchmarks (AMI action-item annotations, meeting summarization datasets) | "I'm building the first public evaluation" would be rebutted by interviewers with an NLP background | Not researched | Add a one-page literature review: existing datasets, metrics, and where the gaps are |

---
## 4. Missing User Segments and Scenarios

U2 scanned 14 segments. The coverage is not narrow, but **several segments most relevant to the project owner's situation were not evaluated separately**:

| Missing segment | Why it deserves evaluation ([Inference]) | Relationship to existing options |
|---|---|---|
| **Joint university–industry labs at the target university** (corporate lab, where an academic team reports regularly to a corporate funder) | It combines two structures: "research semantics" and "client–vendor confirmation". It has contractual milestones and deliverables (a strength of Option E) as well as experiment commitments (a strength of Option C), **and it has a paying party (the corporate funder)**. This could resolve the fatal weakness of Option C, low willingness to pay | The intersection of C and E, and possibly a better wedge |
| **Thesis committee and qualifying exam meetings** (thesis committee, TAC, qualifying exam) | Low frequency (every six months or every year), but each commitment is formally binding and usually needs to be recorded in writing and archived | The high-risk, high-value version of Option B |
| **Undergraduate final-year project (FYP) supervisor meetings** | The target university has a large number of FYPs; each supervisor handles many students, students turn over quickly, and record-keeping requirements are explicit | The scaled-up version of Option B, with high reachability |
| **Cross-institution research consortia and grant projects** (joint multi-university projects, grant milestone reports) | M2 §8 mentions "cross-institution" but does not evaluate it as a segment; cross-organization limitations (Teams and Facilitator do not support external meetings) hurt most here | The landing scenario for G18 |
| **Corporate ML/AI R&D teams** (non-hardware) | The toolchain is identical to Option C's (W&B, Git), but these teams have the ability to pay; U2 only evaluated hardware/robotics | A commercial expansion path for Option C, closer than hardware |
| **Lab managers and research administrators** | The person who actually "keeps an eye on progress" in a lab may not be the PI | Affects who the buyer is and who the user is |
| **Mixed-language speech (Singapore English/Singlish, Malay, Tamil)** | U4 only studied Chinese and English; code-mixing in the Singapore setting is more complex | Scoping for Option D |
| **Journal clubs and reading groups** | High-frequency lab meetings, but the output is "knowledge" rather than "commitments", so they can test the knowledge Q&A line | A scenario for the S0 knowledge Q&A line |

**Another gap is the lack of a control group.** S5 §2.5 and 05 §5 both require a non-lab control group of 3–4 people, but no file specifies who the control group is. I recommend using "corporate ML teams" as the control group directly: if their pain points are the same as the labs', the differentiation lies in "R&D semantics" rather than in "academia".

---

## 5. Coverage Gaps in PM Skill Topics

The user asked for "everything a product manager should pay attention to, plus all the skills needed to discover a good product". I counted keyword occurrences across `00_pm-skills/01–05` (per file), and the following topics have zero or near-zero coverage:

| Missing topic | Keyword hits (S1/S2/S3/S4/S5) | Why this project needs it |
|---|---|---|
| **Cold start and network effects** | "cold start" 0/0/0/0/0; "network effects" appears only once, in S3 | G4 (owner claiming), G6 (supervisor confirmation), and G17 (group-wide board) **all require multiple people to be in the system at the same time**. 05 already lists cold start as an objection, but the methodology has no framework for addressing it (for example, single-player mode, or building single-user value first) |
| **Growth, activation, retention** (AARRR, PLG, Aha moment) | PLG 0; activation 0; Retention 0; retention at most 1 time | Granola's breakout was essentially PLG (individuals adopt first, then it spreads to the team); interviewers will ask "how do you measure week-one retention" |
| **Stakeholder management** | "stakeholder" (Chinese term) 0; stakeholder 0 | The decision chain in research settings is "students feel the pain, the PI pays, university IT approves" (U1 §0, item 6), which is exactly where a stakeholder map is useful |
| **Data privacy regulation and research ethics** (Singapore PDPA, GDPR, IRB) | PDPA and GDPR are both 0 across the 00 series; IRB appears only in M2, M3, and U2 | The target university is in Singapore, so the PDPA is a hard constraint; when recordings involve human-subjects research, IRB review is required |
| **Product teardown and product taste** (teardown, product critique, the criteria for judging "what makes a good product") | teardown 0; product sense 0 | "How to discover a good product" is not only about discovering needs; it also includes **judging what existing products do well** (for example, why Granola is pleasant to use). S2 covers discovering needs but not how to evaluate a product |
| **Pricing strategy and willingness-to-pay measurement** (Van Westendorp, per-seat or per-group pricing) | Pricing has hits in S3 and S5, but there is no method for measuring willingness to pay | The biggest weakness of the research options is payment, and 05 §6 Q13 cannot be answered with the existing methodology |
| **Data analysis and experimentation** (A/B testing, SQL, metric decomposition) | A/B appears only once, in S4; SQL 0 | A must-have in interviews for people transitioning into PM |
| **PM interview case preparation** (product sense, execution, metrics question types) | Scattered hits for "case", nothing systematic | The project needs to be tellable as an answer to a product sense question |
| **Launch and GTM** (launch plan, channels, cold-start list) | launch appears only twice, in S5; GTM 1–2 times | Once positioning is done, you need to answer "where do the first 10 users come from" |
| **Build vs. buy and platform dependency** | 0 | After the MCP move, "build it ourselves vs. assemble it on Granola or Fellow via MCP" is a real decision |
| Accessibility | 0 | Low priority, but meeting transcription is a natural scenario for hearing-impaired users and could be a bonus point |

**Topics with good coverage** (no need to add): Mom Test, Kano, OST (opportunity solution tree), JTBD, Dunford positioning, 7 Powers, AI evaluation (evals), PRD templates, demo scripts, hypothesis-validation experiments.

---
## 6. Contradictions Between Files (those already handled in 05 §7 are not repeated)

| # | Contradiction | A says | B says | Suggested handling |
|---|---|---|---|---|
| C1 | Evidence grade of the UW CS handbook | U1 §0 item 2: verbatim quote [Fact] | U3 §6: search summary, to be verified; when opened this round it redirected to an internal domain requiring login | Downgrade uniformly to "to be verified" |
| C2 | Manual student–advisor workflow has "no tool support" | U3 §0 item 3: it is institutionalized, "just not yet supported by tools" | U3 §6.2 itself lists supervision record systems such as Haplo PhD Manager and LJMU eDoc | Change to "administrative record systems exist, but they are not connected to meeting content" |
| C3 | Whether cross-meeting commitment continuity is a gap | U1 §0 item 3: "what is truly unmet is cross-meeting commitment continuity" | 05 K6, this round's V6: Fellow and Littlebird already do it | The U1 conclusion must be corrected per 05, otherwise the PRD will cite U1 incorrectly |
| C4 | Littlebird's positioning | M2 §0 item 6, 05 G17: personal tool | This round's V3: it has a Team plan | Defer to the official pricing page |
| C5 | Evidence grade of the Nature 2025 data | M3 §8: [Fact], used for frequency scoring | U1 §1, §16: secondhand, numbers conflict in direction | Downgrade; change M3's frequency score to "to be verified" |
| C6 | Strength of the client/vendor segment (甲乙方) | U2 §0: Top 1 (3.70 points, robust under all three weightings) | 05 option E: weakest evidence (E=2), low dogfooding | The two use different scoring dimensions (U2 has no "evidence strength" dimension); 05 should state this handling in §7, which it currently does not |
| C7 | How cross-meeting commitment tracking is labeled within M1 | M1 §0 item 3: [Inference] "none found in search" | M1 §9 #4: [Fact] "entire row ○" | Unify as "[Fact: not found within the search scope]" and add the weakening evidence from V13's "meeting digest" (会议速递) |
| C8 | Krisp's language capability | M2, 05 K8/K12: "English on-device transcription" | This round's V9: the page does not say on-device is English-only, but Chinese is not among the supported languages at all | Rewrite |
| C9 | GitHub integration | M2 §7 #6, 05 K11: "none of the pages fetched this round lists GitHub" | This round's V1: Fellow and Granola both list it | Defer to this round; M2 did not fetch the integration pages for Fellow and Granola at the time |
| C10 | "No product does the glossary chain" | 05 K12 | M1 §10 item 3 itself says "Feishu, Tingwu, and iFlytek may all have hot-word support, but this was not verified"; this round's V13 shows Feishu has enterprise-information recognition | 05 should not write "unverified" as "no product does this" |
| C11 | README reading order and status | README says "first round generating"; step 1 of the reading order points to `03_positioning/` | `03_positioning/`, `04_prd/`, and `05_demo-plan/` are empty directories | Update the README status |

---

## 7. File Format Checks

| Check | Result |
|---|---|
| YAML frontmatter (title, date, author, status, sources_count) | **All 14 files have it.** 05 has one extra metadata field that the other files lack, so fields are inconsistent (low priority) |
| Source list | All 14 have one |
| Credibility notes | All 14 have them; U2 places the "credibility notes" before the "source list", an order different from the other files (low priority) |
| Length | The shortest, S1, is about 38,000 bytes (318 lines); the longest, 05, is about 69,000 bytes; **no file is too short** |
| sources_count vs. unique URLs in the body | Roughly consistent, or the body has more (e.g., S1 states 27, the body has 38 unique URLs). 05 states 72, but its source list is largely "cited from earlier files", and **only 1 was newly verified this round**, so readers can easily mistake all 72 for new evidence |
| Evidence label consistency | **Problem**: composite labels such as "[Summary · to be verified]" appear. U3 has 40 instances of "search summary", U1 35, M4 37, M1 19. A "search summary" is essentially secondhand evidence, yet it is tagged [Fact]. Recommend adding a separate **[Summary]** label that may not be paired with [Fact] |
| Access dates | M2 consistently writes "accessed at the time of writing"; the other files give no access date for individual URLs. Official pages change quickly (this round found Littlebird and Fellow inconsistent with earlier records), so **we recommend writing an access date for every official-page source** |
| Sources that would not open | Haplo (redirect), LJMU PDF (404), Harvard (403), UW CS (login required), LabRAT (connection refused), Fabric pricing (blank), ChatGPT help page (403 this round). Claims supported by these sources should be uniformly marked "to be verified" in the body |
| README | Status is out of date (see C11) |

---

## 8. Overall Assessment: Can This Persuade a Client or Interviewer?

**What can be stated clearly and defended now:**
1. Which things are **not** differentiators: meeting-to-action-item conversion, citations, human confirmation, no bot, no training on user data, binary cross-meeting tracking, engineering-tool integration, and a basic version of commitment-evidence comparison (the last three newly added this round).
2. The limits of international platform products on **mixed-language meetings and cross-organization meetings**. This is now backed by official documentation from Microsoft, Google, and Notion, and is the hardest-evidenced differentiation point this round.
3. No vendor publishes action-item quality metrics. This is "not found within the search scope", but Fellow stating only "human-level accuracy" also corroborates it indirectly.

**What would stump us now:**
1. "How many people have you interviewed? How many commitments does your user miss per week?" The answer is 0 people and no data.
2. "Fellow already has a 1:1 template, cross-meeting carry-over, and GitHub sync. How do you differ from it?" The answer is that Fellow has not yet been tested hands-on.
3. "If I paste the minutes into ChatGPT or Claude, can't it also produce a commitment list?" The answer is that no comparison experiment has been done.
4. "Feishu or Lark already supports mixed Chinese-English. Why wouldn't a Singapore lab use it?" The answer is that Lark's availability in Singapore and the lab's actual choices have not been verified.
5. "The lab can't afford to pay. What is your business story?" The answer is only "portfolio value", with no paying party. The joint university–industry lab proposed in §4 may be a way out, but it has not been researched.

**[Inference] In one sentence**: the current material is enough to prove "I know who is doing what in this red ocean", but not yet enough to prove "I have found a point that is real, painful for someone, and not done by others". Only after completing the P0 work in §9 are we qualified to move into the positioning and PRD stage.

---
## 9. Follow-up Work Required in the Next Round

### P0 (cannot proceed to 03_positioning without these)
1. **Head-to-head experiment on real competitor output**: Take 3–5 synthetic group meetings (mixed Chinese and English, soft commitments, including advisor commitments) and run each through Lark/Feishu Minutes, Otter, and Fellow, plus "ChatGPT/Claude + pasted meeting notes" as a baseline. Manually label 30–100 commitments, then measure the miss rate, wrong-owner rate, fabrication rate, and strength-misjudgment rate. This is the only way to turn "they don't do it well" into numbers (corresponds to 05 Q1).
2. **In-depth Fellow analysis and trial**: Add it to M2, and test in practice the 1-on-1 template, carry-over across meetings, multiple owners, two-way GitHub sync, and whether there is any "confirmation by the assignee".
3. **First-hand user evidence**: 6–8 Mom Test interviews (at least 2 PhD students and 2 PIs each from this group and adjacent groups), plus a comparison group of 3–4 people from enterprise ML teams. Also start a 2-week diary study to measure "commitment frequency × 48-hour miss rate".
4. **Correct earlier files using this round's verification results**: K3, K5, K8, K11, K12, G5, G17, G20 and the differentiation wording of options B and C in 05; the matrix in M2 (Granola integrations, Littlebird team edition, Facilitator); items 2 and 3 in U1 §0.

### P1 (needed for the positioning phase)
5. **Availability and capabilities of Lark international edition in Singapore**, and the target university's official IT policy on AI meeting tools and third-party cloud services (corresponds to 05 Q8).
6. **Verification of competitors' "after the commitment" details**: whether the Littlebird team plan shares commitments, the actual capabilities of the Zoom ZoomMate project agent, Teams Facilitator's Planner tracking, and the documentation pages for Tongyi Tingwu hotwords and multi-file Q&A.
7. **Academic benchmark survey**: existing datasets and metrics for meeting action-item extraction, so that the claim of a "first public evaluation" cannot be refuted.
8. **New segment assessment**: Score the target university's university–industry joint labs, enterprise ML teams, and FYP advisor meetings using the U2 framework.
9. **Supplementary Chinese UGC collection**: The project owner manually excerpts, in a browser, 10–20 complaints from Xiaohongshu, Zhihu, and Bilibili about Feishu Minutes or Tingwu handling mixed Chinese–English speech and terminology recognition, and also adds the original Reddit r/PhD posts (corresponds to 05 Q6, Q7).

### P2 (methodology and format)
10. **Add PM skills topics**: cold start and network effects, PLG and retention, stakeholder maps, PDPA and IRB, product teardown methods, willingness-to-pay measurement, PM interview case frameworks, build vs buy. These can be merged into a single `00_pm-skills/06`.
11. **Unify evidence labels**: Add a [Summary] label, add an access date to every official source, and mark any source that cannot be opened uniformly as "to be verified".
12. **Update the README** with the current status and reading order.

---

## Source List

**Official or original pages opened directly in this round (WebFetch)**
1. Fellow Action Items — https://fellow.ai/features/action-items
2. Fellow Integrations — https://fellow.ai/integrations
3. Fellow × GitHub — https://fellow.ai/integrations/github
4. Granola Integrations — https://www.granola.ai/integrations
5. Granola Security — https://www.granola.ai/security
6. Littlebird Pricing — https://littlebird.ai/pricing
7. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
8. Fabric for Academic Labs — https://fabric.so/teams/academic-labs
9. Notion AI Meeting Notes help page — https://www.notion.com/help/ai-meeting-notes
10. Krisp Pricing — https://krisp.ai/pricing/
11. Fireflies Integrations — https://fireflies.ai/integrations
12. Read AI Integrations — https://www.read.ai/integrations
13. Otter Integrations — https://otter.ai/integrations
14. Circleback Integrations — https://circleback.ai/integrations
15. tl;dv Integrations — https://tldv.io/integrations/
16. Microsoft Learn: Facilitator in Teams — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
17. Zoom AI Companion / ZoomMate product page — https://www.zoom.com/en/products/ai-assistant/
18. Google Meet "Take notes for me" help page — https://support.google.com/meet/answer/14754931
19. Feishu Intelligent Meeting Minutes — https://www.feishu.cn/content/article/7577317993749269689
20. Alibaba Cloud Tongyi Tingwu Help Center — https://help.aliyun.com/zh/tingwu/
21. Golia & Kalita 2023, Action-Item-Driven Summarization of Long Meeting Transcripts — https://arxiv.org/abs/2312.17581
22. PPC Land: coverage of the Granola class action — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
23. Hacker News discussion thread — https://news.ycombinator.com/item?id=48823024

**Attempted in this round but could not be opened**
24. UW CS PhD Advising Guide (301 redirect to an internal domain requiring login) — https://www.cs.washington.edu/academics/phd/handbook/advising-guide/building-a-relationship
- ChatGPT Record help page (HTTP 403) — https://help.openai.com/en/articles/11487532-chatgpt-record

**Scope of review**: the 14 files in this directory (sources cited within the files are not repeated here).

---
## Confidence Notes for This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| Littlebird's GitHub integration, team plan, evidence matching, and vague-commitment filtering already exist | **High** | All taken verbatim from official pages opened directly in this round; but they only prove "claimed to exist", with no hands-on testing of effectiveness |
| Multilingual limitations of Google, Microsoft, Notion, and Krisp | **High** | Verbatim from official help documentation; documentation may be updated at any time, so citations must include the access date |
| The tally for the 14 items verified in this round: "3 overturned, 5 weakened, 4 upheld, 2 pending verification" | **Medium-high** | See §1 for the grading criteria; the boundary between "weakened" and "overturned" involves researcher judgment |
| "No vendor publishes action-item accuracy" still holds | **Medium** | Search was unavailable this round, so no exhaustive check was possible |
| Weak-evidence list (§2) and contradictions between files (§6) | **Medium-high** | Based on locating and cross-checking the conclusion sections and keywords of each file; **I did not read all 14 files line by line**, so further contradictions may remain |
| Value judgments on the missed segments (§4) | **Assumption** | All are [Inference] with no external evidence; they only indicate "worth evaluating" |
| PM skill gaps (§5) | **Medium** | Keyword counting misses content written with synonyms; a few topics may have been covered under other wording |
| Overall verdict: "the existing material is not enough to persuade the client" | **Medium-high** | Based on two objectively checkable facts: "zero interviews, zero hands-on competitor testing" |

**Most important reminder**: This round's verification shows that a "feature gap" has a very short shelf life. M2 and 05 were written on the same day, yet their records of Littlebird and the GitHub integration already disagree with the official pages (or those pages simply weren't captured at the time). So in the next round, any claim that "competitors don't do X" must come with **the official page opened that same day and its access date**, and differentiation should be built first on constraints (multilingual, cross-organization, local, consent) and on segment semantics (research outcomes and evidence), rather than on "some feature nobody else has shipped yet".
