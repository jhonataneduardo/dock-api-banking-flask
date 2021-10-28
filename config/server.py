from flask import Flask
from flask_restful import Api

from app.routes import routes_app


class Server:

    def __init__(self, port=5000, debug=True):

        self._port = port
        self._debug = debug

        self.app = Flask(__name__)
        self.api = Api(self.app)

        routes_app(self.api)

    def run(self):
        return self.app.run(port=self._port, debug=self._port)
