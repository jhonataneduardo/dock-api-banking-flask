from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime

db = SQLAlchemy()


def init_dataload_db(app, **kwargs):
    with app.app_context():

        # init tables
        db.create_all()

        try:
            # create user
            user_data = (kwargs,)
            user_query = text(
                """INSERT INTO users (id, name, cpf, birth_date) VALUES(:id, :name, :cpf, :birth_date)""")
            conn = db.session.connection()
            conn.execute(user_query, user_data)

            # create account
            date_created_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            account_data = {"id": 1, "user_id": 1, "balance": 1000.00,
                            "withdrawal_limit_day": 100.00, "active": True, "type": 1234, "date_created": date_created_datetime}
            account_query = text(
                """INSERT INTO accounts (id, user_id, balance, withdrawal_limit_day, active, type, date_created) VALUES(:id, :user_id, :balance, :withdrawal_limit_day, :active, :type, :date_created)""")
            conn = db.session.connection()
            conn.execute(account_query, account_data)

            db.session.commit()
        except SQLAlchemyError as err:
            return f"Ocorreu algum erro :(. Confere ai: {err}"

    return "Success :D"
