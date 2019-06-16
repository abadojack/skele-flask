from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from api import api_blueprint

from config import AppConfig


api = Api(api_blueprint, doc=False)


def create_app(config=AppConfig):
    """Return app object given config object."""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    return app
