from unittest.mock import patch

from requests.cookies import MockRequest

from src.read_xlsx import get_read_xlsx


@patch('src.read_xlsx.pd.read_excel')
def test_get_read_xlsx_ok(mock_get):
    """Тест при правильном пути"""
    mock_get.return_value.to_dict.return_value = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                              'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
                              'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                              'description': 'Перевод организации'},
                             {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
                              'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
                              'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
                              'description': 'Перевод с карты на карту'}]
    path = 'data/transactions_excel.xlsx'
    result = get_read_xlsx(path)
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
    assert get_read_xlsx('123.xlsx') == []