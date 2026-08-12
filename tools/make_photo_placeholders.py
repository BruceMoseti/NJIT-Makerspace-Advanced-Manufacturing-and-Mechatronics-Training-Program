#!/usr/bin/env python3
"""Generate placeholder images for the gallery so the docs render before the
real photographs are added. Overwrite any file in images/ with the real photo of
the same name; nothing else needs to change.

Usage: python3 tools/make_photo_placeholders.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SIZE = (1200, 900)
BACKGROUND = (238, 240, 243)
BORDER = (203, 209, 217)
TITLE_COLOR = (36, 41, 47)
BODY_COLOR = (101, 109, 118)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
TITLE_FONT = FONT_DIR / "DejaVuSans-Bold.ttf"
BODY_FONT = FONT_DIR / "DejaVuSans.ttf"

PHOTOS = {
    "test-stand-front-assembly.jpg": "Completed motor test stand, front view",
    "test-stand-frame-motor-mount.jpg": "T-slot frame and motor mount",
    "test-stand-ac-enclosure-breaker.jpg": "AC enclosure: breaker and terminal blocks",
    "test-stand-24vdc-power-supply.jpg": "24 VDC DIN-rail power supply",
    "test-stand-dc-panel-lamps.jpg": "DC operator panel: switches and pilot lamps",
    "test-stand-dc-panel-rear.jpg": "Rear 24 VDC distribution terminal blocks",
    "plc-trainer-and-logic.jpg": "Micro820 trainer and basic ladder logic",
    "plc-adder-function-block.jpg": "ADD function block: 100.0 + 200.0 = 300.0",
    "plc-counter-timer-download.jpg": "CTU counter and LIMIT block, downloaded",
    "plc-local-variables-table.jpg": "CCW Local Variables table",
    "breadboard-analog-circuit.jpg": "Bench breadboard analog circuit",
    "arduino-breadboard-circuit.jpg": "Arduino Uno breadboard circuit",
    "pneumatics-frl-blowgun.jpg": "Pneumatic FRL, ball valve and blow gun",
    "electronics-component-kit.jpg": "Electronics component and jumper kit",
}


def load_font(path: Path, size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype(str(path), size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, font, max_width):
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=font) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def build(path: Path, caption: str) -> None:
    image = Image.new("RGB", SIZE, BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.rectangle([(24, 24), (SIZE[0] - 25, SIZE[1] - 25)], outline=BORDER, width=3)

    title_font = load_font(TITLE_FONT, 46)
    body_font = load_font(BODY_FONT, 30)
    name_font = load_font(BODY_FONT, 26)

    max_width = SIZE[0] - 200
    lines = wrap(draw, caption, title_font, max_width)
    line_height = 62
    block_height = len(lines) * line_height + 130
    y = (SIZE[1] - block_height) // 2

    for line in lines:
        width = draw.textlength(line, font=title_font)
        draw.text(((SIZE[0] - width) / 2, y), line, font=title_font, fill=TITLE_COLOR)
        y += line_height

    y += 34
    note = "Photograph pending — replace this file with the photo"
    width = draw.textlength(note, font=body_font)
    draw.text(((SIZE[0] - width) / 2, y), note, font=body_font, fill=BODY_COLOR)

    y += 48
    width = draw.textlength(path.name, font=name_font)
    draw.text(((SIZE[0] - width) / 2, y), path.name, font=name_font, fill=BODY_COLOR)

    image.save(path, "JPEG", quality=82, optimize=True)


def main() -> None:
    target = Path(__file__).resolve().parent.parent / "images"
    target.mkdir(parents=True, exist_ok=True)
    for filename, caption in PHOTOS.items():
        build(target / filename, caption)
        print(f"wrote images/{filename}")


if __name__ == "__main__":
    main()
