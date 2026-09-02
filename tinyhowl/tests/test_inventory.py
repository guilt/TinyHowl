from pathlib import Path
from tinyhowl.inventory import CORE_VOWELS, CONSONANTS, primitives, render_catalog, render_primitive
from tinyhowl.synth import SAMPLE_RATE, wav_bytes, write_wav

def test_primitive_count_is_the_bare_minimum():
    names = [p.name for p in primitives()]
    assert "silence" in names
    for v in CORE_VOWELS:
        assert v in names
    for c in CONSONANTS:
        assert c in names
    assert len(names) == 23

def test_every_primitive_is_pcm16_and_short():
    for pr in primitives():
        s = render_primitive(pr.name)
        assert SAMPLE_RATE // 20 <= len(s) <= SAMPLE_RATE
        if pr.kind != "silence":
            assert max(abs(x) for x in s) > 200

def test_catalog_writes_wav(tmp_path: Path):
    cat = render_catalog()
    blob = wav_bytes(cat["a"])
    assert blob[:4] == b"RIFF" and blob[8:12] == b"WAVE"
    dest = tmp_path / "a.wav"
    write_wav(str(dest), cat["a"])
    assert dest.stat().st_size == len(blob)

def test_unknown_primitive():
    try:
        render_primitive("click")
    except KeyError:
        return
    raise AssertionError("expected KeyError")
