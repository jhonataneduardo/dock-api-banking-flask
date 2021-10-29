from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    cpf = fields.Str(required=True)
    birth_date = fields.DateTime(required=True, format='%Y-%m-%d')

    class Meta:
        ordered = True