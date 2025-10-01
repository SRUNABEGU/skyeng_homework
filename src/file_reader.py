import csv
import os

import pandas as pd

ABSPATH_TO_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
ABSPATH_TO_XLSX = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def csv_reader(path: str = ABSPATH_TO_CSV) -> list:
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


def xlsx_reader(path: str = ABSPATH_TO_XLSX) -> list:
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
