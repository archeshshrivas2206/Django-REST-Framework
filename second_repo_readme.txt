
National Fellowship for Scheduled Tribes (NFST): Support for ST students pursuing M.Phil/Ph.D. in higher educational institutions.
National Overseas Scholarship (NOS): Financial assistance for ST students pursuing Master's, Ph.D., and Post-Doctoral studies abroad.
The system features a dynamic, configurable architecture capable of supporting present and future Ministry schemes without custom code re-engineering.

🛠 Tech Stack
Layer	Technology
Frontend	Next.js 14 (App Router), TypeScript, Tailwind CSS, Framer Motion, Recharts
Backend	FastAPI (Python 3.11+), Pydantic v2, SQLAlchemy 2.0 ORM, Alembic
Database	PostgreSQL 16
Cache & Async	Redis 7, Celery ready
Object Storage	MinIO (Local S3 compatible storage) / Amazon S3 (Production)
AI / OCR Subsystem	PaddleOCR, PyMuPDF, OpenCV, OpenAI API backend service abstraction
Security & Auth	JWT Authentication, Role-Based Access Control (RBAC), SHA-256 Hashing
Containerization	Docker, Docker Compose
Testing	pytest, pytest-asyncio, httpx
📂 Repository Structure
mota-scholarship-management/
├── .env.example
├── .gitignore
├── README.md
├── docker-compose.yml
├── docs/
│   ├── ai-pipeline.md
│   ├── api.md
│   ├── architecture.md
│   ├── database.md
│   ├── development-phases.md
│   ├── scheme-configuration.md
│   └── security.md
├── config/
│   └── settings.py
├── database/
│   ├── alembic.ini
│   ├── alembic/
│   │   ├── env.py
│   │   └── script.py.mako
│   └── seeds/
│       └── initial_data.py
├── backend/
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── router.py
│   │   │   └── v1/
│   │   ├── core/
│   │   │   ├── audit.py
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── rbac.py
│   │   │   └── security.py
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   └── tests/
│       ├── conftest.py
│       ├── test_application.py
│       ├── test_audit.py
│       ├── test_auth.py
│       ├── test_health.py
│       ├── test_models.py
│       └── test_rbac.py
├── ai/
│   ├── README.md
│   ├── interfaces/
│   │   ├── classification.py
│   │   ├── eligibility_explanation.py
│   │   ├── extraction.py
│   │   ├── ocr.py
│   │   └── verification.py
│   └── services/
│       ├── mock_classification.py
│       ├── mock_extraction.py
│       ├── mock_ocr.py
│       └── mock_verification.py
├── storage/
│   ├── README.md
│   ├── base.py
│   └── minio_client.py
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── next.config.js
│   ├── Dockerfile
│   └── src/
└── scripts/
    ├── init_db.py
    └── run_tests.sh
⚡ Quick Start & Local Setup
Prerequisites
Python 3.11+
Node.js 18+
Docker & Docker Compose
1. Environment Setup
Copy the sample environment file:

cp .env.example .env
2. Run with Docker Compose
Start PostgreSQL, Redis, MinIO, Backend, and Frontend:

docker-compose up -d --build
Access points:

Frontend App: http://localhost:3000
FastAPI OpenAPI Specs: http://localhost:8000/docs
MinIO Storage Console: http://localhost:9001 (User: minioadmin, Pass: minioadmin)
3. Run Backend & Tests Locally (without Docker)
# Create virtual environment
python -m venv venv
# Activate on Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Activate on Linux/macOS:
# source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Run Pytest suite
pytest backend/tests -v

# Run FastAPI backend server
uvicorn backend.app.main:app --reload --port 8000
4. Run Frontend Locally
cd frontend
npm install
npm run dev
🔒 Security Architecture
JWT & Password Hashing: Passwords stored via bcrypt. JWT access tokens include user roles.
Backend Authorization: FastAPI dependency RequireRole([RoleEnum.ADMIN, ...]) guarantees authorization at the API level.
Document Protection: Files stored in MinIO/S3; frontend obtains short-lived pre-signed URLs.
Audit Logs: Immutable audit log entries for every sensitive application state change.
Here are the terminal commands to run the project locally. Make sure you are inside the d:\mota\mota-scholarship-management directory.

Option 1: Run Full Stack with Docker Compose (Recommended) This spins up PostgreSQL 16, Redis 7, MinIO S3 storage, the FastAPI Backend, and the Next.js Frontend in containers.

powershell

Navigate to project root
cd d:\mota\mota-scholarship-management

Create environment file if not created
Copy-Item .env.example .env

Build and start all 5 containers in the background
docker-compose up -d --build Access URLs:

Next.js Frontend: http://localhost:3000 FastAPI OpenAPI Docs: http://localhost:8000/docs MinIO Storage Console: http://localhost:9001 (User: minioadmin, Pass: minioadmin) Option 2: Run Backend & Frontend Locally (Without Docker) Terminal 1 — Run Pytest Suite & Start FastAPI Backend: powershell cd d:\mota\mota-scholarship-management

Run Pytest automated test suite (5/5 tests)
.\venv\Scripts\python.exe -m pytest backend/tests -v

Seed initial database (creates roles, super admin, and NFST/NOS scheme templates)
.\venv\Scripts\python.exe scripts/init_db.py

Start FastAPI development server
.\venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --port 8000 Terminal 2 — Start Next.js Frontend: powershell cd d:\mota\mota-scholarship-management\frontend

Start Next.js development server
npm run dev

