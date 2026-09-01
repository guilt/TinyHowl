"""Howl can emit a complete WAV on stdout for another process to consume."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from tinyhowl.baby import coo_samples
from tinyhowl.demo import main
from tinyhowl.synth import SAMPLE_RATE, wav_bytes


HOWL_ROOT = Path(__file__).resolve().parents[2]


def test_wav_bytes_header():
    blob = wav_bytes(coo_samples())
    assert blob[:4] == b"RIFF" and blob[8:12] == b"WAVE"
    assert len(blob) > 44 + SAMPLE_RATE // 4


def test_demo_dash_returns_zero():
    assert main(["coo", "-"]) == 0


def test_process_stdout_pipe(tmp_path: Path):
    dest = tmp_path / "coo.wav"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(HOWL_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONUNBUFFERED"] = "1"
    proc = subprocess.run(
        [sys.executable, "-m", "tinyhowl.demo", "coo", "-"],
        cwd=str(HOWL_ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=15,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr.decode("utf-8", "replace")
    blob = proc.stdout
    assert blob[:4] == b"RIFF" and blob[8:12] == b"WAVE"
    dest.write_bytes(blob)
    assert dest.stat().st_size == len(blob)
    assert b"wrote" in proc.stderr
