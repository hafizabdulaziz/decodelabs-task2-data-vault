import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import get_db
from app.models.user import Base
import os

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.fixture(scope="function")
async def db_engine():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest.fixture
async def db_session(db_engine):
    async with db_engine.connect() as connection:
        # Start a transaction for each test
        transaction = await connection.begin()
        # Bind the session to the connection, not the engine, for atomic transactions
        session = AsyncSession(bind=connection, join_transaction_mode="create_savepoint")
        
        yield session
        
        # Clean up
        await session.close()
        # Rollback the transaction to ensure the DB remains clean
        await transaction.rollback()
        await connection.close()

@pytest.fixture
async def client(db_session):
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()
