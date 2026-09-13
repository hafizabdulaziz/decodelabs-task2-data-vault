from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.crud import user as crud
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await crud.create_user(db, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

@router.get("/", response_model=List[UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_db)):
    user = await crud.update_user(db, user_id, user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None
