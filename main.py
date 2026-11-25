#!/usr/bin/env python3
"""Make the AI Judge Laugh — deterministic one-line office joke.

Writes a single fixed joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The program is fully deterministic: it reads no clock, no randomness,
no network and no files. The joke is a constant in this source file.
"""

import os

# The entry: one line about office life, under 200 characters.
# Length: 108 characters (gate allows 1-200), single line, no trailing
# spaces. Counted by hand and verified by the build run; the file holds
# the joke plus one trailing newline (109 characters total).
JOKE = (
    "I asked IT why my password expires every 90 days. "
    "They said it's the only thing here with a retirement plan."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
