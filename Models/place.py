#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db

class Place(db.Model):

    __tablename__ = 'places'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('cities.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)


    def __init__(self, id, city_id, description):
        self.id = id
        self.city_id = city_id
        self.description = description