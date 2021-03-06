import csv
import os

from awfel.errors import WorkflowError

from .base import BaseOutput

accepted_formats = ['csv']


class CSVOutput(BaseOutput):
    def __init__(self, name=None, format=None, path=None, *args, **kwargs):
        if format.lower() not in accepted_formats:
            raise WorkflowError(f'{format} is not a recognized output format.')

        super().__init__(name=name, format=format)

        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            raise NotADirectoryError(f'Directory {directory} does not exist')

        self.path = path

    def write(self, data):
        """
        Write the output to disk.

        :param data: The data to be written.
        :type data: A dictionary of the data suitable to be written to CSV
        """
        keys = set().union(*[d.keys() for d in data])
        with open(self.path, 'wt', encoding='utf8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
