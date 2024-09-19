"""
Expert-Level Cheat Sheet: Basic Syntax and Data Types - Type conversion and casting - in the Python Programming Language

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization

This cheat sheet serves as a comprehensive guide to type conversion and casting in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Sabbir
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import time
import timeit
from typing import Any, Union, List, Dict, Tuple
from decimal import Decimal
from fractions import Fraction

# 1. Overview and Historical Context
"""
Type conversion and casting in Python refer to the process of changing an object's data type.
These concepts are fundamental to Python's dynamic typing system and play a crucial role in
data manipulation and interoperability between different parts of a program.

Historical Context:
- Python has supported type conversion since its inception in 1991.
- Python 2 had separate functions for integer division ('/') and true division ('//').
- Python 3 unified division under '/' and introduced '//' for floor division.
- Type hints were introduced in Python 3.5 (PEP 484) to support static type checking.

In modern software development, understanding type conversion is crucial for:
- Data processing and analysis
- Interfacing with external systems and APIs
- Optimizing performance in critical code sections
- Ensuring type safety in large-scale applications

Compared to other languages:
- Python's dynamic typing allows for more flexible type conversion than statically-typed languages like Java or C++.
- Python's type conversion is generally more implicit than in languages like C, where explicit casting is often required.
- Python's 'duck typing' philosophy means that explicit type conversion is often unnecessary in day-to-day coding.
"""

# 2. Syntax, Key Concepts, and Code Examples

def basic_type_conversion():
    """Demonstrates basic type conversion in Python."""
    # Integer to Float
    int_num = 10
    float_num = float(int_num)
    print(f"Integer {int_num} to Float: {float_num}")

    # Float to Integer (truncation occurs)
    float_num = 10.8
    int_num = int(float_num)
    print(f"Float {float_num} to Integer: {int_num}")

    # String to Integer
    str_num = "100"
    int_num = int(str_num)
    print(f"String '{str_num}' to Integer: {int_num}")

    # Integer to String
    int_num = 200
    str_num = str(int_num)
    print(f"Integer {int_num} to String: '{str_num}'")

    # String to Float
    str_num = "3.14"
    float_num = float(str_num)
    print(f"String '{str_num}' to Float: {float_num}")

    # Boolean to Integer
    bool_val = True
    int_num = int(bool_val)
    print(f"Boolean {bool_val} to Integer: {int_num}")

def advanced_type_conversion():
    """Demonstrates more advanced type conversion techniques."""
    # List to Tuple
    list_example = [1, 2, 3]
    tuple_example = tuple(list_example)
    print(f"List {list_example} to Tuple: {tuple_example}")

    # Tuple to List
    tuple_example = (4, 5, 6)
    list_example = list(tuple_example)
    print(f"Tuple {tuple_example} to List: {list_example}")

    # String to List of characters
    str_example = "Hello"
    list_chars = list(str_example)
    print(f"String '{str_example}' to List of characters: {list_chars}")

    # List of integers to List of strings
    int_list = [1, 2, 3]
    str_list = list(map(str, int_list))
    print(f"List of integers {int_list} to List of strings: {str_list}")

    # Dictionary keys to List
    dict_example = {'a': 1, 'b': 2, 'c': 3}
    keys_list = list(dict_example.keys())
    print(f"Dictionary keys to List: {keys_list}")

    # Set to List
    set_example = {1, 2, 3, 3, 2, 1}  # Duplicate values are removed in sets
    list_from_set = list(set_example)
    print(f"Set {set_example} to List: {list_from_set}")

def implicit_type_conversion():
    """Demonstrates implicit type conversion (type coercion) in Python."""
    # Integer and Float in arithmetic operations
    result = 5 + 3.14
    print(f"5 + 3.14 = {result} (type: {type(result)})")

    # String and Integer concatenation
    num = 42
    message = "The answer is " + str(num)  # Explicit conversion required
    print(message)

    # Boolean in arithmetic operations
    result = True + 1  # True is treated as 1
    print(f"True + 1 = {result}")

def type_checking():
    """Demonstrates various methods of type checking in Python."""
    # Using type() function
    x = 5
    print(f"Type of x is: {type(x)}")

    # Using isinstance() function
    y = "Hello"
    print(f"Is y a string? {isinstance(y, str)}")

    # Checking multiple types with isinstance()
    z = 3.14
    print(f"Is z a float or an integer? {isinstance(z, (float, int))}")

def custom_type_conversion():
    """Demonstrates custom type conversion using magic methods."""
    class Dollar:
        def __init__(self, amount):
            self.amount = amount

        def __str__(self):
            return f"${self.amount:.2f}"

        def __int__(self):
            return int(self.amount)

        def __float__(self):
            return float(self.amount)

    money = Dollar(49.99)
    print(f"Dollar object: {money}")
    print(f"As integer: {int(money)}")
    print(f"As float: {float(money)}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def best_practices():
    """Demonstrates best practices for type conversion and casting."""
    # Use explicit conversion for clarity
    num_str = "42"
    num = int(num_str)  # Clear intention to convert string to integer

    # Use isinstance() for flexible type checking
    def process_number(num):
        if isinstance(num, (int, float)):
            return num * 2
        raise TypeError("Expected int or float")

    # Handle potential conversion errors
    try:
        num = int("not a number")
    except ValueError as e:
        print(f"Conversion error: {e}")

    # Use appropriate numeric types
    from decimal import Decimal
    price = Decimal('19.99')  # More precise than float for financial calculations

def common_pitfalls():
    """Highlights common pitfalls in type conversion and casting."""
    # Loss of precision in float to int conversion
    float_num = 3.99
    int_num = int(float_num)
    print(f"Float {float_num} to int: {int_num}")  # Loses the decimal part

    # Unexpected results with boolean conversion
    print(f"bool('False'): {bool('False')}")  # True, because non-empty string
    print(f"bool(0): {bool(0)}")  # False
    print(f"bool(0.0): {bool(0.0)}")  # False
    print(f"bool([]): {bool([])}")  # False, empty list

    # Silent truncation in string to float conversion
    str_num = "3.14.15"
    try:
        float_num = float(str_num)
    except ValueError as e:
        print(f"Conversion error: {e}")

def advanced_tips():
    """Provides advanced tips for type conversion and casting."""
    # Using functools.singledispatch for type-based function dispatch
    from functools import singledispatch

    @singledispatch
    def fun(arg):
        print(f"Default behavior: {arg}")

    @fun.register(int)
    def _(arg):
        print(f"Integer behavior: {arg * 2}")

    @fun.register(str)
    def _(arg):
        print(f"String behavior: {arg.upper()}")

    fun(10)  # Calls integer version
    fun("hello")  # Calls string version
    fun(3.14)  # Calls default version

    # Using abstract base classes for more robust type checking
    from collections.abc import Sequence

    def process_sequence(seq: Sequence):
        return len(seq)

    print(process_sequence([1, 2, 3]))  # Works with list
    print(process_sequence("hello"))  # Works with string
    print(process_sequence((1, 2)))  # Works with tuple

def type_conversion_testing():
    """Demonstrates how to write tests for type conversion code."""
    import unittest

    class TestTypeConversion(unittest.TestCase):
        def test_string_to_int(self):
            self.assertEqual(int("42"), 42)

        def test_float_to_int(self):
            self.assertEqual(int(3.14), 3)

        def test_invalid_string_to_int(self):
            with self.assertRaises(ValueError):
                int("not a number")

    # Run the tests
    unittest.main(argv=[''], exit=False)

# 4. Integration and Real-World Applications

def data_processing_example():
    """Demonstrates type conversion in a data processing scenario."""
    # Simulating data from a CSV file
    data = [
        "John,25,1000.50",
        "Jane,30,1500.75",
        "Bob,22,800.25"
    ]

    # Processing the data
    processed_data = []
    for record in data:
        name, age, salary = record.split(',')
        processed_record = {
            'name': name,
            'age': int(age),
            'salary': float(salary)
        }
        processed_data.append(processed_record)

    # Calculating average age and total salary
    total_age = sum(record['age'] for record in processed_data)
    total_salary = sum(record['salary'] for record in processed_data)
    avg_age = total_age / len(processed_data)

    print(f"Processed data: {processed_data}")
    print(f"Average age: {avg_age:.2f}")
    print(f"Total salary: ${total_salary:.2f}")

def api_integration_example():
    """Simulates type conversion in API integration."""
    # Simulated API response
    api_response = {
        "user_id": "1234",
        "name": "Alice",
        "is_active": "true",
        "score": "95.5"
    }

    # Converting API response to appropriate types
    user = {
        "user_id": int(api_response["user_id"]),
        "name": api_response["name"],
        "is_active": api_response["is_active"].lower() == "true",
        "score": float(api_response["score"])
    }

    print(f"Converted API response: {user}")

# 5. Advanced Concepts and Emerging Trends

def advanced_concepts():
    """Explores advanced concepts and emerging trends in Python type conversion."""
    # Type hints and runtime checking
    from typing import List, Union

    def process_numbers(numbers: List[Union[int, float]]) -> float:
        return sum(float(num) for num in numbers)

    result = process_numbers([1, 2.5, "3", 4])  # Note: "3" is a string
    print(f"Sum of numbers: {result}")

    # Using Abstract Base Classes for duck typing
    from collections.abc import Iterable

    def sum_iterable(obj: Iterable) -> Union[int, float]:
        return sum(float(item) for item in obj)

    print(sum_iterable([1, 2, 3]))  # Works with list
    print(sum_iterable({4, 5, 6}))  # Works with set
    print(sum_iterable((7, 8, 9)))  # Works with tuple

    # Structural Pattern Matching (Python 3.10+)
    def type_match(obj):
        match obj:
            case int():
                return "Integer"
            case float():
                return "Float"
            case str():
                return "String"
            case _:
                return "Unknown"

    print(type_match(42))
    print(type_match(3.14))
    print(type_match("hello"))
    print(type_match([1, 2, 3]))

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to type conversion."""
    # Q: How do I convert a string to a datetime object?
    from datetime import datetime
    date_string = "2023-09-18 14:30:00"
    date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(f"Converted datetime: {date_object}")

    # Q: How can I safely convert user input to a number?
    def safe_convert_to_number(value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return None

    print(safe_convert_to_number("42"))  # Integer
    print(safe_convert_to_number("3.14"))  # Float
    print(safe_convert_to_number("not a number"))  # None

    # Q: How do I handle encoding issues when converting between strings and bytes?
    text = "Hello, 世界"
    encoded = text.encode('utf-8')
    decoded = encoded.decode('utf-8')
    print(f"Original: {text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")

# 7. Recommended Tools, Libraries, and Resources

"""
Recommended tools and libraries for type conversion and casting:

1. mypy: Static type checker for Python
   pip install mypy

2. pydantic: Data validation and settings management using Python type annotations
   pip install pydantic

3. typeguard: Runtime type checker for Python
   pip install typeguard

4. PyConvert: A Python library for easy and flexible type conversions
   pip install pyconvert

5. NumPy: Offers efficient type conversion for numerical computations
   pip install numpy

Resources for further learning:
- Python Official Documentation on Built-in Types: https://docs.python.org/3/library/stdtypes.html
- "Fluent Python" by Luciano Ramalho (O'Reilly Media)
- "Effective Python" by Brett Slatkin (Addison-Wesley Professional)
- Real Python's Guide to Type Checking: https://realpython.com/python-type-checking/
- PyData conference talks on YouTube for advanced numerical type handling
"""

# 8. Performance Analysis