from typing import Optional, Tuple

import jwt
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.authentication import AuthCredentials
from starlette.requests import HTTPConnection

from core.config import config
from ..schemas import CurrentUser


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Optional[CurrentUser]]:
        print("AUTHENTICATE USER?")
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            print("not authorization")
            return False, current_user

        try:
            print("authorization: " + authorization)
            scheme, credentials = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user
        except ValueError:
            print("ValueError")
            return False, current_user

        if not credentials:
            print("not credentials")
            return False, current_user

        try:
            payload = jwt.decode(
                credentials,
                config.JWT_SECRET_KEY,
                algorithms=[config.JWT_ALGORITHM],
            )
            print(payload)
            user_id = payload.get("user_id")
        except jwt.exceptions.PyJWTError:
            print("PyJWTError")
            return False, current_user
        current_user.id = user_id
        print(f"AUTHENTICATED USER! - current_user.id =  {user_id}")
        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
