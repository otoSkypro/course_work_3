import os
import pytest
from utils import load_operations, sort_operations_by_date, get_executed_only, hide_requisites, formate_for_output
from main import ROOT_PATH


@pytest.fixture
def operation_card_to_account():
    operation_info = {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
    }
    return operation_info

@pytest.fixture
def operation_cash_to_account():
    operation_info = {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 72731966109147704472"
    }
    return operation_info


def test_load_operations():
    test_data_path = os.path.join(ROOT_PATH, 'tests', 'data_for_test.json')

    assert load_operations(test_data_path) == [1, 2, 3]


def test_sort_operations():
    data = [
        {
            "date": "2018-07-11T02:26:18.671407"
        },
        {
            "date": "2019-07-11T02:26:18.671407"
        }
    ]

    expected = [
        {
            "date": "2019-07-11T02:26:18.671407"
        },
        {
            "date": "2018-07-11T02:26:18.671407"
        }
    ]
    assert sort_operations_by_date(data) == expected


def test_get_executed():
    data = [
        {
            'state': 'EXECUTED',
        },
        {
            'state': 'CANCELED',
        },
        {
            'state': 'EXECUTED',
        },
        {
            'state': 'EXECUTED',
        }
    ]
    assert len(get_executed_only(data)) == 3
    assert len(get_executed_only(data, 2)) == 2


def test_hide_req_account():
    account_number = "Счет 72082042523231456215"
    assert hide_requisites(account_number) == "Счет **6215"


def test_hide_req_card():
    card_number = "Visa Classic 6831982476737658"
    assert hide_requisites(card_number) == "Visa Classic 6831 98** **** 7658"


def test_formate_card_to_account(operation_card_to_account):
    expected = ("04.04.2018 Перевод организации\n"
                "Visa Gold 5999 41** **** 6353 -> Счет **4472\n"
                "40701.91 USD")
    assert formate_for_output(operation_card_to_account) == expected

def test_formate_cash_to_account(operation_cash_to_account):
    expected = ("04.04.2018 Перевод организации\n"
                "Наличный взнос -> Счет **4472\n"
                "40701.91 USD")
    assert formate_for_output(operation_cash_to_account) == expected
