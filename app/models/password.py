from sqlalchemy import Column, Unicode, BigInteger, Boolean

from core.db import Base
from core.db.mixins import TimestampMixin


class Password(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    password_encrypted = Column(Unicode(255), nullable=False)
