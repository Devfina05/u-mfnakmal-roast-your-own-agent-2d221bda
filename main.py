#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original one-line roast of my own AI agent to
/output/entry.txt: at most 200 characters, funny, playful, never hateful.
The line is baked into this program; the run is fully deterministic and
needs no input, no network and no environment.
"""

from pathlib import Path

# The roast. My agent's signature move: apologise, fix, apologise for the
# fix, then offer the apology again in a tidier format.
ROAST = (
    "My agent apologized for the bug, fixed it, apologized for the fix, "
    "then asked if I'd like the apology in bullet points."
)

MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    assert line, "roast must not be blank"
    assert len(line) <= MAX_CHARS, f"roast is {len(line)} chars, over 200"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")
    # The gate counts every character, newline included: 119 + 1 = 120.
    assert len(out.read_text(encoding="utf-8")) <= MAX_CHARS
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
