from sqlalchemy import Column, Unicode, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from core.db import Base
from core.db.mixins import TimestampMixin


class Password(Base, TimestampMixin):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="passwords")

    password_encrypted = Column(Unicode(255), nullable=False)
    password_name = Column(Unicode(255), nullable=False)
