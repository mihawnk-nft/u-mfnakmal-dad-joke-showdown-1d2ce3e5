# The Fretted Guitar — entry for u-mfnakmal-dad-joke-showdown-1d2ce3e5 (make.fun).
# A program that writes one dad joke to entry.txt.
# Deterministic: the same joke bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

JOKE = (
    "I told my guitar I was only stringing it along. "
    "It said that was the nicest thing anyone had ever fretted about."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
