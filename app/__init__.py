import flask.scaffold
import werkzeug
from flask_restx import Api, Resource
#from flask_caching import Cache
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import logging

# configure root logger
logging.basicConfig(level=logging.INFO)

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
werkzeug.cached_property = werkzeug.utils.cached_property
mongo = PyMongo()

def create_app(env=None):
    from .config import config_by_name
    from app.controllers import register_routes

    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/bd-ejemplo"
    app.config.from_object(config_by_name[env or "tests"])
    api = Api(app, title="Ejercicio Flask", version="0.1.0", prefix="/api", url_scheme="/api")

    register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    mongo.init_app(app)
    return app
