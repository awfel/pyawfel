import json
import logging
import re
import secrets
import time

from awfel.actioncontainer import ActionContainer
from awfel.errors import WorkflowError
from awfel.inputs import BaseInput, CSVInput

log = logging.getLogger(__name__)
activity_re = re.compile(r'^\w+Activity$')


def load_from_json(path):
    """Load a workflow from a JSON file."""
    with open(path, 'rt', encoding='utf8') as f:
        kwargs = json.load(f)
    return Workflow(**kwargs)


class Workflow(object):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 steps=None,
                 inputs=None,
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
                raise WorkflowError(msg)
            if input_['name'] in self._inputs:
                msg = (f"The name '{input_['name']}' already exists in the "
                       "workflow inputs. Each input for a worflow must have "
                       "a unique name.")
                raise KeyError(msg)
            key = input_['name']
            if input_['format'] == 'csv':
                log.info("reading a csv input.")
                value = CSVInput(**input_).value()
            else:
                value = BaseInput(input_)
            self._inputs[key] = value

        # Build the activities list
        self.steps = ActionContainer(steps=steps)
        # self.activities = dict()
        # for step in kwargs['steps']:
        #     if step['name'] in self.activities:
        #         msg = (f"The name '{step['name']}' already exists in the "
        #                "workflow steps. Each step must have a unique name.")
        #         raise WorkflowError(msg)
        #     self.activities[step['name']] = step.copy()
        # self._activities = deque(self.activities.values())

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
            raise WorkflowError(msg)

        try:
            self.steps.start()
        except Exception as err:
            log.error('An error happened', err)
        else:
            self.steps.stop()

    def next(self):
        """Move and start the next step in the activities."""
        activity = self._activities.popleft()
        print(activity)
        key = activity['action'].lower()
        action = self.actions[key](workflow=self, **activity)
        start_time = time.perf_counter()
        action.perform()
        run_time = time.perf_counter() - start_time
        log.info(f"{activity.name} completed in {run_time}ms.")

    def stop(self):
        """Stop the current run of the workflow.

        .. note:: If the workflow is not running this does nothing.
        """
        log.info(f"Stop called on the {self.name} ({self.id})")
        self._running = False

    @property
    def inputs(self):
        return self._inputs
