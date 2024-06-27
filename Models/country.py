#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db

class Country(db.Model):

    __tablename__ = 'countries'

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __init__(self, id, name):
        self.id = id
