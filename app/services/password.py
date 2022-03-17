from typing import Optional, List, Union, NoReturn

from sqlalchemy import or_

from app.models import User, Password
from core.db import session
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailOrNicknameException,
)


class PasswordService:
    def __init__(self):
        pass

    async def get_password_list(
        self, limit: int, prev: Optional[int]
    ) -> List[Password]:
        query = session.query(Password)

        if prev:
            query = query.filter(Password.id < prev)

        if limit > 10:
            limit = 10

        return query.order_by(Password.id.desc()).limit(limit).all()

    async def get_password_decrypted(self, pass_id: int) -> Password:
        password = session.query(Password).where(Password().id == pass_id).first()
        return password.password_encrypted  # decrypt

    async def create_password(
        self,
        user: User,
        password_to_encrypt: str,
    ) -> Union[Password, NoReturn]:

        user_id

        password = Password(user_id, password_encrypted)
        session.add(password)

        return password
