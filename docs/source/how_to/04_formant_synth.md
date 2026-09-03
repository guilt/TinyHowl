# How-To: Formant synth

```python
from tinyhowl import vowel_pcm
from tinyhowl.vowels import formant
v = formant("a", "baby")
pcm = vowel_pcm(380, v.f1, v.f2, v.f3, n=4096, energy=0.65)
```
