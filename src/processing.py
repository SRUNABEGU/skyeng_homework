def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """
    фильтрует списки словарей по ключу "state"
    :param dict_list: список словарей
    :param state: значение ключа
    :return: список словарей
    """

    result = []

    for i in dict_list:
        if i.get("state") == state:
            result.append(i)
    return result


def sort_by_date(dict_list: list, reverse: bool = False) -> list:
    """
    сортирует списки словарей по дате
    :param dict_list: список словарей
    :param reverse: порядок сортировки
    :return: отсортированный список словарей
    """

    return sorted(dict_list, key=lambda x: x["date"], reverse=not reverse)
