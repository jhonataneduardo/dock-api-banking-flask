from flask_restful import Resource, request
from flask_marshmallow import exceptions

from banking.models.user import User as UserModel
from banking.schemas.user import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserListCreate(Resource):

    def get(self):
        users_data = UserModel.all()
        return users_schema.dump(users_data), 200

    def post(self):
        # TODO: Validar CPF. Já existe nos registros? Está correto?
        try:
            user_data = user_schema.load(request.get_json())
        except exceptions.ValidationError as err:
            return err.messages, 400

        user = UserModel(**user_data)
        user.save()

        return user_schema.dump(user), 201


class UserRetrieveUpdateDestroy(Resource):
    def get(self, user_id):
        user_data = UserModel.filter_by_id(user_id)

        if user_data is None:
            return {'message': 'User not found'}, 404

        return user_schema.dump(user_data), 200

    def put(self, user_id):
        return {'message': 'Feature disabled :)'}, 410

    def delete(self, user_id):
        user_data = UserModel.filter_by_id(user_id)

        if user_data is None:
            return {'message': 'User not found'}, 404

        UserModel.delete(user_data)

        return False, 204
