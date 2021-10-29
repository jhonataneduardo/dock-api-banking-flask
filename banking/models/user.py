from sqlalchemy.orm import backref
from config.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(120)
    )
    cpf = db.Column(
        db.String(11),
        unique=True
    )
    birth_date = db.Column(
        db.DateTime
    )
    accounts = db.relationship(
        'Account',
        backref='user',
        cascade="all,delete"
    )

    def __init__(self, name, cpf, birth_date):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date

    def json(self):
        return {'id': self.id, 'name': self.name, 'cpf': self.cpf, 'birth_date': self.birth_date}

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete(cls, user):
        db.session.delete(user)
        db.session.commit()

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def filter_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()

    @classmethod
    def filter_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return f"<User {self.name}>"
