#!/usr/bin/env python3
"""The Funniest Out-of-Office (make.fun). Writes the entry to /output/entry.txt."""
import os
TEXT = "I'm out of the office until Monday, teaching my inbox to fetch its own coffee. It has already filed a complaint about me."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
