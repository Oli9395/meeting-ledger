from datetime import date

from app import verify
from app.dates import anchor
from app.parse import parse_text

M = date(2026, 10, 15)  # Thursday


def test_parse_formats():
    u = parse_text("会议：x\n[00:00:03] 周岚：开始吧\n王博: 跑了一半\n[00:01] 没有说话人的一句话，比较长\n纯文本一句")
    assert [(x.ts, x.speaker, x.text) for x in u] == [("00:00:03", "周岚", "开始吧"), (None, "王博", "跑了一半"), ("00:01", None, "没有说话人的一句话，比较长"), (None, None, "纯文本一句")]


def test_dates():
    assert anchor("周日前", M) == ("given", "2026-10-18")
    assert anchor("明天", M) == ("given", "2026-10-16")
    assert anchor("tonight", M) == ("given", "2026-10-15")
    assert anchor("下周一之前", M) == ("given", "2026-10-19")
    assert anchor("by Friday", M) == ("given", "2026-10-16")
    assert anchor("这周末", M) == ("given", "2026-10-18")
    assert anchor("周末前", M) == ("given", "2026-10-16")
    assert anchor("11 月 14 号之前", M) == ("given", "2026-11-14")
    assert anchor("下周组会前", M) == ("given", "2026-10-22")
    assert anchor("过段时间", M) == ("vague", None)
    assert anchor("11 月初", M) == ("vague", None)
    assert anchor("after the maintenance window", M) == ("vague", None)
    assert anchor(None, M) == ("absent", None)


UT = {"U1": {"text": "我周五前把 baseline 跑完", "speaker": "王博"}, "U2": {"text": "maybe someone should clean up", "speaker": None}}


def test_quote_verbatim():
    assert verify.check_quote("把 baseline 跑完", "U1", UT, set()) is None
    assert "not found" in verify.check_quote("把 baseline 跑好", "U1", UT, set())
    assert "does not exist" in verify.check_quote("把 baseline 跑完", "U9", UT, set())
    assert "too short" in verify.check_quote("跑完", "U1", UT, set())
    assert "instruction" in verify.check_quote("把 baseline 跑完", "U1", UT, {"U1"})


def test_owner_needs_basis():
    q = "我周五前把 baseline 跑完"
    assert verify.check_owner({"state": "given", "value": "王博", "basis": "speaker_first_person"}, q, "王博", [])["state"] == "given"
    # First person with an unknown speaker doesn't count
    assert verify.check_owner({"state": "given", "value": "王博", "basis": "speaker_first_person"}, q, None, [])["state"] == "absent"
    # A name that isn't in the quote doesn't count
    assert verify.check_owner({"state": "given", "value": "李雷", "basis": "named_in_quote"}, "把图重画一下", "王博", [])["state"] == "absent"
    assert verify.check_owner({"state": "given", "value": "思远", "basis": "named_in_quote"}, "思远你准备 slides", "周岚", ["陈思远"])["value"] == "陈思远"
    assert verify.check_owner({"state": "given", "value": "someone", "basis": "named_in_quote"}, "someone should do it", None, [])["state"] == "vague"


def test_due_must_be_in_quote():
    assert verify.check_due_raw("周五前", "我周五前跑完") == "周五前"
    assert verify.check_due_raw("下周三", "我周五前跑完") is None


def test_batch_suspicious():
    e = [{"quote": "上周的事都做完了", "utterance_id": "U1"}]
    assert verify.batch_suspicious([{"closure_evidence": e}] * 3)
    # Quoting different sentences from the same long transcript passage is not suspicious
    assert not verify.batch_suspicious([{"closure_evidence": [{"quote": q, "utterance_id": "U1"}]} for q in ("甲做完了", "乙做完了", "丙做完了")])


def test_parse_two_line_formats():
    u = parse_text("小王 21:03\n今晚我把接口写完\n小李 21:05\n收到\n周明远(导师) 00:00:12\n好，我们开始\n王博 00:01:02 我周五前跑完")
    assert [(x.speaker, x.ts, x.text) for x in u] == [("小王", "21:03", "今晚我把接口写完"), ("小李", "21:05", "收到"), ("周明远(导师)", "00:00:12", "好，我们开始"), ("王博", "00:01:02", "我周五前跑完")]


def test_dates_round2():
    assert anchor("11.10 前", M) == ("given", "2026-11-10")
    assert anchor("月底前", M) == ("given", "2026-10-31")
    assert anchor("十一月六号", M) == ("given", "2026-11-06")
    assert anchor("下周吧", M) == ("vague", None)
    assert anchor("this week", M) == ("given", "2026-10-16")
    assert anchor("71.2%", M)[1] is None


def test_nicknames():
    ms = ["王浩", "李芳", "李明"]
    assert verify.canonical_owner("小王", ms) == "王浩"
    assert verify.canonical_owner("芳姐", ms) == "李芳"
    assert verify.canonical_owner("小李", ms) == "小李"  # Two people surnamed Li, so don't guess


def test_owner_round2():
    assert verify.check_owner({"state": "given", "value": "王博", "basis": "speaker_first_person"}, "周五前跑完", "王博", [])["value"] == "王博"
    assert verify.check_owner({"state": "given", "value": "王博", "basis": "speaker_first_person"}, "你周五前跑完", "周岚", [])["state"] == "absent"
    w = [{"speaker": "周岚", "text": "你把图改一下"}, {"speaker": "王博", "text": "好的"}]
    assert verify.check_owner({"state": "given", "value": "王博", "basis": "addressed"}, "你把图改一下", "周岚", [], w)["value"] == "王博"
    # Someone who doesn't appear in the surrounding utterances can't be assigned
    assert verify.check_owner({"state": "given", "value": "李雷", "basis": "addressed"}, "你把图改一下", "周岚", [], w)["state"] == "absent"
    # The person assigning the task can't be treated as its assignee
    assert verify.check_owner({"state": "given", "value": "周岚", "basis": "addressed"}, "你把图改一下", "周岚", [], w)["state"] == "absent"


def test_day_only_and_csv():
    from app.render import csv_cell
    assert anchor("15号", M) == ("given", "2026-10-15")
    assert anchor("3号前", M) == ("given", "2026-11-03")
    assert csv_cell("=HYPERLINK(1)") == "'=HYPERLINK(1)" and csv_cell("@SUM(1)") == "'@SUM(1)" and csv_cell("正常") == "正常"


def test_english_due_words():
    assert anchor("by Friday", M) == ("given", "2026-10-16")
    assert anchor("before next Monday", M) == ("given", "2026-10-19")
    assert anchor("right after the meeting", M) == ("given", "2026-10-15")
    assert anchor("at next week's group meeting", M) == ("given", "2026-10-22")
    assert anchor("sometime soon", M) == ("vague", None)
