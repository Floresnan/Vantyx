# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

**VANTYX** is an AI-powered Sales Command Center for real estate. It transforms sales goals into prioritized daily actions for brokers by scoring leads, simulating scenarios, and coordinating specialized AI agents.

## Development setup

### Backend (FastAPI)

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the API (entry point is main.py at project root)
uvicorn main:app --host 0.0.0.0 --port 8000
```

Swagger UI: `http://localhost:8000/docs`

**Deploy (Render):** configured via `render.yaml`. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend (Next.js)

```bash
cd vantyx-frontend
npm install
npm run dev      # dev server (default port 3000)
npm run build    # production build
npm run lint     # eslint
```

## CLI (`vx`)

The `vx` CLI talks to the API via `httpx` and is the primary user-facing interface:

```bash
vx ping           # test API connectivity
vx ops            # daily operations panel / KPIs
vx recent [n]     # list recent leads
vx top            # top leads by score
vx next           # next lead to contact
vx pipeline       # sales funnel breakdown
vx score          # calculate/display lead scores
vx import-a6 [f]  # import CSV leads
```

## Architecture

Three-layer design:

```
Data (Meta Ads, CSV imports)
  → Engines (scoring, simulation, market radar)
  → Command Center (API + frontend + CLI + dashboard)
```

### Frontend (`vantyx-frontend/`) — Next.js 16 + React 19 + Tailwind v4 + TypeScript

App Router structure under `app/`:
- `page.tsx` — dashboard home (KPI cards)
- `leads/page.tsx` — leads list
- `pipeline/page.tsx` — sales funnel
- `Login/page.tsx` — login screen
- `components/sidebar.tsx` — shared navigation sidebar
- `layout.tsx` — root layout with Geist font

Uses `@hello-pangea/dnd` for drag-and-drop (pipeline board).

### Backend API (`apps/api/`) — FastAPI + SQLAlchemy + PostgreSQL

- `app/models.py` — ORM: `Lead` (UUID PK, contact info, Meta Ads IDs, JSONB `raw` field), `DailyAction`
- `app/schemas.py` — Pydantic schemas (`LeadOut`, `LeadUpsertIn`, etc.)
- `app/db.py` + `app/settings.py` — DB connection (`postgresql+psycopg://vantyx:vantyx_pass@localhost:5432/vantyx`)
- `routers/leads.py` — `/leads` endpoints (upsert, patch, CSV import)
- `routers/ops.py` — `/ops/daily` KPI dashboard
- `routers/ui.py` — `/ui` data endpoints

### Agents (`agents/`) — coordinated by `core/orchestrator.py`

- `alfred_agent.py` — lead management
- `josue_agent.py` — competitor ad radar
- `caleb_agent.py` — strategic analysis
- `isaiah_agent.py` — copy generation
- `mateus_agent.py` — campaign creation
- `salomao_agent.py` — investment analysis

### Core logic

- `core/scoring.py` — lead scoring: `score = interesse + urgencia`, +2 if `renda ≥ 20k` or `entrada ≥ 200k`; tiers: `baixa / media / alta / altissima`
- `core/orchestrator.py` — coordinates agents, simulators, and memory
- `brain/sales_brain.py` — generates sales strategy recommendations
- `engine/sales_simulator.py` — simulates launch scenarios
- `radar/market_radar.py` — market intelligence
- `memory/vantyx_memory.py` — persistent state for decisions

### Other

- **Dashboard** (`apps/dashboard/`) — Streamlit
- **CLI** (`apps/cli/`) — Typer-based

## Key configuration

- `apps/api/app/settings.py` — DB URL and Meta webhook verify token
- `.env` — `OPENAI_API_KEY` and other secrets
- `apps/api/docker-compose.yml` — PostgreSQL 16, container `vantyx_db`, port `5432`

## Tech stack

**Backend:** Python 3.14 · FastAPI · SQLAlchemy 2 · Pydantic 2 · Uvicorn · PostgreSQL 16 · Streamlit · Typer · Anthropic SDK · OpenAI SDK · Pandas · httpx

**Frontend:** Next.js 16 · React 19 · TypeScript · Tailwind CSS v4 · @hello-pangea/dnd
