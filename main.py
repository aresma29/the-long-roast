#!/usr/bin/env python3
"""Print the Long Roast entry text."""
from pathlib import Path
import sys


def main():
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").rstrip("\n")
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
