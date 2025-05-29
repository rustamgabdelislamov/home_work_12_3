from src.new_mask import get_mask_card_number_account
from src.read_csv import get_read_csv
from src.read_xlsx import get_read_xlsx
from src.search_transactions import bank_transaction_and_search_bar, transactions_and_descriptions
from src.sort_date import sort_date
from src.utils import get_accepts_the_transaction

if __name__ == '__main__':
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('''Выберите необходимый пункт меню:
          1. Получить информацию о транзакциях из JSON-файла
          2. Получить информацию о транзакциях из CSV-файла
          3. Получить информацию о транзакциях из XLSX-файла: ''')
    input_menu = int(input())
    if input_menu == 1:
        path_file = 'data/transactions.json'
        transactions_list = get_accepts_the_transaction(path_file)
    elif input_menu == 2:
        path_file = 'data/transactions.csv'
        transactions_list = get_read_csv(path_file)
    elif input_menu == 3:
        path_file = 'data/transactions_excel.xlsx'
        transactions_list = get_read_xlsx(path_file)
    user_state = input(
        """Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: """)
    while user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {user_state} недоступен")
        user_state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ")
    transactions = bank_transaction_and_search_bar(transactions_list, user_state)
    transaction_date = sort_date(transactions)

    input_sort = input('Отсортировать операции по дате? Да/Нет')
    input_sort_lower = input_sort.lower()
    while input_sort_lower not in ['да', 'нет']:
        input_sort = input('Отсортировать операции по дате? Да/Нет')
        input_sort_lower = input_sort.lower()
        if input_sort_lower == 'да':
            input_sort_true = input('Отсортировать по возрастанию или по убыванию?')
            input_sort_true_lower = input_sort_true.lower()
            if input_sort_true_lower == 'по возрастанию':
                transaction_date_sort = sorted(transaction_date, key=lambda x: x['date'])
                transaction_date = transaction_date_sort
            elif input_sort_true_lower == 'по убыванию':
                transaction_date_sort_ = sorted(transaction_date, key=lambda x: x['date'], reverse=True)
                transaction_date = transaction_date_sort_

    input_rub_transactions = input('Выводить только рублевые транзакции? Да/Нет')
    input_rub_transactions_lower = input_rub_transactions.lower()
    while input_rub_transactions_lower not in ['да', 'нет']:
        input_rub_transactions = input('Выводить только рублевые транзакции? Да/Нет')
        input_rub_transactions_lower = input_rub_transactions.lower()
        if input_rub_transactions == 'да':
            transaction_date = [t for t in transaction_date if t.get('currency_code') == 'RUB']

    input_filter_search = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    input_filter_search_lower = input_filter_search.lower()

    if input_filter_search_lower == 'да':
        input_search = input('Доступные слова для поиска: Перевод организации, Перевод с карты на карту,'
                             'Открытие вклада, Перевод со счета на счет')
        input_search_lower = input_search.lower()
        transaction_filter = transactions_and_descriptions(transaction_date, input_search_lower)
        transaction_date = transaction_filter
        print(transaction_date)
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке {len(transaction_date)}')
    for transaction in transaction_date:
        date = transaction["formatted_date"]
        description = transaction["description"]
        from_account = get_mask_card_number_account(transaction["from"]) if transaction["from"] else ""
        to_account = get_mask_card_number_account(transaction["to"])
        amount = transaction["amount"]
        currency = transaction["currency_code"]
        if transaction["description"] == 'Открытие вклада':
            print(f"{date} {description}\n{to_account}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n")
