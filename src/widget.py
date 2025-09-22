from src.masks import get_mask_account_number, get_mask_card_number


def mask_account_card(card_inf: str) -> str:
    """
    обрабатывает информацию как о картах, так и о счетах.
    :param card_inf: строка, содержащая тип и номер карты или счета.
    :return: возвращает строку с замаскированным номером.
    """

    card_data = card_inf.split()
    if len(card_data) > 0:
        if len(card_data[1]) == 20:
            return f"{card_data[0]} {get_mask_account_number(int(card_data[1]))}"  # Счёт

        if len(card_data[1]) == 16:
            return f"{card_data[0]} {get_mask_card_number(int(card_data[1]))}"  # Карта1

        if card_data[1].isalpha() and len(card_data[2]) == 16:
            return f"{card_data[0]} {card_data[1]} {get_mask_card_number(int(card_data[2]))}"  # Карта2
    return "Некорректный ввод"


def get_date(date: str) -> str:
    """
    принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    :param date:
    :return: возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """

    day = date[8:10]
    month = date[5:7]
    year = date[:4]

    if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1 <= int(year) <= 9999:
        return f"{day}.{month}.{year}"
    return "Некорректный ввод"
