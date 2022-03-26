from pydantic import BaseModel


class LoginRequestSchema(BaseModel):
    user_email: str
    user_password: str


class LoginResponseSchema(BaseModel):
    auth_token: str
