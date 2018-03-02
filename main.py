from logger.json_logger import JsonLogger


logger = JsonLogger().get_logger(__name__)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
