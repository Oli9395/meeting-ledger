"""Date anchoring is done only by code; the model only copies the original wording. Anything outside the rule table is vague; never guess."""
import re
from datetime import date, timedelta

WD = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
EN = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6,
      "mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}
VAGUE = ("过段时间", "尽快", "回头", "之后", "以后", "月初", "月底", "月中", "这段时间", "最近", "有空", "上旬", "下旬", "中旬", "asap", "soon",
         "later", "maintenance")


def _monday(d: date) -> date:
    return d - timedelta(days=d.weekday())


CN = {"一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}


def _cn_num(m: re.Match) -> str:
    x = m.group(0)
    if x == "十":
        return "10"
    if "十" in x:
        a, b = x.split("十")
        return str(CN.get(a, 1) * 10 + CN.get(b, 0))
    return str(CN.get(x, x))


def _month_end(y: int, mon: int) -> date:
    return (date(y + (mon == 12), mon % 12 + 1, 1)) - timedelta(days=1)


def anchor(raw: str | None, meeting: date) -> tuple[str, str | None]:
    """Return (state, iso). state: given (can be converted) / vague (has original wording but is not converted) / absent."""
    if not raw or not raw.strip():
        return "absent", None
    s = raw.strip().lower()
    # 十一月六号, 十月二十号 → 11月6号 (only converts month-day notation; leaves "周二" untouched)
    s = re.sub(r"[一二两三四五六七八九十]+(?=\s*月)", _cn_num, s)
    s = re.sub(r"(?<=月)\s*[一二两三四五六七八九十]+(?=\s*[日号])", _cn_num, s)
    if "下个月底" in s or "下月底" in s:
        n = date(meeting.year + (meeting.month == 12), meeting.month % 12 + 1, 1)
        return "given", _month_end(n.year, n.month).isoformat()
    if "月底" in s and not re.search(r"\d+\s*月底", s):
        return "given", _month_end(meeting.year, meeting.month).isoformat()
    if any(v in s for v in VAGUE):
        return "vague", None
    if any(k in s for k in ("下次组会", "下周组会", "下次开会", "下次会", "next meeting", "next group meeting", "next week's meeting", "next week's group meeting")):
        return "given", (meeting + timedelta(days=7)).isoformat()
    m = re.search(r"(20\d{2})[-/.年](\d{1,2})[-/.月](\d{1,2})", s)
    if m:
        return _safe(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.search(r"(\d{1,2})\s*月\s*(\d{1,2})\s*[日号]?", s) or re.search(r"(?<![\d.])(\d{1,2})[/.](\d{1,2})(?![\d.%])", s)
    if m:
        mon, day = int(m.group(1)), int(m.group(2))
        year = meeting.year + 1 if mon < meeting.month - 6 else meeting.year
        return _safe(year, mon, day)
    m = re.search(r"(?<![\d月])(\d{1,2})\s*[号日]", s)  # Only "15号" was said: take the nearest 15th after the meeting
    if m:
        day = int(m.group(1))
        y, mon = meeting.year, meeting.month
        for _ in range(2):
            st, iso = _safe(y, mon, day)
            if iso and iso >= meeting.isoformat():
                return st, iso
            y, mon = (y + 1, 1) if mon == 12 else (y, mon + 1)
        return "vague", None
    if "大后天" in s:
        return "given", (meeting + timedelta(days=3)).isoformat()
    if "后天" in s:
        return "given", (meeting + timedelta(days=2)).isoformat()
    if "明天" in s or "明早" in s or "明晚" in s or "tomorrow" in s:
        return "given", (meeting + timedelta(days=1)).isoformat()
    if "今天" in s or "今晚" in s or "会后" in s or "today" in s or "tonight" in s or "after the meeting" in s or "after this meeting" in s:
        return "given", meeting.isoformat()
    m = re.search(r"(下下|下|这|本)?\s*(?:个)?(?:周|星期|礼拜)([一二三四五六日天])", s)
    if m:
        wd = WD[m.group(2)]
        pre = m.group(1)
        if pre == "下下":
            return "given", (_monday(meeting) + timedelta(days=14 + wd)).isoformat()
        if pre == "下":
            return "given", (_monday(meeting) + timedelta(days=7 + wd)).isoformat()
        if pre in ("这", "本"):
            return "given", (_monday(meeting) + timedelta(days=wd)).isoformat()
        d = _monday(meeting) + timedelta(days=wd)
        return "given", (d if d >= meeting else d + timedelta(days=7)).isoformat()
    m = re.search(r"(next\s+)?\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun)\b", s)
    if m:
        wd = EN[m.group(2)]
        if m.group(1):
            return "given", (_monday(meeting) + timedelta(days=7 + wd)).isoformat()
        d = _monday(meeting) + timedelta(days=wd)
        return "given", (d if d >= meeting else d + timedelta(days=7)).isoformat()
    if "下周末" in s or "next weekend" in s:
        return "given", (_monday(meeting) + timedelta(days=13)).isoformat()
    if "周末前" in s:
        return "given", (_monday(meeting) + timedelta(days=4)).isoformat()
    if "周末" in s or "weekend" in s:
        return "given", (_monday(meeting) + timedelta(days=6)).isoformat()
    if "这周" in s or "本周" in s or "this week" in s:  # Work context: "this week" is treated as this Friday
        return "given", (_monday(meeting) + timedelta(days=4)).isoformat()
    return "vague", None


def _safe(y: int, m: int, d: int) -> tuple[str, str | None]:
    try:
        return "given", date(y, m, d).isoformat()
    except ValueError:
        return "vague", None
