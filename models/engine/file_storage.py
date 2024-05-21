#!/usr/bin/python3
"""
FileStorage manages saving and loading data.
It turns our data into a JSON file when saving, and turns it back into objects when loading.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = 'file.json'  # Path to the JSON file where data will be stored.
    __objects = {}  # Dictionary to store all objects.

    def all(self):
        """Return all objects stored."""
        return self.__objects

    def new(self, obj):
        """Add a new object to our storage."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save all objects to a file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Load all objects from a file."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_id, obj_data in obj_dict.items():
                    cls_name = obj_data['__class__']
                    cls = eval(cls_name)
                    self.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            # If the file doesn't exist, we just skip loading.
            pass

