"""Three-formant syllable renderer."""
from __future__ import annotations

from array import array
from .formant_synth import concat, noise_pcm, silence_pcm, vowel_pcm
from .inventory import PLACE_COLOR_HZ, ms
from .params import HowlParams
from .synth import SAMPLE_RATE
from .vowels import SYLLABLES, WORDS, formant

_CONS_PLACE = {"b":"labial","p":"labial","m":"labial","d":"coronal","t":"coronal",
               "n":"coronal","g":"velar","k":"velar","h":"glottal"}

def synthesize_vowel(name, params, seconds=0.22, stage="baby"):
    v = formant(name, stage=stage)
    n = max(1, int(seconds * SAMPLE_RATE))
    return vowel_pcm(params.base_pitch, v.f1, v.f2, v.f3, n, energy=params.energy)

def synthesize_syllable(token, params, stage="baby"):
    if token not in SYLLABLES:
        raise KeyError(token)
    cons, vow = SYLLABLES[token]
    place = _CONS_PLACE.get(cons, "coronal")
    color = PLACE_COLOR_HZ[place]
    voiced = cons in {"b", "d", "g", "m", "n"}
    if cons in {"m", "n"}:
        burst = vowel_pcm(params.base_pitch, 280.0, color, 2200.0, ms(40),
                          energy=0.35 * params.energy, breath=0.04)
    elif cons == "h":
        burst = noise_pcm(ms(40), 0.22 * params.energy, 400.0)
    else:
        burst = noise_pcm(ms(22), (0.50 if not voiced else 0.32) * params.energy, color)
    return concat(burst, synthesize_vowel(vow, params, seconds=0.16, stage=stage))

def say(word, params, stage="baby"):
    key = word.strip().lower()
    if key not in WORDS:
        raise KeyError(key)
    gap = silence_pcm(int(0.04 * SAMPLE_RATE))
    parts = []
    for i, syl in enumerate(WORDS[key]):
        if i:
            parts.append(gap)
        parts.append(synthesize_syllable(syl, params, stage=stage))
    return concat(*parts)
