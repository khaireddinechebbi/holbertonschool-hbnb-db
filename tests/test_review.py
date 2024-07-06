#!/usr/bin/python3

import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.user import User
from Models.place import Place
from Models.review import Review


class TestReview(unittest.TestCase):
    def test_review_creation(self):
        user = User("reviewer@example.com", "password", "Reviewer", "User")
        place = Place("Beach House", "A house by the beach", "123 Ocean Ave", "Miami", 25.7617, -80.1918, None, 3, 2, 300, 6)
        review = Review(user, place, "Amazing place!", 5)
        self.assertEqual(review.user, user)
        self.assertEqual(review.place, place)
        self.assertEqual(review.text, "Amazing place!")
        self.assertEqual(review.rating, 5)


if __name__ == '__main__':
    unittest.main()
