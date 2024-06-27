#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#!/usr/bin/python3

from app import db

class Amenity(db.Model):

    __tablename__ = 'amenities'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)


    def __init__(self, id, name):
        self.id = id
        self.name = name
