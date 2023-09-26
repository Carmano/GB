import logging
from test_function import log_all


logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()