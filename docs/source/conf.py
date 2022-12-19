# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SciencePlots'
copyright = '2022, John D. Garrett'
author = 'John D. Garrett'
release = '2.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = []

# External links aliases
repo_base_link = 'https://github.com/garrettj403/SciencePlots/'
extlinks = {
    'ghissue': (repo_base_link + 'issues/%s', 'issue %s'),
    'ghpull': (repo_base_link + 'pull/%s', 'pull request '),
    'ghwiki': (repo_base_link + 'wiki/%s', 'wiki '),
    'ghuser': ('https://github.com/%s', '@'),
    'doi': ('http://doi.org/%s', 'DOI: ')
}
# Warn replaceable hardcoded links
extlinks_detect_hardcoded_links = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
