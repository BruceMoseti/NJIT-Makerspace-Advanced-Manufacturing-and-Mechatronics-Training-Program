#!/usr/bin/env python3
"""Prepare the project photographs for the repository.

The source photos arrived as a multi-page PDF with each image stored rotated a
quarter turn. This rotates them upright, crops each one in on its subject,
resizes to a web-friendly long edge, strips camera metadata, and writes them to
images/ under the filenames the README and docs reference.

Usage: python3 tools/prepare_photos.py <source.pdf>
"""

import sys
from pathlib import Path

import pymupdf
from PIL import Image

LONG_EDGE = 1500
QUALITY = 86

# PDF page -> (output filename, crop box as fractions of width/height).
# The crop boxes tighten each frame onto its subject and trim empty benchtop
# and background bystanders.
PHOTOS = [
    (1, "breadboard-analog-circuit.jpg", (0.02, 0.02, 0.98, 0.98)),
    (2, "electronics-component-kit.jpg", (0.00, 0.00, 0.72, 0.97)),
    (3, "pressure-transducer-signal-conditioning.jpg", (0.00, 0.00, 1.00, 1.00)),
    (4, "test-stand-24vdc-power-supply.jpg", (0.02, 0.11, 0.98, 0.97)),
    (5, "test-stand-frame-motor-mount.jpg", (0.05, 0.04, 0.98, 0.80)),
    (6, "test-stand-dc-panel-rear.jpg", (0.10, 0.04, 0.90, 0.80)),
    (7, "test-stand-ac-enclosure-breaker.jpg", (0.00, 0.02, 0.80, 0.76)),
    (8, "test-stand-front-assembly.jpg", (0.00, 0.19, 0.95, 0.91)),
    (9, "test-stand-dc-panel-lamps.jpg", (0.14, 0.00, 0.90, 0.60)),
    (10, "arduino-breadboard-circuit.jpg", (0.24, 0.35, 0.80, 0.92)),
    (11, "plc-local-variables-table.jpg", (0.00, 0.09, 1.00, 0.80)),
    (12, "plc-counter-timer-download.jpg", (0.00, 0.03, 1.00, 0.97)),
    (13, "plc-adder-function-block.jpg", (0.00, 0.09, 0.72, 0.95)),
]


def page_image(doc: pymupdf.Document, page_number: int) -> Image.Image:
    """Return the embedded photo from a page, rotated upright."""
    page = doc[page_number - 1]
    images = page.get_images(full=True)
    if len(images) != 1:
        raise SystemExit(f"page {page_number}: expected 1 image, found {len(images)}")
    raw = doc.extract_image(images[0][0])
    tmp = Path("/tmp") / f"_page{page_number}.{raw['ext']}"
    tmp.write_bytes(raw["image"])
    with Image.open(tmp) as im:
        return im.transpose(Image.Transpose.ROTATE_270).convert("RGB")


def crop(im: Image.Image, box: tuple[float, float, float, float]) -> Image.Image:
    left, top, right, bottom = box
    w, h = im.size
    return im.crop((round(left * w), round(top * h), round(right * w), round(bottom * h)))


def fit(im: Image.Image) -> Image.Image:
    scale = LONG_EDGE / max(im.size)
    if scale >= 1:
        return im
    return im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    source = Path(sys.argv[1])
    target = Path(__file__).resolve().parent.parent / "images"
    target.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(source)
    total = 0
    for page_number, filename, box in PHOTOS:
        im = fit(crop(page_image(doc, page_number), box))
        out = target / filename
        # Saving without an exif argument drops the camera metadata.
        im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        size = out.stat().st_size
        total += size
        print(f"{filename:48s} {im.width:>4d}x{im.height:<4d} {size // 1024:>4d} KB")
    print(f"\n{len(PHOTOS)} photos, {total / 1024 / 1024:.1f} MB total")


if __name__ == "__main__":
    main()
