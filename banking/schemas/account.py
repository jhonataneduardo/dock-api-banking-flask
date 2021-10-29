from marshmallow import Schema, fields


class AccountSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    balance = fields.Float(required=False)
    withdrawal_limit_day = fields.Float(required=False)
    active = fields.Bool()
    type = fields.Int(required=False)
    date_created = fields.DateTime(format='%Y-%m-%d')

    class Meta:
        ordered = True


class AccountUpdateSchema(Schema):
    id = fields.Int()
    balance = fields.Float(required=False)
    withdrawal_limit_day = fields.Float(required=False)
    active = fields.Bool()
    type = fields.Int(required=False)

    class Meta:
        ordered = True


class AccountQueryParameterDepositSchema(Schema):
    value = fields.Float(
        required=True,
        error_messages={
            'required': 'Missing data for required query parameter.',
            'invalid': 'Not a valid number. Float type required.',
        })


class AccountQueryParameterStatementSchema(Schema):
    start_date = fields.DateTime(
        required=True,
        error_messages={
            'required': 'Missing data for required query parameter.',
            'invalid': 'Not a valid number. Date type required. Example: 14-02-2019',
        },
        format='%Y-%m-%d'
    )
    end_date = fields.DateTime(
        required=True,
        error_messages={
            'required': 'Missing data for required query parameter.',
            'invalid': 'Not a valid number. Date type required. Example: 14-02-2019',
        },
        format='%Y-%m-%d'
    )
