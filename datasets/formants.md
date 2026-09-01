# Formant dataset (offline)

TinyHowl does not ship recordings. It ships a **lookup table** of rounded
textbook formant means so a laptop can coo without a network.

Source of the numbers: long-published average F1/F2/F3 for English
monophthongs (Peterson & Barney 1952 / Fant-style adult male means),
with a baby-raised copy (`F1 * 1.15`, `F2 * 1.12`). These are physical
constants in the same sense as "A4 is 440 Hz", not a copyrighted corpus.

| token | IPA | adult F1 | adult F2 | adult F3 |
|-------|-----|----------|----------|----------|
| i     | i   | 270      | 2290     | 3010     |
| I     | ɪ   | 390      | 1990     | 2550     |
| e     | e   | 530      | 1840     | 2480     |
| E     | ɛ   | 610      | 1900     | 2460     |
| ae    | æ   | 860      | 1720     | 2410     |
| a     | ɑ   | 730      | 1090     | 2440     |
| o     | o   | 570      | 840      | 2410     |
| u     | u   | 300      | 870      | 2240     |
| U     | ʊ   | 440      | 1020     | 2240     |
| schwa | ə   | 500      | 1500     | 2500     |

Render the table:

```bash
python examples/vowels_dataset.py
ls examples/out/vowels
```

v0.1 English words built from CV syllables: `ba da goo ma mama dada hi no me`.
