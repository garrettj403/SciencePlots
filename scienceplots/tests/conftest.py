"""
Configuration of SciencePlots tests
"""

import pytest
import scienceplots
import numpy as np

import os
from pathlib import Path

STYLES_PATH = Path(scienceplots.__path__[0], "styles")


def get_styles_in_dir(dir):
    """
    Input: directory path
    Output: set of matplotlib styles filenames (without trailing '.mplstyle')
    """
    styles_paths = Path(dir).glob("*.mplstyle")
    return set(fn.stem for fn in styles_paths)


@pytest.fixture(scope="session")
def styles_in_scienceplots_per_folder():
    """
    Output: dictionary of styles per folder in SciencePlots
    """
    styles_per_folder = {}
    for folder, _, _ in os.walk(STYLES_PATH):  # 1st _ : subdirs, 2nd _ : files
        folder = Path(folder)
        styles_per_folder[folder.name] = get_styles_in_dir(folder)
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
