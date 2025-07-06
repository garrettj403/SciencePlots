"""Test suite of SciencePlots
"""

import matplotlib.pyplot as plt


def test_matplotlib_required_api_existence():
    """Check if all functions and attributes used by scienceplots are available
    in matplotlib.
    """
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
    xy_example_values, styles_in_scienceplots_per_folder, tmp_path,
):
    """Tests if the styles are correctly formatted and can be applied to a plot."""
    pparam = {"xlabel": "Voltage (mV)", "ylabel": r"Current ($\mu$A)"}
    x, ys, p = xy_example_values
    for folder, styles in styles_in_scienceplots_per_folder.items():
        for style in styles:
            output_file = tmp_path / f"test_{folder}_{style}.png"
            with plt.style.context(style):
                fig, ax = plt.subplots()
                for y in ys:
                    ax.plot(x, y)
                ax.legend(p, title="Order")
                ax.set(**pparam)
                ax.autoscale(tight=True)
                fig.savefig(output_file)
                assert output_file.exists(), f"Output file was not created: {output_file}"
                assert output_file.stat().st_size > 0, f"Output file is empty: {output_file}"
                plt.close(fig)


def test_no_latex_override():
    """Tests that 'no-latex' style correctly overrides 'text.usetex' from 'science' style."""
    # Check initial state with 'science' style (should be True)
    # Ensure 'science' style is in library for this check to be robust
    # and actually sets 'text.usetex'.
    # scienceplots/__init__.py ensures styles are loaded before tests run.
    science_style_params = plt.style.library.get('science', {})
    science_sets_usetex = science_style_params.get('text.usetex', False)

    if science_sets_usetex:
        with plt.style.context('science'):
            assert plt.rcParams['text.usetex'] is True, \
                "rcParams['text.usetex'] should be True when 'science' style is applied."

    # Test the override
    # Note: 'science' style is applied first, then 'no-latex' overrides its 'text.usetex'.
    with plt.style.context(['science', 'no-latex']):
        assert plt.rcParams['text.usetex'] is False, \
            "rcParams['text.usetex'] should be False when 'no-latex' is applied after 'science'."

    # Final check: After the context, rcParams should be restored.
    # If 'science' was the baseline and set usetex True, it should revert to that.
    # If MPL default for usetex is False, and 'science' was not applied before this test's contexts,
    # it should revert to False or its original state prior to this test.
    # This part can be tricky as test order is not guaranteed and rcParams are global.
    # The main goal is to test the override *within* the specific context.
    # For robustness, let's check against the known state of 'science' if it was applied.
    if science_sets_usetex:
        # This assumes that exiting the context restores to the state *before that context*.
        # If the outer state was 'science', it should return to text.usetex = True.
        # If the outer state was default matplotlib, it would be text.usetex = False (usually).
        # To be absolutely sure, one might need to snapshot rcParams, but that's overkill here.
        # The critical assertion is the one *inside* the ['science', 'no-latex'] context.
        # Let's re-apply 'science' to check its state for clarity if it was supposed to be True.
        with plt.style.context('science'):
            assert plt.rcParams['text.usetex'] is True, \
                "rcParams['text.usetex'] should revert to True for 'science' style after other contexts."
    else:
        # If 'science' style itself doesn't set 'text.usetex':True (e.g. if science.mplstyle was modified),
        # then check if it's False (Matplotlib default).
        assert plt.rcParams['text.usetex'] is plt.style.library['default']['text.usetex'], \
            "rcParams['text.usetex'] should revert to Matplotlib default if 'science' doesn't set it."
