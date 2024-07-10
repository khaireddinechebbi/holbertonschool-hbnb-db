#!/usr/bin/python3

from setup import db
from models.user import User
from models.country import Country
from models.city import City
from models.place import Place
from models.amenity import Amenity

class DataManager:
    def save_entity(self, entity_type, entity_data):
        if entity_type == 'User':
            self.save_to_database(User, entity_data)
        elif entity_type == 'City':
            self.save_to_database(City, entity_data)
        elif entity_type == 'Country':
            self.save_to_database(Country, entity_data)
        elif entity_type == 'Place':
            self.save_to_database(Place, entity_data)
        elif entity_type == 'Amenity':
            self.save_to_database(Amenity, entity_data)

    def add_entity(self, entity_type, entity_data):
        if entity_type == 'User':
            self.add_to_database(User, entity_data)
        elif entity_type == 'City':
            self.add_to_database(City, entity_data)
        elif entity_type == 'Country':
            self.add_to_database(Country, entity_data)
        elif entity_type == 'Place':
            self.add_to_database(Place, entity_data)
        elif entity_type == 'Amenity':
            self.add_to_database(Amenity, entity_data)

    def update_entity(self, entity_type, entity_id, entity_data):
        if entity_type == 'User':
            self.update_in_database(User, entity_id, entity_data)
        elif entity_type == 'City':
            self.update_in_database(City, entity_id, entity_data)
        elif entity_type == 'Country':
            self.update_in_database(Country, entity_id, entity_data)
        elif entity_type == 'Place':
            self.update_in_database(Place, entity_id, entity_data)
        elif entity_type == 'Amenity':
            self.update_in_database(Amenity, entity_id, entity_data)

    def save_to_database(self, model_cls, entity_data):
        entity = model_cls(**entity_data)
        db.session.add(entity)
        db.session.commit()

    def add_to_database(self, model_cls, entity_data):
        entity = model_cls(**entity_data)
        db.session.add(entity)
        db.session.commit()

    def update_in_database(self, model_cls, entity_id, entity_data):
        entity = model_cls.query.get(entity_id)
        if entity:
            for key, value in entity_data.items():
                setattr(entity, key, value)
            db.session.commit()
