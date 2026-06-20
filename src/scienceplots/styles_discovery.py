import pathlib
import importlib.resources


def read_styles():
    """
    Reads all ``SciencePlots`` stylesheets.

    Returns
    -------
    stylesheets : dict
        Dictionary of stylesheets in the form of ``{style_name: path}``. These
        styles can then be directly used with ``matplotlib.pyplot.style.use``.
    """

    with importlib.resources.path("scienceplots", "styles") as dirname:
        path = pathlib.Path(dirname).resolve()
        return {
            mplstyle.stem: str(mplstyle)
            for mplstyle in path.rglob("*.mplstyle")
        }

