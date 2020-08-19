import tempfile
import logging

log = logging.getLogger(__name__)


class ResourcesWrapper():
    def __init__(self):
        """The wrapper for resources management that allows for items to be
        efficiently created and disposed of.
        """
        self.temp_file = tempfile.SpooledTemporaryFile()
        log.debug("Temporary spooled file created")
        raise NotImplementedError()

    # This will handle creating a collection of resources/outputs for the
    # workflow.
    #
    # See tempfile.SpooledTemporaryFile as a meand for a performant file
    # storage.
