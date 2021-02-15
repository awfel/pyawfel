import logging

from awfel.activities.base import BaseActivity

log = logging.getLogger(__name__)


class CustomActivity(BaseActivity):
    def __init__(self,
                 name="",
                 description=None,
                 code="",
                 timeout=1.0,
                 workflow=None,
                 **kwargs):
        """Defines an activity that has custom code written in to it.

        N.B. This is extremely dangerous and if ever used in a "public" fashion
        should definitely be disabled in some manner.
        """
        self.name = name
        self.description = description
        self._code = code
        self.workflow = workflow

    def run(self):
        """Runs the custom code provided."""
        log.info(f"Run called on '{self.name}' activity")
        raise NotImplementedError()
        eval(self._code, {})  # Empty dict for locals allow __builtin__ only.
