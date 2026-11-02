# Meeting Ledger (BriefPilot v2)

Turn a meeting recording or transcript into confirmed, assignable tasks, then reconcile them against what people say in the next meeting.

**License:** [MIT](LICENSE) | **See it working:** [DEMO.md](DEMO.md)

![Reconciliation page](06_product/docs/screenshots/2_reconcile.png)

This is an AI product management portfolio project. It covers the whole path from competitor research, positioning and a PRD to evaluation and a working product.

## Current status

- The product runs locally and is not deployed.
- **It has 0 real users.**
- Evaluation runs use a real model, but the 135 gold labels were drafted by AI and have not been reviewed by a person.
- User tests were run by 8 AI-simulated personas on an earlier Chinese version. They can expose bugs, but they cannot prove demand.
- The differentiated positioning is still an untested assumption.
- The research, documents and most of the code were produced with AI assistance. All people and meetings in the data are fictional.

## Results

| Metric | Result | Conditions |
|---|---|---|
| Item recall | 131/135 (97%) | English prompts, 5 synthetic meetings, unreviewed gold labels |
| Precision | 131/183 (72%) | Same run, with unreviewed extra items counted as wrong |
| Fabricated items | 0/183 | Same run |
| Wrong owner | 0/57 | Same run |
| Reconciliation type accuracy | 21/23 | Same run, and earlier runs ranged from 17/23 to 21/23 |
| Drafts accepted without edits | 41% to 84% | 8 AI personas over 2 rounds, Chinese version |

See the [full test report](07_results/00_test_report.md).

## Run it

You need [uv](https://docs.astral.sh/uv/) and ffmpeg.

```bash
cd 06_product
./run_local.sh      # then open http://127.0.0.1:8000
```

The sample ledger works without a model. To process your own meetings, set `ANTHROPIC_API_KEY`. The official API path has only been tested against a mock server, so run one meeting yourself after deploying.

```bash
cd 06_product
.venv/bin/python -m pytest -q
```

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
