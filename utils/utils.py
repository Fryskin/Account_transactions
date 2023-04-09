import json


def read_file(path='operations.json'):
    """
    Reading file with info about transactions and returning content from file.
    :param path: file with transactions.
    :return: content from file.
    """
    with open(path, encoding='utf-8') as file:
        content = json.load(file)

        return content


def sort_transactions(path=read_file()):
    content = path

    executed_transactions = []

    for section in content:
        if section['state'] == 'EXECUTED':
            executed_transactions.append(section)

    transactions_date = sorted(i['date'] for i in executed_transactions)
    transactions_sorted_date = sorted(transactions_date, reverse=True)[:5]

    return transactions_sorted_date


def return_sorted_transactions(path_1=read_file(), path_2=sort_transactions()):
    content = path_1
    transactions_sorted_date = path_2

    five_latest_transactions = []

    for date in range(len(transactions_sorted_date)):
        for operation in content:
            if operation['date'] == transactions_sorted_date[date]:
                five_latest_transactions.append(operation)

    return five_latest_transactions


def get_dates_and_descriptions(path=return_sorted_transactions()):
    five_latest_transactions = path

    dates = []
    descriptions = []
    for section in five_latest_transactions:
        date_separated = section['date'].split('T')[0]
        date_separated = date_separated.split('-')
        date_final = f'{date_separated[2]}.{date_separated[1]}.{date_separated[0]}'
        dates.append(date_final)

        descriptions.append(section['description'])

    return dates, descriptions


def get_accounts_from_and_accounts_to(path=return_sorted_transactions()):
    five_latest_transactions = path

    accounts_from = []
    for account_from in five_latest_transactions:
        if 'from' not in account_from:
            account_from['from'] = ''
            accounts_from.append(account_from['from'])

        elif 'Счет' in account_from['from']:
            bill_info = account_from['from'].split(' ')[1]
            bill_info_hidden = f'Счет **{bill_info[-4:]}'
            accounts_from.append(bill_info_hidden)

        else:
            card_name = account_from['from'].split(' ')
            del card_name[-1]
            card_name = ' '.join(card_name)

            card_number = account_from['from'][-16:]
            card_number = card_number.replace(card_number[6:12], '******')
            card_number_hidden = ' '.join(card_number[i*4:(i+1)*4] for i in range(4))
            accounts_from.append(f'{card_name} {card_number_hidden}')

    accounts_to = []
    for account_to in five_latest_transactions:
        bill_info = account_to['to'].split(' ')[1]
        bill_info_hidden = f'Счет **{bill_info[-4:]}'
        accounts_to.append(bill_info_hidden)

    return accounts_from, accounts_to


def get_amounts_and_currencies(path=return_sorted_transactions()):
    five_latest_transactions = path

    amounts = []
    currencies = []
    for section in five_latest_transactions:
        amounts.append(section["operationAmount"]["amount"])
        currencies.append(section["operationAmount"]["currency"]['name'])

    return amounts, currencies


def show_info_about_latest_transactions(path_1=get_dates_and_descriptions(), path_2=get_accounts_from_and_accounts_to(),
                                        path_3=get_amounts_and_currencies()):

    dates, descriptions = path_1
    accounts_from, accounts_to = path_2
    amounts, currencies = path_3

    for i in range(5):
        print(f'{dates[i]} {descriptions[i]}')

        if accounts_from[i] == '':
            print(accounts_to[i])
        else:
            print(f'{accounts_from[i]} -> {accounts_to[i]}')

        print(f'{amounts[i]} {currencies[i]}')
        print('')


print(sort_transactions())