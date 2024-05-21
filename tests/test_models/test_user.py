#!/usr/bin/python3
"""
Tests for the User class.
"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Defines tests for the User class."""

    def test_user_instance(self):
        """Check if a new user is an instance of User."""
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_user_attributes(self):
        """Check user attributes are initialized correctly."""
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

if __name__ == '__main__':
    unittest.main()

