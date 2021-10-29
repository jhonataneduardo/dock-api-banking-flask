from banking.models.user import User as UserModel
from banking.models.account import Account as AccountModel


def check_get_user_exists(user_id):
    user = UserModel.filter_by_id(user_id)
    if user is None:
        return {'msg': 'User not found'}, 404
    return user


def check_get_account_exists(account_id):
    account = AccountModel.filter_by_id(account_id)
    import pdb; pdb.set_trace()
    if account is None:
        return {'msg': 'Account not found'}, 404
    return account
