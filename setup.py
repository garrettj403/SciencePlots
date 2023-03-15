"""Install SciencePlots.

This script (setup.py) will install the SciencePlots package.
In order to expose .mplstyle files to matplotlib, "import scienceplots"
must be called before plt.style.use(...).
"""

import os
from setuptools import setup

PYTHON_VERSION = '>=3.8'
INSTALL_REQUIRE = ['matplotlib']
EXTRAS_REQUIRE = {
    'test': ['pytest', 'flake8'],
    'docs': ['sphinx', 'sphinx-gallery', 'sphinx_copybutton',
             'pydata-sphinx-theme', 'Jinja2', 'numpy']
}
EXTRAS_REQUIRE['all'] = sorted(set(sum(EXTRAS_REQUIRE.values(), [])))

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SciencePlots',
    version='2.0.1',
    author="John Garrett",
    author_email="garrettj403@gmail.com",
    maintainer="Echedey Luis",
    maintainer_email="echelual@gmail.com",
    description="Format Matplotlib for scientific plotting",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/garrettj403/SciencePlots/",

    packages=["scienceplots"],
    package_data={
      'scienceplots': ['styles/**/*.mplstyle'],
    },
    python_version=PYTHON_VERSION,
    install_requires=INSTALL_REQUIRE,
    tests_require=EXTRAS_REQUIRE['test'],
    extras_require=EXTRAS_REQUIRE,

    classifiers=[
        'Framework :: Matplotlib',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
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
