from werkzeug.exceptions import HTTPException

from app.http.v1.error.api import ApiException
from init import create_app

app = create_app(__name__)


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, ApiException):
        return e
    if isinstance(e, HTTPException):
        msg = e.description
        code = e.code
        error_code = 10001
        return ApiException(msg, code, error_code)
    else:
        return ApiException()
