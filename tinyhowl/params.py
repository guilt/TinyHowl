from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HowlParams:
    base_pitch: float = 380.0
    pitch_var: float = 45.0
    rate: float = 0.7
    energy: float = 0.65
    formant_shift: float = 0.25
    breathiness: float = 0.35


@dataclass
class HowlStage:
    name: str
    base: HowlParams


@dataclass
class HowlEmotion:
    name: str
    pitch: float = 0.0
    energy: float = 0.0
    rate: float = 0.0
    breathiness: float = 0.0


EMOTIONS = {
    "happy": HowlEmotion("happy", pitch=25, energy=0.12, rate=0.05),
    "curious": HowlEmotion("curious", pitch=15, energy=0.04, rate=0.02),
    "soft": HowlEmotion("soft", pitch=-20, energy=-0.15, breathiness=0.1),
    "distressed": HowlEmotion("distressed", pitch=40, energy=0.2, rate=0.08, breathiness=0.05),
}


def baby_base() -> HowlParams:
    return HowlParams()


@dataclass
class HowlVoice:
    stage: HowlStage
    emotion: HowlEmotion
    intensity: float = 0.6
    adaptive_pitch: float = 0.0
    adaptive_energy: float = 0.0

    def final(self) -> HowlParams:
        b = self.stage.base
        e = self.emotion
        k = self.intensity
        return HowlParams(
            base_pitch=b.base_pitch + e.pitch * k + self.adaptive_pitch,
            pitch_var=b.pitch_var,
            rate=b.rate + e.rate * k,
            energy=max(0.05, min(1.0, b.energy + e.energy * k + self.adaptive_energy)),
            formant_shift=b.formant_shift,
            breathiness=max(0.0, min(0.9, b.breathiness + e.breathiness * k)),
        )
