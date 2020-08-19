class BaseInput(object):
    def __init__(self,
                 name=None,
                 description=None,
                 format=None,
                 date_fmt='%x',
                 **kwargs):
        """The base for inputs into the system.

        :param name: the unique name for the input.
        :param description: the description for the input that describes what
            it is for other users.
        :param format: the format of the input.
        :param date_fmt: The format to use for any dates found in the file.
            (Deault is the system date format).
        :type name: string
        :type description: string
        :type format: string
        :type date_fmt: string
        """
        if name is None:
            raise AttributeError(msg="""Must provide a unique name for each
                                        input.""")
        self.name = name
        self.description = description
        self.date_fmt = date_fmt
