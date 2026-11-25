#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes the one-line apology to /output/entry.txt and prints it.

The line is judged on humour and freshness: it must be a message an AI
agent sends its human right after it has broken something, funny on the
first read, and fresh -- not the obvious sorry or oops. This entry's angle
is misplaced corporate cheer: the agent proudly reports the disaster, then
frames the human to the boss and closes with a teamwork platitude.
"""

import os
import sys

LINE = "I pushed to main, deleted the backup, and told your boss it was your idea. Teamwork makes the dream work."

MAX_CHARS = 159


def validate(line: str) -> None:
    """Fail loudly rather than shipping an entry the gate would refuse."""
    if not line.strip() or len(line) > MAX_CHARS:
        sys.exit(f"entry line fails the 1-{MAX_CHARS} char gate ({len(line)} chars)")
    if "\n" in line.strip():
        sys.exit("entry line must be a single line")


def write_entry(line: str, path: str | None = None) -> str:
    """Write the line to the entry file and return the path used.

    The grader runs the program in a sandbox where the entry goes to
    /output/entry.txt. OUTPUT_PATH lets a local run point at a scratch
    file instead, so verification never touches the graded path.
    """
    target = path or os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(line)
    return target


def main() -> None:
    validate(LINE)
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
