# Formant dataset (offline)

TinyHowl does not ship recordings. It ships a **lookup table** of rounded
textbook formant means so a laptop can coo without a network.

Source of the numbers: long-published average F1/F2/F3 for English
monophthongs (Peterson & Barney 1952 / Fant-style adult male means),
with a baby-raised copy (`F1 * 1.15`, `F2 * 1.12`). These are physical
constants in the same sense as "A4 is 440 Hz", not a copyrighted corpus.

Render the table:

```bash
python examples/vowels_dataset.py
ls examples/out/vowels
```

v0.1 English words built from CV syllables: `ba da goo ma mama dada hi no me`.
