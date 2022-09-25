from os import listdir
from os.path import isdir, join

import matplotlib.pyplot as plt

import pkg_resources

# register the included stylesheet in the matplotlib style library
# TODO: migrate to importlib_resources when possible
data_path = pkg_resources.resource_filename('SciencePlots', 'styles/')
stylesheets = plt.style.core.read_style_directory(data_path) # Reads styles in /styles
# Reads styles in /styles subfolders
for inode in listdir(data_path):
    new_data_path = join(data_path, inode)
    if isdir(new_data_path):
        new_stylesheets = plt.style.core.read_style_directory(new_data_path)
        stylesheets.update(new_stylesheets)
# Update dictionary of styles
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
