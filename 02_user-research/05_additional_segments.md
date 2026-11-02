---
title: "User Research 05: Evaluation of the 5 Segments Added After the First-Round Review (Corporate Joint Labs, Enterprise ML Teams, FYP, TAC, Cross-Institution Consortia), Compared with the First-Round Top Segments"
status: draft
sources_count: 43
---

# User Research 05: Evaluating the New Segments. Can a Corporate Joint Lab Deliver "Research Semantics + Client–Vendor Confirmation + a Paying Party" at Once?

> **Reading notes**
> - Labeling rules: **[Fact]** means this round opened the original page and checked it, with a URL; **[Summary]** means only the search-result snippet was seen, because the original page was not opened or could not be opened; **[Inference]** is derived from several facts with no direct evidence; **[Assumption · to be validated]** needs interviews or experiments to verify.
> - All sources were accessed at the time of writing. Source IDs use `[N#]` (newly searched this round) and `[R#]` (verified in the first-round review 06 and reused directly this round without reopening). The full list is at the end of the document.
> - **The scoring framework is carried over unchanged from the first round**, [02_segment_other_candidates.md](02_segment_other_candidates.md) §1.1, with six dimensions: D1 unmet need 25%, D2 pain-point evidence 20%, D3 reachability 20%, D4 demo feasibility 15%, D5 compliance threshold (inverted) 10%, D6 willingness to pay 10%. Each is scored 1–5, so old and new scores can be compared directly.
> - **No user interviews were conducted this round.** D3 is therefore still entirely assumption, and the D2 evidence is mainly "institutional and procedural" evidence (job responsibilities, contract clauses, university regulations) rather than "users say it hurts". This is the same limitation as in the first round and must be stated clearly in the conclusions.
> - WebSearch was available this round. About 25 searches were run, and 22 pages were opened in full with WebFetch. In addition, the DESCA contract template PDF was downloaded and its full text extracted locally, and the clauses were checked word for word.

---

## 0. The Answer First (TL;DR)

1. **[Fact] All 5 corporate joint labs at the target university mentioned in the first round exist, but 3 of them have been renamed or have changed form.**
   - The Rolls-Royce lab and Singtel's SCALE lab are still on the university's official list.
   - Alibaba: after the 2018 Joint Research Institute (JRI), the Alibaba Global e-Sustainability CorpLab (ANGEL) was newly established on 2024-09-12, with a 5-year term and up to 200 researchers.
   - The Continental lab now appears in the university's current list as the **AUMOVIO Corporate Lab**.
   - The HP lab is now listed as a **Joint Lab** and is no longer called a Corporate Lab.
   - The university's official list shows **17** corporate labs and joint labs in total [N2]. Other pages of the university give the figure as "around 20" [N5], "25" [N4], and "over 25" [N6], so the counts are inconsistent.
   - The ones closest to the user-research direction (VLA/robotics) are the Hyundai–A\*STAR joint lab (established 2025-10-13, working on AI manufacturing and robotics) [N8], the AUMOVIO lab, and the Schaeffler lab.
2. **[Fact] Corporate joint labs do have an institutional skeleton of "regular reporting to the client", but the public evidence only goes as far as "these meetings and documents exist" and does not reach "the company must formally confirm".** The evidence found:
   - The Rolls-Royce lab's senior project manager posting requires the person to "drive the weekly operation meetings" and "coach the team to prepare for Quarterly reviews and Strategic meetings", and to maintain the "Project Online System" [N9];
   - The Surbana Jurong lab's research engineer posting requires the person to "engage stakeholders/authorities for scheduled progress updates and decision making" and to help set up a "progress report, change log" [N10];
   - The university officially says "each research project is led from the start by a [university] professor and a company scientist or engineer" [N5].
   - What was **not found**: the NRF reporting template for corporate labs, the specific format of milestone reviews, and whether the company signs off on meeting minutes.
3. **Answer to the core question**: can "research semantics" and "client–vendor confirmation" hold in the same scenario, and can "a paying party" be solved along the way? **My judgment: about two and a half of the three are solved.**
   - **Research semantics: yes.** The projects are research projects by definition [Fact].
   - **Client–vendor (Party A/B) structure: present, but the strength of "confirmation" is to be validated.** Dual leads, quarterly reviews, and change logs all have public evidence [Fact]; whether the company actually confirms item by item has no evidence [Assumption · to be validated].
   - **Paying party: exists, but the market is narrow and the procurement chain is long.** The money comes from joint funding by companies and NRF, and the labs already have project-management roles and a project-management system, which suggests precedent for tool spending [Fact + Inference]. But all of Singapore has only a few dozen such labs, and procurement must also clear the university's IT and the company's IP clauses [Inference].
   - **Conclusion: it is a "wedge with a paying party", not a "big market".**
4. **[Fact] Unexpected finding: the hardest "counterparty confirmation" evidence found this round is not in a corporate joint lab but in EU Horizon consortia.** The DESCA consortium agreement template (2026-02, v2.1) states that meeting minutes are "the formal record of all decisions taken". The chair must send out a draft within 10 calendar days after the meeting, and **if no party raises a written objection within 15 calendar days, the minutes are deemed accepted** [N19]. This is a ready-made, contract-grade multi-party confirmation mechanism, and it can also be borrowed directly as a product design pattern: "default acceptance + objection window", which has much less friction than "the other side must click confirm on every item" [Inference]. Unfortunately, it is hard for Singapore-based users to join EU consortia, so reachability is low.
5. **Weighted scores for the 5 new segments (default weights)**:

   | Segment | Weighted score |
   |---|---|
   | Corporate joint labs | 3.50 |
   | FYP supervisor meetings | 3.40 |
   | Cross-institution research consortia | 3.30 |
   | IPP / dual-supervisor industrial PhD (listed separately as a sub-segment of corporate labs) | 3.30 |
   | Enterprise ML teams | 3.25 |
   | TAC | 3.05 |

   **None of them alone exceeds the first-round #1 (client–vendor / Party A/B, 3.70).** However, if it is evaluated as a ladder of "the author's own computing-oriented lab (wedge, dogfooding) → corporate joint labs (paid extension)", the upper bound is about 3.80, on par with the roughly scored "academic labs" in the first round and 0.1 higher than client–vendor. **A gap of less than 0.3 should be treated statistically as the same tier**, so the ranking has to rest on qualitative reasons.
6. **Updated Top 3** (details in §5):

   | Rank | Segment | Compared with the first round |
   |---|---|---|
   | ① | **The "computing-oriented research group → corporate joint lab" ladder** | New entry; absorbs most of the first-round #2, "hardware/robotics" |
   | ② | **Client–vendor requirements meetings** | Down from #1 to #2; its role changes from "main line" to "outward-facing generalization narrative" |
   | ③ | **Open-source communities** | Kept; still only an evaluation venue |

   - **Hardware/robotics is no longer listed separately**: after verification in the first-round review 06, Fellow already offers two-way GitHub sync, Littlebird already does evidence comparison, and MCP is becoming widespread, so its D1 is lowered from 4 to 3 and its weighted score drops to 3.45. Its robotics semantics are now carried by corporate labs in robotics-related directions, such as Hyundai and AUMOVIO.
   - **Enterprise ML teams**: demoted to a control group.
   - **FYP**: replaces "student project teams" as a usability-testing pool.
   - **TAC**: demoted to a feature point, not treated as a segment.
   - **Cross-institution consortia**: demoted to a design reference and a future expansion direction.

