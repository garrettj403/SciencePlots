"""Generate SciencePlots sphinx-gallery examples from templates"""

from pathlib import Path

import jinja2
import scienceplots  # NOQA: F401

# Paths we will need
THIS_FILEDIR = Path(__file__).parent.resolve()
STYLES_PATH = THIS_FILEDIR.joinpath('..\\scienceplots\\styles')
TEMPLATE_PLOT_FILE = THIS_FILEDIR.joinpath('template_plot.py.jinja2')
TEMPLATE_PLOT_SCATTER_FILE = \
    THIS_FILEDIR.joinpath('template_plot_scatter.py.jinja2')
TEMPLATE_README_FILE = THIS_FILEDIR.joinpath('template_README.rst.jinja2')


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
OUTPUT_FOLDERS = {k: '_'.join([k, 'styles']).title()
                  for k in STYLES.keys()}

# Initialize examples subfolders and readmes
# Read README template
with open(TEMPLATE_README_FILE, mode='r') as f:
    readme_template = jinja2.Template(f.read(), keep_trailing_newline=True)

for folder_name in OUTPUT_FOLDERS.values():
    # Create subfolder
    output_folder = THIS_FILEDIR.joinpath(folder_name)
    if not output_folder.exists():
        output_folder.mkdir()
    # Create README.rst from template
    readme_path = output_folder.joinpath('README.rst')
    if not readme_path.exists():
        readme = readme_template.render(title=folder_name.replace('_', ' '))
        with open(readme_path, mode='w') as readme_file:
            readme_file.write(readme)

# Create plot_* examples files

# This is the relevant generator of examples section
# VARIABLES REFERENCE:
#  * STYLES[key]: return set of styles (e.g. {'science', 'notebook', ...})
#    - key: 'BASE', 'COLOR', 'JOURNALS', 'LANGUAGES', 'MISCELLANEOUS'
#    - Use 'group' to select one key of above, in EXAMPLE TEMPLATE GENERATOR
#    - Use 'ignore' to leave out any of the styles
#
# TEMPLATES REFERENCE:
# * template_plot.py.jinja2 notes:
#     Only one parameter is needed:
#        * styles: list-like (just what you would pass to plt.style.use(...))
#         Template will format the string as needed
# * template_plot_scatter.py.jinja2 notes:
#     Same input as above (template_plot.py.jinja2)
# * template_README.rst.jinja2 notes:
#     Creates title for subsection in Gallery.
#     Input:
#       -
# EXAMPLE GENERATOR TEMPLATE:
# group = 'BASE'
# ignore = {'scatter'}
# output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
# for style in STYLES[group]:
#     if style in ignore:
#         continue
#     current_example_path = output_folder.joinpath('plot_' + style + '.py')
#     # Convert style to list (input to template)
#     example_styles = [style]
#     example_text = plot_template.render(styles=example_styles)
#     with current_example_path.open('w') as example:
#         example.write(example_text)
# END OF TEMPLATE
# See BASE Styles code for a complete pattern including ignored styles

# Read example plot_* template
with open(TEMPLATE_PLOT_FILE, mode='r') as f:
    plot_template = jinja2.Template(f.read(), keep_trailing_newline=True)

# Read example plot_scatter* template
with open(TEMPLATE_PLOT_SCATTER_FILE, mode='r') as f:
    scatter_template = jinja2.Template(f.read(), keep_trailing_newline=True)


# BASE Styles
group = 'BASE'
ignore = {'scatter'}
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style]  # Convert each item to list (input to template)
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)
# ignored styles
# Uses same output folder
for style in ignore:
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = scatter_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# COLOR Styles
group = 'COLOR'
ignore = {}
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# JOURNALS Styles
group = 'JOURNAL'
ignore = {}
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# MISCELLANEOUS Styles
group = 'MISCELLANEOUS'
ignore = {}
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)

# # LANGUAGES Styles TODO: WIP
# group = 'LANGUAGES'
# ignore = {}
# output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
# for style in STYLES[group]:
#     if style in ignore:
#         continue
#     current_example_path = output_folder.joinpath('plot_' + style + '.py')
#     example_styles = [style] + ['science']
#     # Style is a string, so we must put it between \' to work
#     style_quoted = "'" + style + "'"
#     example_text = plot_template.render(styles=example_styles)
#     with current_example_path.open('w') as example:
#         example.write(example_text)
