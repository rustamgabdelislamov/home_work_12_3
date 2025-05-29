from datetime import datetime


def sort_date(transactions_list: list[dict], ) -> list[dict]:
    """Функция сортировки даты"""
    for transaction in transactions_list:
        date_str = transaction['date']
        if date_str.endswith('Z'):
            date_str = date_str[:-1]
        dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        transaction['date'] = dt
        transaction['formatted_date'] = dt.strftime('%d.%m.%Y')
    return transactions_list
