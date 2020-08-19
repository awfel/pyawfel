from csv import DictWriter
import logging

from awfel.activities.base import BaseActivity

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
        self.format = output.get('type', 'csv')
        self.workflow = workflow

    def run(self):
        data = self.workflow.inputs[self.dataset]
        fieldnames = data.keys()
        with open(self.output['path'], 'w') as f:
            writer = DictWriter(f, fieldnames=fieldnames)
            writer.writerows(data)

        log.info(f"{self.dataset} saved as {self.output['path']}")
