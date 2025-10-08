import re
from collections import Counter

def filter_by_state(dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
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


def sort_by_date(dict_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    сортирует списки словарей по дате
    :param dict_list: список словарей
    :param reverse: порядок сортировки
    :return: отсортированный список словарей
    """

    return sorted(dict_list, key=lambda x: x["date"], reverse=reverse)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Поиск по описанию
    :param data: список словарей с данными о банковских операциях
    :param search: строка поиска
    :return: список словарей, у которых в описании есть данная строка
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    return [x for x in data if 'description' in x and pattern.search(x['description'])]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    category_counts = Counter()
    valid_categories = set(categories)

    for operation in data:
        description = operation.get('description')
        if description in valid_categories:
            category_counts[description] += 1

    return {category: category_counts.get(category, 0) for category in categories}