---
## 1. Verification: Which Joint Industry Labs Exist at the Target University and What Is Their Current Status

In lab names below, "[Univ]" stands for the target university.

### 1.1 The five labs named in the task

| Lab named in task | Verification result | Status | Evidence |
|---|---|---|---|
| Alibaba-[Univ] | The Alibaba-[Univ] Singapore Joint Research Institute (JRI) was established in 2018. The target university's list classifies it as an "institute," not a lab. On 2024-09-12 the **Alibaba-[Univ] Global e-Sustainability CorpLab (ANGEL)** was newly established: supported by NRF RIE2025, 5-year term, "up to 200" scientists and engineers from the target university and Alibaba, with research directions including energy-efficient AI algorithms, green cloud computing, etc. | Exists (new lab) | [Fact] [N7], [N2] |
| Rolls-Royce@[Univ] | Established in 2013 as the first lab under the Corp Lab programme. The NRF page records a total Phase 2 investment of $88M (listed in 2019). | Exists | [Fact] [N1], [N2]; the Phase 2 span of 2019–2024 and whether it was renewed afterwards is [Summary/to be verified] ([N11]) |
| Continental-[Univ] | NRF lists "Continental-[Univ] 'FOCUS' Lab (2019)" [N1]; the target university's EEE page states S$50M and 16 projects, with directions in autonomous robotics, navigation, AI, etc. [N3]. **The target university's current master list no longer includes "Continental-[Univ]"; it has been replaced by the "AUMOVIO-[Univ] Corporate Lab"** [N2] | Exists (suspected rename) | [Fact] both lists were checked; "AUMOVIO is the new company spun off from Continental's automotive business, so the lab was renamed accordingly" is an [Inference, to be verified] |
| HP-[Univ] | NRF lists it as "HP-[Univ] Digital Manufacturing Corporate Lab (2018)" [N1]; the target university's current list names it "**HP-[Univ] Digital Manufacturing Joint Lab**" [N2] | Exists (form changed from Corp Lab to Joint Lab) | [Fact]; reason for the change to be verified |
| Singtel | SCALE@[Univ] (Singtel Cognitive and AI Lab for Enterprises), listed by NRF as 2017 | Exists | [Fact] [N1], [N2] |

### 1.2 Other corporate labs and joint labs on the target university's current list (17 in total)

[Fact] Source [N2]:

- Alibaba-[Univ] (ANGEL), AUMOVIO-[Univ], Delta-[Univ], ExxonMobil-[Univ]-A\*STAR, Hyundai-[Univ]-A\*STAR, NTI-[Univ], Schaeffler-[Univ] (Intelligent Mechatronics Hub)
- Ant International-[Univ], Mastercard-[Univ] (DigiFI), HP-[Univ], [Biologics firm]-[Univ], Rolls-Royce@[Univ], SCALE@[Univ], SHARE@[Univ] (industrial collaborative robots), SMRT-[Univ], SP Group-[Univ], Surbana Jurong-[Univ]

**[Inference] The ones closest to the user's research direction (VLA, robotics) are the following** and can serve as priority interview targets:

- **Hyundai-[Univ]-A\*STAR**: announced 2025-10-13; focus on AI for smart manufacturing and robots for efficiency gains and defect detection; the target university's EEE, MAE, and CCDS schools participate; it uses a three-party structure of "[Univ] Co-Director + A\*STAR Deputy Co-Director + HMGICS Deputy Co-Director" [Fact, N8]
- AUMOVIO-[Univ] (autonomous robotics, navigation) [N3]
- Schaeffler-[Univ] (Intelligent Mechatronics Hub) [N2]
- SHARE@[Univ] (industrial collaborative robots) [N2]
- Alibaba ANGEL's AI algorithms direction [N7]

### 1.3 Two "three-party" formats adjacent to corporate labs

- **EDB Industrial Postgraduate Programme (IPP)**: trainees "be supervised by an academic faculty from [the target university] and a company staff with appropriate research qualifications," spend at least 50% of research time on-site at the company; the company handles supervision and hosting and "Co-share research grant" [Fact, N12].
- **Alibaba Talent Programme**: students are "Alibaba full-time employees," co-supervised by a supervisor at the target university and an Alibaba co-supervisor, with up to 50% of time at Alibaba [Fact, N13]. The deadline shown on the page is in 2024; whether the programme is still recruiting is **to be verified**.
- **[Inference]** These two formats are 1-on-1 meetings among "**student × academic supervisor × industry supervisor**," a smaller and sharper sub-segment of corporate joint labs (§3.1b).

---

## 2. Corporate Joint Labs: Answering the Three Questions One by One

### 2.1 Typical meetings and outputs (what public evidence can piece together)

| Meeting/mechanism | Evidence | Evidence level |
|---|---|---|
| **Weekly operation meetings** | RR@[Univ] senior project manager duties: "drive the weekly operation meetings" [N9] | [Fact], but the posting dates from 2020 with a deadline of 2020-08-23; current status to be verified |
| **Quarterly reviews and strategic meetings** | Same position: "coach the team to prepare for Quarterly reviews and Strategic meetings" [N9] | [Fact], same as above |
| **Project management system** | Same position: "drive the use of the Project Online System so that all the required information is available when required" [N9] | [Fact] |
| **Managing the university team on behalf of the Co-Director** | Same position: "Drive the [university] team on behalf of the Co-Director" [N9] | [Fact]; indicates a dual-director structure with a university side and an industry side |
| **Scheduled progress updates to stakeholders and decision making** | SJ-[Univ] research engineer duties: "engage stakeholders/authorities for scheduled progress updates and decision making" [N10] | [Fact], also a 2020 posting |
| **Progress report + change log** | Same position: "Assist the Project Manager to establish project objectives, procedures, data inventory, progress report, change log"; "keep him/her constantly informed of project progress, plans and risks/issues" [N10] | [Fact] |
| **Each project jointly led by an academic and an industry lead** | Official statement from the target university: "each research project is led from the start by a [target university] professor and a company scientist or engineer," especially in corporate labs co-funded by government and industry [N5] | [Fact] |
| **Industry involved in setting research direction from day one** | "Industry is engaged from the start of each project, jointly shaping the research direction" [N6] | [Fact] |
| **Arranging project meetings with the industry partner, preparing technical slides and reports** | A certain SJ-[Univ] position: "assisting the PI in arranging project meetings with the industry partner," "prepare technical slides and reports" | [Summary]: a search snippet mentioned this, but the SJ-[Univ] Research Associate page opened in this round ([N10b]) does **not** contain this wording. It may be a different posting; **to be verified** |
| **NRF-level reporting and milestone regime** | The NRF corporate lab programme page only states programme goals, phases (Phase 1/2), and funding amounts, and **does not state governance, review, or reporting requirements** [N1]. NTI-[Univ] describes itself as "aligned with the RIE2025 handbook" [N3], but no public text of this handbook was found in this round | **To be verified** |

