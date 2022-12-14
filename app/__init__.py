import flask.scaffold
import werkzeug
from flask_restx import Api, Resource
#from flask_caching import Cache
from flask import Flask, jsonify

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
werkzeug.cached_property = werkzeug.utils.cached_property
"""
users_cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
institution_cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
"""

def create_app(env=None):
    '''
    Method to initialise flask app and setting up Api gateway
    Then it configures both users_cache & institution_cache(data store)
    '''
    from .config import config_by_name
    from app.controllers import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "tests"])
    api = Api(app, title="Ejercicio Flask", version="0.1.0", prefix="/api", url_scheme="/api")
    """
    users_cache.init_app(app)
    institution_cache.init_app(app)
    """
    register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
