import pytest

@pytest.fixture
def card_number():
    return '7000792289606361'

@pytest.fixture
def account_number():
    return '73654108430135874305'

@pytest.fixture
def maestro_template():
    return 'Maestro 1596837868705199'

@pytest.fixture
def mastercard_template():
    return 'MasterCard 7158300734726758'

@pytest.fixture
def visa_classic_template():
    return 'Visa Classic 6831982476737658'

@pytest.fixture
def visa_platinum_template():
    return 'Visa Platinum 8990922113665229'

@pytest.fixture
def visa_gold_template():
    return 'Visa Gold 5999414228426353'

@pytest.fixture
def account_template():
    return 'Счет 73654108430135874305'

@pytest.fixture
def date_template():
    return '2024-03-11T02:26:18.671407'
