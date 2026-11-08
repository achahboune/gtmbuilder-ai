# GTMBuilder AI

## Overview
GTMBuilder AI is a minimal SaaS that generates Go‑to‑Market (GTM) plans from a single user prompt. It ships with a library of 1 200 pre‑configured actions (simulated in this MVP) and is aimed at founders of AI startups.

## Features
- Instant GTM plan generation from a free‑text prompt
- Responsive landing page with live demo
- FastAPI backend with health check
- Docker ready

## Quick start

```bash
git clone <repo-url>
cd <repo-dir>
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://localhost:8000` in a browser.

### Docker

```bash
docker build -t gtmbuilder .
docker run -p 8000:8000 gtmbuilder
```

## Limitations
- The plan is generated from a static template; no real AI model is called.
- The 1 200 actions are represented by a short hard‑coded sample.

## Next steps
- Plug an LLM (e.g., OpenAI, Anthropic) to generate real plans.
- Load the full 1 200‑action library from a database.
- Add user authentication and plan export.

## Environment
Copy `.env.example` to `.env` and fill in any required variables (currently none).
