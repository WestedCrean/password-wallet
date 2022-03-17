from sqlalchemy import Column, Unicode, BigInteger, Boolean

from core.db import Base
from core.db.mixins import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    
    email = Column(Unicode(255), nullable=False, unique=True)
    master_password_hash = Column(Unicode(255), nullable=False)
    master_password_hash_type = Column(Unicode(10), nullable=False)
    is_admin = Column(Boolean, default=False)