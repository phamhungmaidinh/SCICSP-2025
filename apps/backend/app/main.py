from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os
import platform
import psutil

app = FastAPI(
    title="RepUp Backend API", 
    description="AI-Powered Gym Training Assistant Backend",
    version=os.getenv("APP_VERSION", "0.1.0")
)

class Health(BaseModel):
    status: str
    service: str
    version: str
    timestamp: str
    environment: str
    uptime: str

class HealthCheck(BaseModel):
    status: str
    service: str
    version: str
    timestamp: str
    environment: str
    uptime: str
    system: dict
    memory: dict

# Keep track of app startup time for uptime calculation
startup_time = datetime.utcnow()

def get_uptime():
    """Calculate uptime since app startup"""
    delta = datetime.utcnow() - startup_time
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

@app.get("/", response_model=Health)
def root():
    return Health(
        status="ok",
        service="repup-backend",
        version=app.version,
        timestamp=datetime.utcnow().isoformat(),
        environment=os.getenv("ENVIRONMENT", "development"),
        uptime=get_uptime()
    )

@app.get("/health", response_model=Health)
def health():
    return Health(
        status="ok",
        service="repup-backend",
        version=app.version,
        timestamp=datetime.utcnow().isoformat(),
        environment=os.getenv("ENVIRONMENT", "development"),
        uptime=get_uptime()
    )

@app.get("/healthcheck", response_model=HealthCheck)
def healthcheck():
    """Comprehensive health check endpoint with system information"""
    # Get system information
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return HealthCheck(
        status="healthy",
        service="repup-backend",
        version=app.version,
        timestamp=datetime.utcnow().isoformat(),
        environment=os.getenv("ENVIRONMENT", "development"),
        uptime=get_uptime(),
        system={
            "platform": platform.system(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor() or "Unknown",
            "python_version": platform.python_version(),
            "hostname": platform.node()
        },
        memory={
            "total": f"{memory.total / (1024**3):.2f} GB",
            "available": f"{memory.available / (1024**3):.2f} GB",
            "used": f"{memory.used / (1024**3):.2f} GB",
            "percentage": f"{memory.percent}%",
            "disk_total": f"{disk.total / (1024**3):.2f} GB",
            "disk_free": f"{disk.free / (1024**3):.2f} GB",
            "disk_used_percent": f"{(disk.used / disk.total) * 100:.1f}%"
        }
    )
