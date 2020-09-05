import inspect
import logging
import re
import time
from collections import deque
import secrets

import awfel.activities
from awfel.errors import WorkflowError

log = logging.getLogger(__name__)
activity_re = re.compile(r'^\w+(Activity)$')


def _get_actions():
    actions = dict()
    for name, obj in inspect.getmembers(awfel.activities, inspect.isclass):
        if activity_re.match(name):
            key = name.replace('Activity', '', 1)
            key = key.lower()
            actions[key] = obj
            log.debug(f'{key} added to the actions list {obj}')
    return actions


class ActionContainer(object):
    def __init__(self,
                 name=None,
                 inputs=None,
                 steps=None,
                 actions=None,
                 outputs=None,
                 *args,
                 **kwargs):
        """A container for actions to be performed.

        This is not designed to be used directly, but should instead be
        implementated by another class. For example, a workflow.
        """
        self.name = name
        self.id = id or secrets.token_hex(16)
        self.actions = actions or _get_actions()
        self._running = False

        self.inputs = inputs or dict()
        self.outputs = outputs or dict()

        self.activities = dict()
        for step in steps:
            if step['name'] in self.activities:
                msg = (f"The name '{step['name']}' already exists in the "
                       "workflow steps. Each step must have a unique name.")
                raise WorkflowError(msg)
            self.activities[step['name']] = step.copy()
        self._activities = deque(self.activities.values())

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
            while len(self._activities) > 0:
                self.next()
        except Exception as err:
            log.error('An error happened', err)
        else:
            self.stop()

    def next(self):
        """Move and start the next step in the activities."""
        activity = self._activities.popleft()
        key = activity['action'].lower()
        action = self.actions[key](workflow=self, **activity)
        start_time = time.perf_counter()
        action.perform()
        run_time = time.perf_counter() - start_time
        log.info(f"{activity['name']} completed in {run_time * 1000}ms.")

    def stop(self):
        """Stop the current run of the workflow.

        .. note:: If the workflow is not running this does nothing.
        """
        log.info(f"Stop called on the {self.name} ({self.id})")
        self._running = False
