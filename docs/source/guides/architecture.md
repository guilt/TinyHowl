# Architecture

```{mermaid}
flowchart LR
    CLI[tinyhowl CLI] --> Demo[demo.render]
    Demo --> Baby[baby specials]
    Demo --> Say[phoneme.say]
    Say --> Inv[inventory]
    Inv --> FS[vowel_pcm / noise_pcm]
    FS --> WAV[16 kHz WAV]
    WAV -->|stdout| Ear[TinyEar ingest]
```

| Module | Role |
|---|---|
| `params` | `HowlParams`, stage, emotion |
| `synth` | frames, WAV bytes, sample rate |
| `formant_synth` | 3-formant vowels, noise, nasals |
| `inventory` | 23 atoms + `render_catalog` |
| `phoneme` | CV syllables and `say` |
| `baby` | coo / laugh / whimper / babble |
| `demo` | CLI entry |

The Python mouth is the reference. TinyHowl-C keeps the same atom names
and PCM contract so a later I2S / PDM path can speak the same inventory.
