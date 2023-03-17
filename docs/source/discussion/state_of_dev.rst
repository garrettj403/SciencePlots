State of development
====================

Styles without examples
-----------------------
``russian-font``
^^^^^^^^^^^^^^^^
Due to the following error on ReadTheDocs servers:

.. code-block::
    FileNotFoundError: Matplotlib's TeX implementation searched for a file named 'larm1000.tfm' in your texmf tree, but could not find it

Example `plot_russian-font.py` is not shown at the web.

Deprecated CJK Support
----------------------
CJK Styles have been useful for specific Matplotlib versions.
However, their API has changed and we decided to stop supporting these styles.
See :ghissue:`84`.

.. hint::

    Use other packages that actively maintain CJK fonts,
    e.g. `mplfonts <https://github.com/Clarmy/mplfonts>`_.

