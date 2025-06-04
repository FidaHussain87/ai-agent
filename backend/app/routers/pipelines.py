from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.schemas.pipeline import PipelineCreate, PipelineOut
from app.models.pipeline import Pipeline
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PipelineOut)
def create_pipeline(pipeline: PipelineCreate, db: Session = Depends(get_db)):
    new_pipeline = Pipeline(**pipeline.dict())
    db.add(new_pipeline)
    db.commit()
    db.refresh(new_pipeline)
    return new_pipeline

@router.get("/", response_model=List[PipelineOut])
def list_pipelines(db: Session = Depends(get_db)):
    return db.query(Pipeline).all()
