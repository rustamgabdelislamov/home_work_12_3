from collections import Counter


def bank_transaction_and_search_bar(bank_transactions: list[dict], search_bar: str) -> str | list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска и возвращает
     список словарей, у которых в описании есть данная строка."""
    filtered_transactions = []
    search_lower = search_bar.lower()
    for transaction in bank_transactions:
        transaction_state = transaction.get("state")
        if transaction_state is not None and str(transaction_state).lower() == search_lower:
            filtered_transactions.append(transaction)
    if not filtered_transactions:
        return f'Статус операции {search_bar} недоступен.'
    return filtered_transactions


def transactions_and_descriptions(transactions: list[dict], descriptions_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска и возвращает
     список словарей, у которых в описании есть строка description"""
    descriptions_search_clean = [d.strip().lower() for d in descriptions_search.split(',')]
    if not descriptions_search_clean:
        return []
    transactions_filter = [trans for trans in transactions
                           if any(desc in trans["description"].lower() for desc in descriptions_search_clean)]
    return transactions_filter


def counter_dict(transactions: list[dict], descriptions_search: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа принимает два аргумента:
    список с транзакциями и словарь для подсчета транзакций по описанию."""
    if not descriptions_search:
        {}
    filtered_descriptions = [transaction['description'] for transaction in transactions if
                             transaction['description'] in descriptions_search]
    counted = Counter(filtered_descriptions)
    return dict(counted)
