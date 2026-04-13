"""Base class for creating Plotly templates matching matplotlib styles."""

from abc import ABC, abstractmethod
import plotly.graph_objects as go
import plotly.io as pio


class PlotlyStyleTemplate(ABC):
    """Base class for creating Plotly templates from matplotlib styles."""

    def __init__(self, name: str):
        """
        Initialize the style template.

        Args:
            name: Name to register the template under in plotly.io.templates
        """
        self.name = name
        self._template = None

    @property
    @abstractmethod
    def colors(self) -> list[str]:
        """Return the color cycle for this style. Override in subclasses."""
        pass

    @abstractmethod
    def create_template(self) -> go.layout.Template:
        """
        Create and return the Plotly template. Override in subclasses.

        Returns:
            A configured plotly.graph_objects.layout.Template
        """
        pass

    def get_template(self) -> go.layout.Template:
        """Get the template, creating it if necessary."""
        if self._template is None:
            self._template = self.create_template()
        return self._template

    def apply(self, set_default: bool = True):
        """
        Register and optionally set this template as the default.

        Args:
            set_default: If True, set this as the default template

        Returns:
            The registered template
        """
        template = self.get_template()
        pio.templates[self.name] = template
        if set_default:
            pio.templates.default = self.name
        return template

    def register(self):
        """Register the template without setting it as default."""
        return self.apply(set_default=False)

    def _create_base_layout(
        self,
        width: int = 900,
        height: int = 800,
        font_family: str = "Liberation Sans, Arial, sans-serif",
        font_size: int = 18,
        paper_bgcolor: str = "white",
        plot_bgcolor: str = "white",
        **kwargs,
    ) -> dict:
        """
        Create a base layout configuration with common settings.

        Args:
            width: Figure width in pixels
            height: Figure height in pixels
            font_family: Font family string
            font_size: Base font size
            paper_bgcolor: Background color of the paper
            plot_bgcolor: Background color of the plot area
            **kwargs: Additional layout parameters

        Returns:
            Dictionary of layout parameters
        """
        layout = dict(
            width=width,
            height=height,
            paper_bgcolor=paper_bgcolor,
            plot_bgcolor=plot_bgcolor,
            font=dict(family=font_family, size=font_size, color="black"),
        )
        layout.update(kwargs)
        return layout
