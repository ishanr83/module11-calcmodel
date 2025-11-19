from fastapi import FastAPI
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Calculation API",
    description="API for performing calculations with history",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Calculation API",
        "status": "running",
        "endpoints": {
            "docs": "/docs",
            "health": "/health"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
