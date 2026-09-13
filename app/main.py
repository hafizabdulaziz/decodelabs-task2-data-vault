from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.api import api_router
from app.core.database import engine
from app.models.user import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Cleanup if necessary

@app.get("/")
def read_root():
    return {"message": "Welcome to Data Vault API. Visit /docs for documentation."}

app = FastAPI(title="Data Vault API", lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")
