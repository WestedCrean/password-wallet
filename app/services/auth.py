from typing import Optional, List, Union, NoReturn

import hashlib
import base64
import uuid
import jwt

from sqlalchemy import or_

from app.models import User
from core.config import config
from core.db import session
from core.exceptions import (
    LoginFailureException,
)

from app.services import CryptoService, UserService


from app.schemas import HashType


class AuthService:
    def __init__(self):
        pass

    async def login(self, user_email: str, user_password: str) -> Union[str, NoReturn]:

        print("requested email: " + user_email)
        print("requested user_password: " + user_password)

        users = session.query(User).all()
        for u in users:
            print(u.email)
        user = session.query(User).filter(User.email == user_email).first()

        if not user:
            print("User not found:")
            print(user)
            raise LoginFailureException

        print("Hashing user input")
        hashed_input_password = UserService().get_password_hash_with_user_method(
            user, user_password
        )

        if hashed_input_password != user.master_password_hash:
            print("Second exception")
            print(hashed_input_password)
            print(user.master_password_hash)
            raise LoginFailureException

        credentials = {"email": user.email, "user_id": user.id}
        encoded_token = jwt.encode(
            credentials,
            config.JWT_SECRET_KEY,
            algorithm=config.JWT_ALGORITHM,
        )
        return {"auth_token": encoded_token}
