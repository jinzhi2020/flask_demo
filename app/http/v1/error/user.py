from app.http.v1.error.api import ApiException


class ValidateError(ApiException):
    code = 400
    msg = 'client is invalid'
    error_code = 10000
