from flask import Flask
from app.http.v1 import bp as v1_bp
from app.http.v2 import bp as v2_bp


def create_app(app_name):
    app = Flask(app_name)
    _register_blueprint(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(v1_bp)
    app.register_blueprint(v2_bp)
