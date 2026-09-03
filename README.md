# TinyHowl — Growable Formant Mouth

[![GitHub](https://img.shields.io/badge/GitHub-guilt/TinyHowl-181717?logo=github)](https://github.com/guilt/TinyHowl)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![docs](https://img.shields.io/badge/docs-USER_GUIDE-0A66C2)](docs/USER_GUIDE.md)

Tiny is a markdown cache that can grow ears, a mouth, and borrowed eyes. If a sense is missing it says so. Port 11434. Files you can delete.

Howl writes **sound**, never the knowledge base. Stdlib only. 16 kHz PCM.
The same atoms that a baby uses to coo, laugh, and say `mama` are generated
from a 23-phone inventory — five vowels + schwa and three places × four manners.

```bash
python -m pip install -e ".[dev]"
make tests
make dataset          # datasets/wav/*.wav — 23 generated atoms
tinyhowl coo /tmp/coo.wav
tinyhowl say:mama - | tinyear ingest - --out memory/ --stem mama
```

## The core idea

Not full IPA. World languages mostly need `/i e a o u/` + schwa and consonants
at three places × four manners (23 atoms). Generated, not recorded. TinyEar
classifies the same atoms with Goertzel + spectral tilt — no ASR, no weights.

## Capabilities

| Feature | What it does |
|---|---|
| Specials | `coo`, `laugh`, `whimper`, `babble` |
| `say:` words | `mama`, `hi`, `no`, `ba`, `dada`, `me` |
| 23-atom inventory | vowels, stops, nasals, fricatives, approximants, silence |
| 3-formant synth | additive source-filter so Ear can see F1/F2 peaks |
| stdout pipe | `tinyhowl coo -` writes a RIFF/WAVE blob for TinyEar |
| C twin | [TinyHowl-C](https://github.com/guilt/TinyHowl-C) targets ESP32-S3 |

## Quick start

```bash
git clone https://github.com/guilt/TinyHowl.git
cd TinyHowl && git checkout bananey
python -m pip install -e ".[dev]"
make tests && make dataset
tinyhowl coo /tmp/coo.wav
```

Until PyPI: `pip install "tinyhowl @ git+https://github.com/guilt/tinyhowl.git@bananey"`

## Documentation

| I want to... | Page |
|---|---|
| Get running in 5 minutes | [Getting Started](docs/source/getting_started.md) |
| Understand the mouth | [User Guide](docs/USER_GUIDE.md) |
| Render the 23 atoms | [How-To: Inventory](docs/source/how_to/03_inventory.md) |
| Pipe into TinyEar | [How-To: Pipe](docs/source/how_to/05_pipe_to_ear.md) |
| Look up a symbol | [API Reference](docs/source/api/README.md) |

## Development

```
make tests            pytest with coverage (gate ≥ 80%)
make examples         specials + inventory wavs
make dataset          formant table + 23-atom wavs
make pipe             emit a WAV on stdout
make lint / format    ruff
make docs             regenerate API docs + build Sphinx HTML
make docs-serve       serve docs on localhost
make live-docs        live-reload docs server
```

## Project structure

```
tinyhowl/     params, synth, formant_synth, inventory, phoneme, baby, demo
tinyhowl/cli  generate_api_docs
docs/         USER_GUIDE + Sphinx source (GitHub-friendly markdown)
datasets/     formants.md + generated wav/
```

## Family

- [TinyToT](https://github.com/guilt/TinyToT) — inference server
- [TinyEar](https://github.com/guilt/TinyEar) — ingest + classify
- [TinyEye](https://github.com/guilt/TinyEye) — JPEG + belief sidecar
- [NanoToT](https://github.com/guilt/NanoToT) — clone / child packer
- [TinyHowl-C](https://github.com/guilt/TinyHowl-C) — C / ESP32-S3 twin

## Links

- **GitHub**: [github.com/guilt/TinyHowl](https://github.com/guilt/TinyHowl)
- **Docs**: [USER_GUIDE](docs/USER_GUIDE.md) · [Getting started](docs/source/getting_started.md) · [API](docs/source/api/README.md)
- **C twin**: [TinyHowl-C](https://github.com/guilt/TinyHowl-C)

## License

MIT — see [LICENSE.md](LICENSE.md).
