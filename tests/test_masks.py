from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account(numbers):
    assert get_mask_account('11111111111111111234') == numbers


def test_get_mask_account_len_figure(len_figure):
    assert get_mask_account('111111111111111112') == "Неправильный номер счета"


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


def test_get_mask_card_number_len_figure():
    assert get_mask_card_number('70007922896063') == 'Неправильный номер карты'
