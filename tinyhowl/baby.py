from .params import HowlEmotion, HowlStage, HowlVoice, baby_base
from .synth import synthesize_seconds

BABBLE = ("ba", "da", "goo", "ma")


def baby_voice(emotion: str = "soft", intensity: float = 0.6) -> HowlVoice:
    from .params import EMOTIONS

    return HowlVoice(
        stage=HowlStage("baby", baby_base()),
        emotion=EMOTIONS.get(emotion, HowlEmotion("soft")),
        intensity=intensity,
    )


def coo_samples():
    return synthesize_seconds(baby_voice("soft", 0.7).final(), seconds=0.5)
