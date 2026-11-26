#!/usr/bin/env python3
"""The Best Advice I Ever Got (u-pangg7-the-best-advice-i-ever-got-358cefb0).

Writes a single sentence, no longer than 200 characters, about the best
advice the writer ever received, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3 standard library only; no network, no third-party packages.
The output is a fixed string, so every run is byte-identical.
"""

import os

ENTRY = (
    "My father said never borrow money to look rich, and twenty years "
    "later I still hear him every time I want something I can't afford."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    # Gate: one sentence, 1 to 200 characters, not only white space.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert not any(mark in text for mark in ("!", "?", "\n")), "entry must be one sentence"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
