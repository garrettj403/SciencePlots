FAQ
===

.. contents:: I want to know more about...
    :local:
    :depth: 1


Installing Latex
----------------

SciencePlots requires Latex to be installed on your machine.

- On MacOS, I recommend `MacTex <https://www.tug.org/mactex/>`_.
  Make sure that this Latex installation is added to your path enviroment
  variable. See :ghissue:`this issue <18#issuecomment-752744850>` for more
  troubleshooting tips.

- On Windows, I recommend `MikTex <https://miktex.org/>`_.
  Again, you have to add Latex to your path enviroment variable. See this
  :ghissue:`9` for more troubleshooting tips.

- On Linux (Ubuntu), you can install Tex Live and the other requirements using:

  .. code-block:: bash

    sudo apt-get install dvipng texlive-latex-extra texlive-fonts-recommended cm-super


- Please see `Matplotlib's guide to using Latex
  <https://matplotlib.org/3.1.0/tutorials/text/usetex.html>`_
  for more troubleshooting tips.

- If you don't want to install or use Latex, you can disable Latex by using:

  .. code-block:: python

      plt.style.use(['science','no-latex'])


Installing CJK fonts
--------------------

To use Chinese, Japanese or Korean fonts, you first need to install `Noto CJK
Fonts <https://www.google.com/get/noto/help/cjk/>`_. You can download and
install these fonts from the given link or you can install them with a package
manager:

.. code-block:: bash

    # Ubuntu / Debian
    sudo apt update
    sudo apt install fonts-noto-cjk

    # macOS
    brew tap homebrew/cask-fonts
    brew cask install font-noto-serif-cjk-tc
    brew cask install font-noto-serif-cjk-sc
    brew cask install font-noto-serif-cjk-jp
    brew cask install font-noto-serif-cjk-kr

    # archlinux
    sudo pacman -S noto-fonts-cjk

- For Windows Subsystem for Linux (WSL), you will need to manually download and
  install the fonts by following
  `these instructions <https://www.google.com/get/noto/help/install/>`_.

- Note that `matplotlib` may not find the fonts correctly. You can refresh the
  font cache by running:

    .. code-block:: python

        import matplotlib.font_manager as fm
        fm._rebuild()

- See this :ghissue:`16` for more information.


Installing SciencePlots manually
--------------------------------

If you like, you can install the ``*.mplstyle`` files manually. First, clone
the repository and then copy all of the ``*.mplstyle`` files into your
Matplotlib style directory. If you're not sure where this is, in an interactive
python console type:

.. code-block:: python

    import matplotlib
    import scienceplots
    print(matplotlib.get_configdir())

You should get back something like ``/home/garrett/.matplotlib``. You would
then put the ``*.mplstyle`` files in ``/home/garrett/.matplotlib/stylelib/``
(you may need to create the ``stylelib`` directory):

.. code-block:: bash

    cp styles/*.mplstyle ~/.matplotlib/stylelib/ && cp styles/*/*.mplstyle ~/.matplotlib/stylelib/


Using different fonts
---------------------

SciencePlots uses the default serif font. If you would like to specify a
different font, you can use:

.. code-block:: python

    import matplotlib.pyplot as plt
    import scienceplots
    plt.style.use('science')
    plt.rcParams.update({
        "font.family": "serif",   # specify font family here
        "font.serif": ["Times"],  # specify font here
        "font.size": 11})          # specify font size here


- If you would like to use Times New Roman specifically, please see the
  discussion in this :ghissue:`30`.


Installing SciencePlots within Google Colab, IPython, Jupyter Notebooks, etc.
-----------------------------------------------------------------------------

After version ``2.0.0``, using SciencePlots is the same as explained above.

Prior to version ``2.0.0``, you may have had to reload the Matplotlib style
library.

.. code-block::

    !pip install SciencePlots
    import matplotlib.pyplot as plt
    import scienceplots
    plt.style.reload_library()
    plt.style.use('science')
