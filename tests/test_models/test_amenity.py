#!/usr/bin/python3
"""
Unit test for the Amenity class
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_name_type(self):
        """Test type of name."""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity.name, str))

    def test_instantiation(self):
        """Test instantiation of Amenity object."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

if __name__ == '__main__':
    unittest.main()

