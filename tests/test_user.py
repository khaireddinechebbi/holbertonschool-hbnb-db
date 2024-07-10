#!/usr/bin/python3
"""
"""
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User


class Test(unittest.TestCase):
    def test_creation(self):
        user = User("khaireddine.chebbi@live.fr", "12345", "Khaireddine", "Chebbi")
        self.assertEqual(user.email, "khaireddine.chebbi@live.fr")
        self.assertEqual(user.first_name, "Khaireddine")
        self.assertEqual(user.last_name, "Chebbi")

    def test_id(self):
        user1 = User("khaireddine.chebbi@live.fr", "12345", "Khaireddine", "Chebbi")
        user2 = User("Mike_tayson@gmail.com", "12345", "Mike", "Tayson")
        self.assertNotEqual(user1.id, user2.id)


if __name__ == '__main__':
    unittest.main()
