import pytest

from src.masks import get_mask_card_number, get_mask_account_number


def test_correct_card_number_mask(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


@pytest.mark.parametrize('value, expected', [
    ('70007922896063611', 'Некорректный ввод'),
    ('', 'Некорректный ввод'),
])
def test_unexpected_card_number_mask(value, expected):
    assert get_mask_card_number(value) == expected


def test_correct_account_number_mask(account_number):
    assert get_mask_account_number(account_number) == '**4305'


@pytest.mark.parametrize('value, expected', [
    ('736541084301358743055', 'Некорректный ввод'),
    ('', 'Некорректный ввод'),
])
def test_unexpected_account_number_mask(value, expected):
    assert get_mask_account_number(value) == expected
