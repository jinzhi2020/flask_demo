from flask import Blueprint
from app.http.v2.user import rp as user_redprint

bp = Blueprint('v2', __name__, url_prefix='/v2')

user_redprint.register_blueprint(bp, url_prefix='user')
