import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_operations, process_bank_search


def test_filtering_by_state(list_for_filter_by_state):
    assert filter_by_state(list_for_filter_by_state, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filtering_by_canceled_state(list_for_filter_by_state):
    assert filter_by_state(list_for_filter_by_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filtering_without_state(list_for_filter_without_state):
    assert filter_by_state(list_for_filter_without_state, "EXECUTED") == []


@pytest.mark.parametrize(
    "dict_list, state, expected",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "EXECUTED",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "CANCELED",
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
        ),
    ],
)
def test_different_state_parameter(dict_list, state, expected):
    assert filter_by_state(dict_list, state) == expected


def test_sorting_by_date(list_for_sorting_by_date):
    assert sort_by_date(list_for_sorting_by_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_reverse_sorting_by_date(list_for_sorting_by_date):
    assert sort_by_date(list_for_sorting_by_date, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_process_bank_operations_basic():
    data = [
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод организации'}
    ]

    result = process_bank_operations(data, ['Перевод организации', 'Перевод с карты на карту'])
    expected = {'Перевод организации': 2, 'Перевод с карты на карту': 1}
    assert result == expected


def test_process_bank_operations_empty():
    result = process_bank_operations([], ['Перевод организации'])
    assert result == {'Перевод организации': 0}


def test_process_bank_search_basic():
    data = [
        {'description': 'Перевод организации'},
        {'description': 'Оплата услуг'}
    ]

    result = process_bank_search(data, 'Перевод')
    assert len(result) == 1
    assert result[0]['description'] == 'Перевод организации'


def test_process_bank_search_no_matches():
    data = [{'description': 'Оплата услуг'}]
    result = process_bank_search(data, 'Перевод')
    assert result == []