from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi import Body
from pydantic import BaseModel
from datetime import datetime
import os
import platform
import psutil
from typing import Dict

from .supabase_auth import SupabaseAuth, get_supabase_env, create_supabase_client

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


# --- Supabase Integration ---
@app.on_event("startup")
async def _init_supabase():
    env = get_supabase_env()
    if env["SUPABASE_URL"]:
        app.state.supabase_auth = SupabaseAuth(env["SUPABASE_URL"])
    else:
        app.state.supabase_auth = None
    app.state.supabase = create_supabase_client()


async def require_user(request: Request) -> Dict:
    if not getattr(app.state, "supabase_auth", None):
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Supabase not configured")

    header = request.headers.get("authorization", "")
    if not header.lower().startswith("bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
    token = header.split(" ", 1)[1]
    try:
        return await app.state.supabase_auth.verify(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

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


@app.get("/me")
async def me(user: Dict = Depends(require_user)):
    return {"user_id": user.get("sub"), "email": user.get("email"), "issuer": user.get("iss")}


@app.get("/demo/todos")
async def demo_todos():
    """Demo: list rows from 'todos' table if Supabase is configured; otherwise return stub."""
    if not getattr(app.state, "supabase", None):
        return {"configured": False, "rows": []}
    try:
        resp = app.state.supabase.table("todos").select("*").limit(10).execute()
        return {"configured": True, "rows": resp.data}
    except Exception as e:
        return {"configured": True, "error": str(e)}


@app.post("/demo/todos")
async def create_todo(
    user: Dict = Depends(require_user),
    title: str = Body(..., embed=True)
):
    if not getattr(app.state, "supabase", None):
        raise HTTPException(status_code=503, detail="Supabase not configured")
    user_id = user.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing sub in token")
    try:
        resp = app.state.supabase.table("todos").insert({
            "user_id": user_id,
            "title": title,
            "completed": False,
        }).execute()
        return {"inserted": True, "row": (resp.data or [None])[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
