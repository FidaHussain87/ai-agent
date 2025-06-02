from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class MetricCreate(BaseModel):
    agent_id: int
    input_data: Dict
    output_data: Dict
    confidence: float
    execution_time: float

class MetricOut(MetricCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
