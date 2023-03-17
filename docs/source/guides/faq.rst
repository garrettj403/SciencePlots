FAQ
===
If you need any help with SciencePlots, please first check the
the question has not already been addressed here and search through
`previous GitHub issues <|repo_base_link + "issues?q=is%3Aissue"|>`_.
If you didn't find an answer, you can create a new issue.

You can checkout `Matplotlib's documentation
<https://matplotlib.org/tutorials/introductory/customizing.html>`_
for more information on plotting settings.

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


Installing SciencePlots manually
--------------------------------

If you like, you can install the ``*.mplstyle`` files manually. First, clone
the repository and then copy all of the ``*.mplstyle`` files into your
Matplotlib style directory. If you're not sure where this is, in an interactive
python console type:

.. code-block:: python

    import matplotlib
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
