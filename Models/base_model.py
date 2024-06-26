#!/usr/bin/python3
"""
Module for baseModel class
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from __init__ import *

Base = declarative_base()

class BaseModel(Base):
    """
    Class that defines common attributes and methods for other classes

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp when the instance was created.
        updated_at (datetime): Timestamp when the instance was last updated.
    """

    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)

    def __init__(self):
        """
        Initialize a new instance of BaseModel
        Generates a unique ID and sets the creation and update timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        """
        Return a string representation of the instance.
        """
        return f'<{self.__class__.__name__} {self.id}>'

    def save(self):
        """
        Update the updated_at timestamp
        This method should be called whenever the instance is modified.
        """
        self.updated_at = datetime.utcnow()
        db.session.commit()

    def to_dict(self):
        """
        Convert instance attributes to a dictionary format
        Returns:
            dict: Dictionary containing the instance attributes.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
