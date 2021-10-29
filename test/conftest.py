import pytest

from banking import create_app

# TODO: Analisar: https://testdriven.io/blog/flask-pytest/

@pytest.fixture(scope='module')
def app():
    app = create_app()
    return app