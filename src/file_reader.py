import csv

import pandas as pd


def csv_reader(path: str = "../data/transactions.csv") -> list:
    """
    читает csv файл
    :param path: путь к файлу
    :return: список словарей
    """
    result = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            result.append(row)
    return result


def xlsx_reader(path: str = "../data/transactions_excel.xlsx") -> list:
    """
    читает excel файл
    :param path: путь к файлу
    :return: список словарей
    """
    df = pd.read_excel(path)
    result = df.to_dict("records")
    return result


# print(csv_reader())
# print(xlsx_reader())
