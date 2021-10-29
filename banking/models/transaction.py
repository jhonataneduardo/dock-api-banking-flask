from sqlalchemy import func

from config.db import db
from datetime import datetime


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    account_id = db.Column(
        db.Integer,
        db.ForeignKey('accounts.id', ondelete="CASCADE")
    )
    value = db.Column(
        db.Float(precision=2)
    )
    date = db.Column(
        db.DateTime, default=datetime.now
    )

    def __init__(self, account_id, value):
        self.account_id = account_id
        self.value = value

    def json(self):
        return {'account_id': self.account_id, 'value': self.value, 'date': self.date}

    def register_transaction(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def all_by_account_id(cls, account_id):
        return cls.query.filter_by(account_id=account_id).all()

    @classmethod
    def filter_by_period(cls, start_date, end_date, account_id):
        return cls.query.filter_by(account_id=account_id).filter(func.DATE(Transaction.date) >= start_date).filter(func.DATE(Transaction.date) <= end_date).all()

    def __repr__(self):
        return f"<Transaction {self.id}>"
