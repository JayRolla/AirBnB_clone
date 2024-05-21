#!/usr/bin/python3
"""
Unit test for the City class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_state_id_type(self):
        """Test type of state_id."""
        city = City()
        self.assertTrue(isinstance(city.state_id, str))

    def test_name_type(self):
        """Test type of name."""
        city = City()
        self.assertTrue(isinstance(city.name, str))

    def test_instantiation(self):
        """Test instantiation of City object."""
        city = City()
        self.assertIsInstance(city, City)

if __name__ == '__main__':
    unittest.main()

