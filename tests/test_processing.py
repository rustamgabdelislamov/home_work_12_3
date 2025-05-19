import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("input_list, state, expected", [
    (
        [
            {'id': 1, 'state': 'EXECUTED', 'date': '2020-01-01'},
            {'id': 2, 'state': 'CANCELED', 'date': '2020-01-02'}
        ],
        'EXECUTED',
        [{'id': 1, 'state': 'EXECUTED', 'date': '2020-01-01'}]
    ),
    (
        [
            {'id': 3, 'state': 'CANCELED', 'date': '2020-01-03'},
            {'id': 4, 'state': 'EXECUTED', 'date': '2020-01-04'}
        ],
        'CANCELED',
        [{'id': 3, 'state': 'CANCELED', 'date': '2020-01-03'}]
    ),
    (
        '',
        'EXECUTED',
        'Вы ввели не список'
    ),
    (
        [
            {'id': 5, 'state': 'PENDING', 'date': '2020-01-05'},
            {'id': 6, 'state': 'FAILED', 'date': '2020-01-06'}
        ],
        'EXECUTED',
        []),
    ])
def test_filter_by_state(input_list, state, expected):
    result = filter_by_state(input_list, state)
    assert result == expected


def test_sort_by_date():
    assert sort_by_date(
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    ) == ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
