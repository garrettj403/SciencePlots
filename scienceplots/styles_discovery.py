import os

import matplotlib.pyplot as plt


def read_styles_in_folders(root_path):
    """
    Reads all stylesheets in the given path and its subfolders.

    Parameters
    ----------
    root_path : str
        Path to the root folder containing the stylesheets and other subfolders
        with stylesheets.

    Returns
    -------
    stylesheets : dict
        Dictionary of stylesheets in the form of {style_name: rcParams}.
        Should be compatible with matplotlib's plt.style.library dictionary.
    """
    stylesheets = {}  # plt.style.library is a dictionary
    for folder, _, _ in os.walk(root_path):
        new_stylesheets = plt.style.core.read_style_directory(folder)
        stylesheets.update(new_stylesheets)
    return stylesheets