**[Inference] The typical cadence pieced together is:**

1. **Weekly meeting**: university-side researchers plus the PM; the industry side does not necessarily attend;
2. **Scheduled progress meetings**: with the industry co-lead, possibly monthly, frequency to be verified;
3. **Quarterly review**: both Co-Directors attend, covering milestones, risks, and changes;
4. **Phase review**: the Phase 1 → Phase 2 renewal decision, e.g., RR@[Univ] "completed its first five years before moving into Phase 2" [N1].

Outputs are progress reports, change logs, quarterly review materials, and project entries in Project Online.
### 2.2 Question 1: Does the "research semantics" hold? Yes

- [Fact] These are all research projects, for example the computational engineering work at RR@(target university), ANGEL's energy-efficient AI algorithms [N7], and Hyundai's defect-detection robots [N8]. The researchers are RFs, REs, and PhD students at the target university, which matches the "experiment → result → evidence" workflow described in the first-round files 01/03.
- [Inference] There are two differences from a purely academic group:
  - The party being committed to expands from the "advisor" to include a "corporate co-lead".
  - The criterion for judging results expands from "can it be published as a paper" to include "can it meet the company's milestone metrics".
- As a result, the first-round Option C chain of "commitment → result → evidence" **gains an external acceptor**. The five-value result semantics (achieved, not achieved, partially achieved, conditions changed, not done) also gain a practical use: the quarterly review has to answer them item by item.

### 2.3 Question 2: Does "client–vendor confirmation" hold? The structure holds; the strength of confirmation remains to be validated

- **Supporting evidence** [Fact]:
  - Dual-owner system [N5];
  - Dual-director or tripartite-director structure [N8], [N9];
  - "scheduled progress updates and decision making" and "change log" [N10];
  - Quarterly reviews [N9].
  - Together these show that **the corporate side regularly hears progress updates and makes decisions, and the labs are already recording changes by hand**. This is exactly the structure of the first-round Option E, the "requirements change ledger", except that the object changes from "software requirements" to "research goals and milestones".
- **Missing evidence**:
  - Does the corporate side have to confirm meeting minutes or changes in writing? Not found [To be verified];
  - Who writes the quarterly review materials, how long does it take, and where does the data come from? Not found [To be verified];
  - Have there been disputes in which "the corporate side verbally changed direction and later disowned it"? There is no public evidence either way [Assumption · to be validated].
- **Comparison** [Fact]: The Horizon consortium's DESCA template writes "minutes serve as the formal record of decisions + issued within 10 days + deemed accepted if no objection within 15 days" into the contract [N19]. For corporate labs, **no public clauses of equivalent standing were found**. Such clauses are most likely written into non-public research collaboration agreements (RCAs) [Inference].
- **[Assumption · to be validated] H-CL1**: In at least 2 corporate labs, the corporate co-lead has, within the past 6 months, verbally proposed at least 1 change of direction that was not promptly written into the change log. This item must be validated through interviews.

### 2.4 Question 3: Is there a paying party? A payer exists, but the market is narrow and the procurement chain is long

- **Supporting evidence**:
  - [Fact] Labs are co-funded by companies and the government, for example RR@(target university) Phase 2 with $88M [N1], ANGEL supported by RIE2025 [N7], and Continental-(target university) with S$50M [N3];
  - [Fact] Labs have dedicated project managers and project management systems [N9], which shows there is precedent for "spending money and using tools on project management";
  - [Inference] Quarterly reviews and progress reports are a fixed workload for PMs and PIs, and the time saved can be counted as labor cost.
- **Unfavorable evidence and inferences**:
  - [Inference] **The market is very small**: the target university has 17–25 such labs, the NRF page lists roughly a dozen or so corporate labs nationwide ([N1] lists 14), and adding those at NUS, A\*STAR, and SUTD brings the total to only a few dozen. The "meeting tool" budget of each lab is probably small.
  - [Inference] **Procurement has to clear two gates**: first, the target university's IT, since the university may already have procured Microsoft 365 Copilot or Google tools (an item to be verified in §317 of the first-round file 01); second, the corporate side's IP and confidentiality clauses, which may prohibit handing research data to third-party cloud AI.
  - [Inference] **It is unclear who the buyer is**: it could be the lab PM office, the target university's Vice President (Industry) office (procuring uniformly for all labs), or the corporate side (to see the return on its R&D investment). The three have different motivations.
- **[Inference] Conclusion**: It can answer an interviewer's follow-up that "no one pays in a lab" with: "Corporate-university joint labs have a payer, and there is an established reporting process the product can be embedded into." But it **cannot** answer "how big is the market". To talk about scale, it would need to be generalized to "industry-sponsored university research". US universities generally have progress-reporting clauses aimed at industry sponsors, but most say the reporting frequency is set by the contract ([N32], [N31], both [Summary]), so the evidence for scaling is insufficient.

### 2.5 Existing coverage

- **Single-meeting minutes**: As with every segment, already covered by general-purpose tools.
- **Cross-organization meetings are a blind spot of platform tools** [Fact, R5]: Microsoft Teams Facilitator does not support external meetings, and AI notes support only single-language meetings; Gemini in Meet does not support Chinese, nor multiple languages within the same meeting [R6]. Corporate-university meetings sit exactly at the intersection of "cross-organization (the target university and the company are two tenants) + the mixed Chinese-English common in Singapore".
- **Milestone reporting tools for "university–industry sponsored research"**: This round's search **found no** dedicated product. All that turned up were university policy pages, contract templates, and glossaries [N31], [N32]. RR@(target university) uses the general-purpose Project Online [N9]. This means "not found in search", not "does not exist".
- **Nearest competitive threats** [Fact + Inference]:
  - Fellow's recurring meetings, cross-meeting action items, and two-way GitHub sync [R1];
  - Littlebird's commitment-versus-evidence comparison [R3];
  - Fabric's academic labs page [R8].
  - None of them has a public feature for "external sponsor confirmation" or "milestone mapping". But as noted above, **feature gaps have a very short shelf life**, so the moat should be placed in "cross-organization constraints + research semantics + evaluation".

### 2.6 Scoring (corporate-university joint labs, as a standalone segment)

