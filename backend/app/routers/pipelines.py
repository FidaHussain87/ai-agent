from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PipelineOut)
def create_pipeline(pipeline: schemas.PipelineCreate, db: Session = Depends(get_db)):
    new_pipeline = models.Pipeline(**pipeline.dict())
    db.add(new_pipeline)
    db.commit()
    db.refresh(new_pipeline)
    return new_pipeline

@router.get("/", response_model=List[schemas.PipelineOut])
def list_pipelines(db: Session = Depends(get_db)):
    return db.query(models.Pipeline).all()
