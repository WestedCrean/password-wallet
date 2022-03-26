from core.exceptions import CustomException
from core.exceptions.error_code import ErrorCode


class LoginFailureException(CustomException):
    code = 401
    error_code = ErrorCode.Auth.IncorrectEmailOrPassword
    message = "Incorrect email or password."
