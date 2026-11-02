---
title: BriefPilot v2 · Meeting Ledger — One-Page Summary (Read This First)
status: "summary-v1 (end of round two; positioning is \"conditionally viable\": zero interviews, zero hands-on competitor testing, zero product code)"
sources_count: 0
sources_note: This page introduces no new facts and only summarizes files within the project; for external sources see the sources section of each file (accessed at the time of writing)
---

# One-Page Summary: Others Already Built It, So Why Am I Building It?

> **Update**: The product has been built; see `06_product/`, and for test results see `07_results/00_test_report.md`. This page was written before development, so "zero code" and "start in week 2" in Sections 5 and 6 are out of date. The evaluation ran on a real model, but the gold labels have not been manually reviewed; the personas were played by AI, so real users are still 0. The top risk (Claude reconciling directly and tying) is still untested.

## 1. Final Positioning (One Sentence)

**For graduate students in the target university's computational labs who report progress at a weekly group meeting and whose group has transcript exports or rotating minutes: meeting tools handle the "bookkeeping," and the Meeting Ledger handles the "reconciliation." It uses what is said at the next group meeting to proactively, in batch, propose the current status of every commitment from the previous meeting (fulfilled / partial or rescheduled / dropped / not mentioned), attaches two verbatim-checkable evidence snippets to each entry, and leaves confirmation to you. Rules set in the meeting ("use rank 32 from now on") can also be checked against later run configs. If no evidence is found, it writes "not found" and does not tick anything off for you.**

(See `03_positioning/03_final_positioning.md` §0 for details; the project codename remains BriefPilot v2, and externally it is called the "Meeting Ledger.")

## 2. The Small Unmet Need

- **Step**: Between two group meetings, the step of "what is the status of last week's commitments and decisions now." Status changes are mostly said aloud at the next meeting ("halfway through the run," "not doing it for now," "fixed it") — **this is assumption P-H4, not yet tested**.
- **What already exists on the market (the passing bar, not a selling point)**: carrying over unfinished items (Fellow), cross-meeting Q&A (Otter, Granola, Circleback, Fireflies, Tongyi Tingwu), a weekly check of your commitments (Littlebird), capturing group-meeting decision logs (Fabric), reviewing unclosed action items (ZoomMate), single-item closeout (open-source Minutes).
- **Not seen within the search scope (our increment, one and a half items)**:
  1. In a **multi-person group meeting**, using what is said at the next meeting to **proactively, in batch** propose new statuses for all commitments from the previous meeting and ask for confirmation;
  2. (Second beat, depending on frequency) a **deterministic comparison** of decisions made in meetings against the config of later runs.
- "Not seen within the search scope" does not mean nonexistent; all competitor judgments are still "the page says / doesn't say," with no hands-on testing at all.

## 3. Why Not Feishu Minutes / Otter / Fellow (and Closer Rivals)

| Rival | What it does (official pages) | Difference |
|---|---|---|
| Feishu Minutes + Meeting Digest | Produces action items for each meeting, traceable to the original text; Meeting Digest summarizes a week's action items; recognizes mixed Chinese-English speech | It describes "summarizing," not "using the next meeting's speech to close out the previous meeting's items" |
| Otter and other incumbents | Has full history; can answer cross-meeting questions when asked | Passive Q&A; no mention of proactively proposing in batch and asking for confirmation (E2d to be tested) |
| Fellow | Surfaces unclosed items before each recurring meeting; AI-suggested items can be claimed; syncs to GitHub via Zapier | Completion is ticked by a person; the page doesn't mention automatically changing status from later speech |
| Littlebird (has a grad-student page) | Context includes meetings, email, calendar, screen; each week extracts your commitments from that week's meetings and produces three states by cross-checking email and documents | The page doesn't mention using **later** meeting speech to determine status; the grad-student page only covers advisor meetings, not multi-person group meetings |
| ZoomMate | Can review "unresolved action items" and generate status updates based on decisions | Doesn't mention proactively proposing the previous meeting's statuses and asking for confirmation; regional availability to be verified |
| **You yourself + Claude with long context** | Quite possibly does well — **the top rival** | Test with P-H1 line-by-line pairing; if it fails to pass the pre-set winning count, admit it is "just a workflow" |

## 4. What the Demo Should Show (5 Minutes, `05_demo-plan/02`)

1. **0:00–1:00** A synthetic scenario: the advisor says "the rank 32 main result needs to be rerun," and the following week the student is still reporting the old number 71.2% to a collaborator. First acknowledge what competitors already do.
2. **1:00–2:00** Paste M3 → what comes out is a **diff** against last week's list (4 types of transitions); **place side by side the raw output from handing the same M3 to a Claude expert prompt**, and point out the rows where the judgments differ.
3. **2:00–3:00** Two evidence snippets; show one model rewrite blocked in a real log (admit this is only a trust foundation, and Claude + grep can do it too); injected text is treated as content only.
4. **3:00–4:00** Stale-number check (71.2%), "not mentioned for N meetings," post-meeting follow-up questions on private drafts, exporting the reconciliation sheet; only demonstrate "fulfilled but conditions don't match" if P-H6 has results.
5. **4:00–5:00** One table: the first row is the number of times "half-done but judged fulfilled" (`fgr_mentioned`), with dev set / test set separated, and line-by-line pairing results; anything not run is marked "untested."
- **External demo gate**: Until P-H1 and P-H2 each have at least one real number, **no external demo**.

