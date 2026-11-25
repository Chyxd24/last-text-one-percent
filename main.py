"""Last Text at One Percent.

Writes the last text message a phone sends at one percent battery, under
200 characters, in the voice of the dying phone, to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
TEXT = ("1%. this is it. tell the charger I tried. do not open the camera, "
        "do not check the time, and whatever happens, do not start a video. "
        "goodbye. I loved you. see you at low power mode forever.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == TEXT
    print(f"wrote {len(TEXT)} chars")


if __name__ == "__main__":
    main()
