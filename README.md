# Insurance Claims Fraud Detection & Investigation Workbench

For adjusters: cross-references claim details against historical patterns, flags staged accidents/repeat claimants across shell identities, builds case file with linked evidence via explainable graph + rules engine.

## Architecture
- **Backend:** Django 4.2 + DRF + Celery + Redis, PostgreSQL (sqlite fallback), NetworkX (mock)
- **Frontend:** React 18 + Vite + D3 (graph) + Chart.js
- **15 Apps:** claims, entities, graph, anomalies, rules, investigation, history, scoring, integrations, reporting, workflow, api, frontend, compliance, analytics

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t fraud-workbench .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
celery -A fraud worker -l info
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Features
- **Entity resolution:** fuzzy `Levenshtein + Soundex` for shell identities, repeat claimant across `John Smith` vs `J. Smith` + same DOB/phone
- **Graph:** `claimant -[CLAIMED]-> claim -[INVOLVES]-> vehicle -[OWNED_BY]-> entity` → centrality, community `Louvain` to find rings
- **Rules:** explainable `IF staged_accident AND repeat_claimant_2y>2 THEN flag` with SHAP + audit trail for regulators
- **Case file:** auto-linked evidence `police report + medical + photos` timeline

## License
Proprietary — All rights reserved.
