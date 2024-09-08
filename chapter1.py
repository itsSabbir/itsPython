# Python Cheat Sheet: Data Types and Variables

# 1. Basic Data Types

# Integer: Whole numbers (positive, negative, or zero)
integer_var = 42
print(f"Integer: {integer_var}")  # Output: Integer: 42

# Float: Decimal numbers
float_var = 3.14159
print(f"Float: {float_var}")  # Output: Float: 3.14159

# String: Sequence of characters
str_var = "Hello, Python!"
print(f"String: {str_var}")  # Output: String: Hello, Python!

# Boolean: True or False
bool_var = True
print(f"Boolean: {bool_var}")  # Output: Boolean: True

# NoneType: Represents absence of a value
none_var = None
print(f"NoneType: {none_var}")  # Output: NoneType: None

# Check the type of a variable
print(type(integer_var))  # Output: <class 'int'>
print(type(float_var))    # Output: <class 'float'>
print(type(str_var))      # Output: <class 'str'>
print(type(bool_var))     # Output: <class 'bool'>
print(type(none_var))     # Output: <class 'NoneType'>

# 2. Type Conversion and Casting

# String to Integer
str_to_int = int("42")
print(f"String to Integer: {str_to_int}, Type: {type(str_to_int)}")

# Float to Integer (truncates decimal part)
float_to_int = int(3.14)
print(f"Float to Integer: {float_to_int}, Type: {type(float_to_int)}")

# Integer to Float
int_to_float = float(42)
print(f"Integer to Float: {int_to_float}, Type: {type(int_to_float)}")

# Integer to String
int_to_str = str(42)
print(f"Integer to String: {int_to_str}, Type: {type(int_to_str)}")

# Be careful when converting floats to integers
print(f"int(3.9) = {int(3.9)}")  # Output: 3 (decimal part is truncated)

# 3. Mutable vs Immutable Data Types

# Immutable: int, float, str, tuple
immutable_str = "Hello"
try:
    immutable_str[0] = "h"
except TypeError as e:
    print(f"Error: {e}")  # Output: 'str' object does not support item assignment

# Mutable: list, dict, set
mutable_list = [1, 2, 3]
mutable_list[0] = 4
print(f"Modified list: {mutable_list}")  # Output: [4, 2, 3]

# Checking object identity
original_id = id(mutable_list)
mutable_list.append(5)
new_id = id(mutable_list)
print(f"List IDs same after modification: {original_id == new_id}")  # Output: True

original_id = id(immutable_str)
immutable_str += " World"
new_id = id(immutable_str)
print(f"String IDs same after modification: {original_id == new_id}")  # Output: False

# 4. Complex Numbers

complex_var = 2 + 3j
print(f"Complex: {complex_var}")
print(f"Real part: {complex_var.real}, Imaginary part: {complex_var.imag}")

# Complex number operations
complex_var2 = 1 - 2j
print(f"Addition: {complex_var + complex_var2}")
print(f"Multiplication: {complex_var * complex_var2}")
print(f"Absolute value: {abs(complex_var)}")

# 5. Variables and Assignment

# Dynamic typing
x = 5
print(f"x is initially an integer: {x}")
x = "Now I'm a string"
print(f"x is now a string: {x}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Swapping variables
a, b = b, a
print(f"After swapping: a={a}, b={b}")

# Augmented assignment operators
x = 10
x += 5  # Equivalent to x = x + 5
print(f"Augmented assignment: x += 5 results in x = {x}")

# 6. Constants

# Python doesn't have built-in constant types, but it's a convention to use uppercase names
PI = 3.14159
MAX_SIZE = 100

print(f"PI: {PI}")
print(f"MAX_SIZE: {MAX_SIZE}")

# 7. String Operations

# Concatenation
greeting = "Hello" + " " + "World"
print(f"Concatenation: {greeting}")

# Repetition
repeated = "Python " * 3
print(f"Repetition: {repeated}")

# Indexing and Slicing
text = "Python"
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Slicing (1:4): {text[1:4]}")
print(f"Reverse: {text[::-1]}")

# String methods
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {'hello world'.title()}")
print(f"Strip whitespace: {'  spacey  '.strip()}")

# String formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")  # f-string (Python 3.6+)
print("{} is {} years old".format(name, age))  # .format() method
print("%s is %d years old" % (name, age))  # %-formatting (older style)

# 8. Type Hints (Python 3.5+)

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Type hints are not enforced at runtime
print(greet("Alice"))  # Works fine
print(greet(123))  # Also works, but might be flagged by type checkers

# 9. Memory Management

import sys

# Reference counting and garbage collection
x = [1, 2, 3]
y = x  # y references the same object as x
print(f"x id: {id(x)}, y id: {id(y)}")

del x  # Decreases reference count, but object still exists because y references it
print(f"y after deleting x: {y}")

# Check memory size of an object
int_var = 42
float_var = 3.14
list_var = [1, 2, 3]
dict_var = {'a': 1, 'b': 2}

print(f"Size of int: {sys.getsizeof(int_var)} bytes")
print(f"Size of float: {sys.getsizeof(float_var)} bytes")
print(f"Size of list: {sys.getsizeof(list_var)} bytes")
print(f"Size of dict: {sys.getsizeof(dict_var)} bytes")

# 10. Additional Data Types

# Tuples (immutable sequences)
tuple_var = (1, 2, 3)
print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")

# Sets (unordered collections of unique elements)
set_var = {1, 2, 3, 3, 2, 1}
print(f"Set: {set_var}, Type: {type(set_var)}")

# Dictionaries (key-value pairs)
dict_var = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")
print(f"Accessing dictionary value: {dict_var['name']}")

# Bytes and Bytearray
bytes_var = b'hello'
bytearray_var = bytearray(b'hello')
print(f"Bytes: {bytes_var}, Type: {type(bytes_var)}")
print(f"Bytearray: {bytearray_var}, Type: {type(bytearray_var)}")

# This concludes the detailed Python Cheat Sheet for Data Types and Variables