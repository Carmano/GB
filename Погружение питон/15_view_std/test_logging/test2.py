import logging


logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


logger.debug('Очень подробная отладочная информацияю Заменяем множество "принтов"')
logger.info('Немного информации')
logger.warning('Внимание! Надвигается бурая!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом все')
