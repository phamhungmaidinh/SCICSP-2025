-- Sample table and RLS policies for demo endpoint
create table if not exists public.todos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete set null,
  title text not null,
  completed boolean not null default false,
  created_at timestamptz not null default now()
);

alter table public.todos enable row level security;

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
