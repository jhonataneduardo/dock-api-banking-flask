from config.db import db, init_dataload_db
from config.ma import ma

import click

from flask import Flask
from flask.cli import AppGroup
from flask_restful import Api

from banking.resources.account import AccountListCreate, AccountRetrieveUpdateDestroy, AccountBalanceDepositWithdraw, AccountBlock, AccountStatement
from banking.resources.user import UserListCreate, UserRetrieveUpdateDestroy

from banking.models.user import User as UserModel


def create_app():

    # init app
    app = Flask(__name__)

    # config database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
    db.init_app(app)

    # init marshmallow
    ma.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    # route index
    @app.route("/", methods=['GET'])
    def index():
        return {
            "project": "Dock Tech API Flask",
            "author": "Jhonatan Eduardo <jhonatanepp@gmail.com>",
            "link": "https://github.com/jhonataneduardo/dock-api-banking-flask"
        }

    # register resource
    api = Api(app)
    api.add_resource(
        UserListCreate,
        '/users'
    )
    api.add_resource(
        UserRetrieveUpdateDestroy,
        '/users/<int:user_id>'
    )
    api.add_resource(
        AccountListCreate,
        '/users/<int:user_id>/accounts'
    )
    api.add_resource(
        AccountRetrieveUpdateDestroy,
        '/users/<int:user_id>/accounts/<int:account_id>'
    )
    api.add_resource(
        AccountBalanceDepositWithdraw,
        '/users/<int:user_id>/accounts/<int:account_id>/<string:operation>'
    )
    api.add_resource(
        AccountStatement,
        '/users/<int:user_id>/accounts/<int:account_id>/statement'
    )
    api.add_resource(
        AccountBlock,
        '/users/<int:user_id>/accounts/<int:account_id>/block'
    )

    return app


user_cli = AppGroup('dataload')

@user_cli.command('createuser')
@click.argument('name')
def dataload(name):
    import datetime
    brith_date_datetime = datetime.datetime.strptime('1991-07-13', '%Y-%m-%d')
    msg = init_dataload_db(app, id=1, name=name, cpf="12345678912", birth_date=brith_date_datetime)
    print(msg)

app = create_app()
app.cli.add_command(user_cli)