from awfel.errors import WorkflowError


class BaseOutput(object):
    def __init__(self, name=None, format=None, *args, **kwargs):
        if name is None:
            raise WorkflowError("Name must be defined for the ouput")
        self.name = name
        self.format = format

    def write(self):
        raise NotImplementedError()
