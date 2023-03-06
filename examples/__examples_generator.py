"""Generate SciencePlots sphinx-gallery examples from templates"""

import os
from pathlib import Path

import jinja2
import scienceplots

# Paths we will need
THIS_FILEPATH = Path(__file__).parent.resolve()
STYLES_PATH = THIS_FILEPATH.joinpath('..\\scienceplots\\styles')
TEMPLATE_PLOT_FILE = THIS_FILEPATH.joinpath('template_plot.py.jinja2')
TEMPLATE_README_FILE = THIS_FILEPATH.joinpath('template_README.rst.jinja2')

def get_styles_names_list_in(dir):
    """
    Input: directory path
    Output: set of matplotlib styles filenames (without trailing '.mplstyle')
    """
    styles_paths = set(Path(dir).glob('*.mplstyle'))
    return set(fn.stem for fn in styles_paths)

# Styles per category / folder
STYLES = {
    'BASE': get_styles_names_list_in(STYLES_PATH),
    'COLOR': get_styles_names_list_in(STYLES_PATH.joinpath('color')),
    'JOURNAL': get_styles_names_list_in(STYLES_PATH.joinpath('journals')),
    'LANGUAGE': get_styles_names_list_in(STYLES_PATH.joinpath('languages')),
    'MISCELLANEOUS': get_styles_names_list_in(STYLES_PATH.joinpath('misc'))
}
# Output example folders in ./examples
OUTPUT_FOLDERS = { k: '_'.join([k, 'styles']).title()
                   for k in STYLES.keys() }

# Initialize examples subfolders and readmes
# Read README template
with open(TEMPLATE_README_FILE, mode='r') as f:
    readme_template = jinja2.Template(f.read(), keep_trailing_newline=True)

for folder_name in OUTPUT_FOLDERS.values():
    # Create subfolder
    output_folder = THIS_FILEPATH.joinpath(folder_name)
    if not output_folder.exists():
        output_folder.mkdir()
    # Create README.rst from template
    readme_path = output_folder.joinpath('README.rst')
    if not readme_path.exists():
        readme = readme_template.render(title = folder_name.replace('_', ' '))
        with open(readme_path, mode='w') as readme_file:
            readme_file.write(readme)

# Create plot_* examples files
# Read example plot_* template
with open(TEMPLATE_PLOT_FILE, mode='r') as f:
    example_template = jinja2.Template(f.read(), keep_trailing_newline=True)

#! This is the relevant generator section
# Variables reference used here:
#   * STYLES[key]: return set of styles (e.g. {'science', ...})
#     - key: 'BASE', 'COLOR', 'JOURNALS', 'LANGUAGES', 'MISCELLANEOUS'
#
# template_plot.py.jinja2 notes:
#   Only one parameter is needed:
#      * styles: list-like (just what you would pass to plt.style.use(...))
#         Template will format the string as needed

# BASE Styles
group = 'BASE'
output_folder = THIS_FILEPATH.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style]
    example_text = example_template.render(styles = example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# COLOR Styles
group = 'COLOR'
output_folder = THIS_FILEPATH.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = example_template.render(styles = example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# JOURNALS Styles
group = 'JOURNAL'
output_folder = THIS_FILEPATH.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = example_template.render(styles = example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# MISCELLANEOUS Styles
group = 'MISCELLANEOUS'
output_folder = THIS_FILEPATH.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = example_template.render(styles = example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# # LANGUAGES Styles TODO:WIP
# group = 'LANGUAGES'
# output_folder = THIS_FILEPATH.joinpath(OUTPUT_FOLDERS[group])
# for style in STYLES[group]:
#     current_example_path = output_folder.joinpath('plot_' + style + '.py')
#     example_styles = [style] + ['science']
#     # Style is a string, so we must put it between \' to work
#     style_quoted = "'" + style + "'"
#     example_text = example_template.render(styles = example_styles)
#     with current_example_path.open('w') as example:
#         example.write(example_text)
