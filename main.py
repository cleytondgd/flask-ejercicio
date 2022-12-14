import os
from app import create_app

from flask import Flask
from flask_restx import Resource, Api


"""
app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        return {'hello': 'post'}
"""

app = create_app(os.getenv("FLASK_ENV") or "dev")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)