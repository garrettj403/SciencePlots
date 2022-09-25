"""Install SciencePlots.

This script (setup.py) will install the SciencePlots package.
In order to expose .mplstyle files to matplotlib, "import SciencePlots"
must be called before plt.style.use(...).
"""

import os

from setuptools import setup


# def install_styles():
#     # Find all style files
#     stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
#     # Find stylelib directory (where the *.mplstyle files go)
#     # Copy files over
#     print("Installing styles into", mpl_stylelib_dir)
#     for stylefile in stylefiles:
#         print(os.path.basename(stylefile))
#         shutil.copy(
#             stylefile,
#             os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
# ('notebook.mplstyle', 'scatter.mplstyle', 'science.mplstyle', 'bright.mplstyle', 'high-contrast.mplstyle', 'high-vis.mplstyle', 'light.mplstyle', 'muted.mplstyle', 'retro.mplstyle', 'std-colors.mplstyle', 'vibrant.mplstyle', 'ieee.mplstyle', 'nature.mplstyle', 'cjk-jp-font.mplstyle', 'cjk-kr-font.mplstyle', 'cjk-sc-font.mplstyle', 'cjk-tc-font.mplstyle', 'grid.mplstyle', 'latex-sans.mplstyle', 'no-latex.mplstyle', 'pgf.mplstyle', 'russian-font.mplstyle', 'sans.mplstyle')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SciencePlots',
    version='1.1.0',
    author="John Garrett",
    author_email="garrettj403@gmail.com",
    description="Format Matplotlib for scientific plotting",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/garrettj403/SciencePlots/",

    install_requires=['matplotlib'],
    packages=["SciencePlots"],
    package_data={
      'SciencePlots': ['styles/**/*.mplstyle'],
    },

    classifiers=[
        'Framework :: Matplotlib', 
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "thesis-template",
        "matplotlib-styles",
        "python"
    ],
    # cmdclass={'install': PostInstallMoveFile, },
)
