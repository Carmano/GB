import logging


logger = logging.getLogger(__name__)


def log_all():
    logger.debug('Очень подробная отладочная информацияю Заменяем множество "принтов"')
    logger.info('Немного информации')
    logger.warning('Внимание! Надвигается бурая!')
    logger.error('Поймали ошибку. Дальше только неизвестность')
    logger.critical('На этом все')


if __name__ == '__main__':
    log_all()