| Dimension | Score | Rationale |
|---|---|---|
| D1 Unmet need | 4 | Single-meeting minutes are already covered; no product was found for the combination of "meeting → research milestone → corporate confirmation/objection → quarterly review package"; cross-organization and mixed Chinese-English meetings are official limitations of platform tools [R5, R6] |
| D2 Pain-point evidence | 3 | There is solid **process** evidence (weekly meetings, quarterly reviews, change logs, dual owners [N5, N9, N10]), but **no evidence of actual "pain"** (no user quotes, no frequency data), and the job descriptions are all from 2020 |
| D3 Reachability | 4 | [Assumption] There are more than 17 labs inside the target university, the project owners are at the target university, and researchers (RF/RE/PhD) can be approached for interviews through on-campus channels. **But the reachability of the corporate co-lead is only about 2**, and "confirmation by the other party" is precisely what needs to be validated with the corporate side |
| D4 Demo | 4 | Can synthesize "1 milestone plan + 3 weekly meetings + 1 corporate progress meeting + experiment logs → draft quarterly review package + corporate confirmation/objection sheet". Real data is subject to confidentiality restrictions and cannot be obtained |
| D5 Compliance (inverse) | 2 | Corporate IP and confidentiality clauses, possibly export controls (aviation and energy labs); multi-party recording requires consent; the corporate side may prohibit third-party cloud AI [Inference] |
| D6 Willingness to pay | 3 | A payer exists, with funding coming from companies and NRF co-funding, and there is precedent for spending on project management tools; but the market is narrow and the procurement chain is long |
| **Weighted score** | **3.50** | In the same tier as client–vendor (3.70) and academic labs (3.80) (gap under 0.3) |

---
## 3. The Other 4 New Segments (Plus 1 Sub-segment)

### 3.1b IPP / Alibaba Talent Dual-Mentor Industrial PhD (a sub-segment of university–industry joint labs)

- **Typical meetings** [Inference]: Regular three-way meetings among the student, the academic supervisor, and the company supervisor. The student spends half their time at the company and half at the university, and must report on the same project separately to two supervisors.
- **Evidence** [Fact]: The dual-mentor arrangement and "at least 50% of time at the company" are stated on the official page [N12, N13]; the company also "Funds all other costs related to IPP Project" [N12]. **No** frequency requirement for progress reports or three-way meetings was found.
- **[Inference] Unmet need**: The directions given by the two supervisors may conflict, for example "the company supervisor wants a prototype delivered first, while the academic supervisor wants a paper submitted first." The student needs a three-way ledger of "who asked for what, and who agreed to what." This is the smallest-unit combination of Option B (1:1 supervisor ledger) and Option E (counterparty confirmation) from the first round.
- **Scoring**: D1 4 / D2 3 / D3 3 (number of IPP students unknown, to be verified) / D4 4 / D5 3 / D6 2 (students do not pay; the company might, but a single-person scale is too small), **weighted 3.30**.
- **Summary**: **Not listed as a separate segment; merged into university–industry joint labs** as a type of person to ask about specifically in interviews: they are the most direct firsthand witnesses of the "two clients" conflict.

### 3.2 Corporate ML/AI R&D Teams (Non-Hardware)

- **Typical meetings** [Summary + Inference]: A weekly experiment review, looking at a W&B or MLflow dashboard to decide what experiments to run next; then stand-ups and model release reviews. An article by W&B's founder describes how "every team project meeting starts with a review of the latest wandb experiment report" [N29, Summary, author is a vendor founder]. A practitioner review says W&B reports replaced the "weekly 'let me show you my notebook' meeting" [N30, Summary].
- **Existing coverage**:
  - [Fact] **W&B officially has an MCP server**, providing tools such as `query_wandb_tool`, `compare_runs_tool`, and `create_wandb_report_tool` [N25];
  - [Summary] Granola, Fireflies, Fellow, and MeetGeek all have MCP servers that can read action items [N26];
  - [Inference] In other words, **today a user can attach both the Granola MCP and the W&B MCP in Claude and DIY a check of "did the experiments promised in the meeting actually run."** For corporate ML teams, the "meeting ↔ experiment evidence" feature difference is easily replaced by DIY, which is the concrete manifestation in this segment of the conclusion from review 06 that "integration is not a moat."
- **Pain-point evidence**:
  - [Fact] Shankar et al. (arXiv 2209.09125, 2022) interviewed 18 ML engineers and attributed MLOps success or failure to three variables: Velocity, Validation, and Versioning [N27]. The abstract does not specifically mention meetings or communication.
  - [Summary] Idowu et al. (EMSE 2024) surveyed 81 practitioners; among those not using experiment management tools, 52% were unaware of such tools or did not understand their benefits [N28]. This suggests that "experiment tracking" itself is not yet widespread, so "meeting ↔ experiment" is even further down the line.
  - **No** direct complaints from corporate ML teams about "commitments dropped in meetings" were found.
- **Compliance** [Inference]: Corporate data is confidential and needs to pass security review, but there is no heavy industry regulation. Score 3.
- **Payment** [Inference]: They already pay for tools such as W&B and Granola, so willingness to pay and budget are both clear. Score 4.
- **Reachability** [Assumption]: Singapore has AI teams at Grab, Sea, GovTech, AI Singapore, and others, and alumni of the target university work there too, but access would depend on personal networks. Score 3.
- **Demo**: W&B has public projects and public reports that can serve as material (which specific ones are usable is **to be verified**). Score 4.
- **Scoring**: D1 3 / D2 3 / D3 3 / D4 4 / D5 3 / D6 4, **weighted 3.25**.
- **Summary**: Payment is the clearest here, but the DIY substitution threat is the greatest. **The most suitable role is the "control group" suggested by review 06**: interview 3–4 people. If their pain points match the lab's, the differentiation lies in "R&D semantics" rather than "academia"; if they feel "Granola plus the W&B MCP is already enough," then Option C's feature differentiation does not hold up on the corporate side and can only rely on academic settings and cross-organization constraints.

### 3.3 FYP (Undergraduate Final-Year Project) Supervisor Meetings

- **Typical structure** [Summary]:
  - The FYP at the target university's school of computing (SCSE, now CCDS) has an interim report: students submit the interim report to NTULearn and to the supervisor, describing project progress;
  - The supervisor's marking sheet includes items such as "project management," "interim report," and "general initiative and professional responsibility" (marks are 10/5/10 according to search snippets; **the original PDF returned a 500 error and could not be opened, to be verified**) [N16, N17, N18].
  - FYPs at other schools (in Malaysia, HKUST, etc.) require a logbook to be filled in and signed at every supervisor meeting (search snippets; not from the target university). **No information was found on whether the target university requires a logbook.**
- **Existing coverage** [Inference]: General-purpose tools plus Littlebird's student plan ($15/month, [R4]). There is no dedicated FYP product, but the need here is simple (recording, reminders), and general-purpose tools are basically sufficient.
- **Pain-point evidence**: Weak. Only institutional evidence (the marking sheet has a project management component); the burden on supervisors who handle several students at once is an inference. Score 2.
- **Reachability / Demo**: Strongest. The target university has many undergraduates, and some labs probably supervise FYP students. D3 5 / D4 5.
- **Compliance**: Student data, not subject to heavy industry regulation, but there is an ethical concern about being "monitored" in an assessment context. Score 4.
- **Payment**: Score 1.
- **Scoring**: D1 3 / D2 2 / D3 5 / D4 5 / D5 4 / D6 1, **weighted 3.40**.
- **Summary**: **Replaces the first round's "student project groups" as the usability-testing pool**. The reason is that the FYP structure is "one supervisor to many students, with interim and final milestones," which is closer to the interaction patterns of Options B and C and is more representative than course group projects.
### 3.4 Thesis Advisory Committee (TAC) Meetings

