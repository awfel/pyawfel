from datetime import datetime


# Aliases for datetime.today() and datetime.now()
def today():
    return datetime.today()


def now():
    return datetime.now()


class InlineFunction(object):
    def __init__(self, workflow, arg):
        """Allows for the arbitrary evaluation of a string in the system and
        returns the appropriate value.

        For example, a workflow that processes lists of transcations might
        update an available field in an inventory:
            { "function": "inventory['on_hand'] - item['reserve']" }

        :param arg: The function to be evaluated.
        :type arg: string
        """
        if arg is None:
            raise ValueError("Must provide an argument.")
        self.arg = arg

    def value(self):
        """Evaluate the expression and return the result"""
        return eval(self.arg)
