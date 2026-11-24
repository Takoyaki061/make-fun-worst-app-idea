#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence to /output/entry.txt: a deadpan pitch for PewPilot,
an app that lets parishioners reserve their exact pew four Sundays out --
for churchgoers who cannot worship comfortably more than eleven inches
from where they sat last week. Stdlib only, deterministic.
"""

import os

TEXT = (
    "PewPilot lets parishioners reserve their exact pew four Sundays out, "
    "for churchgoers who cannot worship comfortably more than eleven inches "
    "from where they sat last week."
)


def main() -> None:
    # Gate guard, from the first local grade: the sealed scorer only
    # accepts 1-240 characters of non-whitespace UTF-8 text, so refuse
    # to write anything that would fail the gate instead of shipping it.
    text = TEXT.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, gate allows 1-240"
    assert text.count("\n") == 0, "entry must be one sentence on one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
