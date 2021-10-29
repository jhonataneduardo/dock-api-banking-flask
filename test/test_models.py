from banking.models.account import Account as AccountModel
from banking.models.transaction import Transaction as TransactionModel
from banking.models.user import User as UserModel


def test_model_account():
    """ Test unit model Account """

    # user_id, balance, withdrawal_limit_day, active, type
    account = AccountModel(user_id=1, balance=1000.00,
                           withdrawal_limit_day=300.00, active=True, type=4321)

    assert account.user_id == 1
    assert account.balance == 1000.00
    assert account.withdrawal_limit_day == 300.00
    assert account.active == True
    assert account.type == 4321


def test_model_transaction():
    """ Test unit model transaction """

    # account_id, value
    transaction = TransactionModel(account_id=2, value=50.00)

    assert transaction.account_id == 2
    assert transaction.value == 50.00


def test_model_user():
    """ Test unit model user """

    # name, cpf, birth_date
    user = UserModel(name='Name Test', cpf='12345678912',
                     birth_date='1991-07-13')

    assert user.name == 'Name Test'
    assert user.cpf == '12345678912'
    assert user.birth_date == '1991-07-13'
