#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.base_model import BaseModel, Base
from app import db

class Amenity(BaseModel, db.Model):
    """
    Amenity class representing an amenity offered by a place

    Attributes:
        name (str): Name of the amenity.
    """
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __init__(self, name, *args, **kwargs):
        """
        Initialize a new Amenity instance

        Args:
            name (str): The name of the amenity.
        """
        super().__init__(*args, **kwargs)
        self.name = name

    def to_dict(self):
        """
        Convert instance attributes to a dictionary format
        Returns:
            dict: Dictionary containing the instance attributes.
        """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

if __name__ == "__main__":
    Base.metadata.create_all(bind=db.engine)
