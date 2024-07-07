import json
import os
from app import app, db
from Models import User, Place, City, Country, Amenity


def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

class DataManager:
    def __init__(self):
        self.data_dir = 'data'
        os.makedirs(self.data_dir, exist_ok=True)

    def save_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            users = read_json(f'{self.data_dir}/users.json')
            users[user.id] = {
                'email': user.email,
                'password': user.password,
                'is_admin': user.is_admin
            }
            write_json(f'{self.data_dir}/users.json', users)

    def save_place(self, place):
        if app.config['USE_DATABASE']:
            db.session.add(place)
            db.session.commit()
        else:
            places = read_json(f'{self.data_dir}/places.json')
            places[place.id] = {
                'name': place.name,
                'description': place.description,
                'city_id': place.city_id
            }
            write_json(f'{self.data_dir}/places.json', places)

    def save_city(self, city):
        if app.config['USE_DATABASE']:
            db.session.add(city)
            db.session.commit()
        else:
            cities = read_json(f'{self.data_dir}/cities.json')
            cities[city.id] = {
                'name': city.name,
                'country_id': city.country_id
            }
            write_json(f'{self.data_dir}/cities.json', cities)

    def save_country(self, country):
        if app.config['USE_DATABASE']:
            db.session.add(country)
            db.session.commit()
        else:
            countries = read_json(f'{self.data_dir}/countries.json')
            countries[country.id] = {'name': country.name}
            write_json(f'{self.data_dir}/countries.json', countries)

    def save_amenity(self, amenity):
        if app.config['USE_DATABASE']:
            db.session.add(amenity)
            db.session.commit()
        else:
            amenities = read_json(f'{self.data_dir}/amenities.json')
            amenities[amenity.id] = {'name': amenity.name}
            write_json(f'{self.data_dir}/amenities.json', amenities)

    def get_user(self, user_id):
        if app.config['USE_DATABASE']:
            return User.query.get(user_id)
        else:
            users = read_json(f'{self.data_dir}/users.json')
            user_data = users.get(user_id)
            if user_data:
                return User(
                    id=user_id,
                    email=user_data['email'],
                    password=user_data['password'],
                    is_admin=user_data['is_admin']
                )

    def get_place(self, place_id):
        if app.config['USE_DATABASE']:
            return Place.query.get(place_id)
        else:
            places = read_json(f'{self.data_dir}/places.json')
            place_data = places.get(place_id)
            if place_data:
                return Place(
                    id=place_id,
                    name=place_data['name'],
                    description=place_data['description'],
                    city_id=place_data['city_id']
                )

    def get_city(self, city_id):
        if app.config['USE_DATABASE']:
            return City.query.get(city_id)
        else:
            cities = read_json(f'{self.data_dir}/cities.json')
            city_data = cities.get(city_id)
            if city_data:
                return City(
                    id=city_id,
                    name=city_data['name'],
                    country_id=city_data['country_id']
                )

    def get_country(self, country_id):
        if app.config['USE_DATABASE']:
            return Country.query.get(country_id)
        else:
            countries = read_json(f'{self.data_dir}/countries.json')
            country_data = countries.get(country_id)
            if country_data:
                return Country(id=country_id, name=country_data['name'])

    def get_amenity(self, amenity_id):
        if app.config['USE_DATABASE']:
            return Amenity.query.get(amenity_id)
        else:
            amenities = read_json(f'{self.data_dir}/amenities.json')
            amenity_data = amenities.get(amenity_id)
            if amenity_data:
                return Amenity(id=amenity_id, name=amenity_data['name'])

    def delete_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.delete(user)
            db.session.commit()
        else:
            users = read_json(f'{self.data_dir}/users.json')
            if user.id in users:
                del users[user.id]
                write_json(f'{self.data_dir}/users.json', users)

    def delete_place(self, place):
        if app.config['USE_DATABASE']:
            db.session.delete(place)
            db.session.commit()
        else:
            places = read_json(f'{self.data_dir}/places.json')
            if place.id in places:
                del places[place.id]
                write_json(f'{self.data_dir}/places.json', places)

    def delete_city(self, city):
        if app.config['USE_DATABASE']:
            db.session.delete(city)
            db.session.commit()
        else:
            cities = read_json(f'{self.data_dir}/cities.json')
            if city.id in cities:
                del cities[city.id]
                write_json(f'{self.data_dir}/cities.json', cities)

    def delete_country(self, country):
        if app.config['USE_DATABASE']:
            db.session.delete(country)
            db.session.commit()
        else:
            countries = read_json(f'{self.data_dir}/countries.json')
            if country.id in countries:
                del countries[country.id]
                write_json(f'{self.data_dir}/countries.json', countries)

    def delete_amenity(self, amenity):
        if app.config['USE_DATABASE']:
            db.session.delete(amenity)
            db.session.commit()
        else:
            amenities = read_json(f'{self.data_dir}/amenities.json')
            if amenity.id in amenities:
                del amenities[amenity.id]
                write_json(f'{self.data_dir}/amenities.json', amenities)
