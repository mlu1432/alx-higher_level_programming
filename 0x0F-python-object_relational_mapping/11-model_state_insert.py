# model_state.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
