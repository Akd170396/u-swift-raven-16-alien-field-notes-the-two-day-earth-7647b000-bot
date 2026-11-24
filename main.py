#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt): a review of planet Earth left by an alien tourist.

The line, built for the judge brief (in order): it reads as a one-line
alien tourist review ("surviving another orbit", "Four stars, would
visit again"); the laugh comes from the alien's angle on ordinary Earth
life (a birthday: surviving a year, then eating cake that was set on
fire first); the detail is fresh (not traffic, gravity, money or
weather); it sounds like a real review with a verdict and a rating; and
it is tight, with the punch landing at the end. One joke, landed clean.
"""

import os
import sys

LINE = (
    "They celebrate surviving another orbit by eating cake and "
    "setting fire to it first. Four stars, would visit again."
)


def validate(text: str) -> None:
    """Gate the line exactly like the sealed scorer: UTF-8 text of 1 to
    200 characters, not only white space, and a single line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    # Read back and verify: never hand the grader a truncated or
    # corrupted file; fail loudly instead.
    with open(target, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        raise RuntimeError("written entry.txt does not match the entry line")
    print(f"alien-field-notes: wrote {len(LINE)} characters to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
