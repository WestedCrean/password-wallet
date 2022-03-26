from typing import Optional, List, Union, NoReturn

from sqlalchemy import or_

from app.models import User
from core.db import session
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailException,
)

from .crypto import CryptoService
from app.schemas import HashType


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
        self, email: str, master_password: str, master_password_hash_type: HashType
    ) -> Union[User, NoReturn]:
        if session.query(User).filter(User.email == email).first():
            raise DuplicateEmailException

        master_password_hash = ""
        user_salt = CryptoService.create_salt()
        if master_password_hash_type == HashType.sha:
            master_password_hash = CryptoService.hash_password_sha_256(
                master_password, user_salt
            )
        elif master_password_hash_type == HashType.hmac:
            master_password_hash = CryptoService.hash_password_hmac(
                master_password, user_salt
            )

        user = User(
            email=email,
            master_password_hash=master_password_hash,
            master_password_hash_type=master_password_hash_type,
            password_salt=user_salt,
        )
        session.add(user)
        session.commit()

        print("Created user in db:")
        print(user)
        print("Returning user with db")
        user = session.query(User).filter(User.email == email).first()
        print(user)
        return user

    def get_password_hash_with_user_method(self, user: User, password: str) -> str:
        if user.master_password_hash_type == HashType.sha:
            return CryptoService.hash_password_sha_256(password, user.password_salt)
        elif user.master_password_hash_type == HashType.hmac:
            return CryptoService.hash_password_hmac(password, user.password_salt)

    async def update_master_password(
        self, email: str, master_password_hash: str, master_password_hash_type: str
    ) -> Union[User, NoReturn]:
        user = session.query(User).filter(User.email == email).first()

        passwords: List[Password] = (
            session.query(Password).filter(Password.user_id == user.id).all()
        )
        for password in passwords:
            # decrypt
            master_pass = CryptoService.transform_key_for_encryption(
                user.master_password_hash
            )
            decrypted_pass = CryptoService.decrypt_password(
                password.password_encrypted, master_pass
            )

        session.add(user)
        session.commit()
        return user
