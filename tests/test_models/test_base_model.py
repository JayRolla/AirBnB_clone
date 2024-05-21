#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Defines tests for BaseModel class.
    """

    def test_init(self):
        """
        Test initialization of BaseModel instances.
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), expected)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

