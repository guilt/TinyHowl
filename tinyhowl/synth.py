from __future__ import annotations
import math, struct
from array import array
from .params import HowlParams
from .traj import coo_decay

SAMPLE_RATE = 16000
FRAME = 128

def synthesize_frame(params: HowlParams, phase: float, t_norm: float, envelope=None):
    env_fn = envelope or coo_decay
    env = env_fn(t_norm) * params.energy
    freq = params.base_pitch + params.pitch_var * math.sin(2 * math.pi * t_norm * 2.5)
    f1 = 550 * (1 + params.formant_shift)
    out = []
    local = phase
    inc = 2 * math.pi * freq / SAMPLE_RATE
    for i in range(FRAME):
        buzz = math.sin(local)
        form = math.sin(2 * math.pi * f1 * i / SAMPLE_RATE)
        breath = params.breathiness * math.sin(local * 11.0) * 0.15
        out.append(env * (0.7 * buzz + 0.2 * form + breath))
        local += inc
    return out, local

def synthesize_seconds(params: HowlParams, seconds: float = 0.45, envelope=None):
    n_frames = max(1, int(seconds * SAMPLE_RATE / FRAME))
    samples = array("h")
    phase = 0.0
    for f in range(n_frames):
        frame, phase = synthesize_frame(params, phase, f / n_frames, envelope=envelope)
        for x in frame:
            samples.append(int(max(-1.0, min(1.0, x)) * 28000))
    return samples

def write_wav(path: str, samples: array) -> None:
    n = len(samples)
    with open(path, "wb") as fh:
        fh.write(b"RIFF")
        fh.write(struct.pack("<I", 36 + n * 2))
        fh.write(b"WAVEfmt ")
        fh.write(struct.pack("<IHHIIHH", 16, 1, 1, SAMPLE_RATE, SAMPLE_RATE * 2, 2, 16))
        fh.write(b"data")
        fh.write(struct.pack("<I", n * 2))
        samples.tofile(fh)

def frame_ms() -> float:
    return 1000.0 * FRAME / SAMPLE_RATE
