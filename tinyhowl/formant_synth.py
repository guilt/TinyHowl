"""Three-formant additive source-filter. Stdlib only.

The old `synthesize_frame` path is a cheap coo. Inventory vowels need
real F1/F2 peaks so TinyEar can classify them without a network.
"""
from __future__ import annotations

import math
from array import array

from .synth import SAMPLE_RATE

TWO_PI = 2.0 * math.pi


def _clamp_i16(x: float) -> int:
    return int(max(-1.0, min(1.0, x)) * 28000)


def _env(i: int, n: int, attack: float = 0.04, release: float = 0.12) -> float:
    if n <= 1:
        return 1.0
    t = i / n
    a = 1.0 if t >= attack else t / max(attack, 1e-6)
    r = 1.0 if t <= 1.0 - release else max(0.0, (1.0 - t) / max(release, 1e-6))
    return a * r


def _noise(i: int) -> float:
    x = math.sin(i * 12.9898 + 0.17) * 43758.5453
    return (x - math.floor(x)) * 2.0 - 1.0


def vowel_pcm(f0, f1, f2, f3, n, energy=0.65, breath=0.08):
    out = array("h")
    p0 = p1 = p2 = p3 = 0.0
    i0 = TWO_PI * f0 / SAMPLE_RATE
    i1 = TWO_PI * f1 / SAMPLE_RATE
    i2 = TWO_PI * f2 / SAMPLE_RATE
    i3 = TWO_PI * f3 / SAMPLE_RATE
    for i in range(n):
        env = _env(i, n) * energy
        buzz = 0.45 * math.sin(p0) + 0.22 * math.sin(2.0 * p0) + 0.10 * math.sin(3.0 * p0)
        y = (0.28 * math.sin(p1) + 0.42 * math.sin(p2) + 0.12 * math.sin(p3)
             + 0.18 * buzz + breath * _noise(i) * 0.15)
        out.append(_clamp_i16(y * env))
        p0 += i0; p1 += i1; p2 += i2; p3 += i3
    return out


def noise_pcm(n, energy, color_hz):
    out = array("h")
    phase = 0.0
    inc = TWO_PI * color_hz / SAMPLE_RATE
    prev = 0.0
    for i in range(n):
        env = _env(i, n, attack=0.01, release=0.25) * energy
        white = _noise(i)
        hp = white - prev
        prev = white
        y = 0.7 * hp + 0.3 * math.sin(phase) * white
        out.append(_clamp_i16(y * env))
        phase += inc
    return out


def nasal_pcm(f0, f1, f2, n, energy=0.45):
    return vowel_pcm(f0, f1, f2 * 0.72, f1 * 2.4, n, energy=energy, breath=0.04)


def silence_pcm(n):
    return array("h", [0] * n)


def concat(*parts):
    out = array("h")
    for p in parts:
        out.extend(p)
    return out
