# TinyHowl

Tiny is a markdown cache that can grow ears, a mouth, and borrowed eyes. If a sense is missing it says so. Port 11434. Files you can delete.

**Job:** growable formant voice. Writes sound to a speaker, not to the knowledge base.

No Howl → Tiny is still complete (silent cache).

## v0.1

English + **Baby** only. Laptop speakers first. Watch I2S third.

```bash
pip install -e .
python -m tinyhowl.demo coo
# hear a short coo, or a wav written if the machine has no speaker stack
```

Baby start params: pitch 380, var 45, rate 0.7, energy 0.65, formant 0.25, breathiness 0.35.

Zero malloc in the audio callback is a watch rule. This Python seed pre-allocates frames.
