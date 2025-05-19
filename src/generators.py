from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict, None, None]:
    """
    Функция поочередно выдает транзакции, где валюта операции соответствует заданной
    """

    if not currency:
        raise ValueError("Не указана валюта")
    elif not transactions_list:
        raise ValueError("Не указан список транзакций")
    else:
        for transaction in transactions_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Generator[dict, None, None]:
    """Функция принимает список транзакций и возвращает описание операций"""
    if not transactions_list:
        raise ValueError("Не указан список транзакций")
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    if not start or start > 9999999999999999:
        raise ValueError("Числа должны быть в диапазоне от 1 до 9999999999999999")
    elif not end or end > 9999999999999999:
        raise ValueError("Числа должны быть в диапазоне от 1 до 9999999999999999")
    elif end < start:
        raise ValueError("Второе число не должно быть меньше первого")
    else:
        for number in range(start, end + 1):
            generated_number = f"{"0" * (16 - len(str(number)))}{number}"
            yield f"{generated_number[:4]} {generated_number[4:8]} {generated_number[8:12]} {generated_number[-4:]}"
