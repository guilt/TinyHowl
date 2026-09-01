# HOW_TO_VERIFY — TinyHowl

Tiny is a markdown cache that can grow ears, a mouth, and borrowed eyes.
If a sense is missing it says so. Port 11434. Files you can delete.

Howl writes **sound**, never the knowledge base.

```bash
python -m pip install -e ".[dev]"   # or: PYTHONPATH=. make tests
make tests                          # coverage gate 80%
make examples                       # wavs under examples/out/
tinyhowl coo /tmp/coo.wav
tinyhowl say:mama /tmp/mama.wav
```

Expect:

- `examples/out/coo.wav` is RIFF/WAVE, 16 kHz, longer than 0.25 s
- `examples/out/vowels/` has one wav per vowel in the formant table
- unknown special prints the v0.1 list and exits 1
- frame wall time on a laptop is under 8 ms (`examples/bench_frame.py`)
- `tinyhowl coo -` writes a RIFF/WAVE blob on stdout (`make pipe`)

No Howl installed → Tiny is still complete (silent cache).
