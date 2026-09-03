# Getting Started with TinyHowl

Welcome. This guide gets you from zero to a WAV in under 5 minutes.

## Prerequisites

- Python 3.9+
- A sibling TinyEar checkout only if you want the process pipe

## Installation

```bash
git clone https://github.com/guilt/TinyHowl.git
cd TinyHowl && git checkout bananey
python -m pip install -e ".[dev]"
```

Until PyPI:

```bash
pip install "tinyhowl @ git+https://github.com/guilt/tinyhowl.git@bananey"
```

## First sounds

```bash
tinyhowl coo /tmp/coo.wav
tinyhowl say:mama /tmp/mama.wav
tinyhowl coo - > /tmp/coo-stdout.wav
make dataset
make tests
```

See [HOW_TO_VERIFY.md](../../HOW_TO_VERIFY.md).

## What's next

| I want to... | Guide |
|---|---|
| Understand the mouth | [Core Concepts](guides/concepts.md) |
| Render every atom | [How-To: Inventory](how_to/03_inventory.md) |
| Pipe into TinyEar | [How-To: Pipe](how_to/05_pipe_to_ear.md) |
