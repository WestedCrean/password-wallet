from typing import Optional, List, Union, NoReturn
import os

import hashlib
import base64
import uuid
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
        encryption_key = hashlib.md5(master_key.encode())
        print("Number of bytes in a string:", len(encryption_key.digest()))
        # encrypt using AES with cryptography package
        cipher = Cipher(
            algorithms.AES(encryption_key.digest()),
            modes.CBC(b"\x00" * 16),
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(password.encode()) + encryptor.finalize()
        return base64.b64encode(ciphertext).decode()

    @staticmethod
    def decrypt_password(password: str, master_key: str) -> Optional[str]:
        # decrypt password with master key
        encryption_key = hashlib.md5(master_key.encode())
        # decrypt using AES with cryptography package
        cipher = Cipher(
            algorithms.AES(encryption_key.digest()),
            modes.CBC(b"\x00" * 16),
        )
        decryptor = cipher.decryptor()
        ciphertext = base64.b64decode(password)
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()
