#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from setup import db

class City(db.Model):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

    country = relationship('Country', back_populates='cities')
    places = relationship('Place', back_populates='city')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'population': self.population,
            'country': self.country.name if self.country else None
        }

    def __repr__(self):
        return f"<City(id={self.id}, name='{self.name}', country_id={self.country_id})>"