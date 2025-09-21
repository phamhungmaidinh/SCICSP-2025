from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    data = r.json()
    for k in ["status", "service", "version", "timestamp", "environment", "uptime"]:
        assert k in data


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] in ("ok", "healthy")


def test_healthcheck():
    r = client.get("/healthcheck")
    assert r.status_code == 200
    data = r.json()
    for k in ["system", "memory"]:
        assert k in data
