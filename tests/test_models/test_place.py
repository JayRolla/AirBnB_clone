#!/usr/bin/python3
"""
Unit test for the Place class
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_attributes_types(self):
        """Test attribute types."""
        place = Place()
        self.assertTrue(isinstance(place.city_id, str))
        self.assertTrue(isinstance(place.user_id, str))
        self.assertTrue(isinstance(place.name, str))
        self.assertTrue(isinstance(place.description, str))
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_instantiation(self):
        """Test instantiation of Place object."""
        place = Place()
        self.assertIsInstance(place, Place)

if __name__ == '__main__':
    unittest.main()

