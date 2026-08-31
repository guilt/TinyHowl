"""Write the bundled formant table as 16 kHz wavs under examples/out/vowels/."""
from pathlib import Path

from tinyhowl.params import baby_base
from tinyhowl.phoneme import synthesize_vowel
from tinyhowl.synth import write_wav
from tinyhowl.vowels import list_vowels

out = Path(__file__).resolve().parent / "out" / "vowels"
out.mkdir(parents=True, exist_ok=True)
params = baby_base()
written = []
for name in list_vowels("baby"):
    dest = out / f"baby-{name}.wav"
    write_wav(str(dest), synthesize_vowel(name, params, seconds=0.28, stage="baby"))
    written.append(dest)
print(f"wrote {len(written)} vowels -> {out}")
