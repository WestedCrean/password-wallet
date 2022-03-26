from .user import *
from .password import *
from .auth import *


class ExceptionResponseSchema(BaseModel):
    error: str
