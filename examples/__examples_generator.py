"""Generate SciencePlots sphinx-gallery examples from templates"""

from pathlib import Path

import jinja2
import scienceplots  # NOQA: F401

# Paths we will need
THIS_FILEDIR = Path(__file__).parent.resolve()
STYLES_PATH = THIS_FILEDIR.joinpath('../scienceplots/styles')
TEMPLATE_PLOT_FILE = THIS_FILEDIR.joinpath('template_plot.py.jinja2')
TEMPLATE_PLOT_SCATTER_FILE = \
    THIS_FILEDIR.joinpath('template_plot_scatter.py.jinja2')
TEMPLATE_PLOT_LANGUAGE_FILE = \
    THIS_FILEDIR.joinpath('template_plot_languages.py.jinja2')
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
# A little hack: sphinx-gallery doesn't take very well spaces in directories,
# so we later substitute the underscores before using them
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
        # Use the folder name as title for readme, so substitute underscores
        # by spaces
        readme = readme_template.render(title=folder_name.replace('_', ' '))
        with open(readme_path, mode='w') as readme_file:
            readme_file.write(readme)

# Create plot_* examples files

# This is the relevant generator of examples section
# VARIABLES REFERENCE:
#  * STYLES[key]: return set of styles (e.g. {'science', 'notebook', ...})
#    - key: 'BASE', 'COLOR', 'JOURNALS', 'LANGUAGE', 'MISCELLANEOUS'
#    - Use 'group' to select one key of above, in EXAMPLE TEMPLATE GENERATOR
#    - Use 'ignore' to leave out any of the styles
#
# TEMPLATES REFERENCE:
# * template_plot.py.jinja2 notes:
#     Input:
#        * styles: list-like (just what you would pass to plt.style.use(...))
#            Template will format the string as needed
# * template_plot_scatter.py.jinja2 notes:
#     Input:
#        * styles: list-like (same as in template_plot.py.jinja2)
# * template_README.rst.jinja2 notes:
#     Creates title for subsection in Gallery.
#     Input:
#       - title: string
# * template_plot_languages.py.jinja2 notes:
#     Input:
#       - styles: list-like (same as in template_plot.py.jinja2)
#       - legend_title: string, title for the legend
#       - xlabel: string, label for x-axis
#       - ylabel: string, label for y-axis
#
# EXAMPLE GENERATOR TEMPLATE:
# group = 'BASE'
# ignore = {'scatter'}
# n_group_examples = 0
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
# print(f'Group {group}: created {n_group_examples} examples')
# n_total_examples += n_group_examples
# END OF TEMPLATE
# See BASE Styles code for a complete pattern including ignored styles

# Read example plot_* template
with open(TEMPLATE_PLOT_FILE, mode='r') as f:
    plot_template = jinja2.Template(f.read(), keep_trailing_newline=True)

# Read example plot_scatter* template
with open(TEMPLATE_PLOT_SCATTER_FILE, mode='r') as f:
    scatter_template = jinja2.Template(f.read(), keep_trailing_newline=True)

# Read example Language_Styles/plot_* template
with open(TEMPLATE_PLOT_LANGUAGE_FILE, mode='r') as f:
    language_template = jinja2.Template(f.read(), keep_trailing_newline=True)
LANG_PARAMS = {  # Language dicts to generate examples
    'cjk-tc-font': {'legend_title': 'Order',
                    'xlabel': r'電壓 (mV)',
                    'ylabel': r'電流 ($\mu$A)'},
    'cjk-sc-font': {'legend_title': 'Order',
                    'xlabel': r'电压 (mV)',
                    'ylabel': r'电流 ($\mu$A)'},
    'cjk-jp-font': {'legend_title': 'Order',
                    'xlabel': r'電圧 (mV)',
                    'ylabel': r'電気 ($\mu$A)'},
    'cjk-kr-font': {'legend_title': 'Order',
                    'xlabel': r'전압 (mV)',
                    'ylabel': r'전류 ($\mu$A)'},
    'russian-font': {'legend_title': r'Число',
                     'xlabel': r'Напряжение (mV)',
                     'ylabel': r'Сила тока ($\mu$A)'},
    'turkish-font': {'legend_title': r'Düzen',
                     'xlabel': r'Gerilim/Volt (mV)',
                     'ylabel': r'Mevcut Güç/Akım ($\mu$A)'},
}

n_total_examples = 0

# BASE Styles
group = 'BASE'
ignore = {'scatter'}
n_group_examples = 0
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style]  # Convert each item to list (input to template)
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
# ignored styles
# Use same output folder
for style in ignore:
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = scatter_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: created {n_group_examples} examples')
n_total_examples += n_group_examples

# COLOR Styles
group = 'COLOR'
ignore = {}
n_group_examples = 0
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: created {n_group_examples} examples')
n_total_examples += n_group_examples

# JOURNALS Styles
group = 'JOURNAL'
ignore = {}
n_group_examples = 0
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: created {n_group_examples} examples')
n_total_examples += n_group_examples

# LANGUAGE Styles
group = 'LANGUAGE'
ignore = {}
n_group_examples = 0
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = language_template.render(styles=example_styles,
                                            # Unpack language strings
                                            **LANG_PARAMS[style])
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: created {n_group_examples} examples')
n_total_examples += n_group_examples

# MISCELLANEOUS Styles
group = 'MISCELLANEOUS'
ignore = {}
n_group_examples = 0
output_folder = THIS_FILEDIR.joinpath(OUTPUT_FOLDERS[group])
for style in STYLES[group]:
    if style in ignore:
        continue
    current_example_path = output_folder.joinpath('plot_' + style + '.py')
    example_styles = [style] + ['science']
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: created {n_group_examples} examples')
n_total_examples += n_group_examples

n_of_styles = sum(len(STYLES[k]) for k in STYLES.keys())
print(f'(Created examples) / (Number of Styles): '
      f'{n_total_examples} / {n_of_styles}')
