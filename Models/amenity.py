#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from setup import db

class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Amenity(id={self.id}, name='{self.name}')>"