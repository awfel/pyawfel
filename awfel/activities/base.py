import logging
from enum import Enum
from warnings import warn

log = logging.getLogger(__name__)


class ActivityState(Enum):
    UNSTARTED = 0
    RUNNING = 1
    PAUSED = 2
    COMPLETED = 3


class BaseActivity(object):
    def __init__(self,
                 name,
                 description=None,
                 actiontype="",
                 state=ActivityState.UNSTARTED,
                 workflow=None,
                 *args,
                 **kwargs):
        """An activity performed as part of a workflow. This class is not
        designed to be used directly, instead you should use it to define your
        own activities or use one of the existing derivatives.

        Activity lifecycle is:
            setup() -> run() -> finalize()

        :param name: The unique name in the workflow for the activity.
        :param description: The readable descripton for this activity in the
            workflow.
        :param state: The state of the activity to allow for it to be paused
            and resumed.
        :param workflow: The workflow that the activity is a component of.
        """
        if workflow is None:
            raise AttributeError(msg="Activities must be part of a workflow.")
        self.name = name
        self.description = description
        self.actiontype = kwargs['type']
        self.state = state
        self._percent_complete = 0

    def validate(self):
        """Validates the action with doing any work or producing any outputs.

        Designed to be overridden by any deriving class, but by default
        returns true.

        :returns: True/false depending on whether the validation passes.
        :rtype: bool
        """
        warn((f"Validate has been called on the {self.actiontype} activity, "
              "but it does not implement this functionality."))
        log.debug("Validate called on the base class")
        return True

    def setup(self):
        """Sets the actual work of the activity running. Implement as needed in
        a derived class.

        Intended as a way to invoke anything before starting the actual run.
        """
        pass

    def run(self):
        """Sets the actual work of the Activity running. Must be implemented by
        a derived class.
        """
        raise NotImplementedError()

    def finalize(self):
        """Finalize the Activity performing any cleanup as necessary.

        Intended as a means to cleanup any code and close resources as
        necessary.
        """
        self._percent_complete = 100
        self.state = ActivityState.COMPLETED

        @property
        def percent_complete(self):
            return self._percent_complete

    def perform(self):
        """Handles the lifecycle of the activity."""
        self.setup()
        self.run()
        self.finalize()
