README

Python - almost a circle

Background Context
in this project, we will review everything about Python:
Import
Exceptions
Class
Private attribute
Getter/Setter
Class method
Static method
Inheritance
Unittest
Read/Write file

We will also learn about:
args and kwargs
Serialization/Deserialization
JSON

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.\*)
All your files must be executable
The length of your files will be tested using wc
All your modules should be documented: python3 -c 'print(**import**("my_module").**doc**)'
All your classes should be documented: python3 -c 'print(**import**("my_module").MyClass.**doc**)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(**import**("my_module").my_function.**doc**) and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)'
A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test\_
Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
We strongly encourage you to work together on test cases so that you don't miss any edge case

Tasks: 0. If it's not tested it doesn't work
-All your files, classes and methods must be unit tested and be PEP 8 validated

1. Base class
   -Write the first class Base:

2. First Rectangle
   -Write the class Rectangle that inherits from Base:

3. Validate attributes
   -Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

4. Area first
   -Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. Display #0
   -Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

6. **str**
   -Update the class Rectangle by overriding the **str** method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

7. Display #1
   -Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

8. Update #0
   -Update the class Rectangle by adding the public method def update(self, \*args): that assigns an argument to each attribute:

9. Update #1
   -Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, \*\*kwargs) that assigns a key/value argument to attributes:

10. And now, the Square!
    -Write the class Square that inherits from Rectangle:

11. Square size
    -Update the class Square by adding the public getter and setter size

12. Square update
    -Update the class Square by adding the public method def update(self, \*args, \*\*kwargs) that assigns attributes:

13. Rectangle instance to dictionary representation
    -Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:

14. Square instance to dictionary representation
    -Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

15. Dictionary to JSON string
    -JSON is one of the standard formats for sharing data representation. Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string represented of list_dictionaries:

16. JSON string to file
    -Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

17. JSON string to dictionary
    -Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

18. Dictionary to Instance
    -Update the class Base by adding the class method def create(cls, \*\*dictionary): that returns an instance with all attributes already set:

19. File to instances
    -Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:
