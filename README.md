# Decodelabs Task 2: Data Vault

A resilient Asynchronous Database Persistence Engine.

## Architecture
- FastAPI
- SQLAlchemy 2.0 (Async)
- Pydantic v2
- Alembic

## Database Schema
### ER Diagram
[Placeholder for ER Diagram]

### Schema Design
- **users**:
  - `id`: BigInteger (PK)
  - `email`: String(255), Unique, Indexed
  - `age`: Integer (>= 0)
  - `is_active`: Boolean
  - `created_at`: DateTime

## CRUD Logic Design
The project utilizes the **Repository Pattern** to abstract database operations.
- `create_user`: Creates a new user entry.
- `get_user_by_id`/`get_user_by_email`: Fetches user by unique identifiers.
- `get_users`: Fetches a paginated list of users.
- `update_user`: Updates existing user data.
- `delete_user`: Removes a user from the database.
