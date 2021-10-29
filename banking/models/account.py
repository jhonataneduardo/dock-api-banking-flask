from config.db import db
from datetime import datetime


class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete="CASCADE"),
        nullable=False
    )
    balance = db.Column(
        db.Float(precision=2),
        nullable=False
    )
    withdrawal_limit_day = db.Column(
        db.Float(precision=2),
        nullable=False
    )
    active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )
    type = db.Column(
        db.Integer,
        nullable=False
    )
    date_created = db.Column(
        db.DateTime,
        default=datetime.now,
        nullable=True
    )
    transactions = db.relationship(
        'Transaction',
        backref='account',
        cascade="all,delete"
    )

    def __init__(self, user_id, balance, withdrawal_limit_day, active, type):
        self.user_id = user_id
        self.balance = balance
        self.withdrawal_limit_day = withdrawal_limit_day
        self.active = active
        self.type = type

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'balance': self.balance,
            'withdrawal_limit_day': self.withdrawal_limit_day,
            'active': self.active,
            'type': self.type,
            'creation_date': self.creation_date
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, account_data):
        for key, value in account_data.items():
            setattr(self, key, value)
        db.session.commit()

    def block(self):
        setattr(self, 'active', False)
        db.session.commit()

    @classmethod
    def delete(cls, account):
        db.session.delete(account)
        db.session.commit()

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def filter_by_account_id_and_user_id(cls, account_id, user_id):
        return cls.query.filter_by(id=account_id, user_id=user_id).first()

    def deposit(self, value):
        self.balance += value
        db.session.commit()

    def withdraw(self, value):
        self.balance -= value
        db.session.commit()

    def __repr__(self):
        return f"<Account {self.id}>"
