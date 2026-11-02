---
title: BriefPilot v2 · Meeting Ledger — One-Page PR-FAQ (internal use; result numbers to be filled in)
status: draft-v1 (written at wrap-up to fix the dead links from 00_pm-skills/01 and 01_market-research/05; content extracted from the Q&A notes (not included in this repository) and 03_final_positioning decision-v1.1, no new facts added; the press release is written as "assuming P-H1 and P-H7 both hold", not as the current state)
sources_count: 0
sources_note: No new external facts introduced; competitor facts are in 03_positioning/03_final_positioning.md §5.1 and 01_market-research/07, 09
---

# PR-FAQ: Meeting Ledger

> **How to read this**: An Amazon-style PR-FAQ. Write the "press release for the day the product succeeds" first, which forces **specific users and specific numbers**; if you can't write them, it's too early to write code (a requirement of `00_pm-skills/01`). In the press release below, **every `__` is a number that has not been measured yet**. Do not fill them in or share this externally until P-H1 (DIY comparison), P-H7 (trial retention), and P-H12 (concierge gate) have been run.

## Press Release (Hypothetical, December 2026)

**Graduate student in a computational lab at the target university launches "Meeting Ledger": meeting tools keep the notes, it reconciles the ledger**

Singapore — Every Thursday the group meeting opens with the advisor asking, "Did that run from last week finish?" Most of the answers are spoken aloud in the meeting: half done, put on hold, fixed. Meeting tools generate a fresh set of action items for each session, and can dig up old records when asked, but none of them proactively checks this week's discussion against last week's ledger.

Meeting Ledger does only that one step. A graduate student pastes in the group's transcript export or the rotating-scribe minutes, and it automatically, in batch, reconciles this week's statements against earlier commitments: fulfilled, partial or rescheduled, dropped, or not mentioned. Every entry carries two evidence snippets that can be checked verbatim; when nothing matches it writes "not found" instead of ticking a box for you. If the meeting decided "use rank 32 from now on," it checks whether later runs actually followed that.

"On 5 synthetic group meetings, I compared it line by line against 'paste four weeks of minutes into Claude with an expert prompt'. Across 23 cross-meeting reconciliation rows, there were __ rows where it was wrong and I was right, and __ the other way round; for items that were only half done but got judged 'fulfilled', it did so __ times and I did so __ times," said the project owner. "Two classmates used it for 4 group-meeting weeks, and __ of them reconciled the ledger within 24 hours after the meeting for 3 consecutive weeks and exported a reconciliation sheet before the meeting."

## External FAQ (what users and interviewers will ask)

| Question | Answer | Basis |
|---|---|---|
| Feishu Minutes, Otter, and Fireflies already do this. Why build it? | They turn each meeting into action items and can dig up old records when asked. I only do the "reconciliation" between two group meetings: proactively, in batch, checking this week's statements against last week's commitments and having you confirm. Carrying over unfinished items, cross-meeting Q&A, capturing decisions, and group-level ledgers are table stakes, not my selling point | Positioning §5.2 boundaries |
| Doesn't Littlebird already check commitments every week? | Its context is meetings, email, calendar, and screen; each week it extracts your commitments from this week's meetings and checks them against email and documents. Its pages don't say it determines status from statements in **later** meetings, and its graduate-student page only mentions advisor meetings. I'm testing this on synthetic data | Positioning §5.1 R6, P-H3 |
| Can't I just paste it into Claude? | This is the number one rival. I use it (and "its output + the same verbatim filter") as the baseline and compare line by line; if I don't clear the win threshold written down in advance, I'll admit this is just a workflow and change the deliverable to an evaluation set | Positioning §11 P-H1 |
| Does it need recordings? | No recording, no transcription. The main input is the transcript export the group already has, or rotating-scribe verbatim minutes; your own shorthand notes also work, but count only as "excerpt" evidence | Positioning §4.1 |
| Does the advisor need to sign up? | No sign-up, but real use requires one-time informed consent from the whole group; without it, only your own commitments are recorded | Positioning §2.1 R2; PRD §16 P1 |
| Will post-meeting follow-ups be sent to the group chat automatically? | No. The default is a private draft; whether to send it, and to whom, is your decision | PRD §4.2 |

## Internal FAQ (questions I must answer for myself first)

| Question | Current answer | When I can answer better |
|---|---|---|
| Is the need real? | **Unknown**. Zero interviews, zero diaries. The earliest kill gate is P-H12: manually make 2 reconciliation sheets each for 2 classmates; if 0 of 2 are willing to paste them into their slides, stop the UI | End of W2 (P-H12); W3–W6 (P-H4, P-H5, P-H7) |
| How much better is it than DIY, really? | Not tested. Execution assets are built: `eval-kit/score_recon.py`, the draft transition gold labels, and the E2 / E2-naive / E2c / E2d prompts | W1 D1–D2 (P-H1 shortcut) |
| Have competitors been tested hands-on? | No. Every competitor judgment is "the page says / doesn't say" | W2 (test only one) |
| How long is the window? | Feature level: 1–3 months; evaluation and ledger: 6–12 months. Enough for a portfolio piece, not enough to present as a "market gap" | Competitor-alert recheck on the 1st of each month |
| Was this direction chosen because it ranked first in the simulated scoring? | No. The 0.23 score gap is within the noise. I chose it because it is **the fastest to falsify, and the evaluation assets can be reused after a failure** | — |
| What if P-H1 fails? | The deliverable becomes "a cross-meeting reconciliation evaluation set + DIY workflow recipe + failure-mode table"; in interviews I'd say, "I used data to falsify my own capability hypothesis" | — |
