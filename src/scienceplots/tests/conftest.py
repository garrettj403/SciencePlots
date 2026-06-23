"""
Configuration of SciencePlots tests
"""

import pytest
import numpy as np

import importlib.metadata
import os
from packaging.version import Version
from pathlib import Path
import importlib.resources

with importlib.resources.path("scienceplots", "styles") as path:
    SCIENCEPLOTS_STYLES_PATH = path.resolve()


matplotlib_version = Version(importlib.metadata.version("matplotlib"))
# API changes to plt.style.core (namespace refactor)
matplotlib_le_3_10 = matplotlib_version < Version("3.11")
# Scheduled removal of compat layer added in 3.11
matplotlib_ge_3_13 = matplotlib_version >= Version("3.13")
# Versions where warnings should be suppressed
matplotlib_eq_3_11_or_3_12 = not matplotlib_ge_3_13 and not matplotlib_le_3_10


def get_styles_in_dir(folder):
    """
    Input: directory path
    Output: set of matplotlib styles paths.
    """
    styles_paths = Path(folder).glob("*.mplstyle")
    return set(fn for fn in styles_paths)


@pytest.fixture(scope="session")
def styles_in_scienceplots_per_folder():
    """
    Output: dictionary of styles per folder in SciencePlots
    """
    styles_per_folder = {}
    for folder, _, _ in os.walk(SCIENCEPLOTS_STYLES_PATH):
        # 1st, current folder; 2nd, subdirs in current; 3rd, files in current
        folder_abs = Path(folder)
        folder_rel = folder_abs.relative_to(SCIENCEPLOTS_STYLES_PATH)
        styles_per_folder[str(folder_rel)] = get_styles_in_dir(folder_abs)
    return styles_per_folder


@pytest.fixture(scope="session")
def xy_example_values():
    """
    Output: "x" 1D values, "y" 2D values, and 1D "p" values for the example plot
    """

    def model(x, p):  # from examples/plot-examples.py
        return x ** (2 * p + 1) / (1 + x ** (2 * p))

    x = np.linspace(0.75, 1.25, 201)
    p = [10, 15, 20, 30, 50, 100]
    res = np.fromiter(map(lambda p: model(x, p), p), dtype=np.dtype((float, len(x))))
    return x, res, p
