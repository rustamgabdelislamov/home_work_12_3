import re


def get_mask_card_number_account(card_number_or_account: str) -> str:
    """Функция скрывающая полный номер карты или счета"""
    if isinstance(card_number_or_account, float):
        return ""
    else:
        match = re.search(r'(\w+)\s+(\d+)', card_number_or_account)
        if len(str(match.group(2))) == 16:
            return f'{match.group(1)} {match.group(2)[0:4]} {match.group(2)[4:6]}** **** {match.group(2)[12:]}'

        elif len(match.group(2)) == 20:
            return f'{match.group(1)} **{match.group(2)[-4:]}'
