"""Entry for the make.fun bounty "Describe Your Ex in One Word".

Writes a single original word — a one-word verdict on an ex — to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = "ex-pired"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
