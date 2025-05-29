import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_accepts_the_transaction(path: str) -> list[dict]:
    """Функция принимает транзакцию в json и возвращает в виде списка словарей"""
    try:
        logger.info('Открываем транзакцию')
        with open(path, 'r', encoding='utf-8') as transactions_json:
            transactions_api = json.load(transactions_json)

            logger.info('Проверяем что транзакция список и он не пустой')
            if isinstance(transactions_api, list) and transactions_api != '':
                return transactions_api

            logger.warning('Транзакция не список')
            return []
    except FileNotFoundError as ex:
        logging.error(f'Произошла ошибка {ex}')
        return []
    except json.JSONDecodeError as ex:
        logging.error(f'Произошла ошибка {ex}')
        return []
