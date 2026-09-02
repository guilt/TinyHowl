# TinyHowl

Growable formant mouth. Writes sound, not the knowledge base.

```bash
python -m pip install -e ".[dev]"
make tests
make dataset          # datasets/wav/*.wav — 23 generated atoms
tinyhowl coo /tmp/coo.wav
tinyhowl say:mama - | tinyear ingest - --out memory/ --stem mama
```

## Inventory

Not full IPA. World languages mostly need `/i e a o u/` + schwa and consonants
at three places × four manners (23 atoms). Generated, not recorded.

C twin (ESP32-S3): https://github.com/guilt/TinyHowl-C
