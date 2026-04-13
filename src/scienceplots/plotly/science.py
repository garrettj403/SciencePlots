"""Science-style Plotly template."""

import plotly.graph_objects as go
from .base import PlotlyStyleTemplate
from typing import Optional

class ScienceTemplate(PlotlyStyleTemplate):
    """
    Plotly template matching the science matplotlib style.

    This is a minimal, clean scientific plotting style based on SciencePlots.
    Color cycle: blue, green, yellow, red, violet, gray
    """

    def __init__(self,
                 font_family: str = "serif",
                 font_size: int = 18,
                 font_title_size: Optional[int] = None,
                 font_legend_size: Optional[int] = None,
                 font_axis_size: Optional[int] = None,
                 font_tick_size: Optional[int] = None):
        super().__init__(name="science")
        self.font_family = font_family
        self.font_size = font_size
        self.font_title_size = font_title_size or int(font_size * 1.44)  # x-large
        self.font_legend_size = font_legend_size or int(font_size * 1.2)  # large
        self.font_axis_size = font_axis_size or int(font_size * 1.44)  # x-large for axis labels
        self.font_tick_size = font_tick_size or int(font_size * 1.2)  # large for tick labels

    @property
    def colors(self):
        """Return the science color cycle: blue, green, yellow, red, violet, gray."""
        return [
            "#0C5DA5",
            "#00B945",
            "#FF9500",
            "#FF2C00",
            "#845B97",
            "#474747",
            "#9e9e9e",
        ]

    def create_template(self) -> go.layout.Template:
        """Create the science template."""
        # Layout configuration matching science.mplstyle
        layout = go.Layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            # Color cycle
            colorway=self.colors,
            # Font settings
            font=dict(
                family=self.font_family, size=self.font_size, color="black"
            ),
            # Title settings
            title=dict(
                font=dict(
                    size=self.font_title_size,
                    family=self.font_family,
                    color="black",
                ),
                x=0.5,
                xanchor="center",
            ),
            # Legend settings
            legend=dict(
                font=dict(size=self.font_legend_size),
                bgcolor="rgba(0,0,0,0)",
                bordercolor="rgba(0,0,0,0)",
                borderwidth=0,
            ),
            # X-axis: ticks inside, on top and bottom
            xaxis=dict(
                title=dict(
                    font=dict(
                        size=self.font_axis_size,
                        family=self.font_family,
                        color="black",
                    ),
                    standoff=10,  # titlepad
                ),
                tickfont=dict(size=self.font_tick_size),
                showline=True,  # Show axis line
                linewidth=1,
                linecolor="black",
                mirror=True,  # Show ticks on top as well
                ticks="inside",
                ticklen=3,
                tickwidth=0.5,
                minor=dict(ticks="inside", ticklen=1.5, tickwidth=0.5, showgrid=False),
                showgrid=False,
                zeroline=False,
            ),
            # Y-axis: ticks inside, on left and right
            yaxis=dict(
                title=dict(font=dict(size=self.font_axis_size)),
                tickfont=dict(size=self.font_tick_size),
                showline=True,
                linewidth=1,
                linecolor="black",
                mirror=True,  # Show ticks on right as well
                ticks="inside",
                ticklen=3,
                tickwidth=0.5,
                minor=dict(ticks="inside", ticklen=1.5, tickwidth=0.5, showgrid=False),
                showgrid=False,
                zeroline=False,
            ),
            margin=dict(l=60, r=40, t=50, b=50),
        )

        # Set default trace styles with template constructor
        template = go.layout.Template(
            layout=layout,
            data={
                "scatter": [go.Scatter(line=dict(width=1.0), marker=dict(size=5))],
            },
        )

        return template


# Create a singleton instance
science = ScienceTemplate()
