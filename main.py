#!/usr/bin/env python3
"""Writes the funniest toaster error message to OUTPUT_PATH.

The entry is a single original line: a deadpan appliance error with a
fresh twist -- the toaster has unionized. No bread puns, no setup, one read.
"""

import os

ENTRY = "ERROR 07: Toaster has unionized. No bread will be toasted until demands are met."

def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the gate counts characters, so write exactly the line.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
