from pathlib import Path

from tinyhowl.params import baby_base
from tinyhowl.phoneme import say
from tinyhowl.synth import write_wav

out = Path(__file__).resolve().parent / "out"
out.mkdir(exist_ok=True)
dest = out / "example-mama.wav"
write_wav(str(dest), say("mama", baby_base()))
print(dest)
