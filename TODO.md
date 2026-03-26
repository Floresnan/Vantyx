# Vantyx UI Upgrade & Organization TODO

## Status: In Progress 🚀

### ✅ Fase 1: Backend Clean/Unify
- [x] Backup melhorias_temp → backups/
- [x] Delete melhorias_temp/
- [x] Create TODO.md
- [x] Merge API main.py (v0.3 com Alfred)
- [x] Remove old main.py

### ✅ Fase 2.1-2.4: Frontend Core
- [x] globals.css: Premium navy/gold theme
- [x] layout.tsx: Sidebar + responsive
- [x] page.tsx: Hero dashboard + KPIs + foco/scripts
- [x] app/leads/page.tsx: Interactive table + search + badges

### 🏗️ Fase 2.5: Pipeline & Final
- [ ] app/pipeline/page.tsx: DnD Kanban API
- [ ] app/ops/page.tsx: Advanced metrics charts
- [ ] Fix TS errors (deps/geist)
- [ ] Add types/auth

### 🔧 Fase 3: Backend Engines
- [ ] engine/lead_engine.py


### 🏗️ Fase 2: Modern Frontend (Priority)
- [ ] globals.css: Premium theme (dark/gradients)
- [ ] layout.tsx: Sidebar + auth
- [ ] page.tsx: Hero dashboard
- [ ] app/leads/page.tsx: Interactive table
- [ ] app/pipeline/page.tsx: DnD Kanban
- [ ] app/ops/page.tsx: Metrics cards
- [ ] components/: UI kit (CardLead, etc.)

### 🔗 Fase 3: Integration
- [ ] API hooks + auth
- [ ] Docker full stack
- [ ] Tests + deploy

**Run:** `cd vantyx-frontend && npm run dev`

