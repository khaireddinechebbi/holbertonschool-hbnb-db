#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db

class City(db.Model):

    __tablename__ = 'cities'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country_id = db.Column(db.String(36), db.ForeignKey('countries.id'), nullable=False)


    def __init__(self, id, name, country_id):
        self.id = id
        self.name = name
        self.country_id = country_id
