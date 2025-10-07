import json
import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

ABSPATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
ABSPATH_TO_LOG = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(ABSPATH_TO_LOG, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_file_reader(path: str = ABSPATH_TO_FILE) -> list:
    """
    читает файл в формате .JSON
    :param path: принимает на вход путь до JSON-файла
    :return: возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                logger.error("Содержимое файла не является списком")
                return []
            logger.debug("Файл успешно найден")
            return data

    except (json.JSONDecodeError, FileNotFoundError, Exception) as error:
        logger.error(f"Ошибка {error}")
        return []


def convert_transaction_amount(transaction: dict) -> str | float:
    """
    отдаёт сумму транзакции,
    :param transaction: принимает на вход транзакцию
    :return: возвращает сумму транзакции в рублях
    """
    try:
        print("Выполняется запрос...")
        transaction_currency = str(transaction.get("operationAmount", {}).get("currency", {}).get("code"))
        transaction_amount = transaction.get("operationAmount", {}).get("amount", '0')
        if transaction_currency not in ("USD", "EUR"):
            return float(transaction_amount)
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&"
            f"from={transaction_currency}&amount={transaction_amount}"
        )
        payload = {}
        headers = {"apikey": f"{os.getenv('API_KEY')}"}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.debug(f"Запрос к API с конвертацией {transaction_amount} {transaction_currency} в рубли")
        result = json.loads(response.text)
        logger.debug(f'Успешная работа функции, результат: {result["result"]} рублей')
        return float(result["result"])

    except Exception as error:
        logger.error(f"Ошибка: {error}")
        return f"Ошибка: {error}"