- **Typical structure** [Fact]: The target university's SBS rules require a TAC to be formed within 8-9 months of enrolment, with at least 3 members, one of whom must be external to the target university. "The TAC should meet the student at the 9th, 30th and 42nd month". The TAC may "recommend the termination of PhD candidature" [N14]. **The page mentions no requirement for minutes or a form.** At NUS, some faculties require one TAC meeting within 3 months before the PQE report and before thesis submission [N15, [Summary]]. Rules differ by school, and the rules of the user's own school are **to be verified**.
- **[Inference] Unmet need**: TAC recommendations (for example "add a set of ablation experiments" or "narrow the scope") are formally binding, but the two meetings are 21 months apart, so by the next one, who remembers what was said last time? This calls for a ledger of "formal recommendation → response → evidence".
- **Pain** [Inference]: The risk per meeting is high, but the frequency is very low, less than once a year. Score: 2.
- **Reachability**: The target university has many PhD students, so retrospective interviews on "how did you prepare for your last TAC" are possible. But the chance of observing a real TAC meeting within 2-4 weeks is very low. Score: 4.
- **Demo**: Very few samples, so only synthetic data is possible. Score: 3. **Compliance**: It is an evaluative meeting with external members, so recording is sensitive. Score: 3. **Willingness to pay**: 1.
- **Scoring**: D1 4 / D2 2 / D3 4 / D4 3 / D5 3 / D6 1, **weighted 3.05**.
- **Summary**: **Not a segment; downgraded to a feature**: "treat formal review feedback (TAC, qualifying exam, reviewer comments) as a special class of commitment and track it over the long term". This is the same kind of object as the "reviewer-comment mapping" mentioned in the first-round file 03.

### 3.5 Cross-Institution Research Consortia (Horizon Europe consortia, A\*STAR multi-party projects)

- **Typical structure** [Fact]:
  - DESCA is the most commonly used consortium agreement template for Horizon Europe ("most commonly used" is an [Inference]; the template itself is a [Fact]). Its v2.1 (2026-02) specifies:
    - General Assembly "at least once every six months";
    - an optional Work Package Leaders Group "every three months";
    - **minutes are "the formal record of all decisions taken"; a draft is issued within 10 calendar days, and it is deemed accepted if no written objection is received within 15 calendar days**;
    - decisions on newly added agenda items can be vetoed within 15 days of receiving the draft minutes [N19].
  - EU-side reporting requirements: the periodic report is submitted by the coordinator and must update the status of deliverables, milestones and risks, and explain deviations from plan [N20]. The periodic report is also a precondition for payment ([Summary], seen only in a search-result snippet; the original page was not opened).
  - A vendor guide recommends a meeting cadence of "monthly work package leader calls, quarterly all-partner meetings, and annual general assemblies" [N21, vendor].
- **Existing coverage**:
  - [Fact] EMDESK is a tool built specifically for EU project management, covering project management, EC reporting, work packages, and milestone and deliverable tracking, and it also has collaboration features such as video conferencing. **Its homepage does not mention meeting minutes, action items or AI** [N22].
  - [Fact] Teams Facilitator does not support external meetings [R5], while consortium meetings are inherently cross-organisational.
  - [Inference] No dedicated product was found for the chain "consortium meeting → draft minutes → objection window for each party → decisions written into deliverable and milestone status".
- **Reachability** [Fact + Inference]:
  - Singapore has not formally joined Horizon Europe: exploratory talks began in 2024, and the Council of the EU has authorised the opening of formal negotiations [N24, [Summary]]; **as of this round, no source was found showing that an agreement has been signed**.
  - In 2025-12, Singapore launched the "Singapore-Horizon Europe Complementary Fund" to fund domestic entities participating in Pillar II consortium projects [N23]. According to a search snippet, Singapore entities cannot serve as coordinator ([Summary], to be verified).
  - So people at the target university **can participate, but mostly not as coordinator**, whereas the minutes and objection process are handled by the coordinator or chair. Score: 2.
