#!/usr/bin/python3
"""write a class City inherits from Base
links to MySQL table cities
class attribute id"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    class City inherits from Base
    links to MySQL table cities
    class attribute
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
