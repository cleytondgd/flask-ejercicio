import os
from app import create_app
from flask import Flask
from flask_restx import Resource, Api

app = create_app(os.getenv("FLASK_ENV") or "dev")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)