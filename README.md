# AirBnB Clone Project

## Description
This project is a simplified clone of AirBnB. It includes a custom command-line interface for managing your objects.

## Command Interpreter
The command interpreter is used to manage the application's functionalities from the command line.

### How to Start It
To start the command interpreter, navigate to the project directory and run:
```
./console.py
```

### How to Use It
Here are some basic commands you can use in the interpreter:

- `help`: Displays all documented commands.
- `quit`: Exits the command interpreter.
- `EOF`: Also exits the command interpreter.
- `create <class name>`: Creates a new instance of class.
- `show <class name> <id>`: Shows an instance based on the class name and id.
- `destroy <class name> <id>`: Deletes an instance based on the class name and id.
- `all <class name>`: Displays all instances of a class.

### Examples
Starting the interpreter:
```
$ ./console.py
(hbnb)
```

Listing all commands:
```
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
```

Creating a new instance of BaseModel:
```
(hbnb) create BaseModel
```

Exiting the interpreter:
```
(hbnb) quit
$
```

## Testing
To run tests, execute:
```
python3 -m unittest discover tests
```
Or for individual tests:
```
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
- Molapo Kgarose <JayRolla@github.com>

