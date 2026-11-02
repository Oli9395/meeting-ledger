---
title: "03_positioning Candidate 1 (dogfood-feasibility perspective): pre-group-meeting \"experiment commitments × run reconciliation sheet\""
status: draft-v1 (one of several candidates, pending comparison review against candidates from other perspectives; zero user interviews, zero hands-on competitor testing)
sources_count: 31
perspective: "dogfood-feasibility (feasibility and self-use first: the project owner is a member of a computational lab at the target university, building a demo solo in 2–4 weeks)"
---

# Candidate 1 (dogfood-feasibility): pre-group-meeting "experiment commitments × run reconciliation sheet"

> **Reading notes**
> - Labels follow the project-wide convention: **[Fact]** has a source URL and the original page was opened; **[Summary]** only a search snippet or secondhand account was seen; **[Inference]** derived from facts; **[Assumption·to be verified]** needs interviews, diaries, or hands-on testing to confirm. "Not seen" means "the page doesn't say so", not "the product doesn't have it".
> - **Input scope**: fully read `00_pm-skills/03`, `01_market-research/05` (§0–§4, §6, §7), `06`, `07`, `05_demo-plan/eval-kit/README.md`, and `gold/decisions_hypotheses.md`; read §0 and §5–§6 of `08`, §0, §3, §5, §6, §13–§15 of `02_user-research/01`, §0 and §3–§5 of `03`, §0 and §5–§6 of `05`, §1 of `06`, §0, §4.4–§4.7, §8.3, and §9.1 of `00_pm-skills/06`, plus the §0 conclusions of the remaining files (M1–M4, U2, U4). **I did not read all 1.1 MB of body text line by line**; every citation names its source section so it can be checked.
> - **Newly verified this round (WebFetch/WebSearch)**: only 3 items, all related to this proposal's "life-or-death competitors": ① the Littlebird graduate-student page (confirmed that the page does not mention GitHub, W&B, experiments, or code); ② the official W&B MCP server GitHub repository (confirmed it has `compare_runs_tool`, so the DIY route of "Claude + W&B MCP" already works technically); ③ the MCP page on the W&B docs site (after two 301 redirects it lands on CoreWeave docs that require an access code and could not be opened, **to be verified**). All other competitor facts carry over from the conclusions already verified in Round 2 (07, 06) and were not reopened.
> - **This document's perspective is biased**: it prioritizes "the project owner can use it themselves starting tomorrow, can obtain real material, and the demo can actually run end to end", so it systematically underweights dimensions like "business story" and "market size". Please factor this in when comparing against candidates from other perspectives.

---

## 0. Conclusion first

1. **Recommended proposal**: take Option C (the commitment–result–evidence chain for computational research groups) and **cut it in half again**, keeping only one step: **on the night before a group meeting (or a 1-on-1 with the advisor), while the student prepares the "last week's plan / last week's progress" slide, match the experiments verbally promised at last week's meeting, condition by condition, against the runs that were actually executed in W&B / Git**. The output is a "reconciliation sheet": one row per commitment, with only four statuses: **Consistent / Condition mismatch / No evidence found / Not tracked (soft commitments, rejected options)**. Every row carries the quote source and the run link. **If no evidence is found, write "No evidence found"; never tick a box on the user's behalf.**
2. **The one sharp edge of unmet need**: **"Done, but not the thing that was promised."** For example, the meeting agreed on "add chunking up to 5 seeds, all with rank 32"; W&B does contain 5 runs, but the config of one of them is `lora_rank=16`. According to the Round 2 verification, none of the existing products' completion states has a "condition mismatch" state:
   - Fellow has only complete, archived ("won't do"), and AI-suggested states, with no result or evidence fields (07 F11, F12) [Fact];
   - Littlebird has only Kept / In progress / Needs a note, and its evidence sources are email, documents, calendar, and on-screen content (07 L2, L3) [Fact];
   - Feishu's "Meeting Digest" summarizes a week's action items, and Zoom can identify unclosed Jira issues (07 C5, Z6) [Fact / Summary].

   [Inference] For experiment-type commitments, these products can at most answer "was it done", but cannot answer "was the thing done the thing that was promised".
3. **Why choose it from the dogfood perspective** (details in §1, §2):
   - **It works for a single person**: no need for the advisor, assignees, or the whole group to join the system, so there is no cold-start problem (00/06 §1);
   - **The material is at hand**: W&B / Git run metadata already exists, and commitments come from the user's own meeting notes, with no recording needed, so it sidesteps three gates: recording consent, IRB recording clauses, and "uploading real transcripts to an external GenAI" (00/06 §4.4–§4.5);
   - **The demo can really run**: eval-kit already contains 4 consecutive weeks of synthetic group meetings and cross-meeting commitment chains (M1–M4); adding a matching synthetic run table is enough to demonstrate and score it end to end;
   - **It is still a gap left after Round 2**: 07 §8 concludes that G5 leaves only "research result values + experiment artifacts as evidence"; this proposal takes only the **observable half** (evidence and conditions) and drops the "five-value result" that has no evidence behind it yet (06 W10).
