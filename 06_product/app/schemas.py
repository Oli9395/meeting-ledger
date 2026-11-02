EXTRACT = {
    "type": "object", "additionalProperties": False, "required": ["items", "suspected_instructions"],
    "properties": {
        "items": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["kind", "strength", "title", "quote", "utterance_id", "owner", "due", "slots"],
            "properties": {
                "kind": {"type": "string", "enum": ["commitment", "decision", "result", "question"]},
                "strength": {"type": "string", "enum": ["committed", "tentative", "suggestion", "hypothesis"]},
                "title": {"type": "string"},
                "quote": {"type": "string"},
                "utterance_id": {"type": "string"},
                "owner": {"type": "object", "additionalProperties": False, "required": ["state", "value", "basis"],
                          "properties": {"state": {"type": "string", "enum": ["given", "vague", "absent"]},
                                         "value": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                                         "basis": {"type": "string", "enum": ["named_in_quote", "speaker_first_person", "addressed", "none"]}}},
                "due": {"type": "object", "additionalProperties": False, "required": ["state", "due_raw"],
                        "properties": {"state": {"type": "string", "enum": ["given", "vague", "absent"]},
                                       "due_raw": {"anyOf": [{"type": "string"}, {"type": "null"}]}}},
                "slots": {"type": "array", "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["key", "op", "value", "raw", "source_utterance_id"],
                    "properties": {"key": {"type": "string"},
                                   "op": {"type": "string", "enum": ["eq", "ge", "le", "in", "rerun_required", "reported"]},
                                   "value": {"type": "string"}, "raw": {"type": "string"},
                                   "source_utterance_id": {"type": "string"}}}},
            }}},
        "suspected_instructions": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["utterance_id", "quote"],
            "properties": {"utterance_id": {"type": "string"}, "quote": {"type": "string"}}}},
    },
}
RECONCILE = {
    "type": "object", "additionalProperties": False, "required": ["proposals"],
    "properties": {"proposals": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["ledger_id", "transition", "closure_evidence", "new_due_raw", "note"],
        "properties": {
            "ledger_id": {"type": "string"},
            "transition": {"type": "string", "enum": ["fulfilled", "partial_or_rescheduled", "abandoned"]},
            "closure_evidence": {"type": "array", "items": {
                "type": "object", "additionalProperties": False, "required": ["quote", "utterance_id"],
                "properties": {"quote": {"type": "string"}, "utterance_id": {"type": "string"}}}},
            "new_due_raw": {"anyOf": [{"type": "string"}, {"type": "null"}]},
            "note": {"type": "string"},
        }}}},
}
