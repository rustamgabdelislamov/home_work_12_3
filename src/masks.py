import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая полный номер карты"""
    if len(str(card_number)) == 16:
        logger.info('Проверяем что пользователь ввел правильный номер карты')

        return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}'
    logger.error('Неправильный номер карты')
    return 'Неправильный номер карты'


def get_mask_account(account: str) -> str:
    """Функция скрывающая полный номер счета"""
    if len(account) == 20:
        logger.info('Проверяем что пользователь ввел правильный номер счета')

        return f'**{account[-4:]}'
    logger.error('Неправильный номер счета')
    return 'Неправильный номер счета'


def div(a, b):
    return a / b


print(get_mask_card_number("1234123412341234"))
print(get_mask_account("12341234123412341234"))
