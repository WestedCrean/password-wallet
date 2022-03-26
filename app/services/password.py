from typing import Optional, List, Union, NoReturn

from sqlalchemy import or_

from app.models import User, Password
from core.db import session


from app.services import CryptoService
import hashlib
import base64
import uuid


class PasswordService:
    def __init__(self):
        pass

    async def get_password_list(self, user_id: int) -> List[Password]:

        query = session.query(Password)

        query.filter(Password.user_id == user_id)

        return query.order_by(Password.id.desc()).all()

    async def get_user_password_single(self, user: User, pass_id: int) -> Password:
        password = (
            session.query(Password)
            .where(Password.user_id == user.id)
            .where(Password.id == pass_id)
            .first()
        )
        return CryptoService.decrypt_password(
            password.password_encrypted,
            user.master_password_hash,
        )  # decrypt

    async def create_password(
        self, user_id, password_plaintext: str, password_name: str
    ) -> Union[Password, NoReturn]:
        user = session.query(User).filter(User.id == user_id).first()

        password_encrypted = CryptoService.encrypt_password(
            password_plaintext,
            user.master_password_hash,
        )
        password = Password(
            user_id=user.id,
            password_encrypted=password_encrypted,
            password_name=password_name,
        )
        session.add(password)
        session.commit()
        return password
