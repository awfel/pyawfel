from csv import DictReader

from .base import BaseInput


class CSVInput(BaseInput):
    def __init__(self, name=None, description=None, path=None, **kwargs):
        """A CSV input for the system and various helper methods."""
        self.name = name
        self.description = description
        self.path = path
        self._value = None

    @property
    def value(self):
        # resolve only when and if called.
        if self._value is None:
            with open(self.path, 'rt') as f:
                return list(DictReader(f))
                print(self._value)

        return self._value

    @value.setter
    def value(self, value):
        self._value = value
