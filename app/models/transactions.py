from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey('washing_machines.id'))
    transaction_type = Column(String(10))
    amount = Column(Integer)
    date = Column(DateTime(True), default=datetime.now)
    comment = Column(String(255), nullable=True)
    created_at = Column(DateTime(True), default=datetime.now)
    updated_at = Column(DateTime(True), default=datetime.now, onupdate=datetime.now)

    machine = relationship('WmModel', back_populates='transactions')  