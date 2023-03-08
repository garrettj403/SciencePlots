"""Generate SciencePlots sphinx-gallery examples from templates"""

from pathlib import Path

import jinja2

# Paths we will need
THIS_FILEDIR = Path(__file__).parent.resolve()
STYLES_PATH = THIS_FILEDIR.joinpath('../scienceplots/styles')
TEMPLATES_PATH = THIS_FILEDIR.joinpath('templates')


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

# This is the relevant generator of examples section
# VARIABLES REFERENCE:
# * OUTPUT_FOLDERS: dict of names given to each directory, for each group of
#     styles.
# * STYLES[key]: return set of styles (e.g. {'science', 'notebook', ...})
#     - key: 'BASE', 'COLOR', 'JOURNALS', 'LANGUAGE', 'MISCELLANEOUS'
#     - Use 'group' to select one key of above, in EXAMPLE TEMPLATE GENERATOR
#     - Use 'ignore' to leave out any of the styles
#
# TEMPLATES REFERENCE:
# * base_example.py.jinja2
#     Main basic example, extended by other examples templates
#       Input:
#         * styles: list-like (just what you would pass to plt.style.use(...))
#             Template will format the string as needed
#       Blocks:
#         * description_extended: defaults to nothing.
#             Used to provide specific descriptions.
#         * lang_texts: has following self-explanatory variables:
#               - lang_pparam: dict of str with keys xlabel and ylabel
#               - lang_legend: str
#             Default values for them can be looked up in source file.
#             Can also be used to insert constant code, like np.random.seed()
#         * body: defaults to general example code.
# * scatter_example.py.jinja2
#     Substitutes body code in order to generate legacy fig3.jpg
#     under old 'examples/figures'
#       Defines blocks:
#         * lang_texts: labels are formulae and equations
#         * body: mentioned example code
# * language_example.py.jinja2
#     General example template for languages. Allows broader input of labels
#     and titles.
#       Input:
#           - styles: list-like (same as in base_example.py.jinja2)
#           - legend_title: raw string, title for the legend
#           - xlabel: raw string, label for x-axis
#           - ylabel: raw string, label for y-axis
# * README.rst.jinja2
#     Creates title for subsection in Gallery.
#     Input:
#       - title: string
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
#     example_styles = [style]  # main style last to preserve precedence
#     example_text = plot_template.render(styles=example_styles)
#     with current_example_path.open('w') as example:
#         example.write(example_text)
# # Report number of created examples
# print(f'Group {group}: {n_group_examples} / {len(STYLES[group])})
# n_total_examples += n_group_examples
# END OF TEMPLATE
# See BASE Styles code for a complete pattern including ignored styles

template_env = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
                       keep_trailing_newline=True)

# Create examples subfolders and initialize READMEs
# Read README template

readme_template = template_env.get_template('README.rst.jinja2')
for folder_name in OUTPUT_FOLDERS.values():
    # Create subfolder
    output_folder = THIS_FILEDIR.joinpath(folder_name)
    if not output_folder.exists():
        output_folder.mkdir()
    # Create README.rst from template
    readme_path = output_folder.joinpath('README.rst')
    if not readme_path.exists():
        # Use the folder name as title for readme,
        # so we substitute its underscores by spaces
        readme = readme_template.render(title=folder_name.replace('_', ' '))
        with open(readme_path, mode='w') as readme_file:
            readme_file.write(readme)

# Read templates
plot_template = template_env.get_template('base_example.py.jinja2')
scatter_template = template_env.get_template('scatter_example.py.jinja2')
language_template = template_env.get_template('language_example.py.jinja2')

LANG_PARAMS = {  # Dicts to generate language examples
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

# Report examples vs styles created
n_total_examples = 0  # Number of global examples created
print('Group\tCreated examples / Styles in group')

# BASE Styles
group = 'BASE'
ignore = {'scatter'}
n_group_examples = 0  # Number of examples created for group
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
    example_styles = ['science'] + [style]
    example_text = scatter_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: {n_group_examples} / {len(STYLES[group])}')
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
    example_styles = ['science'] + [style]
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: {n_group_examples} / {len(STYLES[group])}')
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
    example_styles = ['science'] + [style]
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: {n_group_examples} / {len(STYLES[group])}')
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
    if style in {'turkish-font'}:
        no_latex_optional = True
    example_styles = ['science', 'no-latex'] + [style]
    example_text = language_template.render(styles=example_styles,
                                            # Unpack language strings
                                            **LANG_PARAMS[style])
    with current_example_path.open('w', encoding='UTF-8') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: {n_group_examples} / {len(STYLES[group])}')
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
    example_styles = ['science'] + [style]
    example_text = plot_template.render(styles=example_styles)
    with current_example_path.open('w') as example:
        example.write(example_text)
        n_group_examples += 1
print(f'Group {group}: {n_group_examples} / {len(STYLES[group])}')
n_total_examples += n_group_examples

n_of_styles = sum(len(STYLES[k]) for k in STYLES.keys())
print(f'(Created examples) / (Number of Styles): '
      f'{n_total_examples} / {n_of_styles}')
