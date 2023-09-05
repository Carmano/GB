import logging
from test_function import log_all


logging.basicConfig(filemode='w', filename='test4_file.log', encoding='utf-8', level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
