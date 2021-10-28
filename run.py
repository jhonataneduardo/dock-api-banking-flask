from config.server import Server


# def create_app():
#     app = Flask(__name__)
#     api = Api(app)

# TODO: Analisar...
# https://auth0.com/blog/best-practices-for-flask-api-development/


if __name__ == '__main__':
    server = Server(port=5000, debug=True)
    server.run()
