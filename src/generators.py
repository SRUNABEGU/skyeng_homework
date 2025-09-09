
def filter_by_currency(transactions: list, currency: str):
    """
    поочередно выдает транзакции, где валюта операции соответствует заданной
    :param transactions: список словарей, представляющих транзакции.
    :param currency: валюта операции
    :return: итератор, который поочередно выдает транзакции
    """
    result = (x for x in transactions if x.get('operationAmount', {}).get('currency', {}).get('code') == currency)
    return result


def transaction_descriptions(transactions: list):
    """
    принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    :param transactions: список словарей с транзакциями
    :return: описание операции
    """
    result = (x.get('description') for x in transactions)
    return result


def card_number_generator(start, stop):
    """
    выдает номера банковских карт в формате XXXX XXXX XXXX XXXX от 0000 0000 0000 0001 до 9999 9999 9999 9999
    :return:
    """
    for card_number in range(start, stop + 1):
        card_str = f"{card_number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
