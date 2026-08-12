"""Rasterize breast cancer subtype PDFs and compose README figures.

Produces:
  - assets/breast cancer subtypes/splsda_combined.png
      splsda_3D_plots.pdf + splsda_corr_circle.pdf side by side, native scale.
  - assets/breast cancer subtypes/shap_value_plot.png
      shap_value_plot.pdf rasterized on its own.
"""

import tempfile
from pathlib import Path

from PIL import Image

from figure_utils import label_panel, label_size_gutter_pad, rasterize_pdf

PADDING = 40
ASSETS_DIR = Path(__file__).parent.parent / "assets" / "breast cancer subtypes"


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        splsda_3d = rasterize_pdf(ASSETS_DIR / "splsda_3D_plots.pdf", tmp_dir)
        corr_circle = rasterize_pdf(ASSETS_DIR / "splsda_corr_circle.pdf", tmp_dir)
        shap = rasterize_pdf(ASSETS_DIR / "shap_value_plot.pdf", tmp_dir)

        shap.save(ASSETS_DIR / "shap_value_plot.png")

        row_height = max(splsda_3d.height, corr_circle.height)
        label_size, gutter, pad = label_size_gutter_pad(row_height)

        splsda_3d = label_panel(splsda_3d, "A", label_size, gutter, pad)
        corr_circle = label_panel(corr_circle, "B", label_size, gutter, pad)

        combined_width = splsda_3d.width + PADDING + corr_circle.width
        combined_height = row_height

        combined = Image.new("RGB", (combined_width, combined_height), "white")
        combined.paste(splsda_3d, (0, 0))
        combined.paste(corr_circle, (splsda_3d.width + PADDING, 0))
        combined.save(ASSETS_DIR / "splsda_combined.png")

        print(f"shap_value_plot.png: {shap.size}")
        print(f"splsda_combined.png: {combined.size}")


if __name__ == "__main__":
    main()