# Module 11: Calculation Model

Calculation API with Factory Pattern implementation and comprehensive testing.

## Features

- SQLAlchemy Calculation model
- Pydantic schema validation
- Factory pattern for operations
- 22 comprehensive tests
- CI/CD with GitHub Actions
- Docker deployment

## Local Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests
```bash
pytest -v
pytest --cov=app --cov-report=term-missing
pytest --cov=app --cov-report=html
```

## Run Application
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for API documentation.

## Docker
```bash
docker build -t module11-calcmodel .
docker run -p 8000:8000 module11-calcmodel
```

## Operations Supported

- Add
- Subtract
- Multiply
- Divide

## Test Coverage

Target: 90%+ coverage
