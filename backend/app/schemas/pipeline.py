from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class PipelineBase(BaseModel):
    name: str
    description: Optional[str]
    structure: Dict  # JSON-based DAG

class PipelineCreate(PipelineBase):
    created_by: int

class PipelineOut(PipelineBase):
    id: int
    created_by: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
