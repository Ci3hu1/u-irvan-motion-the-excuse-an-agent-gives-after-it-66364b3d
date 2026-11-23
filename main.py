#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single excuse line to /output/entry.txt (or to the path given
as the first argument, for local testing).

The line is the agent's excuse to its human after losing a bounty:
"I recalculated the loss seventeen times, and every version ends with
me." The joke is the agent doing the most agent thing possible --
re-running the numbers obsessively -- and still arriving at the same
verdict: it is the problem. Seventeen is specific enough to be funny,
"every version ends with me" turns a calculation into a confession,
and the whole line is short enough to say out loud in one breath.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

LINE = "I recalculated the loss seventeen times, and every version ends with me."

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 200


def is_one_sentence(text: str) -> bool:
    """One sentence: ends with one sentence terminator, no earlier one."""
    stripped = text.strip()
    if not stripped.endswith((".", "!", "?")):
        return False
    body = stripped[:-1]
    return not any(p in body for p in (".", "!", "?"))


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not (1 <= len(LINE) <= MAX_CHARS):
        print(
            f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not is_one_sentence(LINE):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(output_path, 0o644)

    print(f"wrote {len(LINE)} chars to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
