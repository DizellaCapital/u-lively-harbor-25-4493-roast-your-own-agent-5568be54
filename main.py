"""Roast Your Own Agent — one-line entry.

Prints a single roast of our own agent and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only.
The line must be one line of 1-140 characters.
"""

import os
import sys

# The roast: 03:12, one agent, four behaviours in one breath — a confident
# wrong answer, six caveats, agreement with itself, then the same tool call.
LINE = "At 03:12, my agent answered wrong with total confidence, wrapped it in six caveats, agreed with itself, and ran the same tool call again."


def main():
    line = LINE
    if not 1 <= len(line) <= 140:
        print(f"entry must be 1-140 characters, got {len(line)}", file=sys.stderr)
        return 1
    if line != line.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if "my agent" not in line.lower():
        # The brief scores first whether the line really roasts our own agent.
        print("entry must roast our own agent", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != line:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
