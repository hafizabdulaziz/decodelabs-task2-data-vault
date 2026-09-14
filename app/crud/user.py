from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash
from typing import List, Optional

async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return list(result.scalars().all())

async def create_user(db: AsyncSession, user: UserCreate) -> User:
    user_data = user.model_dump()
    password = user_data.pop("password")
    db_user = User(**user_data, hashed_password=get_password_hash(password))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate) -> Optional[User]:
    # Ensure the session doesn't expire attributes
    query = update(User).where(User.id == user_id).values(**user_update.model_dump(exclude_unset=True)).returning(User)
    result = await db.execute(query)
    await db.commit()
    user = result.scalar_one_or_none()
    if user:
        await db.refresh(user) # Explicitly refresh to avoid lazy loading issues
    return user

async def delete_user(db: AsyncSession, user_id: int) -> bool:
    result = await db.execute(delete(User).where(User.id == user_id))
    await db.commit()
    return result.rowcount > 0
