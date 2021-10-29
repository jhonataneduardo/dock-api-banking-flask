from banking.models.user import User as UserModel
from banking.schemas.user import UserSchema

import json

account_schema = UserSchema()


def test_resource_post_user(client, app):
    """ Test Resource POST User"""

    headers = {
        'content-type': 'application/json'
    }

    data = {
        "name": "Carla Fonseca Pereira",
        "cpf": "13188677707",
        "birth_date": "1991-07-13",
    }
    response = client.post("/users", data=json.dumps(data), headers=headers)
    assert 201 == response.status_code
