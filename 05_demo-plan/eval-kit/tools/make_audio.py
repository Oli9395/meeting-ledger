#!/usr/bin/env python3
# ---
# title: Synthetic meeting audio generation script (macOS say + ffmpeg)
# status: v1 (verified with --limit on the author's machine; the full generation must be run by the project owner)
# ---
"""Convert meetings/*.md into multi-speaker audio for products that only accept audio (Feishu Minutes, Tongyi Tingwu, Otter, Fellow).

Dependencies: macOS's built-in `say`; `ffmpeg` from Homebrew (brew install ffmpeg). The script itself uses only the standard library.

  python3 -I tools/make_audio.py --meeting M3                 # Generate audio/M3.m4a and audio/M3.offsets.csv
  python3 -I tools/make_audio.py --meeting all
  python3 -I tools/make_audio.py --meeting M3 --limit 4       # Synthesize only the first 4 utterances for a test listen
  python3 -I tools/make_audio.py --list-voices                # See which Chinese/English voices this machine has

Known limitations (be sure to include these in the "experimental conditions" of the results):
- This machine has only a few Chinese voices (Tingting zh_CN and Meijia zh_TW on the author's machine), so the 5 Chinese speakers can only be distinguished by "different voice + different speaking rate".
  Speaker diarization may be harder or easier than with real human recordings, so results cannot be directly extrapolated to real group meetings.
- Chinese voices pronounce English technical terms unnaturally, which lowers ASR term recall. This is a TTS issue, not entirely a problem with the product under test.
  The README therefore recommends that at least 1–2 segments be read aloud by real people (yourself and classmates), with TTS serving only as a reproducible control condition.
- Actual times in the audio differ from the estimated timestamps in the transcript; offsets.csv records the true start of each utterance in the audio, so use it to convert times when processing product output.
"""
import argparse
import csv
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINE = re.compile(r"^\[(\d\d:\d\d:\d\d)\] (.+?)：(.*)$")
DEFAULT_VOICES = {
    # Speaker: [voice, speaking rate (words/minute)]. Use --voices to point to a custom JSON override.
    "周岚": ["Tingting", 170],
    "陈思远": ["Meijia", 185],
    "李沐晴": ["Tingting", 205],
    "王博": ["Meijia", 155],
    "赵敏": ["Tingting", 190],
    "Daniel Ong": ["Daniel", 180],
    "Priya Nair": ["Karen", 175],
    "Marco Rossi": ["Fred", 170],
}
GAP_SEC = 0.6


def need(tool):
    if shutil.which(tool) is None:
        sys.exit(f"[Error] Cannot find {tool}. say is only available on macOS; ffmpeg can be installed with `brew install ffmpeg`.")


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        sys.exit(f"[Error] Command failed: {' '.join(cmd)}\n{r.stderr[-800:]}")
    return r.stdout


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", path])
    return float(out.strip())


def fmt(sec):
    sec = int(round(sec))
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def build(mid, voices, outdir, limit=None):
    files = glob.glob(os.path.join(HERE, "meetings", f"{mid}_*.md"))
    if len(files) != 1:
        sys.exit(f"[Error] Cannot find meeting {mid}")
    utts = [LINE.match(l.rstrip("\n")).groups() for l in open(files[0], encoding="utf-8") if LINE.match(l.rstrip("\n"))]
    if limit:
        utts = utts[:limit]
    os.makedirs(outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        silence = os.path.join(tmp, "gap.wav")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", str(GAP_SEC), silence])
        parts, rows, t = [], [], 0.0
        for i, (ts, spk, text) in enumerate(utts):
            if spk not in voices:
                sys.exit(f"[Error] No voice configured for speaker {spk}")
            voice, rate = voices[spk]
            aiff = os.path.join(tmp, f"s{i:03d}.aiff")
            wav = os.path.join(tmp, f"s{i:03d}.wav")
            run(["say", "-v", voice, "-r", str(rate), "-o", aiff, text])
            run(["ffmpeg", "-y", "-loglevel", "error", "-i", aiff, "-ar", "16000", "-ac", "1", wav])
            rows.append([i + 1, ts, fmt(t), spk, voice])
            t += duration(wav) + GAP_SEC
            parts += [wav, silence]
        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w", encoding="utf-8") as f:
            for p in parts:
                f.write(f"file '{p}'\n")
        out = os.path.join(outdir, f"{mid}.m4a")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c:a", "aac", "-b:a", "96k", out])
    with open(os.path.join(outdir, f"{mid}.offsets.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["utterance_no", "transcript_ts", "audio_ts", "speaker", "voice"])
        w.writerows(rows)
    print(f"{mid}: {len(utts)} utterances, about {fmt(t)}, output {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meeting", default="all", help="M1..M5 or all")
    ap.add_argument("--voices", help="Custom voice JSON: {speaker: [voice, rate]}")
    ap.add_argument("--out", default=os.path.join(HERE, "audio"))
    ap.add_argument("--limit", type=int)
    ap.add_argument("--list-voices", action="store_true")
    a = ap.parse_args()
    need("say")
    if a.list_voices:
        print("\n".join(l for l in run(["say", "-v", "?"]).splitlines() if re.search(r"\b(zh_|en_)", l)))
        return
    need("ffmpeg"); need("ffprobe")
    voices = DEFAULT_VOICES
    if a.voices:
        with open(a.voices, encoding="utf-8") as f:
            voices = {**voices, **json.load(f)}
    mids = ["M1", "M2", "M3", "M4", "M5"] if a.meeting == "all" else [a.meeting]
    for mid in mids:
        build(mid, voices, a.out, a.limit)


if __name__ == "__main__":
    main()
