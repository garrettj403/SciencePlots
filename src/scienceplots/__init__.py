import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt

import scienceplots
from .styles_discovery import read_styles_in_folders

# register the bundled stylesheets in the matplotlib style library
scienceplots_path = scienceplots.__path__[0]
styles_path = os.path.join(scienceplots_path, "styles")

# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Update dictionary of styles - plt.style.library
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
plt.style.core.available[:] = sorted(plt.style.library.keys())
