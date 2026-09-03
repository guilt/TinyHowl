# TinyHowl

**Growable formant mouth. Writes sound, not the knowledge base.**

---

## The thesis

A growing organism needs a mouth that can make the same atoms an ear can classify. Howl generates those atoms. It does not write beliefs.

---

## Documentation

```{toctree}
:maxdepth: 1
:caption: Get started

getting_started
```

```{toctree}
:maxdepth: 1
:caption: Guides

guides/concepts
guides/architecture
```

```{toctree}
:maxdepth: 1
:caption: How-To

how_to/index
```

```{toctree}
:maxdepth: 1
:caption: Reference

api/README
```

---

## Architecture

```{mermaid}
flowchart LR
    P[params / stage] --> S[formant_synth]
    I[23-atom inventory] --> S
    S --> W[WAV 16 kHz]
    W --> E[TinyEar]
```

See [Architecture Guide](guides/architecture) for the full explanation.

---

## What's next

| I want to... | Guide |
|---|---|
| Hear a coo | [Getting Started](getting_started) |
| Render atoms | [How-To: Inventory](how_to/03_inventory) |
| Pipe to Ear | [How-To: Pipe](how_to/05_pipe_to_ear) |
