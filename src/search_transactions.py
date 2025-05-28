import re

from collections import Counter


def bank_transaction_and_search_bar(bank_transactions: list[dict], search_bar: str) -> str | list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска и возвращает
     список словарей, у которых в описании есть данная строка."""
    banking_transactions_match = []
    pattern = re.compile(search_bar, re.IGNORECASE)
    for transaction in bank_transactions:
        state_ = transaction.get("state")
        if pattern.search(str(state_)):
            keys_to_keep = ['date', 'amount', 'from', 'to', 'description', 'currency_code']
            filtered_transactions = {key: transaction.get(key) for key in keys_to_keep}
            banking_transactions_match.append(filtered_transactions)
    if banking_transactions_match != []:
        print (f'Операции отфильтрованы по статусу {search_bar}')
        return banking_transactions_match
    return f'Статус операции {search_bar} недоступен.'


def transactions_and_descriptions(transactions: list[dict], descriptions_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска и возвращает
     список словарей, у которых в описании есть строка description"""
    descriptions_search_clean = [d.strip().lower() for d in descriptions_search.split(',')]
    transactions_filter = [trans for trans in transactions
                           if any(desc in trans["description"].lower() for desc in descriptions_search_clean)]
    return transactions_filter


def counter_dict(transactions: list[dict], descriptions_search: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа принимает два аргумента:
    список с транзакциями и словарь для подсчета транзакций по описанию."""
    filtered_descriptions = [transaction['description'] for transaction in transactions if
                            transaction['description'] in descriptions_search]
    counted = Counter(filtered_descriptions)
    return dict(counted)

















