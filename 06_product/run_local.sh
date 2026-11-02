#!/bin/zsh
# Local startup. Uses the official API if ANTHROPIC_API_KEY is set; otherwise uses the local Claude Code.
cd "$(dirname "$0")"
[ -d .venv ] || { uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -e '.[asr,dev]'; }
export BP_ADMIN_KEY="${BP_ADMIN_KEY:-localadmin}"
exec .venv/bin/uvicorn app.main:app --host "${HOST:-127.0.0.1}" --port "${PORT:-8000}"
