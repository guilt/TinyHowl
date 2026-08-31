"""Published-average English + baby-ish formant table.

Numbers are rounded textbook means (Peterson & Barney / Fant-style
adult male, plus a baby-raised copy). This is a lookup table, not a
recording corpus. TinyHowl writes sound; TinyToT writes markdown.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Formant:
    name: str
    ipa: str
    f1: float
    f2: float
    f3: float


# Adult-ish English monophthongs, Hz.
ENGLISH = {
    "i": Formant("i", "i", 270, 2290, 3010),   # fleece
    "I": Formant("I", "ɪ", 390, 1990, 2550),   # kit
    "e": Formant("e", "e", 530, 1840, 2480),   # face (steady)
    "E": Formant("E", "ɛ", 610, 1900, 2460),   # dress
    "ae": Formant("ae", "æ", 860, 1720, 2410), # trap
    "a": Formant("a", "ɑ", 730, 1090, 2440),   # father
    "o": Formant("o", "o", 570, 840, 2410),    # goat (steady)
    "u": Formant("u", "u", 300, 870, 2240),    # goose
    "U": Formant("U", "ʊ", 440, 1020, 2240),   # foot
    "schwa": Formant("schwa", "ə", 500, 1500, 2500),
}

# Baby start: raise F1/F2 a bit, keep the same names.
BABY = {
    key: Formant(v.name, v.ipa, v.f1 * 1.15, v.f2 * 1.12, v.f3 * 1.05)
    for key, v in ENGLISH.items()
}

# CV tokens used by babble / first English.
SYLLABLES = {
    "ba": ("b", "a"),
    "da": ("d", "a"),
    "ga": ("g", "a"),
    "goo": ("g", "u"),
    "ma": ("m", "a"),
    "pa": ("p", "a"),
    "ta": ("t", "a"),
    "hi": ("h", "i"),
    "no": ("n", "o"),
    "me": ("m", "i"),
}

WORDS = {
    "ba": ("ba",),
    "da": ("da",),
    "goo": ("goo",),
    "ma": ("ma",),
    "mama": ("ma", "ma"),
    "dada": ("da", "da"),
    "hi": ("hi",),
    "no": ("no",),
    "me": ("me",),
}


def formant(name: str, stage: str = "baby") -> Formant:
    table = BABY if stage == "baby" else ENGLISH
    if name not in table:
        raise KeyError(f"unknown vowel {name!r}; know {sorted(table)}")
    return table[name]


def list_vowels(stage: str = "baby") -> list[str]:
    table = BABY if stage == "baby" else ENGLISH
    return list(table)
