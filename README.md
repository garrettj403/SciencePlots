Science Plots
=============

[![PyPI version](https://badge.fury.io/py/SciencePlots.svg)](https://badge.fury.io/py/SciencePlots)
[![DOI](https://zenodo.org/badge/144605189.svg)](https://zenodo.org/badge/latestdoi/144605189)

*Matplotlib styles for scientific figures*

This repo has Matplotlib styles to format your figures for scientific papers, presentations and theses.

<p align="center">
<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig1.jpg" width="500">
</p>

You can find [the full gallery of included styles here](https://github.com/garrettj403/SciencePlots/wiki/Gallery).

Getting Started
---------------

The easiest way to install SciencePlots is by using `pip`:

```bash
# to install the lastest release (from PyPI)
pip install SciencePlots

# to install the latest commit (from GitHub)
pip install git+https://github.com/garrettj403/SciencePlots

# to clone and install from a local copy
git clone https://github.com/garrettj403/SciencePlots.git
cd SciencePlots
pip install -e .
```

The pip installation will automatically move all of the Matplotlib style files `*.mplstyle` into the appropriate directory on your computer.

**Notes:** 
- SciencePlots requires Latex ([see Latex installation instructions](https://github.com/garrettj403/SciencePlots/wiki/FAQ#installing-latex)). 
- If you would like to use CJK fonts, you will need to install these font separately ([see CJK font installation instructions](https://github.com/garrettj403/SciencePlots/wiki/FAQ#installing-cjk-fonts)).

Please see the [FAQ](https://github.com/garrettj403/SciencePlots/wiki/FAQ) for more information and troubleshooting.

Using the Styles
----------------

``"science"`` is the primary style in this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt

plt.style.use('science')
```

You can also combine multiple styles together by:

```python
plt.style.use(['science','ieee'])
```

In this case, the ``ieee`` style will override some of the parameters from the ``science`` style in order to configure the plot for IEEE papers (column width, fontsizes, etc.).

To use any of the styles temporarily, you can use:

```python
with plt.style.context('science'):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

Examples
--------

The basic ``science`` style is shown below:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig1.jpg" width="500">

It can be cascaded with other styles to fine-tune the appearance. For example, the ``science`` + ``notebook`` styles (intended for Jupyter notebooks):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig10.jpg" width="500">

Please see [the project Wiki](https://github.com/garrettj403/SciencePlots/wiki/Gallery) for a full list of available styles.

Specific Styles for Academic Journals
-------------------------------------

The ``science`` + ``ieee`` styles for IEEE papers:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig2a.jpg" width="500">

   - IEEE requires figures to be readable when printed in black and white. The ``ieee`` style also sets the figure width to fit within one column of an IEEE paper.

The ``science`` + ``nature`` styles for Nature articles:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig2c.jpg" width="500">

   - Nature recommends sans-serif fonts.

Other languages
---------------

SciencePlots currently supports [traditional Chinese](https://github.com/garrettj403/SciencePlots/wiki/Gallery#traditional-chinese), [simplified Chinese](https://github.com/garrettj403/SciencePlots/wiki/Gallery#simplified-chinese), [Japanese](https://github.com/garrettj403/SciencePlots/wiki/Gallery#japanese), [Korean](https://github.com/garrettj403/SciencePlots/wiki/Gallery#korean) and [Russian](https://github.com/garrettj403/SciencePlots/wiki/Gallery#russian).

Example: Traditional Chinese (`science` + `no-latex` + `cjk-tc-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14a.jpg" width="500">

See the [FAQ](https://github.com/garrettj403/SciencePlots/wiki/FAQ#installing-cjk-fonts) for information on installing CJK fonts.

Other color cycles
------------------

SciencePlots comes with a variety of different color cycles. For a full list, [see the project Wiki](https://github.com/garrettj403/SciencePlots/wiki/Gallery#color-cycles). Two examples are shown below.

The ``bright`` color cycle (color blind safe):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig6.jpg" width="500">

The ``high-vis`` color cycle:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig4.jpg" width="500">

Help and Contributing
---------------------

Please feel free to contribute to the SciencePlots repo! For example, it would be good to add new styles for different journals and add new color cycles. Before starting a new style or making any changes, please create an issue through the [GitHub issue tracker](https://github.com/garrettj403/SciencePlots/issues). That way we can discuss if the changes are necessary and the best approach.

If you need any help with SciencePlots, please first check the [FAQ](https://github.com/garrettj403/SciencePlots/wiki/FAQ) and search through the [previous GitHub issues](https://github.com/garrettj403/SciencePlots/issues). If you can't find an answer, create a new issue through the [GitHub issue tracker](https://github.com/garrettj403/SciencePlots/issues).

You can checkout [Matplotlib's documentation](https://matplotlib.org/tutorials/introductory/customizing.html) for more information on plotting settings.

FAQ
---

You can find [the FAQ in the project Wiki.](https://github.com/garrettj403/SciencePlots/wiki/FAQ)

SciencePlots in Academic Papers
-------------------------------

The following papers use ``SciencePlots``:

- Y. Liu, X. Liu, Y. Sun, ["QGrain: An open-source and easy-to-use software for the comprehensive analysis of grain size distributions"](https://doi.org/10.1016/j.sedgeo.2021.105980), *Sedimentary Geology*, vol. 423, 105980, Aug. 2021.

- J. Garrett, and E. Tong, ["A Dispersion-Compensated Algorithm for the Analysis of Electromagnetic Waveguides,"](https://ieeexplore.ieee.org/document/9447194) *IEEE Signal Process. Lett.*, vol. 28, pp. 1175-1179, Jun. 2021.

- G. Jegannathan, *et al.*, ["Current-Assisted SPAD with Improved p-n Junction and Enhanced NIR Performance"](https://www.mdpi.com/1424-8220/20/24/7105), *Sensors*, Dec 2020. ([open access](https://www.mdpi.com/1424-8220/20/24/7105))

- H. Tian, *et al.*, ["ivis Dimensionality Reduction Framework for Biomacromolecular Simulations"](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.0c00485), *J. Chem. Inf. Model.*, Aug 2020. ([open access](https://arxiv.org/pdf/2004.10718.pdf))

- P. Stoltz, *et al.*, ["A new simple algorithm for space charge limited emission,"](https://aip.scitation.org/doi/10.1063/5.0020781) *Phys. Plasmas*, vol. 27, no. 9, pp. 093103, Sep. 2020. ([open access](https://aip.scitation.org/doi/10.1063/5.0020781))

- J. Garrett, *et al.*, ["A Nonlinear Transmission Line Model for Simulating Distributed SIS Frequency Multipliers,"](https://ieeexplore.ieee.org/abstract/document/9050728)  *IEEE Trans. THz Sci. Technol.*, vol. 10, no. 3, pp. 246-255, May 2020. ([open access](https://ora.ox.ac.uk/objects/uuid:5ca31c2c-a984-462c-b21a-3fe16eee0d9b/download_file?safe_filename=XXXX_final_JohnGarrett.pdf&type_of_work=Journal+article))

- J. Garrett, *et al.*, ["Simulating the Behavior of a 230 GHz SIS Mixer Using Multi-Tone Spectral Domain Analysis,"](https://ieeexplore.ieee.org/document/8822760/) *IEEE Trans. THz Sci. Technol.*, vol. 9, no. 9, pp. 540-548, Nov. 2019. ([open access](https://ora.ox.ac.uk/objects/uuid:0fd4537d-258c-454a-bbfb-09b1bcd88d49/download_file?file_format=pdf&safe_filename=XXXX_final.pdf&type_of_work=Journal+article))

- J. Garrett, *et al.*, ["A Compact and Easy to Fabricate E-plane Waveguide Bend,"](https://ieeexplore.ieee.org/document/8760521) *IEEE Microw. Wireless Compon. Lett.*, vol. 29, no. 8, pp. 529-531, Aug. 2019. ([open access](https://ora.ox.ac.uk/objects/uuid:496855f9-be2a-47cd-b498-1753d8033f50/download_file?file_format=pdf&safe_filename=Waveguide_Bend__IEEE_MWCL_.pdf&type_of_work=Journal+article))

- J. Garrett, ["A 230 GHz Focal Plane Array Using a Wide IF Bandwidth SIS Receiver,"](https://ora.ox.ac.uk/objects/uuid:d47fbf3b-1cf3-4e58-be97-767b9893066e/download_file?file_format=pdf&safe_filename=GarrettJ_DPhilThesis.pdf&type_of_work=Thesis) DPhil thesis, University of Oxford, Oxford, UK, 2018. ([open access](https://ora.ox.ac.uk/objects/uuid:d47fbf3b-1cf3-4e58-be97-767b9893066e/download_file?file_format=pdf&safe_filename=GarrettJ_DPhilThesis.pdf&type_of_work=Thesis))

If you use ``SciencePlots`` in your paper/thesis, feel free to add it to the list!

Citing SciencePlots
-------------------

You don't have to cite SciencePlots if you use it but it's nice if you do:

    @article{SciencePlots,
      author       = {John D. Garrett},
      title        = {{garrettj403/SciencePlots}},
      month        = sep,
      year         = 2021,
      publisher    = {Zenodo},
      version      = {1.0.9},
      doi          = {10.5281/zenodo.4106649},
      url          = {http://doi.org/10.5281/zenodo.4106649}
    }
