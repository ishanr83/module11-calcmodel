# Module 11: Calculation Model with Factory Pattern

## Overview

This project implements a Calculation API with:
- SQLAlchemy models for database operations
- Pydantic schemas for validation
- Factory pattern for calculation operations
- Comprehensive unit and integration tests
- CI/CD pipeline with GitHub Actions
- Docker containerization and deployment

## Features

 **SQLAlchemy Calculation Model**
- Fields: `id`, `a`, `b`, `type`, `result`, `created_at`
- Store results in database
- Support for Add, Subtract, Multiply, Divide operations

 **Pydantic Schemas**
- `CalculationCreate`: Input validation with divide-by-zero check
- `CalculationRead`: Output serialization
- `CalculationUpdate`: Partial updates

 **Factory Pattern**
- Strategy pattern for calculation operations
- Extensible design for new operations
- Clean separation of concerns

 **Comprehensive Testing**
- 25 unit and integration tests
- 90%+ code coverage
- PostgreSQL integration tests

 **CI/CD Pipeline**
- Automated testing on push
- Docker image build and push
- PostgreSQL container for testing

## Local Setup

### Prerequisites
- Python 3.11+
- Docker (optional, for containerization)
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/ishanr83/module11-calcmodel.git
cd module11-calcmodel

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

### Run All Tests
```bash
pytest -v
```

### Run with Coverage
```bash
pytest --cov=app --cov-report=term-missing
```

### Run Specific Test Files
```bash
pytest tests/test_calculation_factory.py -v
pytest tests/test_calculation_schema.py -v
pytest tests/test_calculation_integration.py -v
```

### Generate HTML Coverage Report
```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

## Running the Application

### Locally
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for API documentation.

### With Docker
```bash
# Build image
docker build -t module11-calcmodel .

# Run container
docker run -p 8000:8000 module11-calcmodel

# Or pull from Docker Hub
docker pull ishanr83/module11-calcmodel:latest
docker run -p 8000:8000 ishanr83/module11-calcmodel:latest
```

## Docker Hub

**Repository:** https://hub.docker.com/r/ishanr83/module11-calcmodel

**Pull command:**
```bash
docker pull ishanr83/module11-calcmodel:latest
```

**Available tags:**
- `latest` - Most recent build
- `<commit-sha>` - Specific commit builds

## Project Structure
```
module11-calcmodel/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── database.py             # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── calculation.py      # SQLAlchemy model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── calculation.py      # Pydantic schemas
│   └── services/
│       ├── __init__.py
│       └── calculation_factory.py  # Factory pattern
├── tests/
│   ├── __init__.py
│   ├── test_calculation_factory.py
│   ├── test_calculation_schema.py
│   └── test_calculation_integration.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # GitHub Actions workflow
├── Dockerfile
├── requirements.txt
├── README.md
└── REFLECTION.md
```

## Calculation Operations

| Operation | Type String | Example |
|-----------|-------------|---------|
| Addition | `"Add"` | 5 + 3 = 8 |
| Subtraction | `"Subtract"` | 10 - 3 = 7 |
| Multiplication | `"Multiply"` | 4 × 5 = 20 |
| Division | `"Divide"` | 10 ÷ 2 = 5 |

## API Endpoints

Currently implemented (read-only):
- `GET /` - Welcome message
- `GET /health` - Health check

Coming in Module 12:
- `POST /calculations` - Create calculation
- `GET /calculations` - List calculations
- `GET /calculations/{id}` - Get specific calculation
- `PUT /calculations/{id}` - Update calculation
- `DELETE /calculations/{id}` - Delete calculation

## Testing Strategy

### Unit Tests (12 tests)
- Factory pattern strategy selection
- Individual calculation operations
- Input validation
- Error handling

### Schema Tests (8 tests)
- Pydantic validation rules
- Divide-by-zero prevention
- Type enforcement
- Required field validation

### Integration Tests (5 tests)
- Database CRUD operations
- Query filtering
- Data persistence
- Transaction handling

## CI/CD Pipeline

### GitHub Actions Workflow

**Triggers:**
- Push to `main` branch
- Pull requests to `main` branch

**Jobs:**

1. **Test Job**
   - Set up Python 3.11
   - Install dependencies
   - Run pytest with PostgreSQL
   - Generate coverage reports
   - Upload to Codecov

2. **Build and Push Job** (only on main push)
   - Build Docker image
   - Push to Docker Hub
   - Tag with `latest` and commit SHA
   - Use layer caching for speed

## Test Coverage

**Current Coverage:** 90%+

Coverage excludes:
- Configuration classes (`pragma: no cover`)
- Main application endpoints (tested in Module 12)
- Database connection helpers
- Abstract methods

## Dependencies
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-multipart==0.0.6
psycopg2-binary==2.9.9
alembic==1.12.1
pytest==7.4.3
pytest-cov==4.1.0
pytest-asyncio==0.21.1
httpx==0.25.1
```

## Author

Ishan Rehan (@ishanr83)
