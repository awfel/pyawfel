import json
import logging
import os
import re
import secrets
from pathlib import Path

from awfel.actioncontainer import ActionContainer
from awfel.errors import WorkflowError
from awfel.inputs import resolve_input
from awfel.outputs import resolve_output

log = logging.getLogger(__name__)
activity_re = re.compile(r'^\w+Activity$')
cwd = os.getenv('AWFEL_BASEPATH', os.getcwd())


def load_from_json(path):
    """Load a workflow from a JSON file.

    Creates a new :class:Workflow from a JSON file and return it.

    :param path: The path to the definition file.
    :type path: int, path
    :returns: A :class:Workflow object
    """
    with open(Path().joinpath(cwd, path), 'rt', encoding='utf8') as f:
        kwargs = json.load(f)
    return Workflow(**kwargs)


class Workflow(object):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 steps=None,
                 inputs=None,
                 outputs=None,
                 *args,
                 **kwargs):
        """Workflow is the container that executes activities according to the
        strategy/order in the definition.

        :param id: An id for the worklflow instance.
        :param name: The name of the workflow that is also used as the key.
        :param description: the readable decsription so that users can
            understand what the workflow does.
        :param inputs: the collection of inputs for the workflow.
        """
        self.id = id or secrets.token_hex(8)
        if name is None:
            raise WorkflowError('Name must be defined for the workflow')
        self.name = name
        self.description = description
        self._running = False

        # Add inputs to the workflow
        self._inputs = dict()
        for input_ in inputs:
            if input_['name'] == 'item':
                msg = ("The name 'item' is reserved for use inside an awfel "
                       "workflow. Provide a different name for the input.")
                log.Error(msg)
                raise WorkflowError(msg)
            if input_['name'] in self._inputs:
                msg = (f"The name '{input_['name']}' already exists in the "
                       "workflow inputs. Each input for a worflow must have "
                       "a unique name.")
                log.Error(msg)
                raise KeyError(msg)
            key = input_['name']
            print(input_)
            value = resolve_input(**input_)
            self._inputs[key] = value

        # register the outputs
        self._outputs = dict()
        for output in outputs:
            key, value = output['name'], resolve_output(**output)
            self._outputs[key] = value

        self.steps = ActionContainer(steps=steps,
                                     inputs=self._inputs,
                                     outputs=self._outputs)

        log.debug(f"Workflow '{self.name}' succesfully created")

    def start(self, force=False):
        """Start the workflow.

        :param force: should you force the workflow to restart if it is already
            in a running state.
        :type force: bool
        """
        if self._running and not force:
            msg = (f"Workflow '{self.name}' with id {self.id} is already "
                   "running.")
            log.error(msg)
            raise WorkflowError(msg)

        try:
            self.steps.start()
        except Exception as err:
            log.error('Unable to start workflow', err)
        else:
            self.steps.stop()

    def stop(self):
        """Stop the current run of the workflow.

        .. note:: If the workflow is not running this does nothing.
        """
        log.info(f"Stop called on the {self.name} ({self.id}) workflow")
        self._running = False

    @property
    def inputs(self):
        return self._inputs
