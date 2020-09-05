from .csv import CSVOutput


def resolve_output(*args, **kwargs):
    """Resolve the output to a type and location that can be written."""
    if kwargs['format'].lower() == 'csv':
        return CSVOutput(name=kwargs['name'],
                         format=kwargs['format'],
                         description=kwargs.get('description'),
                         path=kwargs['path'])

    raise NotImplementedError(f"unknown input format: {kwargs['format']}")
