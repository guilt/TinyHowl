from pathlib import Path

from tinyhowl.baby import BABBLE, babble_samples, coo_samples, laugh_samples, whimper_samples
from tinyhowl.demo import main
from tinyhowl.mix import mix
from tinyhowl.params import EMOTIONS, HowlStage, baby_base
from tinyhowl.phoneme import say, synthesize_syllable, synthesize_vowel
from tinyhowl.synth import FRAME, SAMPLE_RATE, frame_ms, synthesize_frame, write_wav
from tinyhowl.traj import ease_in, ease_out, linear
from tinyhowl.vowels import WORDS, formant, list_vowels


def test_frame_budget():
    assert frame_ms() == 8.0
    frame, phase = synthesize_frame(baby_base(), 0.0, 0.0)
    assert len(frame) == FRAME and phase != 0


def test_coo_is_pcm():
    s = coo_samples()
    assert len(s) >= SAMPLE_RATE // 4
    assert max(abs(x) for x in s) > 0


def test_specials_nonzero():
    for fn in (laugh_samples, whimper_samples, babble_samples):
        s = fn()
        assert max(abs(x) for x in s) > 0


def test_mix_happy_raises_pitch():
    base = baby_base()
    happy = mix(HowlStage("baby", base), EMOTIONS["happy"], intensity=1.0)
    assert happy.base_pitch > base.base_pitch


def test_mix_soft_lowers_energy():
    base = baby_base()
    soft = mix(HowlStage("baby", base), EMOTIONS["soft"], intensity=1.0)
    assert soft.energy < base.energy


def test_traj():
    assert linear(0) == 0 and linear(2) == 1
    assert ease_in(0.5) < ease_out(0.5)


def test_babble_tokens():
    assert BABBLE == ("ba", "da", "goo", "ma")
    assert len(babble_samples()) > len(coo_samples())


def test_demo_writes(tmp_path: Path):
    out = tmp_path / "coo.wav"
    assert main(["coo", str(out)]) == 0
    assert out.stat().st_size > 44
    assert main(["nope"]) == 1


def test_demo_say(tmp_path: Path):
    out = tmp_path / "mama.wav"
    assert main(["say:mama", str(out)]) == 0
    assert out.stat().st_size > 44
    assert main(["say:xyzzy"]) == 1


def test_write_wav_header(tmp_path: Path):
    p = tmp_path / "x.wav"
    write_wav(str(p), coo_samples())
    data = p.read_bytes()
    assert data[:4] == b"RIFF" and data[8:12] == b"WAVE"


def test_formant_table():
    baby_a = formant("a", "baby")
    adult_a = formant("a", "english")
    assert baby_a.f1 > adult_a.f1
    assert "a" in list_vowels("baby")


def test_unknown_vowel():
    try:
        formant("zzz")
    except KeyError:
        return
    raise AssertionError("expected KeyError")


def test_say_mama_longer_than_ma():
    p = baby_base()
    assert len(say("mama", p)) > len(say("ma", p))
    assert len(synthesize_syllable("ba", p)) > FRAME
    assert len(synthesize_vowel("i", p, seconds=0.1)) >= FRAME


def test_words_inventory():
    assert set(WORDS) >= {"mama", "hi", "no", "ba", "dada"}
