#!/usr/bin/python3

import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        user = User("host@example.com", "password", "Host", "User")
        place = Place("Beach House", "A house by the beach", "123 Ocean Ave", "Miami", 25.7617, -80.1918, user, 3, 2, 300, 6)
        self.assertEqual(place.name, "Beach House")
        self.assertEqual(place.city, "Miami")
        self.assertEqual(place.host, user)

    def test_add_amenity(self):
        place = Place("Beach House", "A house by the beach", "123 Ocean Ave", "Miami", 25.7617, -80.1918, None, 3, 2, 300, 6)
        place.add_amenity("WiFi")
        self.assertIn("WiFi", place.amenities)

    def test_add_review(self):
        user = User("host@example.com", "password", "Host", "User")
        place = Place("Beach House", "A house by the beach", "123 Ocean Ave", "Miami", 25.7617, -80.1918, user, 3, 2, 300, 6)
        review = {"text": "Great place!", "rating": 5}
        place.add_review(review)
        self.assertIn(review, place.reviews)


if __name__ == '__main__':
    unittest.main()
