import logging

from awfel.activities.base import BaseActivity
from awfel.outputs.csv import CSVOutput

log = logging.getLogger(__name__)


class SaveActivity(BaseActivity):
    def __init__(self,
                 name=None,
                 description=None,
                 dataset=None,
                 output=None,
                 workflow=None,
                 **kwargs):
        """Save a dataset to a predefined output point."""
        self.name = name
        self.description = description
        self.dataset = dataset
        self.output = output
        self.format = kwargs.get('format', 'csv')
        self.workflow = workflow

    def run(self):
        data = self.workflow.inputs[self.dataset].value
        output = self.workflow.outputs[self.output]

        if self.format == "csv":
            csv = CSVOutput("csvout", "csv", output.path)
            csv.write(data)
        else:
            with open(output.path, "w") as f:
                f.write(str(data))

        log.info(f"{self.dataset} saved as {output.path}")
