Basic Styles
============

The ``science`` style:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig01a.jpg" width="500">

The ``science`` + ``no-latex`` style:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig01b.jpg" width="500">

The ``science`` + ``grid`` styles:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig11.jpg" width="500">

The ``science`` + ``scatter`` styles for scatter plots:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig03.jpg" width="500">

The ``science`` + ``notebook`` styles for Jupyter notebooks:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig10.jpg" width="500">

Styles for Specific Academic Journals
=====================================

The ``science`` + ``ieee`` styles for IEEE papers:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig02a.jpg" width="500">

- IEEE requires figures to be readable when printed in black and white. The ``ieee`` style also sets the figure width to fit within one column of an IEEE paper and the resolution to 600 DPI.
- Note: The IEEE style will make your figures massive if you use it with ``plt.show()``. To get around this, you can add ``plt.rcParams.update({'figure.dpi': '100'})`` to the top of your script (see [issue](https://github.com/garrettj403/SciencePlots/issues/60)).

The ``science`` + ``nature`` styles for Nature articles:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig02c.jpg" width="500">

- Nature recommends sans-serif fonts.

Support for Other Languages
===========================

> CJK font styles have been deprecated in favour of other packages that maintain it actively.
> For example, make use [`mplfonts`](https://github.com/Clarmy/mplfonts)
> See issue #84.
>
> Till we get some more info, we will preserve this wiki section.

See the [FAQ](https://github.com/garrettj403/SciencePlots#faq) for information on installing CJK fonts.

Traditional Chinese
-------------------

Traditional Chinese (`science` + `no-latex` + `cjk-tc-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14a.jpg" width="500">

Simplified Chinese
------------------

Simplified Chinese (`science` + `no-latex` + `cjk-sc-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14b.jpg" width="500">

Japanese
--------

Japanese (`science` + `no-latex` + `cjk-jp-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14c.jpg" width="500">

Korean
------

Korean (`science` + `no-latex` + `cjk-kr-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig14d.jpg" width="500">

Russian
-------

Russian/cyrillic (`science` + `russian-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig16.jpg" width="500">

Turkish
-------

Turkish (`science` + `turkish-font`):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig17.jpg" width="500">

Color Cycles
============

Color Blind Safe
----------------

The ``okabe-ito`` color cycle (8 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig_okabe-ito.jpg" width="500">

**Note:** The following color cycles are from [Paul Tol&#39;s website](https://sronpersonalpages.nl/~pault/).

The ``bright`` color cycle (7 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig06.jpg" width="500">

The ``vibrant`` color cycle (7 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig07.jpg" width="500">

The ``muted`` color cycle (10 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig08.jpg" width="500">

The ``high-contrast`` color cycle (3 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig12.jpg" width="500">

The ``light`` color cycle (9 colors):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig13.jpg" width="500">

### Discrete Rainbow

There are 23 different cycles, with the name ``discrete-rainbow-<n>`` (``<n>`` ranges from 1 to 23, inclusive). The number defines the amount of unique colors in the cycle. Some examples below:

- ``discrete-rainbow-6``:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig_dr_6.jpg" width="500">

- ``discrete-rainbow-15``:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig_dr_15.jpg" width="500">

- ``discrete-rainbow-23``:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig_dr_23.jpg" width="500">

Other
-----

The ``std-colors`` color cycle (used to override other color cycles, e.g., the color cycle from ``ieee``):

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig02b.jpg" width="500">

The ``high-vis`` color cycle:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig04.jpg" width="500">

The ``retro`` color cycle:

<img src="https://github.com/garrettj403/SciencePlots/raw/master/examples/figures/fig09.jpg" width="500">
