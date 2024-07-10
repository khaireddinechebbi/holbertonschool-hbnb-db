#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from setup import db

class Place(db.Model):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    city = relationship('City', back_populates='places')
    user = relationship('User', back_populates='places')

    def __repr__(self):
        return f"<Place(id={self.id}, name='{self.name}', city_id={self.city_id})>"