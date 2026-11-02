---
title: "User Research 01: Segmenting \"Academic Research Labs\" — In-Depth Personas, Scenarios, JTBD, and Pain-Point Ranking"
status: draft (revised in place, Round 2, per review 06)
sources_count: 61
sources_count_method: number of unique URLs in the sources section (recalculated at wrap-up; original value 50)
---

# User Research 01: Academic Research Labs (PI / PhD Student / Postdoc / Master's Student / RA) as the Target Segment

> **Reading notes**
> - Labeling rules: **[Fact]** has a source that can be checked; **[Inference]** is derived from several facts but has no direct evidence; **[Assumption]** awaits interviews or experiments to verify.
> - **(Added in Round 2)** **[Summary]** = only the search-engine snippet was seen; the original page was not opened. Compound labels in the original text such as "[Fact] (search snippet)" have been unified as [Summary] and are no longer listed alongside [Fact]. Claims that were overturned are kept as ~~strikethrough~~; see "Revision Log (Round 2)" at the end for the changes.
> - This document focuses on people and scenarios: who holds which meetings, what happens afterward, where it hurts, and why existing tools don't solve it. Competitor feature details are already written up in `01_market-research/03_competitors_research_lab_tools.md` (hereafter "Competitors 03"); they are cited here only when needed and not repeated.
> - **Hard limits of this round of research (must be stated up front)**:
>   1. **Reddit (r/PhD, r/GradSchool) could not be fetched.** The search tool returned "domain not accessible" for reddit.com, so this document contains no quotes from original Reddit posts. Student voices instead come from the GradCafe forum, official university guides, academic blogs, Chinese media, and paraphrases in papers.
>   2. **Original Zhihu posts could not be fetched** (403). Chinese student voices can only come from search-result titles, Editage's paraphrases of Zhihu content, the publicly available rules and regulations of research groups at China Agricultural University and Nankai University, and one paper from *Research on Graduate Education*.
>   3. **The search quota ran out before writing**, so three items were not covered: "original Twitter/X posts from academia," "historical HN Show HN posts," and "papers on using LLMs to summarize research meetings." See §14.
>   4. All personas are **synthetic characters** assembled from public evidence, not interview results.

---

## 0. Conclusions First (Answer First, Then Explain Why)

1. **[Fact] Meetings in research labs are frequent, mandatory, and institutionally constrained.** In small research groups in China, it is common to have "one group meeting a week, about 2–3 hours each, with each person presenting about once a month" (a 2022 paper). Some labs require a one-page weekly report to be sent to a shared mailbox "before 8 a.m. every Monday," and two consecutive missed submissions earn a "notice of criticism on the bulletin board" (rules of the functional dairy lab at China Agricultural University). Several UK universities require PhD students to **keep a written record of every supervision meeting** (Newcastle, Liverpool, Sheffield). So in this segment, "meet → record → report at the next meeting" is not an optional habit but a workflow required by institutional rules.
2. ~~**[Fact]**~~ **[Summary · to be verified] + [Fact]** **"What did my advisor say last time?" is a problem officially acknowledged, and the responsibility is explicitly pushed onto the student.** ~~Verbatim from the UW CS PhD handbook:~~ The UW CS PhD handbook (**search snippet only**): "If your advisor can't remember what was discussed at the last meeting, don't be upset." It also asks students to keep their own notes and send a written summary after meetings. (Correction: this is not a "verbatim quote [Fact]." The original page redirects with a 301 to internal.cs.washington.edu, which requires login; review 06 and this round's second attempt both failed to open it. U3 §6.1 also marks it "search snippet, to be verified," so both files are now unified as [Summary · to be verified]; see 06 W1, C1. Before citing externally, replace it with a source that can be opened, for example MIT's advising policy, which has been read in full: it requires students to send notes and action items to everyone after a meeting and to review them item by item at the next meeting, https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf .) There is also **[Fact]** evidence from the PI side: the author of Prograds is a UBC professor, and he states his motivation as "advisors often don't know what stage their students have reached."
3. **[Inference]** ~~**What is truly unmet is not "transcription" or "summarization" but "commitment continuity across meetings."** Specifically, three things: who promised what in this meeting (including the advisor's promises to the student); whether what was promised last time got done; and, at the start of the next 1:1, automatically presenting "key points from last time + unclosed items." General-purpose meeting tools take a single meeting as the unit,~~ (Correction: a **binary version** of "cross-meeting commitment continuity" **has already been built by others**, so it can no longer be called "unmet." Fellow will "track whether items are still open and resurfaces them before the next relevant meeting," and its pre-meeting brief will "remind every attendee of the follow up items from previous conversations"; Littlebird lists, each week, what you promised your advisor and compares against outcomes (Kept / In progress / Needs a note); Feishu's "Meeting Express" compiles action items from "the smart minutes of the past week." Sources: https://fellow.ai/features/action-items , https://littlebird.ai/routines/promise-tracker , https://www.feishu.cn/content/article/7577317993749269689 , all accessed at the time of writing; see also 05 K6, 06 V6, C3.)
   **Revised statement [Inference]**: carrying unfinished items forward across meetings is now an expected feature; what remains unmet in research 1:1s is **three attributes of this continuity**: ① **Bidirectional**: the advisor's promises to the student are recorded too (not seen within the searched scope, and with zero direct evidence; see §15 H2); ② **Consensus**: it only counts once the student drafts it and the advisor confirms (Fellow's action-items page shows no assignee confirmation); ③ **Outcome semantics**: beyond "was it done," also record "whether the result supported or refuted something" ([Assumption · to be validated], see U3). What labs need is still a rolling ledger organized by "student × project × timeline," but the selling point can only be these three attributes, not "cross-meeting" itself.
