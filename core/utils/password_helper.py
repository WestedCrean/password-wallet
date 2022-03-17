from datetime import datetime, timedelta
from typing import Union, NoReturn

from core.config import config
from core.exceptions import DecodeTokenException, ExpiredTokenException


class PasswordHelper:
    @staticmethod
    def hash_sha(payload:str) -> str:
        pass
    
    @staticmethod
    def hash_hmac(payload:str) -> str:
        pass

    @staticmethod
    def encrypt(payload: str, type: str) -> str:
        return payload

    @staticmethod
    def decrypt(encrypted_payload: str) -> Union[str, NoReturn]:
        try:
            return encrypted_payload
        except Exception:
            raise DecodeTokenException
