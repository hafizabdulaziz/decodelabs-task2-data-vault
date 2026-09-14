import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    response = await client.post("/api/v1/users/", json={"email": "test@example.com", "age": 25, "password": "password123"})
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"

@pytest.mark.asyncio
async def test_create_duplicate_user(client: AsyncClient):
    await client.post("/api/v1/users/", json={"email": "dup@example.com", "age": 25, "password": "password123"})
    response = await client.post("/api/v1/users/", json={"email": "dup@example.com", "age": 30, "password": "password123"})
    assert response.status_code == 409

@pytest.mark.asyncio
async def test_read_users(client: AsyncClient):
    await client.post("/api/v1/users/", json={"email": "list1@example.com", "age": 20, "password": "password123"})
    response = await client.get("/api/v1/users/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

@pytest.mark.asyncio
async def test_update_user(client: AsyncClient):
    create_res = await client.post("/api/v1/users/", json={"email": "update@example.com", "age": 20, "password": "password123"})
    user_id = create_res.json()["id"]
    response = await client.put(f"/api/v1/users/{user_id}", json={"age": 21})
    assert response.status_code == 200
    assert response.json()["age"] == 21

@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient):
    create_res = await client.post("/api/v1/users/", json={"email": "delete@example.com", "age": 20, "password": "password123"})
    user_id = create_res.json()["id"]
    response = await client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_login(client: AsyncClient):
    # Register first
    await client.post("/api/v1/users/", json={"email": "login@example.com", "age": 25, "password": "password123"})
    
    # Login
    response = await client.post("/api/v1/auth/login", data={"username": "login@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
