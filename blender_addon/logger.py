import logging

from .constants import LOGGER_NAME


_logger = logging.getLogger(LOGGER_NAME)


def setup_logger():

    if _logger.handlers:
        return _logger

    _logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(

        "[%(levelname)s] %(message)s"

    )

    handler.setFormatter(formatter)

    _logger.addHandler(handler)

    return _logger


log = setup_logger()