#!/usr/bin/python3
"""
Unit test for the Review class
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_attributes_types(self):
        """Test attribute types."""
        review = Review()
        self.assertTrue(isinstance(review.place_id, str))
        self.assertTrue(isinstance(review.user_id, str))
        self.assertTrue(isinstance(review.text, str))

    def test_instantiation(self):
        """Test instantiation of Review object."""
        review = Review()
        self.assertIsInstance(review, Review)

if __name__ == '__main__':
    unittest.main()

