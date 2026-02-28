# Vantyx — Ponto de Retomada

## Como rodar
- Postgres: pg_isready -h 127.0.0.1 -p 5432
- API: cd ~/vantyx/apps/api && source ~/vantyx/.venv/bin/activate && uvicorn app.main:app --host 127.0.0.1 --port 8000
- CLI: cd ~/vantyx && source .venv/bin/activate && vx ping && vx ops

## Endpoints existentes
- GET /health
- GET /ops/daily
- POST /leads/upsert
- PATCH /leads/{lead_id}
- GET/POST webhooks meta (se estiverem no main.py)

## Último status conhecido
- /health OK
- /ops/daily retorna "Modo seguro estabilizado"
- Postgres rodando em 127.0.0.1:5432

## Próximas tarefas
- Ajustar score/top para refletir interesse/urgência/etapa/recência
- Padronizar schemas (LeadOut / LeadUpsertIn)
- Garantir permissões do DB e migrations (evitar create_all em prod)
