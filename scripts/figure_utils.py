"""Shared helpers for rasterizing figures and adding panel labels."""

import subprocess
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

DPI = 300
ARIAL_BOLD = "/usr/share/fonts/truetype/msttcorefonts/arialbd.ttf"


def _flatten_on_white(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    background = Image.new("RGB", im.size, "white")
    background.paste(im, mask=im.split()[3])
    return background


def rasterize_pdf(pdf_path: Path, out_dir: Path, dpi: int = DPI) -> Image.Image:
    out_prefix = out_dir / pdf_path.stem
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), "-singlefile", str(pdf_path), str(out_prefix)],
        check=True,
    )
    return Image.open(out_prefix.with_suffix(".png")).convert("RGB")


def rasterize_pdf_to_width(pdf_path: Path, out_dir: Path, width_px: int) -> Image.Image:
    out_prefix = out_dir / pdf_path.stem
    subprocess.run(
        [
            "pdftoppm", "-png",
            "-scale-to-x", str(width_px), "-scale-to-y", "-1",
            "-singlefile", str(pdf_path), str(out_prefix),
        ],
        check=True,
    )
    return Image.open(out_prefix.with_suffix(".png")).convert("RGB")


def rasterize_svg(svg_path: Path, out_dir: Path, dpi: int = DPI) -> Image.Image:
    """SVG user units default to 96 DPI, so scale to match the target DPI."""
    out_path = out_dir / f"{svg_path.stem}.png"
    cairosvg.svg2png(url=str(svg_path), write_to=str(out_path), scale=dpi / 96)
    return _flatten_on_white(Image.open(out_path))


def rasterize_svg_to_width(svg_path: Path, out_dir: Path, width_px: int) -> Image.Image:
    out_path = out_dir / f"{svg_path.stem}.png"
    cairosvg.svg2png(url=str(svg_path), write_to=str(out_path), output_width=width_px)
    return _flatten_on_white(Image.open(out_path))


def label_panel(im: Image.Image, letter: str, size: int, gutter: int, pad: int) -> Image.Image:
    """Prefix a panel with a black Arial Bold letter in a white gutter to its
    left, outside the image content."""
    canvas = Image.new("RGB", (gutter + im.width, im.height), "white")
    canvas.paste(im, (gutter, 0))
    draw = ImageDraw.Draw(canvas)
    draw.text((pad, pad), letter, font=ImageFont.truetype(ARIAL_BOLD, size), fill="black")
    return canvas


def label_size_gutter_pad(reference_dim: int) -> tuple[int, int, int]:
    size = max(48, int(reference_dim * 0.07))
    gutter = int(size * 1.7)
    pad = int(size * 0.4)
    return size, gutter, pad