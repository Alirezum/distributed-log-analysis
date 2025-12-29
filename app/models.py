from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    level = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
