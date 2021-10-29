from datetime import datetime

from banking.schemas.account import AccountSchema, AccountUpdateSchema, AccountQueryParameterDepositSchema, AccountQueryParameterStatementSchema
from banking.schemas.transaction import TransactionSchema
from banking.schemas.user import UserSchema

account_schema = AccountSchema()
account_update_schema = AccountUpdateSchema()
account_query_parameter_deposit_schema = AccountQueryParameterDepositSchema()
account_query_parameter_statement_schema = AccountQueryParameterStatementSchema()
user_schema = UserSchema()
transaction_schema = TransactionSchema()


def test_account_schema():
    """ Test unit Account Schema """

    data = {
        'id': 1,
        'user_id': 3,
        'balance': 1000.00,
        'withdrawal_limit_day': 500.00,
        'active': False,
        'type': 2233,
        'date_created': '2021-08-21'
    }

    account = account_schema.load(data)

    assert isinstance(account, dict) == True
    assert account['id'] == 1
    assert account['user_id'] == 3
    assert account['balance'] == 1000.00
    assert account['withdrawal_limit_day'] == 500.00
    assert account['active'] == False
    assert account['type'] == 2233
    assert isinstance(account['date_created'], datetime)


def test_account_update_schema():
    """ Test unit Account Update Schema """

    data = {
        'id': 1,
        'balance': 1000.00,
        'withdrawal_limit_day': 500.00,
        'active': False,
        'type': 2233,
    }

    account = account_update_schema.load(data)

    assert isinstance(account, dict) == True
    assert account['id'] == 1
    assert account['balance'] == 1000.00
    assert account['withdrawal_limit_day'] == 500.00
    assert account['active'] == False
    assert account['type'] == 2233


def test_account_query_parameter_deposit_schema():
    """ Test unit Account Query Parameter Deposit Schema """

    data = {
        'value': 60.00,
    }

    account = account_query_parameter_deposit_schema.load(data)

    assert isinstance(account, dict) == True
    assert account['value'] == 60.00


def test_account_query_parameter_statement_schema():
    """ Test unit Account Statement Statement Schema """

    data = {
        'start_date': '2021-10-30',
        'end_date': '2021-10-01'
    }

    account = account_query_parameter_statement_schema.load(data)

    assert isinstance(account, dict) == True
    assert isinstance(account['start_date'], datetime)
    assert isinstance(account['end_date'], datetime)


def test_user_schema():
    """ Test unit Account User Schema """

    data = {
        'id': 1,
        'name': 'Name Test Unit',
        'cpf': '12345678912',
        'birth_date': '1991-07-13'
    }
    user = user_schema.load(data)

    assert isinstance(user, dict) == True
    assert user['id'] == 1
    assert user['name'] == 'Name Test Unit'
    assert user['cpf'] == '12345678912'
    assert isinstance(user['birth_date'], datetime)


def test_transaction_schema():
    """ Test unit Account Transaction Schema """

    data = {
        'id': 1,
        'account_id': 2,
        'value': 70.00,
        'date': '2021-07-13'
    }
    transaction = transaction_schema.load(data)

    assert isinstance(transaction, dict) == True
    assert transaction['id'] == 1
    assert transaction['account_id'] == 2
    assert transaction['value'] == 70.00
    assert isinstance(transaction['date'], datetime)
