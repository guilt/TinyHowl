"""Three-formant syllable renderer. Control thread picks targets; audio
thread only walks frames. No cloud TTS. No weights.
"""
from __future__ import annotations

import math
from array import array

from .params import HowlParams
from .synth import FRAME, SAMPLE_RATE, synthesize_seconds
from .traj import ease_out
from .vowels import SYLLABLES, WORDS, formant


def _burst_gain(phone: str) -> float:
    return {
        "b": 0.35,
        "p": 0.45,
        "d": 0.40,
        "t": 0.50,
        "g": 0.38,
        "m": 0.22,
        "n": 0.22,
        "h": 0.18,
    }.get(phone, 0.0)


def synthesize_vowel(name: str, params: HowlParams, seconds: float = 0.22, stage: str = "baby"):
    v = formant(name, stage=stage)
    # Encode formants into the existing HowlParams knobs so synthesize_frame
    # stays the only audio primitive. f1 drives formant_shift; f2 rides pitch_var.
    p = HowlParams(
        base_pitch=params.base_pitch,
        pitch_var=max(8.0, (v.f2 - v.f1) / 40.0),
        rate=params.rate,
        energy=params.energy,
        formant_shift=max(-0.4, min(1.8, v.f1 / 550.0 - 1.0)),
        breathiness=params.breathiness,
    )
    return synthesize_seconds(p, seconds=seconds, envelope=ease_out)


def synthesize_syllable(token: str, params: HowlParams, stage: str = "baby"):
    if token not in SYLLABLES:
        raise KeyError(f"unknown syllable {token!r}")
    cons, vow = SYLLABLES[token]
    burst_n = int(0.025 * SAMPLE_RATE)
    burst = array("h")
    g = _burst_gain(cons)
    for i in range(burst_n):
        t = i / max(burst_n, 1)
        env = (1.0 - t) * g * params.energy
        # cheap unvoiced burst + a hint of F2
        noise = math.sin(i * 12.9898) * 0.6 + math.sin(i * 78.233) * 0.4
        burst.append(int(max(-1.0, min(1.0, env * noise)) * 22000))
    vowel = synthesize_vowel(vow, params, seconds=0.16, stage=stage)
    out = array("h")
    out.extend(burst)
    out.extend(vowel)
    return out


def say(word: str, params: HowlParams, stage: str = "baby"):
    key = word.strip().lower()
    if key not in WORDS:
        raise KeyError(f"v0.1 English/Baby words: {sorted(WORDS)}")
    gap = array("h", [0] * int(0.04 * SAMPLE_RATE))
    out = array("h")
    for i, syl in enumerate(WORDS[key]):
        if i:
            out.extend(gap)
        out.extend(synthesize_syllable(syl, params, stage=stage))
    return out
