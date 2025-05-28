from unittest.mock import patch

import pytest

from src.search_transactions import bank_transaction_and_search_bar


def test_bank_transaction_and_search_bar():
    """Поиск по EXECUTED"""
    transactions = [
        {
            "state": "EXECUTED",
            "description": "Перевод организации",
            "date": "2023-01-01",
            "amount": "100.00",
            "from": "Счет А",
            "to": "Организация",
            "currency_code": "RUB"
        },
        {
            "state": "EXECUTED",
            "description": "Перевод с карты на карту",
            "date": "2023-01-02",
            "amount": "500.00",
            "from": "Карта 1",
            "to": "Карта 2",
            "currency_code": "RUB"
        },
        {
            "state": "CANCELED",
            "description": "Перевод с карты на карту",
            "date": "2023-01-03",
            "amount": "200.00",
            "from": "Карта 3",
            "to": "Карта 4",
            "currency_code": "RUB"
        },
        {
            "state": "pending",  # Проверяем регистронезависимость
            "description": "Запрос на перевод",
            "date": "2023-01-04",
            "amount": "75.00",
            "from": "Счет В",
            "to": "Счет С",
            "currency_code": "USD"
        }
    ]

    result = bank_transaction_and_search_bar(transactions,"EXECUTED")
    assert result == [
        {
            "date": "2023-01-01",
            "amount": "100.00",
            "from": "Счет А",
            "to": "Организация",
            "description": "Перевод организации",
            "currency_code": "RUB"
        },
        {
            "date": "2023-01-02",
            "amount": "500.00",
            "from": "Карта 1",
            "to": "Карта 2",
            "description": "Перевод с карты на карту",
            "currency_code": "RUB"
        }
    ]


def test_bank_transaction_and_search_bar_empty_list():
    """Тест с пустым списком входных транзакций."""
    transactions = []
    search_term = "EXECUTED"
    expected_output = f'Статус операции {search_term} недоступен.'
    result = bank_transaction_and_search_bar(transactions, search_term)
    assert result == expected_output