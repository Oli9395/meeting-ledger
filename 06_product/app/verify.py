"""Deterministic checks (V1–V12 from §4.5 of the demo plan). The model's word doesn't count; only what passes these code checks does."""
import re
import unicodedata

FIRST_PERSON = re.compile(r"我|咱来|(?<![A-Za-z])(I|I'll|I'm|I've|Ill|Im)(?![A-Za-z])")
CJK = re.compile(r"[一-鿿]")
WORD = re.compile(r"[A-Za-z0-9_'-]+")
VAGUE_OWNER = {"我们", "大家", "有人", "someone", "somebody", "we", "everyone", "anyone", "谁", "团队", "组里", "team"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s or "")).strip()


def is_substring(quote: str, source: str) -> bool:
    q = norm(quote)
    return bool(q) and q in norm(source)


def long_enough(quote: str) -> bool:
    q = norm(quote)
    if CJK.search(q):
        return len(CJK.findall(q)) + len(WORD.findall(q)) >= 4
    return len(WORD.findall(q)) >= 3


def check_quote(quote: str, uid: str, utts: dict[str, dict], banned: set[str]) -> str | None:
    """V1/V2/V3/V6. Returns the rejection reason, or None if the quote passes."""
    if uid not in utts:
        return f"Utterance {uid} does not exist or does not belong to this meeting"
    if uid in banned:
        return f"Utterance {uid} looks like an instruction aimed at the AI and cannot be used as evidence"
    if not long_enough(quote):
        return f"Quote is too short: {quote!r}"
    if not is_substring(quote, utts[uid]["text"]):
        return f"Quote not found in {uid}; copy it verbatim from that utterance"
    return None


def aliases_for(name: str, members: list[str] | None = None) -> list[str]:
    n = norm(name)
    out = {n}
    if re.fullmatch(r"[一-鿿]{2,4}", n):
        out.add(n[1:] if len(n) > 2 else n)
        for ch in {n[0], n[-1]}:  # Chinese nicknames such as 小王, 老王, 阿珍, 芳姐
            out |= {"小" + ch, "老" + ch, "阿" + ch, ch + "姐", ch + "哥", ch + "老师", ch + "博"}
    for part in n.split():
        if len(part) >= 2:
            out.add(part)
    return list(out)


def canonical_owner(value: str | None, members: list[str]) -> str | None:
    if not value:
        return None
    v = norm(value)
    hits = [m for m in members if v == norm(m)] or [m for m in members if v.lower() in [a.lower() for a in aliases_for(m)]]
    return hits[0] if len(hits) == 1 else v  # If a nickname matches several people, don't guess; keep the original word


SECOND_PERSON = re.compile(r"你|您|(?<![A-Za-z])(you|your|please)(?![A-Za-z])|麻烦|帮忙|帮我|请", re.I)
NOT_SELF = re.compile(r"你|您|大家|有人|谁|(?<![A-Za-z])(you|someone|everyone|we)(?![A-Za-z])", re.I)


def check_owner(owner: dict, quote: str, speaker: str | None, members: list[str], window: list[dict] | None = None) -> dict:
    """V4: an owner must have supporting evidence, otherwise it is downgraded. window holds the utterances around this one; speakers is used to work out who is being addressed."""
    state, value, basis = owner.get("state"), owner.get("value"), owner.get("basis")
    if state == "given":
        v = norm(value or "")
        if not v or v.lower() in VAGUE_OWNER:
            return {"state": "vague" if v else "absent", "value": v or None, "basis": "none"}
        if basis == "speaker_first_person":
            # Chinese often drops the subject ("周五前跑完", "finish running it by Friday"), so as long as no word points to someone else, it counts as the speaker
            q = norm(quote)
            if speaker and (FIRST_PERSON.search(q) or not NOT_SELF.search(q)):
                return {"state": "given", "value": canonical_owner(speaker, members), "basis": basis}
            return {"state": "absent", "value": None, "basis": "none"}
        if basis == "addressed":
            canon = canonical_owner(v, members)
            if window and canon and norm(canon) != norm(speaker or ""):
                names = [n.lower() for n in aliases_for(canon) + [v]]
                speakers = {norm(u["speaker"]) for u in window if u.get("speaker")}
                # With only two speakers, "you" is the other person; otherwise this person must have spoken or been named in the surrounding utterances
                in_window = any(n in norm(u["text"]).lower() or n in norm(u.get("speaker") or "").lower() for u in window for n in names)
                if in_window or (len(speakers) == 2 and norm(canon) in speakers):
                    return {"state": "given", "value": canon, "basis": basis}
            return {"state": "absent", "value": None, "basis": "none"}
        if basis == "named_in_quote":
            names = aliases_for(v) + [v]
            canon = canonical_owner(v, members)
            if canon:
                names += aliases_for(canon)
            if any(n.lower() in norm(quote).lower() for n in names if n):
                return {"state": "given", "value": canon, "basis": basis}
        return {"state": "absent", "value": None, "basis": "none"}
    if state == "vague":
        return {"state": "vague", "value": norm(value or "") or None, "basis": "none"}
    return {"state": "absent", "value": None, "basis": "none"}


def check_due_raw(due_raw: str | None, *sources: str) -> str | None:
    """V5: the raw date wording must actually appear in the quote; otherwise treat it as absent."""
    if due_raw and any(is_substring(due_raw, s) for s in sources):
        return norm(due_raw)
    return None


def bigrams(s: str) -> set[str]:
    t = re.sub(r"[\W_]+", "", norm(s).lower())
    return {t[i:i + 2] for i in range(len(t) - 1)}


def similarity(a: str, b: str) -> float:
    x, y = bigrams(a), bigrams(b)
    if not x or not y:
        return 0.0
    return len(x & y) / len(x)


POSSIBLE_MENTION = 0.5


def possible_mention(quote: str, utts: list[dict]) -> dict | None:
    """V9: don't silently count a possible mention as not mentioned."""
    best, top = None, 0.0
    for u in utts:
        sc = similarity(quote, u["text"])
        if sc > top:
            best, top = u, sc
    if best and top >= POSSIBLE_MENTION:
        return {"utterance_id": best["id"], "score": round(top, 2), "text": best["text"]}
    return None


def batch_suspicious(props: list[dict]) -> bool:
    """V10: if a single utterance supports more than half of the transitions, hold the whole batch for human review."""
    if len(props) < 3:
        return False
    counts: dict[str, int] = {}
    for p in props:
        for q in {norm(e["quote"]) for e in p["closure_evidence"]}:  # A recorded transcript segment can be very long, so count by the quoted sentence, not the whole segment
            counts[q] = counts.get(q, 0) + 1
    return max(counts.values(), default=0) >= 3 and max(counts.values()) > len(props) * 0.5
