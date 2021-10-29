import pytest
import tempfile
import os

from banking import create_app
from config.db import db


@pytest.fixture(scope='module')
def app():
    db_fd, db_fname = tempfile.mkstemp()

    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.config["TESTING"] = True

    db.session.remove()
    os.close(db_fd)
    os.unlink(db_fname)

    return app
