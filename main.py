import json
import logging


class LoggerHandler(logging.Handler):
    def emit(self, record):
        f = self.format(record)
        print(f'{f}')


class SimpleJsonFormatter(logging.Formatter):
    def format(self, record):
        ret = {}

        for attr, value in record.__dict__.items():
            if attr == 'asctime':
                value = self.formatTime(record)
            if attr == 'exc_info' and value is not None:
                value = self.formatException(value)
            if attr == 'stack_info' and value is not None:
                value = self.formatStack(value)
            ret[attr] = value

        return json.dumps(ret)


logger = logging.getLogger('test')

handler = LoggerHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(SimpleJsonFormatter())

logger.addHandler(handler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
