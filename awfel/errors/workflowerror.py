class WorkflowError(BaseException):
    def __init__(self, msg=None):
        self.msg = msg

    @property
    def msg(self):
        return self.msg or ""
