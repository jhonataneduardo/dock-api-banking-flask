import json


def test_resource_post_user(client, app):
    """ Test Resource POST User"""

    headers = {
        'content-type': 'application/json'
    }

    data = {
        "name": "Test Fullname",
        "cpf": "12345678912",
        "birth_date": "1991-07-13",
    }
    response = client.post("/users", data=json.dumps(data), headers=headers)
    assert 201 == response.status_code


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


def test_resource_list_accounts(client):
    """ Test Resource list Accounts"""

    response = client.get(f"/users/1/accounts")
    assert 200 == response.status_code


def test_resource_post_statement_not_parameters(client):
    """ Test Resource Statement not parameters """

    response = client.get("/users/1/accounts/1/statement")
    assert 200 == response.status_code


def test_resource_post_statement_with_parameters(client):
    """ Test Resource Statement with parameters """

    params = {
        "start_date": "2021-07-13",
        "end_date": "2021-07-15",
    }
    response = client.get("/users/1/accounts/1/statement", query_string=params)
    assert 200 == response.status_code


def test_resource_account_balance(client):
    """ Test Resource account balance """

    response = client.get("/users/1/accounts/1/balance")
    assert 200 == response.status_code


def test_resource_account_deposit(client):
    """ Test Resource account deposit """

    headers = {
        'content-type': 'application/json'
    }

    params = {
        "value": 50,
    }

    response = client.post("/users/1/accounts/1/deposit",
                           query_string=params, headers=headers)
    assert 204 == response.status_code, response.data


def test_resource_account_withdraw(client):
    """ Test Resource account withdraw """

    headers = {
        'content-type': 'application/json'
    }

    params = {
        "value": 50,
    }

    response = client.post("/users/1/accounts/1/withdraw",
                           query_string=params, headers=headers)
    assert 204 == response.status_code, response.data


def test_resource_account_block(client):
    """ Test Resource account block """

    response = client.post("/users/1/accounts/1/block")
    assert 204 == response.status_code


def test_resource_delete_account(client):
    """ Test Resource DELETE Account"""

    response = client.delete(f"/users/1/accounts/1")
    assert 204 == response.status_code
