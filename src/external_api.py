import os
from dotenv import load_dotenv
import requests
from src.utils import get_accepts_the_transaction
import json

load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_to_rub(transactions: list[dict]) -> list[dict]:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            continue
        else:
            try:
                currency = transaction["operationAmount"]["currency"]["code"]
                rub = "RUB"
                amounts = float(transaction["operationAmount"]["amount"])
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={currency}&amount={amounts}"


                payload = {}
                headers = {
                    "apikey": API_KEY
                }
                print(f"API Key перед запросом: {API_KEY}")
                response = requests.request("GET", url, headers=headers, data=payload)

                status_code = response.status_code
                if status_code == 200:
                    try:
                        result = response.json()
                        converted_amount = result["result"]
                        transaction["operationAmount"]["currency"]["code"] = "RUB"
                        transaction["operationAmount"]["amount"] = converted_amount
                    except Exception as f:
                        print(f'Проблема с сервером')
            except Exception as e:
                print(f"Ошибка при запросе к API: {type(e).__name__} - {str(e)}")
        return transactions




transactions_list = get_accepts_the_transaction('../../../h_12_1/data/operations.json')
print(convert_to_rub(transactions_list))

