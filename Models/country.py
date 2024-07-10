#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from setup import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    cities = relationship('City', back_populates='country')

    def __repr__(self):
        return f"<Country(id={self.id}, name='{self.name}')>"