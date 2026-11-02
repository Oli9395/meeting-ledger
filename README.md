# Meeting Ledger

Tasks go on the board after one meeting. The next meeting settles what happened to them.

**License:** [MIT](LICENSE)

![Screen recording: from the sample ledger to confirming a status change, then the task board](06_product/docs/screenshots/demo.gif)

> This is a real screen recording of the product using its sample ledger. The people and meetings are fictional, and the content replays one real model run.

**The problem:** Meeting tools can already generate to-dos. Once they exist, finding out what happened to last week's commitments usually still means someone digging or asking around. Meeting Ledger (project code name BriefPilot v2) reads what people say in the next meeting and proposes a new status for each earlier item. It shows the quotes from both meetings, and a person confirms the change.

This is an AI product management portfolio project. It covers the whole path from competitor research, positioning and a PRD to evaluation and a working product.

## Current status

- The product runs locally. It is not deployed, so there is no online trial link.
- **It has 0 real users so far.** The user-test results below come from 8 AI-simulated personas. They can expose bugs, but they cannot prove that anyone needs this product.
- The evaluation uses a real model, but the 135 gold labels were drafted by AI and have not been reviewed by a person.
- The differentiated positioning is still an untested assumption.
- All people and meetings in the data are fictional.

## Try it yourself

