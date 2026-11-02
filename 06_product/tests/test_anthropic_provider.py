"""Without a real key, use a local fake server to verify the SDK path: request shape, JSON parsing, and error mapping."""
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from app import llm, schemas

SEEN = {}


def sse(events):
    return "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events).encode()


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["content-length"])))
        SEEN.update(body=body, beta=self.headers.get("anthropic-beta"), path=self.path)
        if SEEN.get("status"):
            self.send_response(SEEN["status"]); self.send_header("content-type", "application/json"); self.end_headers()
            self.wfile.write(b'{"type":"error","error":{"type":"x","message":"nope"}}')
            return
        text = json.dumps({"proposals": []})
        stop = SEEN.get("stop", "end_turn")
        out = sse([
            {"type": "message_start", "message": {"id": "m", "type": "message", "role": "assistant", "model": "claude-opus-5-5", "content": [], "stop_reason": None, "stop_sequence": None, "usage": {"input_tokens": 5, "output_tokens": 0}}},
            {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}},
            {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": text}},
            {"type": "content_block_stop", "index": 0},
            {"type": "message_delta", "delta": {"stop_reason": stop, "stop_sequence": None}, "usage": {"output_tokens": 7}},
            {"type": "message_stop"},
        ])
        self.send_response(200); self.send_header("content-type", "text/event-stream"); self.end_headers(); self.wfile.write(out)


@pytest.fixture()
def prov(monkeypatch):
    srv = HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    monkeypatch.setenv("ANTHROPIC_BASE_URL", f"http://127.0.0.1:{srv.server_port}")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    SEEN.clear()
    p = llm.AnthropicProvider()
    p.client = p.client.with_options(max_retries=0)
    yield p
    srv.shutdown()


def test_request_and_parse(prov):
    r = prov.complete("reconcile", "sys", "user", schemas.RECONCILE)
    assert r.data == {"proposals": []} and r.input_tokens == 5 and r.output_tokens == 7
    b = SEEN["body"]
    assert b["model"] == "claude-opus-5-5" and b["fallbacks"] == "default" and b["stream"] is True
    assert b["output_config"]["format"]["type"] == "json_schema" and b["output_config"]["effort"] == "high"
    assert "server-side-fallback-2026-07-01" in SEEN["beta"]


@pytest.mark.parametrize("stop,msg", [("refusal", "refused"), ("max_tokens", "truncated")])
def test_stop_reasons(prov, stop, msg):
    SEEN["stop"] = stop
    with pytest.raises(llm.LLMError, match=msg):
        prov.complete("x", "s", "u", schemas.RECONCILE)


@pytest.mark.parametrize("status,msg", [(401, "key"), (429, "Too many"), (500, "later")])
def test_errors(prov, status, msg):
    SEEN["status"] = status
    with pytest.raises(llm.LLMError, match=msg):
        prov.complete("x", "s", "u", schemas.RECONCILE)
