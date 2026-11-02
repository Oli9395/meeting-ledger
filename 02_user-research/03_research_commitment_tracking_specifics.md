---
title: "User Research 03: The Special Nature of Commitment Tracking and Knowledge Recall in Research Settings (with a Draft Requirements Spec)"
status: draft (revised in place, Round 2, following review 06)
sources_count: 55
sources_count_method: Number of unique URLs in the sources section (recounted at the close of at the time of writing; original value 46)
---

# User Research 03: Why "Commitments / Hypotheses / Decisions / Results" in Research Discussions Are Not Enterprise Action Items

> **Reading notes**
> - Labeling rules: **[Fact]** can be checked against a source; **[Inference]** is reasonably derived from multiple facts but has no direct evidence; **[Assumption]** awaits interviews or experiments to verify.
> - Every source is marked with its verification level: **read in full** (the original page or PDF body was opened); **search snippet** (only the search-engine snippet was seen, the original was not opened, uniformly marked "to be verified"); **carried over** (cited from this project's completed [01_market-research/03_competitors_research_lab_tools.md](../01_market-research/03_competitors_research_lab_tools.md), which has already been verified).
> - **Research method and limitations**: This document ran about 30 searches in Chinese and English and fetched about 25 original pages; 3 of the PDFs were parsed locally in full text (Gautam et al. FAccT'26, MIT Cahoy advisor policy, the ar5iv version of Liu et al. CHI'20). **The shared search quota for the whole round (200 searches) ran out during writing**, so the following were not covered: Reddit (the crawler was refused by the site, so the original posts could not be retrieved), Twitter/X, a systematic ACM DL search for "lab meeting" papers, surveys of ELN adoption in ML/computational labs, and the official documentation for the Otter/Fireflies action-item fields (the official pages returned 403 or 404). See Section 10 for details.
> - The VLA (vision-language-action model) example sentences in this document are **fictional examples made up for illustration**, not real group meeting records.
> - **(Added in Round 2)** **[Summary]** = only the search snippet was seen; the original page was not opened. The original "[摘要·待核实]" label has been unified to **[Summary·to be verified]**, and "[摘要·证据弱]" to **[Summary·weak evidence]**; they are no longer listed alongside [Fact]. Claims that were overturned are kept as ~~strikethrough~~; changes are listed in "Revision log (Round 2)" at the end.

---

## 0. The Answer First

1. **[Inference, medium-to-strong evidence] The core output of a research discussion is a causal network of "hypothesis → experiment commitment → result → evidence → decision", whereas the core output of an enterprise meeting is a "who / does what / by when" to-do list.** This is a structural difference, not a difference of degree: the completion semantics of an enterprise action item are binary (done / not done), while the completion semantics of a research commitment have at least five values: supported, refuted, inconclusive, abandoned, superseded. Regardless of "whether it was done", **the result itself becomes input to the next round of discussion**. The action-item templates of general-purpose tools (Feishu: action item / owner / priority / deadline) cannot hold "which hypothesis this experiment was meant to test, what the result was, and where the evidence is".
2. **[Fact] Researchers' after-the-fact recall of "why we chose this back then" is unreliable.** The CHI 2020 interview study (Liu, Althoff, Heer; 9 researchers, 190 decision rationales) found that many decision points are made implicitly; scripts do not preserve the full exploration history; and the authors explicitly warn that **hindsight bias** may lead researchers to misremember after-the-fact explanations as prior hypotheses. This directly supports "decision recall" as a real problem that memory cannot solve.
3. ~~**[Fact]**~~ **[Fact] (MIT) / [Summary·to be verified] (UW, UK supervision systems)** **"The advisor can't remember what was said last time" is taken for granted at the institutional level.** The UW CS PhD handbook tells students directly that "advisors won't remember what was discussed last time, don't be upset" (search snippet, to be verified); a written advisor policy from an MIT professor requires students to email their notes and action items to everyone after the meeting and to review them item by item at the next meeting (read in full); several UK universities have formal "supervision meeting record" systems, written by the student and confirmed by the advisor (~~partly read~~ correction: §6.2 itself marks this as a search snippet; the Haplo page returned a 301 redirect to the Cayuse help center home page, the LJMU PDF returned 404, and the Wolverhampton PDF came back empty in this round's fetch, so **not a single one had its original opened**). In other words, **the manual workflow of "student records → advisor confirms → reviewed next time" has already been institutionalized, ~~it just doesn't have tool support yet.~~** (correction: this sentence contradicts §6.2. This document itself lists supervision record systems such as Haplo PhD Manager and LJMU eDoc, and those are tools. The accurate statement is: **administrative record systems exist (form-based, no AI, evidence is [Summary·to be verified]), but they are not connected to meeting content**: they do not draft commitments from the meeting, do not carry the source of the original words, and do not link to experiment results. Among general-purpose tools, Fellow brings unfinished items back before a meeting and Littlebird tracks personal commitments, but neither page shows an "advisor confirms" step. See 06 C2, W8.)
4. **[Fact] Researchers' attitude toward AI is "you can help me organize, but you can't judge for me", and they are broadly worried about data leakage.** The Wiley 2025 survey (2,430 people): privacy/security concerns rose from 47% to 58%, and hallucination concerns rose from 51% to 64%. OUP 2024 (2,300+ people): only 8% trust AI companies not to use their research data without permission. In the FAccT'26 think-aloud study (15 people), 10 limited AI to "organizational, peripheral" tasks, and the uses mentioned in the original text include "tracking decision points" and "recording intermediate reasoning that would otherwise be lost". **This closely matches BriefPilot's design philosophy of "sourced, human-confirmed, never making judgments for the user".**
5. **[Inference] The strongest direction for differentiating features is not "more accurate transcription" but "commitment–result closure" and "sourced decision recall".** Closure means: for an experiment promised last time, what the result is this time and where the evidence link is; recall means: when writing a paper or replying to reviewers, being able to ask "why did we choose 8 for the action chunk" and get the original words from that meeting and the corresponding experiment run. The strongest potential competitor, Fabric, already claims a "decision log" on its marketing page (read in full), so the differentiator has to rest on **the completion semantics of closure**, **evidence links to experiment artifacts**, and **local/private deployment**, rather than on "having a decision log" itself. (Added at the time of writing: the generic version of "commitment–result closure" is already half-built by others — Littlebird's promise tracker compares commitments against "the email that went out, the document that shipped" and outputs Kept / In progress / Needs a note; Fellow syncs issue status bidirectionally with GitHub via Zapier. Sources: https://littlebird.ai/routines/promise-tracker , https://fellow.ai/integrations/github , accessed at the time of writing. So "closure" itself is not the differentiator; **the five-valued research semantics + W&B/config evidence** is, and the five-valued semantics remains this document's [Inference].)
6. **[Fact, negative finding] Within the available search budget, no CHI/CSCW paper specifically studying "lab meeting → commitment tracking" was found.** Related research falls into four categories: data-analysis decision paths (CHI'20), how researchers manage ideas (C&C'22), exploration history in computational notebooks (CHI'18), and design-rationale capture in design meetings (MIT 2002, etc.). A CSCW 2017 survey notes that only 26 papers in the CSCW literature explicitly discuss project management, and most focus on IT development. **This is a sign of an academic gap, but it cannot prove that none exists; a systematic ACM DL search is needed to confirm.**

---
## 1. Why this question determines the differentiation direction

The objection from a client or interviewer is: "Meeting-to-task is already done by Feishu Minutes, Otter, and Fireflies." If BriefPilot only swaps the setting from "company" to "lab" and the output is still "who / what / when", the objection holds. Research users can simply use Feishu Minutes, which already exports action items as an Excel sheet with "action item, owner, priority, due date", converts them into Feishu tasks in one click, and syncs the completion status back to the minutes ([Fact, full text read] two articles on the Feishu website).

So the question that really needs answering is: **is what research discussions produce structurally different, at the data level, from an enterprise action item?** If it is, the differentiation lies in the "object model". A competitor would have to change its schema and workflow to follow, and adding a template would not close the gap. If it is not, research is just a re-skinned marketing segment. This document concludes the former, but the strength of evidence varies, as explained item by item below.

---

## 2. A typology of research-discussion outputs (Research Question 1)

### 2.1 Academic evidence: researchers themselves divide "ideas" into different types

- **[Fact, abstract page read]** Inie, Frich Pedersen, and Dalsgaard (C&C '22, DOI 10.1145/3527927.3532813) ran a qualitative survey with 51 participants and in-depth interviews with 18, and distinguished **4 types** of research ideas: research questions or problems, methods, hypotheses or anti-hypotheses, and theories. They also summarized the attributes of good ideas and identified where tools could support idea management. Source: https://researcher.itu.dk/en/publications/how-researchers-manage-ideas/
- **[Fact, full text read]** Liu et al. (CHI 2020) grouped researchers' decision rationales into 6 categories: methodology, prior work (mentioned by all 9 participants), data constraints (8/9), expertise (8/9), communication (6/9), and sensitivity (4/9). They also grouped the motivations for "trying alternative paths" into opportunistic (7/9), contingency (5/9), robustness (4/9), and systematic (3/9). Source: https://ar5iv.arxiv.org/html/1910.13602
- **[Carried over]** The fields of an academic minutes template are "experiment ID / hypothesis / steps / results / interpretation / open questions" and "next experiment: goal / success criteria / dependencies" (see competitor research 03, §5).

**Why it matters**: this shows that "hypotheses", "method choices", and "decision rationales" are **first-class objects** in researchers' mental models, not notes fields on a task.

### 2.2 Typology table: ten kinds of output and their counterparts in enterprise meetings

| # | Research output | Example (fictional VLA group meeting) | Counterpart in enterprise meetings? | Can a generic action item template express it? | Basis |
|---|---|---|---|---|---|
| 1 | **Experiment commitment** (run an experiment, run a baseline, add an ablation) | "Next week, run the OpenVLA baseline on LIBERO with 3 seeds" | Yes (a task) | **Partly**: who and when can be written, but "what it is meant to verify", "what the success criteria are", and "where the results go" cannot | [Inference] combining Feishu fields (full text read) with academic templates (carried over) |
| 2 | **Reading commitment** | "Go read the flow matching part of the π0 paper" | Weak counterpart ("research the competitors") | Can be written, but the output is "understanding/conclusions", not a deliverable | [Inference] |
| 3 | **Hypothesis** | "We suspect that too short an action chunk causes jitter" | **Essentially none** (the closest enterprise notion is a "product hypothesis", but it rarely appears in weekly meeting minutes) | **No**: it has no owner and no due date; it is a proposition awaiting testing | [Fact] Inie et al. list hypotheses as a separate type; [Inference] no enterprise counterpart |
| 4 | **Decision** (including abandoning a method) | "Drop the diffusion head and switch to flow matching" | Yes ("decided to ship plan A") | **Cannot be an action item**; Feishu has "meeting conclusions", but with no structure for the decision rationale or the rejected alternatives | [Fact] Feishu only mentions "meeting conclusions" (full text read) |
| 5 | **Open question** | "Why is it good in sim but poor on the real robot? Nobody knows yet" | Weak counterpart ("pending items") | No: it has no owner and may persist for months | [Inference] |
| 6 | **Parameter/config change** | "Change lr from 1e-4 to 3e-5, batch 256" | **Essentially none** (the closest is an engineering change, but that lives in Git/Jira, not in meeting minutes) | No: it needs links to the config, commit, and run | [Inference] corresponds to Gundersen's three factors of "experiment / data / method" |
| 7 | **Advisor suggestion** | "The advisor suggests not doing the real robot yet and stabilizing the sim metrics first" | Yes ("boss's opinion") | Cannot distinguish a "suggestion" from an "instruction"; the power asymmetry makes it hard for students to follow up afterward | [Fact] the "advisor changes their mind" frustration documented on Substack and Degree Doctor; [Inference] |
| 8 | **Reviewer/committee comment** | "R2 asks for an additional real-world experiment" | Weak counterpart (customer feedback) | Can be split into tasks, but loses the mapping "original comment → response → corresponding experiment" | [Carried over] Overleaf comment threads, Granola academic scenarios; [Inference] |
| 9 | **Deadline** | "A complete draft is needed 4 weeks before the CoRL deadline" | Yes (a milestone) | Can be written, but a research deadline is an externally fixed submission date, and every commitment must be scheduled backward from it | [Fact] Cahoy: "review the outline of a 10-page document 4 weeks ahead, and the full draft 2 weeks ahead" |
| 10 | **Result/observation** ("the loss didn't go down in that last experiment") | "Seed 2 diverged; the other two were normal" | Weak counterpart ("progress report") | **No**: it is a "result backfill" onto an existing commitment, not a new task | [Inference] |

**Summary [Inference]**: of the ten types, only 1, 2, and 9 can be reasonably well expressed by the "who / what / when" template. The five types 3, 4, 5, 6, and 10 either have no counterpart in enterprise meeting minutes or would not be treated there as structured objects. **This is where the v1 PRD's `title / owner / due_date` schema cannot fit research scenarios.**

---
## 3. The Iterative Structure of Research: Commitments Must Be Linked to Results and Evidence (Research Question 2)

### 3.1 What the Loop Looks Like

The basic research loop is "discuss → commit → experiment → result → discuss → new commitment." The most common question in it is: "**Did we ever try that idea from last week? How did it turn out?**"

- **[Fact, original read]** The written advising policy of Kerri Cahoy (MIT AeroAstro, Fall 2019) states that at the weekly lunch group meeting, students write up weekly progress as key points on a single slide. At research progress meetings, students bring a short agenda, "take notes and action items during the meeting, and email them to all attendees afterward," and "**review these items from the previous meeting at the next meeting**." Research projects in that lab typically involve 2–6 people. Source: https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf
- **[Carried over]** Imperial College's supervision agenda recommends opening with "outcomes since the last meeting."
- **[Fact, original read]** Liu et al. found that researchers often "try multiple analysis paths and then choose the one that leads to the desired result," and "usually report only the desired results" (selective reporting: 52 instances in total, involving 7 of 9 participants).

### 3.2 Why "Check Off as Done" Is Wrong for Research

| Dimension | Enterprise task | Research commitment |
|---|---|---|
| Completion semantics | done / not done | **supported / refuted / inconclusive / abandoned / superseded**, plus "done, but the result shows the hypothesis itself was the wrong question" |
| Value after completion | The task ends and its information value declines | **The result is input to the next round of discussion**; failed results are equally valuable ("ruled out") |
| Form of evidence | Delivery links (PRs, documents) | W&B/TensorBoard runs, configs, Git commits, figures, logs, Overleaf sections |
| Relationships | Tasks relate through dependencies | A commitment has a "tests" relationship to a **hypothesis** and a "basis" relationship to a **decision** |

**[Inference]** If a system supports only check-off completion, the most valuable information ("ran it, H2 was rejected, so we decided to drop method A") ends up scattered across oral updates at the next meeting and is lost again. This is exactly the kind of information that PI Bahlai meant in Nature 2021 when saying "Slack is not good for recording anything for posterity" and "long-term goals keep falling through the cracks" (carried over).

**[Assumption H-A]** Students are willing to add a one-line result and an evidence link when marking a commitment "complete" (about 30 seconds of effort), provided that the system automatically lists "commitments awaiting results" before the next meeting. To be validated through interviews and dogfooding.

---

## 4. Links Between Reproducibility, Experiment Records (ELNs), and Paper Writing (Research Question 3)

### 4.1 Factual Basis

- **[Fact, abstract page read]** Gundersen & Kjensmo (AAAI 2018) surveyed 400 papers from IJCAI/AAAI and divided the variables needed for reproduction into three factors: experiment, data, and method. **No paper documented all variables, and each factor had only 20%–30% of its variables documented.** Both hypotheses ("AI research documentation is insufficient for reproduction" and "documentation practice improves over time") were supported. Source: https://mlanthology.org/aaai/2018/gundersen2018aaai-state
- **[Fact, secondary]** Baker's 2016 survey in Nature (about 1,576 respondents): more than 70% had tried and failed to reproduce another researcher's experiments, and more than half had failed to reproduce their own; 52% thought there was a "significant crisis"; selective reporting and publication pressure were listed among the main causes. The share failing to reproduce their own experiments comes from a secondary summary and is **to be verified against the original** (the Nature original requires login). Sources: https://www.nature.com/articles/533452a ; https://reproduciblebiomodels.org/1500-scientists-lift-the-lid-on-reproducibility/
- **[Carried over]** Kanza et al. 2017: ELN adoption in academia is limited; paper notebooks remain the main recording method because they are easy to use, cheap, and need no training; some people who tried ELNs went back to Word. ELN vendors (eLabFTW, SciNote, LabArchives, Labguru, Benchling) all **lack a "meeting" object**.
- **[Fact, original read]** W&B Reports can organize runs, embed visualizations, and "describe findings," and support export as a LaTeX zip or PDF (official documentation). A W&B community blog post describes a workflow for importing the LaTeX zip into Overleaf (search summary, to be verified). Sources: https://docs.coreweave.com/products/wandb/reports.md ; https://wandb.ai/andrea0/note_taking/reports/A-Snappy-TeX-Workflow-for-Reports--VmlldzozNTEyNzY1
- **[Fact, original read]** Overleaf Cloud's Git integration is a **paid feature**; it is available in Server Pro 4.0 and above, but is off by default. Source: https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git
- **[Summary · to be verified]** In Zhihu Q&A threads such as "How do you keep experiment records?", some views hold that many people record only parameters and not "why this experiment was run"; others fill in records afterward from memory and end up missing conditions that were changed ad hoc. Sources: https://www.zhihu.com/question/66730795 ; https://www.zhihu.com/question/36506395 ; https://user.guancha.cn/main/content?id=195206
### 4.2 Conclusions and Implications for BriefPilot

- **[Inference]** In computational labs such as ML/robotics, "experiment records" are already scattered across W&B/TensorBoard (numerical results), Git (code and configs), and Overleaf (conclusions). **What is missing is not the records themselves, but the context of "why this run was done"**, and that context is produced precisely in the group meeting. Gundersen's finding that "20%–30% of variables are recorded" refers to the final record in the paper; for the stretch from meeting decision to paper, no tool is responsible.
- **[Inference] BriefPilot should not be an ELN**, and it should not compete with W&B on experiment tracking. It should act as a "context layer": attaching the hypotheses, decisions, and commitments from meetings to existing artifacts via **links** (run URL, commit hash, config path, Overleaf section).
- **[Assumption H-B]** Graduate students in computational labs are willing to paste a run link or commit hash into a committed result, but are unwilling to learn a new ELN for it. To be validated.

---

## 5. The "Decision Traceback" Need: When Writing a Paper, Recalling "Why We Chose This Setting" (Research Question 4)

### 5.1 Evidence

- **[Fact, original read]** Liu et al. (CHI'20) have three findings. First, many decision points **are not recognized as decisions**: researchers implicitly pick an option, especially in data processing and inference steps. Second, "not all scripts retain a complete history". Third, the authors warn that **hindsight bias may lead researchers to misremember post-hoc explanations as prior hypotheses**. Their proposed design directions include: combining decision graphs with provenance tracking to "provide some degree of automated recording"; writing and discussing the decision graph before analysis; and using multiverse analysis tools to aggregate multiple paths. Sources: https://ar5iv.arxiv.org/html/1910.13602 ; https://idl.uw.edu/papers/analysis-decision-points
- **[Summary · to be verified]** The classic conclusion of design rationale research is that the reasons behind decisions mostly go unrecorded, and that meeting discussions are the main place where rationale is lost. Hammond, Gajos, Davis, and Shrobe of MIT (2002) built an agent system that records and indexes software design meetings, and pointed out that what is typically omitted is "why this solution was adopted". A WICSA 1999 paper discusses the tension that "capturing during a meeting interrupts the work, while adding notes afterward incurs extra cost". Jane Burge of Colorado College has an NSF project studying the capture and retrieval of key decisions across multiple meetings. Sources: https://groups.csail.mit.edu/mug/pubs/Hammond2002Agent.pdf ; https://icsa-conferences.org/series/WICSA/1999/final/richter.pdf ; https://sites.coloradocollege.edu/jburge/research ; https://risk.designsociety.org/download-publication/39797/How+explicit+are+we+in+a+design+meeting%3A+Investigation+on+meeting+knowledge+structuring+with+design+rationale
- **[Fact, original read, marketing]** Fabric's academic labs page claims: the decision log captures the analysis and method choices that come up in meetings and channels, and "when a reviewer asks about a method, the answer is already on record with its context"; answers can link to "the exact page or timestamp"; a weekly summary is generated for the PI; and "your lab's data will never be used to train AI models". **No customer case studies, no independent verification.** Source: https://fabric.so/teams/academic-labs

### 5.2 Typical Trigger Scenarios for Decision Traceback [Inference]

1. **Writing the methods and experimental setup sections**: "Why 3 seeds instead of 5?" "Why report on LIBERO-Long rather than CALVIN?"
2. **Responding to reviewer comments**: a reviewer asks "why was there no comparison with X", and you need to find the original words and reasoning behind the decision not to compare with X (e.g., "X is not open source").
3. **Thesis writing and handover within the group**: a new member or the next cohort of students takes over the project and asks "why is this config set this way?"
4. **The advisor's own recall**: "Why did we abandon the diffusion head back then?"

**Why this is a natural extension of BriefPilot**: the core capability of v1 is "Q&A with provenance, plus refusal to answer". Decision traceback **changes the retrieval target of Q&A from "documents" to "decision records and their original meeting excerpts"**, and "with provenance, and refuse when there is no basis" matters especially here. Liu et al. have shown that people's post-hoc recall flatters itself, so the system **must not fill in reasons by inference**; it can only give the words said at the time, or state clearly that "there is no record".

### 5.3 A Design Caution from the Liu Study [Inference]

Since researchers selectively report and embellish after the fact, a tool that records "abandoned options and why" has positive value for ethics and research integrity (it supports complete reporting); but it may also make students uneasy ("my advisor can see all my failed attempts"). This leads to the permissions question in Section 6.

---

## 6. The Advisor's "Memory Burden" and Students' Complaints (Research Question 5)

### 6.1 Advisor Side

- **[Summary · to be verified]** The UW CS PhD handbook (the page now requires login), gist of the original: "If your advisor can't remember what you discussed last time, don't be upset"; "recording what was discussed is a must, and usually you take brief notes during the meeting"; it recommends sending an agenda before the meeting. Source: https://www.cs.washington.edu/academics/phd/handbook/advising-guide/building-a-relationship
- **[Fact, original read]** Cahoy's advising policy (see 3.1) writes "record + email + review at the next meeting" as a formal requirement for students, and notes that "we are a fairly large lab".
- **[Summary · to be verified]** A time-management guide for new faculty (from CMU/Cornell, hosted by UW ADVANCE) recommends: meeting with graduate students on a fixed weekly schedule, with one flexible slot reserved in addition; a meeting without an agenda and goals is a waste; and having students bring a notebook to meetings. Source: https://advance.washington.edu/sites/advance/files/8_Time%20Management%20for%20New%20Faculty.pdf
- **[Carried over]** Nature 2025 advisor survey: about half of PhD students meet their advisor for less than 1 hour per week (61% in the UK and 60% in Germany); satisfaction is 82% for students who meet more often and 69% for those who meet less.
- **[Inference]** The advisor's memory burden comes from "N students × several parallel experiment threads each × a short meeting every week or every two weeks". A PI supervising 8 students, each with 3 in-progress experiment commitments per week, has to keep the state of about 24 threads in their head (**this is illustrative arithmetic, not survey data**). The institutional solution is to outsource memory to students' post-meeting emails, but emails are unstructured and cannot answer "what did we decide last month?"
### 6.2 Student Side

- **[Fact, original read]** A student who wrote in to the Soft Academia column said that their supervisor assigned tasks without giving full information, then criticized them afterward for that missing information; the supervisor suggested revisions, later criticized those revisions, and finally reverted to the student's original draft without giving credit, "about three meetings per cycle"; "it feels like being trapped in a maze whose exit keeps moving." The column's advice: send your own written minutes after the meeting and ask the supervisor to confirm them; request a recording or transcript of the meeting, which can be supported by a letter from the disability services office. Source: https://softacademia.substack.com/p/dear-bewildered-and-burnt-out
- **[Fact, original read]** A Degree Doctor blog post explains "why supervisors keep changing their minds": the project itself is taking shape; the supervisor's role shifts from guiding content to guiding process; expectations are often implicit. It recommends clarifying on the spot during the meeting, and restating the next steps before leaving and asking the supervisor to confirm them. Source: https://www.thedegreedoctor.com/blog/phd-supervisor-changing-expectations-qualitative-research
- **[Summary · to be verified]** Guides from multiple universities (McMaster, Loyola, the QUB students' union, etc.) treat "the student takes meeting notes, sends an email summary afterward, and asks the supervisor to confirm whether the notes reflect the discussion" as standard practice. Sources: https://hsed.mcmaster.ca/wp-content/uploads/2022/04/supervisory_relationship.pdf ; https://www.luc.edu/media/lucedu/history/graduateprogramhandbook/adviceonbeingasuccessfulgraduatestudent/Graduate%20School%20Survival%20Guide.pdf ; https://q-su.org/studentvoice/studentsupervisorrelationshiptoolkit/SupervisionMeetings
- **[Summary · to be verified]** Some UK universities have formal supervision meeting record systems. Haplo PhD Manager supports viewing and downloading past supervision meeting records by academic year, and also lets a meeting be logged as "not held." LJMU's eDoc process has the student enter attendees, date, format, notes, and "agreed action points," which become the official record only after the main supervisor reviews and approves them (the guidance PDF now returns 404). Wolverhampton's record-keeping guidelines mention that international students may need such records to demonstrate academic engagement to UKVI. (Retried: the Haplo link redirects via 301 to the https://support.cayuse.com/hc/en-us home page, so the original content is not visible; the Wolverhampton PDF fetch returned empty; the LJMU PDF still returns 404. All three remain [Summary · to be verified]. **These systems are themselves "tools," which contradicts the original statement in §0, item 3, that "there is no tool support yet"; this has been corrected in §0.**) Sources: https://support.haplo.com/phd-manager/user-guidance/supervision-meetings ; https://www.wlv.ac.uk/media/departments/research/documents/Appendix-3---Guidelines-on-Records-of-Meetings-between-Supervisors-and-Students.pdf
- **[Summary · weak evidence]** On the Chinese side, only generic discussions were found on Zhihu, such as "supervisor-complaint gatherings," "how to present well at a group meeting when there is no progress," and "my PhD student hasn't contacted me proactively in half a month"; **no specific post about "the supervisor forgot what they said last time" was found**. Sources: https://zhuanlan.zhihu.com/p/83019548 ; https://www.zhihu.com/question/491712440 ; https://blog.csdn.net/qazplm12_3/article/details/133626842
- **[Not covered]** Reddit's r/PhD and r/AskAcademia could not be fetched (the site blocks crawlers), so this document **cites no original Reddit posts**.

### 6.3 A Key Finding: "Student Records → Supervisor Confirms" Is the Human Confirmation Gate [Inference, moderate evidence]

The UK supervision record systems (the student writes, and the record becomes official after the supervisor confirms; note from at the time of writing: this source is [Summary · to be verified]), MIT's supervisor policy (the student sends an email, reviewed at the next meeting), and the Soft Academia advice (send minutes and ask the supervisor to confirm) independently describe **the same workflow**: "student drafts → supervisor confirms → becomes the shared record → reviewed next time." This is structurally isomorphic to BriefPilot v1's "AI draft → human confirmation → official task," except that the confirmer changes from the "project manager" to the "supervisor," and the thing being confirmed changes from "tasks" to "commitments + decisions + supervisor advice."

**Why this matters for differentiation**: it suggests that BriefPilot's human confirmation gate in research settings is **not an extra burden but the digitization of an existing practice** (corrected wording: the UK already has form-based digital record systems, so what BriefPilot can do is **link them to meeting content, original-quote sources, and experimental results**, rather than being "the first to digitize"). Once the supervisor has confirmed, "the supervisor changed their mind" has a traceable written basis, which directly addresses the pain point of the student who wrote to Soft Academia.

**[Assumption H-C]** Supervisors are willing to spend under 5 minutes each week confirming the draft of "this week's commitments and decisions" submitted by the student. This is the biggest adoption risk in this direction and must be validated.

---

## 7. Academic Attitudes Toward AI Tools: Trust, Privacy, and Leakage of Unpublished Results (Research Question 6)

| Source | Sample and time | Key figures or findings | Verification |
|---|---|---|---|
| Wiley ExplanAItions 2025 | 2,430 researchers, August 2025 | AI usage rose from 57% to 84%; use for research and publication tasks rose from 45% to 62%; **privacy/security concerns rose from 47% to 58%**; **hallucination concerns rose from 51% to 64%**; the share who believe AI outperforms humans in more than half of use cases fell from over 50% to about 30%; 80% use general-purpose tools (such as ChatGPT), and only 25% use AI research assistants; average awareness of dedicated research tools is 11% | Original read https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx |
| OUP survey (reported by THE) | 2,300+ people, published May 2024 | 76% have used some AI tool; **only 8% believe AI companies will not use their research data without permission**; 6% believe AI companies can meet privacy and security needs; 46% say their institution has no AI policy; about three in five worry about harm to intellectual property | Original read https://www.timeshighereducation.com/news/use-ai-research-widespread-distrust-still-high-oup |
| Gautam, Liu, Choi, Lease (FAccT'26, arXiv 2604.23136) | 15 academic researchers, think-aloud | 2/15 explicitly worry that platforms training on prompts would "leak your research questions or research data"; 9/15 believe core scholarly judgment cannot be handed to AI; **10/15 limit AI to organizational, peripheral tasks, and the paper lists "tracking decision points" and "recording intermediate reasoning steps that would otherwise be lost"**; 8/15 repeatedly verify manually; 15/15 rely on social credibility heuristics (such as author familiarity) | Full PDF text parsed https://arxiv.org/pdf/2604.23136 |
| AI-assisted qualitative analysis study (arXiv 2509.18297) | Sample not verified | Data confidentiality affects whether researchers use AI; some de-identify data first; being unable to verify how data is stored or whether it is used for training heightens discomfort | Search summary, to be verified |
| Enago 2025 peer review survey | 124 people (small sample, not peer-reviewed) | 20% worry about confidentiality leaks ("Will uploading a manuscript leak confidential ideas?"); confidentiality is the top concern among non-users | Search summary, to be verified https://www.enago.com/academy/ai-assisted-peer-review-early-findings/ |

**Conclusions**
- **[Fact]** Adoption is rising quickly, but so are concerns; both are true at once. Researchers mainly use general-purpose tools and know little about dedicated research tools (11%).
- **[Inference]** Lab meetings contain **unpublished ideas and results**, which is what researchers most fear leaking (FAccT'26 P11's exact words: "leak your research questions or research data"). Therefore, "no cloud upload / can run locally / not used for training / deletable" are not bonus features but the **threshold** for entering research settings.
- **[Inference]** The FAccT'26 findings give BriefPilot a good positioning statement: **"AI doesn't make research judgments for you; it only helps you remember the judgments you've made."** This line corresponds directly to the use that 10/15 participants endorsed.
- **[Not covered, to be verified]** Direct evidence for the need for local deployment (for example, university IT policies prohibiting uploading meeting recordings to third parties, or cases of labs self-hosting Whisper and local LLMs) was not searched for in time. The self-hosted eLabFTW (AGPLv3) and Overleaf Server Pro mentioned in competitor research 03 are indirect evidence that academia has an existing demand for self-hosting.

---
## 8. Related Academic Research Map (Research Question 7)

| Study | Setting | Relevance to this project | What it does **not** answer |
|---|---|---|---|
| Liu, Althoff, Heer, "Paths Explored, Paths Omitted, Paths Obscured" (CHI 2020) | Interviews with 9 researchers | Taxonomy of decision rationale, implicit decisions, hindsight bias, a recommendation to track provenance | Meeting settings; decisions within teams or between advisors and students |
| Inie, Frich Pedersen, Dalsgaard, "How Researchers Manage Ideas" (C&C 2022) | Survey of 51 people + interviews with 18 | Ideas fall into four types (problem, method, hypothesis, theory); tooling opportunities | How ideas become commitments in group meetings |
| Kery et al., "The Story in the Notebook" (CHI 2018); Kery & Myers, Verdant (VL/HCC 2018) | Computational notebooks | Exploratory programming needs version records beyond the code itself | Discussion and decision context (citation details verified; full text not read) |
| Gautam et al. (FAccT 2026) | 15 participants, think-aloud | Trust, transparency, and accountability for AI in research; positioning AI for "peripheral tasks" | Meeting settings |
| Shankar et al., "Operationalizing ML: An Interview Study" (arXiv 2209.09125) | 18 ML engineers | Three factors: velocity, validation, versioning; experimentation is a loop | Leans toward industrial MLOps, not academic labs (abstract only) |
| Design rationale capture: Hammond et al. 2002 (MIT), WICSA 1999, Burge's NSF project | Software or engineering design meetings | **Closest precedent**: "rationale raised in meetings gets lost, automatic capture is valuable, but recording during the meeting interrupts the work" | Research settings; solutions in the LLM era |
| Stephens & Lewis, "Doing laboratory ethnography" (Qualitative Research 2017); Zhang (Frontiers in Education 2022); Latour & Woolgar, *Laboratory Life* | Laboratory ethnography | The group meeting is a site of identity negotiation and disciplinary culture; newcomers are socialized through group meetings and 1-on-1s | Tool design (abstract only) |
| "Project Management Practices as a Subject of Research for CSCW" (PACM HCI, CSCW 2017) | Survey | Only 26 papers in the CSCW literature explicitly discuss project management, mostly focused on IT development | Research project management (search abstract) |
| Survey of hybrid meeting systems (arXiv 2111.06172) | Survey | Meeting research is most concentrated at CHI (17 papers) and CSCW (14 papers) | Not specific to labs |

**[Inference]** The gap in the literature is that there is little HCI research on the span "from meeting discussion to research commitment to experimental evidence", at least none found within this round's budget. **This counts in the portfolio's favor**: if BriefPilot's user study runs 5–8 interviews and a 4-week dogfooding log in a lab at the target university, it could itself become a CHI Late-Breaking Work topic ([Assumption], needs the advisor's judgment).

---

## 9. Requirements Spec Sketch: Research Commitments and Knowledge Retrospection

### 9.1 Object Model

```text
Meeting (group meeting / 1-on-1 / review discussion)
  └─ SourceSpan (original excerpt: minutes paragraph, timestamp, whiteboard photo region) ── the provenance of every object, required

Hypothesis                 id, statement, status: open|supported|refuted|inconclusive|retired,
                           proposed_in: SourceSpan, owner?: null allowed
Commitment                 id, kind: experiment|reading|writing|analysis|other,
                           statement, owner?, due? (anchored to a Deadline or a date),
                           tests: Hypothesis[] (the testing relation, may be empty),
                           success_criterion? ("2 points higher than baseline"),
                           status: proposed → confirmed → in_progress → resolved | dropped,
                           resolution?: Result
Result                     id, commitment_id, outcome: supported|refuted|inconclusive|not_run|superseded,
                           summary, reported_in: SourceSpan (which meeting it was reported in),
                           evidence: Evidence[]
Evidence                   id, type: wandb_run|git_commit|config_file|figure|paper|overleaf_section|note,
                           uri, captured_at (links first, no copying of data)
Decision                   id, statement, chosen, rejected_alternatives[], rationale (verbatim quotes only),
                           based_on: Result[] | Feedback[], made_in: SourceSpan,
                           confirmed_by (advisor or owner), supersedes?: Decision
Feedback                   id, source: advisor|reviewer|committee|peer, text, made_in: SourceSpan,
                           addressed_by: Commitment[] | Decision[]
OpenQuestion               id, question, raised_in, related: Hypothesis[], status
ConfigChange               id, param, from, to, reason → Decision, evidence: Evidence
Deadline                   id, name (CoRL 2027 submission deadline), date, kind: external|internal
```

**Design principles (each with its rationale)**
1. **SourceSpan is required.** Rationale: v1's "no source, no output" principle extends here; Liu et al. have already shown that after-the-fact recall is unreliable.
2. **Decision.rationale may only quote verbatim; the model must not generate rationale.** Rationale: a reason filled in by the model is itself a kind of "hindsight" and would contaminate the decision record. When no verbatim quote exists, mark it "rationale not recorded".
3. **Completing a Commitment must attach a Result**; a checkbox alone is not enough. Rationale: see Section 3.2. `not_run` and `superseded` are allowed so people aren't pushed into fabricating results.
4. **owner and due may be empty.** Rationale: hypotheses, open questions, and many soft commitments have no owner by nature; this follows v1's "leave missing fields blank, don't guess".
5. **Evidence stores links only.** Rationale: lowers privacy risk and avoids duplicating W&B/ELN.
6. **A Decision needs confirmation by the advisor or owner** to become a "consensus decision". Rationale: this matches the institutionalized workflow in Section 6.3 and also serves as written grounds when "the advisor changes their mind".
### 9.2 Differences from a Generic Action Item (Comparison Table)

| Dimension | Generic action item (Feishu Minutes / Otter / Fireflies / BriefPilot v1) | Research commitment model (BriefPilot v2 candidate) | Basis |
|---|---|---|---|
| First-class objects | Tasks only | Hypotheses, commitments, results, evidence, decisions, feedback, open questions | Typology in Section 2; Inie et al. |
| Core fields | Action item / owner / priority / due date (Feishu export fields) | + which hypothesis is tested / success criteria / result / evidence link / which result the decision is based on | Feishu (original text read); academic templates (carried over) |
| Completion semantics | Binary; status synced on completion | Five-valued outcome + required result summary | Section 3.2 |
| Cross-meeting relations | Weak: each meeting is independent | **Strong**: the next meeting automatically lists "commitments awaiting results" and "decisions challenged by new results" | Cahoy's "review at next meeting"; Imperial agenda |
| Provenance | Feishu lets users click text to jump to audio/video (original text read); Fabric claims links to timestamps (marketing) | Provenance traces to a SourceSpan, **and** a decision can be traced back to the results and evidence it relies on | This document's claim |
| Rationale | Not modeled | Rationale quotes only the original words and records rejected alternatives | Liu et al.; design rationale literature |
| Confirmer | Meeting organizer / task owner | **Advisor confirms** decisions and suggestions; students confirm their own commitments | Section 6.3 |
| External objects | Jira / Feishu Tasks / Asana | W&B runs, Git commits, configs, Overleaf sections, papers | Section 4 |
| Time structure | Due date | Backward planning from external submission deadlines + research cycles measured in months | Cahoy |
| Privacy expectations | Enterprise SSO and compliance | Unpublished results; leans toward local/self-hosted, no training, deletable | Section 7 |

### 9.3 Candidate Feature Differentiation List

> Confidence indicates how credible it is that "this is a real, unmet need"; it does not represent commercial value. **High**: supported by multiple independent factual sources; **Medium**: factual support exists, but a key link is inference; **Low**: mostly assumption.

| # | Candidate feature | User problem | Evidence | Confidence | Difference from competitors | Demo feasibility |
|---|---|---|---|---|---|---|
| F1 | **Commitment → result backfill loop**: before the next meeting, automatically generate a "last meeting's commitments" list and require an outcome and evidence link for each item | "Did you run the experiment you mentioned last week? What was the result?" | Cahoy's "review at next meeting" (original text read); Imperial agenda; Bahlai's "long-term goals fall through the cracks" (carried over) | **High** | Feishu's "sync status on completion" is binary; Fabric does not mention result backfill (added at the time of writing: Littlebird already has three-state evidence comparison, and Fellow syncs status bidirectionally with GitHub; the remaining difference is the five-valued research semantics and experiment-artifact evidence) | High (plain text + state machine) |
| F2 | **Decision recall Q&A with provenance**: "Why did we choose 8 for the action chunk?" returns the decision, the original quote snippet, and the supporting result and run links; with no record, it declines to answer | Recall when writing papers, responding to reviewers, and handing over work | Liu et al. (hindsight bias, implicit decisions); design rationale literature; Fabric is also doing this (marketing) | **High** (need) / **Medium** (differentiation, since Fabric already claims it) | The difference lies in "quotes only original words, can decline to answer, links to experiment artifacts", not in "having a decision log" | High: directly reuses v1's RAG + citation verification |
| F3 | **Hypothesis ledger**: hypotheses as first-class objects, linked to the commitments and results that test them, with status moving among open/supported/refuted | "Which conjectures have we actually tested?" | Inie et al.'s four idea types; Liu et al.'s path exploration | **Medium** | No meeting tool found that models "hypotheses" (based on verified Feishu and Fabric pages; other competitors still to be verified) | Medium |
| F4 | **Advisor confirmation gate + advisor suggestion records**: students submit this week's commitments and draft decisions, and the advisor confirms or edits with one click; advisor suggestions form their own category with version history | Advisor's memory burden; written grounds for "the advisor changed their mind" | UW handbook, Cahoy, UK supervision record systems, Soft Academia, Degree Doctor | **Medium** (the need is real, **but whether advisors are willing to confirm is the biggest risk**) | UK supervision systems are forms, with no AI and no link to experiments; generic tools have no student/advisor roles | High |
| F5 | **Reviewer comment → response → experiment mapping**: each reviewer comment is linked to the corresponding commitment, result, and paper revision | Tracking during the rebuttal phase | Overleaf comment flow and Granola academic scenarios in competitor research 03 (carried over); Fabric's "answers are already recorded when reviewers ask about methods" | **Medium** | Overleaf only handles text revisions and is not connected to experiments | Medium |
| F6 | **Decision conflict alert**: when a new result contradicts the basis of a confirmed decision, prompt "Decision D12's basis R5 has been overturned by R9; reconsider?" | Prevent continuing to build on outdated conclusions | [Inference] Derived from the data model; no direct user evidence | **Low** | No competitor seen | Medium (rule matching suffices; no complex reasoning needed) |
| F7 | **Methods and setup section draft assistant**: based on the settings used in a paper, aggregate the related decisions and original quotes, and generate "setup notes + citation list" for the author's reference (not written directly into the paper) | Recalling settings when writing the methods section | Gundersen (20%–30% of variables recorded); W&B supports LaTeX export | **Medium** | W&B only aggregates numerical values, without discussion context | Medium |
| F8 | **Local-first / no training / deletable**: supports local models or self-hosting; meeting transcripts stay on the machine by default | Worry about leaks of unpublished results | Wiley 58%; OUP 8%; FAccT'26 P11 | **High** (as a threshold requirement) | Fabric claims no training but is still a cloud SaaS; Feishu and Otter are both cloud-based | Medium (the demo can use a local model) |
| F9 | **Non-Zoom input**: accept Markdown notes written by students after the meeting, whiteboard photos, and phone recordings as SourceSpans | In-person group meetings, whiteboards, mixed Chinese/English | Competitor research 03, Section 6 (carried over) | **Medium** | Generic tools are mainly meeting bots | High (Markdown input is simplest) |
| F10 | **Newcomer handover package**: per project, generate a list of "confirmed decisions + rejected alternatives + open questions" | Handover when cohorts change | Zhang 2022 on newcomer socialization; [Inference] | **Low** | No competitor seen | High |

**[Inference] Recommended demo main line**: F1 + F2 + F4, plus the stance of F8. There are three reasons: (a) these three have the strongest evidence; (b) they maximize reuse of the RAG, citation verification, and human confirmation gate already designed in v1, so engineering risk is low; (c) they can explain in 3 minutes "why Feishu Minutes can't do this": Feishu produces tasks with checkboxes, while BriefPilot produces a traceable chain of "commitment → result → decision".
### 9.4 What we explicitly do not build (and why)

- **No ELN or experiment tracking**: W&B, Git, and ELNs already cover this, so we only link to them.
- **No model inference of decision rationale or hypothesis conclusions**: this avoids hindsight contamination, and it matches the preference in FAccT'26 for humans retaining academic judgment (9/15).
- **No transcription-engine race**: we do not compete with Feishu on mixed Chinese-English WER.
- **No default visibility of all of a student's commitments to the advisor**: the psychology of permissions is unvalidated (an assumption from Competitor Research 03), so the default is "shared only after the student confirms."

### 9.5 Assumptions to validate and interview questions

| ID | Assumption | How to validate | Failure signal |
|---|---|---|---|
| H-A | Students are willing to spend about 30 seconds back-filling results and evidence | 4 weeks of dogfooding, measuring the back-fill rate | Back-fill rate below 50% |
| H-B | Computational labs are willing to paste run or commit links | Interviews + logs | Most people say "I just remember it myself" |
| H-C | Advisors are willing to spend under 5 minutes a week confirming | Concept tests with 2–3 PIs | PIs say "let the students manage it" |
| H-D | Decision look-back is frequent enough when writing papers and responding to reviewers (e.g., 10+ times per paper) | Retrospective interviews: "When you wrote your last paper, how many times did you go back to old meeting notes?" | Frequency is very low, or people can always just ask a peer |
| H-E | On-premises deployment is a hard requirement, not a preference | Ask about their institution's data policy and their actual behavior | People use ChatGPT anyway |

In interviews, **ask about behavior, not willingness**: "The last time you couldn't remember why you picked a certain setting, how did you recover it? How long did it take?" and "Where do you record the things you said you'd do at last week's group meeting?"

---

## 10. Gaps and next steps

1. **Original Reddit / Twitter posts**: the sites block crawlers, so this document does not cite them. Next step: manually search r/PhD, r/AskAcademia, and r/MachineLearning for "advisor doesn't remember", "lab meeting notes", and "why did we choose", and excerpt 10–20 original posts.
2. **Systematic ACM DL search**: not completed before the search quota ran out. Suggested queries: "lab meeting", "research group meeting", "doctoral supervision", "advisor-advisee", "research provenance", limited to CHI, CSCW, DIS, and C&C.
3. **Adoption rates of ELNs and experiment tracking in ML labs**: no quantitative data found.
4. **Official action-item fields of Otter / Fireflies / Granola**: the official help pages returned 403 or 404; to be filled in by Competitor Research 02.
5. **The share of "failed to reproduce their own work" in Baker 2016**: needs checking against the original Nature article.
6. **Direct evidence for the on-premises requirement**: university IT policies are not covered (a starting point is the target university's own AI usage policy).

---

## Source list

**Academic research**
1. Liu, Althoff, Heer. Paths Explored, Paths Omitted, Paths Obscured. CHI 2020. https://ar5iv.arxiv.org/html/1910.13602 ; https://idl.uw.edu/papers/analysis-decision-points ; https://dblp.dagstuhl.de/rec/conf/chi/LiuAH20.html (original read)
2. Gautam, Liu, Choi, Lease. How Researchers Navigate Accountability, Transparency, and Trust When Using AI Tools in Early-Stage Research. FAccT'26. https://arxiv.org/pdf/2604.23136 (PDF parsed)
3. Inie, Frich Pedersen, Dalsgaard. How Researchers Manage Ideas. C&C 2022. https://researcher.itu.dk/en/publications/how-researchers-manage-ideas/ (abstract page read)
4. Kery et al. The Story in the Notebook. CHI 2018 (citation info from https://arxiv.org/pdf/2303.04059 ); Verdant: https://www.hcii.cmu.edu/news/kery-myers-win-best-paper-vlhcc-verdant-prototype (search snippet)
5. Gundersen & Kjensmo. State of the Art: Reproducibility in AI. AAAI 2018. https://mlanthology.org/aaai/2018/gundersen2018aaai-state (abstract page read)
6. Baker. 1,500 scientists lift the lid on reproducibility. Nature 533, 2016. https://www.nature.com/articles/533452a ; secondary: https://reproduciblebiomodels.org/1500-scientists-lift-the-lid-on-reproducibility/ (secondary source, to be verified)
7. Shankar et al. Operationalizing Machine Learning: An Interview Study. https://arxiv.org/abs/2209.09125 (abstract page read)
8. Hammond, Gajos, Davis, Shrobe. MIT 2002. https://groups.csail.mit.edu/mug/pubs/Hammond2002Agent.pdf (search snippet)
9. WICSA 1999 (SAAM rationale). https://icsa-conferences.org/series/WICSA/1999/final/richter.pdf (search snippet)
10. Jane Burge research page. https://sites.coloradocollege.edu/jburge/research (search snippet)
11. Design Society studies on design-meeting rationale: https://risk.designsociety.org/download-publication/39797/How+explicit+are+we+in+a+design+meeting%3A+Investigation+on+meeting+knowledge+structuring+with+design+rationale ; https://asiachapter.designsociety.org/download-publication/25563/A+Study+of+Information+%26+Knowledge+Generated+During+Engineering+Design+Meetings (search snippet; correspondence with "2007 Strathclyde" to be verified)
12. Stephens & Lewis. Doing laboratory ethnography. Qualitative Research, 2017. https://doi.org/10.1177/1468794116678040 (search snippet)
13. Zhang. The production of laboratory scientists. Frontiers in Education, 2022. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2022.1000905/full (search snippet)
14. Project Management Practices as a Subject of Research for CSCW. PACM HCI CSCW 2017. https://dl.acm.org/citation.cfm?id=3134660 (search snippet)
15. What was Hybrid? A Systematic Review of Hybrid Collaboration and Meetings Research. https://arxiv.org/pdf/2111.06172 (search snippet)
16. AI-incorporated Qualitative Data Analysis. https://arxiv.org/pdf/2509.18297 (search snippet)
17. Practitioner Motives to Use Different HPO Methods. https://arxiv.org/pdf/2203.01717 (search snippet; methodological reference only)
18. The Trust Paradox: How CS Researchers Engage LLM Leaderboards. https://arxiv.org/pdf/2605.28966 (search snippet; related work only)

**Surveys and news coverage**
19. Wiley ExplanAItions 2025 press release. https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx (original read)
20. THE coverage of the OUP survey, 2024. https://www.timeshighereducation.com/news/use-ai-research-widespread-distrust-still-high-oup (original read)
21. Enago 2025 survey on AI-assisted peer review. https://www.enago.com/academy/ai-assisted-peer-review-early-findings/ (search snippet)
22. Help Net Security, 2026-04-29, on researchers' concerns about prompt confidentiality. https://www.helpnetsecurity.com/2026/04/29/ai-prompt-confidentiality-researchers/ (search snippet; apparently reports a second study)

**Advising and supervision policies**
23. MIT AeroAstro, Kerri Cahoy Advising Philosophy 2019. https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf (PDF parsed)
24. UW CS PhD Advising Guide – Building a relationship. https://www.cs.washington.edu/academics/phd/handbook/advising-guide/building-a-relationship (now requires login; search snippet; a retry got a 301 to internal.cs.washington.edu and then an SSO prompt, to be verified)
25. UW CS Advising Guide – Troubleshooting. https://www.cs.washington.edu/academics/graduate/phd-program/handbook/advising-guide/troubleshooting (search snippet)
26. Loyola Graduate School Survival Guide. https://www.luc.edu/media/lucedu/history/graduateprogramhandbook/adviceonbeingasuccessfulgraduatestudent/Graduate%20School%20Survival%20Guide.pdf (search snippet)
27. McMaster supervisory relationship. https://hsed.mcmaster.ca/wp-content/uploads/2022/04/supervisory_relationship.pdf (search snippet)
28. QUB Students' Union supervision meetings toolkit. https://q-su.org/studentvoice/studentsupervisorrelationshiptoolkit/SupervisionMeetings (search snippet)
29. Haplo PhD Manager supervision meetings. https://support.haplo.com/phd-manager/user-guidance/supervision-meetings (search snippet; now redirects; a retry got a 301 to the Cayuse help center home page, to be verified)
30. Wolverhampton Guidelines on Records of Meetings. https://www.wlv.ac.uk/media/departments/research/documents/Appendix-3---Guidelines-on-Records-of-Meetings-between-Supervisors-and-Students.pdf (search snippet; fetch returned empty, to be verified)
31. LJMU eDoc meeting record guidance. https://cd-prod.ljmu.ac.uk/-/media/files/ljmu/doctoral-academy/edoc-guidance-for-completing-a-meeting-record.pdf (now 404; content taken from search snippet)
32. Time Management for New Faculty. https://advance.washington.edu/sites/advance/files/8_Time%20Management%20for%20New%20Faculty.pdf (search snippet)
33. Soft Academia, "Dear bewildered and burnt out". https://softacademia.substack.com/p/dear-bewildered-and-burnt-out (original read)
34. Degree Doctor, Why your PhD supervisor keeps changing their mind. https://www.thedegreedoctor.com/blog/phd-supervisor-changing-expectations-qualitative-research (original read)
**Products and Tools**
35. Fabric for Academic Labs. https://fabric.so/teams/academic-labs (original read; marketing page)
36. Feishu Smart Meeting Minutes AI Features Explained. https://www.feishu.cn/content/article/7594772423082396858 (original read)
37. Feishu: Meeting Summaries and Exporting Action Items. https://www.feishu.cn/content/article/7602953888668339380 (original read)
38. W&B Reports documentation. https://docs.coreweave.com/products/wandb/reports.md (original read); W&B LaTeX workflow blog post https://wandb.ai/andrea0/note_taking/reports/A-Snappy-TeX-Workflow-for-Reports--VmlldzozNTEyNzY1 (search snippet)
39. Overleaf Git integration documentation. https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git (original read)

**Chinese-Language Community**
40. Zhihu Q&A on experiment records: https://www.zhihu.com/question/66730795 ; https://www.zhihu.com/question/36506395 ; Guancha.cn https://user.guancha.cn/main/content?id=195206 (search snippet)
41. Zhihu discussions on advisors and group meetings: https://zhuanlan.zhihu.com/p/83019548 ; https://www.zhihu.com/question/491712440 ; https://blog.csdn.net/qazplm12_3/article/details/133626842 (search snippet; weak evidence)

**Internal to this project (carried over)**
42. Competitor research 03 (includes verified sources such as Nature 2021 Powell, Kanza 2017, the Nature 2025 advisor survey, the Imperial supervision agenda, and Duke JACMP 2025): <repo>/01_market-research/03_competitors_research_lab_tools.md ; BriefPilot PRD: the earlier v1 docs (not included)

---

**New in the Round 2 revision (accessed at the time of writing)**
43. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
44. Fellow × GitHub — https://fellow.ai/integrations/github
45. Fellow Action Items — https://fellow.ai/features/action-items
46. Cayuse Help Center home page (the target of the Haplo link redirect; original content not seen) — https://support.cayuse.com/hc/en-us

## Confidence in This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| Research outputs are structurally different from enterprise action items (Section 2) | **Medium-high** | Supported by academic taxonomies (Inie, Liu) and competitor fields (Feishu, original read); "no counterpart in enterprise meetings" is an inference, with no comparative corpus analysis of enterprise minutes |
| Commitments need a closed loop with outcomes and evidence (Section 3) | **Medium-high** | The MIT advisor policy and the Imperial agenda directly reflect "review at the next meeting"; the five-value fulfillment semantics are an inference |
| Recalling the rationale for decisions after the fact is unreliable (Section 5) | **High** | CHI 2020 original read, with an explicit hindsight-bias warning; but the sample is only 9 people and the setting is not meetings |
| The advisor's memory burden is institutionally accepted as the default (Section 6) | ~~**Medium**~~ **Medium-low** (revised at the time of writing) | MIT policy original read; the UW handbook and UK supervision systems come **entirely** from search snippets (both still failed to open on the retry); no original Reddit posts; weak Chinese-language evidence. The sentence "no tool supports this yet" was changed to "administrative record systems exist, but they are not connected to meeting content" |
| Researchers worry about privacy and prefer AI to handle peripheral organizing (Section 7) | **High** | Wiley and OUP are large samples, original read; FAccT'26 full text parsed. But "local deployment is a hard requirement" remains an inference |
| The HCI literature lacks studies on tracking lab meeting commitments (Section 8) | **Low to medium** | A negative finding, limited by search budget; must be re-checked in the ACM DL |
| Feature candidates F1, F2, F4, F8 are worth a demo | **Medium** | Demand evidence is fairly strong; the degree of differentiation is affected by features Fabric already claims; whether advisors are willing to confirm (H-C) is the biggest unknown |
| All numeric illustrations ("8 students × 3 threads") | **No data** | For illustration only; must not be cited as survey data in interviews |

---

## Revision Log (Round 2)

> Based on `01_market-research/06_research_integrity_review.md` §2 (W1, W8, W10), §6 (C1, C2), §7 (evidence labels), §9 P0-4. On the UW CS handbook (login required), Haplo (redirects to the Cayuse home page), and the Wolverhampton PDF (fetched empty) were retried, and the Littlebird Promise Tracker and Fellow pages were opened.

| # | Location | Change | Basis |
|---|---|---|---|
| 1 | Frontmatter, reading notes | Status marked as revised; sources_count 42 → 46; added explanation of the [Summary] label | 06 §7 |
| 2 | §0 item 3 | Label split into [Fact] (MIT) / [Summary·to be verified] (UW, UK); "partially read" struck through; "just no tool support yet" struck through and changed to "administrative record systems exist, but they are not connected to meeting content"; added that Fellow and Littlebird show no advisor confirmation | 06 C2, W8 |
| 3 | §0 item 5 | Added comparison with Littlebird's three-state evidence and Fellow's GitHub sync, noting that the "closed loop" itself is not a differentiator | 06 V1, V4 |
| 4 | §4, §5, §6.1, §6.2 | 6 instances of "[Summary·to be verified]" → [Summary·to be verified] (Zhihu experiment records, design-rationale literature, UW CS handbook, UW ADVANCE time management, McMaster/Loyola/QUB, UK supervision systems); 1 instance of "[Summary·weak evidence]" → [Summary·weak evidence] | 06 §7 |
| 5 | §6.2 UK supervision systems | Added the retry results and pointed out the contradiction with the original wording in §0 | 06 C2, W8 |
| 6 | §6.3 | Added a [Summary·to be verified] note to the UK sources; changed "digitizing existing institutions" to "connecting existing record systems to meeting content, provenance, and experiment results" | 06 C2 |
| 7 | §9.3 F1 | Added Littlebird and Fellow to the differentiation-from-competitors cell | 06 V1, V4 |
| 8 | Confidence table, sources | Section 6 confidence medium → medium-low; added retry results to sources 24, 29, 30; added sources 43–46 (accessed at the time of writing) | — |

**Left unchanged for later:** the labels "[Fact, secondary]" (Baker 2016) and "[Fact, abstract page read]" (meaning the paper's abstract page was opened, not a search snippet) are kept as is; confidence levels for the remaining F entries in §9.3 have not been re-assessed.
