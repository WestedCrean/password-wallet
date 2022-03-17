from pydantic import BaseModel


class GetPasswordListResponseSchema(BaseModel):
    id: int
    password_encrypted: str

    class Config:
        orm_mode = True

class GetPasswordDecrypted(BaseModel):
    id: int
    password_plaintext: str

class CreatePasswordRequestSchema(BaseModel):
    password_plaintext: str


class CreatePasswordResponseSchema(BaseModel):
    id: int
    password_encrypted: str

    class Config:
        orm_mode = True