import pytest
import json


@pytest.fixture
def test_text():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "CANCELED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  }
]


@pytest.fixture
def test_text_2():
    return [{"id": 441945886}]


@pytest.fixture()
def executed_list():
    executed_transactions = ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                             '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075',
                             '2019-04-04T23:20:05.206878']
    return executed_transactions


@pytest.fixture()
def dates():
    return ['26.08.2019', '03.07.2019', '30.06.2018', '23.03.2018', '04.04.2019']


@pytest.fixture()
def descriptions():
    return ['Перевод организации', 'Перевод организации', 'Перевод организации', 'Открытие вклада',
            'Перевод со счета на счет']


@pytest.fixture()
def accounts_from():
    return ['Maestro 1596 83** **** 5199', 'MasterCard 7158 30** **** 6758', 'Счет **6952', '', 'Счет **8542']


@pytest.fixture()
def accounts_from_wrong():
    return ['Maestro 1596 83** **** 5199', 'MasterCard 7158 30** **** 6758', 'Счет **6952', 'Счет **8542']


@pytest.fixture()
def accounts_to():
    return ['Счет **9589', 'Счет **5560', 'Счет **6702', 'Счет **2431', 'Счет **4188']


@pytest.fixture()
def accounts_to_wrong():
    return ['Счет **9589', 'Счет **5560', 'Счет **6702', 'Счет **4188']


@pytest.fixture()
def amounts():
    return ['31957.58', '8221.37', '9824.07', '48223.05', '79114.93']


@pytest.fixture()
def currencies():
    return ["руб.", "USD", "USD", "руб.", "USD"]


@pytest.fixture()
def dates_wrong():
    return ['26.08.2019', '03.07.2019', '30.06.2018', '23.03.2018']


@pytest.fixture()
def descriptions_wrong():
    return ['Перевод организации', 'Перевод организации', 'Перевод организации', 'Открытие вклада']


@pytest.fixture()
def amounts_wrong():
    return ['31957.58', '8221.37', '9824.07', '48223.05']


@pytest.fixture()
def currencies_wrong():
    return ["руб.", "USD", "USD", "руб."]
