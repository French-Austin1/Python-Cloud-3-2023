import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler('mylog.log', when='midnight', backupCount=5)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('This is a debug message')
logger.info('This is an info message')


DEBUG = 0
INFO = 1
FATAL = 2
ERROR = 3
CRITICAL = 4 

