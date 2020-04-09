"""Install SciencePlots.

This will copy the *.mplstyle files into the appropriate directory.

This code is based on a StackOverflow answer:
https://stackoverflow.com/questions/31559225/how-to-ship-or-distribute-a-matplotlib-stylesheet

"""

from setuptools import setup
from setuptools.command.install import install
import os
import shutil
import atexit
import glob

import matplotlib

def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)

    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir() ,"stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)

    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            # os.path.join(os.path.dirname(__file__), stylefile),
            stylefile, 
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)

setup(
    name='SciencePlots',
    version='1.0.0',
    author="John Garrett",
    author_email="garrettj403@gmail.com",
    description="Format Matplotlib for scientific plotting",
    license="MIT",
    keywords=[
        "matplotlib-style-sheets", 
        "matplotlib-figures", 
        "scientific-papers", 
        "thesis-template", 
        "matplotlib-styles", 
        "python"
    ],
    url="https://github.com/garrettj403/SciencePlots/",
    # py_modules=['styles'],
    package_data = {
        'styles': [
            "misc/no-latex.mplstyle",
            "misc/pgf.mplstyle",
            "science.mplstyle",
            "color/muted.mplstyle",
            "color/vibrant.mplstyle",
            "color/high-vis.mplstyle",
            "color/bright.mplstyle",
            "color/retro.mplstyle",
            "scatter.mplstyle",
            "journals/ieee.mplstyle",
            "notebook.mplstyle"
        ]
    },
    install_requires=[
        'matplotlib',
    ],
    cmdclass={
        'install': PostInstallMoveFile,
    }
)
