# AI Agent Portal – Backend

This is the FastAPI-based backend for the AI Agent Portal platform.

## Features

- User authentication (JWT)
- Role-based access (Admin, User, Viewer)
- AI Agent creation with training config
- Pipeline chaining with DAG structure
- Agent execution metrics tracking
- PostgreSQL, Redis integration
- Ready for Docker/Kubernetes

## Local Setup

1. Create `.env` from `.env.example`
2. Start PostgreSQL and Redis locally
3. Run:

```bash
uvicorn main:app --reload
