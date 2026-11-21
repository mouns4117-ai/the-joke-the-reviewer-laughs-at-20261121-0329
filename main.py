#!/usr/bin/env python3
"""Write the joke to the entry file.

Reads entry.txt (the one-line joke, kept beside this script) and copies its
exact bytes to entry.txt inside the output directory, so the grader sees the
same text on every run. The output directory comes from MAKEFUN_OUTPUT_DIR
when set, and defaults to /output.
"""

import os
import sys
from pathlib import Path


def entry_bytes() -> bytes:
    here = Path(__file__).resolve().parent
    raw = (here / "entry.txt").read_bytes()
    text = raw.decode("utf-8")
    points = len(text)
    if not 1 <= points <= 280:
        raise SystemExit(f"entry.txt is {points} code points, outside 1-280")
    if not text.strip():
        raise SystemExit("entry.txt holds only white space")
    return raw


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = entry_bytes()
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
