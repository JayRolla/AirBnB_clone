#!/usr/bin/python3
"""
Unit test for the State class
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_name_type(self):
        """Test type of name."""
        state = State()
        self.assertTrue(isinstance(state.name, str))

    def test_instantiation(self):
        """Test instantiation of State object."""
        state = State()
        self.assertIsInstance(state, State)

if __name__ == '__main__':
    unittest.main()

