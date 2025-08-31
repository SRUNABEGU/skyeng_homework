import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


@pytest.mark.parametrize('value, expected', [
    ('70007922896063611', 'Некорректный ввод'),
    ('', 'Некорректный ввод')
])
def test_unexpected_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == '**4305'




