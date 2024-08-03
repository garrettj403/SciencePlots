import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt

import scienceplots

# register the bundled stylesheets in the matplotlib style library
scienceplots_path = scienceplots.__path__[0]
styles_path = os.path.join(scienceplots_path, 'styles')

# Reads styles in /styles folder and all subfolders
stylesheets = {}  # plt.style.library is a dictionary
for folder, _, _ in os.walk(styles_path):
    new_stylesheets = plt.style.core.read_style_directory(folder)
    stylesheets.update(new_stylesheets)

# Update dictionary of styles - plt.style.library
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
plt.style.core.available[:] = sorted(plt.style.library.keys())
