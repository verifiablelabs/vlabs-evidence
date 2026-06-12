"""CI gate: every evidence artifact must be synthetic/redacted and secret-free."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRET = re.compile(r"sk-or-v1-[A-Za-z0-9]|AKIA[0-9A-Z]{16}|xox[baprs]-")
MARKERS = ("illustrative", "synthetic", "redacted")


def main() -> int:
    bad: list[str] = []
    for p in sorted((ROOT / "evidence").rglob("*")):
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if SECRET.search(text):
            bad.append(f"{p}: secret-shaped string")
        if not any(m in text.lower() for m in MARKERS):
            bad.append(f"{p}: missing illustrative/synthetic/redacted marker")
        if p.suffix == ".json":
            try:
                json.loads(text)
            except ValueError as e:
                bad.append(f"{p}: invalid JSON ({e})")
    for b in bad:
        print("FAIL:", b)
    print("OK: all evidence artifacts synthetic/redacted" if not bad else f"{len(bad)} violation(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
