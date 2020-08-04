from . import rp


@rp.route('/login', methods=['GET', 'POST'])
def login():
    return 'Hello, login'


@rp.route('/register')
def register():
    return 'Hello, Register'


@rp.route('/auth')
def auth():
    return 'Hello, Auth'
