"""Plotly templates matching matplotlib scienceplots styles."""

try:
    from .base import PlotlyStyleTemplate
    from .science import science, ScienceTemplate

    __all__ = ['PlotlyStyleTemplate', 'science', 'ScienceTemplate']
except ImportError:
    # Plotly not installed, don't expose API
    __all__ = []
