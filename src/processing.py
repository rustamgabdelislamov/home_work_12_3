def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция которая возвращает список словарей с парметром 'state'"""
    if isinstance(list_dict, list):
        filter_by_state_ = [el for el in list_dict if el.get('state') == state]
        if not filter_by_state_ and list_dict == []:
            return []
        return sort_by_date(filter_by_state_)
    return 'Вы ввели не список'


def sort_by_date(filter_by_state_: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    sorted_list = sorted(filter_by_state_, key=lambda x: x['date'], reverse=reverse)
    return sorted_list
