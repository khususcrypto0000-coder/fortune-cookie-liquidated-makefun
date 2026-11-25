"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line to /output/entry.txt (UTF-8, no trailing
newline), then reads it back and asserts it is byte-identical.
Stdlib only.
"""

import os
import sys

ENTRY = "The stars foretell great wealth in your future \u2014 they simply decline to say whose future, or when."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    # Gate guards: plain-text fortune, 1-160 chars, at most 20 words.
    assert text.strip(), "entry must not be whitespace only"
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert len(text.split()) <= 20, "entry must be at most 20 words"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "round-trip mismatch"
    assert not data.endswith(b"\n"), "no trailing newline"
    print("wrote %s (%d chars, %d words)"
          % (OUTPUT_PATH, len(text), len(text.split())))


if __name__ == "__main__":
    main()
