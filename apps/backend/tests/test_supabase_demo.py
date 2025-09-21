import os
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_demo_todos_endpoint():
    r = client.get("/demo/todos")
    assert r.status_code == 200
    data = r.json()
    assert "configured" in data
    # When not configured, expect rows to be empty
    if not os.environ.get("SUPABASE_URL"):
        assert data["configured"] is False
    else:
        assert data["configured"] is True
