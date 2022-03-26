from sqlalchemy import Column, Unicode, Integer, Boolean
from sqlalchemy.orm import relationship

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(Unicode(255), nullable=False, unique=True)
    master_password_hash = Column(Unicode(255), nullable=False)
    master_password_hash_type = Column(Unicode(10), nullable=False)
    password_salt = Column(Unicode(255), nullable=False)
    is_admin = Column(Boolean, default=False)

    passwords = relationship("Password", back_populates="user")
