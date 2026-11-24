"""Dog Ate My Homework: Funniest Excuse — entry program.

Writes one original line (under 200 characters) in which a dog explains
why the homework got eaten, to /output/entry.txt.

The line: a dog takes its teacher's instruction to "digest the material"
literally, and stays proudly unrepentant about it — dog logic, twist at
the end, no embarrassment, and none of the stock lines (cat, taste of
paper, good boy).

Output contract: exactly one line of 112 characters, written as UTF-8
plus a trailing newline to /output/entry.txt. The line itself is fixed —
any change to it would change the entry, so the validations in main()
guard the format (length, single line, no surrounding whitespace, no
control characters) without ever altering the text.
"""

import hashlib
import os
import sys

LINE = (
    "The teacher said to digest the material. I took her literally, "
    "and frankly, I understood it better than you did."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"invalid line length: {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("line must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if any(ord(c) < 32 or ord(c) == 127 for c in LINE):
        print("line must not contain control characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Round-trip self-check: re-read and compare bytes.
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote /output/entry.txt ({len(LINE)} chars)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
