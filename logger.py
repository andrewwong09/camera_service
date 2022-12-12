import os
import sys
import logging


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, level):
       self.logger = logger
       self.level = level
       self.linebuf = ''

    def write(self, buf):
       for line in buf.rstrip().splitlines():
          self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass


def setup_logging(log_filename):
    logging.basicConfig(filename=f"{os.path.join(os.getcwd(), log_filename)}",
                        format='%(asctime)s, %(levelname)s (%(module)s): %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        encoding='utf-8',
                        level=logging.DEBUG)
    log = logging.getLogger('foobar')
    sys.stdout = StreamToLogger(log, logging.INFO)
    sys.stderr = StreamToLogger(log, logging.ERROR)
    return log
