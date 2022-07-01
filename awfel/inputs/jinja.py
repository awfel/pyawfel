from jinja2 import Template

from .base import BaseInput


class JinjaInput(BaseInput):
    def __init__(self, name=None, path=None, *args, **kwargs):
        self.path = path
        self.name = name
        # super().__init__(args, kwargs)

    def value(self):
        """Returns the Jinja2 template so that it can be rendered.

        >>> self.value().render()  # will return the html.
        """
        with open(self.path, 'rt', encoding='utf8') as f:
            return Template(f.read())
