# Decodelabs Task 2: Data Vault

A resilient Asynchronous Database Persistence Engine.

## Features
- FastAPI for high-performance API endpoints.
- SQLAlchemy 2.0 (Async) with Pydantic v2.
- Alembic for database migrations.
- Comprehensive Test Suite (`pytest` + `httpx`).
- CI/CD Pipelines (GitHub Actions & CodeQL).

## Installation
1. Clone the repository: `git clone <url>`
2. Create virtual environment: `python -m venv .venv`
3. Install requirements: `pip install -r requirements.txt`

## Running Tests
Run the test suite using `pytest`:
```bash
pytest
```

## API Documentation
| Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| POST | `/api/v1/auth/login` | Login/Get JWT | 200, 401 |
| POST | `/api/v1/users/` | Create User | 201, 409 |
| GET | `/api/v1/users/` | List Users | 200 |
| GET | `/api/v1/users/{id}` | Get User | 200, 404 |
| PUT | `/api/v1/users/{id}` | Update User | 200, 404 |
| DELETE | `/api/v1/users/{id}` | Delete User | 204, 404 |
