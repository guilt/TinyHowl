from .params import EMOTIONS, HowlEmotion, HowlParams, HowlStage, HowlVoice, baby_base
from .synth import SAMPLE_RATE, FRAME, frame_ms, synthesize_frame, synthesize_seconds, write_wav
from .mix import mix

__version__ = "0.1.0"
__all__ = [
    "HowlParams", "HowlStage", "HowlEmotion", "HowlVoice", "EMOTIONS",
    "baby_base", "mix", "synthesize_frame", "synthesize_seconds", "write_wav",
    "SAMPLE_RATE", "FRAME", "frame_ms", "__version__",
]
