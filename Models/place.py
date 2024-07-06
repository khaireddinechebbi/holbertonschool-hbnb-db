#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import db
from Models.base_model import BaseModel, Base

class Place(BaseModel, Base, db.Model):
    """
    Place class representing a place for rent

    Attributes:
        name (str): Name of the place.
        description (str): Description of the place.
        address (str): Address of the place.
        city (str): City where the place is located.
        latitude (float): Latitude of the place's location.
        longitude (float): Longitude of the place's location.
        host_id (str): ID of the host User.
        number_of_rooms (int): Number of rooms in the place.
        number_of_bathrooms (int): Number of bathrooms in the place.
        max_guests (int): Maximum number of guests the place can accommodate.
        price_per_night (float): Price per night for renting the place.
    """

    __tablename__ = 'places'

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)

    host = db.relationship('User', backref='place')
    amenities = db.relationship('Amenity', backref='place')
    reviews = db.relationship('Review', backref='place')

    def __init__(self, name, description, address, city, latitude, longitude,
                 host_id, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, *args, **kwargs):
        """
        Initialize a new Place instance

        Args:
            name (str): Name of the place.
            description (str): Description of the place.
            address (str): Address of the place.
            city (str): City where the place is located.
            latitude (float): Latitude of the place's location.
            longitude (float): Longitude of the place's location.
            host_id (str): ID of the host User.
            number_of_rooms (int): Number of rooms in the place.
            number_of_bathrooms (int): Number of bathrooms in the place.
            max_guests (int): Max. number of guests the place can accommodate.
            price_per_night (float): Price per night for renting the place.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        """
        Add an amenity to the place's list of amenities

        Args:
            amenity (str): The amenity to be added.
        """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        """
        Add a review to the place's list of reviews

        Args:
            review (str): The review to be added.
        """
        self.reviews.append(review)

    def to_dict(self):
        """
        Convert instance attributes to a dictionary format
        Returns:
            dict: Dictionary containing the instance attributes.
        """
        place_dict = super().to_dict()
        place_dict.update({
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'max_guests': self.max_guests,
            'price_per_night': self.price_per_night,
        })
        return place_dict
    
Base.metadata.create_all(bind=db.engine)