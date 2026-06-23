"""
Test SciencePlots against Matplotlib 3.11 and 3.12

Tests MPL API deprecation period after namespace changes.
Utilities are scheduled for v3.13 removal.
"""

import pytest
import matplotlib.pyplot as plt

import scienceplots
from .conftest import matplotlib_eq_3_11_or_3_12

skip_if_mpl_not_3_11_or_3_12 = pytest.mark.skipif(not matplotlib_eq_3_11_or_3_12, reason="Matplotlib 3.11 or 3.12 is not installed")


@skip_if_mpl_not_3_11_or_3_12
def test_matplotlib_3_11_required_api_existence():
    """Check if all functions and attributes used by scienceplots are available
    in matplotlib>=3.11,<3.13.
    """
    assert hasattr(plt.style, "read_style_directory")
    assert hasattr(plt.style, "update_nested_dict")
    assert hasattr(plt.style, "available")
    assert hasattr(plt.style, "library")


@skip_if_mpl_not_3_11_or_3_12
def test_styles_existence(styles_in_scienceplots_per_folder):
    """Check all styles are available in matplotlib."""
    for folder, styles in styles_in_scienceplots_per_folder.items():
        assert len(styles) > 0, f"No styles found in {folder}."
        for style in styles:
            with plt.style.context(scienceplots.styles([style.stem])):
                pass


@skip_if_mpl_not_3_11_or_3_12
def test_usage_of_each_style(
    xy_example_values, styles_in_scienceplots_per_folder, tmp_path,
):
    """Tests if the styles are correctly formatted and can be applied to a plot."""
    pparam = {"xlabel": "Voltage (mV)", "ylabel": r"Current ($\mu$A)"}
    x, ys, p = xy_example_values
    for folder, styles in styles_in_scienceplots_per_folder.items():
        folder = folder.replace("/", "_").replace("\\", "_")  # Fix accessing styles subfolders
        for style in styles:
            output_file = tmp_path / f"test_{folder}_{style.stem}.png"
            with plt.style.context(style):
                fig, ax = plt.subplots()
                for y in ys:
                    ax.plot(x, y)
                ax.legend(p, title="Order")
                ax.set(**pparam)
                ax.autoscale(tight=True)
                fig.savefig(output_file)
                plt.close(fig)
