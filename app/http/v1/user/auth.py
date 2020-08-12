from flask import request

from . import rp
from ..validators.user import UserRegister


@rp.route('/login', methods=['GET', 'POST'])
def login():
    return 'Hello, login'


@rp.route('/register', methods=['POST'])
def register():
    validator = UserRegister(data=request.json)
    if validator.validate():
        return 'Success'
    print(validator.errors)
    return 'Error'


@rp.route('/auth')
def auth():
    return 'Hello, Auth'
