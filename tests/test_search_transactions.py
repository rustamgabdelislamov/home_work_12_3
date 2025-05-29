from src.search_transactions import bank_transaction_and_search_bar, counter_dict


def test_bank_transaction_and_search_bar():
    """Поиск по EXECUTED"""
    trans = [{"state": "EXECUTED", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "PENDING", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "CANCELLED", "amount": 16210.0, "description": "Перевод организации"}]
    result = [{"state": "EXECUTED", "amount": 16210.0, "description": "Перевод организации"}]
    assert (bank_transaction_and_search_bar(trans, "EXECUTED")) == result


def test_bank_transaction_and_search_bar_empty_list():
    """Тест с пустым списком входных транзакций."""
    transactions = []
    search_term = "EXECUTED"
    expected_output = f'Статус операции {search_term} недоступен.'
    result = bank_transaction_and_search_bar(transactions, search_term)
    assert result == expected_output


def test_counter_dict():
    """Тест проверяет счетчик операций транзакций если он не пуст"""
    trans = [{"state": "EXECUTED", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "PENDING", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "CANCELLED", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "CANCELLED", "amount": 16210.0, "description": "Открытие вклада"}]
    result = {"Перевод организации": 3, "Открытие вклада": 1}
    assert (counter_dict(trans, ["Перевод организации", "Открытие вклада"])) == result


def test_counter_dict_empty():
    """Тест проверяет счетчик операций транзакций если он пуст"""
    trans = [{"state": "EXECUTED", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "PENDING", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "CANCELLED", "amount": 16210.0, "description": "Перевод организации"},
             {"state": "CANCELLED", "amount": 16210.0, "description": "Открытие вклада"}]
    result = {}
    assert (counter_dict(trans, [])) == result
