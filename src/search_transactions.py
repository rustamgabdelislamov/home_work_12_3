import re

from src.read_csv import get_read_csv


def bank_transaction_and_search_bar(bank_transactions: list[dict], search_bar: str) -> str | list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска и возвращает
     список словарей, у которых в описании есть данная строка."""
    banking_transactions_match = []
    pattern = re.compile(search_bar, re.IGNORECASE)
    for transaction in bank_transactions:
        state_ = transaction.get("state")
        if pattern.search(state_):
                banking_transactions_match.append(transaction)
    if banking_transactions_match != []:
        return f'Операции отфильтрованы по статусу {search_bar} {banking_transactions_match}'
    return f'Статус операции {search_bar} недоступен.'


