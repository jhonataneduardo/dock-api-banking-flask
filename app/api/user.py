from flask_restful import Resource


class UserListCreate(Resource):
    def get(self):
        return {'test': 'UserListCreate'}, 200

    def post(self):
        return {'test': 'UserListCreate'}, 201


class UserRetrieveUpdateDestroy(Resource):
    def get(self, user_id):
        return {'test': 'UserRetrieveUpdateDestroy'}, 200

    def put(self, user_id):
        return {'test': 'UserRetrieveUpdateDestroy'}, 200

    def delete(self, user_id):
        return {'test': 'UserRetrieveUpdateDestroy'}, 200
