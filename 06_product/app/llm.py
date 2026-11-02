"""Model invocation layer. Production uses the official SDK; without a local key it can go through the Claude Code CLI; tests and the sample ledger use replay."""
import json
import os
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field

MODEL = os.environ.get("BP_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("BP_EFFORT", "high")


class LLMError(Exception):
    pass


@dataclass
class Result:
    data: dict
    provider: str
    model: str
    ms: int
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float | None = None
    stop_reason: str | None = None


class AnthropicProvider:
    name = "anthropic"

    def __init__(self):
        import anthropic
        self.anthropic = anthropic
        self.client = anthropic.Anthropic()

    def complete(self, step: str, system: str, user: str, schema: dict) -> Result:
        t = time.time()
        a = self.anthropic
        try:
            with self.client.beta.messages.stream(
                model=MODEL,
                max_tokens=64000,
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": schema}},
                system=system,
                messages=[{"role": "user", "content": user}],
            ) as stream:
                r = stream.get_final_message()
        except a.RateLimitError as e:
            raise LLMError("Too many model requests, please try again later") from e
        except a.AuthenticationError as e:
            raise LLMError("The server's model API key is invalid") from e
        except a.BadRequestError as e:
            raise LLMError(f"Model request rejected: {e.message}") from e
        except a.APIStatusError as e:
            raise LLMError(f"Model service error ({e.status_code}), please try again later") from e
        except a.APIConnectionError as e:
            raise LLMError("Could not connect to the model service, please try again later") from e
        if r.stop_reason == "refusal":
            raise LLMError("The model refused to process this content")
        if r.stop_reason == "max_tokens":
            raise LLMError("The meeting is too long and the model output was truncated")
        text = next((b.text for b in r.content if b.type == "text"), None)
        if not text:
            raise LLMError("The model returned no content")
        return Result(json.loads(text), self.name, r.model, int((time.time() - t) * 1000),
                      r.usage.input_tokens, r.usage.output_tokens, None, r.stop_reason)


def _cli_path() -> str | None:
    return os.environ.get("BP_CLAUDE_BIN") or os.environ.get("CLAUDE_CODE_EXECPATH") or shutil.which("claude")


class ClaudeCliProvider:
    """For local development and evaluation only: reuses the local Claude Code login session; not suitable for public deployment."""
    name = "claude_cli"

    def complete(self, step: str, system: str, user: str, schema: dict) -> Result:
        t = time.time()
        cmd = [_cli_path(), "-p", "--model", MODEL, "--effort", EFFORT, "--output-format", "json",
               "--json-schema", json.dumps(schema, ensure_ascii=False), "--tools", "",
               "--no-session-persistence", "--setting-sources", "", "--strict-mcp-config",
               "--system-prompt", system]
        with tempfile.TemporaryDirectory() as cwd:
            try:
                p = subprocess.run(cmd, input=user, capture_output=True, text=True, timeout=600, cwd=cwd)
            except subprocess.TimeoutExpired as e:
                raise LLMError("Model call timed out") from e
        try:
            d = json.loads(p.stdout)
        except json.JSONDecodeError as e:
            raise LLMError(f"Claude Code did not return JSON: {(p.stderr or p.stdout)[:300]}") from e
        if d.get("is_error"):
            raise LLMError(f"Claude Code reported an error: {str(d.get('result'))[:300]}")
        data = d.get("structured_output")
        if data is None:
            data = json.loads(d["result"])
        u = d.get("usage") or {}
        return Result(data, self.name, MODEL, int((time.time() - t) * 1000),
                      (u.get("input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0),
                      u.get("output_tokens") or 0, d.get("total_cost_usd"), d.get("stop_reason"))


@dataclass
class ReplayProvider:
    """Replays recorded real model output, keyed by (step, meeting code, call number). The sample ledger costs nothing."""
    recordings: dict
    name: str = "replay"
    calls: dict = field(default_factory=dict)
    meeting_code: str = ""

    def complete(self, step: str, system: str, user: str, schema: dict) -> Result:
        key = f"{step}:{self.meeting_code}"
        rec = self.recordings.get(key)
        if rec is None:
            raise LLMError(f"The sample ledger has no recorded data for {key}")
        return Result(rec, self.name, "recorded", 0)


def get_provider():
    choice = os.environ.get("BP_PROVIDER", "auto")
    if choice == "anthropic" or (choice == "auto" and os.environ.get("ANTHROPIC_API_KEY")):
        return AnthropicProvider()
    if choice in ("claude_cli", "auto") and _cli_path():
        return ClaudeCliProvider()
    return None
