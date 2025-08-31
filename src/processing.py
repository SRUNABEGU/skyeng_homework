def filter_by_state(dict_list: list[dict], state="EXECUTED") -> list[dict] | None:
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


def sort_by_date(dict_list: list[dict], sort_metod=False) -> list[dict] | None:
    """
    сортирует списки словарей по дате
    :param dict_list: список словарей
    :param sort_metod: значение ключа
    :return: отсортированный список словарей
    """

    return sorted(dict_list, key=lambda x: x["date"], reverse=sort_metod)
