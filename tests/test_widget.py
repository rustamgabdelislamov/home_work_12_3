
import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Visa Platinum 70007922896063',  'Visa Platinum неправильный номер'),
])
def test_widget_mask(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('value_, expected_', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2024-03!11T02:26:18.671407', "Неправильный формат даты"),
])
def test_widget_get_date(value_, expected_):
    assert get_date(value_) == expected_
