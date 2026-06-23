from .styles_discovery import read_styles


class StyleRegistry:
    def __init__(self, stylesheets):
        self.stylesheets = stylesheets

    def get(self, names):
        if isinstance(names, str):
            names = [names]

        for name in names:
            if name not in self.stylesheets:
                raise ValueError(f"'{name}' is not a known SciencePlots style")

        return [self.stylesheets[name] for name in names]

    def __call__(self, names):
        return self.get(names)


styles = StyleRegistry(read_styles())
