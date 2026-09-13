# Executive Prompt: Decodelabs Task 2 (Data Vault)

## Core Architectural & Engineering Objective
Build a durable relational state persistence layer using FastAPI, SQLAlchemy 2.0 (AsyncSession), aiosqlite (dev) / AsyncPG (prod), Pydantic v2, and Alembic migrations.

## Enterprise GitHub Workflow Rules (STRICT)
1. Do NOT push directly to `main` for feature implementations. Create feature branches.
2. Merge feature branches into `main` using structured commit messages.
3. Keep `README.md` continuously updated.

---

### PHASE 1: Repository Hardening, Issues & Security Setup
1. Initialize local folder `user-vault-service` and link remote: `https://github.com/hafizabdulaziz/decodelabs-task2-data-vault.git`
2. Create `.gitignore`
3. Create `SECURITY.md`
4. Create `.github/ISSUE_TEMPLATE/`
5. Setup `requirements.txt`
6. Create `.env.example` and `.env`
7. Update `README.md`
8. COMMIT & PUSH Phase 1 directly to main.

---

### PHASE 2: Database Engine & Schema Design
1. Checkout `feature/db-schema-engine`
2. Implement `app/core/config.py`, `app/core/database.py`, `app/models/user.py`.
3. Configure `alembic`.
4. COMMIT/Merge to main.

---

### PHASE 3: Pydantic v2 & Service Layer
1. Checkout `feature/schemas-and-crud`
2. Implement `app/schemas/user.py`, `app/crud/user.py`.
3. COMMIT/Merge to main.

---

### PHASE 4: API Endpoints & 409 Conflict Gatekeeper
1. Checkout `feature/api-endpoints`
2. Implement `app/api/v1/endpoints/users.py`, connect in `app/main.py`.
3. COMMIT/Merge to main.

---

### PHASE 5: Automated Testing, GitHub Actions CI & Security Integration
1. Checkout `feature/ci-testing-suite`
2. Implement `tests/conftest.py`, `tests/test_users.py`, `.github/workflows/ci.yml`, `.github/workflows/codeql.yml`.
3. COMMIT/Merge to main.
