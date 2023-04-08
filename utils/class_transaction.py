class Transaction:
    def __init__(self, transaction_id, state, date, operation_amount, description, account_from, account_to):
        self.transaction_id = transaction_id
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.account_from = account_from
        self.account_to = account_to

    def __repr__(self):
        return f'Transactions({self.transaction_id}, {self.state}, {self.date}, {self.operation_amount}, ' \
               f'{self.description}, {self.account_from}, {self.account_to})'

    def reverse_date(self):
        date_and_time_separated = self.date.split('T')[0]
        date_separated = date_and_time_separated.split('-')
        date_reverse = f'{date_separated[2]}.{date_separated[1]}.{date_separated[0]}'

        return date_reverse

    def hide_and_split_bill_number_from(self):
        if self.account_from is None:
            return ''

        elif 'Счет' in self.account_from:
            bill_info = self.account_from.split(' ')[1]
            bill_info_hidden = f'Счет **{bill_info[-4:]}'
            return bill_info_hidden

        else:
            card_info = self.account_from
            card_name = ''

            if card_info.count(' ') == 1:
                card_name = card_info.split()[0]

            elif card_info.count(' ') == 2:
                card_name = ' '.join(card_info.split()[0:2])

            card_number = card_info[-16:]
            card_number = card_number.replace(card_number[6:12], '******')
            card_number_hidden = ' '.join(card_number[i*4:(i+1)*4] for i in range(4))

            return f'{card_name} {card_number_hidden}'

    def hide_and_split_bill_number_to(self):
        if 'Счет' in self.account_to:
            bill_info = self.account_to.split(' ')[1]
            bill_info_hidden = f'Счет **{bill_info[-4:]}'
            return bill_info_hidden

        else:
            card_info = self.account_to
            card_name = ''

            if card_info.count(' ') == 1:
                card_name = card_info.split()[0]

            elif card_info.count(' ') == 2:
                card_name = ' '.join(card_info.split()[0:2])

            card_number = card_info[-16:]
            card_number = card_number.replace(card_number[6:12], '******')
            card_number_hidden = ' '.join(card_number[i*4:(i+1)*4] for i in range(4))

            return f'{card_name} {card_number_hidden}'

    def show_info(self):
        print(f'{self.reverse_date()} {self.description}')
        if self.hide_and_split_bill_number_from() == '':
            print(f'{self.hide_and_split_bill_number_to()}')
        else:
            print(f'{self.hide_and_split_bill_number_from()} -> {self.hide_and_split_bill_number_to()}')

        print(f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}')
