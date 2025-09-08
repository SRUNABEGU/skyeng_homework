
def filter_by_currency(transactions, currency):
    result = (x for x in transactions if transactions[0]['operationAmount']['currency']['name'] == currency)
    return list(result)