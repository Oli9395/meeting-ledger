"""S1: Split meeting text into utterance units. Utterance units are the single source of truth for verbatim verification and are immutable once stored."""
import re
from dataclasses import dataclass

TS = r"\[?(\d{1,2}:\d{2}(?::\d{2})?)\]?"
LINE_TS_SPK = re.compile(rf"^{TS}\s*([^：:\[\]]{{1,24}}?)\s*[：:]\s*(.+)$")
LINE_TS = re.compile(rf"^{TS}\s*(.+)$")
LINE_SPK_TS = re.compile(rf"^([^\s：:\[\]][^：:\[\]]{{0,30}}?)\s+{TS}\s*(?:[：:]\s*)?(.*)$")
LINE_SPK = re.compile(r"^([^：:，。,.!?！？\s][^：:，。,.!?！？]{0,23}?)\s*[：:]\s*(.+)$")
HEADER = re.compile(r"^(会议|日期|时间|地点|参会人|与会人|主持人|记录人|Meeting|Date|Attendees)\s*[：:]")
NOT_SPEAKER = {"注意", "备注", "结论", "决定", "todo", "TODO", "问题", "note", "Note", "http", "https"}


@dataclass
class Utterance:
    seq: int
    ts: str | None
    speaker: str | None
    text: str


def parse_text(raw: str) -> list[Utterance]:
    out: list[Utterance] = []
    pending: tuple[str, str] | None = None  # Common in Feishu and WeChat: first line is "speaker time", content is on the second line
    for line in raw.replace("\r\n", "\n").split("\n"):
        line = line.strip()
        if not line or HEADER.match(line) or line.startswith("#"):
            continue
        line = re.sub(r"^[-*•]\s+", "", line)
        ts, spk, text = None, None, line
        m = LINE_TS_SPK.match(line)
        h = LINE_SPK_TS.match(line)
        if h and not LINE_TS.match(line):
            if h.group(3).strip():
                out.append(Utterance(len(out) + 1, h.group(2), h.group(1).strip(), h.group(3).strip()))
            else:
                pending = (h.group(1).strip(), h.group(2))
            continue
        if pending and not m:
            spk, ts = pending
            pending = None
            out.append(Utterance(len(out) + 1, ts, spk, line))
            continue
        pending = None
        if m:
            ts, spk, text = m.group(1), m.group(2).strip(), m.group(3).strip()
        else:
            m = LINE_TS.match(line)
            if m:
                ts, text = m.group(1), m.group(2).strip()
            else:
                m = LINE_SPK.match(line)
                if m and m.group(1).strip() not in NOT_SPEAKER:
                    spk, text = m.group(1).strip(), m.group(2).strip()
        out.append(Utterance(len(out) + 1, ts, spk, text))
    return out


def fmt_ts(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"
