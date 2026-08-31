from __future__ import annotations
from .params import EMOTIONS, HowlEmotion, HowlStage, HowlVoice, baby_base
from .synth import synthesize_seconds
from .traj import coo_decay, ease_in, ease_out

BABBLE = ("ba", "da", "goo", "ma")

def baby_voice(emotion: str = "soft", intensity: float = 0.6) -> HowlVoice:
    return HowlVoice(stage=HowlStage("baby", baby_base()),
                     emotion=EMOTIONS.get(emotion, HowlEmotion("soft")), intensity=intensity)

def coo_samples():
    return synthesize_seconds(baby_voice("soft", 0.7).final(), seconds=0.5, envelope=coo_decay)

def laugh_samples():
    return synthesize_seconds(baby_voice("happy", 0.85).final(), seconds=0.35, envelope=ease_out)

def whimper_samples():
    return synthesize_seconds(baby_voice("distressed", 0.55).final(), seconds=0.4, envelope=ease_in)

def babble_samples():
    parts = []
    for i, _cv in enumerate(BABBLE):
        emo = ("curious", "happy", "soft", "curious")[i]
        parts.append(synthesize_seconds(baby_voice(emo, 0.65).final(), seconds=0.18, envelope=ease_out))
    out = parts[0]
    for p in parts[1:]:
        out.extend(p)
    return out
