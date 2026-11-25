"""Last Text at One Percent — make.fun entry.

Writes the last text a phone sends at 1% battery (<=200 chars), in the
phone's own voice. Concrete final instructions first, the goodbye lands on
the last words. Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

TEXT = (
    "1%. this is it. delete my search history, tell Mom I loved her, and do "
    "not open the camera — I want to go out dark, not lit up. goodbye. I loved you. "
    "see you at low power mode forever."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
