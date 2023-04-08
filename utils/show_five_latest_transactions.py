from get_last_transactions import get_five_latest_transactions
from class_transaction import Transaction


def show_five_latest_transactions():
    """
    Takes five latest transactions from 'get_five_latest_transactions' and use the methods of class to shows them.
    """
    transactions_samples_list = []

    five_latest_transactions = get_five_latest_transactions()

    for transaction in five_latest_transactions:
        if 'from' not in transaction:
            transaction['from'] = None

        transactions_samples_list.append((transaction["id"], transaction["state"], transaction["date"],
                                          transaction["operationAmount"], transaction["description"],
                                          transaction["from"], transaction["to"]))

    for sample in transactions_samples_list:
        transaction_id, state, date, operation_amount, description, account_from, account_to = sample

        transaction = Transaction(transaction_id, state, date, operation_amount, description, account_from, account_to)

        transaction.show_info()
        print('')

show_five_latest_transactions()