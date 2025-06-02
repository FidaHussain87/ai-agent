from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from app.database import Base

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    input_data = Column(JSON)
    output_data = Column(JSON)
    confidence = Column(Float)
    execution_time = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
