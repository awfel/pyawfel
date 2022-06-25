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
        self.format = kwargs.get('format', 'csv')
        self.workflow = workflow

    def run(self):
        data = self.workflow.inputs[self.dataset].value
        output = self.workflow.outputs[self.output]
        with open(data, "w") as f:
            f.write(data)

        log.info(f"{self.dataset} saved as {output.path}")
