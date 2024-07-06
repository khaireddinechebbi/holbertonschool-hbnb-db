#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db
from Models.base_model import BaseModel

class City(BaseModel):
    """
    City class representing a city

    Attributes:
        name (str): Name of the city.
        country_id (int): Foreign key referencing the country's ID.
        country (Country): Relationship to the Country model.
    """
    __tablename__ = 'cities'

    name = db.Column(db.String(128), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

    # Relationship
    country = db.relationship('Country', backref=db.backref('cities', lazy=True))

    def __init__(self, name, country):
        """
        Initialize a new City instance

        Args:
            name (str): The name of the city.
            country (Country): The country where the city is located.
        """
        super().__init__()
        self.name = name
        self.country = country