- **Scoring**: D1 4 / D2 4 (mandated by the rules and tied to payment, but lacking first-hand voices on the "pain") / D3 2 / D4 4 (the DESCA text is public and the project structures on CORDIS are public; minutes can only be synthetic) / D5 2 (multi-party consent; EU partners are bound by GDPR) / D6 3 (coordinators' project-management costs; EU project consultancies are potential buyers; the existence of EMDESK shows that this layer has a paying market), **weighted 3.30**.
- **Summary**: **It provides the hardest evidence this round that "confirmation by the counterparty is a rule-based requirement", and it also yields a design pattern that can be borrowed directly**: "draft → objection window → default acceptance → archive of the accepted version". But the user cannot get in, so it **does not enter the Top 3 and serves as a design reference and a mid-to-long-term expansion direction**. The three-party corporate labs in which A\*STAR participates (the ExxonMobil and Hyundai labs run jointly with the target university and A\*STAR) are structurally closer to a "consortium" and can be interviewed together with university-industry joint labs.

---

## 4. Scoring Matrix: New Segments vs. First-Round Top Segments

### 4.1 Necessary corrections to first-round scores (adopting the verification conclusions of the first-round 06 review)

| Segment | Correction | Reason |
|---|---|---|
| Hardware/robotics R&D | D1 lowered from 4 to 3; weighted score lowered from 3.70 to **3.45** | The first round gave 4 on the premise that "nobody has closed the meeting → experiment loop". The 06 review verified that: Fellow already syncs two-way with GitHub [R1]; Littlebird already does a three-state evidence comparison of "commitment vs. what actually happened" [R3]; Circleback, Otter, Granola and others all have MCP, so "integration" is no longer a barrier. What remains is only "experiment semantics", and that applies equally to computational research groups and university-industry labs |
| Client-vendor requirements meetings | **Stays at 3.70**, with a sensitivity note: if D2 drops from 4 to 3, it becomes **3.50** | Review item C6 of 06 points out that file 05 gave its "evidence strength" only 2 points, so U2's D2=4 is optimistic. The evidence is mainly experience articles and law-firm advice, with no frequency data |
| Academic labs (rough scoring in the first round) | Stays at 3.80, marked "rough scoring" | The 06 review holds that the "commitment → result → evidence" chain in research semantics is still remaining differentiation space; but Fabric academic labs [R8] and Littlebird's student edition [R4] have already entered |
### 4.2 Main Matrix (default weights D1 25% / D2 20% / D3 20% / D4 15% / D5 10% / D6 10%)

| Segment | Source | D1 | D2 | D3 | D4 | D5 | D6 | **Weighted score** |
|---|---|---|---|---|---|---|---|---|
| **Combined ladder: own computational lab → university-industry joint lab** | This round's combination | 4 | 3 | 5 | 4 | 3 | 3 | **3.80** (upper-bound estimate, see note) |
| Academic research lab | Round 1 scoring reused | 4 | 3 | 5 | 4 | 4 | 2 | 3.80 |
| Client–vendor requirements meetings | Round 1 #1 | 4 | 4 | 3 | 4 | 3 | 4 | 3.70 (3.50 if D2=3) |
| Student course/competition project teams | Round 1 alternate | 3 | 3 | 5 | 5 | 4 | 1 | 3.60 |
| **University-industry joint lab (standalone)** | This round | 4 | 3 | 4 | 4 | 2 | 3 | **3.50** |
| Hardware/robotics R&D (revised) | Round 1 #2 | 3 | 3 | 4 | 4 | 4 | 3 | 3.45 (originally 3.70) |
| **FYP supervisor meetings** | This round | 3 | 2 | 5 | 5 | 4 | 1 | **3.40** |
| Open-source community | Round 1 #3 | 3 | 3 | 3 | 5 | 5 | 1 | 3.30 |
| **Cross-institution research consortium** | This round | 4 | 4 | 2 | 4 | 2 | 3 | **3.30** |
| **IPP / dual-supervisor industrial PhD** | This round (sub-segment) | 4 | 3 | 3 | 4 | 3 | 2 | **3.30** |
| **Enterprise ML/AI R&D team** | This round | 3 | 3 | 3 | 4 | 3 | 4 | **3.25** |
| **PhD thesis committee / TAC** | This round | 4 | 2 | 4 | 3 | 3 | 1 | **3.05** |

> **Note**: The combined ladder is scored as follows: D3 takes the own-lab score of 5 (dogfooding is possible), D6 takes the university-industry lab score of 3 (there is a paying party), and D5 takes the midpoint of the two, 3. This is an **upper-bound estimate**. It assumes that the two stages can share the same product core (§5.1) and that the user can extend smoothly from their own lab to at least 1 industry lab. If the extension fails, it falls back to the old problem of "academic lab at 3.80, but only 2 points on payment." **A gap of less than 0.3 counts as the same tier**, consistent with the Round 1 rule.

### 4.3 Weight Sensitivity (reusing the three scenarios from Round 1)

| Segment | Default | Commercial priority (D6 20%, D3 10%) | Portfolio/demo priority (D4 25%, D2 15%, D6 5%) |
|---|---|---|---|
| Combined ladder (own lab → university-industry) | 3.80 | 3.60 | 3.90 |
| Academic lab | 3.80 | 3.50 | 3.95 |
| Client–vendor | 3.70 | **3.80** | 3.70 |
| Student project teams | 3.60 | 3.20 | 3.90 |
| University-industry joint lab (standalone) | 3.50 | 3.40 | 3.60 |
| Hardware/robotics (revised) | 3.45 | 3.35 | 3.55 |
| FYP | 3.40 | 3.00 | 3.75 |
| Open source | 3.30 | 3.10 | 3.60 |
| Cross-institution consortium | 3.30 | 3.40 | 3.35 |
| IPP dual-supervisor | 3.30 | 3.20 | 3.45 |
| Enterprise ML | 3.25 | 3.35 | 3.30 |
| TAC | 3.05 | 2.75 | 3.20 |

**[Inference] Interpretation:**

- **The combined ladder and client–vendor are both in the top three under all three weightings.** The structure matches Round 1's "client–vendor + hardware are robust" conclusion, except that hardware has been replaced by the ladder.
- **Under commercial priority, client–vendor ranks first** (3.80 vs. 3.60). This shows that if the interviewer only cares about "who pays and how big the market is," client–vendor is still the better story.
- **None of the newly added segments ranks in the top two in any single scenario.** The value of the university-industry joint lab lies in being **the intersection of two existing routes**, not in its standalone score.
- Enterprise ML and the cross-institution consortium rise slightly under commercial priority, but both are held back by reachability or DIY substitutes.

---

## 5. Updated Top 3 and Rationale (Explicit Comparison with Round 1)

### 5.0 Differences at a Glance

| Rank | Round 1 (U2 §4) | This round's update | Change |
|---|---|---|---|
| 1 | Client–vendor requirements meetings (3.70) | **"Computational research group → university-industry joint lab" ladder** (3.80 upper bound; standalone university-industry 3.50) | New entry |
| 2 | Hardware/robotics R&D (3.70) | **Client–vendor requirements meetings** (3.70, sensitivity 3.50) | Down from 1st to 2nd, role changed |
| 3 | Open-source community → issue (3.30) | **Open-source community → issue** (3.30) | Unchanged, still an evaluation venue |
| Dropped | — | Hardware/robotics (3.45) | Fell out after revision; the robotics angle is absorbed into the ladder, and enterprise labs in robotics are prioritized for interviews |
| Role change | Student project teams = interview pool | **FYP supervisor meetings = usability-testing pool** (replaces student project teams) | Closer to the one-supervisor-to-many form |
| New role | No control group | **Enterprise ML team = control group** (3–4 people) | Adopts the suggestion from 06 |
| New role | — | **Cross-institution consortium = design reference** (DESCA objection-window mechanism) | New |
| New role | — | **TAC = feature source** (formal review-comment ledger) | New |

### 5.1 Top 1: Computational Research Group (Wedge) → University-Industry Joint Lab (Paid Extension)

- **Sharpest unmet need**: **"Quarterly review pack + funder objection window."**
  1. At each weekly group meeting or operations meeting, extract "experiment commitments" using Round 1's Option C, and reconcile them against experiment evidence (W&B runs, Git, logs) before the next meeting;
  2. The system automatically attaches commitments and results to **contract milestones**, forming a rolling ledger of "milestone × commitment × evidence × five-valued outcome";
  3. After each progress meeting with the company, generate a one-page draft "decisions and change order" and send it to the company-side co-lead. **Borrowing the DESCA mechanism: no objection within N days counts as acceptance; any objection is flagged item by item**;
  4. Before the quarterly review, generate a draft review pack in one click, with every conclusion carrying a citation (the location of the verbatim meeting quote, and links to experiment evidence).
- **Why this one** [Inference]:
  - **It is the only scenario where Round 1's Option C (research evidence chain) and Option E (counterparty-confirmed change ledger) naturally overlap.** One core can answer both of the interviewer's questions: "How is this different from Feishu?" (research semantics + cross-organization confirmation) and "Who pays?" (company-funded labs).
  - **Its differentiation comes mainly from constraints, not features.** The pattern from the 06 review is: "Feature gaps get filled quickly, while constraint-type gaps are instead confirmed by official documentation." University-industry meetings hit three constraints at once: cross-organization (Teams Facilitator does not support external meetings [R5]), mixed Chinese-English speech (Gemini does not support Chinese or multiple languages in the same session [R6]), and IP confidentiality (local or private processing is required). This is more durable than "a feature nobody has shipped yet."
  - **Reachability**: the wedge stage is the user's own lab, where dogfooding is possible; the extension stage is at the same university, which has 17+ labs, and the robotics-focused partners Hyundai, AUMOVIO, Schaeffler, and SHARE are close to the user's research direction.
- **Its weaknesses (must be stated proactively)**:
  - There is no public evidence for how strongly the company side confirms things (§2.3);
  - The market is narrow (§2.4);
  - The compliance score is only 2 (§2.6); real data is almost impossible to obtain, so the demo can only use synthetic data plus de-identified data from the user's own lab.
- **Hypotheses to validate**:
  - **H-CL1**: Company-side direction changes are sometimes "raised verbally and hard to trace afterwards" (see §2.3);
  - **H-CL2**: Preparing a quarterly review pack takes a PM or PI at least half a day of "archaeology," compiling from weekly meeting notes, emails, and experiment logs;
  - **H-CL3**: The company-side co-lead can accept "default acceptance + objection window" rather than being asked to click to confirm item by item;
  - **H-CL4**: The lab's research collaboration agreement (RCA) or the company's IT allows AI processing of meeting text in a local or university-hosted environment.
- **Kill criteria (after 2 weeks of interviews)**:
  - If **none** of the 3 enterprise labs holds "regular meetings with the company side, with written progress or change records," fall back to the pure academic lab route (the payment problem remains);
  - If all of them forbid any AI processing (even local), pivot to the client–vendor route.
### 5.2 Top 2: Client–vendor requirements meetings (kept, but moved from 1st to 2nd)

- **Why it stays in the top three**: It is in the top three under all three weightings and ranks first under the commercial-priority weighting. It maps directly to the scenario the interviewer challenged, and no mature product has been found for "cross-meeting requirement diff + counterparty confirmation sheet" (Round 1 U2 §2.12).
- **Why it drops to 2nd** [Inference]:
  1. Both 05 and 06 point out that its evidence is the weakest (06 C6), and the project owner has no scenario of their own to dogfood it in;
  2. Its core mechanism, "counterparty confirmation", can be **validated first in university–industry labs**, where an institutional skeleton already exists and users are reachable. After validation, it can be generalized to software outsourcing and agencies.
- **Change of role**: From "main-line segment" to "**external generalization narrative**". In interviews it can be framed like this: "The core is validated first in university–industry research collaborations with institutional constraints, then transferred to software outsourcing, which has the same 'baseline + change + counterparty confirmation' structure."

### 5.3 Top 3: Open-source community meetings → issues (unchanged)

- **Why it is not swapped for cross-institution consortia**: The two score the same, 3.30. Open source is **the only segment where quantitative evaluation can use real public data (recordings, minutes, issue history)** (Round 1 U2 §2.7). Consortium minutes are not public, so only synthetic data could be used, and users are not reachable.
- **Role unchanged**: It is the evaluation main line, not the commercial main line. It supplies Top 1 and Top 2 with credible numbers for "decision → external object matching accuracy".

### 5.4 How to use the new segments that did not make the Top 3

| Segment | Role | Specific use |
|---|---|---|
| Enterprise ML teams | **Control group** | Interview 3–4 people. If they say "Granola MCP plus W&B MCP is good enough" [N25, N26], it means the research evidence chain would be replaced by DIY on the enterprise side, and Top 1's differentiation can only rest on cross-organization and academic constraints |
| FYP supervisor meetings | **Usability-testing pool** | Replaces student project groups; used to test the "one supervisor to many students" dashboard and the student back-fill rate (the Round 1 05 Q4 failure line is 50%) |
| IPP / dual supervisors | **Key population in Top 1 interviews** | They are the smallest unit of conflicting direction between "two clients", and the most likely witnesses for H-CL1 |
| TAC | **Feature point** | A "formal review-comment ledger": TAC comments, qualifying-exam comments and peer-review comments are all tracked as "comment → response → evidence" |
| Cross-institution consortia | **Design reference + mid-to-long-term expansion** | Adopt DESCA's "draft issued within 10 days, 15-day objection window, deemed accepted by default, accepted version archived" as the default rule for the confirmation interaction; Singapore's Complementary Fund [N23] can serve as an expansion path later |

---

## 6. Next steps (input to 03_positioning and the interview plan)

1. **Book interviews in weeks 1–2 (to validate D3 and H-CL1 to H-CL4)**:
   - University–industry labs: 3 researchers or PMs on the target university side, prioritizing Hyundai–(target university)–A\*STAR, AUMOVIO–(target university), Schaeffler–(target university) and RR@(target university); 1–2 co-leads on the corporate side (hardest to reach; the target university side can be asked to introduce them); 1–2 IPP or Alibaba Talent participants.
   - Control group: 3–4 enterprise ML engineers.
   - Example Mom Test questions: "Before your last quarterly review, how long did it take you, and from where did you piece the material together?" "The last time the corporate side changed direction, how was it recorded? Did anyone later disagree about what was actually said at the time?" "What does your collaboration agreement say about giving meeting content to AI tools?"
2. **Items to verify**:
   - The reporting and review regime of the NRF corporate labs (the public version of the RIE2025 handbook);
   - Why Continental was renamed AUMOVIO; when HP–(target university) changed from Corp Lab to Joint Lab;
   - Whether RR@(target university) has a Phase 3 after Phase 2;
   - The original text of the FYP grading forms of the target university's CCDS and EEE (the PDFs returned 500 this round);
   - The TAC rules of the user's own school;
   - Whether a Singapore entity can act as coordinator in a Horizon project.
3. **Demo data preparation**: Use DESCA-style "objection window" rules to synthesize "milestone plan + 4 weeks of meetings + corporate progress meeting + experiment log". In addition, take 2–3 weeks of group-meeting minutes from the author's own lab (anonymized) as the data for the wedge segment.

---

## 7. Confidence of this document's conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| The 5 named labs exist, plus the list and status | **High** | The target university's list, the NRF list and the EDB press release were all opened and checked against the originals; the reason for the renaming is an inference |
| University–industry labs have weekly meetings, quarterly reviews, change logs and dual leads | **Medium** | All are [Fact], but the job descriptions date from 2020; the dual leads come from the target university's official news |
| The corporate side formally confirms minutes or changes | **Low** | No public evidence at all; entirely pending interviews |
| University–industry labs "have a paying party" | **Medium** | Precedents for funding and tool spending are facts; "willing to pay for this kind of tool" and "who signs the order" are both inferences |
| DESCA's multi-party confirmation mechanism | **High** | Checked verbatim against the original model contract (v2.1, 2026-02) |
| Enterprise ML teams would DIY with MCP instead | **Medium** | The official W&B MCP is a fact; "users would really assemble it this way" is an inference |
| The new Top 3 ranking | **Low to medium** | Score gaps are all within 0.3, so ranking rests mainly on qualitative reasons, and D3 is entirely assumption |

**Not covered or weak**:

- No interviews at all;
- NUS and A\*STAR corporate labs were not verified one by one;
- Chinese university–industry joint labs (for example, joint labs between domestic universities and companies) are outside the scope of this round;
- Evidence for enterprise ML team pain points consists only of the abstracts of two papers and vendor-related practitioner articles.

---

## Source list (all accessed at the time of writing)

> Legend: (opened) = the original was opened with WebFetch and checked this round; (summary) = only the search-result summary was seen; (vendor) = vendor self-description; (R) = verified in the Round 1 06 review, not reopened this round.

**New this round (N)**

- N1 NRF Corporate Laboratories programme page (opened) https://www.nrf.gov.sg/programmes/corp-labs/
- N2 The target university's Industry Partnerships list (17 labs, opened) (university page; link removed)
- N3 The target university's EEE Corporate and Joint Research Laboratories (opened) (university page; link removed)
- N4 The target university's Vice President (Industry) Office page ("25 corporate and joint labs", opened) (university page; link removed)
- N5 News from the target university, "Putting research to work" (2024-09-06; "each research project is led from the start by a professor from the university and a company scientist or engineer", opened) (university page; link removed)
- N6 News from the target university, "Fast-tracking innovation with industry titans" (2025-06-12, opened) (university page; link removed)
- N7 EDB: the target university and Alibaba Group launch corporate lab (ANGEL, 2024-09-12, opened) (link removed)
- N8 Hyundai Motor Group press release: Hyundai–(target university)–A\*STAR Corporate Lab (2025-10-13, opened, vendor) https://www.hyundai.com/worldwide/en/newsroom/detail/0000001025
- N9 THE UniJobs: Rolls-Royce@(target university) Corporate Lab Senior Project Manager (deadline 2020-08-23, opened) https://www.timeshighereducation.com/unijobs/listing/214963/senior-project-manager-engineering/
- N10 THE UniJobs: SJ–(target university) Corporate Lab Research Engineer (deadline 2020-11-13, opened) https://www.timeshighereducation.com/unijobs/listing/229527/research-engineer/
- N10b THE UniJobs: SJ–(target university) Corporate Lab Research Associate (opened, no meeting or reporting duties seen) https://www.timeshighereducation.com/unijobs/en-au/listing/229203/research-associate-computer-engineering/
- N11 The target university's Rolls-Royce@(target university) introduction page (summary; the about-us page returned 404) (university page; link removed)
- N12 The target university's Graduate College: Industrial Postgraduate Programme (IPP) (opened) (university page; link removed)
- N13 The target university's CCDS: Alibaba Talent Programme (opened; the page's deadline is in 2024, current status to be verified) (university page; link removed)
- N14 The target university's SBS: Thesis Advisory Committee (TAC) (opened) (university page; link removed)
- N15 NUS Medicine: Thesis Advisory Committee (summary) https://medicine.nus.edu.sg/graduatestudies/current-students/examination-matters/thesis-advisory-committee
- N16 The target university's SCSE FYP Supervisor Assessment Form (summary; PDF returned 500) (university page; link removed)
- N17 The target university's SCSE FYP Important Dates Aug 2024 (summary; PDF returned 500) (university page; link removed)
- N18 The target university's SCSE FYP Report Guide (summary) (university page; link removed)
- N19 DESCA Model Consortium Agreement for Horizon Europe v2.1 with elucidations (2026-02; PDF downloaded, full text extracted locally, §6.3.2.1, §6.3.5.3, §6.3.6 and the Work Package Leaders Group module checked) https://www.desca-agreement.eu/assets/helmholtz_gemeinschaft/user_upload/Brussels_Office/DESCA/2026/20260228_DESCA_HorizonEurope_.2.1_with_elucidations_final.pdf
- N20 PNO Innovation: Reporting in Horizon Europe (opened, consultancy) https://www.pnoinnovation.com/insights/reporting-in-horizon-europe/
- N21 EMDESK: Managing Horizon Europe Projects guide (opened, vendor) https://www.emdesk.com/horizon-2020-horizon-europe-basics-guide/horizon-europe-project-management-guide
- N22 EMDESK homepage (opened, vendor) https://www.emdesk.com/
- N23 European Commission: Singapore launches Horizon Europe complementary fund (2025-12-12, opened) https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/singapore-launches-horizon-europe-complementary-fund-strengthening-research-and-innovation-2025-12-12_en
- N24 EUR-Lex: Council Decision (EU) 2024/2971 (summary) https://eur-lex.europa.eu/eli/dec/2024/2971/oj
- N25 GitHub: wandb/wandb-mcp-server (official W&B MCP server, opened) https://github.com/wandb/wandb-mcp-server
- N26 Granola: Granola MCP blog (summary, vendor) https://www.granola.ai/blog/granola-mcp-claude-chatgpt-cursor
- N27 Shankar et al., "Operationalizing Machine Learning: An Interview Study", arXiv:2209.09125 (abstract page opened) https://arxiv.org/abs/2209.09125
- N28 Idowu et al., "Machine learning experiment management tools: a mixed-methods empirical study", EMSE 2024 (summary; the Springer page requires login) https://www.cse.chalmers.se/~bergert/paper/2024-emse-expmgmt.pdf
- N29 Lukas Biewald, "Machine learning experiment tracking" (summary; the author is the W&B founder) https://medium.com/@l2k/machine-learning-experiment-tracking-93b796e501b0
- N30 Enterprise DNA: Practitioner review of Weights & Biases (summary) https://enterprisedna.co/resources/blog/practitioner-weights-biases
- N31 CASRAI: Project milestone term (summary) https://casrai.org/rdm-glossary/term/project-milestone
- N32 Wayne State University: Sponsoring research (summary) https://techtransfer.wayne.edu/techtransfer/industry/sponsoring-research
**Verified in the first round and carried over this round (R)**

- R1 Fellow GitHub integration (two-way sync) https://fellow.ai/integrations/github
- R2 Fellow action items (no "assignee confirmation" seen) https://fellow.ai/features/action-items
- R3 Littlebird Promise Tracker (Kept / In progress / Needs a note; "Vague maybes are skipped") https://littlebird.ai/routines/promise-tracker
- R4 Littlebird pricing (Team plan, student pricing) https://littlebird.ai/pricing
- R5 Microsoft Learn: Facilitator in Teams (external meetings not supported, single language only) https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
- R6 Google Meet "Take notes for me" supported languages (no Chinese, no multiple languages within the same meeting) https://support.google.com/meet/answer/14754931
- R7 Feishu smart minutes (meeting digest, enterprise information recognition, mixed Chinese-English recognition) https://www.feishu.cn/content/article/7577317993749269689
- R8 Fabric academic labs (marketing page, no customer case studies) https://fabric.so/teams/academic-labs
- R9 Granola integrations (connects to GitHub/Linear/Jira via Zapier) https://www.granola.ai/integrations
- R10 Granola class-action lawsuit (2026-07-30, 3:26-cv-07926-EMC) https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
