from src.read_csv import get_read_csv

from unittest.mock import patch


@patch('csv.DictReader')
def test_read_csv_path_ok(mock_get):
    """Тест при правильном пути"""
    mock_get.return_value = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                              'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
                              'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                              'description': 'Перевод организации'},
                             {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
                              'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
                              'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
                              'description': 'Перевод с карты на карту'}]
    path = 'data/transactions.csv'
    result = get_read_csv(path)
    assert result == [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                       'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
                       'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                       'description': 'Перевод организации'},
                      {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
                       'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
                       'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
                       'description': 'Перевод с карты на карту'}]


def test_read_csv_path_no():
    """Тест при не правильном пути"""
    assert get_read_csv('123.csv') == []