4. **[Fact] This segment has a constraint that general-purpose tools cannot get around: institutional restrictions on AI meeting bots.** Harvard (2025-02) does not permit AI meeting assistants in university meetings, except for tools covered by an enterprise agreement. UCSD prohibits AI assistants in meetings that discuss research involving identifiable human subjects. Mississippi State blocks otter.ai and read.ai in Teams outright. CIHR prohibits AI transcription in peer-review meetings. In addition, **in-person group meetings, whiteboard discussions, and mixed Chinese-English speech** all break the "bot joins Zoom" model.
5. **[Fact] Some are already working on this, but all are very early-stage.** Fabric has an academic labs marketing page (no customer cases); Littlebird has a page aimed at graduate students, claiming to generate a "what you've promised" brief before meetings, at a student price of $15/month (added at the time of writing: there is also a Team plan from $17 per seat per month, including shared projects, https://littlebird.ai/pricing ); Supervisor Meeting Brief is a Chrome extension with 3 users, including a "last meeting" panel and "stale action item detection"; phd-weekly-review is an Agent Skill with 2 installs; and there is Research Lab Hub (0 ratings, see Competitors 03). **The direction has been validated in the sense that others have thought of it, but there is no evidence of large-scale adoption for any of them.** (Added at the time of writing: the general-purpose tool Fellow has also built cross-meeting carry-forward and two-way GitHub sync; it is not "academia-specific" but still constitutes a substitute, https://fellow.ai/integrations/github .)
6. **[Assumption] The conclusion has two layers. Commercially, this segment has weak willingness to pay, a fragmented market, and an odd decision chain (students feel the pain, PIs pay, university IT approves). For a portfolio and demo, it is almost the optimal choice**: the project owner is personally in a lab at the target university, so can dogfood, obtain real or semi-real meeting material, and run 5 or more usability tests within a week. I recommend treating it as the **"wedge segment" of BriefPilot v2**, and not presenting it as the final market.

---
## 1. Research Methods and Structure of Evidence Sources

| Evidence type | Representative sources | Count | Credibility |
|---|---|---|---|
| Peer-reviewed / academic journals | PLoS Comput Biol, "Ten simple rules for productive lab meetings" (2021); a group-meeting paper in *Research on Graduate Education* (2022); the JACMP Duke case (2025, see Competitor 03); Nature 2021 report on digital tools for labs | 4 | High |
| Official university policies / handbooks | UCSD, Harvard, Mississippi State, UNM, Utah, CU Anschutz, Sheffield, Newcastle, Liverpool, UW CS, Loyola, HKU, the target university | ~13 | High (some seen only in search snippets, flagged as such) |
| Public lab rules / handbooks | China Agricultural University functional dairy lab, a Nankai University research group, Endy Lab (Stanford/MIT OpenWetWare), Beheshti group (Macquarie), Fischer Lab, Warwick MIBTP supervisor self-description | ~7 | High (primary sources), but the sample is biased (labs willing to publish their rules are mostly the well-managed ones) |
| Student forums / media | GradCafe posts, Editage's retelling of Zhihu, Queen's 2009 department survey | 3–4 | Medium |
| Products / attempts | Fabric, Littlebird, Supervisor Meeting Brief, phd-weekly-review, PhD-Plan, Prograds | 6 | Medium (mostly self-described marketing) |
| Survey data | Nature 2025 PhD student survey (secondary source, figures conflict), HEPI | 2 | Medium-low (original source to be verified) |

**Why this mix**: The user asked for "evidence-based" conclusions. Student complaints are the easiest evidence to obtain, but also the most prone to survivorship bias (the people who complain are the ones in the most pain). So I prioritized **institutional evidence** (what university and lab rules actually say, which shows the problem is widespread enough to need written rules), then used forum and media content to add a sense of emotional intensity.

---

## 2. The Landscape of Research-Lab Meetings: Types, Frequency, Participants, Outputs

| Meeting type | Typical structure | Frequency | Participants | Outputs (current state) | Evidence |
|---|---|---|---|---|---|
| **Group meeting / Lab meeting** | Members present in turn (slides), with questions from the advisor and peers; or, per Ten simple rules, rotating among literature discussion, topic discussion, and feedback on manuscripts/defense rehearsals | Small groups: once a week, about 2–3 hours, each person presenting roughly once a month; large groups: about once a month; the China Agricultural University case: every two weeks | PI, postdocs, PhD students, master's students, undergraduates, visiting scholars, occasionally external experts | Slides stay on personal computers; minutes mostly don't exist or are written by a student on rotation; action items live in individual notebooks | [Fact] the 2022 group-meeting paper in *Research on Graduate Education*; China Agricultural University rules; PLoS CB 2021 |
| **Advisor 1-on-1 / Advisor meeting / Supervision** | Review of last time and action items → progress this period → problems and blockers → next steps (nearly every guide recommends this four-part structure) | Weekly early on, biweekly or monthly later (Warwick supervisor self-description); the Nature 2025 survey indicates about half of students get less than 1 hour per week with their advisor (secondary source, to be verified) | Student + 1–2 advisors (including co-advisor) | Student's personal notes, post-meeting summary emails (recommended but not necessarily done); some UK universities require entry into a system | [Fact] a public GitHub gist; Imperial agenda suggestions; UW CS; Warwick; Nature 2025 |
| **Weekly report / Weekly update (asynchronous)** | One page with three sections: "Done last week / Main problems / Plan for next week" | Weekly | Student → PI (or compiled by an administrator) | Word/PDF, email, OneDrive, GitHub PRs | [Fact] China Agricultural University; Beheshti group; Fischer Lab; Whitaker Lab (Competitor 03) |
| **Journal club / Reading group** | One person presents a paper, followed by group discussion | Weekly or biweekly; some groups fold it into the group meeting | Whole group or across groups | Presenter's slides; the discussion is basically not preserved | [Fact] PLoS CB 2021; Lab Manager |
| **Collaborator meeting / Collaboration meeting** | Cross-institution, mostly online; often involves "who runs which experiments, who writes which section" | Irregular (project-driven, more frequent near deadlines) | Multiple PIs, students, industry partners | Shared Google Doc / Overleaf comments / email | [Inference] based on Granola's academic promotional article and Competitor 03; no direct survey data |
| **Grant / project reporting** | Stage progress, milestones, budget usage, list of outputs | Quarterly / annual / at project close | PI, project team, funder or university | Formal report, which requires "archaeology" through a year of group meetings and weekly reports | [Inference] based on the Duke case's description of the project lifecycle; no direct primary source |
| **Sub-project huddle / Experiment alignment meeting** | Two or three people discuss parameters and experimental design at a whiteboard | Any time | PhD student + postdoc + RA | Whiteboard photos (a GradCafe reply mentions photographing the whiteboard after meetings) | [Fact] GradCafe |

**Why this table matters**:
- **[Inference] Group meetings and 1-on-1s are two different product problems.** A group meeting is "one-to-many broadcast + public accountability"; its pain points are that the audience gains little and the presenter bears a high preparation cost (the complaint relayed by Editage: "presenters struggle to prepare, and the audience gets nothing out of it"). A 1-on-1 is "high-density guidance + private commitments"; its pain point is "can't remember, can't keep up." BriefPilot's "meeting → action item" capability is **better suited to 1-on-1s**, because commitment density is high, the parties are clear (student ↔ advisor), and they meet every week.
- **[Fact] The weekly report is a ready-made "output slot."** Many labs already mandate weekly reports in a fixed "done / problems / plan" format. If the tool can **draft the weekly report** from the past week's meetings and logs, no new process needs to be introduced, and it directly replaces an existing painful task. This is critical for adoption resistance (in the Duke case the biggest obstacle was precisely "uneven adoption by members and the need for ongoing supervision to keep things updated," see Competitor 03).

---
## 3. What Happens After the Meeting: Where Information Breaks Down

### 3.1 Who Takes Notes

- **[Fact]** The PLoS CB paper "Ten simple rules" lists the notetaker as an **optional** role, alongside the timekeeper. It does not prescribe a formal process for minutes or action items, and only stresses the cycle of "preparation before the meeting, participation during the meeting, follow-up after the meeting". Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8158921/
- **[Fact]** The lab rules at China Agricultural University state that group meetings are "convened by the leader of each research group", and that an administrator compiles the weekly reports. **No one is designated to record minutes**; the management focus is on "whether you handed it in, whether you were late". Source: https://fdl.cau.edu.cn/col/col41806/index.html
- **[Summary]** In a small 2009 survey within a Queen's University department, 13 out of 13 respondents said they took notes in advisor meetings, using tools including Google Docs and Google Sites (search snippet; very small sample). Source: https://research.cs.queensu.ca/home/audrey/papers/GHC2009.BOFslides.pdf
- **[Fact]** A GradCafe post (2018): the poster said taking notes during a meeting is "distracting", while recording means "having to go back and sift through 30–60 minutes of audio, which is more of a hassle". Replies describe these approaches: write 2–3 words per item before the meeting, jot one line per item during the meeting, and photograph the whiteboard afterward; type on a laptop (with the advisor's consent); record only in high-density meetings, such as discussing two thesis chapters. Source: https://forum.thegradcafe.com/topic/108546-note-taking-during-advisor-meetings

> **Why it matters**: This post states the product opportunity clearly. The student's dilemma is "take notes and miss part of the discussion, or record and never listen back". Recording itself is cheap; the real cost is that **no one organizes it afterward**. This is exactly where "transcript → structured commitments → human confirmation" comes in.

### 3.2 How Commitments Are Tracked

- **[Summary · to be verified]** UW CS PhD handbook (search snippet; the page still redirected to an internal domain that requires login): "Don't be upset if your advisor cannot remember what was discussed in your previous meeting"; "It is essential to record what was discussed"; it recommends sending an agenda before the meeting and a written summary afterward. Source: https://www.cs.washington.edu/academics/phd/handbook/advising-guide/building-a-relationship
- **[Summary]** The Loyola graduate student survival guide recommends sending the advisor a short summary email after every meeting to avoid misunderstandings (search snippet). Source: https://www.luc.edu/media/lucedu/history/graduateprogramhandbook/adviceonbeingasuccessfulgraduatestudent/Graduate%20School%20Survival%20Guide.pdf
- **[Summary]** HKU Office of the Dean of Students/Student Affairs: "students may forget key points and miss follow-up actions; notes help recall action items" (search snippet). Source: https://aas.hku.hk/adv_news/etips-apr2021/
- **[Summary]** A Soft Academia column suggests that if an advisor is unwilling to put project details in email, the student should write a summary after the meeting and ask the advisor to confirm it (search snippet). Source: https://softacademia.substack.com/p/dear-bewildered-and-burnt-out
- **[Fact]** A gist by weitsang (self-described as "AI-generated, key points provided by the author") recommends this process: settle the key points two days before the meeting and send the agenda the day before; during the meeting, follow "review last action items → progress → problems → plan"; send a summary email within a few hours afterward; keep a daily research log and compile it into a weekly report at the weekend. Source: https://gist.github.com/weitsang/5d95b790d5d58d2a5ccb291dd215e554

**[Inference] Takeaway**: Every guide offers the **same manual process**: "agenda before the meeting + quick notes during it + summary email afterward + review at the next meeting". That it is recommended again and again suggests it works; that it needs to be recommended again and again also suggests many people cannot sustain it. **This is a classic JTBD of "known best practice, but costly to execute"**. AI's value lies not in inventing a new process, but in bringing the execution cost of this widely accepted process close to zero.

### 3.3 How to Report Next Week

- **[Summary]** In Chinese-language contexts, "how to report at a group meeting when you have no progress" is a recurring, high-traffic question (Zhihu questions "研究生组会，没有进展怎么汇报？" (How should a graduate student report at a group meeting when there is no progress?) and "如何在课题没有进展的情况下，讲一场让导师满意的组会？" (How to give a group meeting that satisfies your advisor when your project has made no progress?), The Paper's "科研毫无进展，如何堂堂正正地水组会？" (With no research progress, how do you openly coast through a group meeting?), and Hupu's "组会没进度怎么汇报" (How to report at a group meeting with no progress)). The recommended reporting structure is "previous assignments → current progress and difficulties → next-step plan" (search snippet). Sources: https://www.zhihu.com/question/268901881 ; https://www.zhihu.com/question/491712440 ; https://m.thepaper.cn/newsDetail_forward_20351898
- **[Inference]** The "previous assignments" section requires the student to accurately restate **what the advisor assigned last time**. Without a record, the student can only scroll through WeChat chats, ask senior labmates, or rely on memory. This is the actual form of the "what did my advisor tell me to do last time?" problem. It erupts in a concentrated way the night before the report, carries a sense of anxiety, and is high in intensity.

### 3.4 Institutional Level: Universities Also Require "Records"

- **[Summary]** Newcastle's PGR code of practice requires all students to keep records of all supervisory meetings; Liverpool requires full-time students to log formal supervisory meetings monthly (search snippet). Sources: https://www.ncl.ac.uk/student-progress/pgr/activities/meetings ; https://liverpool.ac.uk/pgr-development/toolbox/supervisory-meetings
- **[Summary]** Sheffield stipulates that recordings require the supervisor's permission; if refused, students must "not attempt unauthorized recording", and students are encouraged to write notes whether or not they record (search snippet). Source: https://sheffield.ac.uk/media/29592/download
- **[Fact]** McGill uses myProgress, Southampton uses PGR Tracker, and UBC and other universities use Prograds to track degree progress. Prograds' author Fred Cutler (a professor of political science at UBC) points out: "PhD committees don't share notes, department information is inaccessible to supervisors"; the page says paying customers already include U of Toronto, UMass-Amherst, and Texas A&M, but gives no user counts or revenue. Source: https://cutler.portfolio.arts.ubc.ca/activities/prograds-the-grad-student-progress-app/

> **Why it matters**: (1) Institutions requiring "keep records" shows that record-keeping is a hard requirement, and that there is a **department / graduate-school-level paying party** (Prograds' paying customers are universities). (2) These systems manage **term-level milestones** (whether meetings happened, whether requirements are met), not **week-level commitments** (which set of experiments to run this week). The gap between the two is this segment's opportunity band.

---
## 4. Public Voices from Three Perspectives

### 4.1 Student side

| Pain point | Evidence | Label |
|---|---|---|
| Hard to take notes and listen at the same time; recordings are never replayed | GradCafe 2018: "Recording the conversation seems more cumbersome having to filter through 30-60 minutes of audio." | [Fact] |
| Dread of group meetings; high preparation cost | Yideji (意得辑) relaying a highly upvoted Zhihu answer: "just thinking about the group meeting makes my whole body go cold, like winter"; "the content presented on stage is fragmented and has nothing to do with me" | [Fact] (secondary relay) |
| Not knowing how to report when there is no progress | Titles of several high-traffic questions on Zhihu, The Paper (澎湃), and Hupu | [Fact] (titles only) |
| Advisor can't remember the last meeting; students have to fill the gap | UW CS handbook (search snippet; original page requires login) | ~~[Fact]~~ [Summary · to be verified] (corrected at the time of writing, 06 C1) |
| Little supervision time; satisfaction correlates with meeting time | Nature 2025 survey (3,700+ doctoral students): about half of students spend <1 hour per week with their advisor, ~~satisfaction 69% vs. 82%~~. **However, the Springer Nature community response piece states the direction the opposite way**; the original needs checking, doi:10.1038/d41586-025-03416-7. A HEPI report separately says 63% meet their advisor for <1 hour per week. **(Added at the time of writing)** This round I opened the Springer Nature community response piece: it says "69% of students who spent more than one hour per week with their supervisor were satisfied" and "82% of students who felt emotionally and academically supported reported satisfaction". **The 82% corresponds to "feeling supported", not "meeting more"**, so "69% vs. 82%" cannot be used as a comparison of meeting time. The Nature original redirects to a login page, and the UCF reprint PDF fetched this round yielded only font metadata, so **the original figures remain to be verified**. | ~~[Fact] (numbers conflict, to be verified)~~ [Summary · to be verified] (corrected at the time of writing: original not opened; downgraded to match the [Fact] labels in M3 §2 table and §8, 06 W6, C5) |

**[Inference]** The less meeting time there is, the higher the information density per minute, and the greater the cost of anything missed. This supports the high value of "1-on-1 meeting minutes", but it needs confirmation through interviews.

### 4.2 PI side

- **[Fact]** In a 2021 Nature article, PI Christie Bahlai says "Slack is not a great way to record anything for posterity", and that long-term goals "keep falling through the cracks"; Mark Gerstein uses Google Recorder + Rev + Grammarly to turn discussions into documents; Titus Brown opposes weekly group meetings but requires that students can book a 1-on-1 with him at any time (see competitor 03). Source: https://www.nature.com/articles/d41586-021-01752-y
- **[Fact]** (Beheshti) / **[Summary]** (Fischer Lab, Warwick) PIs respond by **requiring students to submit written material**: the Beheshti group requires a one-page weekly report, which the PI uses to "measure your progress in a qualitative way"; the Fischer Lab requires a weekly progress email before Friday; a Warwick supervisor requires a one-page progress report every two weeks (the latter two are from search snippets). Sources: https://data-science-group.github.io/weekly-report.html ; https://sites.evergreen.edu/fischerlab/?p=72 ; https://warwick.ac.uk/fac/cross_fac/mibtp/phd/supervisors/mgreenhalgh/
- **[Fact]** In a lab at China Agricultural University, an administrator sends the advisor a list of students who have not submitted each week, and the advisor checks the group meeting records every two months. The management cost is shifted onto the "administrator" role.
- **[Inference]** The PI's core pain point is not "can't remember one particular meeting" but the **combinatorial explosion of "10+ people × multiple commitments each week"**. What the PI needs is a **cross-person view** of "who is stuck, who is drifting, and what I promised whom", not a single-meeting summary. Fabric's claim of a "PI weekly digest, so the PI stays current without scheduling another meeting" targets exactly this (marketing claim, unverified).

### 4.3 Lab administrator / secretary / senior-labmate side

- **[Fact]** (China Agricultural University) / **[Summary]** (Zhaopin) The China Agricultural University rules define an explicit "administrator" role responsible for collecting weekly reports, compiling statistics, uploading to a shared drive, and reporting the list of those who have not submitted. Zhaopin also has a job description for a research group secretary, with duties that include "tracking progress and recording meetings" (search snippet; job details to be verified). Sources: https://fdl.cau.edu.cn/col/col41806/index.html ; https://m-pre.zhaopin.com/jobs/CC315171120J40792855103.htm
- **[Fact]** The Nature 2021 article targets groups of "5–15 people without a full-time lab manager" (competitor 03), which shows that **most groups have no dedicated administrator**; the function falls to the PI personally or to senior students (the "大师兄/大师姐" senior labmates, senior PhDs, postdocs).
- **[Inference]** The administrator's pain point is **compiling and chasing submissions**, which is repetitive and not creative work. If a tool can automatically generate a "this week's whole-group progress table + open commitments", the administrator is the most direct beneficiary and may also be the most active internal advocate.

---
## 5. Research-Meeting-Specific Content Types (and Why Generic Tools Miss Them)

| Content type | Example (synthetic) | How generic meeting tools handle it | What the research setting requires | Label |
|---|---|---|---|---|
| **Hypothesis / conjecture** | "I suspect the action chunking length is causing the jitter" | Treated as an ordinary statement, or dropped | Tag separately as "hypothesis to verify" and link to later experiment results | [Inference] |
| **Experiment design and parameters** | "Change lr to 3e-4, batch 64, run 3 seeds" | Numbers are easily mistranscribed and not structured | Preserve exactly, traceable to the timestamp of the original utterance | [Inference]; for number and formula transcription errors, see the Speech-to-LaTeX study cited in competitor 03 |
| **Interpretation of results** | "This ablation shows the vision encoder is not the bottleneck" | Summarized as "discussed the results" | Distinguish "observed facts" from "interpretation" | [Inference] |
| **Literature references** | "Take a look at how the OpenVLA paper and π0 do it" | Paper names are not recognized or linked | Recognize the paper and link it to Zotero or arXiv | [Inference] |
| **Soft commitments** | "I'll try it next week" / "I'll ask Prof. X for you when I have time" | Either dropped or treated as a hard task | Tag commitment strength (soft/hard); **allow no due date** | [Assumption] inference from competitor 03 |
| **Advisor → student commitments** | "I'll open up the dataset permissions for you" / "I'll write you a recommendation letter" | Generally only captures "what the student has to do" | Record both directions; students usually **feel awkward chasing their advisor** | [Assumption] proposed in this document, pending interviews |
| **Reviewer comments / rebuttal assignments** | "R2 says the baseline is insufficient, you add a Diffusion Policy" | Not recognized | Link to the submission and its deadline | [Inference] |
| **Deadline** | "We need real-robot experiments before the CoRL submission deadline" | Treated as an ordinary date | Connect to long-term milestones (a public gist also suggests linking each week's tasks to conference deadlines and paper milestones) | [Fact + Inference] |
| **Whiteboard / hand-drawn sketches / formulas** | Block diagrams, derivations | Audio-only tools cannot see them | Photo + OCR/multimodal understanding; GradCafe replies and a Rocketbook user's write-up both show the need exists | [Fact] (the need exists) |

**Why it matters**: This table gives a direct basis for reworking BriefPilot's "action item extraction" schema. The current PRD fields are "who / what / when"; the research version needs at least three more: **commitment direction (who to whom), commitment strength, and linked object (paper/experiment/submission)**, while keeping the existing principle of "leave missing fields blank rather than guess". This principle matters more in research settings than in company settings, because most research commitments have no explicit due date.

---

## 6. Environmental Constraints: In-Person, Multilingual, Privacy

### 6.1 More In-Person Than Online Meetings → Recording Method

- **[Fact]** Group meetings are mainly in person, moving online or hybrid during the pandemic and when the advisor is traveling (a 2022 study). Whiteboard discussion is common (GradCafe, Nature 2021).
- **[Fact]** Littlebird claims to "keep bots out of meetings", capturing audio from the computer and using an iPhone app for in-person settings; Fabric claims "no-bot recording" (both vendor self-descriptions). Sources: https://littlebird.ai/for/graduate-students ; https://fabric.so/for-your/meeting-notes
- **[Inference]** Ranked by feasibility, the recording methods for in-person lab meetings are: (1) the presenter's laptop, since it is already used for screen sharing; (2) a phone placed on the table; (3) an omnidirectional meeting-room microphone, which is rare. **"Upload a recording or a handwritten/shorthand set of minutes"** fits labs better than a "real-time bot joining the meeting", and it matches BriefPilot's existing "upload a document" technical form.

### 6.2 Multilingual

- **[Fact]** The original paper on the SEAME corpus (spontaneous Mandarin–English code-switching speech from Singapore/Malaysia) notes that intra-sentential Mandarin–English mixing is common in Singapore and Malaysia; the model card for A*STAR I²R's MERaLiON-3-ASR says it is trained specifically on Singapore English, dialects, and English-X code-switching (accuracy is vendor self-reported and not independently verified). Sources: https://www.isca-archive.org/interspeech_2010/lyu10_interspeech.html ; https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR
- **[Inference]** The typical speech pattern in Singaporean / overseas Chinese labs is "Chinese sentence frame + English terminology" or the reverse, for example "这个 policy 的 rollout 在 sim 里 OK，但 real robot 上 gripper 会 drift" (roughly: this policy's rollout is fine in sim, but on the real robot the gripper drifts). In labs in China it is "Chinese + English abbreviations/model names". **Generic ASR errors concentrate on terminology and model names, which are exactly the most critical nouns in action items.** Remedy: use the lab's own glossary or paper library for hotwords and post-correction. This also makes use of BriefPilot's RAG capability, feeding the knowledge base into transcript correction. [Assumption] The effect needs to be tested.

### 6.3 Privacy and Unpublished Data

- **[Fact]** UCSD: only the host may "capture" a meeting; you may not send an AI assistant to "attend" in your place; only AI assistants that have passed a privacy and security review and have a signed written agreement may be used; use is prohibited when discussing identifiable human-subjects research (unless the AI itself is part of the research and is written into the IRB protocol); "research planning" falls under P-3 information requiring "extreme caution". Source: https://privacy.ucsd.edu/ai-guidelines/
- **[Summary · to be verified]** Harvard (2025-02, search snippet, original page returned 403): AI meeting assistants may not be used in university meetings, except under an enterprise agreement. Source: https://www.huit.harvard.edu/news/guidance-ai-meeting-assistants-data-privacy-principles
- **[Summary]** Mississippi State blocks otter.ai and read.ai in Teams; UNM requires hosts to remove AI assistants that were not disclosed; Utah recommends Teams Premium / Zoom AI Companion and does not recommend Otter/Fireflies; CIHR prohibits AI transcription in peer-review meetings (including discussions before and after) (all from search snippets). Sources: https://servicedesk.msstate.edu/TDClient/45/Portal/KB/ArticleDet?ID=2129 ; https://airesources.unm.edu/ai-guidance/ai-meeting-capture.html ; https://ai.utah.edu/blog ; https://cihr-cri.gc.ca/e/54129.html
- **[Fact]** The target university has published its position on the use of generative AI in research, requiring "ethical, responsible, transparent, and accountable" use; **this round found no specific rule from the target university on AI meeting transcription tools (to be verified)**. Source: (university page; link removed)
- **[Fact]** A student-built PhD planning tool (H-tr/PhD-Plan) encrypts data in the browser with AES-256-GCM and stores only ciphertext in the repository, which shows that the research plan itself is treated as sensitive information. Source: https://github.com/H-tr/PhD-Plan
- **[Inference]** Privacy concerns fall into three layers: (a) **institutional compliance** (whether IT has approved the tool, whether data leaves the country, whether it is used for training); (b) **academic competition** (unpublished ideas being leaked or learned by models); (c) **power dynamics within the group** (students may not want the PI to see all the raw discussion, and the PI may not want to be recorded). Layer (c) is a dimension generic tools barely consider, and it is also where designs like Fabric's, from the PI's perspective and automatically creating tasks for each member, may meet resistance. [Assumption]

> **Why it matters**: This section points directly to a differentiation direction. **"Private by default, owned by the student, shared only after confirmation, local/self-hostable, no training"** is itself a positioning point that sets the product apart from Otter/Fireflies, and it is consistent with BriefPilot's existing principle that "formal tasks are generated only after human confirmation".

---
## 7. Personas (synthetic, based on public evidence, pending interview validation)

### Persona A: Lin, third-year PhD student (primary persona) [Assumption]
- **Background**: Robotics / VLA research at a Singapore university, a mix of computational work and real-robot experiments; a group of 12. One group meeting per week (mainly in English), one 30-minute 1-on-1 with the advisor per week (mixed Chinese and English), and one Zoom call every two weeks with overseas collaborators.
- **Tools**: Notion (personal), Overleaf, Zotero, GitHub, Slack or WeChat groups, handwritten notes on an iPad, phone photos of the whiteboard.
- **Goals**: Submit CoRL/ICRA papers on time; come across as "reliable" to the advisor; avoid being caught off guard in group meetings.
- **Pain points**:
  1. During 1-on-1s, taking notes while listening means missing parameter details (evidence: the GradCafe dilemma).
  2. When writing the weekly report on Sunday night, digging through chat history and notebooks: "Which baseline was I supposed to add last time?" (evidence: the "previous arrangements" reporting structure on Zhihu).
  3. Feeling awkward about chasing the advisor on things promised (e.g., opening a GPU quota, introducing a collaborator). [Assumption]
  4. Not daring to hand recordings to Otter, for fear of violating university rules or leaking unpublished ideas (evidence: §6.3).
- **What success looks like**: Within 5 minutes after the meeting, a checklist of "decisions / my commitments / advisor's commitments / hypotheses to verify"; after confirming it, a one-click weekly report draft; before the next 1-on-1, "3 items left open from last time" appears automatically.
- **Quote (synthetic, not real)**: "I don't need a verbatim transcript. I need to know what I promised and what he promised."

### Persona B: Prof. Chen, PI (economic decision-maker) [Assumption]
- **Background**: Associate professor supervising 3 postdocs, 8 PhD students, and 4 master's students/RAs, with 2 grants and 1 industry collaboration at the same time. Weekly group meeting plus a biweekly 1-on-1 with each person; roughly 10–15 student-related meetings per week.
- **Tools**: Outlook calendar, email, paper notebook, WeChat/Slack, occasionally students' Notion pages.
- **Goals**: Every student graduates on schedule and produces output; grants close out on time; recruit good students.
- **Pain points**:
  1. Can't remember where each student got stuck last time, and only recalls it in the 5 minutes before each 1-on-1 (evidence: the UW handbook acknowledges that advisors forget [Summary · to be verified]; the Prograds author's own account).
  2. Doesn't know who is "drifting"; by the time it's noticed, months have passed (evidence: Bahlai, "long-term goals fall through the cracks").
  3. Writing closeout reports and recommendation letters requires "archaeology" on what a student did all year (evidence: Durrant Lab uses GitLab records to write recommendation letters; see competitor 03).
- **Concerns**: Reluctance about, or concerns over, recordings; unwilling to add burden to students; worried about university IT compliance.
- **What success looks like**: Every Monday, a one-page "whole-group commitments board": who delivered, who is overdue, what I owe whom. No need for yet another meeting.
- **Ability to pay**: Has funding, but purchases go through reimbursement or procurement; below a certain unit price it may be possible to pay by credit card and claim reimbursement. [Assumption] The threshold is unknown.

### Persona C: Wang, lab administrator (operator / enabler) [Assumption]
- **Background**: A senior PhD student or a full-time lab secretary / lab manager; collects weekly reports, schedules group meetings, manages equipment bookings, and maintains the shared drive.
- **Pain points**: Chasing weekly reports every Monday and compiling them by hand into a table for the PI (evidence: China Agricultural University's policy); nobody writes group meeting minutes, or if written, nobody reads them; newcomers can't find historical decisions.
- **What success looks like**: Weekly reports are compiled automatically; group meeting minutes are archived automatically to the project page; newcomers can ask "Why doesn't our group use method X?" and get an answer with citations. This matches BriefPilot's existing "cited knowledge Q&A" capability.

### Persona D (secondary): Postdoc / collaborator Dr. Rao [Assumption]
- Works with the PI, multiple students, and external collaborators at once, and is the "hub" of the commitment network. The pain point is dependencies across meetings and people ("wait for A's data → only then can I run B").

---

## 8. A Week in the Life (PhD student × PI, two tracks, synthetic)

| Time | PhD student Lin | PI Chen | Current tools and breakpoints |
|---|---|---|---|
| Mon 9:00 | Submits weekly report (one page) | Receives reports, skims | The weekly report is pieced together from memory and chat history, **breakpoint ①** |
| Mon 14:00 | Group meeting (English, slides, 2 hours) | Chairs, asks questions | No minutes, or minutes from a rotating student; cross-group tasks the PI assigns verbally vanish in the meeting room, **breakpoint ②** |
| Tue | Runs experiments; revises experiment design with a postdoc at the whiteboard | Grant meeting / teaching | Whiteboard photos sit in the camera roll, **breakpoint ③** |
| Wed 15:00 | 1-on-1 with the advisor (30 minutes, mixed Chinese and English) | 4th 1-on-1 of the day: "Where did we leave off?" | Student's shorthand + memory; PI's memory, **breakpoint ④ (core)** |
| Thu | Zoom with overseas collaborators; discusses rebuttal division of labor | — | May have Zoom's built-in transcript, but it doesn't enter the lab knowledge base |
| Fri | Reads papers; prepares for journal club | Reviews papers; when writing recommendation letters, can't find what the student did last year | **Breakpoint ⑤** |
| Sun night | Anxious: "Which baseline did my advisor ask me to add last time?" | — | Digs through WeChat, asks senior labmates |

**[Inference] Breakpoint ④ is the most frequent, most intense, and most private one**, making it suitable as the MVP's sole entry scenario; breakpoint ① (weekly report) is the best "output slot"; breakpoint ⑤ (PI archaeology) is the reason a PI would be willing to pay.

---

## 9. JTBD List (Jobs To Be Done)

Format: When …, I want to …, so that …

**PhD students / master's students / RAs**
1. When I finish a 1-on-1 with my advisor, I want to get **what I promised and what the advisor promised** within 5 minutes, so that nothing is missed and I don't have to awkwardly ask again. [Core]
2. When I prepare for the next 1-on-1 or group meeting, I want to automatically see **last time's open items and the original wording at the time**, so that I can report using the "previous arrangements → progress → plan" structure. [Core]
3. When I write my weekly report, I want the tool to **draft** it from this week's meetings and logs, so that I save that hour on Sunday night.
4. When a paper or a parameter comes up in a meeting, I want it recorded **verbatim** and linked to my reference library, so that I can reproduce it later.
5. When the discussion involves unpublished results, I want to be sure that **data stays within my control and isn't used for training**, so that I can use the tool with peace of mind.
6. When my advisor and I disagree about "what was said last time", I want **traceable evidence** (timestamp / original wording), so that misunderstandings can be resolved peacefully.

**PI**
7. When I have several 1-on-1s back to back, I want to see each student's **key points from last time + overdue items** 30 seconds before each one starts, so that I don't rely on memory. [Core]
8. When I start work every Monday, I want to see the **whole-group commitments board** (who is stuck, who is overdue, what I owe whom), so that I can spot "drifting" students early.
9. When I write a closeout report or recommendation letter, I want to search a student's / project's **decisions and outputs** over the past year, with sources.
10. When I decide whether to adopt a tool, I want to confirm that it **complies with university IT and ethics rules** and doesn't add burden to students, so that I don't get into trouble.

**Lab administrator**
11. When the weekly report deadline arrives, I want group progress to be **compiled automatically**, with non-submitters listed, so that I don't have to chase people by hand.
12. When a newcomer joins the group, I want them to be able to **ask about** historical decisions and the reasons behind method choices, so that repeated explanations are reduced.

---
## 10. Pain Point Ranking (Frequency × Intensity × Satisfaction with Current Solutions)

> Scores are the researcher's judgments (1–5) based on the evidence in this document and are **not measured values**; the lower the "satisfaction with current solutions," the more painful the problem. Opportunity score = frequency × intensity × (6 − satisfaction), used only for ranking.

| # | Pain point | Frequency | Intensity | Satisfaction with current solutions | Opportunity score | Main evidence | Label |
|---|---|---|---|---|---|---|---|
| P1 | Forgetting / misremembering commitments and parameters after a 1-on-1 ("what did my advisor ask me to do last time?") | 5 (weekly) | 4 | 2 | 80 | GradCafe; UW handbook; Zhihu report structures | [Inference] |
| P2 | Unable to quickly review the previous meeting and unresolved items before the next meeting (both students and PIs) | 5 | 4 | 2 | 80 | weitsang gist four-part structure; Supervisor Meeting Brief has a "From last meeting" feature | [Inference] |
| P3 | High cost for PIs to follow up across students; noticing that a student is "drifting" too late | 4 | 5 | 2 | 80 | Nature 2021 Bahlai; Prograds; Duke case | [Inference] |
| P4 | Writing weekly / progress reports is time-consuming and pieced together | 5 | 3 | 2 | 60 | China Agricultural University; Beheshti; Fischer | [Inference] |
| P5 | Compliance and privacy concerns make people reluctant to use existing AI tools | 3 (affects adoption) | 4 | 2 | 48 | UCSD; Harvard; MSU; CIHR | [Fact + Inference] |
| P6 | Group meeting minutes are missing, so group decisions cannot be searched and newcomers cannot inherit them | 4 | 3 | 2 | 48 | PLoS CB (notetaker is optional); China Agricultural University (no note-taker); Fabric's headline pitch of "newcomers can search history" suggests vendors reach the same judgment | [Inference] |
| P7 | Mixed Chinese-English speech / terminology transcription errors | 3 (high in Singapore/Malaysia and overseas Chinese groups, medium-high in China) | 3 | 2 | 36 | SEAME; MERaLiON; competitor 03 | [Inference] |
| P8 | Whiteboard / handwritten content is lost | 3 | 2 | 2 | 24 | GradCafe photographing whiteboards; Nature 2021 Rocketbook | [Fact] (the need exists) |
| P9 | "Archaeology" for final reports / recommendation letters | 1–2 (quarterly / yearly) | 4 | 2 | 24–32 | Durrant Lab; Duke | [Inference] |
| P10 | Group meetings themselves are inefficient and attendees gain nothing | 5 | 3 | 2 | 60 | Paraphrased from Editage | [Fact], **but BriefPilot is not recommended to address it**, as it is an organizational culture problem |

**Why P1–P3 rank highest**: They satisfy all three criteria at once: they happen every week; institutional or guideline evidence shows they are widespread; and the existing solutions are purely manual. **Although P10 scores high, it is a question of "whether the meeting should be run this way," not "how information flows after the meeting,"** so it falls outside the product boundary. BriefPilot is positioned as a "post-meeting assistant," not a "meeting coach."

---

## 11. Comparison of Unmet Needs × Where Existing Products Fall Short

| Unmet need | General meeting tools (Otter/Fireflies/Feishu Minutes/Zoom AI) | General knowledge bases (Notion AI/Fabric) | Academic-specific attempts (Littlebird/Supervisor Meeting Brief/Research Lab Hub/Prograds) | Manual processes (pen and paper/Google Doc/email/weekly report templates) | Possible entry point for BriefPilot |
|---|---|---|---|---|---|
| **Cross-meeting commitment ledger** (rolling by student × project, not by individual meeting) | ~~Works per individual meeting; action items are not tracked across meetings [Inference]~~ (Corrected at the time of writing: Fellow brings unfinished items into the pre-meeting view, Feishu "Meeting Express" summarizes a week's action items, and Otter/Granola offer pre-meeting briefs, so the binary version is already covered [Fact]; see 05 K6. What has not been seen is organization by "student × project" and two-way commitments) | Fabric claims to "prepare the next meeting based on past meetings" [vendor claim] | Littlebird claims its pre-meeting brief shows "what you committed to"; the SMB plugin has "From last meeting" and stale-item detection [self-reported, very few users] | Relies on self-discipline | Commitment ledger + automatic pre-meeting review, **with verbatim quotes** |
| **Two-way commitments** (the advisor's commitments to the student) | Generally extracts only "who does what," without distinguishing the direction of power [Inference] | Not seen [unverified] | No explicit description seen | Students are reluctant to write them down | Explicit "commitment direction" field [Assumption: real pain point] |
| **Soft commitments / no deadline** | Tend to fill in a deadline or ignore the item [Inference] | Fabric claims to "create tasks with deadlines" | — | — | Keep "leave missing fields blank, don't guess" + intensity labels |
| **In-person / whiteboard** | Depend on a bot joining or an app recording; no whiteboard support [Inference] | Fabric supports computer audio [self-reported] | Littlebird iPhone in-person recording [self-reported] | Taking photos | Upload recordings / handwritten notes / whiteboard photos |
| **Mixed Chinese-English + terminology** | Uneven multilingual support; code-switching is a known difficulty [competitor 03] | No dedicated handling seen | Not seen | — | Use the lab's literature library for terminology correction [Assumption] |
| **Compliance / no training / local deployment** | Multiple universities have banned or restricted Otter and Read.ai [Fact] | Fabric states "not used for training," AES-256 [self-reported] | SMB stores data locally; Littlebird SOC 2 [self-reported] | Safest | Student-owned, private by default, self-hostable |
| **Power dynamics within the group** (students share selectively) | Not considered | Fabric leans toward the PI's perspective, "create tasks for each member" [Inference] | SMB is a personal student tool (no sharing) | Student stays in control | A **"student drafts → confirms → shares with advisor"** confirmation flow |
| **Output into existing slots** (weekly report / progress log / university forms) | Produces generic summaries | Automatic documents | Prograds manages semester-level milestones | Weekly report template | One-click "done / issues / plan" weekly report draft |
| **Linking papers / experiments / code** | None | Fabric can index papers [self-reported] | — | Manual links | Reuse BriefPilot's RAG + citations |

**[Inference] Takeaway**: Looking at each cell individually, almost every need has been partly addressed by someone. **No one delivers the combination of "a student-owned cross-meeting commitment ledger + two-way commitments + share after confirmation + weekly report output."** The differentiation should be framed as the combination and the embedding in the workflow, not as any single feature. (Added at the time of writing: the "cross-meeting commitment ledger" component of the combination has already been built in a binary version by Fellow and Littlebird; "no one delivers the combination" is a judgment within the scope of the search, and the combination itself is easy to copy, so it must be defended by the three attributes as revised in §0, item 3.)

---
## 12. Existing Attempts and Their Results

| Attempt | Form | Result / adoption evidence | Implication for us | Source |
|---|---|---|---|---|
| **Fabric for Academic Labs** | Vertical landing page of a general-purpose AI workspace | No customers, no case studies; only shows an App rating of 4.6 (3.5K+) | A large vendor has judged that "lab = meetings + papers + decision log" is worth building; **the potential competitor most worth watching** | https://fabric.so/teams/academic-labs |
| **Littlebird (for graduate students / researchers)** | Bot-free personal AI memory tool | Students $15/month (.edu, first two months free); claims to generate a pre-meeting brief of "commitments + open feedback + reading" and to list "what you promised your advisor" on Mondays; no adoption data | **Nearly isomorphic to JTBD #1 and #2 in this document**, which gives the pain-point judgment external corroboration; but ~~it is a personal tool~~ its commitment tracking is a personal view ("tuned to yours") (correction: Littlebird has a Team plan from $17 per seat per month, including shared projects and admin controls, https://littlebird.ai/pricing ). The page does not describe a PI view or a lab knowledge base | https://littlebird.ai/for/graduate-students |
| **Supervisor Meeting Brief** (Chrome extension) | Free, local storage | v1.0.0 (2026-05-30), **3 users** | Feature design (7-section pre-meeting brief, 8 post-meeting capture categories, stale action item detection, multiple advisors) is highly consistent with this document's JTBD, but it relies on purely manual entry, has no AI and no distribution → **proves that "thinking of it" is easy and "getting people to use it" is hard** | https://chromeboard.com/extension/supervisor-meeting-brief-fmibimgfmoaogdajeoeedledhejppgll |
| **phd-weekly-review** (Agent Skill) | Guided weekly report / reflection | 2 installs, 1 star (first seen 2026-04) | The idea of turning the "weekly report" into an AI-guided flow has appeared, but only as a personal project | https://www.skills.sh/a-green-hand-jack/phd-skills/phd-weekly-review |
| **PhD-Plan** (GitHub) | Encrypted PhD planning + lab GPU board | 0 stars | When students build their own tools, **encryption comes first**, which corroborates privacy sensitivity | https://github.com/H-tr/PhD-Plan |
| **Prograds** (built by a UBC professor) | University-level degree progress system | Claims paying customers at 6 universities | **The only one with evidence of payment**; the payer is the university or department, and it manages semester-level milestones | https://cutler.portfolio.arts.ubc.ca/activities/prograds-the-grad-student-progress-app/ |
| **Research Lab Hub / LabRAT / Notion templates** | Individual developer projects or templates | 0 ratings / personal project / many free templates | See Competitor 03 | Competitor 03 |
| **HN "Show HN"** | — | This round found no Show HN post specifically about lab meetings; only posts about research tools such as paper figure Q&A and paper-to-code | Search coverage is limited; **we cannot assert that none exists** | https://news.ycombinator.com/submitted?id=loganye |

**[Inference] Conclusion**: The shape of this space is "many small attempts, zero winners." Possible reasons: (a) weak willingness to pay; (b) adoption requires changing habits, and the Duke case shows that even monday.com needs sustained supervision; (c) personal tools have no network effects, while lab tools need the PI to pay. This is good for the portfolio: it lets me say "I looked at 5 failed or early-stage attempts, and here is how my design addresses the reasons they failed."

---

## 13. Willingness to Pay, Budget Sources, and Reachable Channels

### 13.1 Willingness to Pay and Budget

- **[Fact]** Student-side price anchors: Otter gives .edu users 20% off Pro, about $79.99/year (third-party roundup, to be verified), with a 50%-off back-to-school promotion in August 2026 (reposted press release); Notion offers Plus (single-person workspace) free to students with school email addresses, and student organizations can also use Plus for free; Littlebird is $15/month for students. Sources: https://www.meetjamie.ai/blog/otter-ai-pricing ; https://www.01net.it/back-to-school-half-the-price-otter-ai-offers-students-50-off-to-turn-lectures-into-study-guides-quizzes-and-exam-prep/ ; https://www.notion.com/help/notion-for-education
- **[Fact]** Researchers are generally **unwilling to pay out of pocket** and prefer to pay from grants or institutional budgets. The 2022 Idaho study concerned article processing charges (APCs), not software, so it is only an indirect reference. A common institutional practice is centralized purchasing or reselling of academic licenses (Mass General Brigham research computing center). Sources: https://id.erudit.org/iderudit/1088074ar ; https://rc.partners.org/news-events/announcements/research-software-annual-interest-survey
- **[Inference] Three payment paths and their difficulty**:
  1. **Individual student subscription**: price-sensitive (the anchors are free Notion and tools at $6–15/month); scale is only possible below $5/month. **Easiest to close, hardest to make money from.**
  2. **PI grant funds**: low unit price, fine as long as it is reimbursable, but the PI must be persuaded that it is "useful for the whole group," and the PI's pain point (P3) can only be solved if the whole group uses it, which creates a cold-start problem.
  3. **University / graduate school procurement**: Prograds proves it is feasible, but the cycle is long and it must pass IT security review; **compliance is both a barrier and a moat**.
- **[Assumption]** For Singapore universities such as the target university and NUS, path 3 may conflict with "the Microsoft Copilot / Google Gemini the university has already procured": the university will ask "why not use the Copilot we already have?" The target university's AI tool procurement needs to be verified. A report on the target university rolling out free Google AI tools is at https://www.dpexnetwork.org/news/view/BAV66qk5bNgVeLawfVQpmH (headline only, to be verified).
### 13.2 Reachable Channels

| Channel | Reachable population | Cost | Suitable stage | Label |
|---|---|---|---|---|
| The project owner's own lab (dogfood) | Size not public | Zero | Discovery / usability testing | [Assumption] |
| Other labs in the same school and department (referrals, graduate student association) | Dozens of people | Low | Interviews / small pilot | [Inference] |
| Academic Twitter/X, Bluesky, Xiaohongshu "PhD life" topics, Zhihu | Broad but scattered | Low–medium | Demand validation, waitlist | [Inference]; actual community sizes not verified in this round |
| Supervisor groups / the school's teaching development center / the graduate school | PIs, administrators | Medium | Payment validation | [Inference] |
| Research computing / IT department | Procurement decision-makers | High | Scaling up | [Inference] |

---

## 14. Risks

| Risk | Description | Severity | Evidence / label | Mitigation |
|---|---|---|---|---|
| **Small, fragmented market** | A single lab has 5–15 people; decisions are scattered across individual PIs | High (commercial) | [Fact] Nature 2021 reader profile; [Inference] | Position as "wedge segment + portfolio piece", with lateral transfer to "1-on-1s in small R&D teams and consulting teams" |
| **Weak willingness to pay** | Students don't pay, PIs need reimbursement to pay, and university procurement is slow | High (commercial) | [Fact] Indirect evidence from the Idaho APC study; Notion's free-tier anchor | Prove value first; don't discuss pricing at the demo stage |
| **Adoption friction** | Requires confirmation after every meeting; students don't update (Duke case) | High | [Fact] Duke case | Embed into an existing slot (the weekly report); a single confirmation takes ≤ 1 minute |
| **Compliance blocking** | Universities ban AI meeting tools that haven't been approved | High | [Fact] UCSD/Harvard/MSU | Upload mode (no bot), local / self-hosted option, no training on user data, explicit consent |
| **Power dynamics / trust** | Students don't want the PI to see the raw discussion; PIs don't want to be recorded | Medium–high | [Assumption] | Student-owned data, sharing only after confirmation, summary-level sharing |
| **Big-vendor encroachment** | Fabric, Littlebird, Notion AI, and Feishu Minutes could add an "academic" template at any time | Medium | [Fact] Fabric/Littlebird already exist | Differentiate on workflow composition and trust design, not on a single feature |
| **ASR quality** | Mixed Chinese-English speech, jargon, in-person far-field recording | Medium | [Fact] The existence of SEAME/MERaLiON research shows the difficulty; [Inference] | At the demo stage, use text minutes / shorthand notes as input, with transcription as an option |
| **Confirmation bias** | The owner is themselves a target user and may easily "treat themselves as the user" | Medium | [Inference] | Interview labs from at least 3 different disciplines and 2 countries, and include PIs |

---

## 15. Implications for BriefPilot v2 (for use in 03_positioning)

1. **[Inference] Recommended wedge scenario**: **"A two-way commitment ledger after supervisor 1-on-1s"**. The input is a recording, shorthand notes, or handwritten minutes; the output is "decisions / my commitments / supervisor's commitments / hypotheses to verify / papers mentioned", which enter the ledger after human confirmation. Before the next meeting, it automatically generates "unclosed items from last time + verbatim quotes", and it produces a weekly report draft with one click each week.
2. **[Inference] Alignment with the existing PRD**: The three existing principles, "leave missing fields blank rather than guess", "generate formal tasks only after confirmation", and "answer with citations", are **more persuasive** in a research setting. They don't need to be overturned; only the schema needs to change (adding commitment direction, strength, and linked objects), along with the scenario (from "team meetings" to "1-on-1 + group meetings").
3. **[Inference] Interview narrative**: ~~"Feishu Minutes solves 'what was said in this meeting'; I solve 'what did we promise each other over the past 10 meetings, and did we follow through'.~~ (Corrected at the time of writing: this line would be directly rebutted. Feishu's "meeting digest" already summarizes a week of action items, Fellow already brings unfinished items back before meetings, and Littlebird already compares whether commitments were fulfilled. Revised to: "They can tell you 'did the thing promised last time get done'; what I record are commitments **confirmed by both student and supervisor**, including what **the supervisor owes the student**, and after something is 'done' I also record 'what the result showed'.") "I chose research labs because institutions require records to be kept, AI meeting bots are restricted by universities, and there is a lot of in-person and mixed Chinese-English speech. These factors make general-purpose tools fail here, and I can dogfood it weekly myself."
4. **[Assumption] Six questions that must be validated through interviews** (recommended for the research plan):
   - H1: Students have at least one experience per week of "can't remember what the supervisor specifically asked for last time" (frequency).
   - H2: Supervisors' unfulfilled commitments to students are a common pain point that students are reluctant to chase (whether two-way commitment is a real pain).
   - H3: Students are willing to spend ≤ 1 minute after a meeting confirming an AI draft (adoption cost threshold).
   - H4: PIs are willing to view a "group-wide commitment board" but not the raw transcripts (sharing granularity).
   - H5: The proportion of supervisors who consent to being recorded (feasibility of the input method).
   - H6: The highest unit price a lab would pay and the payment path (individual / grant funds / university).

---

## 16. Items Not Covered in This Round

- Original Reddit r/PhD and r/GradSchool posts (the tool cannot access reddit.com).
- Full text of original Zhihu posts (403); only titles and secondhand paraphrases are available.
- Original posts from academic circles on Twitter/X and Bluesky; a systematic HN Show HN search; academic papers on "LLMs for summarizing research meetings" (search quota exhausted).
- The direction of the supervision-hours and satisfaction figures in the original Nature 2025 doctoral student survey (secondary sources contradict each other). (Partially clarified at the time of writing: a Springer Nature community response states that 69% corresponds to "meets their supervisor for more than 1 hour per week" and 82% to "feels supported"; the original Nature article has still not been opened.)
- (Added at the time of writing) The original UW CS handbook (login required); UK supervision record systems (Haplo redirect, LJMU 404) — see U3 §6.2.
- The target university's specific IT policy on AI meeting transcription.
- Original policy pages for Harvard, St Andrews, and others (403 or login required); currently relying on search snippets.

---
## Source List

1. GradCafe, "Note-taking during advisor meetings" (2018) — https://forum.thegradcafe.com/topic/108546-note-taking-during-advisor-meetings
2. UW CS PhD Handbook, Advising guide: building a relationship (search snippet; original page requires login; retried at the time of writing: 301 redirect to internal.cs.washington.edu, then SSO required; to be verified) — https://www.cs.washington.edu/academics/phd/handbook/advising-guide/building-a-relationship
3. Loyola Graduate School Survival Guide (search snippet) — https://www.luc.edu/media/lucedu/history/graduateprogramhandbook/adviceonbeingasuccessfulgraduatestudent/Graduate%20School%20Survival%20Guide.pdf
4. HKU AAS, Making your advising meeting impactful (search snippet) — https://aas.hku.hk/adv_news/etips-apr2021/
5. Queen's University 2009 BOF slides (search snippet) — https://research.cs.queensu.ca/home/audrey/papers/GHC2009.BOFslides.pdf
6. Soft Academia, "Dear bewildered and burnt out" (search snippet) — https://softacademia.substack.com/p/dear-bewildered-and-burnt-out
7. Progress Meeting with Advisor: A Guide for Students (GitHub Gist) — https://gist.github.com/weitsang/5d95b790d5d58d2a5ccb291dd215e554
8. UC San Diego Privacy, AI Guidelines — https://privacy.ucsd.edu/ai-guidelines/
9. Harvard HUIT, Guidance on AI meeting assistants (2025-02, search snippet, original page returns 403) — https://www.huit.harvard.edu/news/guidance-ai-meeting-assistants-data-privacy-principles
10. Mississippi State, Blocks Third Party AI Services (search snippet) — https://servicedesk.msstate.edu/TDClient/45/Portal/KB/ArticleDet?ID=2129
11. UNM, AI Meeting Capture (search snippet) — https://airesources.unm.edu/ai-guidance/ai-meeting-capture.html
12. University of Utah AI blog (search snippet) — https://ai.utah.edu/blog
13. CIHR, Policy on AI in peer review meetings (search snippet) — https://cihr-cri.gc.ca/e/54129.html
14. CU Anschutz ISIC, Approved AI transcription tools (search snippet) — https://isic.cuanschutz.edu/news-initiatives/ISIC-News-approved-ai-transcription-tools-and-best-practices
15. University of Sheffield, recording supervisory meetings (search snippet; PDF could not be parsed) — https://sheffield.ac.uk/media/29592/download
16. Newcastle University, PGR meetings (search snippet) — https://www.ncl.ac.uk/student-progress/pgr/activities/meetings ; MyProgress recording meetings — https://www.ncl.ac.uk/learning-and-teaching/digital-technologies/my-progress/recordingmeetings/
17. University of Liverpool, PGR toolbox supervisory meetings (search snippet, original page returns 404) — https://liverpool.ac.uk/pgr-development/toolbox/supervisory-meetings
18. Prograds (UBC) — https://cutler.portfolio.arts.ubc.ca/activities/prograds-the-grad-student-progress-app/
19. McGill, Supervision & Progress Tracking (search snippet) — https://www.mcgill.ca/ahcs/node/42183
20. China Agricultural University Functional Dairy Laboratory, "Graduate Work Reporting and Group Meeting Management Rules" — https://fdl.cau.edu.cn/col/col41806/index.html
21. "An Analysis of the Educational Function of the 'Group Meeting'," *Research on Graduate Education* 2022(2):52–58 — https://html.rhhz.net/yjyjyyj/html/20220208.htm
22. Editage, "How Afraid Are Today's Graduate Students of Group Meetings?" — https://www.editage.cn/sci-writing/3669/
23. Zhihu, "How do you report at a graduate group meeting when you have made no progress?" (title only) — https://www.zhihu.com/question/268901881
24. Zhihu, "How can you give a group meeting that satisfies your advisor when your project has made no progress?" (title only) — https://www.zhihu.com/question/491712440
25. The Paper (Pengpai), "With No Research Progress, How Can You Openly Coast Through a Group Meeting?" (title only) — https://m.thepaper.cn/newsDetail_forward_20351898
26. Nankai University, research group lab management rules (search snippet) — https://panglab.nankai.edu.cn/info/1039/1102.htm
27. "Ten simple rules for productive lab meetings", PLoS Comput Biol 2021;17(5):e1008953 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8158921/
28. Endy Lab, Making group meetings more effective (OpenWetWare) — https://openwetware.org/wiki/Endy:Making_group_meetings_more_effective
29. Nature 2025-10-23, "What makes PhD students happy? Good supervision" (secondhand paraphrase, figures to be verified) — https://graduate.ucf.edu/wp-content/uploads/sites/8/2025/10/Nature_mentoring-1.pdf
30. Springer Nature Communities, A response to "What makes PhD students happy?" (original page opened at the time of writing) — https://communities.springernature.com/posts/a-response-to-what-makes-phd-students-happy-good-supervision
31. HEPI, PhD Life: The UK student experience (search snippet) — https://www.hepi.ac.uk/reports/phd-life-the-uk-student-experience/
32. Warwick MIBTP supervisor self-description pages (three supervisors, search snippet) — https://warwick.ac.uk/fac/cross_fac/mibtp/phd/supervisors/mgreenhalgh/
33. Fischer Lab, Evergreen (search snippet) — https://sites.evergreen.edu/fischerlab/?p=72
34. Weekly Reports (university data science group page) — https://data-science-group.github.io/weekly-report.html
35. Supervisor Meeting Brief (Chrome extension) — https://chromeboard.com/extension/supervisor-meeting-brief-fmibimgfmoaogdajeoeedledhejppgll
36. phd-weekly-review skill — https://www.skills.sh/a-green-hand-jack/phd-skills/phd-weekly-review
37. Littlebird for graduate students — https://littlebird.ai/for/graduate-students ; for researchers — https://littlebird.ai/for/researchers
38. Fabric for Academic Labs — https://fabric.so/teams/academic-labs ; Fabric meeting notes — https://fabric.so/for-your/meeting-notes
39. H-tr/PhD-Plan — https://github.com/H-tr/PhD-Plan
40. Otter student discount (third-party roundup) — https://www.meetjamie.ai/blog/otter-ai-pricing ; back-to-school promotion — https://www.01net.it/back-to-school-half-the-price-otter-ai-offers-students-50-off-to-turn-lectures-into-study-guides-quizzes-and-exam-prep/
41. Notion for Education (official help page and mirror) — https://www.notion.com/help/notion-for-education
42. University of Idaho 2022 willingness-to-pay study on APCs (EBLIP) — https://id.erudit.org/iderudit/1088074ar ; Mass General Brigham Research Software — https://rc.partners.org/news-events/announcements/research-software-annual-interest-survey
43. SEAME (Interspeech 2010) — https://www.isca-archive.org/interspeech_2010/lyu10_interspeech.html ; MERaLiON-3-3B-ASR — https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR
44. The target university's Position on the Use of GAI in Research — (university page; link removed) ; report on the target university's free Google AI tools (title only) — https://www.dpexnetwork.org/news/view/BAV66qk5bNgVeLawfVQpmH
45. Nature 2021, "Digital secrets of successful lab management" (verified via Competitor 03) — https://www.nature.com/articles/d41586-021-01752-y
46. Primary sources from Competitor 03: Duke JACMP 2025 (PMC12401938), Durrant Lab, Whitaker Lab — https://pmc.ncbi.nlm.nih.gov/articles/PMC12401938 ; https://durrantlab.pitt.edu/durrant-lab-project-management-system/ ; Zhaopin job posting for a research-group secretary (search snippet) — https://m-pre.zhaopin.com/jobs/CC315171120J40792855103.htm

---

**Added in Round 2 revision (accessed at the time of writing)**
47. Fellow Action Items — https://fellow.ai/features/action-items
48. Fellow × GitHub — https://fellow.ai/integrations/github
49. Littlebird Pricing — https://littlebird.ai/pricing ; Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
50. Feishu AI meeting minutes (meeting quick-view, enterprise information recognition) — https://www.feishu.cn/content/article/7577317993749269689 ; MIT advisor policy (replaces the UW citation; cited from the original text already read in U3) — https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf
## Confidence Notes for This Document

- **High confidence (original page opened and checked)**: UCSD AI guidelines, China Agricultural University lab regulations, Hu Yonghong et al. 2022 paper, PLoS CB Ten simple rules, Endy Lab page, GradCafe post, Beheshti weekly report requirements, weitsang gist, Prograds page, content of the Fabric / Littlebird / Supervisor Meeting Brief / phd-weekly-review / PhD-Plan pages (**the page content is accurate, but the product capabilities described there are the vendors' own claims**), Enago article.
- **Medium confidence (search snippets only; original page returned 403/404/required login)**: Harvard, Mississippi State, UNM, Utah, CIHR, CU Anschutz, Sheffield, Newcastle, Liverpool, UW CS, Loyola, HKU, Queen's, Warwick, Fischer Lab, Nankai research group, the target university's research GAI stance, Otter student pricing.
- **(Added at the time of writing) Corrected conclusions**: §0 item 2 (the UW evidence is downgraded to [Summary·to be verified]), §0 item 3 ("cross-meeting commitment continuity is unmet" does not hold; replaced with three properties), §15 item 3 interview narrative.
- **Low confidence / to be verified**: the direction of the numbers for "supervision time × satisfaction" in the 2025 Nature survey (secondary sources contradict each other; the response article was opened, the original was not); the 63% figure from HEPI; the terms of Otter's 50%-off promotion; the target university's AI meeting tool policy (not found); details of the Zhaopin job posting.
- **Pure inference / assumption**: all personas, the one-week scenarios, the JTBD wording, the pain-point scoring table (the researcher's subjective judgment, not measurement), the two insights "two-way commitment" and "power asymmetry leads to selective sharing" (proposed in this document, **no direct evidence; these are the parts most in need of interview validation**), and the willingness-to-pay assessment.
- **Systematic bias warnings**: (1) Student voices lack original Reddit and Zhihu posts, so the evidence for emotional intensity is weak; (2) labs with public regulations skew toward "well-run groups," so real-world disorder may be higher; (3) the researcher belongs to this segment, which creates a risk of self-projection.

---

## Revision Log (Round 2)

> Based on `01_market-research/06_research_integrity_review.md` §1 supplementary checks, §2 (W1, W6, W9), §6 (C1, C3, C5), §7 (evidence labels), §9 P0-4. In this round, I retried the UW CS handbook (still requires login), the original Nature article (redirects to login), and the UCF reprint PDF (only metadata could be retrieved), and opened the Springer Nature community response article, two Fellow pages, two Littlebird pages, and the Feishu smart minutes page.

| # | Location | Change | Basis |
|---|---|---|---|
| 1 | frontmatter, reading notes | status marked as revised; sources_count 46 → 50; added explanation of the [Summary] label | 06 §7 |
| 2 | §0 item 2 | "UW CS PhD handbook verbatim [Fact]" struck through and changed to [Summary·to be verified]; recommend using the MIT Cahoy policy, whose original text has been read, instead; the Prograds portion keeps [Fact] | 06 W1, C1 |
| 3 | §0 item 3 | "What is truly unmet is cross-meeting commitment continuity" struck through; added evidence from Fellow, Littlebird, and Feishu meeting express digest; rewritten as three properties: "two-way, consensus, outcome semantics" | 06 C3, V6, V13; 05 K6 |
| 4 | §0 item 5 | added Littlebird Team plan and Fellow as a general-purpose alternative | 06 V1, V3 |
| 5 | §3.1–§3.4, §4.2, §6.3 | 12 entries of "[Fact] (search snippet)" changed to [Summary] or [Summary·to be verified]: Queen's, UW CS, Loyola, HKU, Soft Academia, Zhihu group meeting titles, Newcastle/Liverpool, Sheffield, Harvard, Mississippi State/UNM/Utah/CIHR; Beheshti/Fischer/Warwick and China Agricultural University/Zhaopin split into separately labeled [Fact]/[Summary] | 06 §7, W9 |
| 6 | §4.1 table | UW CS row [Fact] → [Summary·to be verified]; Nature 2025 row "69% vs. 82%" struck through, added the original sentence from the Springer Nature response article (82% corresponds to "feeling supported"), whole row downgraded to [Summary·to be verified] | 06 W6, C5; response article opened this round |
| 7 | §7 Persona B | added [Summary·to be verified] to the UW evidence | 06 C1 |
| 8 | §11 table | "General-purpose meeting tools do not track action items across meetings" struck through; added explanation to the summary paragraph | 06 C3 |
| 9 | §12 table | Littlebird "personal tool" struck through, added Team plan | 06 V3 |
| 10 | §15 item 3 | original interview narrative sentence struck through and rewritten (the original sentence would be directly refuted by Feishu meeting express digest, Fellow, and Littlebird) | 06 C3 |
| 11 | §16, sources, confidence notes | added partial clarification of Nature and the UW retry result; added sources 47–50 (all accessed at the time of writing) | — |

**Not changed, left for later**: the statement in the §2 meeting overview table that "the 2025 Nature survey shows about half of students spend <1 hour per week (secondary source, to be verified)" was already marked to be verified and was not changed further; the Otter student price in §13 (third-party aggregation) was not rechecked; the "high confidence" classification in the §1 evidence structure table was not recalculated.
