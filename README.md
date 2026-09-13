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
