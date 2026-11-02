"""Persona test utilities. Usage: from kit import * (when outside the persona_tests directory, add it via sys.path)."""
import json
import urllib.request

URL = "http://localhost:8765"


def new_ledger(name, members, tag):
    """Create a ledger via the API so it can carry a batch tag; all subsequent actions go through the browser. Returns the ledger link."""
    req = urllib.request.Request(URL + "/api/ledgers", data=json.dumps({"name": name, "members": members, "tag": tag}).encode(), headers={"Content-Type": "application/json"})
    token = json.load(urllib.request.urlopen(req))["token"]
    return f"{URL}/l/{token}", token
