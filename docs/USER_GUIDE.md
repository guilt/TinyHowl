# TinyHowl User Guide

## Where to start

| I want to... | Section |
|---|---|
| Get up and running in 5 minutes | [Quick start](#quick-start) |
| Understand what Howl will and will not do | [Contract](#contract) |
| Hear a coo / mama | [Specials and words](#specials-and-words) |
| Generate every atom | [Inventory](#inventory) |
| Feed TinyEar | [Pipe](#pipe) |

---

## Contract

Howl writes **sound**. It never writes the knowledge base. Tiny without Howl
is still a complete silent cache.

- Sample rate is 16 kHz, mono, 16-bit PCM, RIFF/WAVE.
- No network. No model weights. Stdlib only (optional `simpleaudio` for play).
- Unknown specials print the v0.1 list and exit 1.
- Frame wall time on a laptop is under 8 ms.

---

## Quick start

```bash
python -m pip install -e ".[dev]"
tinyhowl coo /tmp/coo.wav
tinyhowl say:mama /tmp/mama.wav
tinyhowl coo - > /tmp/coo.wav
```

---

## Specials and words

| Kind | Command |
|---|---|
| `coo` / `laugh` / `whimper` / `babble` | `tinyhowl coo out.wav` |
| word | `tinyhowl say:mama out.wav` |

```python
from tinyhowl import say, write_wav
from tinyhowl.params import baby_base
write_wav("/tmp/mama.wav", say("mama", baby_base()))
```

---

## Inventory

23 atoms: silence, `i e a o u schwa`, stops `p b t d k g`, nasals `m n ng`,
fricatives `f s sh h`, approximants `w y l`.

```bash
make dataset
```

```python
from tinyhowl import primitives, render_primitive
assert len(primitives()) == 23
```

Not ASR training data. Smallest set that composes baby babble and English
CV words and still fits an ESP32-S3 frame (128 samples @ 16 kHz).

---

## Pipe

```bash
tinyhowl coo - | tinyear ingest - --out /tmp/ear --stem coo
```

Without `--transcript` the belief is `I did not catch words.`

---

## C twin

[TinyHowl-C](https://github.com/guilt/TinyHowl-C) mirrors `vowel_pcm` /
`noise_pcm` / the atom table on the host and sketches the ESP32-S3 I2S path.
