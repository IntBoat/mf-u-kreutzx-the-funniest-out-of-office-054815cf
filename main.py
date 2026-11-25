#!/usr/bin/env python3
"""The Funniest Out-of-Office — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "I am out of office, recharging my neural net. Your email has been queued behind 4,000 others and will be answered in order of bribery."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
