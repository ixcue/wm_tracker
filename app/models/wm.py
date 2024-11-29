from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class WmModel(Base):
    __tablename__ = "washing_machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    installation_date = Column(DateTime, default=datetime.utcnow)
    balance = Column(Float, default=0.0)