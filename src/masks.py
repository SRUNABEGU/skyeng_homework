import logging
import os

ABSPATH_TO_LOG = os.path.join(os.path.dirname(__file__), "..", "logs", "masks.log")

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(ABSPATH_TO_LOG, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты
    :param card_number: номер карты в виде числа
    :return: строка в формате XXXX XX** **** XXXX
    """

    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        logger.debug("Маскируется номер карты")
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
    return "Некорректный ввод"


def get_mask_account_number(account_number: int) -> str:
    """
    Маскирует номер счёта
    :rtype: str
    :param account_number: номер счёта в виде числа
    :return: строка в формате **XXXX
    """

    account_number_str = str(account_number)
    if len(account_number_str) == 20:
        logger.debug("Маскируется номер счёта")
        return f"**{account_number_str[-4:]}"
    return "Некорректный ввод"


get_mask_card_number(1234567890123456)
get_mask_account_number(12345678901234567890)
