import os
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS ledgers(id INTEGER PRIMARY KEY, token TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
  members_json TEXT NOT NULL DEFAULT '[]', terms_json TEXT NOT NULL DEFAULT '[]', is_sample INTEGER NOT NULL DEFAULT 0, tag TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS meetings(id INTEGER PRIMARY KEY, ledger_id INTEGER NOT NULL REFERENCES ledgers(id) ON DELETE CASCADE,
  seq INTEGER NOT NULL, code TEXT NOT NULL, date TEXT NOT NULL, title TEXT, kind TEXT NOT NULL DEFAULT 'group',
  source TEXT NOT NULL, status TEXT NOT NULL, stage TEXT, error TEXT, created_at TEXT NOT NULL, finished_at TEXT,
  ms_transcribe INTEGER, ms_extract INTEGER, ms_reconcile INTEGER, ms_total INTEGER, retries INTEGER NOT NULL DEFAULT 0,
  rejected_json TEXT NOT NULL DEFAULT '[]', injections_json TEXT NOT NULL DEFAULT '[]', suspicious INTEGER NOT NULL DEFAULT 0,
  audio_seconds REAL, UNIQUE(ledger_id, code));
CREATE TABLE IF NOT EXISTS utterances(id TEXT NOT NULL, ledger_id INTEGER NOT NULL REFERENCES ledgers(id) ON DELETE CASCADE,
  meeting_id INTEGER NOT NULL REFERENCES meetings(id) ON DELETE CASCADE, seq INTEGER NOT NULL, ts TEXT, speaker TEXT, text TEXT NOT NULL,
  PRIMARY KEY(ledger_id, id));
CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, ledger_id INTEGER NOT NULL REFERENCES ledgers(id) ON DELETE CASCADE,
  meeting_id INTEGER REFERENCES meetings(id) ON DELETE CASCADE, code TEXT NOT NULL, kind TEXT NOT NULL, strength TEXT, quote TEXT,
  utterance_id TEXT, title TEXT, owner_state TEXT NOT NULL DEFAULT 'absent', owner_value TEXT, owner_basis TEXT, due_state TEXT NOT NULL DEFAULT 'absent',
  due_raw TEXT, due_date TEXT, ai_owner TEXT, ai_due_date TEXT, slots_json TEXT NOT NULL DEFAULT '[]',
  review TEXT NOT NULL DEFAULT 'pending', task_status TEXT NOT NULL DEFAULT 'todo', edited INTEGER NOT NULL DEFAULT 0,
  manual INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL, decided_at TEXT, updated_at TEXT);
CREATE TABLE IF NOT EXISTS proposals(id INTEGER PRIMARY KEY, ledger_id INTEGER NOT NULL REFERENCES ledgers(id) ON DELETE CASCADE,
  item_id INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE, meeting_id INTEGER NOT NULL REFERENCES meetings(id) ON DELETE CASCADE,
  transition TEXT NOT NULL, evidence_json TEXT NOT NULL DEFAULT '[]', new_due_raw TEXT, new_due_date TEXT, note TEXT,
  flags_json TEXT NOT NULL DEFAULT '[]', decision TEXT NOT NULL DEFAULT 'pending', proposed_by TEXT NOT NULL, decided_at TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY, ledger_id INTEGER REFERENCES ledgers(id) ON DELETE CASCADE, target_type TEXT, target_id TEXT,
  rating TEXT, reason TEXT, comment TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS surveys(id INTEGER PRIMARY KEY, ledger_id INTEGER REFERENCES ledgers(id) ON DELETE CASCADE, sean_ellis TEXT, value_text TEXT, missing TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, ledger_id INTEGER REFERENCES ledgers(id) ON DELETE CASCADE, name TEXT NOT NULL, props_json TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS llm_calls(id INTEGER PRIMARY KEY, ledger_id INTEGER REFERENCES ledgers(id) ON DELETE CASCADE, meeting_id INTEGER, step TEXT, attempt INTEGER, provider TEXT, model TEXT,
  prompt_version TEXT, input_tokens INTEGER, output_tokens INTEGER, cost_usd REAL, ms INTEGER, ok INTEGER, error TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS audit_log(id INTEGER PRIMARY KEY, ledger_id INTEGER REFERENCES ledgers(id) ON DELETE CASCADE, action TEXT, target TEXT, before_json TEXT, after_json TEXT, created_at TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS i_items ON items(ledger_id, meeting_id);
CREATE INDEX IF NOT EXISTS i_props ON proposals(ledger_id, meeting_id);
"""
_lock = threading.Lock()


def path() -> str:
    return os.environ.get("BP_DB", os.path.join(os.path.dirname(__file__), "..", "data", "app.db"))


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect() -> sqlite3.Connection:
    c = sqlite3.connect(path(), timeout=30)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    c.execute("PRAGMA journal_mode=WAL")
    return c


@contextmanager
def tx():
    c = connect()
    try:
        yield c
        c.commit()
    except Exception:
        c.rollback()
        raise
    finally:
        c.close()


def init():
    os.makedirs(os.path.dirname(os.path.abspath(path())), exist_ok=True)
    with tx() as c:
        c.executescript(SCHEMA)
        cols = [r[1] for r in c.execute("PRAGMA table_info(ledgers)")]
        if "terms_json" not in cols:
            c.execute("ALTER TABLE ledgers ADD COLUMN terms_json TEXT NOT NULL DEFAULT '[]'")


def event(c, ledger_id, name, props="{}"):
    c.execute("INSERT INTO events(ledger_id,name,props_json,created_at) VALUES(?,?,?,?)", (ledger_id, name, props, now()))
