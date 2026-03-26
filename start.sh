#!/bin/bash

# Vantyx — Start Script
ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "🚀 Iniciando Vantyx..."

# Verifica PostgreSQL
if ! pg_isready -h 127.0.0.1 -p 5432 -q; then
  echo "❌ PostgreSQL não está rodando. Inicie o banco antes."
  exit 1
fi
echo "✅ PostgreSQL OK"

# API (backend)
source "$ROOT/.venv/bin/activate"
cd "$ROOT/apps/api"
uvicorn app.main:app --host 127.0.0.1 --port 8000 &
API_PID=$!
echo "✅ API iniciada (PID $API_PID) → http://localhost:8000"

# Aguarda API subir
sleep 2

# Frontend
cd "$ROOT/vantyx-frontend"
npm run dev &
FRONT_PID=$!
echo "✅ Frontend iniciado (PID $FRONT_PID) → http://localhost:3000"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Vantyx rodando!"
echo "  Dashboard → http://localhost:3000"
echo "  API Docs  → http://localhost:8000/docs"
echo "  CLI       → vx ops"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Pressione Ctrl+C para encerrar"
echo ""

# Aguarda Ctrl+C e mata os processos
trap "echo ''; echo 'Encerrando...'; kill $API_PID $FRONT_PID 2>/dev/null; exit 0" INT
wait
