from flask import Blueprint
from app.http.v1.user import rp as user_redprint
from app.http.v1.demo import rp as demo_redprint

bp = Blueprint('v1', __name__, url_prefix='/v1')

user_redprint.register_blueprint(bp, url_prefix='/user')
demo_redprint.register_blueprint(bp, url_prefix='/demo')


