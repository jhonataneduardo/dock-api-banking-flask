from banking.models.user import User as UserModel
from banking.schemas.user import UserSchema

import json

account_schema = UserSchema()


def test_resource_post_account(client):
    """ Test Resource POST Account"""

    headers = {
        'content-type': 'application/json'
    }

    data = {
        "balance": 600.00,
        "withdrawal_limit_day": 100.00,
        "active": True,
        "type": 1234,
    }
    response = client.post(f"/users/1/accounts",
                           data=json.dumps(data), headers=headers)
    assert 201 == response.status_code


def test_resource_update_account(client):
    """ Test Resource UPDATE Account"""

    headers = {
        'content-type': 'application/json'
    }

    data = {
        "balance": 500.00,
        "withdrawal_limit_day": 100.00,
        "active": True,
        "type": 1234,
    }
    response = client.put("/users/1/accounts/1",
                           data=json.dumps(data), headers=headers)
    assert 200 == response.status_code


def test_resource_delete_account(client):
    """ Test Resource DELETE Account"""

    response = client.delete(f"/users/1/accounts/9")
    assert 204 == response.status_code


def test_resource_list_accounts(client):
    """ Test Resource LIST Accounts"""

    response = client.get(f"/users/1/accounts")
    assert 200 == response.status_code
