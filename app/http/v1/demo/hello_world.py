from . import rp


@rp.route('/hello', methods=['POST'])
def hello():
    return 'Hello World'
