class WorkflowError(BaseException):
    def __init__(self, msg=None):
        self._msg = msg

    @property
    def msg(self):
        return self._msg or ""
