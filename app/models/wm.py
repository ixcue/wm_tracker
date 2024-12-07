from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class WmModel(Base):
    __tablename__ = "washing_machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    installation_date = Column(DateTime, default=datetime.now)
    location = Column(String, nullable=True)
    balance = Column(Integer, default=0)
    description = Column(String, nullable=True)

    transactions = relationship("Transactions", back_populates="machine")