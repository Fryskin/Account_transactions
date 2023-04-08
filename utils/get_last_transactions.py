from read_file import read_json_file


def get_five_latest_transactions():
    """
    Takes all info from def 'read_json_file' and returning five latest transactions.
    :return: five latest transactions.
    """
    executed_transactions = []
    five_latest_transactions = []

    content = read_json_file('operations.json')

    for dicts in content:
        if dicts['state'] == 'EXECUTED':
            executed_transactions.append(dicts)

    date_and_time = []

    for transaction in executed_transactions:
        date_and_time.append(transaction['date'])

    date_sorted = sorted(date_and_time, reverse=True)
    date_sorted = date_sorted[0:6]

    index = 0
    while index < 5:
        for transaction in executed_transactions:
            if transaction['date'] in date_sorted[index]:
                five_latest_transactions.append(transaction)
                index += 1

    return five_latest_transactions