## 5. Current Strength of Evidence (Honest Version)

| Aspect | What exists | What's missing | Strength |
|---|---|---|---|
| Competitor capabilities | Official pages verified item by item (07, 09; Littlebird, ZoomMate, Fabric, Minutes checked verbatim this round) | **Zero hands-on product testing** | Medium (only up to "what the page says") |
| Need | The lab handbook has a "review last week's action items" step | **Zero interviews, zero diaries**; "first said aloud," "not written back," "has a cost," "will use it weekly" are all assumptions | **Weak** |
| Capability difference | Evaluation assets built: 5 synthetic meetings, 135 gold labels, draft transition gold labels (23 rows + 75 not-mentioned rows), `score_recon.py` (self-test passed), DIY baseline prompt | DIY baseline not yet run; gold labels drafted by a model, not double-annotated | **Unknown** (most likely to be overturned) |
| Second beat (decisions × runs) | Synthetic run table (landmines I planted myself) | Zero data on real frequency | Weak |
| Rationale for selection | "Fastest to be falsified, and the evaluation assets can be reused after failure" | Not "ranked first on score" (simulated judges' score gap of 0.23 is within noise) | — |
## 6. Execution plan for the next 2 weeks (all done by the project owner)

**Week 1: no product code**
- [ ] D1 morning: send the IRB determination email (template in `02_user-research/06` §6.3), and in the same email ask whether the target university's IT has an approved cloud AI (P-H10)
- [ ] D1: review the draft transition gold labels `05_demo-plan/eval-kit/gold/recon/transitions.gold.jsonl`, adjudicate the 4 rows marked "pending adjudication"; write the winning count k into `eval-kit/results-template.md` §6.1 and sign with the date
- [ ] D1–D2: **competitor test, DIY track**: following `eval-kit/templates/expert_reconcile_prompt.md`, run E2 and E2-naive 3 times each → `score_recon.py --from-diy` → E2c → score; check whether the P-H1 shortcut is triggered
- [ ] D2–D3: find 1 classmate to annotate the 23 rows independently, plus sample ≥20 not-mentioned rows, and compute κ (P-H8)
- [ ] D3–D5: **interview + diary recruitment**: 3–5 people for a 2-week diary (at least 2 from outside this group; the form includes D13, D14, D15, F4), and at the same time schedule 2–3 Mom Test interviews (`02_user-research/06` §3)
- [ ] D3–D5: **concierge round 1** (P-H12): manually produce one reconciliation sheet each for 2 classmates (at least 1 from outside this group)
- [ ] End of W1: 30-minute decision meeting, fill in only "pass / fail / gray zone"

**Week 2: start the demo (if the P-H1 shortcut was not triggered)**
- [ ] **Start the demo**: P0 = F01–F06 + F11, CLI + static HTML (`05_demo-plan/01` §13 Prompts ②③)
- [ ] **Competitor test**: first a 30-minute feasibility check (Meeting Express weekly cadence, Lark, whether Fellow can upload audio, ZoomMate regions), then test **one** product; for E2d, pick one incumbent product's cross-meeting Q&A
- [ ] Littlebird: in a meeting set containing only your own meetings, play M1–M5 through TTS on a weekly basis (first check in the app whether a target university email can get the student price)
- [ ] Ask a non-owner to rewrite M3 and M4 in their real shorthand note-taking style (shorthand-notes condition)
- [ ] Concierge round 2; **P-H12 gate at end of W2: 0 of 2 people willing to paste it into their slides → stop the UI and deliver only the evaluation**
- [ ] If the target university has no approved cloud tool: at the end of W2 run one evaluation round with Ollama Qwen3 as the release condition for dogfooding
- [ ] Continue the diary and interviews

## 7. File navigation

| Read first | File | In one sentence |
|---|---|---|
| 1 | `03_positioning/03_final_positioning.md` | Full positioning: the five-component positioning framework, value curve, defensibility, 12 make-or-break assumptions (P-H1–P-H12) |
| 2 | `03_positioning/pr-faq.md` | One-page PR-FAQ: press release and common follow-up questions |
| 3 | `05_demo-plan/02_demo_script_and_pitch.md` | Minute-by-minute 5-minute script, release conditions, elevator pitch |
| 4 | `04_prd/01_PRD_v2.md` | PRD: assumptions, metrics, scope (§11.0 priority mapping), feature specs, data model, AI behavior spec, evaluation |
| 5 | `05_demo-plan/01_demo_scope_and_tech_plan.md` | Technical plan, schedule (W1–W4 + 2-week compressed version), evaluation integration, Claude Code segmented prompts |
| 6 | `05_demo-plan/eval-kit/README.md` | How to run the evaluation kit (`score.py` + `score_recon.py`) |
| 7 | `02_user-research/06_user_research_kit.md` | Interview guide, diary form, recruitment, IRB email, decision tree |
| 8 | `05_demo-plan/04_consistency_check.md` | Cross-file consistency check + fix log at the end (what has been fixed, what is still yours to do) |
| 9 | `01_market-research/07`, `09` | Item-by-item competitor verification; Minutes and experiment-tracking tools |
| — | `README.md` | Full file list with a one-sentence description of each |
