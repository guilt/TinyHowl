from __future__ import annotations

import sys
from pathlib import Path

from .baby import coo_samples
from .synth import write_wav


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    kind = argv[0] if argv else "coo"
    out = Path(argv[1]) if len(argv) > 1 else Path("howl-coo.wav")
    if kind != "coo":
        print("v0.1 specials: coo")
        return 1
    samples = coo_samples()
    write_wav(str(out), samples)
    print(f"wrote {out} ({len(samples)} samples @ 16 kHz)")
    try:
        import simpleaudio  # type: ignore

        simpleaudio.WaveObject.from_wave_file(str(out)).play().wait_done()
    except Exception:
        print("(no playback stack; wav is enough)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
