from marshmallow import Schema, fields


class TransactionSchema(Schema):
    id = fields.Int()
    account_id = fields.Int(required=True)
    value = fields.Float(required=True)
    date = fields.DateTime(format='%Y-%m-%d')

    class Meta:
        ordered = True