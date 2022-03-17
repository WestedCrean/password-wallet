from pydantic import BaseModel

from enum import Enum

class HashType(str, Enum):
    sha = 'sha256'
    hmac = 'hmac'

class GetUserListResponseSchema(BaseModel):
    id: int
    email: str
    nickname: str

    class Config:
        orm_mode = True


class CreateUserRequestSchema(BaseModel):
    email: str
    master_password_hash: str
    master_password_hash_type: HashType


class CreateUserResponseSchema(BaseModel):
    id: int
    email: str
    nickname: str

    class Config:
        orm_mode = True