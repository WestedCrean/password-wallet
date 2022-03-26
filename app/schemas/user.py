from pydantic import BaseModel

from enum import Enum


class HashType(str, Enum):
    sha = "sha256"
    hmac = "hmac"


class GetUserListResponseSchema(BaseModel):
    id: int
    email: str
    master_password_hash_type: HashType

    class Config:
        orm_mode = True


class CreateUserRequestSchema(BaseModel):
    email: str
    master_password: str
    master_password_hash_type: HashType


class CreateUserResponseSchema(BaseModel):
    email: str

    class Config:
        orm_mode = True
