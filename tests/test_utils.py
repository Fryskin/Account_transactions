from utils.utils import sort_transactions, return_sorted_transactions, get_dates_and_descriptions,\
                        get_accounts_from_and_accounts_to, get_amounts_and_currencies,\
                        show_info_about_latest_transactions


def test_sort_transactions(test_text, test_text_2, executed_list):
    assert TypeError, sort_transactions('')
    assert sort_transactions(test_text) == executed_list[0:4]
    assert KeyError, sort_transactions(test_text_2)


def test_return_sorted_transactions(test_text, test_text_2, executed_list):
    assert return_sorted_transactions('') == []
    assert return_sorted_transactions(test_text, executed_list) == test_text
    assert KeyError, return_sorted_transactions(test_text_2)
    assert TypeError, return_sorted_transactions([1, 2, 3])


def test_get_dates_and_descriptions(test_text, dates, descriptions, test_text_2):
    assert get_dates_and_descriptions('') == ([], [])
    assert get_dates_and_descriptions(test_text) == (dates, descriptions)
    assert KeyError, get_dates_and_descriptions(test_text_2)
    assert TypeError, get_dates_and_descriptions([1, 2, 3])


def test_get_accounts_from_and_accounts_to(test_text, test_text_2, accounts_from, accounts_to, accounts_from_wrong,
                                           accounts_to_wrong):

    assert get_accounts_from_and_accounts_to('') == ([], [])
    assert get_accounts_from_and_accounts_to(test_text) == (accounts_from, accounts_to)
    assert get_accounts_from_and_accounts_to(test_text) != (accounts_from_wrong, accounts_to_wrong)
    assert KeyError, get_accounts_from_and_accounts_to(test_text_2)
    assert TypeError, get_accounts_from_and_accounts_to([1, 2, 3])


def test_get_amounts_and_currencies(test_text, test_text_2, amounts, currencies):

    assert get_amounts_and_currencies(test_text) == (amounts, currencies)
    assert get_amounts_and_currencies('') == ([], [])
    assert KeyError, get_amounts_and_currencies(test_text_2)
    assert TypeError, get_amounts_and_currencies([1, 2, 3])


def test_show_info_about_latest_transactions(dates_wrong, descriptions_wrong, accounts_from_wrong, accounts_to_wrong,
                                             amounts_wrong, currencies_wrong):
    assert IndexError, show_info_about_latest_transactions((dates_wrong, descriptions_wrong),
                                                           (accounts_from_wrong, accounts_to_wrong),
                                                           (amounts_wrong, currencies_wrong))

    assert ValueError, show_info_about_latest_transactions('', '', '')
    assert ValueError, show_info_about_latest_transactions(dates_wrong, descriptions_wrong, amounts_wrong)
