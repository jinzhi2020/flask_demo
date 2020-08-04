from app.http.v2.user import rp


@rp.route('/login')
def login():
    return 'Hi, Login'


@rp.route('/register')
def register():
    return 'Hi, Register'


@rp.route('/auth')
def auth():
    return 'Hi, Auth'
