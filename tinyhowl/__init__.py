from .params import EMOTIONS, HowlEmotion, HowlParams, HowlStage, HowlVoice, baby_base
from .synth import SAMPLE_RATE, FRAME, frame_ms, synthesize_frame, synthesize_seconds, write_wav
from .mix import mix
from .vowels import ENGLISH, BABY, WORDS, formant, list_vowels
from .phoneme import say, synthesize_syllable, synthesize_vowel

__version__ = "0.1.1"
__all__ = [
    "HowlParams", "HowlStage", "HowlEmotion", "HowlVoice", "EMOTIONS",
    "baby_base", "mix", "synthesize_frame", "synthesize_seconds", "write_wav",
    "SAMPLE_RATE", "FRAME", "frame_ms", "say", "synthesize_syllable",
    "synthesize_vowel", "formant", "list_vowels", "ENGLISH", "BABY", "WORDS",
    "__version__",
]
