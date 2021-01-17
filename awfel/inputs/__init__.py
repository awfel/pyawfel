# flake8: noqa
from .base import BaseInput
from .csv import CSVInput
from .jinja import JinjaInput


def resolve_input(*args, **kwargs):
    """Returns a dictionary of all of the input types and the function to
    initialize them.

    :param name: The unique key for the function.
    :type name: string
    :returns: a dictionary of types mapped to the keys.
    """
    # For now we implement an incredibly naive solution
    if kwargs['format'].lower() == 'csv':
        return CSVInput(name=kwargs['name'],
                        description=kwargs.get('description'),
                        path=kwargs['path'])

    if kwargs['format'].lower() == 'jinja':
        print(kwargs['path'])
        return JinjaInput(name=kwargs['name'],
                          description=kwargs.get('description'),
                          path=kwargs['path'])

    if kwargs['format'].lower() == 'variable':
        return eval(kwargs['value'])

    raise NotImplementedError(f"unknown input format: {kwargs['format']}")
