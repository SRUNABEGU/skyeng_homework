def filter_by_state(dict_list: list[dict], state="EXECUTED") -> list[dict]:
    """
    фильтрует списки словарей по ключу "state"
    :param dict_list: список словарей
    :param state: значение ключа
    :return: список словарей
    """

    result = []

    for i in dict_list:
        if i.get('state') == state:
            result.append(i)
    return result


def sort_by_date(dict_list: list[dict], reverse=False) -> list[dict]:
    """
    сортирует списки словарей по дате
    :param dict_list: список словарей
    :param sort_metod: значение ключа
    :return: отсортированный список словарей
    """

    return sorted(dict_list, key=lambda x: x["date"], reverse = not reverse)

# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], True))
