"""final = stage.base + emotion.modifier * intensity + adaptive"""
from __future__ import annotations
from .params import HowlEmotion, HowlParams, HowlStage, HowlVoice

def mix(stage: HowlStage, emotion: HowlEmotion, intensity: float = 0.6,
        adaptive_pitch: float = 0.0, adaptive_energy: float = 0.0) -> HowlParams:
    return HowlVoice(stage=stage, emotion=emotion, intensity=intensity,
                     adaptive_pitch=adaptive_pitch, adaptive_energy=adaptive_energy).final()
