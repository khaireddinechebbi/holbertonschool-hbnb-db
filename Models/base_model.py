#!/usr/bin/python3
"""
Module for baseModel class
"""
import uuid
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import db

Base = declarative_base()

class BaseModel(db.Model):
    """
    Class that defines common attributes and methods for other classes

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp when the instance was created.
        updated_at (datetime): Timestamp when the instance was last updated.
    """
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __repr__(self):
        """
        Return a string representation of the instance.
        """
        return f"<{self.__class__.__name__} id={self.id}>"

    def save(self):
        """
        Save the instance to the database
        """
        session = db.session()
        session.add(self)
        session.commit()

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

if __name__ == "__main__":
    engine = create_engine("sqlite:///mydb.db", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()