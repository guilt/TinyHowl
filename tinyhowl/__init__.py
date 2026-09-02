from .params import EMOTIONS, HowlEmotion, HowlParams, HowlStage, HowlVoice, baby_base
from .synth import SAMPLE_RATE, FRAME, frame_ms, synthesize_frame, synthesize_seconds, write_wav, wav_bytes
from .mix import mix
from .vowels import ENGLISH, BABY, WORDS, formant, list_vowels
from .phoneme import say, synthesize_syllable, synthesize_vowel
from .inventory import CORE_VOWELS, CONSONANTS, primitives, render_catalog, render_primitive
from .formant_synth import vowel_pcm, noise_pcm

__version__ = "0.1.3"
__all__ = [
    "HowlParams", "HowlStage", "HowlEmotion", "HowlVoice", "EMOTIONS",
    "baby_base", "mix", "synthesize_frame", "synthesize_seconds", "write_wav",
    "wav_bytes", "SAMPLE_RATE", "FRAME", "frame_ms", "say", "synthesize_syllable",
    "synthesize_vowel", "formant", "list_vowels", "ENGLISH", "BABY", "WORDS",
    "CORE_VOWELS", "CONSONANTS", "primitives", "render_catalog", "render_primitive",
    "vowel_pcm", "noise_pcm", "__version__",
]
