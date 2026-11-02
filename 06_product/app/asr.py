"""Local speech-to-text: audio never leaves the server. Decoded with ffmpeg, then passed to faster-whisper."""
import os
import re
import shutil
import subprocess
import threading

import numpy as np

from .parse import Utterance, fmt_ts

ASR_MODEL = os.environ.get("BP_ASR_MODEL", "small")
_model = None
_lock = threading.Lock()


def available() -> bool:
    try:
        import faster_whisper  # noqa: F401
    except ImportError:
        return False
    return shutil.which("ffmpeg") is not None


def _get_model():
    global _model
    with _lock:
        if _model is None:
            from faster_whisper import WhisperModel
            _model = WhisperModel(ASR_MODEL, device="cpu", compute_type="int8")
    return _model


def decode(path: str) -> np.ndarray:
    p = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", path, "-f", "s16le", "-ac", "1",
                        "-acodec", "pcm_s16le", "-ar", "16000", "-"], capture_output=True)
    if p.returncode != 0 or not p.stdout:
        raise ValueError("Could not read this audio file. It may be corrupted. Please try again with an mp3, m4a, or wav file")
    return np.frombuffer(p.stdout, np.int16).astype(np.float32) / 32768.0


def transcribe(path: str, hint: str = "") -> list[Utterance]:
    audio = decode(path)
    prompt = "这是一场中英夹杂的工作会议。" + hint
    segs, _ = _get_model().transcribe(audio, initial_prompt=prompt[:400], vad_filter=True, beam_size=5)
    out = []
    for s in segs:
        # A single whisper segment can be long; split it into sentences so quotes and timestamps stay fine-grained
        for t in re.split(r"(?<=[。！？!?；;])\s*", s.text.strip()):
            if t.strip():
                out.append(Utterance(len(out) + 1, fmt_ts(s.start), None, t.strip()))
    return out
