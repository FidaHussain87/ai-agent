from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class AgentBase(BaseModel):
    name: str
    task_type: str
    data_source: Optional[str]
    training_parameters: Optional[Dict]

class AgentCreate(AgentBase):
    created_by: int

class AgentOut(AgentBase):
    id: int
    model_version: str
    created_by: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
