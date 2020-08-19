from csv import DictReader
# import os

from .base import BaseInput


class CSVInput(BaseInput):
    def __init__(self, name=None, description=None, path=None, **kwargs):
        """A CSV input for the system and various helper methods."""
        self.name = name
        self.description = description
        self.path = path
        self._value = None

    def value(self):
        if self._value is None:
            with open(self.path, 'rt') as f:
                self._value = DictReader(f.readlines())

        return self._value
