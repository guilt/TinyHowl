"""Bare-minimum spoken-sound inventory.

Not every IPA phone. UPSID/Maddieson: ~90% of languages have /i a u/;
the most common full system is /i e a o u/. Consonants collapse to three
places and four manners. Those atoms compose baby babble and English CV
words and fit an ESP32-S3 frame (128 samples @ 16 kHz).
"""
from __future__ import annotations

from dataclasses import dataclass
from array import array

from .formant_synth import concat, nasal_pcm, noise_pcm, silence_pcm, vowel_pcm
from .params import HowlParams, baby_base
from .synth import SAMPLE_RATE
from .vowels import BABY, ENGLISH, formant

CORE_VOWELS = ("i", "e", "a", "o", "u", "schwa")
PLACE_COLOR_HZ = {"labial": 800.0, "coronal": 1800.0, "velar": 1400.0, "glottal": 400.0}
CONSONANTS = {
    "p": ("stop", "labial", False), "b": ("stop", "labial", True),
    "t": ("stop", "coronal", False), "d": ("stop", "coronal", True),
    "k": ("stop", "velar", False), "g": ("stop", "velar", True),
    "m": ("nasal", "labial", True), "n": ("nasal", "coronal", True),
    "ng": ("nasal", "velar", True),
    "f": ("fricative", "labial", False), "s": ("fricative", "coronal", False),
    "sh": ("fricative", "coronal", False), "h": ("fricative", "glottal", False),
    "w": ("approx", "labial", True), "y": ("approx", "coronal", True),
    "l": ("approx", "coronal", True),
}

@dataclass(frozen=True)
class Primitive:
    name: str
    kind: str
    place: str
    voiced: bool
    ipa: str

def primitives():
    rows = [Primitive("silence", "silence", "none", False, "")]
    for name in CORE_VOWELS:
        v = formant(name, "baby")
        rows.append(Primitive(name, "vowel", "vowel", True, v.ipa))
    ipa_cons = {"p":"p","b":"b","t":"t","d":"d","k":"k","g":"g","m":"m","n":"n",
                "ng":"ng","f":"f","s":"s","sh":"sh","h":"h","w":"w","y":"j","l":"l"}
    for name, (kind, place, voiced) in CONSONANTS.items():
        rows.append(Primitive(name, kind, place, voiced, ipa_cons[name]))
    return rows

def ms(n_ms):
    return max(1, int(SAMPLE_RATE * n_ms / 1000.0))

def render_primitive(name, params=None, stage="baby"):
    p = params or baby_base()
    if name == "silence":
        return silence_pcm(ms(180))
    if name in ENGLISH or name in BABY:
        v = formant(name, stage=stage)
        return vowel_pcm(p.base_pitch, v.f1, v.f2, v.f3, ms(260), energy=p.energy)
    if name not in CONSONANTS:
        raise KeyError(name)
    kind, place, voiced = CONSONANTS[name]
    color = PLACE_COLOR_HZ[place]
    if kind == "fricative":
        hz = 3200.0 if name == "sh" else (2200.0 if name == "s" else color)
        gain = 0.55 if name != "h" else 0.28
        return noise_pcm(ms(220), gain * p.energy, hz)
    if kind == "nasal":
        v = formant("a" if place != "velar" else "u", stage=stage)
        return nasal_pcm(p.base_pitch, v.f1, color, ms(220), energy=0.5 * p.energy)
    if kind == "approx":
        vow = {"w": "u", "y": "i", "l": "schwa"}[name]
        v = formant(vow, stage=stage)
        return vowel_pcm(p.base_pitch * 0.9, v.f1, v.f2, v.f3, ms(180), energy=0.45 * p.energy)
    burst = noise_pcm(ms(22), (0.55 if not voiced else 0.35) * p.energy, color)
    if voiced:
        v = formant("a", stage=stage)
        tail = vowel_pcm(p.base_pitch, v.f1, color, v.f3, ms(90), energy=0.4 * p.energy)
        return concat(burst, tail)
    return concat(burst, silence_pcm(ms(40)))

def render_catalog(stage="baby"):
    p = baby_base()
    return {pr.name: render_primitive(pr.name, p, stage=stage) for pr in primitives()}
