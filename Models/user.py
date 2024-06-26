#!/usr/bin/python3
"""
User module containing the User class
"""
from sqlalchemy import Column, String
from Models.base_model import BaseModel, Base  # Assuming you have a BaseModel and Base class
from __init__ import *

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

    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)

    def __init__(self, email, password, first_name=None, last_name=None):
        """
        Initialize a new User instance

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
