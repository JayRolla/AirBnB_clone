#!/usr/bin/python3
"""
Enhanced command interpreter for managing the AirBnB objects.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, line):
        """Handle advanced class command syntax <class name>.action()."""
        try:
            cls_name, command = line.split(".")
            if cls_name in self.class_dict:
                if command == "all()":
                    self.do_all(cls_name)
                elif command == "count()":
                    self.do_count(cls_name)
                elif command.startswith("show("):
                    idx = command.find("(") + 1
                    id = command[idx:-2].replace('"', '').replace("'", "")
                    self.do_show(f"{cls_name} {id}")
                elif command.startswith("destroy("):
                    idx = command.find("(") + 1
                    id = command[idx:-2].replace('"', '').replace("'", "")
                    self.do_destroy(f"{cls_name} {id}")
                elif command.startswith("update("):
                    args = command[7:-2].split(", ")
                    if len(args) == 3:
                        obj_id, attr_name, attr_value = args
                        obj_id = obj_id.replace('"', '').replace("'", "")
                        attr_name = attr_name.replace('"', '').replace("'", "")
                        attr_value = attr_value.replace('"', '').replace("'", "")
                        self.do_update(f"{cls_name} {obj_id} {attr_name} {attr_value}")
                    elif len(args) == 2:
                        obj_id, dictionary = args
                        obj_id = obj_id.replace('"', '').replace("'", "")
                        self.do_update(f"{cls_name} {obj_id} {dictionary}")
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print("*** Unknown syntax:", line)

    def do_create(self, arg):
        """Creates a new instance of specified class, saves it to the JSON file, and prints the id."""
        if not arg or arg not in self.class_dict:
            print("** class name missing **" if not arg else "** class doesn't exist **")
        else:
            new_obj = self.class_dict[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Shows an instance based on its class and id."""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            obj_dict = storage.all()
            obj_key = f"{args[0]}.{args[1]}"
            if obj_key in obj_dict:
                print(obj_dict[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance based on its class and id."""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            obj_dict = storage.all()
            obj_key = f"{args[0]}.{args[1]}"
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class, or all instances if no class is specified."""
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
        elif arg in self.class_dict:
            print([str(obj) for obj in obj_dict.values() if isinstance(obj, self.class_dict[arg])])
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        if arg in self.class_dict:
            print(len([obj for obj in storage.all().values() if isinstance(obj, self.class_dict[arg])]))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attributes."""
        args = arg.split()
        if len(args) < 3:
            print("** attribute name missing **" if len(args) == 2 else "** instance id missing **")
        elif args[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            obj_dict = storage.all()
            obj_key = f"{args[0]}.{args[1]}"
            if obj_key in obj_dict:
                obj = obj_dict[obj_key]
                if len(args) == 4:
                    setattr(obj, args[2], args[3])
                    obj.save()
                elif len(args) == 3 and isinstance(args[2], dict):
                    for key, value in args[2].items():
                        setattr(obj, key, value)
                    obj.save()
                else:
                    print("** value missing **")
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

