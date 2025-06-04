from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, agents, pipelines, metrics, users
from app.database import engine, Base

# Initialize the database
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(title="AI Agent Portal Backend")

# Enable CORS for local/frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(agents.router, prefix="/agents", tags=["Agents"])
app.include_router(pipelines.router, prefix="/pipelines", tags=["Pipelines"])
app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])

@app.get("/")
def root():
    return {"message": "AI Agent Portal Backend is running."}
@app.get("/health")
def health_check():
    return {"status": "healthy"}
