import logging
import secrets
from datetime import datetime  # noqa: F401

from .base import BaseActivity

log = logging.getLogger(__name__)


class UpdateActivity(BaseActivity):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 dataset='item',
                 output='',
                 workflow=None,
                 field='',
                 value='',
                 *args,
                 **kwargs):
        self.id = id or secrets.token_hex(16)
        self.name = name
        self.description = description
        self.workflow = workflow
        self.dataset = self.workflow.inputs[dataset]
        if not isinstance(self.dataset, dict):
            self.dataset = self.dataset.value
        self.field = field
        self.value = value

    def function(self, value, item):
        if isinstance(value, dict):
            if 'field' in value.keys():
                # return the field
                return item.get(value['field'], '')
            if 'expr' in value.keys():
                return eval(value['expr'])

        return value

    def run(self):
        if isinstance(self.dataset, list):
            raise NotImplementedError()

        key, value = self.field, self.function(self.value, self.dataset)
        self.dataset[key] = value
