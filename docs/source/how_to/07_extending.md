# How-To: Extending

1. Add a row to `CONSONANTS` or `CORE_VOWELS` in `inventory.py`.
2. Teach `render_primitive` how to paint it.
3. Add a formant row if it is a vowel.
4. `make dataset` and classify with TinyEar.
5. Keep ESP32-S3 in mind: one frame is 128 samples @ 16 kHz.