4. **The three biggest risks, which must be stated up front**:
   - **(1) "Claude + official W&B MCP + pasted meeting notes" can temporarily assemble most of the functionality** (this round's verification confirms the official W&B MCP has `compare_runs_tool`);
   - **(2) Littlebird is already in the graduate-student market**; connecting a W&B or GitHub data source could close this window within a single iteration;
   - **(3) Frequency may be insufficient**: among the 70 synthetic action items in eval-kit, a rough keyword count finds only about 13 related to experiments / runs (about 19%, [Inference], synthetic data does not represent real group meetings). If "experiment commitments with conditions" are rarer in real group meetings, this moment of magic will trigger infrequently.

   §8 sets a predefined abandonment threshold for each risk.
5. **The project owner's own dogfooding has a gap, which must be stated honestly**: the project owner is currently working on a VLA survey; the local `survey/papers/txt` holds the text of 110 papers, but this directory is not a git repository. Whether the owner is a heavy W&B user is not yet known ([Assumption·to be verified]). Therefore:
   - **Dogfooding the "W&B reconciliation" leg depends on labmates who run experiments**, on the condition that they give informed consent and the data is processed only locally;
   - The project owner can use the "literature / writing commitments × local files and git" adapter themselves, genuinely, every week.

---
## 1. Perspective: The Five Gates of Dogfood Feasibility

[Inference] The five gates below are screening criteria defined by this perspective, used to narrow "worth building" down to "the owner can actually build, actually use, and actually test within 2–4 weeks."

| Gate | Question | Why it matters for one person in 2–4 weeks | Basis |
|---|---|---|---|
| **G-1 Real users exist now** | Can the owner or a labmate start using it next Monday? | A solo project has no recruiting budget; self-use is the fastest feedback loop | 03 §10.4 "Why you: you are a lab member, so you can dogfood"; U1 §0-6 |
| **G-2 Real material is usable within compliance rules** | Can we get input without recording audio or uploading real transcripts to external models? | The target university's GenAI policy: "Any confidential or sensitive information, and/or personal data must not be uploaded to any external GenAI" (00/06 §4.5, [Fact]); interviews and observation that count as research must go through IRB beforehand (00/06 §4.4, [Fact]) | 00/06 §4.4, §4.5 |
| **G-3 Single-user value, no cold start** | Is it valuable when only one person uses it? | Chris Dixon: "come for the tool, stay for the network"; G4, G6 and G17 all require multiple people to be present (00/06 §0-1, §1) | 00/06 §1 |
| **G-4 Runs end to end and is testable** | Can we build "input → output → evaluation numbers" in 2–4 weeks? | The demo must be compressed into "one magic moment + a trust boundary" (05 §5); evaluation is the proof mechanism shared by all options (05 §0-5) | eval-kit README; 08 §5.5 |
| **G-5 Still a gap after Round 2** | After the checks in 07, has no one done this yet? | Gaps of the "feature present or absent" type get filled about once a quarter (07 §0-7, §8.1) | 07 §8 |

---

## 2. Derivation

### 2.1 Screening A–F and the U5 Ladder Through the Five Gates

Scoring: ● = passes, ◐ = partially passes, ○ = fails. The basis is written in each cell; all of it is [Inference].

| Option | G-1 Real users | G-2 Compliant material | G-3 Single-user value | G-4 Runs in 2–4 weeks | G-5 Still a gap | Verdict |
|---|---|---|---|---|---|---|
| **A** Verifiable, claimed commitment layer | ◐ Anyone can use it, but nobody *has to* | ● Synthetic data is enough | ○ Claiming (G4) inherently needs multiple people | ● | ○ G4 is already covered by Fellow (07 F8, 2026-10-01); G2 provenance is covered by Feishu (07 C7) | **No**; keep only G2 and G3 as the passing bar |
| **B** PhD student–advisor 1:1 ledger | ● The owner has an advisor | ◐ 1:1 content is sensitive, with a power relationship (U1 §6.3(c)) | ○ The advisor-confirmation gate needs the advisor in the system; the single-user version = Littlebird's grad-student page already does it (07 L9) | ● | ◐ Only "advisor-side confirmation + two-way" remains, and no institutional lever was found at the target university (07 U7) | **No** (as the main line); exporting supervision forms is left for Later |
| **C** Commitment–result–evidence chain for computational research groups | ● Our own group is the user | ● Run metadata already exists; commitments are entered as text | ◐ Back-filling results costs students extra effort (U6 H04 failure line <30%) | ◐ Building the five-value result and decision-recall Q&A in full is tight for 4 weeks | ◐ The evidence source and research semantics are still a gap, but there is no evidence for the five-value semantics (06 W10) | **Adopt, but trim** (§2.2) |
| **D** Mixed Chinese–English terminology assistant | ◐ | ○ Testing ASR needs real audio, which involves recording consent | ● | ◐ The ASR pipeline is heavy | ◐ Feishu already has enterprise-term recognition (07 C6); there is no first-hand Chinese pain point (06 W4) | **No**; terminology recall stays only in the evaluation |
| **E** Vendor-side requirement-change ledger | ○ The owner is not a vendor PM | ○ Cannot obtain material | ◐ | ◐ | ● | **No** |
| **F** Open-source meeting → issue | ○ The owner is not a maintainer | ● Public data | ● | ● | ◐ | **No**; used only as an evaluation data source |
| **U5 Ladder** Computational group → university–industry joint lab (quarterly review pack + objection window) | ◐ The wedge segment works; the extension segment needs external interviews | ○ Compliance score 2; enterprise data is unavailable (U5 §5.1) | ○ The objection window needs the enterprise side present | ○ Only fully synthetic within 4 weeks | ● | **The wedge segment is identical to this plan; the extension segment goes to Later (bowling pin 2)** |

**[Inference] Summary**: Only C has no "○" on the five gates. But the original C has two components that cannot pass the gates:
- "Five-value result back-fill": weak evidence, and the back-fill cost falls on students;
- "Decision-recall Q&A" (G12): already partly covered (07 §8), and its frequency has not been validated (U6 H11).

So they must be trimmed.

### 2.2 Trimming Option C into "Condition Reconciliation": Why Not the "Five-Value Result"

| Component of original Option C | Handling | Rationale |
|---|---|---|
| Commitment extraction + verbatim quote + no guessing on missing fields + no chasing soft commitments | **Keep, as the passing bar** | G2 and G3 are already partly covered (07 §8), so they cannot be the selling point; but without them the reconciliation sheet is not trustworthy |
| Five-value result (supported / refuted / inconclusive / abandoned / superseded) | **Demote to an optional field**, not required by default | 06 W10: derived only from the data model, and "reads like fact"; U3 H-A and U6 H04 both list "whether students are willing to back-fill" as a make-or-break line |
| Evidence links (run, commit, config) | **Change to "the system finds candidates, the user only clicks to confirm"** | Turns "student fills in" into "system finds, student clicks," cutting back-fill cost from "typing + finding links" to "one click" [Assumption · to be verified] |
| **Condition comparison** (in original Option C, mentioned in a single line: "done, but conditions differ from the commitment") | **Promote to the core selling point** | This is the only component that is ① objectively decidable (just look at the config), ② absent from existing products' status models, and ③ usable by one person the same evening [Inference] |
| Decision-recall Q&A (G12) | **Cut** | 07 §8: cited Q&A is now commonplace, and "refusal + evidence links" depends on G5's data; U6 H11's frequency is still untested |
| Group-wide dashboard, advisor confirmation | **Next / Later** | Gate G-3 |

**Why "condition reconciliation" suits the sharp edge better than the "five-value result"** [Inference]:
- **Observable**: The five-value result is a researcher's judgment and needs a person to fill it in; whether conditions match is a comparison between the config and the original words, which a machine can do a first pass on, leaving people only to review.
- **Testable**: Condition reconciliation has objective gold labels (whether a given run's config satisfies a given commitment), so we can compute precision and recall and, most importantly, the "**false-green rate**" (marked consistent when actually inconsistent). There is no data yet on annotation agreement for the five-value result.
- **Academic grounds for why it matters**: Gundersen & Kjensmo (AAAI 2018) surveyed 400 IJCAI/AAAI papers and found that only 20%–30% of each category of reproducibility variable was documented (U3 §4.1, [Fact, abstract page read]); Liu et al. CHI 2020 found that many analysis decisions are made implicitly, and warned of hindsight bias (U3 §5.1, [Fact]). [Inference] There is a missing stretch of context between "the conditions decided at the meeting" and "the conditions actually run," and this falls exactly into that gap. **But this only shows that "condition drift" exists at the paper level; it does not prove that pre-meeting reconciliation is a pain point for students**, which is [Assumption · to be verified] (§8 H-D1).
### 2.3 Narrowed to one step in one scenario

- **Scenario**: the **weekly group meeting or advisor 1-on-1** in a computational lab (ML / robotics / VLA).
- **Step**: **the night before the meeting**, when the student prepares the slide for "previous assignments / last week's progress" within the "previous assignments → current progress → next plan" structure (the Zhihu-recommended structure for "how to report when the group meeting has no progress," cited in U1 §3.3, [Summary]).
- **Sub-action**: for the **experiment commitments** the student verbally agreed to at last week's meeting (including those the advisor assigned to the student), confirm three things:
  1. Whether there is a corresponding run;
  2. Whether the run's conditions (benchmark, dataset split, number of seeds, key hyperparameters, model version) are the ones stated in the meeting;
  3. Which runs were executed but never promised by anyone (a side note).
- **How it is done today**: dig through the WeChat group or Slack, personal shorthand notes, and the W&B dashboard, then piece it together from memory. U1 §3.3 [Inference]: "It erupts all at once the night before the report, carries a sense of anxiety, and is high in intensity." There is currently **no first-hand data** on frequency or time spent; see §8 H-D1, H-D2.
- **JTBD**: *When I have to report last week's progress at tomorrow morning's group meeting, I want to confirm within 5 minutes that "every experiment I promised to run was run under the agreed conditions, with a link as proof," so that I don't freeze when the advisor asks "was this 5 seeds?" and don't put numbers from the wrong conditions into my slides.* ([Assumption, to be validated]; worded following the U1 §9 JTBD format, not a user quote.)

---

## 3. Dunford's Five Elements

### 3.1 Competitive alternatives (what students would do without this product)

| # | Alternative | How far it gets at this step | What it cannot do (relevant to this proposal) | Evidence |
|---|---|---|---|---|
| R1 | **Do nothing**: report from memory, and when asked say "let me go back and check" | Zero cost | Mismatched conditions only surface when writing the paper or reproducing results | [Inference]; Gundersen's 20%–30% documentation rate (U3 §4.1, [Fact]) indirectly shows that this kind of gap is real |
| R2 | **Manual reconciliation**: dig through group chats and shorthand notes, open the W&B dashboard and check each config one by one | Doable, and the most accurate | Time-consuming, depends on that night's attention; no persistent ledger, so it starts over every week | Rashid Lab handbook: "Review last week's action items," and at the end of the meeting "confirm assignees and due dates" (07 P7, [Fact]); MIT Cahoy policy requires reviewing the previous meeting's action items at the next meeting (U3 §3.1, [Fact]) |
| R3 | **ChatGPT / Doubao with pasted minutes**: "list last week's action items for me" | Can list action items; sufficient for a single use (07 A8, [Inference]) | Cannot see runs; starts from zero each time, with no ledger; uploading real group meeting content to external GenAI is subject to the target university's policy (00/06 §4.5) | 07 §5; 00/06 §4.5 |
| R4 | **DIY assembly: Claude + the official W&B MCP (+ Fellow / Granola MCP)** | **Technically can do most of it**: the official W&B MCP has `compare_runs_tool`: "Compare selected metrics and configuration across runs"; the Fellow MCP has `get_action_items` (07 F14) | ① A prompt must be written every time, with no fixed "condition slots" or judgment rules, so reproducibility is unknown; ② no "don't tick it if not found" discipline; ③ meeting content and run metadata must both be sent to a cloud model, subject to the target university's GenAI policy; ④ no persistent ledger | Opened this round: https://github.com/wandb/wandb-mcp-server ([Fact]); 07 F14, A7 |
| R5 | **Fellow** | Assignment during and after meetings, assignees accept or dismiss, unfinished items carried over per series with Always / Never / Ask me, two-way sync with GitHub via Zapier | Status is only complete, archived, and an AI-suggested state; **no result / evidence field seen**; no link from an action item to its source sentence seen; no education pricing | 07 F4, F8, F11–F13, F18, F20 ([Fact]) |
| R6 | **Littlebird (graduate student page)** | Records advisor meetings, lists "what you promised your advisor," and pre-meeting briefs include commitments and unaddressed feedback; Promise tracker compares commitments with "what actually happened" and outputs three states; student price $15/month | **Evidence sources are email, calendar, files, and on-screen content**; this round's check found the graduate student page **does not mention GitHub, W&B, experiments, or code**; the three states describe "whether it was fulfilled," not "whether the conditions were right" | 07 L2, L3, L9; opened this round: https://littlebird.ai/for/graduate-students ([Fact]) |
| R7 | **Feishu Meeting Express / Feishu Minutes** | Generates an "action item report" from the past week's smart minutes; action items trace back to the original text, and owners are identified automatically | Action items sync only completion status (U3 §1); no experiment-artifact evidence; in Singapore the international edition, Lark, is needed, and its availability is to be verified (06 §3) | 07 C5, C7, C8 ([Fact]) |
| R8 | **ZoomMate / Teams Facilitator** | Project agent, "weekly action items," can identify unclosed Jira issues (summary); Planner sync (preview) | Evidence source is the status in Jira / Planner; Facilitator supports only a single language and does not support 1-on-1 or external meetings | 07 Z1, Z3, Z6, T1, T6, T8 |
| R9 | **W&B Reports itself** | Organizes runs, embeds charts, "describes findings," exports LaTeX | Does not know what was promised in the meeting, and has no "commitment" object | U3 §4.1 ([Fact, original text read]) |
| R10 | Fabric, Supervisor Meeting Brief | Fabric's marketing page has a decision log and PI weekly reports, but names no customers; Supervisor Meeting Brief is a non-AI 1-on-1 extension with 0 ratings | Neither reconciles against experiment artifacts | 07 P1, P2, P4 ([Fact]) |

**[Inference] Ranking of the real opponents**: R2 (manual) ≈ R1 (do nothing) > R4 (DIY) > R6 (Littlebird) > the rest. Dunford says "No decision" is the biggest competitive alternative (03 §1.4, [Fact, secondhand]); for students with no budget, R1 and R2 are what must be beaten. R4 and R6 determine how long the window stays open.
### 3.2 Unique attributes (what the alternatives lack and this proposal has)

| # | Attribute | Compared against | Status |
|---|---|---|---|
| U-1 | **Committed "experiment-condition slots"**: extract benchmark / data split, number of seeds, key hyperparameters, model version, and comparison baselines from meeting notes as structured fields; missing slots stay empty, never guessed | R3–R8 only have "task / owner / due date" | [Inference]; not seen on any product page verified in 07 |
| U-2 | **Deterministic run reconciliation**: slots are compared against W&B config / Git metadata by rule, producing four states (consistent / condition mismatch / no evidence found / not tracked); **"not found" is never displayed as done** | R5 only has complete / archived, R6 only has three states, and neither uses runs as an evidence source | [Fact] (competitors' status models, 07) + [Inference] (this proposal's design) |
| U-3 | **Decisions as constraints**: decisions made in the meeting (e.g., "use rank 32 for all later experiments", "LIBERO-Long uses 5 seeds across the board") automatically become check conditions for later runs | Not seen | [Inference]; the eval-kit gold labels already contain sample decisions (M2-03, M3-09) |
| U-4 | **Default path where data never leaves the university**: text input, no recording; the LLM only does slot extraction and can be swapped for a local model; comparison is done by deterministic code | R3 and R4 default to cloud models | [Inference]; motivation in 00/06 §4.5 |
| U-5 | **Public reconciliation evaluation**: report precision / recall of condition reconciliation and the "false-green rate" on synthetic group meetings + synthetic run tables | 08 §5.2: academic benchmarks are sentence-level detection, and there are no public metrics on the product side | [Inference, not seen within the search scope] (08 §0-4) |

[Inference] U-1 to U-3 are feature differences, and any one of them taken alone can be copied. U-4 and U-5 are "constraint + proof", which echoes the pattern in 06 §1: "constraint-type gaps are actually confirmed by official documentation".

### 3.3 Value and evidence

| Value cluster | For whom | Existing evidence | What is missing |
|---|---|---|---|
| **V1 Less panic before the group meeting: 5 minutes to confirm "everything promised last week was run as agreed"** | Students | U1 §3.3 [Summary]: "what to report when there's no progress" is a recurring high-heat issue; manual workflows are repeatedly recommended, which suggests many people can't sustain them (U1 §3.2 [Inference]) | Preparation time, frequency of omissions: **zero first-hand data**. Fill in with R0 and classmates' diaries (§8 H-D1, H-D2) |
| **V2 Keep numbers with mismatched conditions out of slides / papers** | Students, PIs | Gundersen 2018 on variable-recording rates ([Fact]); Liu 2020 on implicit decisions and hindsight bias ([Fact]) | Incidence of "condition drift" at the group-meeting level: **zero data** (§8 H-D1) |
| **V3 Evidence that can be clicked open, not relying on memory** | PIs | Manual workflows at MIT Cahoy and Rashid Lab ([Fact]) | Whether PIs care: related to U6 H05, untested |
| **V4 Safe to use in real group meetings** | Students, the target university | The target university's GenAI policy and research data ownership (00/06 §4.5, [Fact]) | Whether the target university already has an approved enterprise AI tool, to be verified (00/06 open questions) |

**[Inference] Honest summary**: There is indirect evidence that the problems in V1 and V2 exist, but that **"reconciliation before the group meeting" is a pain point** currently has zero direct evidence. This is the biggest unknown in this proposal, and also the reason it chose "dogfood first": **it is the fastest of all the candidates to yield first-hand evidence**. The project owner and 1–2 classmates, over 2 weeks, can count the real number of commitments, the number of condition mismatches, and the preparation time.

### 3.4 Target customers (beachhead)

**Beachhead**: **Graduate students and RAs in computational labs (ML / robotics / VLA) at the target university who report experiment progress every week at group meetings or advisor 1-on-1s, and who record experiments with W&B (or TensorBoard + Git)**. The first cohort is the project owner's own group, then neighboring groups in the same school that share the GPU cluster.

| Moore criterion | Assessment | Basis |
|---|---|---|
| **Big enough to matter** | ◐ Big enough for a portfolio and validation; not big enough commercially | Scale: the number of computational labs and students at the target university is **not counted, to be verified**, no numbers invented; U1 §14 [Fact]: a single lab has 5–15 people; weak willingness to pay (U1 §13.1) |
| **Small enough to lead** | ● | An AI product built specifically for advisor meetings or group meetings "genuinely has no one building it as a standalone product" (07 §6 summary, [Inference]); the W&B reconciliation niche was not seen within the scope verified in 07 |
| **Good fit with crown jewels** | ● | The project owner is a member of this group; can read configs and experiment semantics; S0 already has the design of "citations validated server-side, missing fields not guessed, confirmation gate" (BriefPilot README / PRD) |
| **One key pain point** | ◐ | "Pre-meeting reconciliation" itself is [Assumption, to be validated] |
| **Reference customer / story** | ◐ | The project owner's own PI and classmates, provided the IRB and consent process goes through |
| **Next bowling pin** | ● Clear path | ① Neighboring computational labs → ② university-industry joint labs at the target university (U5 §5.1: Hyundai-[Univ]-A*STAR, AUMOVIO-[Univ], and other robotics directions, which have paying sponsors and whose quarterly review packs need "commitments × evidence") → ③ enterprise ML teams (U5 §5.4 control group; if U6 H10 does not hold, i.e. enterprises hurt just as much, the commercial story gets stronger) |

**Who we explicitly do not serve** (the cost of positioning): wet labs (evidence lives in ELNs and paper notebooks, with no run config); phases dominated by literature and writing (including the project owner's own current literature review work, which uses only a simplified adapter); people who need recording and verbatim transcripts; PIs who want a whole-group dashboard (deferred to Next).

### 3.5 Market category

- **Do not call it an "AI meeting assistant"**. In that category, Feishu, Otter, and Fellow are Class A core competitors competing on transcription and integrations, and this proposal would certainly lose.
- **Call it "the meeting layer for experiment tracking", or "the pre-group-meeting reconciliation sheet"**: place itself inside the W&B / Git workflow as the segment of context they lack (U3 §4.2 [Inference]: "BriefPilot should not build an ELN, and should not compete with W&B on experiment tracking. It should be a 'context layer'").
- [Inference] Per the user-scenario grid in 03 §9.2, classified this way, Feishu and Otter drop from Class A to Class B (overlapping scenario, different users), while W&B Reports and manual reconciliation move up to Class A / C. **Once the category changes, the "others" in "others have already built it" become a different set of players.**
### 3.6 Related Trends (Optional)

- [Fact] MCP adoption is spreading: W&B, Fellow, Granola, and Otter all have official or semi-official MCP servers (06 V2, 07 F14, this round's W&B repository). [Inference] This cuts both ways: it makes R4 (DIY) feasible, and it also means this proposal does not need to build its own integrations (00/06 §8.3, "integrations are not a moat").
- [Fact] Researchers' attitude toward AI is "it can help me organize, but it cannot judge for me," and privacy concerns are rising (Wiley 2025: from 47% to 58%; OUP 2024: only 8% trust AI companies not to misuse research data; U3 §0-4). [Inference] This maps to U-2 (never tick a box for the user) and U-4 (data stays on campus).

---

## 4. ERRC Grid

| Action | Factor | Rationale |
|---|---|---|
| **Eliminate** | Recording, meeting-joining bots, live transcription, voiceprint or speaker identification | Sidesteps recording consent, IRB recording clauses, and BIPA-style litigation risk (eval-kit README §5; Granola lawsuit 3:26-cv-07926-EMC); "no bot" is no longer a differentiator (05 §0-1) |
| **Eliminate** | Assignee claim UI, whole-group board, task-system integrations | G4 is already covered by Fellow (07 F8); a whole-group board needs multiple people present (G-3); integrations are not a moat (00/06 §8.3) |
| **Eliminate** | Decision-recall Q&A (G12) | Partly covered already, frequency untested (07 §8; U6 H11) |
| **Reduce** | Meeting summaries and key points: produce only the one-page "last week's experiment commitments reconciliation", not a full set of minutes | "nobody will ever read those notes" (M4 H1, [Fact]); Linear-style subtraction (03 §8.3) |
| **Reduce** | Output fields: owner / due date are filled only when the source text supports them | G3 passing bar |
| **Reduce** | Cloud dependency: real data goes to a local model by default; comparison uses deterministic code, not an LLM | The target university's GenAI policy (00/06 §4.5) |
| **Raise** | Evidence discipline: "no evidence found ≠ done", with the false-green rate as the primary metric | Answers the "can't trust it" complaints on HN (M4 §0-1); PAIR's principle of explaining "why" in high-stakes settings (05 G3) |
| **Raise** | A citation to the original words on every row (meeting-notes line number or timestamp), validated server-side | S0 ADR-004; G2 passing bar |
| **Raise** | Soft commitments, hypotheses, and rejected proposals are not tracked by default (grey, expandable) | eval-kit trap T-M1-1, etc.; Littlebird already does this binary split, so here it is only a passing bar |
| **Create** | **Experiment-condition slots × run config reconciliation (the "condition mismatch" state)** | §3.2 U-1, U-2; not seen within the scope verified in 07 |
| **Create** | **Meeting decisions → constraint checks on later runs** | §3.2 U-3 |
| **Create** | **A public "commitment–run reconciliation" mini-benchmark**: synthetic group meetings + synthetic run table + gold labels + scoring script | The incremental cell in 08 §5.2; reuses eval-kit |

**Value curve (text version)** [Inference]: On "transcription quality, number of integrations, degree of automation, full summaries," this proposal is **below** every meeting tool; on "evidence discipline, experiment semantics, data staying on campus, a reproducible public benchmark," it is **far above** them. The shape is different, not uniformly higher (03 §2.2 step 4).

---

## 5. Positioning Statement

**Moore six-line version** (03 §3.3 template):

```
For        graduate students and RAs in computational (ML / robotics / VLA) labs at the target university who report experiment progress every week at group meetings or in 1-on-1s with their advisor
Who        are dissatisfied with  flipping through group chats, meeting notes, and W&B dashboards the night before the group meeting, piecing together from memory "what we promised to run last week versus what actually ran";
           meeting tools can only tell them whether an action item is ticked
Our product is a  pre-meeting "experiment commitment × run" reconciliation sheet (the meeting layer for W&B / Git)
That provides  one click to match the experiments verbally promised at last week's meeting against the actual runs, item by item, by condition (dataset, number of seeds, key hyperparameters),
           marking each as "consistent / condition mismatch / no evidence found", with the original quote and a run link on every row, and no tick when no evidence is found
Unlike     Fellow, Littlebird, and Feishu meeting digests (which track "done or not", with task status, email, and documents as the evidence source),
           and "paste the minutes into ChatGPT/Claude" (starts from zero every time, has no ledger, and requires uploading real group-meeting content to an external model)
We have assembled  experiment-condition slot extraction, deterministic config comparison, verbatim-quote citation checks, no guessing on missing fields, no tracking of soft commitments,
           an interface that can switch to a local model, and a publicly reproducible reconciliation benchmark
```

**Dunford one-sentence version**: For graduate students in computational labs who, the night before the group meeting, have to check "the experiments we promised last week" against "the runs that actually ran in W&B," BriefPilot is a "pre-meeting reconciliation sheet": meeting tools tell you whether an action item is ticked, while it tells you **whether what ran is the one you promised**, and it will not tick a box for you when it cannot find evidence.

---

## 6. "Others already do this, so why are you building it?": the 30-second answer

> "Right, Feishu Minutes, Otter, and Fellow can all turn meetings into action items. Last month Fellow even launched 'assignees accept or reject for themselves,' and Littlebird also checks your email and documents to see whether you've followed through. I've verified all of this, and I don't treat any of it as a selling point.
> I only cover one step they don't: the **night before the group meeting**, a student in a computational lab has to match the experiments verbally promised last week against the runs that actually ran in W&B. The meeting said 5 seeds, all with rank 32, and the result is that one run used rank 16. That kind of 'it was done, but what ran wasn't what was promised' has no corresponding state in theirs, and their evidence source isn't runs.
> My tool produces the reconciliation sheet in one click, with the original quote and a run link on every row. When it can't find evidence, it writes 'not found' and doesn't tick the box for you. It doesn't record audio, it can run on a local model, and it meets the target university's requirements for research data. My groupmates and I use it every week, and its reconciliation accuracy has been tested on a public synthetic group-meeting set."

**What must be done before saying this** (otherwise delete the corresponding half-sentence): the last sentence's "use it every week" and "tested" can only be said once H-D2 in §8 and the benchmark have been completed. Until then, change it to "I plan to test it this way, and the abandonment threshold is ...".

**Three questions that will surely be asked**:

| Follow-up | Key points of the answer |
|---|---|
| "Can't Claude connect to the official W&B MCP, and then I just paste in the minutes?" | Concede that most of it can be pieced together (the official W&B MCP has `compare_runs_tool`, [Fact]). There are four differences: ① fixed condition slots and decision rules, so results are reproducible; ② "not found" is never shown as done, and this is measured with the false-green rate; ③ real group-meeting content does not have to be sent to an external model; ④ there is a cross-week ledger. **Abandonment threshold**: if the measurement in §8 H-D3 shows that DIY has a false-green rate and recall no worse than this proposal on the same benchmark, stop building and deliver the benchmark set and workflow (prompt + MCP configuration) as the output. This is the honest exit condition already written in 00/06 §8.3. |
| "Littlebird already serves graduate students; wouldn't adding a W&B data source let it catch up with you?" | Concede it; this is the top risk (07 §2 summary). This round verified that its graduate-student page does not mention GitHub, W&B, experiments, or code ([Fact]). Its route is "all-purpose personal memory" (email, screen, files), while this proposal's route is "experiment semantics + evidence discipline + data staying on campus". The window is 6–12 months per the 07 estimate; the demo's goal is to prove "someone wants this cell and it can be done accurately", not to claim a moat (03 §7.2). |
| "How frequent is this pain point?" | Answer honestly: there is currently zero first-hand data. In the synthetic samples, experiment-type action items account for about 19% (rough keyword count, [Inference]). A 2-week diary study will give real numbers; the abandonment threshold is in H-D1. |

---
## 7. The Demo's Magic Moment

### 7.1 The Magic Moment (30 seconds)

> **Wednesday, 23:40. Chen Siyuan (a synthetic persona) has a group meeting tomorrow morning.** He pastes in the notes from last week's group meeting (the plain-text version of eval-kit M3), selects the run source `lumavla-sim` (a synthetic run table, or fake runs written by script into a W&B test project), and clicks "Reconcile before meeting". About 10 seconds later a table appears:
> - ✅ **Resolution constraint satisfied**: M2 [Resolution M2-03] "From now on, LIBERO-Long always uses 5 seeds." All of his LIBERO-Long runs from last week used 5 seeds, and each one has a clickable link.
> - ⚠️ **Condition mismatch**: "Fill chunking up to 5 seeds and show me at next week's group meeting" (M3 [00:03:03], Zhou Lan). Five `chunk_size=8` runs were found, but the config of the seed=3 run has `lora_rank=16`, which contradicts the resolution at M3 [00:02:25], "use rank 32 for all experiments from now on".
> - ❓ **No evidence found**: the run corresponding to one commitment was deliberately deleted from the synthetic run table. It shows "not found" and is **not shown as fulfilled**, with a "Paste link manually" button next to it.
> - ⬜ **Not tracked (expandable)**: Daniel's "I might be able to look at…no promises" (a soft commitment), and "Maybe we should also filter by duration" (already rejected in M3-21).
>
> He opens the run link on the ⚠️ row, confirms he forgot to change the config, and reruns one seed. Then he clicks "Export last week's progress" and gets a one-page Markdown file to paste into his slides.
>
> **The magic is on the second row**: if the same notes are given to meeting tools, then according to the status model verified in 07, the most they can output is "chunking 5 seeds: done" or "action item". They have no "condition mismatch" state ([Inference], to be verified when testing on eval-kit).

### 7.2 Trust Boundaries (must be stated at the start of the demo)

- All data is synthetic (eval-kit README §5). The people, lab, and project are fictional, and the run table was built separately to match the synthetic story.
- In real use: text input and a local model. The comparison rules are deterministic code; the LLM is only responsible for extracting slots from the notes.
- Extraction can be wrong, so every row links back to the original wording. "Not found" does not mean "not done"; it only means "not found in the sources you provided".

### 7.3 Doing It in 2–4 Weeks (Solo)

| Week | What to do | Deliverables | Pass bar (written in advance, [Assumption]) |
|---|---|---|---|
| **W1** | ① Build the synthetic run table: following the cross-meeting chains in eval-kit M1–M4 (M1-04, M2-05, M3-04, M3-13, etc.), create 20–30 runs, seeding 2 condition mismatches, 1 missing run, and several "uncommitted runs". Optional: write them by script into a W&B test project so that R4 (Claude + W&B MCP) can be compared on the same data. ② **Run the DIY baseline first (H-D3)**. ③ Email irb@university.example, and log in to the university intranet to check the Graduate College template (07 §10-1). ④ R0 starts keeping a personal-use diary | `runs_lumavla.csv`, reconciliation gold labels (about 30–40 commitment–run pairs), DIY baseline results | If the DIY false-green rate and recall are already good enough, the abandonment line is triggered (§8) |
| **W2** | Extraction: reuse the eval-kit schema and add a `conditions` field. Comparison: config key-name normalization + rule matching; resolution constraint checks; report generation + quoted-sentence verification (reusing the S0 design) | End-to-end CLI version | On eval-kit, recall and citation accuracy for experiment-type commitments reach the pre-set thresholds |
| **W3** | Minimal UI (single page: paste → choose source → reconciliation table → export); local model provider (Ollama; an M1 Max with 32GB can run 8–14B models, U4 §0); scoring on eval-kit and the reconciliation gold labels (extend `score.py`) | Demo-ready version; evaluation report v1 | False-green rate ≤ the pre-set threshold |
| **W4** | Two rounds of real dogfooding: R0 uses the literature / writing adapter; 1–2 peers use the W&B adapter (run locally, with written consent). Write the 5-minute demo script and fill in the results template | Dogfood log, demo video script, results report | Preliminary numbers for H-D1 and H-D2 in §8 |

**The project owner's own dogfood adapter** [Inference]: commitments in survey work are mostly of the form "finish reading papers X and Y, and add column Z to the comparison table". The evidence source is the `survey/papers/txt` directory (110 files) and the revision history of the writing files. The mechanism is the same (commitment slots × artifact reconciliation), just without the W&B magic. **It is used only to ensure "real use every week" and does not go into the external narrative.**

### 7.4 Evaluation (Reusing eval-kit, with One New Item)

- **Inherited**: the extraction metrics eval-kit already has (recall of experiment-type commitments, owner / due non-guessing rate, soft-commitment promotion rate, trap false-extraction rate, injection).
- **New**: the four-state confusion matrix for commitment–run reconciliation, the **false-green rate** (the proportion of items whose gold label is "condition mismatch" or "not found" but which are output as "consistent"), and evidence-link accuracy.
- **Comparison groups**:
  - R3: ChatGPT / Claude with pasted notes + run table CSV;
  - R4: Claude + W&B MCP (if the W&B test project is built);
  - Optional: the action-item output of Feishu / Fellow, manually mapped to the four states; they can only land in the two states "consistent / not found".
- **Sample-size warning**: the reconciliation sample is only 30–40 pairs, so confidence intervals are wide (08 §5.5). Draw conclusions only where the gap is clear, and **do not publish a leaderboard**.

---

## 8. Make-or-Break Hypotheses and How to Validate Them

The thresholds are set in advance in this document [Assumption · to be validated], to prevent moving the goalposts after the fact. The samples are small, so always report n/N.

| ID | Hypothesis | How to validate (dogfood first, results within 2 weeks) | Pass line | Abandon line | What to do if it fails | Corresponding U6 |
|---|---|---|---|---|---|---|
| **H-D1 Frequency** | Students in computational labs have at least 1 "conditional experiment commitment" per week, and a considerable share of them are in "condition mismatch" or "no evidence found" before the meeting | R0 + 2–3 peers who run experiments, a 2-week diary: after each group meeting, note the experiment-type commitments; reconcile against runs once before the next meeting and record the result (no audio recording, text notes only) | Median ≥1 experiment commitment per week for ≥3 people; **and** "mismatch + not found" ≥15% of cumulative experiment commitments | Median <1 experiment commitment per week, **or** "mismatch + not found" <5% | Too few magic moments: fall back to Option A's evaluation route (G1 + G3) and demote reconciliation to a secondary feature | H01, H02 |
| **H-D2 Single-user value** | Students are willing to use the reconciliation sheet instead of manual reconciliation before group meetings, for 2 consecutive weeks | Give the W3 version to 2–3 peers; record whether they use it voluntarily in week 2 and their pre-meeting preparation time (self-reported, before vs. after) | ≥2/3 use it voluntarily in week 2 | 0/3 use it voluntarily, or they all say "I remember it myself / a quick look in W&B is enough" | The value is not enough to change behavior: stop productizing and keep the evaluation set | H04 (alternative form: the system finds, the user clicks) |
| **H-D3 DIY substitute** | Claude + W&B MCP (or pasting a CSV) is clearly worse than this approach on the same reconciliation gold labels (especially the false-green rate) | W1 test: the same notes + the same run source, fixed prompt, run 3 times | This approach's false-green rate is ≥15 percentage points lower than DIY, **or** DIY needs ≥3 rounds of manual follow-up to finish | Gap <10 percentage points, and DIY finishes in one round | **Trigger an honest exit** (00/06 §8.3): do not build the product; deliver "evaluation set + DIY workflow" as the portfolio piece | — |
| **H-D4 Extraction feasibility** | An LLM can reliably extract condition slots from mixed Chinese-English notes; a local 8–14B model is not much worse | eval-kit M1–M4 + reconciliation gold labels; run once with an API model and once with a local model | Slot accuracy ≥80% (API); local model gap ≤15 percentage points | Slot accuracy <60% | Switch to a "semi-structured note template" (students write `@exp dataset=… seeds=…`) to lower the extraction difficulty | — |
| **H-D5 Compliance path** | Local processing + text input can be legitimately used on this group's real meeting content | Written IRB reply by email; check whether the target university has an already-approved AI tool; ask the advisor | IRB determines dogfooding is not research, or approves it; advisor gives written consent | Even local processing is prohibited | Use only synthetic data + R0's own literature commitments for the demo, and state this honestly externally | H08 |
| **H-D6 Window** | Littlebird / Fellow have not launched an "experiment-artifact evidence source" before the demo is finished | Every 2 weeks, re-check the official pages listed in 07 (with access dates) | Not seen within 4 weeks | Already launched | Change the narrative to "I built a public evaluation on top of them; their false-green rate on condition reconciliation is X", shifting from "building a product" to "building evaluations and workflows" | — |

**Decision tree** [Inference]:
- H-D3 runs first (W1), because it is the cheapest and can veto building the product on its own.
- H-D1 and H-D4 decide "whether to build reconciliation at all".
- H-D2 decides "whether to tell the product story".
- H-D5 decides "whether real data can be used".

---
## 9. Rejected Alternatives and Rationale

| Alternative | Reason for rejection (from this perspective) | What is kept |
|---|---|---|
| **Option A** A verifiable, claimed commitment layer | G4 is already covered by Fellow (07 F8, 2026-10-01); provenance is covered by Feishu (07 C7); a purely horizontal feature, and "feature differentiation alone is the most fragile" (03 §8.5); claiming requires multiple people, which fails G-3 | G2 (verbatim quote) and G3 (don't guess missing fields, don't chase soft commitments) as the passing bar; the G1 evaluation as the means of proof |
| **Option B** PhD student–advisor 1:1 two-way ledger + advisor confirmation gate | Littlebird's graduate-student page already covers the personal-perspective version (07 L9); zero evidence for "commitments the advisor owes the student" (U6 H06); no advisor-supervision record system found on the target university's public pages (07 U7); the advisor confirmation gate requires advisors to enter the system (cold start, power dynamics) | Later: export Loughborough / Surrey-style supervision forms (the single-user feature suggested in 07 §8.1-4) |
| **Option C, original version** (five-value outcome + decision-retrospective Q&A) | No evidence for the five-value semantics (06 W10); back-filling cost falls on the student (U6 H04); frequency of decision retrospectives untested (U6 H11); cannot be finished in 4 weeks | The five values as an optional field; Q&A deferred until ledger data exists |
| **Option D** Mixed Chinese–English terminology assistant | Needs real audio, which involves recording consent and IRB; no first-hand Chinese pain points (06 W4); Feishu has enterprise information recognition (07 C6); the text-first route makes the ASR problem disappear | The term-recall metric in the evaluation (already in eval-kit) |
| **Option E** Vendor-side requirement-change ledger | The project owner has no material, so dogfooding doesn't hold (05 §4.7) | The outward-facing generalization narrative (U5 §5.2) |
| **Option F** Open-source meeting → issue | The project owner is not a maintainer; willingness to pay is 0 | Public data can serve as supplementary evaluation |
| **U5 ladder extension segment**: university–industry joint lab "quarterly review pack + objection window" | Zero evidence of confirmation from the company side; compliance score 2; within 4 weeks it can only be fully synthetic, and moving forward requires external interviews (U5 §5.1) | **Bowling pin 2**; DESCA's "default accept + objection window" as the default rule for future confirmation interactions |
| **G10 weekly report drafting** | Pasting into ChatGPT is enough (07 §5) | The ledger's "export last week's progress" is itself a section of the weekly report, included as a bonus rather than sold |
| **Brand-new option: pure evaluation product** (only public evaluation + competitor error analysis, no product) | Can answer interviewers, but has no "use it myself every week" loop, which doesn't fit this perspective | **The fallback if H-D3 fails**, which is exactly this |

---

## 10. Response to New Round 2 Evidence

| New Round 2 evidence | Source | Impact on this plan | This plan's response |
|---|---|---|---|
| Fellow's AI-suggested action items can be accepted or dismissed by the assignee; auto-accept is off by default (2026-10-01) | 07 F8 | G4 is out; Option A loses its main selling point | No claiming UI; the comparison table honestly states that Fellow has claiming |
| Fellow has only complete, archived, and AI-suggested states, with no outcome or evidence fields; GitHub sync goes through Zapier | 07 F11–F13 | Proves the "conditions don't match" state does not exist in Fellow's status model | Used as comparison evidence for U-2; "GitHub sync" is not treated as a selling point |
| Littlebird graduate-student page, promise tracker comparing against "what actually happened", student price $15 | 07 L2, L3, L9; re-verified this round | The top risk; the evidence source is isomorphic | Differentiation rests on "evidence source is the run + condition-level comparison + data never leaves the university"; this round confirmed the graduate-student page does not mention GitHub or W&B; H-D6 rechecks every 2 weeks |
| Feishu meeting digest, action item traceback to source text, enterprise information recognition | 07 C5–C8 | Weekly summaries and provenance are already covered in the Chinese market | Used only as the passing bar; do not pitch "cross-meeting tracking" |
| Window of 6–12 months, "could be closed by a single Littlebird iteration" | 07 §8.1 | Cannot claim a "market gap" | The narrative uses "how far others have gone, where I go deeper, proven with numbers" (07 §8.1-3) |
| Academic benchmarks: ICSI is exactly research group meetings; AMC-A claims to be the first Chinese one; cannot claim "first" | 08 §0, §5.1 | The evaluation narrative must change | Say only "existing benchmarks evaluate sentence-level detection; what I evaluate is **commitment–run condition reconciliation** and **not guessing when information is missing**, not seen within the search scope"; recheck arXiv the week before interviews (08 §6) |
| Target university IRB: interviews count as research and need prior approval; the target university's GenAI policy does not allow uploading confidential / personal data to external GenAI | 00/06 §4.4, §4.5 | The cloud path for real group-meeting data is restricted | Text-first + local model + deterministic comparison; send the IRB email before dogfooding; demo uses synthetic data only (H-D5) |
| Cold start: be useful to a single person first, then grow a network | 00/06 §1 | Supports a single-user plan | Now is entirely single-user in this plan; whole-group board and advisor confirmation go to Next / Later |
| Build / Buy: build only commitment semantics, verification, outcome back-fill, and the evaluation set; "stitching together on Fellow / Granola via MCP" needs an exit condition | 00/06 §8.3 | Maps directly to H-D3 | The abandonment line is already fixed |
| New segment: university–industry joint lab 3.50, ladder ceiling about 3.80; enterprise ML teams as a comparison group | U5 §0, §5 | Bowling-pin path | Pin 2 = university–industry lab, pin 3 = enterprise ML (see U6 H10) |
| eval-kit: 5 synthetic meetings, 135 gold labels, 30 cross-meeting commitment chains, `score.py` self-tested | eval-kit README | Lets the G-4 gate pass | Reuse M1–M4 directly; add a run table and reconciliation gold labels; the gold labels were AI-drafted, so they need manual review and double annotation before going public (README §5-6) |
| User research execution pack: 14 hypotheses, diary study, IRB email template | U6 §1, §4, §6 | Validation tooling is ready-made | H-D1 maps to H01, H02; H-D2 to a variant of H04; H-D5 to H08; add one field to the diary form: "whether the conditions of the experiment commitment match the run" |
| W&B's official MCP has `compare_runs_tool` (new this round) | https://github.com/wandb/wandb-mcp-server | The DIY route works, and R4 becomes a real opponent | Run H-D3 in week 1; if it doesn't pass, exit honestly |
| ChatGPT Record is macOS-only, works best in English (summary; original page returned 403) | 07 A1–A4 | Small impact on this plan (it does not record audio) | R3 serves as the baseline for pasted minutes |

---
## 11. 7 Powers Self-Check and Window

- **There is no Power today** [Inference]: U-1 through U-3 are all features, and Littlebird, Fellow, and W&B can each add them on their own.
- **Possible seeds**:
  1. **Weak counter-positioning**: The big vendors sell "more automatic, auto-mark as done" (M2 §0-3); this proposal sells "no evidence found, no checkmark." For vendors built on a "fully automatic" narrative, proactively showing "not found" would undercut their pitch (03 §4.2 [Assumption]).
  2. **Switching cost**: If someone uses it for a full semester, the ledger of "commitment × run × decision" becomes source material for writing the thesis (U3 §5.2 scenario 1), and switching tools would lose that context (03 §4.2 [Inference]).
  3. **Evaluation set**: A public reconciliation evaluation set is not a moat in itself, but it is a source of credibility and the starting point for the G21 correction feedback loop.
- **Window**: Following the estimate in 07, 6–12 months, and it could be closed by a single Littlebird iteration [Inference]. **The goal of the 2–4 week demo is "prove that someone wants this slot and that it can be done accurately," not "capture the market."**

---

## 12. Items to Verify and Owner's Next Steps (by priority)

1. **W1 day 1**: Send the IRB email (template in U6 §6); log in to the university intranet to check the Graduate College template (07 §10-1); ask the advisor whether the tool can be dogfooded in this group (local run, text input).
2. **W1**: Confirm the actual toolchain of yourself and your labmates: is it W&B, or TensorBoard / CSV / MLflow ([Assumption, to be verified], determines adapter priority).
3. **W1**: Run H-D3 (Claude + W&B MCP DIY baseline). In this round, the W&B docs site's MCP page landed on an access-code page, so **treat the GitHub repository README as authoritative, and verify the hosted endpoint and permissions when actually trying it**.
4. **W1–W2**: Add an "experiment commitment condition reconciliation" field to the diary study (the D form in U6 §4.4).
5. **Re-check cadence**: Open the Littlebird graduate-student page, the promise tracker page, and the Fellow help center's AI suggestion article every 2 weeks, and record the access date (H-D6).
6. **One week before the interview**: Search arXiv for "meeting action item owner deadline benchmark" and "experiment provenance meeting" to confirm that a "conditional reconciliation evaluation" still does not appear (08 §6).

---

## Source List

**Newly opened this round (accessed at the time of writing)**
1. Littlebird graduate-student page — https://littlebird.ai/for/graduate-students [Fact: the page does not mention GitHub, W&B, experiments, or code; it says "what you promised your advisor", pre-meeting briefs, and a student price of $15]
2. W&B official MCP server repository — https://github.com/wandb/wandb-mcp-server [Fact: "The official implementation of the W&B Models and Weave MCP server"; `compare_runs_tool`: "Compare selected metrics and configuration across runs"]
3. W&B MCP docs page — https://weave-docs.wandb.ai/reference/gen_notebooks/wandb_mcp_server → 301 → docs.wandb.ai → 301 → docs.coreweave.com (access code required) [To be verified]
4. WebSearch summary: W&B hosted MCP endpoint https://mcp.withwandb.com, API key required [Summary]

**Official sources verified in Round 2 and reused (original access date at the time of writing, not reopened for this document)**
5. Fellow AI-Suggested Action Items — https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items (07 F8–F10)
6. Fellow Action item page — https://help.fellow.ai/en/articles/4144380-action-item-page (07 F6, F11)
7. Fellow Carry incomplete items forward — https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward (07 F4)
8. Fellow Action items feature page — https://fellow.ai/features/action-items (07 F12)
9. Fellow × GitHub — https://fellow.ai/integrations/github (07 F13)
10. Fellow MCP server — https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server (07 F14)
11. Fellow pricing — https://fellow.ai/pricing (07 F18, F19)
12. Littlebird Promise tracker — https://littlebird.ai/routines/promise-tracker (07 L1–L4)
13. Littlebird pricing — https://littlebird.ai/pricing (07 L8)
14. Littlebird Teams — https://littlebird.ai/teams (07 L7)
15. Feishu intelligent meeting minutes — https://www.feishu.cn/content/article/7577317993749269689 (07 C5, C6, C11)
16. Feishu Tasks and reminders — https://www.feishu.cn/content/article/7600354912756681687 (07 C7–C9)
17. Zoom AI Companion / ZoomMate — https://www.zoom.com/en/products/ai-assistant/ (07 Z1, Z3)
18. Microsoft Teams Facilitator — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (07 T1, T6, T8)
19. Fabric academic labs page — https://fabric.so/teams/academic-labs (07 P1, P2)
20. Supervisor Meeting Brief (Chrome extension) — https://chromewebstore.google.com/detail/fmibimgfmoaogdajeoeedledhejppgll (07 P4)
21. Rashid Lab meeting leader guide — https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html (07 P7)
22. Target university SBS TAC page — (university page; link removed) (07 U7)
23. ChatGPT Record help page — https://help.openai.com/en/articles/11487532-chatgpt-record (403, 07 A1–A4 [Summary])

**Research and policy sources reused from earlier files (see the original files for access details)**
24. MIT Cahoy advising policy — https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf (U3 §3.1, [Fact, original text read])
25. Gundersen & Kjensmo, AAAI 2018 — https://mlanthology.org/aaai/2018/gundersen2018aaai-state (U3 §4.1, [Fact, abstract page read])
26. Liu, Althoff, Heer, CHI 2020 — https://ar5iv.arxiv.org/html/1910.13602 (U3 §5.1, [Fact])
27. W&B Reports docs — https://docs.coreweave.com/products/wandb/reports.md (U3 §4.1)
28. Target university policy on generative AI use in research — (university page; link removed) (00/06 §4.5)
29. Zhihu, "研究生组会，没有进展怎么汇报？" (How to report at a graduate group meeting when there is no progress?) — https://www.zhihu.com/question/268901881 (U1 §3.3, [Summary])
30. Granola class-action coverage (3:26-cv-07926-EMC) — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ (06 V14)
31. Hacker News thread ("nobody will ever read those notes") — https://news.ycombinator.com/item?id=48823024 (06 supplementary verification)

**Methodology**: April Dunford's five components, Blue Ocean ERRC, Moore's beachhead and positioning template, and 7 Powers are all covered in `00_pm-skills/03` (items 1–38 of its source list). Cold start, IRB, Build / Buy, and Now-Next-Later are covered in `00_pm-skills/06`.

---
## Confidence in This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| The competitors' status models have no "condition mismatch" state, and their evidence source is not a run | **Medium-high** | Based on the official pages opened on 07 and this round's Littlebird re-check; "the page doesn't say so" ≠ "the product doesn't have it", so this can't be stated definitively before eval-kit testing |
| DIY (Claude + W&B MCP) is technically feasible | **High (feasibility) / Unknown (effectiveness)** | The official repository confirms the tools exist; effectiveness has not been tested (H-D3) |
| "Reconciliation before the group meeting" is a real pain point and occurs frequently enough | **Low** ([Assumption]) | Only indirect evidence (reproducibility literature, summary-level UGC about reporting anxiety); zero interviews, zero diaries |
| This approach beats A–F on the five dogfood gates | **Medium** | The gates were defined by this perspective itself, and the scoring is the researcher's judgment; other perspectives (business, interview narrative) might produce a different ranking |
| It can be finished end to end in 2–4 weeks | **Medium-high** | eval-kit and the S0 design can be reused; the risks are the extraction quality of local models (H-D4) and the unknown real toolchain (§12-2) |
| The project owner can dogfood the W&B adapter personally | **Low** | The project owner is currently working on a literature review, and their W&B usage is unknown; the W&B leg depends on a labmate in the same group |
| Experiment-type actions make up about 19% | **Low** | Comes from AI-drafted synthetic gold labels, counted roughly by keywords; it is only used to flag risk and must not be cited externally |
