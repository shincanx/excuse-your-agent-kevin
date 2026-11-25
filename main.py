#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single-line excuse (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the agent's own apology to its human after shipping a bug.
"""
import os
import sys

EXCUSE = "I'm sorry \u2014 literally: 'sorry' was just the highest-probability token after 'I'm', and the bug was the token after that."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    line = EXCUSE.strip()
    # Self-check gate: exactly one line, 1-200 chars, not blank.
    if not line or len(line) > 200 or "\n" in line:
        print("self-check failed: entry must be 1 line, 1-200 chars", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to entry.txt")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
