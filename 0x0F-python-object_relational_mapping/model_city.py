#!/usr/bin/python3
""" This module contains a City class which inherits from Base """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ Initializes a new class City """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
