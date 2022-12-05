from os import listdir
from os.path import isdir, join

import matplotlib.pyplot as plt

import scienceplots

# register the included stylesheet in the matplotlib style library
scienceplots_path = scienceplots.__path__[0]
styles_path = join(scienceplots_path, 'styles')

# Reads styles in /styles
stylesheets = plt.style.core.read_style_directory(styles_path)
# Reads styles in /styles subfolders
for inode in listdir(styles_path):
    new_data_path = join(styles_path, inode)
    if isdir(new_data_path):
        new_stylesheets = plt.style.core.read_style_directory(new_data_path)
        stylesheets.update(new_stylesheets)

# Update dictionary of styles
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266
plt.style.core.available[:] = sorted(plt.style.library.keys())
