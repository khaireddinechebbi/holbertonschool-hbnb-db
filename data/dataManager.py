#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import current_app
from Models.user import User
from Models.city import City
from Models.country import Country
from Models.amenity import Amenity
from Models.place import Place
from app import db 


class DataManager:
    def save_user(self, user):
        if current_app.config.get('USE_DATABASE'):
            db.session.add(user)
            db.session.commit()
        else:
            with open('user_data.txt', 'a') as file:
                file.write(f"{user}\n")
    
    def get_user_by_id(self, user_id):
        if current_app.config.get('USE_DATABASE'):
            return User.query.filter_by(id=user_id).first()
        else:
            with open('user_data.txt', 'r') as file:
                for line in file:
                    if line.startswith(str(user_id)):
                        return line.strip().split(',')
        return None
    
    def save_city(self, city):
        if current_app.config.get('USE_DATABASE'):
            db.session.add(city)
            db.session.commit()
        else:
            with open('city_data.txt', 'a') as file:
                file.write(f"{city}\n")
    
    def get_city_by_id(self, city_id):
        if current_app.config.get('USE_DATABASE'):
            return City.query.filter_by(id=city_id).first()
        else:
            with open('city_data.txt', 'r') as file:
                for line in file:
                    if line.startswith(str(city_id)):
                        return line.strip().split(',')
        return None
    
    def save_country(self, country):
        if current_app.config.get('USE_DATABASE'):
            db.session.add(country)
            db.session.commit()
        else:
            with open('country_data.txt', 'a') as file:
                file.write(f"{country}\n")
    
    def get_country_by_id(self, country_id):
        if current_app.config.get('USE_DATABASE'):
            return Country.query.filter_by(id=country_id).first()
        else:
            with open('country_data.txt', 'r') as file:
                for line in file:
                    if line.startswith(str(country_id)):
                        return line.strip().split(',')
        return None
    
    def save_amenity(self, amenity):
        if current_app.config.get('USE_DATABASE'):
            db.session.add(amenity)
            db.session.commit()
        else:
            with open('amenity_data.txt', 'a') as file:
                file.write(f"{amenity}\n")
    
    def get_amenity_by_id(self, amenity_id):
        if current_app.config.get('USE_DATABASE'):
            return Amenity.query.filter_by(id=amenity_id).first()
        else:
            with open('amenity_data.txt', 'r') as file:
                for line in file:
                    if line.startswith(str(amenity_id)):
                        return line.strip().split(',')
        return None
    
    def save_place(self, place):
        if current_app.config.get('USE_DATABASE'):
            db.session.add(place)
            db.session.commit()
        else:
            with open('place_data.txt', 'a') as file:
                file.write(f"{place}\n")
    
    def get_place_by_id(self, place_id):
        if current_app.config.get('USE_DATABASE'):
            return Place.query.filter_by(id=place_id).first()
        else:
            with open('place_data.txt', 'r') as file:
                for line in file:
                    if line.startswith(str(place_id)):
                        return line.strip().split(',')
        return None