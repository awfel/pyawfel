import copy
import logging
import secrets

from awfel.activities.base import BaseActivity

log = logging.getLogger()


class AddColumnActivity(BaseActivity):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 dataset=None,
                 column=None,
                 default=None,
                 workflow=None,
                 **kwargs):
        """Adds a property to the specified input sets."""
        self.id = id or secrets.token_hex(16)
        self.name = name
        self.description = description
        self.inputs = workflow.inputs
        self.dataset = dataset
        self.output = kwargs.get('output', None)
        self.column = column
        self.default = default
        self.workflow = workflow

    def run(self):
        # for each of the items in inputs add a property with the default.
        log.info("AddColumnActivity called.")
        dataset = self.workflow.inputs[self.dataset].value
        for item in dataset:
            if self.column in item:
                raise KeyError(f"{self.column} already exists.")
            item[self.column] = self.default

        result = copy.deepcopy(self.workflow.inputs[self.dataset])
        result.value = dataset
        self.workflow.inputs[self.output] = result
