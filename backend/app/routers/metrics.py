from fastapi import APIRouter, Depends
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

@router.post("/", response_model=schemas.MetricOut)
def log_metric(metric: schemas.MetricCreate, db: Session = Depends(get_db)):
    new_metric = models.Metric(**metric.dict())
    db.add(new_metric)
    db.commit()
    db.refresh(new_metric)
    return new_metric

@router.get("/agent/{agent_id}", response_model=List[schemas.MetricOut])
def get_agent_metrics(agent_id: int, db: Session = Depends(get_db)):
    return db.query(models.Metric).filter(models.Metric.agent_id == agent_id).all()
