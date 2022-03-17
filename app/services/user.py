from typing import Optional, List, Union, NoReturn

from sqlalchemy import or_

from app.models import User
from core.db import session
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailOrNicknameException,
)

from app.services.password


class UserService:
    def __init__(self):
        pass

    async def get_user_list(self, limit: int, prev: Optional[int]) -> List[User]:
        query = session.query(User)

        if prev:
            query = query.filter(User.id < prev)

        if limit > 10:
            limit = 10

        return query.order_by(User.id.desc()).limit(limit).all()

    async def create_user(
        self, email: str, master_password_hash: str, master_password_hash_type: str
    ) -> Union[User, NoReturn]:
        if session.query(User).filter(User.email == email).first():
            raise DuplicateEmailOrNicknameException

        user = User(
            email=email,
            master_password_hash=master_password_hash,
            master_password_hash_type=master_password_hash_type,
        )
        session.add(user)

        return user

    async def update_master_password(
        self, email: str, master_password_hash: str, master_password_hash_type: str
    ) -> Union[User, NoReturn]:
        user = session.query(User).filter(User.email == email).first()

        passwords: List[Password] = (
            session.query(Password).filter(Password.user_id == user.id).all()
        )
        for password in passwords:
            # decrypt
            master_pass = user.master_password_hash # md5( .. )
            decrypted_pass = password.password_encrypted
            

        session.add(user)

        return user
