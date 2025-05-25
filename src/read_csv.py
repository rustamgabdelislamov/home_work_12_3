import csv


def get_read_csv(path:str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла"""

    try:
        transactions = []
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                transaction = {
                    'id': row['id'],
                    'state': row['state'],
                    'date': row['date'],
                    'amount': row['amount'],
                    'currency_name': row['currency_name'],
                    'currency_code': row['currency_code'],
                    'from': row['from'],
                    'to': row['to'],
                    'description': row['description']
                }
                transactions.append(transaction)
        return transactions
    except Exception:
        return []




