-- Sample table and RLS policies for demo endpoint
-- Ensure pgcrypto for gen_random_uuid()
create extension if not exists "pgcrypto";

create table if not exists public.todos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete set null,
  title text not null,
  completed boolean not null default false,
  created_at timestamptz not null default now()
);

alter table public.todos enable row level security;

-- Recreate policies (PostgreSQL does not support IF NOT EXISTS on policies)
drop policy if exists "Users can view their todos" on public.todos;
create policy "Users can view their todos"
  on public.todos for select
  using (auth.uid() = user_id);

drop policy if exists "Users can insert their todos" on public.todos;
create policy "Users can insert their todos"
  on public.todos for insert
  with check (auth.uid() = user_id);

drop policy if exists "Users can update their todos" on public.todos;
create policy "Users can update their todos"
  on public.todos for update
  using (auth.uid() = user_id);

drop policy if exists "Users can delete their todos" on public.todos;
create policy "Users can delete their todos"
  on public.todos for delete
  using (auth.uid() = user_id);
