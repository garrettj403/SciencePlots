"""Install SciencePlots.

This script (setup.py) will install the SciencePlots package.
In order to expose .mplstyle files to matplotlib, "import scienceplots"
must be called before plt.style.use(...).
"""

import os
from setuptools import setup

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SciencePlots',
    version='2.1.0',
    author="John Garrett",
    author_email="garrettj403@gmail.com",
    maintainer="Echedey Luis",
    maintainer_email="echelual@gmail.com",
    description="Format Matplotlib for scientific plotting",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/garrettj403/SciencePlots/",

    install_requires=['matplotlib'],
    packages=["scienceplots"],
    package_data={
      'scienceplots': ['styles/**/*.mplstyle'],
    },

    classifiers=[
        'Framework :: Matplotlib', 
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "thesis-template",
        "matplotlib-styles",
        "python"
    ],
)
