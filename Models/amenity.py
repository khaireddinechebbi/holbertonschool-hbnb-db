#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.base_model import BaseModel
from app import db

class Amenity(BaseModel):

    __tablename__ = 'amenities'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(120), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
