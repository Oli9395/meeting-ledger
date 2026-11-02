# Meeting Ledger (BriefPilot v2)

Upload a meeting recording or paste text, and get draft action items with owners, due dates, and verbatim quotes. Items only reach the task board after a person confirms them. When the next meeting says things like "it's half done" or "let's hold off on that", the ledger automatically matches them back to the earlier action item, and a person confirms before the status is updated.

## Implemented Features

| Feature | Description |
|---|---|
| Input | Paste text; upload txt or md files; upload audio (transcribed locally with faster-whisper, and the audio is deleted immediately after transcription) |
| Text formats | `[time] Name: content`, `Name: content`, `Name time` followed by content on a new line (Feishu, WeChat), plain text |
| Draft action items | Short title, owner, due date, intensity, verbatim quote; click the quote to jump to its place in the transcript |
| Assigning tasks | Assign an owner (nicknames are automatically normalized to the member list), change the date, confirm or reject; unconfirmed items do not reach the task board |
| Task board | Four-column kanban, filter by person, per-person summary of how many items are owed and how many are overdue, add tasks manually |
| Cross-meeting reconciliation | Fulfilled, not finished or rescheduled, dropped, not mentioned this time; verdicts can be overridden or undone; items not mentioned for several consecutive meetings are flagged red |
| Minutes | Decisions, outcomes, open questions; Markdown export; task CSV export; post-meeting follow-up message |
| Feedback | 👍/👎 on each item with a reason; a "Give feedback" questionnaire; metrics on the `/admin` endpoint are computed from the database |
| Reliability | Verbatim quote verification, owners and dates must be backed by evidence, injected text is not executed, XSS and CSV formula injection protection, one-click complete deletion |

## Prompts

The live prompts are `extract_v3_en` and `reconcile_v2_en`. The prompt files without the `_en` suffix are the original Chinese versions. They stay in the repository so that the earlier runs in `eval_runs/` can be reproduced.

To re-record the sample ledger after changing a prompt, run `scripts/record_sample.py`.

## Running Locally

```bash
./run_local.sh     # Installs dependencies automatically on first run, then opens http://127.0.0.1:8000
```

Choose one of two model sources: set `ANTHROPIC_API_KEY`, or have Claude Code already logged in on your machine (suitable only for development and evaluation; do not use it to serve external users). The first audio transcription run downloads the whisper small model and requires ffmpeg.

To view metrics:

```bash
curl 'http://127.0.0.1:8000/api/admin/metrics?key=localadmin'
```

## Deploying for Others

You need your own Anthropic API key and a hosting account. The `Dockerfile` and `render.yaml` are ready; the database lives on the mounted disk `/data`, and `ANTHROPIC_API_KEY` and `BP_ADMIN_KEY` must be set. Share the link with classmates only after deployment.

The official API path has so far only been tested against a local fake server for request shape, parsing, and error handling; it has not been run with a real key. After deploying, run a meeting through it yourself first.

## Testing

```bash
.venv/bin/python -m pytest -q                       # 22 unit and API tests
BP_PROVIDER=claude_cli .venv/bin/python scripts/run_eval.py --name v4 --extract-prompt extract_v3_en --reconcile-prompt reconcile_v2_en
.venv/bin/python scripts/rescore_recon.py v4
.venv/bin/python scripts/persona_report.py          # Summarizes persona tests; requires data/persona.db
```

## Known Limitations

- Audio has no speaker diarization, so first-person action items must be assigned manually. The glossary helps only a little with transcription errors.
- Reconciliation may judge a completed item as "not finished", and may also miss implied completions, so it relies on human confirmation and overrides.
- Whole-team items ("everyone submit the weekly report by Friday") do not always generate a task. "Xiao Chen and the third-year PhD student together" keeps only one owner.
- The interface is in English, and the parser and date rules handle English, Chinese and mixed meetings. There is no Linear or Feishu push integration, and no account system; the link is the password.
- The "decision × experiment run configuration" check and the stale-number check have not been built yet.
