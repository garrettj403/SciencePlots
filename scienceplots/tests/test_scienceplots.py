"""
Test suite of SciencePlots
"""

import matplotlib.pyplot as plt


def test_matplotlib_required_api_existence():
    """Check if all necessary functions and attributes are available in matplotlib."""
    assert hasattr(plt.style, "core")
    assert hasattr(plt.style.core, "read_style_directory")
    assert hasattr(plt.style.core, "update_nested_dict")
    assert hasattr(plt.style, "available")
    assert hasattr(plt.style, "library")


def test_styles_existence(styles_in_scienceplots_per_folder):
    """Check all styles are available in matplotlib."""
    for folder, styles in styles_in_scienceplots_per_folder.items():
        assert len(styles) > 0, f"No styles found in {folder}."
        for style in styles:
            assert (  # both in list of names and the library they are retrieved from
                style in plt.style.available and style in plt.style.library
            ), f"'{style}' not in available styles. Style in folder {folder}."


def test_usage_of_each_style(
    xy_example_values, styles_in_scienceplots_per_folder, tmp_path
):
    """Tests if the styles are correctly formatted and can be applied to a plot."""
    pparam = dict(xlabel="Voltage (mV)", ylabel=r"Current ($\mu$A)")
    x, ys, p = xy_example_values
    for folder, styles in styles_in_scienceplots_per_folder.items():
        for style in styles:
            output_file = tmp_path / f"test_{folder}_{style}.png"
            with plt.style.context(style):
                fig, ax = plt.subplots()
                for y in ys:
                    ax.plot(x, y)
                ax.legend(p, title="Order")
                ax.autoscale(tight=True)
                ax.set(**pparam)
                fig.tight_layout()
                fig.savefig(output_file)