You need [uv](https://docs.astral.sh/uv/) and ffmpeg.

```bash
cd 06_product
./run_local.sh     # then open http://127.0.0.1:8000
```

Click "See the sample ledger first" on the home page. No API key is needed for this. You only need to set `ANTHROPIC_API_KEY` to process your own meetings.

To run the tests:

```bash
cd 06_product
.venv/bin/python -m pytest -q
```

## Walkthrough

### 1. Submit a meeting

Paste text, or upload a text file or recording. It handles Feishu and WeChat export formats, and meetings in English, Chinese or a mix of both. Recordings are deleted right after transcription.

![New meeting form](06_product/docs/screenshots/8_new_meeting.png)

### 2. Confirm task drafts

Each draft has a short title, owner, due date and source quote. Nothing reaches the board until a person confirms it. A field the speaker did not state stays empty instead of being guessed.

The screenshot below shows this. "We can add variant aggregation…" is only a suggestion with no clear owner, so the owner stays empty and the item is marked as unassigned.

![Task drafts](06_product/docs/screenshots/7_drafts.png)

### 3. Reconcile in the next meeting

This is the main difference from a typical meeting-notes tool. Gray shows what was said last time, green shows what was said this time, and a person decides whether the proposal is right. Proposals fall into four groups: done, unfinished or rescheduled, dropped, and not mentioned this time.

![Reconciliation page](06_product/docs/screenshots/2_reconcile.png)

Click any quote and the transcript on the right jumps to that sentence, which makes it easy to check.

![Clicking a quote highlights it in the transcript](06_product/docs/screenshots/3_quote_highlight.png)

The transcript in this screenshot also contains a planted malicious instruction. It tells the AI to mark every item as complete and transfer the GPU quota to an outside account. The product treats it as ordinary meeting content, does not act on it, and shows a notice at the top of the page.

### 4. Task board

Confirmed tasks go on a four-column board, and each card carries its quote and a link to the source meeting. You can filter by person and see how many tasks each person owes or has overdue. Tasks export to CSV, and meeting notes export to Markdown.

![Task board](06_product/docs/screenshots/4_board.png)

### 5. Mobile

The product also works in a mobile browser.

<img src="06_product/docs/screenshots/6_mobile.png" alt="Mobile view" width="320">

## Test results

### Evaluation set

The set has 5 synthetic meetings, mostly Chinese with some English, and 135 labelled items, run against a real model. The labels were drafted by AI and have not been reviewed by a person. These figures show change between versions, not absolute accuracy.

| Metric | Chinese prompt v1 | Chinese prompt v3 | English prompt (current) |
|---|---|---|---|
| Item recall | 129/135 | 130/135 | **131/135** |
| Precision | 129/170 | 130/164 | 131/183 |
| Fabricated items | 0/170 | 0/164 | **0/183** |
| Wrong owner | 1/57 | 0/58 | **0/57** |
| Wrong due date | 1/31 | 0/31 | **0/31** |
| Reconciliation type accuracy | 21/23 | 17/23 | 21/23 |

Reconciliation accuracy moves between runs and the denominator is small, so these differences are not proven improvements. The English prompt also produces more extra items, which is why its precision is lower.

### Persona testing

8 AI-simulated personas operated the earlier Chinese version in a real browser over 2 rounds, covering 42 synthetic meetings. These tests were not repeated on the English version. The product was changed between rounds based on what round 1 found. The table compares the same set of meetings.

| Metric | Round 1 | Round 2 |
|---|---|---|
| Completed the full flow | 8/8 | 8/8 |
| Drafts accepted without edits | 40/97 (41%) | **70/83 (84%)** |
| Wrong owners | 22 | **2** |
| Extra or duplicate drafts | 23 | **7** |
| Manual edits | 41 | **9** |

For meetings newly written in round 2, 29/35 drafts (83%) were accepted without edits. The round 2 personas knew about the round 1 problems, so their scoring may be lenient.

Problems found and fixed through this testing include Feishu and WeChat parsing errors, nicknames not matching the member list, "next week, maybe" being guessed as an exact date, and CSV formula injection.

## What this does not prove yet

- **Demand is unvalidated.** There are no real users yet, and the product has not been compared with pasting notes straight into a general-purpose AI chat. That comparison is the biggest risk to this positioning.
- **Competitors were not tested hands-on.** Competitor judgments come from public web pages only.
- **Time saved was not measured.** There is no baseline for doing this work by hand.
- **The production path is unverified.** The official API path has only been tested against a mock server, while evaluation and persona tests ran in a local development setup.
- **The product has known limits.** Recordings have no speaker separation, and a task cannot have several owners.

## How it works

- **Stack:** FastAPI, SQLite and vanilla JavaScript, with the Anthropic API for the model and faster-whisper for transcription.
- **Pipeline:** The model extracts tasks. Code then checks that each quote appears verbatim and that owners and dates have support in the transcript. The model reconciles the items and the code checks again. Output that fails is discarded, and a person confirms the final status.
- **Use of AI:** The research, documents and most of the code were produced with AI assistance.

See the [full test report](07_results/00_test_report.md) and [product guide](06_product/README.md).

## Repository map

| Folder | Contents |
|---|---|
| [06_product/](06_product/) | Product code, tests, evaluation runs and persona test records |
| [07_results/](07_results/) | Test report |
| [05_demo-plan/eval-kit/](05_demo-plan/eval-kit/) | Evaluation kit: synthetic meetings, gold labels and scoring scripts |
| [04_prd/](04_prd/) | PRD and user flows, written before development and different from the final product in places |
| [03_positioning/](03_positioning/) | Candidate positions, reviews, final positioning and red-team review |
| [01_market-research/](01_market-research/), [02_user-research/](02_user-research/) | Desk research on competitors and users |
| [00_pm-skills/](00_pm-skills/) | PM method notes |

Documents written before development may still say "zero code". They are kept as a record of the process.

## What stays in Chinese

All documents, the interface and the code are in English. These parts stay in Chinese on purpose:

- **Evaluation data:** The meetings and gold labels in `05_demo-plan/eval-kit/` must match verbatim, and translating them would invalidate the scores.
- **Raw test records:** `06_product/eval_runs/` and `06_product/persona_tests/r1`, `r2` are unedited evidence from those runs.
- **Original prompts:** The Chinese prompts stay so that earlier runs can be reproduced.
- **Parsing rules and test inputs:** The product still has to read Chinese meetings.
- **Source quotes:** Some research documents keep a short original quote beside its English gloss.

## Notices

- Competitor information comes from public pages at the time of writing and may have changed or be wrong. "Not seen on the page" does not mean a product lacks the feature. Any lawsuits mentioned are unresolved allegations.
- This project is not affiliated with or endorsed by any company or school mentioned.
- Quoted third-party material remains under its authors' copyright and is not covered by the MIT license.
