from flask_restful import Resource, request
from flask_marshmallow import exceptions

from banking.models.account import Account as AccountModel
from banking.models.user import User as UserModel
from banking.models.transaction import Transaction as TransactionModel
from banking.schemas.account import AccountSchema, AccountUpdateSchema, AccountQueryParameterDepositSchema, AccountQueryParameterStatementSchema
from banking.schemas.transaction import TransactionSchema

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
account_update_schema = AccountUpdateSchema()
account_deposit_query_parameter_schema = AccountQueryParameterDepositSchema()
account_statement_parameter_schema = AccountQueryParameterStatementSchema()
transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)


class AccountListCreate(Resource):
    def get(self, user_id):
        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        accounts = AccountModel.all()
        return accounts_schema.dump(accounts)

    def post(self, user_id):
        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        try:
            account_data = account_schema.load(request.get_json())
        except exceptions.ValidationError as err:
            return err.messages, 400

        account = AccountModel(user_id=user.id, **account_data)
        account.save()

        return account_schema.dump(account), 201


class AccountRetrieveUpdateDestroy(Resource):
    def get(self, user_id, account_id):
        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found.'}, 404

        return account_schema.dump(account), 200

    def put(self, user_id, account_id):
        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found'}, 404

        try:
            account_data = account_update_schema.load(request.get_json())
        except exceptions.ValidationError as err:
            return err.messages, 400

        account.update(account_data)

        return account_schema.dump(account), 200

    def delete(self, user_id, account_id):
        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found.'}, 404

        AccountModel.delete(account)

        return False, 204


class AccountBalanceDepositWithdraw(Resource):
    def post(self, user_id, account_id, operation):

        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found.'}, 404

        try:
            query_parameters = account_deposit_query_parameter_schema.load(
                dict(request.args))
        except exceptions.ValidationError as err:
            return err.messages, 400

        value = query_parameters['value']
        if value <= 0:
            return {'message': 'Invalid value.'}, 400

        if not account.active:
            return {'message': 'Blocked bank account.'}, 403

        if operation == 'deposit':

            account.deposit(value)

            transaction_data = transaction_schema.load(
                {'account_id': account.id, 'value': value})
            transaction = TransactionModel(**transaction_data)
            transaction.register_transaction()

            return False, 204

        if operation == 'withdraw':
            
            # TODO: Verificar limite de saque por dia.

            simulate_balance = account.balance - value
            if simulate_balance < 0:
                return {'message': 'Insufficient account balance.'}, 403

            account.withdraw(value)

            transaction_data = transaction_schema.load(
                {'account_id': account.id, 'value': -abs(value)})
            transaction = TransactionModel(**transaction_data)
            transaction.register_transaction()

            return False, 204

        return {'message': 'Operation not found.'}, 404

    def get(self, user_id, account_id, operation):
        if not operation == 'balance':
            return {'message': 'Operation not found'}, 404

        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found'}, 404

        return {'balance': account.balance}, 200


class AccountBlock(Resource):
    def post(self, user_id, account_id):

        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found.'}, 404

        account.block()

        return False, 204


class AccountStatement(Resource):
    def get(self, user_id, account_id):

        user = UserModel.filter_by_id(user_id)
        if user is None:
            return {'message': 'User not found.'}, 404

        account = AccountModel.filter_by_account_id_and_user_id(account_id, user_id)
        if account is None:
            return {'message': 'Account not found.'}, 404

        if not request.args:
            transactions = TransactionModel.all_by_account_id(account_id)
        else:
            try:
                query_parameters = account_statement_parameter_schema.load(
                    dict(request.args))
            except exceptions.ValidationError as err:
                return err.messages, 400

            start_date = query_parameters['start_date'].strftime('%Y-%m-%d')
            end_date = query_parameters['end_date'].strftime('%Y-%m-%d')

            transactions = TransactionModel.filter_by_period(
                start_date, end_date, account.id)

        return transactions_schema.dump(transactions), 200
