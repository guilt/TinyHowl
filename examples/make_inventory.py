#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from tinyhowl.inventory import primitives, render_primitive
from tinyhowl.synth import SAMPLE_RATE, write_wav

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datasets" / "wav"

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = ["# Inventory WAV manifest", "",
            "| file | primitive | kind | place | voiced | IPA | samples |",
            "|------|-----------|------|-------|--------|-----|---------|"]
    for pr in primitives():
        samples = render_primitive(pr.name)
        dest = OUT / f"{pr.name}.wav"
        write_wav(str(dest), samples)
        rows.append(f"| `{dest.name}` | {pr.name} | {pr.kind} | {pr.place} | {str(pr.voiced).lower()} | {pr.ipa} | {len(samples)} |")
    (OUT / "MANIFEST.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"wrote {len(primitives())} wavs @ {SAMPLE_RATE} Hz -> {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
