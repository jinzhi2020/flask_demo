from flask import Flask
from app.http.v1 import bp as v1_bp
from app.http.v2 import bp as v2_bp
from app.http.v1.models.products import db


def create_app(app_name):
    app = Flask(app_name)
    _load_configs(app)
    _register_blueprint(app)
    _init_database(app)
    return app


def _load_configs(app):
    app.config.from_object('app.configs.secure')
    app.config.from_object('app.configs.setting')


def _init_database(app):
    db.init_app(app)


def _register_blueprint(app):
    app.register_blueprint(v1_bp)
    app.register_blueprint(v2_bp)
