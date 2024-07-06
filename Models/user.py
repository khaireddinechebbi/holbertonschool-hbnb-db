#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import db
from Models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """
    User class representing a user in the system

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    def __init__(self, email, password, first_name, last_name, *args, **kwargs):
        """
        Initialize a new User instance

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
        """
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        """
        Convert instance attributes to a dictionary format
        Returns:
            dict: Dictionary containing the instance attributes.
        """
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
        })
        return user_dict
    
Base.metadata.create_all(bind=db.engine)
