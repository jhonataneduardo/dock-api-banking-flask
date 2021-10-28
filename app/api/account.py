from flask_restful import Resource


class AccountListCreate(Resource):
    def get(self, user_id):
        return {'test': 'AccountList'}, 200

    def post(self, user_id):
        return {'test': 'AccountListCreate'}, 201


class AccountRetrieveUpdateDestroy(Resource):
    def get(self, account_id):
        return {'test': 'AccountDeleteGet'}, 200

    def put(self, account_id):
        return {'test': 'AccountDeleteGet'}, 200

    def delete(self, account_id):
        return {'test': 'AccountDeleteGet'}, 200
