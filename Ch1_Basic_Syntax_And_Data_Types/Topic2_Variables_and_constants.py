"""
Expert-Level Cheat Sheet: Basic Syntax and Data Types - Variables and constants - in the Python Programming Language

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization

This cheat sheet serves as a comprehensive guide to variables and constants in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Claude AI
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import time
from typing import Any, Dict, List, Union
from dataclasses import dataclass
from enum import Enum, auto

# 1. Overview and Historical Context
"""
Variables and constants are fundamental concepts in Python, used to store and manipulate data.

- Variables: Named references to memory locations that store data. They can be reassigned.
- Constants: Variables whose values should not change throughout the program execution.

Python, created by Guido van Rossum in 1991, has always supported variables. However, it lacks
built-in support for true constants. The community has adopted conventions to represent constants.

In modern software development, proper use of variables and constants is crucial for writing
clean, maintainable, and efficient code. Python's dynamic typing system offers flexibility
but requires careful consideration in variable management.

Compared to other languages:
- Unlike Java or C++, Python doesn't require explicit type declarations for variables.
- Python lacks true constants, unlike languages like C++ or Java which have the 'const' keyword.
- Python's use of uppercase names for constants is a convention, not enforced by the language.
"""

# 2. Syntax, Key Concepts, and Code Examples

def variable_basics():
    """Demonstrates basic variable usage in Python."""
    # Variable assignment
    x = 5  # Integer
    y = 3.14  # Float
    name = "Alice"  # String
    is_python_fun = True  # Boolean

    # Multiple assignment
    a, b, c = 1, 2, 3

    # Type inference and dynamic typing
    var = 10
    print(f"var is initially an integer: {var}")
    var = "Now I'm a string"
    print(f"var is now a string: {var}")

    # Variable naming conventions
    snake_case_variable = "This is the preferred naming style for variables in Python"
    UPPERCASE_CONSTANT = "This naming style is used for constants by convention"

    # Using variables in expressions
    result = x + y
    print(f"Result of {x} + {y} is {result}")

def constant_convention():
    """Demonstrates the convention for constants in Python."""
    # Constants are typically defined in all uppercase
    PI = 3.14159
    MAX_USERS = 1000
    DEFAULT_TIMEOUT = 30

    # Note: These are not true constants and can be modified
    PI = 3.14  # This is allowed but discouraged

    print(f"The value of PI is {PI}")

def variable_scoping():
    """Demonstrates variable scoping in Python."""
    # Global variable
    global_var = "I'm global"

    def outer_function():
        # Enclosing function's variable
        outer_var = "I'm from the outer function"

        def inner_function():
            # Local variable
            local_var = "I'm local to inner_function"
            print(local_var)
            print(outer_var)  # Can access outer_var
            print(global_var)  # Can access global_var

        inner_function()
        print(outer_var)
        # print(local_var)  # This would raise a NameError

    outer_function()
    print(global_var)
    # print(outer_var)  # This would raise a NameError

def advanced_variable_concepts():
    """Demonstrates more advanced concepts related to variables."""
    # Reference vs Value
    a = [1, 2, 3]
    b = a  # b references the same list as a
    b.append(4)
    print(f"a: {a}, b: {b}")  # Both a and b are [1, 2, 3, 4]

    # Variable unpacking
    first, *rest, last = [1, 2, 3, 4, 5]
    print(f"First: {first}, Rest: {rest}, Last: {last}")

    # Using variables as functions
    def greet(name):
        return f"Hello, {name}!"

    say_hello = greet
    print(say_hello("World"))

    # Type annotations (available since Python 3.5)
    def add_numbers(a: int, b: int) -> int:
        return a + b

    result: int = add_numbers(5, 7)
    print(f"Result of addition: {result}")

def asynchronous_variables():
    """Demonstrates variable usage in asynchronous context."""
    import asyncio

    async def fetch_data(delay: float) -> str:
        await asyncio.sleep(delay)
        return f"Data fetched after {delay} seconds"

    async def main():
        task1 = asyncio.create_task(fetch_data(1.0))
        task2 = asyncio.create_task(fetch_data(2.0))

        result1 = await task1
        result2 = await task2

        print(result1)
        print(result2)

    asyncio.run(main())

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def best_practices():
    """Demonstrates best practices for using variables and constants."""
    # Use descriptive names
    user_age = 25  # Good
    ua = 25  # Avoid abbreviations unless widely understood

    # Use constants for values that shouldn't change
    MAX_ATTEMPTS = 3
    DEFAULT_TIMEOUT = 30

    # Type hinting for better code readability and tool support
    def calculate_area(length: float, width: float) -> float:
        return length * width

    # Use context managers for resource management
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')

def common_pitfalls():
    """Demonstrates common pitfalls when working with variables."""
    # Mutable default arguments
    def add_item(item, items=[]):  # Dangerous!
        items.append(item)
        return items

    print(add_item(1))  # [1]
    print(add_item(2))  # [1, 2] - Unexpected!

    # Correct way
    def add_item_safe(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items

    # Variable shadowing
    x = 10
    def func():
        x = 20  # Creates a new local variable, doesn't modify the global x
        print(f"Local x: {x}")

    func()
    print(f"Global x: {x}")

def advanced_tips():
    """Provides advanced tips for working with variables."""
    # Using `__slots__` for memory efficiency
    class Point:
        __slots__ = ['x', 'y']
        def __init__(self, x, y):
            self.x = x
            self.y = y

    # Weak references for cache-like structures
    import weakref
    class Cache:
        def __init__(self):
            self._cache = weakref.WeakValueDictionary()

    # Using descriptors for managed attributes
    class Positive:
        def __set_name__(self, owner, name):
            self._name = name

        def __get__(self, obj, type=None):
            return getattr(obj, f"_{self._name}")

        def __set__(self, obj, value):
            if value <= 0:
                raise ValueError(f"{self._name} must be positive")
            setattr(obj, f"_{self._name}", value)

    class Product:
        price = Positive()
        quantity = Positive()

        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

# 4. Integration and Real-World Applications

def real_world_example():
    """Demonstrates a real-world application using variables and constants."""
    import random
    from datetime import datetime, timedelta

    # Constants
    MIN_TEMPERATURE = -20
    MAX_TEMPERATURE = 40
    SIMULATION_DAYS = 7

    class WeatherStation:
        def __init__(self, location):
            self.location = location
            self.temperatures = []

        def record_temperature(self, temp):
            self.temperatures.append(temp)

        def average_temperature(self):
            return sum(self.temperatures) / len(self.temperatures)

    def simulate_weather(station):
        start_date = datetime.now()
        for day in range(SIMULATION_DAYS):
            date = start_date + timedelta(days=day)
            temp = random.uniform(MIN_TEMPERATURE, MAX_TEMPERATURE)
            station.record_temperature(temp)
            print(f"{date.date()}: {temp:.2f}°C")

        print(f"Average temperature: {station.average_temperature():.2f}°C")

    # Usage
    berlin_station = WeatherStation("Berlin")
    simulate_weather(berlin_station)

# 5. Advanced Concepts and Emerging Trends

def advanced_concepts():
    """Explores advanced concepts and emerging trends in Python variables."""
    # Type hinting with generics (Python 3.9+)
    from typing import TypeVar, Generic

    T = TypeVar('T')

    class Box(Generic[T]):
        def __init__(self, content: T):
            self.content = content

    int_box = Box[int](5)
    str_box = Box[str]("Hello")

    # Pattern matching (Python 3.10+)
    def describe_type(obj):
        match obj:
            case int():
                return "It's an integer"
            case str():
                return "It's a string"
            case list():
                return "It's a list"
            case _:
                return "It's something else"

    print(describe_type(42))
    print(describe_type("Hello"))

    # Structural Pattern Matching (Python 3.10+)
    def http_error(status):
        match status:
            case 400:
                return "Bad request"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case _:
                return "Something's wrong with the internet"

    print(http_error(418))

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to variables and constants."""
    # Q: How do I create a true constant in Python?
    # A: Python doesn't have built-in support for true constants. Use UPPERCASE naming convention.

    # Q: What's the difference between '==' and 'is'?
    # A: '==' compares values, 'is' compares identities (memory addresses).
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a == b: {a == b}")  # True
    print(f"a is b: {a is b}")  # False
    print(f"a is c: {a is c}")  # True

    # Q: How do I handle circular imports when using variables?
    # A: Use import statements inside functions or methods to avoid circular imports.

    # Debugging tip: Use the `id()` function to check if two variables refer to the same object
    x = [1, 2, 3]
    y = x
    print(f"id(x): {id(x)}, id(y): {id(y)}")

