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


def render(kind: str):
    if kind in SPECIALS:
        return SPECIALS[kind]()
    if kind.startswith("say:"):
        return say(kind.split(":", 1)[1], baby_base())
    raise KeyError(kind)


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    kind = argv[0] if argv else "coo"
    raw_out = argv[1] if len(argv) > 1 else f"howl-{kind}.wav"
    try:
        samples = render(kind)
    except KeyError:
        print("v0.1 specials:", ", ".join(SPECIALS), file=sys.stderr)
        print("english: say:mama say:hi say:no say:ba say:dada say:me", file=sys.stderr)
        return 1
    piping = raw_out in ("-", "/dev/stdout")
    write_wav(raw_out if piping else str(Path(raw_out)), samples)
    print(f"wrote {raw_out} ({len(samples)} samples @ 16 kHz)", file=sys.stderr)
    if piping:
        return 0
    try:
        import simpleaudio
        simpleaudio.WaveObject.from_wave_file(str(Path(raw_out))).play().wait_done()
    except Exception:
        print("(no playback stack; wav is enough)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
