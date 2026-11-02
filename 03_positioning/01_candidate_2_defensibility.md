---
title: "Positioning Candidate 2 (Defensibility Perspective): 'Experiment-Commitment Reconciliation That Never Leaves Campus': The First 5 Minutes of a Computational Lab's Group Meeting"
status: draft-candidate (one of the candidates, pending 03_positioning review; no user-side conclusion has been validated through interviews)
sources_count: 35
sources_count_method: number of unique URLs in the sources section (recounted at wrap-up; original value 34)
perspective: defensibility (7 Powers / counter-positioning / vertical workflow encoding / proprietary evaluation assets)
---

# Positioning Candidate 2 (Defensibility Perspective): Experiment-Commitment Reconciliation That Never Leaves Campus

> **Reading notes**
> - This file answers one question only: **if we must pick one option, and must first answer "why won't Feishu, Otter, Fellow, or Littlebird copy it within three months?", which option do we pick and why?**
> - Labels follow the project-wide convention: **[Fact]** has a source URL and the original page was opened; **[Summary]** was seen only in a search snippet or secondhand account; **[Inference]** is derived from facts; **[Assumption · to be validated]** needs interviews or experiments. Sources that could not be opened are marked "to be verified". All official sources were accessed on **at the time of writing**.
> - **Inputs**: fully read `00_pm-skills/03` (positioning method), `01_market-research/05` (gap synthesis, options A–F), `06` (review), `07` (supplementary verification of commitment-tracking competitors), `08` (academic benchmarks), `02_user-research/05` (new segments), and `05_demo-plan/eval-kit/README.md`; read the conclusions, scores, and credibility sections of the remaining files, and searched their bodies as needed (`00_pm-skills/01, 02, 04, 05, 06`, `01_market-research/01–04`, `02_user-research/01–04, 06`).
> - **Newly verified this round (WebFetch/WebSearch)**: ① re-opened the Littlebird graduate-student page; ② re-opened the original page of the target university's "Position on Generative AI Use in Research" (including the RCA conditions); ③ a report on NUS opening ChatGPT Edu to the whole university; ④ searched for an existing "meeting action item ↔ W&B run" integration (none found).
> - **A stance that must be stated first**: per the observation in 07 §8, feature-presence gaps get filled roughly once a quarter (Fellow's claim mechanism shipped on 2026-10-01). This document therefore **does not claim a moat**. It claims this: pick **a position the big players have reason not to occupy**, then use **a compounding evaluation asset** to hold that position for a while. The exact wording of one reminder is "The workflow you ship on day one is not the moat" (00/03 §7.2, citing a16z).

---

## 0. Conclusion First

1. **Recommended option (one sentence)**: BriefPilot v2 does one thing only: in the **"last week's commitments review" at the start of the weekly group meeting of a computational (ML / robotics / VLA) lab**, it maps each **experiment commitment** spoken aloud last week to this week's **experiment artifacts** (W&B runs, Git commits, configs), and marks the scientific conclusion and the evidence. **The whole process runs on the lab's or the university's own compute, and no meeting content is handed to any external cloud service**; when the owner, the date, or the evidence is missing, it writes `UNKNOWN` explicitly and does not guess.
2. **The "one small bit" of unmet need (down to the exact step)**:
   > At the opening of the group meeting, the PI asks, "Did last week's baseline run? How did it turn out?" That question needs an answer **within 3 seconds**: "who promised what last week (original sentence) → which run/commit it corresponds to → what the conclusion is / there is no evidence yet." And this step **must be completed on the premise that group meeting content never leaves campus**.
   - Today this step is done by "students reporting verbally from memory + the PI following up from memory" (one lab's handbook writes "Review last week's action items" as an opening step of the meeting [Fact, 07 P7]).
   - Existing products each cover one piece: Fellow carries over unfinished items (binary), Littlebird does a weekly three-state check (with email and documents as evidence), and Feishu's meeting digest summarizes a week of action items. **But no vendor has swapped the evidence source for experiment artifacts, and none can do it under the condition that "data never leaves campus"** (§2, §5).
3. **Why this option (the three legs of defensibility)**:
   - **Counter-positioning (main leg)**: all four competitors are cloud-hosted products whose revenue and product iteration are built on "hosting your meeting data." Building, for a niche research segment, a form in which "the vendor can never see the meeting content" would run against their own business model (§6.1). The target university's GenAI research policy turns "stays on campus" from a preference into a rule ([Fact], §4.3).
   - **Vertical workflow encoding (second leg)**: the rules for reconciling commitments against experiment artifacts, the extraction discipline of "write UNKNOWN when missing," and mixed Chinese-English research terminology are the seeds of "process power," written into the schema and the annotation guidelines, and they take repeated calibration in real group meetings to get right (§6.2).
   - **Proprietary evaluation asset (proof and compounding)**: neither academia nor the product world has an evaluation of "mixed Chinese-English research group meetings × field-level (owner / deadline / strength / evidence) × UNKNOWN allowed × real outputs from multiple commercial products" (08 §0 item 4, §3.5 summary [Inference, not found within the search scope]). Competitors could build such an asset themselves, but have no motivation to do so **publicly** (§6.3).
4. **Honest limits**:
   - Today **not a single Power has taken shape yet**, only seeds. The reason competitors "won't copy it" within three months is **motivation**, not **capability**.
   - The biggest risks are **Littlebird** (already has a graduate-student page, student pricing, and three-state commitment checks) and a **DIY assembly of "Granola/Fellow MCP + W&B MCP + Claude"** (§8).
   - Counter-positioning holds only if "group meeting content is treated as restricted research data at the target university, and the university has not approved an enterprise cloud AI tool that covers it." NUS has opened ChatGPT Edu to the whole university starting 2026-08 ([Fact, media], §4.3); **if the target university does the same, the main leg will weaken noticeably**. This must be settled in week 1.
5. The **30-second answer** is in §9; the **demo magic moment** is in §10; the **make-or-break assumptions** are in §11.

---
## 1. Derivation: Why Starting from "Defensibility" Lands Here

### 1.1 Step 1: First delete the candidates that "could be matched within one quarter"

| Candidate differentiator | Status after Round 2 verification | Probability of being matched within one quarter [Inference] | Handling |
|---|---|---|---|
| G4 Assignee acceptance | **Already covered**: Fellow "any assignee can accept or dismiss it"; auto-accept is off by default (2026-10-01) [Fact, 07 F8] | Already happened | Delete |
| G11 Cross-meeting tracking (binary) | **Already covered**: Fellow Always/Never/Ask me, ZoomMate weekly action items, Feishu meeting digest [Fact, 07 §8] | Already happened | Treat as infrastructure only |
| G10 Weekly report slot | **Already covered**: general-purpose LLMs, Feishu, Littlebird, Fabric [07 §8] | Already happened | Delete |
| G2 Traceability to the original sentence | Feishu "supports tracing action items back to the original meeting text" [Fact, 07 C7] | Already happened (Chinese market) | Treat as a passing bar only |
| G3 Commitment-strength label | Littlebird skips "vague maybes" [Fact, 07 L4] | High: a single field | Treat as a passing bar; counts as a differentiator only if **evaluable** |
| G6 Advisor confirmation gate | University systems in the UK already occupy the confirmation step (Loughborough Co-Tutor, Surrey) [Fact, 07 U3–U4]; Littlebird graduate-student page [Fact] | Medium-high: Littlebird adding "share with advisor" is a small iteration | Do not build a confirmation gate |
| G8 Mixed Chinese–English terminology | Feishu "recognizes in the original language" and enterprise-term recognition [Fact]; AssemblyAI native support from 2026-08 [Fact, U4] | Medium-high: the ASR layer is catching up | Treat as an evaluation dimension only |

**What remains** is the judgment in 07 §8.1: two lines, **"research semantics × evidence source"** and **"two-sided × institutional formats"**, plus the cross-cutting **constraint-type gap** (06 §1 pattern: "feature gaps get filled fast, whereas constraint-type gaps are instead confirmed by official documentation").

### 1.2 Step 2: Among what remains, ask "why wouldn't competitors want to do it", not "can competitors do it"

Helmer's reverse-positioning logic is that an incumbent's failure to follow is a "rational response", because following would damage its existing business (00/03 §4.1, secondhand summary, original book to be verified). Going through the items by this standard:

| Remaining gap | **Can** competitors do it? | **Do** competitors **want** to? | Defensibility |
|---|---|---|---|
| Swap the evidence source to W&B/Git | Yes (W&B has an official MCP [Fact, U5 N25]) | Probably not: the research niche is too small and not on their roadmaps [Inference] | Weak: purely a feature, one connector |
| Five-valued research outcome | Yes (one custom field) | Probably not | Weak, and the demand itself is an [Assumption] (06 W10) |
| Advisor two-sided confirmation + university forms | Yes | Singapore lacks institutional leverage (07 U7) | Weak |
| **Meeting content never goes to the vendor's cloud** | Technically yes (self-hosted edition) | **No**: it hurts hosted-tier revenue, data-driven product improvement, and per-seat cloud billing [Inference] | **Medium: the only one that rests on the competitor's incentives** |
| **Write UNKNOWN when information is missing; never auto-create tasks** | Yes | Partly no: the mainstream selling point is "more automatic" (Fireflies "Create tasks automatically", Krisp "automatically assigns", ZoomMate "assign tasks" [Fact, 05 K4, 07 Z4]) | Weak: Fellow already turned auto-accept off by default, which shows some are willing to be conservative |
| **Public field-level evaluation of Chinese–English mixed research group meetings** | Yes | Don't want to do it **publicly**: publicly testing competitors is free advertising for them, and testing themselves is risky [Inference] | Medium (as proof); compounds with corrected data |

**[Inference] Conclusion**: Taken individually, every one of these can be copied. But when "**experiment-artifact evidence** (feature) × **data stays on campus** (constraint, reverse positioning) × **public evaluation** (proof)" are stacked on one specific step, a competitor has to do three things at once that it has no incentive to do. This is the "shape" of the proposal: it is not that any single item ranks higher, but that the value curve has a different shape (the ERRC test in 00/03 §2.2).

### 1.3 Step 3: Compress the three into one step

At which specific step are all three **simultaneously** useful?

- Experiment-artifact evidence is useful only when "looking back at last time's commitments" → the step must be the **review at the start of the next meeting**, not in-meeting note-taking and not a post-meeting summary.
- Keeping data on campus is a hard constraint only when "the content is unpublished research data" → the scenario must be the **research group meeting**, specifically a computational lab (artifacts live in W&B/Git and can be linked).
- Public evaluation needs reproducible data → the three consecutive weekly group meetings M2→M3→M4 in the eval-kit happen to embed 30 cross-meeting links ([Fact, eval-kit gold statistics; synthetic data]).

This yields the single step described in §0.

---

## 2. Competing Alternatives (Dunford element 1: if BriefPilot did not exist, what would they do)

> Ordered by "what users would realistically choose", not by fame. For the persona, see §5.

| # | Alternative | How it handles "reviewing last week's experiment commitments at the start of the group meeting" | Where it falls short | Evidence |
|---|---|---|---|---|
| 0 | **Do nothing** (verbal review + memory) | The PI asks, the student recalls on the spot and digs through W&B for charts | No original sentence, so the content of a commitment gets "embellished after the fact"; nobody tracks the PI's own commitments; soft and real commitments are mixed together | Rashid Lab handbook "Review last week's action items", "confirm assignees and due dates" [Fact, 07 P7]; Liu et al. CHI'20 hindsight bias [Fact, U3 §5.1]; Bahlai "long-term goals keep falling through the cracks" [Fact, M3 §2.1] |
| 1 | **Manual template** (Google Doc/Notion/HackMD group-meeting minutes + manual check next week) | A rotating member takes the minutes, and next week someone remembers to check | Depends on people sticking with it; minutes are not linked to runs; the biggest obstacle in the Duke case was "members don't update, requiring continuous supervision" | [Fact, 05 G5 citing PMC12401938]; M3 §2.1 |
| 2 | **ChatGPT/Claude + pasted minutes** | Paste last week's and this week's minutes and ask "which were done" | **No persistent ledger**, starting from zero every time; not linked to experiment artifacts; **pasting real group-meeting content into an external GenAI at the target university requires meeting 4 conditions at once** (including "data is not retained") | The target university's GenAI research policy [Fact, §4.3]; 07 §5 summary [Inference]; ChatGPT Record "works best in English today" [Summary, 07 A4] |
| 3 | **DIY assembly: Granola/Fellow MCP + W&B MCP + Claude** | Have Claude read action items from the meeting tool and runs from W&B at the same time | Technically **can assemble most of it** (this is the strongest alternative); but the meeting data goes into Granola's/Fellow's cloud first; no "don't guess when missing" evaluation discipline; no persistent schema | Fellow MCP `get_action_items` [Fact, 07 F14]; W&B official MCP `query_wandb_tool`, `compare_runs_tool` [Fact, U5 N25]; Granola MCP [Summary]; U5 §3.2 inference |
| 4 | **Littlebird (graduate-student page)** | Monday routine lists "what you promised your advisor"; pre-meeting brief includes "what you committed to, the feedback still open"; weekly check of commitments "against what actually happened" | Evidence sources are email, calendar, files, and screen; **the integrations named in the FAQ are Gmail, Google Calendar, Google Drive, Outlook, Dropbox**, with no W&B/GitHub seen; "stay private to you unless you choose to share" means a single-person view; cloud product | [Fact] https://littlebird.ai/for/graduate-students (reopened at the time of writing); https://littlebird.ai/routines/promise-tracker [Fact, 07 L1–L4] |
| 5 | **Fellow** | Recurring meeting series automatically carry over unfinished items; AI-suggested items must be accepted by the assignee | Status is only complete / archived ("won't do"), with no outcome or evidence field; the pre-meeting brief looks only at the previous meeting and is Business+ only; no link from action item to original sentence seen | [Fact, 07 F4, F5, F8, F11, F12, F20] |
| 6 | **Feishu/Lark Minutes + meeting digest** | Weekly action-item roll-up; action items traceable to the original text; mixed Chinese–English recognized in the original language | No assignee acceptance, no outcome field, no experiment artifacts; cloud; Lark international edition's capabilities in Singapore to be verified | [Fact, 07 C5–C11]; 06 §3 Lark to be verified |
| 7 | **W&B Reports** | Students use a report to present the week's experiments | Has numbers and charts, but no context of "which commitment of whose this run was meant to fulfill"; does not touch meetings | [Fact, U3 §4.1 W&B Reports documentation] |
| 8 | Supervisor Meeting Brief (Chrome extension) | Manually fill in "me / supervisor / both" action items, with a "From last meeting" panel | No AI, manual, 0 ratings | [Fact, 07 P4] |

**[Inference] How to read this**: The real competitors are **0 (do nothing)** and **3 (DIY assembly)**, not Otter. This is a direct expression of Dunford's "no decision is the biggest competitor" (00/03 §1.4). Otter is almost absent from this scenario: it officially supports only English, Spanish, and French [Fact, eval-kit README §2.2 citing otter.ai/mp3-to-text].

---
## 3. Unique Attributes (Dunford Element 2)

> "Unique" holds only **within this one workflow step × this one user type**. Carried over to a generic meeting scenario, every item becomes "others have it too".

| # | Attribute | Current competitor status | Source of uniqueness | Label |
|---|---|---|---|---|
| U1 | **Commitment ↔ experiment-artifact reconciliation**: last week's experiment commitments are automatically matched to candidate runs/commits/configs, and a person confirms with one click | Littlebird checks emails/documents; Fellow syncs GitHub issue status via Zapier; no meeting tool connected to W&B runs has been seen | Feature (easy to copy) | [Fact] competitor status; [Fact · not seen within search scope] W&B meeting integration (not seen in this round's WebSearch) |
| U2 | **Deployment that stays on campus**: the LLM provider can be switched to the local machine (Ollama) or a university cluster; raw minutes are not uploaded by default | All four competitors process in the cloud; Granola: "Transcription and AI summarization use cloud processing" [Fact, 06 V14] | **Constraint + counter-positioning** (the hard one to copy) | [Fact] competitor status; [Inference] competitors do not want to build this |
| U3 | **Field-level "no guessing"**: when owner, due date, or evidence is missing, output `UNKNOWN`, and publish this as an evaluation metric | Feishu "can be filled in manually", DingTalk assigns to the initiator by default [Fact, single hands-on test]; Fellow requires an accept before taking effect | Discipline + evaluation (medium) | [Fact] competitor status; effect [Assumption · to be validated] (eval-kit H3, H4) |
| U4 | **Public evaluation**: Chinese-English mixed research group meetings × field-level × UNKNOWN allowed × side-by-side with real competitor outputs | No vendor publishes action-item accuracy [Fact: not seen within search scope, 05 K1]; academic benchmarks are sentence-level binary classification [Fact, 08 §0] | Asset (medium, compounds over time) | [Inference] incremental judgment in 08 §5.2 |
| U5 | **The PI's own commitments are also on the ledger** (eval-kit groups recall by owner) | No product has been seen that specifically evaluates missed extraction of "the advisor's own commitments" | Evaluation slice (weak) | [Assumption · to be validated] the need itself has zero direct evidence (05 G6 objection 1) |

**Deliberately not listed as unique attributes**: citations, human confirmation, carrying items across meetings, assignee claiming, no bot, no training on data, GitHub integration. All have been confirmed as "others have it too" (05 §0, 06 §8, 07 §8).

---

## 4. Value and Evidence (Dunford Element 3)

### 4.1 Value Clusters (at most 3)

| Value cluster | For whom | Supported by attributes | Current evidence | Gap |
|---|---|---|---|---|
| **V1 Opening a group meeting without "archaeology"**: the status of last week's experiment commitments is visible in 3 seconds, with the original sentence and the run | Students, PI | U1, U3 | Institutional evidence: MIT Cahoy, "review these items at subsequent meetings" [Fact, U3 §3.1]; Rashid Lab opens with a review [Fact]; Imperial's agenda opens with "results since last time" [Fact, 05 G5] | **No frequency or cost data** (H01–H03 await the diary study) |
| **V2 Using AI on group meetings in a compliant way**: no forced choice between "using AI" and "following policy" | PI, industry-academia lab PM | U2 | Target university policy [Fact, §4.3]; the funder's demand in the M5 synthetic meeting that "data must not go to a public cloud" is only a **synthetic storyline, not evidence** | Need to confirm it is a "threshold" rather than a "preference" (H08); need to confirm whether the target university has an approved enterprise cloud tool |
| **V3 AI output that can be trusted in a quantified way**: knowing which kinds of items it gets wrong | PI, interviewers, procurers | U3, U4 | 05 K1; 08 §5.2; eval-kit is executable but **has not yet been run** | All numbers await actual eval-kit measurement |

### 4.2 Newly Verified in §4.3: The Target University's Generative AI Research Policy (Factual Foundation for Counter-Positioning)

- [Fact] The target university's "Position on the Use of Generative Artificial Intelligence in Research" ((university page; link removed), published 2023-07-04, reviewed 2025-11-07, accessed at the time of writing): "Any confidential or sensitive information, and/or personal data must not be uploaded to any external GenAI software, system, or platform unless" four conditions are all met: it does not violate laws or institutional policies; access is limited to authorized research members; **"The data is not retained in or by the GenAI"**; and, where applicable, written permission from the data owner is obtained, **or "the use of such GenAI has been agreed upon in the Research Collaboration Agreement (RCA)"**.
- [Fact] Same page: the page **does not name any enterprise-grade GenAI tool approved by the target university**; ChatGPT, Copilot, and Gemini appear only as examples of GenAI.
- [Fact] The target university's research data policy: "The University owns all research data produced by research projects", and data must be stored on facilities where the "University has full access and control" (00/06 §4.5).
- [Fact, media] NUS and OpenAI are expanding their partnership; from August 2026, ChatGPT Edu and Codex will be available to all students, faculty, and staff. The report says only "enterprise-level security and controls" and does not state training or retention terms (https://www.edtechinnovationhub.com/news/the-national-university-of-singapore-brings-chatgpt-edu-and-codex-to-all-students-faculty-and-staff , accessed at the time of writing).
- **[Inference] Implications**:
  1. Unpublished results in group meetings most likely count as "confidential research data". Pasting them into ChatGPT (Alternative 2) or first sending them through the Granola/Fellow cloud (Alternative 3) must clear all four conditions. **The "not retained" condition depends on the vendor's retention terms, which an ordinary personal account can hardly satisfy.**
  2. **The RCA clause** makes the constraint harder for industry-academia joint labs: whether GenAI is used must be written into the collaboration agreement (this is the basis for the second pin in the §5.3 bowling-alley strategy).
  3. **Counter-evidence**: NUS has already procured campus-wide ChatGPT Edu. Singapore universities are moving toward "buy one approved enterprise cloud tool". If the target university makes a similar purchase that covers research data, "stays on campus" drops from a threshold to a preference, and the counter-positioning weakens considerably (§11 D2).

---
## 5. Target Customer and Beachhead (Dunford element 4 + Moore's three beachhead criteria)

### 5.1 Beachhead definition (using observable traits, not demographics)

**Computational research groups at the target university (ML / robotics / VLA), 5–15 people, with a weekly group meeting, running experiments on W&B or TensorBoard + Git, whose group meetings mix Chinese and English and whose content is unpublished research data.** The seed is the project owner's own group.

Identification signals (can be asked in the interview screening questionnaire):
1. A regular weekly group meeting or 1-on-1;
2. Reviews like "did that experiment from last week finish running?" come up in the meeting;
3. Experiments have a run link or commit that can be pointed to;
4. Someone in the group has said "this can't be pasted into ChatGPT" or has used a workaround (redaction, pasting only summaries).

### 5.2 Self-assessment against Moore's three criteria

| Criterion | Assessment | Label |
|---|---|---|
| **Big enough to matter** | The target university has many computational research groups; so do other Singapore universities and comparable groups at A\*STAR; **enough for a portfolio and interviews, not enough for a business** | [Inference]; exact numbers to be verified |
| **Small enough to lead** | Within the scope of this document's search, no product specifically occupies "reconciling experiment commitments without data leaving campus"; the closest, Littlebird, is a personal cloud assistant | [Fact · within search scope] + [Inference] |
| **Fit with crown jewels** | The project owner is in a computational VLA lab at the target university, so can dogfood; understands W&B/Git/VLA terminology; has access to labs at their own university; the eval-kit's 5 synthetic meetings are exactly VLA group meetings | [Fact] (project owner's background, see task background) |

### 5.3 Bowling pins (directions only; entry conditions written down in advance)

| Pin | Segment | Why adjacent | Added whole product | Entry condition |
|---|---|---|---|---|
| 1 | The project owner's own computational research group (dogfood) | — | Single-user ledger + reconciliation | — |
| 2 | University–industry joint robotics labs (Hyundai-[target university]-A\*STAR, AUMOVIO-[target university], Schaeffler-[target university], etc. [Fact, U5 §1.2]) | Same experiment commitments; **the RCA constraint makes "data stays on campus" a harder requirement**; there is a paying party (company + NRF co-funding [Fact, U5 §2.4]) | "Decisions and change orders" for funder progress meetings, borrowing DESCA's "draft → objection window → default acceptance" pattern [Fact, U5 N19] | At least 1 of the 3 university–industry labs confirms "meets regularly with the company side and keeps written progress or change records" (U5 §5.1 cut-off line) |
| 3 | Computational groups at other Singapore/overseas universities | Same shape of data policy | Deployment guides adapted to each university's policy | Pin 1 week-4 retention ≥50% (n≥6) (00/06 §9.1) |
| 4 | Enterprise ML teams | Same W&B/Git toolchain | Enterprise private deployment | **Decided by the H10 result**: if on the enterprise side "Granola MCP + W&B MCP is enough", do not enter |

---

## 6. Defensibility Analysis (the core of this perspective)

### 6.1 Item-by-item diagnosis of the 7 Powers

| Power | Does this plan have it | Strength (today / in 12 months, [Inference]) | Where the barrier comes from | How it could fail |
|---|---|---|---|---|
| **Counter-positioning** | **Nascent** | Medium / Medium | Competitors' revenue and improvement loops are built on hosted data; building "the vendor can't see the data" for a small research niche has negative ROI and would also undermine their main narrative of "fully automatic, cross-app memory" | The university procures and approves an enterprise cloud tool (already happened at NUS); a competitor ships a zero-retention enterprise edition that the university accepts; local model quality is too poor and users voluntarily give up the constraint |
| **Process power** (encoding vertical workflows) | Nascent | Weak / Medium | The reconciliation rules, `UNKNOWN` discipline, strength-judgment order, and 27 edge cases (eval-kit annotation-guide) have to be calibrated round by round in real group meetings; the process is opaque and accumulates slowly | Written-down rules can be read; without real user corrections flowing back, it is just a document |
| **Cornered resource** (proprietary evaluation assets) | Nascent | Weak / Medium | Gold labels for mixed Chinese-English research group meetings × field-level × UNKNOWN; archived real competitor outputs; user-correction triples (05 G21). The identity of a **neutral third party** is itself something competitors cannot obtain | The gold labels are currently AI-drafted and not double-annotated (eval-kit README §5.6); public datasets such as ICSI are usable by anyone; small sample |
| **Switching costs** | None → Present | None / Weak–Medium | A group's months-long chain of "commitment — run — conclusion — decision"; switching tools loses it | Only exists with sustained use; zero in the Now phase |
| **Network economies** | None | None / Weak | The atomic network is one research group, and the hard side is the PI (00/06 §1) | Multi-user is not built in the Now phase |
| Scale economies | None | None | — | — |
| Branding | None | None | — | — |

**[Inference] In one sentence**: What can be claimed today is only "the counter-positioning position + two nascent powers". In interviews, say proactively: "The Powers don't exist yet; these are nascent ones I designed deliberately, along with their failure conditions." This is more credible than claiming a moat (00/03 §10.2 step 5).

### 6.2 "Why they won't copy this within three months" — answered competitor by competitor

> Every cell is [Inference], with the basis given in parentheses. "Warning signals" are what to check monthly.

| Competitor | What it would need to change to match this plan | Why it most likely won't within three months | Most likely first block to be copied | Warning signals (trigger re-evaluation) |
|---|---|---|---|---|
| **Feishu / Lark** | Add experiment-artifact data sources + research-conclusion fields + private deployment | Its target is "enterprises that keep IM, docs, and calendar all on Feishu" (M1 §2.1); Singapore research groups are not its main battlefield; private deployment goes through large-account sales and won't be opened up for a small research group | R&D meeting templates, stronger weekly summaries | Lark pushes an education offering at Singapore universities; Meeting Express adds "link external data sources" |
| **Otter** | Support Chinese first | Officially supports only English, Spanish, and French [Fact]; its direction is a sales agent (M2 §0 item 3) | Almost irrelevant | Chinese support launches |
| **Fellow** | Add result/evidence fields + W&B connection + self-hosting | Its context is "manager and direct reports" (07 §1 summary); per-seat cloud subscription with no education pricing [Fact, 07 F18–F19]; GitHub sync goes through Zapier and the help center has no dedicated GitHub article [Fact, 07 F13], indicating engineering integrations are not a build priority | **Result field + custom statuses** (doable in one iteration) | Outcome/evidence fields appear on the action-item page; a self-hosted or data-residency offering appears |
| **Littlebird** | Add W&B/GitHub data sources + shared team commitments + data stays on campus | Its product claim is "remembers what you see in any app" [Fact]; cross-app cloud memory is its core asset, and "data stays on campus" would dismantle it; the FAQ lists only Gmail, Google Calendar, Google Drive, Outlook, and Dropbox as integrations [Fact]; but it **understands grad students best** and is the most likely to add the first two | **Evidence-source expansion** (screen memory may already "see" the W&B pages the user opens; this is **to be tested in practice**); "share with advisor" | W&B/GitHub appear on the grad-student page; a Team plan adds shared commitments; a local mode or data-residency statement appears |
| Zoom / Teams Facilitator | — | Facilitator does not support external meetings, supports only a single language, and Planner tracking is still in preview [Fact, 07 T1, T6, T8] | Project-level agent | Facilitator supports multiple languages |
| **DIY (MCP assembly)** | Users write their own prompts | **No one needs to copy it**; it can be assembled today (U5 §3.2) | The entire feature layer | **Measure with eval-kit**: if DIY meets the H3/H4 metrics, this plan's feature layer does not hold (§11 D7) |

**[Inference] Overall judgment**: Within three months, the **feature layer** is most likely to have one block each filled in by Littlebird and Fellow; the **"data stays on campus"** layer has a low probability of being filled in by any of the four within three months, because it requires changing the deployment form and business model rather than adding a feature. So this plan's narrative must center on "data stays on campus + quantifiable trust", and **must not** center on "we can connect to W&B".
### 6.3 Why the evaluation asset is "proof + compounding," not just proof

- **Proof**: It turns "they don't do it well" into a number; without numbers, every differentiator is just "not mentioned on their website" (06 §0, item 4).
- **Compounding** ([Inference], based on 00/04 domain G, F4): Every time a user edits an entry in the reconciliation interface (rejecting a match, changing a conclusion, filling in an UNKNOWN), it is recorded as an "(original output, user correction, source sentence)" triple and added to the regression set. If the score on a fixed held-out set rises as corrections accumulate, that is compounding; if it doesn't rise, it is just accumulation.
- **Why competitors won't do this publicly**: Publicly benchmarking competitors amounts to advertising for them; publicly measuring your own UNKNOWN rate amounts to admitting "it sometimes doesn't know," which conflicts with a "fully automatic" narrative [Inference].
- **Wording boundaries** (08 §5.1): We cannot say "the first public action-item benchmark" (AMC-A, ICSI, and MUG already exist), and we cannot say "the first research group meeting dataset" (ICSI is itself a research group's weekly meeting). We can only say: "field-level, allows UNKNOWN, mixed Chinese-English, includes real competitor outputs — not found within the scope of my search."

---

## 7. Market Category and ERRC

### 7.1 Market category (Dunford's 5th element)

- **Do not call it** an "AI meeting assistant" — in that category our rivals are Feishu and Otter, and they compete on transcription and automation, where we would certainly lose.
- **Call it a "group meeting experiment ledger" (lab-resident experiment ledger)**: place it next to W&B Reports and "group meeting slides + verbal recap," not next to Otter.
- **Why this category choice is also defensive** [Inference]: Once the category changes, meeting products will see us as a "small research tool" rather than a competitor, which puts us in the "denial" stage Helmer describes (00/03 §4.1); experiment-tracking products (W&B), in turn, will not treat "meeting context" as their own concern (U3 §4.2).
- **Related trend (optional 6th element)**: Universities' rules on GenAI handling of research data are tightening and becoming more detailed (the target university's policy, reviewed 2025-11-07 [Fact]); at the same time, universities are procuring and approving tools (a Singapore university [Fact, media]). Both forces exist at once and must be stated honestly.

### 7.2 ERRC grid (the Blue Ocean four actions)

| Action | Element | Rationale | Evidence |
|---|---|---|---|
| **Eliminate** | Meeting-joining bots, audio recording storage, cloud hosting of raw meeting notes, speaking-time/sentiment analysis, auto-created tasks, auto-sending externally | Bots are banned by universities (Waterloo, etc. [Fact, U2 §1.2]); recording-consent lawsuits (Otter, Granola 3:26-cv-07926-EMC [Fact]); cloud hosting conflicts with the target university's policy | 05 G7, U2, 00/06 §4 |
| **Reduce** | Full-length summaries, in-house ASR (Now: text input only, local ASR can be connected later), number of integrations (only W&B/Git read-only), multi-user accounts (Now: single user) | Nobody reads summaries (HN smartmic [Fact]); integrations are not a moat (06 V1–V2); cold start (00/06 §1) | 05 G14, G20; 00/06 §8.3 |
| **Raise** | Field-level UNKNOWN discipline, sentence-by-sentence source verification, recall of mixed Chinese-English research terminology, recall of the PI's own commitments, data residency | Competitors fill in by default or require manual completion; mixed Chinese-English datasets have no action-item annotation [Fact, 08 §3.5] | 05 G2, G3, G8; 08 §5.2 |
| **Create** | Commitment ↔ experiment artifact reconciliation; research conclusion labels (five values, [Assumption · to be validated]); a provider form that never leaves campus; public field-level evaluation + real competitor outputs | Meeting tools have no research objects, and research tools have no meeting objects (05 K13) | 05 K13; 07 §8; 08 §5.2 |

**Value curve check** [Inference]: On industry factors such as "transcription, automation, integrations, real-time," we are **deliberately below** competitors; on "no guessing, evidence from experiment artifacts, data stays on campus, publicly measurable," we are **far above** them. The shape is different; it is not simply higher overall.

---

## 8. Positioning Statement (Moore Template)

```
For        compute-heavy research groups doing ML/robotics research at universities such as the target university (5–15 people, weekly group meetings, experiments run on W&B/Git)
Who        are dissatisfied with opening group meetings by relying on memory to recall "did that experiment from last week finish running," while existing meeting AI either doesn't understand experiments
           or requires handing unpublished group meeting content to an external cloud
Our product is a group meeting experiment ledger that never leaves campus
That       provides the original sentence of each experiment commitment from last week, the corresponding run/commit, the conclusion, and an explicit "no evidence yet" marker,
           running entirely on the lab's or the university's own compute
Unlike     cloud-based meeting assistants such as Fellow, Littlebird, and Feishu Minutes (which track "done or not," with evidence coming from email and task status),
           and "paste the notes into ChatGPT" (which has no ledger and cannot get around the university's GenAI data rules)
We have assembled commitment↔experiment-artifact reconciliation, an extraction discipline that writes UNKNOWN when information is missing, a model interface switchable to local/university clusters,
           and a public field-level evaluation of mixed Chinese-English research group meetings
```

**Dunford one-sentence version**: For compute-heavy research groups whose group meeting content cannot be casually handed to external AI, and who have to answer "did that experiment from last week finish running" every week, BriefPilot is an experiment ledger that stays inside the lab: it matches last week's verbal commitments to this week's runs and commits, writes "unknown" when it doesn't know, and publicly discloses which kinds of entries it gets wrong.

---

## 9. "Others already do it, so why are you building it?" — the 30-second answer

> About 150 Chinese characters, compressed in five steps per 00/03 §10.2: acknowledge → that one step → why this group cares → why big companies won't do it first → honest boundaries.

"Right, Feishu, Otter, and Fellow can all turn meetings into action items, and Fellow launched assignee accept-or-decline last month. I don't do any of that. I only do the one step at the start of a compute-heavy lab's group meeting: 'Did that baseline from last week run?' — matching last week's verbal commitments to this week's W&B runs and commits. There's a hard constraint here: under the target university's GenAI research policy, unpublished group meeting content can't be casually uploaded to external AI. They are all cloud products that make money by hosting data, so building 'data never leaves campus' for a small research niche runs against their own business model, and that is my position. I use a public mixed Chinese-English group meeting evaluation to show where they go wrong, and I will report the numbers honestly, **including where they do well**."

**Follow-up prep** (one sentence each):
- "Littlebird already handles graduate-student commitments?" — "Yes, and it's the competitor I worry about most. Its evidence comes from email and documents, the integrations listed in its FAQ are Gmail, Google Drive, and the like, and its core is remembering everything on your screen in the cloud, which is the opposite of 'never leaves campus.'"
- "Can't I just stitch together Claude with Granola and the W&B MCP myself?" — "You can build most of it that way, so I include it in the evaluation as a baseline group; if it meets the bar on 'don't guess when missing,' I'll give up building my own and switch to evaluation and workflow solutions." (00/06 §8.3 exit condition)
- "What if the target university buys Copilot?" — "Then 'never leaves campus' goes from a threshold to a preference, and my position weakens. So in week one I'll check whether the target university has approved any enterprise tool that covers research data."
- "Aren't you refereeing your own evaluation?" — "The annotation guidelines, gold labels, and the ICSI (CC BY 4.0) subset are all public, two annotators label and I report κ, and anyone can reproduce it (08 §5.6)."

---
## 10. The Demo's Magic Moment

### 10.1 The Magic Moment (One Screen)

> **Screen**: A simulated M3 group-meeting opening (eval-kit synthetic meeting, 2026-10-15). The left side of the screen shows "Last week's (M2) commitment reconciliation." The top right shows a **network egress counter: 0 bytes**, with the provider displayed as "Local Ollama."
>
> The PI asks: "Did that baseline run last week?"
>
> Within 3 seconds, row M2-05 on the reconciliation sheet expands:
> - **Original sentence** (M2 timestamp) + owner Wang Bo;
> - **Matched artifacts**: one SimplerEnv run record (a locally mocked W&B export) + one commit;
> - **Conclusion**: partially done. The Google robot set finished (visual matching about 0.48, quoting the original sentence from M3-01); the WidowX set did not run (M3-02, reason: numpy dependency conflict);
> - Two other rows on the same screen: the PI's own commitment from last week is marked "**no evidence found**"; Daniel's "I might… no promises though" is shown as **tentative, not added to action items** (gold M3-03).
>
> **Then switch to the comparison**: feed the same M2+M3 plain text to "ChatGPT/Claude + paste" and to Fellow (eval-kit conditions B-Text / A-TTS), and show their outputs side by side. **The specific gaps in the comparison column may only be filled in with measured eval-kit results; before running it, write no numbers and do not presume they will be wrong.**

**Why this screen** [Inference]: It packs three legs into 10 seconds: experiment-artifact reconciliation (function), 0 bytes of egress (counter-positioning), and a measurable difference against competitors shown side by side (evaluation asset). Paul Graham and 00/05 both require a demo to show just one magic moment (00/05 §0, item 5).

### 10.2 Scope for 2–4 Weeks (Now)

| Do | Don't do |
|---|---|
| Text input (post-meeting notes / pasted transcripts); commitment extraction schema (type/owner/due/strength/evidence, UNKNOWN allowed); original-sentence verification (reusing the S0 citation allowlist); read-only matching against W&B export JSON + local git log; switchable local provider (Ollama) and API provider; reconciliation view; eval-kit scoring, shown inside the demo | Audio recording, ASR, meeting-joining bots; multi-user accounts, advisor confirmation, claiming UI; write-back to GitHub/W&B; weekly report generation; knowledge Q&A (G12 only after H11 holds) |

**Data discipline**: Use only eval-kit synthetic meetings (the people, the lab, and Kestrel Robotics are all fictional [Fact, eval-kit README §5.1]); do not use real group meetings until written permission from the advisor and an IRB determination are obtained (00/06 §4.5, 02/06 §6).

---

## 11. Make-or-Break Hypotheses and How to Validate Them

> The decision thresholds are [Assumption, to be validated] set in this document and fixed in advance to prevent moving the goalposts. Where eval-kit H1–H8 and 02/06 H01–H14 can be reused, they are reused directly.

| # | Make-or-break hypothesis | What happens if wrong | Validation method | Success line | Abandon line | Timing |
|---|---|---|---|---|---|---|
| **D1** | Group-meeting commitments really do get lost, and the "review last week" step has a cost | The need does not exist; the whole plan is downgraded to a portfolio demo | 02/06 H01, H02, H03 (diary + interviews) | Per the original 02/06 thresholds | Neither H01 nor H02 holds | Weeks 1–3 |
| **D2** | **"Data stays on campus" is a hard requirement, not a preference**: the target university has not approved any enterprise cloud AI covering group-meeting research data, or members have actually refused to upload | The counter-positioning main leg fails and the plan degrades to pure functionality (easy to copy) | ① In week 1, email the target university's IT / research integrity office (merge with the IRB email); ② 02/06 H08; ③ Check whether the university intranet lists a procurement similar to NUS ChatGPT Edu | No approved tool covers research data, **or** ≥3 interviewees describe a specific "was refused / did not dare to paste" incident | The target university has approved an enterprise cloud tool covering research data, **and** most interviewees already use cloud tools for group meetings | Conclusion in week 1 |
| **D3** | Competitors have reproducible failures on "no guessing / soft commitments / PI commitments / terminology" | There is no provable difference at the functional layer | eval-kit H1, H2, H3, H4, H6 (B-Text + A-TTS) | At least 2 hypotheses hold, with a gap of ≥15 percentage points (see the sample-size caveat in 08 §5.5) | H1–H4 all fail | Week 2 |
| **D4** | **Local model quality is sufficient**: an 8–14B model on the local machine is not noticeably worse than a cloud API on field-level metrics under the B-Text condition | Users will give up the constraint for quality, and "data stays on campus" becomes a burden | Run the same eval-kit on Ollama (e.g., qwen3 8B/14B) vs. a cloud API (synthetic data may go to the cloud) | Gap versus cloud on key fields (owner accuracy, UNKNOWN rate, item F1) ≤10 percentage points | Gap >20 percentage points | Week 2 |
| **D5** | Commitments can be matched to experiment artifacts automatically, or students are willing to add links | The reconciliation layer relies on manual effort and the value collapses | ① Automatic-matching precision on synthetic runs/commits; ② 02/06 H04 backfill test | Matching precision ≥80% (after human confirmation); or H04 backfill rate ≥50% | Precision <60% **and** backfill rate <30% | Weeks 2–3 |
| **D6** | During the window, Littlebird/Fellow do not add both "experiment-artifact evidence + data stays on campus" | The position is taken | On the 1st of each month, open Littlebird's graduate-student page, its promise tracker, Fellow's action-item page and changelogs, and record changes | Neither shows a W&B/GitHub evidence source + a local/residency option | Either one shows both at once | Ongoing |
| **D7** | DIY (Fellow/Granola MCP + W&B MCP + Claude) cannot reach the same metrics as D3 | Users can assemble it themselves, so building is pointless | Run DIY as one eval-kit condition | DIY is clearly worse than this plan on UNKNOWN rate or soft-commitment promotion rate (≥15 points) | DIY differs from this plan by <10 points | Week 3 |
| D8 (secondary) | The five-value research conclusion is useful | Only affects the granularity of the "conclusion label" | Interviews + dogfood backfill: see which values students actually use | ≥3 values actually used | Only "done / not done" is used | Weeks 3–4 |

**Decision rule** [Inference]: If either D2 or D4 fails → drop the "data stays on campus" main narrative, return to Plan A's "verifiable commitment layer + public evaluation," and say honestly in interviews, "I tested this counter-positioning and it did not hold." If both D3 and D7 fail → stop building and switch to "evaluation + workflow recipes" (the honest exit condition in 00/06 §8.3).

---
## 12. Rejected Alternatives and Rationale

| Alternative | Reason for rejection (defensibility perspective) | What was kept |
|---|---|---|
| **Option A: a verifiable, owner-claimed commitment layer** | Easiest to copy: G4 is already covered by Fellow (2026-10-01), and G2 is covered by Feishu; no niche segment to fall back on (00/03 §8.5, "feature differentiation alone is the most fragile") | UNKNOWN discipline; original-sentence verification as the passing bar |
| **Option B: PhD student 1-on-1 ledger + advisor confirmation** | Littlebird's graduate-student page already covers the personal version; UK university systems already occupy the "confirmation" step (07 §7 summary); Singapore lacks an institutional lever (07 U7); advisor confirmation has a cold-start problem | The PI's own commitments as an evaluation slice |
| **Option C original (selling the "five-value result")** | The five values are an [Assumption] (06 W10); Littlebird already does half of "evidence comparison", and "connecting W&B" is just one connector that Littlebird could add in a single iteration | **Keep "experiment artifact evidence"**, but shift the defensive center of gravity from features to "data stays on campus + evaluation" |
| **Option D: accurate Chinese-English terminology assistant** | No first-hand Chinese pain point (06 W4); the ASR layer is catching up quickly; Feishu can already recognize by original language | Term recall as an evaluation dimension |
| **Option E: vendor requirement-change ledger** | Weakest evidence, and cannot be dogfooded (05 §4.7) | Outward-facing generalization narrative; the "objection window" pattern goes into the second bowling pin |
| **Option F: open-source community issue write-back** | No paying party, no felt pain | The public evaluation uses ICSI (CC BY 4.0, research-group weekly meetings) as the reproducible English baseline (08 §5.3) |
| **University-industry joint lab as the beachhead directly** (U5 Top 1, later stage) | Zero public evidence of confirmation from the company side; reachability of the company co-lead scored about 2; compliance score 2; real data cannot be obtained (U5 §2.6) | Serves as the second bowling pin; the RCA clause is a harder version of "data stays on campus" |
| **"Local-first meeting notes" as a standalone position** | Meetily and anarlog already own the mindshare (U4 §0, item 4); local-only is merely a threshold | Local only matters when combined with "experiment-commitment reconciliation" |
| **"First public action-item evaluation" narrative** | Directly refuted by AMC-A, ICSI, and MUG (08 §0) | Replaced with an incremental claim: "field-level + UNKNOWN + Chinese-English code-switching + real competitor outputs" |

---

## 13. Point-by-Point Response to Round 2 New Evidence

| Round 2 new evidence | Source | Impact on this plan | This plan's response |
|---|---|---|---|
| Fellow AI suggestions: "any assignee can accept or dismiss it", with auto-accept off by default | 07 F8 | Owner claiming is no longer a differentiator; it also shows that some vendors are willing to ship "conservative defaults", weakening the "anti-automation" counter-positioning | Drop owner claiming; the counter-positioning does not bet on "being conservative" but on "data residency" |
| Fellow dismissal = permanent deletion, no reason recorded | 07 F9 | A very narrow gap | Not pursued (in the single-user stage there is no one to dismiss) |
| Littlebird graduate-student page, student price $15, three-state commitment check, can track "what others owe you" | 07 L1–L9; graduate-student page reopened this round | Top risk; G6 personal version is already covered | Do not compete on "commitment tracking"; differentiate only on "evidence from experiment artifacts + data stays on campus"; D6 monthly monitoring |
| Littlebird graduate-student page FAQ lists only Gmail, Google Calendar, Google Drive, Outlook, Dropbox as integrations; "remembers what you see in any app" | [Fact] this round | The evidence sources are still general office data; but screen memory **may** already indirectly cover W&B pages | Listed as an item to test (Littlebird student plan is free for 2 months); differentiation cannot rest solely on "it doesn't connect to W&B" |
| UK supervision systems verified (Loughborough, Surrey) | 07 §7 | The confirmation step is already occupied by university systems | No confirmation gate |
| No per-session supervision record system found in Singapore | 07 U7 | Option B lacks a lever | Option B not chosen; this plan's constraint lever is replaced with the target university's GenAI / research-data policy |
| Academic benchmarks: ICSI, AMI, AMC-A, MUG, AIR; "first" cannot be claimed | 08 §0 | The evaluation narrative must change | Use the "can say" wording from 08 §5.1; ICSI as the reproducible English baseline |
| The cross-cell of "Chinese-English code-switching meetings + action-item field annotation" is empty | 08 §3.5 | The incremental claim for the evaluation asset holds (within the search scope) | Treat as a seed of a "monopoly resource"; re-search arXiv one week before the interview (08 §6) |
| eval-kit is ready and selftest passes, but has not been run; gold labels are AI-drafted | eval-kit README | The demo has data, but the numbers are blank | Use M2→M3 directly for the magic moment; the comparison column is filled with measured values only; first have two annotators label M1 and M3 |
| Tongyi Tingwu API returns at most 6 action items | eval-kit README §2.2 | Recall comparison must report the "product design ceiling" | Comply |
| University-industry joint lab: structure exists, no confirming evidence, has a paying party; DESCA objection window | U5 §0, §5.1 | An extension with a paying party | Treat as the second bowling pin; the RCA clause connects directly to item 4 of the target university's GenAI policy |
| Enterprise ML teams can DIY with W&B MCP + Granola MCP | U5 §3.2 | The feature layer can be DIY'd | D7 hands-on test; enterprise ML enters only after the H10 result |
| IRB, research-data ownership, and GenAI policy of the target university | 00/06 §4.4–4.5 | Supports "data stays on campus" | Reopened the original GenAI policy page this round, filling in the RCA conditions and "no approved tool named" |
| A Singapore university opened ChatGPT Edu campus-wide | [Fact, media] this round | **Counter-evidence**: universities may solve compliance by "procuring approved cloud tools" | D2 listed as a make-or-break assumption that must be settled in week one |
| Granola class-action lawsuit 3:26-cv-07926-EMC | 06 V14 | Recording-consent risk | Recording removed in ERRC |
| Gemini does not support Chinese or multiple languages in the same session; Notion speaker labeling supports English only; Krisp does not support Chinese | 06 V8, V9, V12 | International platforms are absent from the Chinese-English code-switching scenario | Do not test these three; use as "competitors absent" background |
| "Feature gaps get closed about once a quarter" | 07 §8.1 | A pure feature-based plan has a lifespan of about one quarter | This plan explicitly does not rely on feature-based defense |

---
## 14. Self-critique: where this plan is most likely wrong

1. **Mistaking a "rule" for a "pain"**: The existence of the target university's policy doesn't mean group members care about it. Many researchers keep using ChatGPT anyway (U3 H-E failure signal). D2 exists to test exactly this.
2. **A local model drags down the experience**: If the on-device model is clearly worse at mixed Chinese-English speech, users will choose quality over compliance (D4).
3. **Small market**: Even with two more beachhead segments, that is only a few dozen to a few hundred groups. This is first of all a **portfolio and interview story**. The commercial story can only be generalized through university-industry labs and "industry-funded research" (U5 §2.4), and it is untested.
4. **Author self-projection**: The project owner is the target user (U1 §14 warns about this). The comparison group (corporate ML teams of 3–4 people) and samples from outside the owner's own group cannot be skipped (02/06 §2).
5. **Credibility of the evaluation assets**: The gold labels were drafted by AI. Until two-person annotation is done and κ reaches the threshold, no "we are better" claim may be made externally (eval-kit README §5.6).

---

## Source list (all accessed at the time of writing)

**Newly opened or newly searched this round**
1. Littlebird graduate students page (reopened) — https://littlebird.ai/for/graduate-students [Fact]
2. The target university's position on the use of generative AI in research (reopened; published 2023-07-04, reviewed 2025-11-07) — (university page; link removed) [Fact]
3. EdTech Innovation Hub: NUS brings ChatGPT Edu and Codex to all students, faculty and staff — https://www.edtechinnovationhub.com/news/the-national-university-of-singapore-brings-chatgpt-edu-and-codex-to-all-students-faculty-and-staff [Fact; media report, not an official NUS page]
4. WebSearch: "meeting notes action items linked to Weights & Biases runs" — no ready-made integration found; results were generic guides and Notion templates, e.g. https://www.notion.com/blog/connect-meeting-notes-to-projects , https://www.resolution.de/post/meeting-notes-and-action-items/ [Fact · not found within the search scope]
5. WebSearch: "approved generative AI tools" for the target university — no list of approved tools found; NUS teaching AI policy https://ctlt.nus.edu.sg/wp-content/uploads/2026/04/Policy-for-Use-of-AI-in-Teaching-and-Learning.pdf [Summary, not opened]

**Official sources already verified in Round 1/Round 2 (cited onward; accessed at the time of writing)**
6. Fellow AI-Suggested Action Items — https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items
7. Fellow Action Item Page — https://help.fellow.ai/en/articles/4144380-action-item-page
8. Fellow Carry incomplete items forward — https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward
9. Fellow Meeting Briefs — https://help.fellow.ai/en/articles/9773836-meeting-briefs
10. Fellow MCP server — https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server
11. Fellow × GitHub — https://fellow.ai/integrations/github
12. Fellow Pricing — https://fellow.ai/pricing
13. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
14. Littlebird Pricing — https://littlebird.ai/pricing
15. Littlebird Teams — https://littlebird.ai/teams
16. Feishu smart meeting minutes — https://www.feishu.cn/content/article/7577317993749269689
17. Feishu AI action-item breakdown — https://www.feishu.cn/content/article/7600354912756681687
18. Microsoft Learn: Facilitator in Teams — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
19. Google Meet "Take notes for me" — https://support.google.com/meet/answer/14754931
20. Zoom AI Companion / ZoomMate — https://www.zoom.com/en/products/ai-assistant/
21. Otter MP3-to-text page (supported languages) — https://otter.ai/mp3-to-text
22. Granola Security — https://www.granola.ai/security
23. Granola class-action coverage — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
24. Official W&B MCP server — https://github.com/wandb/wandb-mcp-server
25. Rashid Lab meeting leader guide — https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html
26. MIT advising philosophy policy (Aeronautics and Astronautics) — https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf
27. CHI 2020 paper — https://ar5iv.arxiv.org/html/1910.13602
28. Loughborough Co-Tutor — https://lboro.ac.uk/students/handbook/starting/attendance/co-tutor-supervisory/
29. The target university's list of corporate labs — (university page; link removed)
30. DESCA Horizon Europe v2.1 — https://www.desca-agreement.eu/assets/helmholtz_gemeinschaft/user_upload/Brussels_Office/DESCA/2026/20260228_DESCA_HorizonEurope_.2.1_with_elucidations_final.pdf
31. AMC-A paper, 2023 — https://arxiv.org/abs/2303.16763
32. ICSI Corpus (Edinburgh, CC BY 4.0) — https://groups.inf.ed.ac.uk/ami/icsi/
33. a16z, Avoiding Death on the Yellow Brick Road — https://a16z.com/avoiding-death-on-the-yellow-brick-road/
34. 7 Powers book summary (secondary source; to be checked against the original book) — https://blas.com/7-powers/

**Files in this project (evidence chain)**: `00_pm-skills/03`, `00_pm-skills/04`, `00_pm-skills/06`; `01_market-research/05`, `06`, `07`, `08`; `02_user-research/01`, `03`, `04`, `05`, `06`; `05_demo-plan/eval-kit/README.md` and `gold/`.

---
## Confidence Notes for This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| Claiming, cross-meeting binary tracking, weekly reports, and provenance are no longer differentiators | **High** | Official help docs verified page by page in 07 |
| All four competitors process in the cloud; no W&B evidence source seen | **Medium-high** | "Not seen" on official pages ≠ "does not exist"; Littlebird's screen memory may cover it indirectly, to be tested |
| The four conditions and the RCA clause of the target university's GenAI research policy | **High** | Original page re-opened in this round |
| "Data never leaves campus" is a threshold for labs, not a preference | **Low (assumption)** | Zero interviews; a Singapore university already has a counterexample path (D2) |
| Competitors "don't want" to offer data residency (reverse positioning) | **Medium-low (inference)** | Based on business-model reasoning; the Helmer framework comes from secondhand book excerpts; no insider information on competitors |
| Incremental value of the evaluation assets (field-level + UNKNOWN + mixed Chinese-English + competitor outputs) | **Medium** | Not found within the search scope of 08; not exhaustive |
| Competitors would err in this scenario | **Unknown** | eval-kit has not been run; **no numbers may be cited externally** |
| Local model quality is sufficient | **Unknown** | No public evaluation (05 Q11); D4 still to be tested |
| Beachhead size and business story | **Low** | Only the portfolio value is certain; the paid path depends on validation with university-industry labs |

**Most important reminder**: The defensibility argument of this plan rests on **competitors' incentives**, not on competitors' capabilities; and its first premise ("data never leaves campus" is a threshold) has **no user evidence today**. If D2 in week 1 or D3 and D4 in week 2 fail, downgrade immediately according to the decision rules in §11 rather than looking for new justifications.
