from typing import Optional, List, Union, NoReturn
import os

import hashlib
import base64
import uuid
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet


class CryptoService:
    def __init__(self):
        pass

    @staticmethod
    def create_salt() -> str:
        return base64.urlsafe_b64encode(uuid.uuid4().bytes)

    @staticmethod
    def hash_password_sha_256(password: str, salt: str) -> str:
        t_sha = hashlib.sha512()
        t_sha.update(password.encode() + salt)
        return t_sha.hexdigest()

    @staticmethod
    def hash_password_hmac(password: str, salt: str) -> str:
        t_hmac = hmac.new(key.encode(), password.encode(), hashlib.sha256)
        return t_hmac.hexdigest()

    @staticmethod
    def transform_key_for_encryption(master_key: str) -> str:
        return master_key

    @staticmethod
    def encrypt_password(password: str, master_key: str) -> str:
        encryption_key = hashlib.md5(master_key.encode("utf-8"))
        concat = hashlib.sha256()
        concat.update(encryption_key.digest())
        concat.update(encryption_key.digest())
        encryption_key = base64.b64encode(concat.digest())[:44]
        f = Fernet(encryption_key)
        return f.encrypt(password.encode("utf-8"))

    @staticmethod
    def decrypt_password(password: str, master_key: str) -> Optional[str]:
        encryption_key = hashlib.md5(master_key.encode("utf-8"))
        concat = hashlib.sha256()
        concat.update(encryption_key.digest())
        concat.update(encryption_key.digest())
        encryption_key = base64.b64encode(concat.digest())[:44]
        f = Fernet(encryption_key)
        return f.decrypt(password.encode("utf-8"))
