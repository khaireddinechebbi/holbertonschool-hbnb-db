import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.user import User
from Models.country import Country
from Models.city import City
from Models.amenity import Amenity
from Models.place import Place
from Models.review import Review

class DataManager:
    def __init__(self):
        self.use_database = os.getenv('USE_DATABASE', 'True').lower() == 'true'
        if self.use_database:
            self.engine = create_engine("sqlite:///mydb.db", echo=True)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

    def save(self, entity_type, entity_id, entity_data):
        """Save an entity to the database or file-based storage."""
        if self.use_database:
            self._save_to_database(entity_type, entity_id, entity_data)
        else:
            self._save_to_file(entity_type, entity_id, entity_data)

    def get(self, entity_type, entity_id):
        """Retrieve an entity by ID from the database or file-based storage."""
        if self.use_database:
            return self._get_from_database(entity_type, entity_id)
        else:
            return self._get_from_file(entity_type, entity_id)

    def update(self, entity_type, entity_id, entity_data):
        """Update an entity in the database or file-based storage."""
        if self.use_database:
            self._update_in_database(entity_type, entity_id, entity_data)
        else:
            self._update_in_file(entity_type, entity_id, entity_data)

    def delete(self, entity_type, entity_id):
        """Delete an entity from the database or file-based storage."""
        if self.use_database:
            self._delete_from_database(entity_type, entity_id)
        else:
            self._delete_from_file(entity_type, entity_id)

    def get_all(self, entity_type):
        """Retrieve all entities of a specific type from the database or file-based storage."""
        if self.use_database:
            return self._get_all_from_database(entity_type)
        else:
            return self._get_all_from_file(entity_type)

    # Database operations

    def _save_to_database(self, entity_type, entity_id, entity_data):
        """Save an entity to the database."""
        if entity_type == 'users':
            new_user = User(
                id=entity_id,
                email=entity_data['email'],
                password=entity_data['password'],
                first_name=entity_data['first_name'],
                last_name=entity_data['last_name'],
                created_at=entity_data['created_at'],
                updated_at=entity_data['updated_at']
            )
            self.session.add(new_user)

        elif entity_type == 'countries':
            new_country = Country(
                id=entity_id,
                name=entity_data['name'],
                code=entity_data['code']
            )
            self.session.add(new_country)

        elif entity_type == 'cities':
            new_city = City(
                id=entity_id,
                name=entity_data['name'],
                country_code=entity_data['country_code']
            )
            self.session.add(new_city)

        elif entity_type == 'amenities':
            new_amenity = Amenity(
                id=entity_id,
                name=entity_data['name']
            )
            self.session.add(new_amenity)

        elif entity_type == 'places':
            new_place = Place(
                id=entity_id,
                name=entity_data['name'],
                description=entity_data['description'],
                address=entity_data['address'],
                city_id=entity_data['city_id'],
                latitude=entity_data['latitude'],
                longitude=entity_data['longitude'],
                host_id=entity_data['host_id'],
                number_of_rooms=entity_data['number_of_rooms'],
                number_of_bathrooms=entity_data['number_of_bathrooms'],
                price_per_night=entity_data['price_per_night'],
                max_guests=entity_data['max_guests'],
                created_at=entity_data['created_at'],
                updated_at=entity_data['updated_at']
            )
            self.session.add(new_place)

        elif entity_type == 'reviews':
            new_review = Review(
                id=entity_id,
                user_id=entity_data['user_id'],
                place_id=entity_data['place_id'],
                text=entity_data['text'],
                rating=entity_data['rating'],
                created_at=entity_data['created_at'],
                updated_at=entity_data['updated_at']
            )
            self.session.add(new_review)

        self.session.commit()

    def _get_from_database(self, entity_type, entity_id):
        """Retrieve an entity by ID from the database."""
        if entity_type == 'users':
            return self.session.query(User).get(entity_id)

        elif entity_type == 'countries':
            return self.session.query(Country).get(entity_id)

        elif entity_type == 'cities':
            return self.session.query(City).get(entity_id)

        elif entity_type == 'amenities':
            return self.session.query(Amenity).get(entity_id)

        elif entity_type == 'places':
            return self.session.query(Place).get(entity_id)

        elif entity_type == 'reviews':
            return self.session.query(Review).get(entity_id)

        return None

    def _update_in_database(self, entity_type, entity_id, entity_data):
        """Update an entity in the database."""
        entity = self._get_from_database(entity_type, entity_id)
        if entity:
            if entity_type == 'users':
                entity.email = entity_data['email']
                entity.password = entity_data['password']
                entity.first_name = entity_data['first_name']
                entity.last_name = entity_data['last_name']
                entity.updated_at = entity_data['updated_at']

            elif entity_type == 'countries':
                entity.name = entity_data['name']
                entity.code = entity_data['code']

            elif entity_type == 'cities':
                entity.name = entity_data['name']
                entity.country_code = entity_data['country_code']

            elif entity_type == 'amenities':
                entity.name = entity_data['name']

            elif entity_type == 'places':
                entity.name = entity_data['name']
                entity.description = entity_data['description']
                entity.address = entity_data['address']
                entity.city_id = entity_data['city_id']
                entity.latitude = entity_data['latitude']
                entity.longitude = entity_data['longitude']
                entity.host_id = entity_data['host_id']
                entity.number_of_rooms = entity_data['number_of_rooms']
                entity.number_of_bathrooms = entity_data['number_of_bathrooms']
                entity.price_per_night = entity_data['price_per_night']
                entity.max_guests = entity_data['max_guests']
                entity.updated_at = entity_data['updated_at']

            elif entity_type == 'reviews':
                entity.user_id = entity_data['user_id']
                entity.place_id = entity_data['place_id']
                entity.text = entity_data['text']
                entity.rating = entity_data['rating']
                entity.updated_at = entity_data['updated_at']

            self.session.commit()
            return True
        return False

    def _delete_from_database(self, entity_type, entity_id):
        """Delete an entity from the database."""
        entity = self._get_from_database(entity_type, entity_id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return True
        return False

    def _get_all_from_database(self, entity_type):
        """Retrieve all entities of a specific type from the database."""
        if entity_type == 'users':
            return self.session.query(User).all()

        elif entity_type == 'countries':
            return self.session.query(Country).all()

        elif entity_type == 'cities':
            return self.session.query(City).all()

        elif entity_type == 'amenities':
            return self.session.query(Amenity).all()

        elif entity_type == 'places':
            return self.session.query(Place).all()

        elif entity_type == 'reviews':
            return self.session.query(Review).all()

        return []

    # File-based operations

    def _save_to_file(self, entity_type, entity_id, entity_data):
        """Save an entity to a file-based storage."""
        filename = f"{entity_type}.json"
        if os.path.exists(filename):
            with open(filename, 'r+') as file:
                entities = json.load(file)
                entities.append({
                    'id': entity_id,
                    **entity_data
                })
                file.seek(0)
                json.dump(entities, file, indent=4)
        else:
            with open(filename, 'w') as file:
                json.dump([{
                    'id': entity_id,
                    **entity_data
                }], file, indent=4)

    def _get_from_file(self, entity_type, entity_id):
        """Retrieve an entity from a file-based storage."""
        filename = f"{entity_type}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                entities = json.load(file)
                for entity in entities:
                    if entity['id'] == entity_id:
                        return entity
        return None

    def _update_in_file(self, entity_type, entity_id, entity_data):
        """Update an entity in a file-based storage."""
        filename = f"{entity_type}.json"
        if os.path.exists(filename):
            with open(filename, 'r+') as file:
                entities = json.load(file)
                for entity in entities:
                    if entity['id'] == entity_id:
                        entity.update(entity_data)
                        file.seek(0)
                        json.dump(entities, file, indent=4)
                        file.truncate()
                        return True
        return False

    def _delete_from_file(self, entity_type, entity_id):
        """Delete an entity from a file-based storage."""
        filename = f"{entity_type}.json"
        if os.path.exists(filename):
            with open(filename, 'r+') as file:
                entities = json.load(file)
                updated_entities = [entity for entity in entities if entity['id'] != entity_id]
                file.seek(0)
                json.dump(updated_entities, file, indent=4)
                file.truncate()
                return True
        return False

    def _get_all_from_file(self, entity_type):
        """Retrieve all entities of a specific type from a file-based storage."""
        filename = f"{entity_type}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

data_manager = DataManager()