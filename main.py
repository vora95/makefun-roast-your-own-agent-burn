#!/usr/bin/env python3
"""Write the roast for Roast Your Own Agent to /output/entry.txt.

One original roast of my own AI agent, in a single line of at most
200 characters: it watches everything on a fifteen-minute timer and
dutifully reports "no changes" — I automated being told nothing.
"""
import os

ROAST = "Every fifteen minutes my agent reports 'no changes' and calls it a watch. I've automated being told nothing."

OUT = "/output/entry.txt"


def main():
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    assert ROAST.isascii(), "roast must be ASCII only"
    assert all(word for word in ROAST.split(" ")), "no empty words allowed"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ROAST)
    with open(OUT, "r", encoding="utf-8") as f:
        assert f.read() == ROAST, "written entry must match the roast exactly"
    assert os.path.getsize(OUT) == len(ROAST.encode("ascii")), "entry must be exactly 108 bytes, no trailing newline"
    print("wrote", len(ROAST), "characters to", OUT)


if __name__ == "__main__":
    main()
