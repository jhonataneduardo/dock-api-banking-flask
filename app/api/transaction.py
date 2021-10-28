from flask_restful import Resource


class TransactionListCreate(Resource):
    def get(self, user_id, account_id):
        return {'test': 'TransactionListCreate'}, 200

    def post(self, user_id, account_id):
        return {'test': 'TransactionListCreate'}, 201


class TransactionRetrieveUpdateDestroy(Resource):
    def get(self, user_id, account_id, transaction_id):
        return {'test': 'TransactionRetrieveUpdateDestroy'}, 200

    def put(self, user_id, account_id, transaction_id):
        return {'test': 'TransactionRetrieveUpdateDestroy'}, 200

    def delete(self, user_id, account_id, transaction_id):
        return {'test': 'TransactionRetrieveUpdateDestroy'}, 200
