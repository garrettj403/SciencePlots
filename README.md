Science Plots
=============

[![PyPI version](https://badge.fury.io/py/SciencePlots.svg)](https://badge.fury.io/py/SciencePlots)
[![DOI](https://zenodo.org/badge/144605189.svg)](https://zenodo.org/badge/latestdoi/144605189)

*Matplotlib styles for scientific plotting*

This repo has Matplotlib styles to format your plots for scientific papers, presentations and theses.

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig1.jpg" width="500">

Installation
------------

The easiest way to install SciencePlots is using ``pip``:

```bash
# for latest commit
pip install git+https://github.com/garrettj403/SciencePlots.git

# for lastest release
pip install SciencePlots
```

The pip installation will automatically move all of the ``*.mplstyle`` files into the appropriate directory. Please see the [FAQ](#FAQ) for more information and troubleshooting.

Using the Styles
----------------

``science.mplstyle`` is the main style from this repo. Whenever you want to use it, simply add the following to the top of your python script:

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
with plt.style.context(['science', 'ieee']):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

Examples
--------

The ``science`` style:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig1.jpg" width="500">

The ``science`` + ``grid`` styles:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig11.jpg" width="500">

The ``science`` + ``ieee`` styles for IEEE papers:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig2.jpg" width="500">

   - IEEE requires figures to be readable when printed in black and white. The ``ieee`` style also sets the figure width to fit within one column of an IEEE paper.

The ``science`` + ``scatter`` styles for scatter plots:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig3.jpg" width="500">

The ``science`` + ``notebook`` styles for Jupyter notebooks:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig10.jpg" width="500">

You can also combine these styles with the other styles that come with Matplotlib. For example, the ``dark_background`` + ``science`` + ``high-vis`` styles:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig5.jpg" width="500">

**Note:** See the ``examples/`` directory for more!

CJK Fonts
---------

Traditional Chinese (`science` + `cjk-tc-font` + `no-latex`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14a.jpg" width="500">

Simplified Chinese (`science` + `cjk-sc-font` + `no-latex`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14b.jpg" width="500">

Japanese (`science` + `cjk-jp-font` + `no-latex`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14c.jpg" width="500">

See the [FAQ](https://github.com/garrettj403/SciencePlots#faq) for information on installing CJK fonts.

Color Blind Safe Color Cycles
-----------------------------

The ``bright`` color cycle (7 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig6.jpg" width="500">

The ``vibrant`` color cycle (7 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig7.jpg" width="500">

The ``muted`` color cycle (10 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig8.jpg" width="500">

The ``high-contrast`` color cycle (3 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig12.jpg" width="500">

The ``light`` color cycle (9 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig13.jpg" width="500">

**Note:** These color cycles are from [Paul Tol's website](https://personal.sron.nl/~pault/).

Other Color Cycles
------------------

The ``high-vis`` color cycle:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig4.jpg" width="500">

The ``retro`` color cycle:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig9.jpg" width="500">

Help and Contributing
---------------------

Please feel free to contribute to the SciencePlots repo! For example, it would be good to add new styles for different journals and add new color cycles. Before starting a new style or making any changes, please create an issue through the [GitHub issue tracker](https://github.com/garrettj403/SciencePlots/issues). That way we can discuss if the changes are necessary and the best approach.

If you need any help with SciencePlots, please first check the [FAQ](https://github.com/garrettj403/SciencePlots#faq) and search through the [previous GitHub issues](https://github.com/garrettj403/SciencePlots/issues). If you can't find an answer, create a new issue through the [GitHub issue tracker](https://github.com/garrettj403/SciencePlots/issues).

You can checkout [Matplotlib's documentation](https://matplotlib.org/tutorials/introductory/customizing.html) for more information on plotting settings.

FAQ
---

1. Errors related to Latex:

   - If you get an error saying ``RuntimeError: Failed to process string with tex because latex could not be found``, this means that you do not have Latex installed on your computer (or at least that Python/Matplotlib can't find it). You have two options: (1) install Latex, or (2) disable Latex using the ``no-latex`` option:

      ```python
      plt.style.use(['science','no-latex'])
      ```

   - For Windows users, you may need to manually add Latex to your environment path ([see issue](https://github.com/garrettj403/SciencePlots/issues/9)).

2. Manual installation:

   - If you like, you can install the ``*.mplstyle`` files manually. First, clone the repository and then copy all of the ``*.mplstyle`` files into your Matplotlib style directory. If you're not sure where this is, in an interactive python console type:

      ```python
      import matplotlib
      print(matplotlib.get_configdir())
      ```

   - You should get back something like ``/home/garrett/.matplotlib``. You would then put the ``*.mplstyle`` files in ``/home/garrett/.matplotlib/stylelib/`` (you may need to create the ``stylelib`` directory):

      ```bash
      cp styles/*/*.mplstyle ~/.matplotlib/stylelib/
      ```

3. Using different fonts:

   - SciencePlots uses the default serif font. If you would like to specify a different font, you can use:

      ```python
      import matplotlib.pyplot as plt 
      plt.style.use('science')
      plt.rcParams.update({
          "font.family": "serif",   # specify font family here
          "font.serif": ["Times"],  # specify font here
          "font.size":11})          # specify font size here
      ```

   - If you would like to use Times New Roman specifically, please see the discussion in [this issue](https://github.com/garrettj403/SciencePlots/issues/30).

4. Using CJK fonts:

   - To use CJK fonts, you first need to install [Noto CJK Fonts](https://www.google.com/get/noto/help/cjk/). You can download and install these fonts from the given link or you can install them with a package manager:

      ```bash
      # Ubuntu / Debian
      $ sudo apt update
      $ sudo apt install fonts-noto-cjk

      # macOS
      $ brew tap homebrew/cask-fonts
      $ brew cask install font-noto-serif-cjk-tc
      $ brew cask install font-noto-serif-cjk-sc
      $ brew cask install font-noto-serif-cjk-jp
      $ brew cask install font-noto-serif-cjk-kr

      # archlinux
      $ sudo pacman -S noto-fonts-cjk
      ```

      Note that `matplotlib` may not find the fonts correctly. You can refresh the font cache by running:

      ```python
      import matplotlib.font_manager as fm
      fm._rebuild()
      ```

   - You should use the parameter `backend='pgf'` for the `savefig()` to use XeLaTeX instead of PdfLaTeX (this LaTeX engine doesn't work with CJK fonts properly). Besides, it can't export the `jpg` format when you use the parameter `backend='pgf'` for the `savefig()`.

5. Installing SciencePlots within Google Colab, IPython, Jupyter Notebooks, etc.:

   - After installing SciencePlots within one of these environments, you may need to reload the Matplotlib style library. For example:

      ```python
      !pip install SciencePlots
      import matplotlib.pyplot as plt
      plt.style.reload_library()
      plt.style.use('science')
      ```

SciencePlots in Academic Papers
-------------------------------

The following papers use ``SciencePlots``:

- Jegannathan, G., *et al.*, ["Current-Assisted SPAD with Improved p-n Junction and Enhanced NIR Performance"](https://www.mdpi.com/1424-8220/20/24/7105), *Sensors*, Dec 2020. ([open access](https://www.mdpi.com/1424-8220/20/24/7105))

- H. Tian, *et al.*, ["ivis Dimensionality Reduction Framework for Biomacromolecular Simulations"](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.0c00485), *J. Chem. Inf. Model.*, Aug 2020. ([open access](https://arxiv.org/pdf/2004.10718.pdf))

- P. Stoltz, *et al.*, ["A new simple algorithm for space charge limited emission,"](https://aip.scitation.org/doi/10.1063/5.0020781) *Phys. Plasmas*, vol. 27, no. 9, pp. 093103, Sep. 2020. ([open access](https://aip.scitation.org/doi/10.1063/5.0020781))

- J. Garrett, *et al.*, ["A Nonlinear Transmission Line Model for Simulating Distributed SIS Frequency Multipliers,"](https://ieeexplore.ieee.org/abstract/document/9050728)  *IEEE Trans. THz Sci. Technol.*, vol. 10, no. 3, pp. 246-255, May 2020. ([open access](https://ora.ox.ac.uk/objects/uuid:5ca31c2c-a984-462c-b21a-3fe16eee0d9b/download_file?safe_filename=XXXX_final_JohnGarrett.pdf&type_of_work=Journal+article))

- J. Garrett, *et al.*, ["Simulating the Behavior of a 230 GHz SIS Mixer Using Multi-Tone Spectral Domain Analysis,"](https://ieeexplore.ieee.org/document/8822760/) *IEEE Trans. THz Sci. Technol.*, vol. 9, no. 9, pp. 540-548, Nov. 2019. ([open access](https://ora.ox.ac.uk/objects/uuid:0fd4537d-258c-454a-bbfb-09b1bcd88d49/download_file?file_format=pdf&safe_filename=XXXX_final.pdf&type_of_work=Journal+article))

- J. Garrett, *et al.*, ["A Compact and Easy to Fabricate E-plane Waveguide Bend,"](https://ieeexplore.ieee.org/document/8760521) *IEEE Microw. Wireless Compon. Lett.*, vol. 29, no. 8, pp. 529-531, Aug. 2019. ([open access](https://ora.ox.ac.uk/objects/uuid:496855f9-be2a-47cd-b498-1753d8033f50/download_file?file_format=pdf&safe_filename=Waveguide_Bend__IEEE_MWCL_.pdf&type_of_work=Journal+article))

- J. Garrett, ["A 230 GHz Focal Plane Array Using a Wide IF Bandwidth SIS Receiver,"](https://ora.ox.ac.uk/objects/uuid:d47fbf3b-1cf3-4e58-be97-767b9893066e/download_file?file_format=pdf&safe_filename=GarrettJ_DPhilThesis.pdf&type_of_work=Thesis) DPhil thesis, University of Oxford, Oxford, UK, 2018. ([open access](https://ora.ox.ac.uk/objects/uuid:d47fbf3b-1cf3-4e58-be97-767b9893066e/download_file?file_format=pdf&safe_filename=GarrettJ_DPhilThesis.pdf&type_of_work=Thesis))

If you use ``SciencePlots`` in your paper/thesis, feel free to add it to the list!

Citing SciencePlots
-------------------

You don't have to cite SciencePlots if you use it, but it's nice if you do:

    @article{SciencePlots,
      author       = {J. D. Garrett},
      title        = {{SciencePlots (v1.0.6)}},
      month        = oct,
      year         = 2020,
      publisher    = {Zenodo},
      doi          = {10.5281/zenodo.4106650},
      url          = {http://doi.org/10.5281/zenodo.4106650}
    }
