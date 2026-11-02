"""All product metrics are computed from the database, never entered by hand. Can be filtered by tag to report different batches of usage separately."""
import json
from statistics import median

from . import db


def pct(a, b):
    return round(100 * a / b, 1) if b else None


def compute(tag: str | None = None) -> dict:
    with db.tx() as c:
        where, args = ("WHERE l.tag=?", (tag,)) if tag else ("", ())
        ledgers = [dict(r) for r in c.execute(f"SELECT l.* FROM ledgers l {where}", args)]
        ids = [l["id"] for l in ledgers if not l["is_sample"]]
        if not ids:
            return {"tag": tag, "ledgers": 0}
        q = ",".join("?" * len(ids))
        meetings = [dict(r) for r in c.execute(f"SELECT * FROM meetings WHERE ledger_id IN ({q})", ids)]
        items = [dict(r) for r in c.execute(f"SELECT * FROM items WHERE ledger_id IN ({q}) AND manual=0", ids)]
        props = [dict(r) for r in c.execute(f"SELECT * FROM proposals WHERE ledger_id IN ({q})", ids)]
        fb = [dict(r) for r in c.execute(f"SELECT * FROM feedback WHERE ledger_id IN ({q})", ids)]
        sv = [dict(r) for r in c.execute(f"SELECT * FROM surveys WHERE ledger_id IN ({q})", ids)]
        ev = [dict(r) for r in c.execute(f"SELECT * FROM events WHERE ledger_id IN ({q})", ids)]
        calls = [dict(r) for r in c.execute(f"SELECT * FROM llm_calls WHERE ledger_id IN ({q})", ids)]
    ready = [m for m in meetings if m["status"] == "ready"]
    drafts = [i for i in items if i["kind"] == "commitment" and i["review"] != "merged"]  # Items merged by the system don't count as human decisions
    decided = [i for i in drafts if i["review"] != "pending"]
    conf = [i for i in decided if i["review"] == "confirmed"]
    noedit = [i for i in conf if not i["edited"]]
    given_owner = [i for i in drafts if i["ai_owner"]]
    owner_changed = [i for i in conf if i["ai_owner"] and i["owner_value"] != i["ai_owner"]]
    due_changed = [i for i in conf if i["ai_due_date"] and i["due_date"] != i["ai_due_date"]]
    mp = [p for p in props if p["proposed_by"] == "model"]
    mp_dec = [p for p in mp if p["decision"] in ("confirmed", "dismissed")]
    up = [f for f in fb if f["rating"] == "up"]
    down = [f for f in fb if f["rating"] == "down"]
    se = [s for s in sv if s["sean_ellis"]]
    very = [s for s in se if s["sean_ellis"] == "very"]
    rej = sum(len(json.loads(m["rejected_json"])) for m in ready)
    exported = {e["ledger_id"] for e in ev if e["name"] == "exported"}
    reconciled = {p["ledger_id"] for p in props if p["decision"] == "confirmed"}
    return {
        "tag": tag, "ledgers": len(ids),
        "meetings": {"total": len(meetings), "ready": len(ready), "failed": sum(m["status"] == "failed" for m in meetings),
                     "from_audio": sum(m["source"] == "audio" for m in meetings)},
        "pipeline_seconds_median": round(median([m["ms_total"] for m in ready if m["ms_total"]]) / 1000, 1) if ready else None,
        "transcribe_seconds_median": round(median([m["ms_transcribe"] for m in ready if m["ms_transcribe"]] or [0]) / 1000, 1),
        "drafts": {"total": len(drafts), "decided": len(decided), "confirmed": len(conf), "rejected": len(decided) - len(conf),
                   "accepted_without_edit": len(noedit), "accepted_without_edit_pct_of_decided": pct(len(noedit), len(decided)),
                   "ai_owner_given": len(given_owner), "owner_changed_by_user": len(owner_changed), "due_changed_by_user": len(due_changed)},
        "reconcile": {"model_proposals": len(mp), "decided": len(mp_dec), "confirmed": sum(p["decision"] == "confirmed" for p in mp_dec),
                      "confirmed_pct": pct(sum(p["decision"] == "confirmed" for p in mp_dec), len(mp_dec)),
                      "not_mentioned": sum(p["transition"] == "not_mentioned" for p in props)},
        "verifier_rejected": rej,
        "activation": {"ledgers_with_confirmed_reconcile": len(reconciled), "ledgers_exported": len(exported)},
        "feedback": {"up": len(up), "down": len(down), "up_pct": pct(len(up), len(up) + len(down))},
        "sean_ellis": {"answers": len(se), "very_disappointed": len(very), "very_pct": pct(len(very), len(se))},
        "llm": {"calls": len(calls), "failed": sum(not x["ok"] for x in calls), "cost_usd": round(sum(x["cost_usd"] or 0 for x in calls), 3)},
    }
