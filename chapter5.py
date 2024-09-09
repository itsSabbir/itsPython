# Python Cheat Sheet: Modules and Packages (Detailed Version)

# 1. Importing Modules

# Basic import
import math
print(f"Pi: {math.pi}")  # Output: 3.141592653589793

# Import with alias
import math as m
print(f"Square root of 16: {m.sqrt(16)}")  # Output: 4.0

# Import specific items
from math import pi, sqrt
print(f"Pi: {pi}")    # Output: 3.141592653589793
print(f"Square root of 25: {sqrt(25)}")  # Output: 5.0

# Import all (use cautiously)
from math import *
print(f"Cosine of pi: {cos(pi)}")  # Output: -1.0

# Tip: Avoid using 'import *' in production code as it can lead to naming conflicts

# 2. Creating Modules

# Let's create a simple module named 'mymodule.py'
# Contents of 'mymodule.py':
"""
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f"{self.name} says hello!"
"""

# Now we can use our module
import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(f"PI from mymodule: {mymodule.PI}")  # Output: 3.14159

person = mymodule.Person("Bob")
print(person.say_hello())  # Output: Bob says hello!

# 3. Exploring Built-in Modules

# sys module
import sys

print(f"Python version: {sys.version}")
print(f"Module search paths: {sys.path}")
# sys.exit()  # This would exit the program

# os module
import os

print(f"Current working directory: {os.getcwd()}")
print(f"List of files and directories: {os.listdir()}")

# Create and remove a directory
os.mkdir("new_directory")
os.rmdir("new_directory")

print(f"Environment variables: {dict(os.environ)}")

# Use os.path for cross-platform file path handling
print(f"Joined path: {os.path.join('folder', 'subfolder', 'file.txt')}")

# datetime module
import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

# Create a specific date
date = datetime.date(2023, 6, 15)
print(f"Specific date: {date}")

# Time delta
delta = datetime.timedelta(days=7)
future_date = now + delta
print(f"Date 7 days from now: {future_date}")

# 4. Creating and Using Packages

# Assume we have the following directory structure:
# my_package/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# Contents of my_package/module1.py
"""
def greet(name):
    return f"Hello, {name}!"
"""

# Contents of my_package/module2.py
"""
def farewell(name):
    return f"Goodbye, {name}!"
"""

# Contents of my_package/subpackage/module3.py
"""
def calculate_square(n):
    return n ** 2
"""

# Contents of my_package/__init__.py
"""
from .module1 import greet
from .module2 import farewell
from .subpackage.module3 import calculate_square
"""

# Using the package
import my_package

print(my_package.greet("Alice"))  # Output: Hello, Alice!
print(my_package.farewell("Bob"))  # Output: Goodbye, Bob!
print(f"Square of 5: {my_package.calculate_square(5)}")  # Output: 25

# Alternative import methods
from my_package import greet, farewell
from my_package.subpackage.module3 import calculate_square

print(greet("Charlie"))  # Output: Hello, Charlie!
print(f"Square of 3: {calculate_square(3)}")  # Output: 9

# 5. Module Search Path

import sys
print(f"Module search paths: {sys.path}")

# Adding a directory to the module search path
sys.path.append('/path/to/your/module/directory')

# 6. Reloading a Module

import importlib

# Assume we've made changes to 'mymodule.py'
importlib.reload(mymodule)

# 7. Exploring Module Attributes

import math

# List all names in a module
print(f"Names in math module: {dir(math)}")

# Get help on a module
help(math)

# Check the file location of a module
print(f"Location of math module: {math.__file__}")

# 8. Creating a Module Dynamically

import types

dynamic_module = types.ModuleType("dynamic_module", "This is a dynamically created module")
dynamic_module.dynamic_variable = 42
print(f"Dynamic variable: {dynamic_module.dynamic_variable}")  # Output: 42

# 9. Using __all__ in a Module

# In a file named 'my_module.py':
"""
__all__ = ['public_function']

def public_function():
    pass

def _private_function():
    pass
"""

# When someone does 'from my_module import *', only 'public_function' will be imported

# 10. Circular Imports

# Circular imports can lead to issues. Here's how to handle them:

# file1.py
"""
from file2 import function_from_file2

def function_from_file1():
    return "I'm from file1"

print(function_from_file2())
"""

# file2.py
"""
from file1 import function_from_file1

def function_from_file2():
    return "I'm from file2"

print(function_from_file1())
"""

# To resolve, you can move the import inside the function:

# file1.py
"""
def function_from_file1():
    return "I'm from file1"

def use_file2():
    from file2 import function_from_file2
    print(function_from_file2())
"""

# file2.py
"""
def function_from_file2():
    return "I'm from file2"

def use_file1():
    from file1 import function_from_file1
    print(function_from_file1())
"""

# 11. Using Virtual Environments

# Create a virtual environment
# python -m venv myenv

# Activate the virtual environment
# On Windows: myenv\Scripts\activate
# On Unix or MacOS: source myenv/bin/activate

# Deactivate the virtual environment
# deactivate

# 12. Package Management with pip

# Install a package
# pip install package_name

# Install a specific version
# pip install package_name==1.0.4

# Upgrade a package
# pip install --upgrade package_name

# Uninstall a package
# pip uninstall package_name

# List installed packages
# pip list

# Generate a requirements file
# pip freeze > requirements.txt

# Install packages from a requirements file
# pip install -r requirements.txt

# This concludes the detailed Python Cheat Sheet for Modules and Packages