# 7. Recommended Tools, Libraries, and Resources

"""
Recommended tools and libraries for working with variables and constants:

1. mypy: Static type checker for Python
   pip install mypy

2. pylint: Code analysis tool for detecting errors and enforcing coding standards
   pip install pylint

3. black: Code formatter to ensure consistent style
   pip install black

4. dataclasses: Built-in module for creating classes with automatically added special methods
   from dataclasses import dataclass

5. typing: Built-in module for support with type hints
   from typing import List, Dict, Optional

Resources for further learning:
- Official Python Documentation: https://docs.python.org/3/
- "Fluent Python" by Luciano Ramalho
- "Effective Python" by Brett Slatkin
- Real Python website: https://realpython.com/
"""

# 8. Performance Analysis and Optimization

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques."""
    import timeit
    import sys

    def memory_usage(obj):
        return sys.getsizeof(obj)

    # Comparing list comprehension vs loop
    def list_comp():
        return [i**2 for i in range(1000)]

    def loop():
        result = []
        for i in range(1000):
            result.append(i**2)
        return result

    print("Time for list comprehension:", timeit.timeit(list_comp, number=1000))
    print("Time for loop:", timeit.timeit(loop, number=1000))

    # Memory usage of different data types
    int_var = 42
    float_var = 3.14
    string_var = "Hello, World!"
    list_var = [1, 2, 3, 4, 5]

    print(f"Memory usage of int: {memory_usage(int_var)} bytes")
    print(f"Memory usage of float: {memory_usage(float_var)} bytes")
    print(f"Memory usage of string: {memory_usage(string_var)} bytes")
    print(f"Memory usage of list: {memory_usage(list_var)} bytes")

def main():
    """Main function to demonstrate various concepts."""
    print("1. Variable Basics:")
    variable_basics()

    print("\n2. Constant Convention:")
    constant_convention()

    print("\n3. Variable Scoping:")
    variable_scoping()

    print("\n4. Advanced Variable Concepts:")
    advanced_variable_concepts()

    print("\n5. Asynchronous Variables:")
    import asyncio
    asyncio.run(asynchronous_variables())

    print("\n6. Best Practices:")
    best_practices()

    print("\n7. Common Pitfalls:")
    common_pitfalls()

    print("\n8. Advanced Tips:")
    advanced_tips()

    print("\n9. Real-World Example:")
    real_world_example()

    print("\n10. Advanced Concepts:")
    advanced_concepts()

    print("\n11. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()

    print("\n12. Performance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()

# To contribute to this cheat sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes, ensuring they follow the existing style and structure.
# 3. Add your name to the list of contributors at the end of the file.
# 4. Submit a pull request with a clear description of your changes.

# Contributors:
# - Sabbir Hossain

# End of cheat sheet