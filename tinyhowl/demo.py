from __future__ import annotations
import sys
from pathlib import Path
from .baby import babble_samples, coo_samples, laugh_samples, whimper_samples
from .params import baby_base
from .phoneme import say
from .synth import write_wav

SPECIALS = {
    "coo": coo_samples,
    "laugh": laugh_samples,
    "soft_laugh": laugh_samples,
    "whimper": whimper_samples,
    "babble": babble_samples,
}


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    kind = argv[0] if argv else "coo"
    out = Path(argv[1]) if len(argv) > 1 else Path(f"howl-{kind}.wav")
    if kind in SPECIALS:
        samples = SPECIALS[kind]()
    elif kind.startswith("say:"):
        word = kind.split(":", 1)[1]
        try:
            samples = say(word, baby_base())
        except KeyError as e:
            print(e)
            return 1
    else:
        print("v0.1 specials:", ", ".join(SPECIALS))
        print("english: say:mama say:hi say:no say:ba say:dada say:me")
        return 1
    write_wav(str(out), samples)
    print(f"wrote {out} ({len(samples)} samples @ 16 kHz)")
    try:
        import simpleaudio
        simpleaudio.WaveObject.from_wave_file(str(out)).play().wait_done()
    except Exception:
        print("(no playback stack; wav is enough)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
