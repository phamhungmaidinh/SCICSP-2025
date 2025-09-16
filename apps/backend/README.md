# RepUp Backend (FastAPI)

Quickstart:

```bash
cp .env.example .env
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host ${HOST:-0.0.0.0} --port ${PORT:-3000} --reload
```

Health check:

```bash
curl http://localhost:3000/health
```
