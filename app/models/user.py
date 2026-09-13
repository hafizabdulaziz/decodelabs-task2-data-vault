from sqlalchemy import Column, Integer, String, Boolean, DateTime, CheckConstraint, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    age = Column(Integer, CheckConstraint('age >= 0', name='check_age_non_negative'))
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
