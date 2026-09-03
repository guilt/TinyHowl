# Core Concepts

A mouth that writes the knowledge base is a liar. Howl only writes PCM.
Belief lives in markdown written by a human or by TinyEar's honest miss.

## Source-filter, not a vocoder

`formant_synth.py` is a three-formant additive source-filter: pulse/noise
at F0, resonators at F1/F2/F3, cheap envelope. Inventory vowels need real
F1/F2 peaks so TinyEar can classify them without a network.

## Baby stage

`HowlParams` plus a stage shift pitch, energy, and formants. Baby F0 sits
around 350–400 Hz. Ear's voiced detector looks for F0 in 80–1000 Hz.

## 23 atoms, not IPA

UPSID / Maddieson: most languages have `/i a u/`; the common full system is
`/i e a o u/`. Consonants collapse to three places and four manners.
