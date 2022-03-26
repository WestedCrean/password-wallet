from .base import (
    CustomException,
    BadRequestException,
    NotFoundException,
    ForbiddenException,
    UnprocessableEntity,
    DuplicateValueException,
    UnauthorizedException,
)
from .token import DecodeTokenException, ExpiredTokenException
from .user import (
    PasswordDoesNotMatchException,
    DuplicateEmailException,
)

from .auth import LoginFailureException


__all__ = [
    "CustomException",
    "BadRequestException",
    "NotFoundException",
    "ForbiddenException",
    "UnprocessableEntity",
    "DuplicateValueException",
    "UnauthorizedException",
    "DecodeTokenException",
    "ExpiredTokenException",
    "PasswordDoesNotMatchException",
    "DuplicateEmailException",
]
