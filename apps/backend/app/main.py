from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI(title="RepUp Backend", version=os.getenv("APP_VERSION", "0.1.0"))

class Health(BaseModel):
    status: str
    service: str
    version: str
    timestamp: str

@app.get("/", response_model=Health)
def root():
    return Health(
        status="ok",
        service="repup-backend",
        version=app.version,
        timestamp=datetime.utcnow().isoformat(),
    )

@app.get("/health", response_model=Health)
def health():
    return Health(
        status="ok",
        service="repup-backend",
        version=app.version,
        timestamp=datetime.utcnow().isoformat(),
    )
