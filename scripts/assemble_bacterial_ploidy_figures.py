"""Rasterize and stitch the bacterial ploidy figures into one composite for the README.

Layout is a 4-column grid (all sources are vector, so each panel is rendered
directly at its target pixel width - no upscaling artifacts):
  row 1: A (schematic, 1 col) | empty (1 col) | B (volcano plots, 2 col)
  row 2: C (GO enrichment, 3 col)             | D (STRING network, 1 col)

Produces: assets/bacterial ploidy/bacterial_ploidy_combined.png
"""

import tempfile
from pathlib import Path

from PIL import Image

from figure_utils import (
    label_panel,
    label_size_gutter_pad,
    rasterize_pdf_to_width,
    rasterize_svg_to_width,
)

COLUMN_WIDTH = 2200
PADDING = 40
ASSETS_DIR = Path(__file__).parent.parent / "assets" / "bacterial ploidy"


def span_width(n_cols: int) -> int:
    """Pixel width of a panel spanning n_cols grid columns (gutters included)."""
    return n_cols * COLUMN_WIDTH + (n_cols - 1) * PADDING


def pack_row(images: list[Image.Image]) -> Image.Image:
    """Lay panels out left to right, top-aligned, hugging their own sizes."""
    height = max(im.height for im in images)
    width = sum(im.width for im in images) + PADDING * (len(images) - 1)
    row = Image.new("RGB", (width, height), "white")
    x = 0
    for im in images:
        row.paste(im, (x, 0))
        x += im.width + PADDING
    return row


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        schematic = rasterize_pdf_to_width(ASSETS_DIR / "schematic.pdf", tmp_dir, span_width(1))
        volcano = rasterize_pdf_to_width(ASSETS_DIR / "figure_volcano_both.pdf", tmp_dir, span_width(2))
        go_all = rasterize_pdf_to_width(ASSETS_DIR / "figure_go_all.pdf", tmp_dir, span_width(3))
        string_graphic = rasterize_svg_to_width(
            ASSETS_DIR / "string_vector_graphic.svg", tmp_dir, span_width(1)
        )

        label_size, gutter, pad = label_size_gutter_pad(
            max(schematic.height, volcano.height, go_all.height, string_graphic.height)
        )
        schematic = label_panel(schematic, "A", label_size, gutter, pad)
        volcano = label_panel(volcano, "B", label_size, gutter, pad)
        go_all = label_panel(go_all, "C", label_size, gutter, pad)
        string_graphic = label_panel(string_graphic, "D", label_size, gutter, pad)

        empty_column = Image.new("RGB", (COLUMN_WIDTH, max(schematic.height, volcano.height)), "white")

        row1 = pack_row([schematic, empty_column, volcano])
        row2 = pack_row([go_all, string_graphic])

        canvas_width = max(row1.width, row2.width)
        canvas_height = row1.height + PADDING + row2.height
        combined = Image.new("RGB", (canvas_width, canvas_height), "white")
        combined.paste(row1, ((canvas_width - row1.width) // 2, 0))
        combined.paste(row2, ((canvas_width - row2.width) // 2, row1.height + PADDING))
        combined.save(ASSETS_DIR / "bacterial_ploidy_combined.png")

        print(f"bacterial_ploidy_combined.png: {combined.size}")


if __name__ == "__main__":
    main()
