import json
import os

def get_accepts_the_transaction(path: str) -> list[dict]:
    """Функция принимает транзакцию в json и возвращает в виде списка словарей"""
    try:
        with open(path, 'r', encoding='utf-8') as transactions_json:
            transactions = json.load(transactions_json)
            if isinstance(transactions, list) and transactions != '':
                return transactions
            return []
    except Exception:
        return []




