v1.0.8 (02-Jun-2021)
====================

- ``nature``:
   - Added style for Nature articles
   - Uses sans-serif fonts
- ``latex-sans``:
   - Added style for using LaTeX with sans-serif fonts
- ``std-colors``:
   - Added style to recover the standard color cycle of the SciencePlots package
   - For example, if you use ``plt.style.use(["science", "ieeee"]). The figure will use the ``"ieee"`` color cycle. To revert to the standard color cycle, you can use ``plt.style.use(["science", "ieee", "std-colors"])``.
- ``science``:
   - Added ``amssymb`` to LaTeX preamble
- ``grid``: 
   - Set ``axes.axisbelow`` to True
- Minor updates to README

v1.0.7 (28-Feb-2021)
====================

- Add support for CJK fonts:
   - see README for details
- Add example of CJK fonts:
   - see Fig 14a, Fig 14b, Fig 14c, Fig 14d
- ``science`` style:
   - use default serif font
- ``ieee`` style: 
   - use Times font
- ``grid`` style:
   - change line style to '--'
- README:
   - add badge for Zenodo reference
   - add info on citing SciencePlots
   - add info on using Times New Roman
   - add more papers using SciencePlots
   
v1.0.6 (19-Oct-2020)
====================

- The main reason for this release is to trigger Zenodo:
   - I've added SciencePlots to Zenodo (an archiving service).
   - It only archives after new releases, so I will make a trivial version bump.
- Trivial changes to README:
   - Added installation info for Google Colab, Jupyter Notebooks, etc.
   - Added PyPI badge
   - Added more papers to list

v1.0.5 (8-Sep-2020)
===================

- New color blind safe color cycles (``high-contrast.mplstyle``, ``light.mplstyle``). Taken from [Paul Tol's website](https://personal.sron.nl/~pault/).
- Fixed color order in ``muted.mplstyle``, ``vibrant.mplstyle``, and ``bright.mplstyle``.

v1.0.4 (14-Aug-2020)
====================

- New style: ``grid``
   - this will add grid lines
- ``science`` style:
   - use a serif font with mathtex
- README:
   - Add example of the ``notebook`` style
   - Add FAQ
   - Update publications
   - Other misc changes...
