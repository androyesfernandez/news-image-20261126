#!/usr/bin/env python3
"""news-image-20261126 entry program (Python 3.13, standard library only).

Copies the bundled poster image to the grader's output directory
(MAKEFUN_OUTPUT_DIR, else /output) as entry.png. The poster itself is a
1024x1024 broadsheet front page summing up Thursday 26 November 2026:
46 numbered stories across 7 regions, 13 drawn as scenes, a UTC timeline,
a six-numbers row, a dotted world map with numbered pins, and a red
DATE CHECK box naming the 25-Nov stories left out on purpose.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size == 0 or size > 1048576:
        print("bad output size: %d bytes" % size, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
