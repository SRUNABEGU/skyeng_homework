def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты
    :param card_number: номер карты в виде числа
    :return: строка в формате XXXX XX** **** XXXX
    """
    card_number_str = str(card_number)

    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счёта
    :rtype: str
    :param account_number: номер счёта в виде числа
    :return: строка в формате **XXXX
    """
    account_number_str = str(account_number)

    return f"{account_number_str[:2]}****"
