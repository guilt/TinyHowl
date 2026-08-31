# TinyHowl

Tiny is a markdown cache that can grow ears, a mouth, and borrowed eyes. If a sense is missing it says so. Port 11434. Files you can delete.

**Job:** growable formant voice. Writes sound to a speaker, not to the knowledge base.

No Howl → Tiny is still complete (silent cache).

## Quick start

```bash
python -m pip install -e ".[dev]"
make tests          # coverage gate 80%
make examples       # writes examples/out/*.wav and vowels/
tinyhowl coo /tmp/coo.wav
tinyhowl say:mama /tmp/mama.wav
```

## v0.1

English + **Baby** only. Laptop speakers first. Watch I2S third.

Specials: `coo`, `laugh` / `soft_laugh`, `whimper`, `babble` (`ba da goo ma`).

English words from CV syllables: `ba da goo ma mama dada hi no me`.

Emotions: happy, curious, soft, distressed.

Baby start: pitch 380, var 45, rate 0.7, energy 0.65, formant 0.25, breathiness 0.35.

16 kHz, 128 samples = 8 ms. Control thread writes targets. Audio thread only smooths.

Formant table lives in `datasets/formants.md` and `tinyhowl/vowels.py`. It is a
lookup table of published average F1/F2/F3, not a recording dump.

Watch size aim: code 70–150 KB flash, RAM 100–250 KB (Howl ≤ 0.35 MB with emotion).
