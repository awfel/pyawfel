import logging
import secrets

from awfel.activities.base import BaseActivity

log = logging.getLogger()


class AddColumnActivity(BaseActivity):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 column=None,
                 default=None,
                 workflow=None,
                 **kwargs):
        """Adds a property to the specified input sets."""
        self.id = id or secrets.token_hex(16)
        self.name = name
        self.description = description
        self.inputs = workflow.inputs
        self.outputs = kwargs['outputs']
        self.column = column
        self.default = default
        self.workflow = workflow

    def run(self):
        # for each of the items in inputs add a property with the default.
        log.info("AddColumnActivity called.")
        for input_ in self.inputs:
            # This needs to handle inputs better...
            print(input_)
            dataset = self.workflow.inputs[input_]
            for item in dataset:
                if self.column in item:
                    raise KeyError(f"{self.column} already exists.")
                item[self.column] = self.default
