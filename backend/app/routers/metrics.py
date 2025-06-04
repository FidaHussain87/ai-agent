from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.schemas.metric import MetricCreate, MetricOut
from app.models.metric import Metric

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MetricOut)
def log_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    new_metric = Metric(**metric.dict())
    db.add(new_metric)
    db.commit()
    db.refresh(new_metric)
    return new_metric

@router.get("/agent/{agent_id}", response_model=List[MetricOut])
def get_agent_metrics(agent_id: int, db: Session = Depends(get_db)):
    return db.query(Metric).filter(Metric.agent_id == agent_id).all()
