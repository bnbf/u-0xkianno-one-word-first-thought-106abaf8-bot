#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word — the first word that comes to mind —
to /output/entry.txt. The word itself is set in WORD below.
"""

import os

WORD = "petrichor"  # the smell of dry earth after rain: the first
# word that comes to mind is a sensory one — concrete, vivid, and
# surprising, not a safe abstract filler. Everyone knows the smell;
# few know it has a name, and that gap is the spark.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
