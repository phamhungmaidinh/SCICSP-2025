# RepUp Backend API# RepUp Backend (FastAPI) - WORKING VERSION



🏋️‍♂️ **AI-Powered Gym Training Assistant Backend**🏋️‍♂️ **AI-Powered Gym Training Assistant Backend API**
# RepUp Backend (FastAPI) + Supabase

AI-Powered Gym Training Assistant Backend with FastAPI, dockerized, and integrated with Supabase (Auth + Postgres + Storage).

## Quick Start

Start locally (dev):

```bash
cd apps/backend
source .venv/bin/activate
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Test endpoints (in a second terminal):

```bash
curl -s http://localhost:8000/healthcheck | jq . | head
curl -s http://localhost:8000/health
curl -s http://localhost:8000/
```

## Supabase E2E Integration

We use Supabase for Auth and Postgres. FastAPI stays as the compute service (Render/Cloud Run/Railway/Fly.io). To wire E2E:

1) Create a Supabase project and get:
   - SUPABASE_URL (Project settings → API → Project URL)
   - SUPABASE_ANON_KEY (for frontend; optional here)
   - SUPABASE_SERVICE_ROLE_KEY (server-side; keep secret!)

2) Configure environment:

```bash
cp .env.example .env
# edit .env and set SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
```

3) Apply schema (create a sample table with RLS policies). In Supabase SQL Editor, run:

```sql
-- Table
create table if not exists public.todos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete set null,
  title text not null,
  completed boolean not null default false,
  created_at timestamptz not null default now()
);

-- Enable RLS
alter table public.todos enable row level security;

-- Policies: users read/write their rows
create policy if not exists "Users can view their todos"
  on public.todos for select
  using (auth.uid() = user_id);

create policy if not exists "Users can insert their todos"
  on public.todos for insert
  with check (auth.uid() = user_id);

create policy if not exists "Users can update their todos"
  on public.todos for update
  using (auth.uid() = user_id);

create policy if not exists "Users can delete their todos"
  on public.todos for delete
  using (auth.uid() = user_id);
```

4) Run server and test demo endpoints:

```bash
source .venv/bin/activate
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

# List demo data (uses supabase client if configured):
curl -s http://localhost:8000/demo/todos | jq .
```

5) Auth-protected route (optional):

```bash
# Requires a valid Supabase user JWT from your app
curl -H "Authorization: Bearer <USER_JWT>" http://localhost:8000/me
```

Notes:
- If Supabase env is not set, /demo/todos returns {configured: false}.
- If configured but no table exists, you will see an error message from Supabase.

## Endpoints

- GET / → Basic health
- GET /health → Health
- GET /healthcheck → Extended health with system info
- GET /me → Returns claims from Supabase JWT (requires Authorization: Bearer)
- GET /demo/todos → Reads first 10 rows from public.todos (if Supabase configured)

## Environment

See `.env.example`. Minimal variables for Supabase:

- SUPABASE_URL
- SUPABASE_SERVICE_ROLE_KEY (or ANON_KEY for read-only)

## Tests

Run tests from repo root or backend folder:

```bash
cd apps/backend
source .venv/bin/activate
pytest -q
```

Supabase tests are conditional: if no SUPABASE_URL is set, they only assert that the demo endpoint responds.

## CI

GitHub Actions workflow runs lint and tests. To enable Supabase integration in CI, add these repository secrets:

- SUPABASE_URL
- SUPABASE_SERVICE_ROLE_KEY

## Deploy (example with Render)

Create a Web Service from this repo using the Dockerfile in `apps/backend`. Set env vars in Render dashboard:

- ENVIRONMENT=production
- HOST=0.0.0.0
- PORT=8000
- SUPABASE_URL=...
- SUPABASE_SERVICE_ROLE_KEY=...

Expose port 8000. Health check path: /healthcheck.

## Troubleshooting

- Healthcheck ok but Supabase demo returns configured=false → set SUPABASE_URL and key in environment
- 401 on /me → missing/invalid Authorization header, or Supabase not configured
- Supabase errors on /demo/todos → apply the SQL schema above in your project
