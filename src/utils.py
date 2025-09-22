import json
import os

import requests
from dotenv import load_dotenv

ABSOLUTE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'operations.json')


def transaction_reader(path: str = ABSOLUTE_PATH) -> list:
    """
    читает файл в формате .JSON
    :param path: принимает на вход путь до JSON-файла
    :return: возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            result = data[0].get('operationAmount', {}).get('currency', {}).get('code')
            return result

    except (json.JSONDecodeError, FileNotFoundError, Exception):
        return []


def convert_transaction_amount(transaction: dict) -> float:
    """
    отдаёт сумму транзакции,
    :param transaction: принимает на вход транзакцию
    :return: возвращает сумму транзакции в рублях
    """

    global result
    transaction_currency = str(transaction.get('operationAmount', {}).get('currency', {}).get('code'))
    transaction_amount = float(transaction.get('operationAmount', {}).get('amount', {}))
    load_dotenv()
    api_key = os.getenv('api_key')

    if transaction.get('operationAmount', {}).get('currency', {}).get('code') in ('USD', 'EUR'):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction_currency}&amount={transaction_amount}"

        payload = {}
        headers = {
            "apikey": f"{os.getenv('api_key')}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = json.loads(response.text)
    return float(result['result'])
