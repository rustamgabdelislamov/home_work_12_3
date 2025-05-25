import pandas as pd

def get_read_xlsx(path:str) -> list[dict]:
    """Функция принимает путь к excel файлу и преобразует в список словарей"""
    try:
        df = pd.read_excel(path)
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception:
        return []
