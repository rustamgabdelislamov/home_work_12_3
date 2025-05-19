from unittest.mock import patch

from src.external_api import convert_to_rub

from src.utils import get_accepts_the_transaction


@patch("src.external_api.requests.request")
def test_convert_to_rub(mock_get):
        """
        Тестирует успешную конвертацию в рубли.
        """
        mock_get.status_code = 200
        mock_get.json.return_value = {"result": 100.0}

        transactions_list = get_accepts_the_transaction('../../../h_12_1/data/operations.json')



        assert convert_to_rub(transactions_list) ==


