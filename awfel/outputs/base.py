class BaseOutput(object):
    def __init__(self, name=None, format=None, *args, **kwargs):
        self.name = name
        self.format = format

    def write(self):
        raise NotImplementedError()
