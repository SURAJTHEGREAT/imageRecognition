from __future__ import absolute_import
import os
from logger.log import getLogger

__all__ = [
    'create_logger'
]


def create_logger(filename):
    # GENERATE THE LOG PATH FROM CURRENT FILE NAME
    log_path = os.path.expanduser("~") + '/' + filename + '.log'
    log = getLogger(__name__, log_path)
    return log