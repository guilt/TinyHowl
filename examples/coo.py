from pathlib import Path
from tinyhowl.baby import coo_samples
from tinyhowl.synth import write_wav
out = Path(__file__).resolve().parent / "out"
out.mkdir(exist_ok=True)
dest = out / "example-coo.wav"
write_wav(str(dest), coo_samples())
print(dest)
