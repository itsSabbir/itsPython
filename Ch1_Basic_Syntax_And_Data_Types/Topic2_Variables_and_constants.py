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

Author: Sabbir
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import time
from typing import Any, Dict, List, Union
from dataclasses import dataclass
from enum import Enum, auto

# ========================================
# Imports
# ---------------------------------
import sys  # Provides system-specific parameters and functions (e.g., sys.exit(), sys.argv)
import time  # Offers various time-related functions (e.g., time.sleep(), time.time())
from typing import Any, Dict, List, Union  # Typing utilities used for type hints to improve code readability and maintainability
from dataclasses import dataclass  # Provides a decorator and functions for creating immutable/flexible data structures
from enum import Enum, auto  # Enables the creation of enumerations, offering a way to define symbolic names for unique values

# ========================================
# 1. Overview and Historical Context
# ---------------------------------
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
- Python lacks true constants, unlike languages like C++ or Java, which have the 'const' keyword.
- Python's use of uppercase names for constants is a convention, not enforced by the language.
"""

# ========================================
# 2. Syntax, Key Concepts, and Code Examples
# ---------------------------------
def variable_basics():
    """Demonstrates basic variable usage in Python."""

    # Variable assignment
    x = 5  # Integer assignment; integers in Python have arbitrary precision
    y = 3.14  # Float assignment; Python uses double-precision (64-bit) floats internally
    name = "Alice"  # String assignment; strings are immutable sequences of Unicode characters
    is_python_fun = True  # Boolean assignment; True and False are capitalized in Python

    # Advanced Insight: Python integers (`int`) are objects and can grow as large as the available memory allows.
    # This differs from languages with fixed-width integer types (e.g., C's 32-bit or 64-bit `int`).

    # Multiple assignment - A concise way to assign multiple variables at once
    a, b, c = 1, 2, 3

    # Best Practice: Ensure the number of variables matches the number of values in multiple assignment
    # to avoid `ValueError`. For example: `x, y, z = 1, 2` will raise an error due to mismatch.

    # Type inference and dynamic typing
    var = 10  # Python infers the type of `var` as an integer
    print(f"var is initially an integer: {var}")
    var = "Now I'm a string"  # Reassigning `var` to a string demonstrates Python's dynamic typing
    print(f"var is now a string: {var}")

    # Advanced Tip: Dynamic typing allows flexibility but can introduce subtle bugs if not managed properly.
    # Consider using type hints (`var: int = 10`) and static analysis tools (e.g., `mypy`) to catch type-related issues early.

    # Variable naming conventions
    snake_case_variable = "This is the preferred naming style for variables in Python"  # Standard variable naming
    UPPERCASE_CONSTANT = "This naming style is used for constants by convention"  # Conventionally used for constants

    # Best Practice: Stick to `snake_case` for variable names and `UPPERCASE_WITH_UNDERSCORES` for constants
    # to maintain consistency and readability in your codebase.

    # Using variables in expressions
    result = x + y  # Arithmetic operation combining `int` and `float`
    print(f"Result of {x} + {y} is {result}")

    # Advanced Tip: Python will implicitly convert `x` to a float in the expression `x + y` (implicit type conversion).
    # This is known as "type coercion" and can sometimes lead to unexpected behavior, especially with `int` to `float` or `float` to `str` conversions.
    # It's good practice to be explicit with conversions using `int()`, `float()`, `str()`, etc., when precision is critical.

    # Example Pitfall: Modifying immutable data structures like strings through reassignment may lead to inefficient memory usage.
    # For instance, concatenating strings repeatedly can be inefficient due to the creation of new string objects.
    # Instead, use `str.join()` for efficient string concatenation.

# ========================================
# Advanced Considerations
# ---------------------------------
# 1. Constants in Python:
#    Although Python lacks true constants, using `UPPERCASE_WITH_UNDERSCORES` is a widely recognized convention.
#    To enforce immutability, consider using `@dataclass(frozen=True)` or `Enum` for more complex constant structures.

@dataclass(frozen=True)
class PhysicalConstants:
    """An example of using @dataclass to create immutable constants."""
    SPEED_OF_LIGHT: float = 299792458  # Speed of light in m/s
    PLANCK_CONSTANT: float = 6.62607015e-34  # Planck constant in J·s

# Usage:
constants = PhysicalConstants()
# constants.SPEED_OF_LIGHT = 300000000  # This will raise an error due to `frozen=True`

# 2. Enumerations for Named Constants:
class Status(Enum):
    """Defines possible status values using Enum, providing named constants."""
    SUCCESS = auto()
    FAILURE = auto()
    PENDING = auto()

# Usage:
current_status = Status.SUCCESS

# ========================================
# Explanation and Insights
# ---------------------------------
# 1. Using `@dataclass(frozen=True)` creates immutable objects, making it suitable for defining constants
#    or configurations that shouldn't be altered during runtime.
# 2. Enumerations (`Enum`) are a powerful way to define sets of named values, providing both clarity and
#    immutability, unlike basic constants.
# 3. Using `auto()` for `Enum` members automatically assigns unique integer values, simplifying enumeration management.

# ========================================
# Summary
# ---------------------------------
# - Python's dynamic typing offers flexibility but requires careful handling to avoid bugs.
# - Follow established naming conventions (`snake_case`, `UPPERCASE`) for maintainability.
# - Utilize advanced techniques such as `@dataclass(frozen=True)` and `Enum` for constant management, offering structure and immutability.


# ========================================
# Constants, Variable Scoping, Advanced Concepts, and Asynchronous Variables
# ========================================

def constant_convention():
    """Demonstrates the convention for constants in Python."""
    
    # Constants are typically defined in ALL_UPPERCASE to indicate immutability and signify that these values should not change.
    # However, Python does not enforce immutability, so these are "soft" constants by convention only.
    PI = 3.14159  # Common mathematical constant (π)
    MAX_USERS = 1000  # Maximum number of users allowed (example use case)
    DEFAULT_TIMEOUT = 30  # Default timeout value in seconds

    # Note: These are not true constants and can be modified
    PI = 3.14  # This is allowed but strongly discouraged in practice as it defeats the purpose of using a constant

    # Best Practice: Use constants to represent values that are truly meant to remain unchanged throughout the program.
    # Consider using namedtuples, enums, or frozen dataclasses if immutability is crucial.

    print(f"The value of PI is {PI}")  # Output will be 3.14, demonstrating that reassignment is possible

# ========================================
def variable_scoping():
    """Demonstrates variable scoping in Python."""

    # Global variable (accessible throughout the module)
    global_var = "I'm global"

    def outer_function():
        # Variable in the enclosing scope of `inner_function`
        outer_var = "I'm from the outer function"

        def inner_function():
            # Local variable within `inner_function`
            local_var = "I'm local to inner_function"
            print(local_var)  # Outputs: I'm local to inner_function
            print(outer_var)  # Can access enclosing variable: I'm from the outer function
            print(global_var)  # Can access global variable: I'm global

        inner_function()
        print(outer_var)  # Outputs: I'm from the outer function
        # print(local_var)  # Would raise a NameError because local_var is not accessible here

    outer_function()
    print(global_var)  # Outputs: I'm global
    # print(outer_var)  # Would raise a NameError because outer_var is not accessible in this scope

# Advanced Tips:
# - Use `global` variables sparingly, as they can lead to code that is hard to debug and maintain.
# - Understand Python's LEGB (Local, Enclosing, Global, Built-in) scope resolution to avoid unintended variable shadowing.
# ========================================

def advanced_variable_concepts():
    """Demonstrates more advanced concepts related to variables."""


    # Reference vs Value Example
    a = [1, 2, 3]  # `a` is a reference to a list object
    b = a  # `b` now references the same list as `a`, not a copy
    b.append(4)  # Modifying `b` also affects `a`
    print(f"a: {a}, b: {b}")  # Outputs: a: [1, 2, 3, 4], b: [1, 2, 3, 4]

    # Best Practice: Use `copy` or `deepcopy` from the `copy` module when you need to create independent copies of mutable objects.
    # Advanced Tip: Understand mutable vs immutable types and how they affect memory management and performance.

    # Variable unpacking: Powerful feature for destructuring data
    first, *rest, last = [1, 2, 3, 4, 5]
    print(f"First: {first}, Rest: {rest}, Last: {last}")  # Outputs: First: 1, Rest: [2, 3, 4], Last: 5

    # Using variables as functions
    def greet(name):
        return f"Hello, {name}!"

    say_hello = greet  # `say_hello` is now an alias for `greet`
    print(say_hello("World"))  # Outputs: Hello, World!

    # Advanced Tip: Functions are first-class citizens in Python, meaning they can be passed around, stored in variables, and used as arguments or return values.

    # Type annotations (available since Python 3.5) - Improves code readability and is useful for static type checking
    def add_numbers(a: int, b: int) -> int:
        return a + b

    result: int = add_numbers(5, 7)  # Explicit type annotation (optional but informative)
    print(f"Result of addition: {result}")  # Outputs: Result of addition: 12

# ========================================
def asynchronous_variables():
    """Demonstrates variable usage in an asynchronous context."""
    import asyncio  # `asyncio` module allows for asynchronous programming; great for I/O-bound tasks

    async def fetch_data(delay: float) -> str:
        # `await asyncio.sleep(delay)` suspends execution here without blocking other tasks
        await asyncio.sleep(delay)
        return f"Data fetched after {delay} seconds"

    async def main():
        # `asyncio.create_task` schedules coroutines concurrently
        task1 = asyncio.create_task(fetch_data(1.0))
        task2 = asyncio.create_task(fetch_data(2.0))

        # `await` ensures we wait for the tasks to complete and capture their results
        result1 = await task1
        result2 = await task2

        print(result1)  # Outputs: Data fetched after 1.0 seconds
        print(result2)  # Outputs: Data fetched after 2.0 seconds

    # Run the asynchronous event loop
    asyncio.run(main())

# Advanced Tips:
# - Always use `await` for asynchronous calls; otherwise, you might inadvertently block the execution flow.
# - Be cautious of potential race conditions in shared state when working with asynchronous code.
# - Use `asyncio.gather()` when you need to run multiple coroutines concurrently and wait for all of them to complete.


# ========================================
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# ---------------------------------

def best_practices():
    """Demonstrates best practices for using variables and constants."""

    # Use descriptive names for variables to enhance code readability and maintainability.
    user_age = 25  # Good: Clearly indicates the purpose of the variable.
    ua = 25  # Avoid: Ambiguous and unclear; hard to understand without context.

    # Use constants (ALL_CAPS naming convention) for values that shouldn't change.
    MAX_ATTEMPTS = 3  # This constant implies a limit on the number of allowed attempts.
    DEFAULT_TIMEOUT = 30  # Represents a default timeout period, indicating its purpose.

    # Type hinting improves code readability and enables better tool support (e.g., IDEs, static analyzers).
    # It helps both the developer and others reading the code to understand the expected data types.
    def calculate_area(length: float, width: float) -> float:
        return length * width  # Explicit return type ensures clarity of function output.

    # Always use context managers (the `with` statement) for resource management, such as file handling.
    # This ensures resources are properly released even if an error occurs, avoiding resource leaks.
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')  # 'file' is automatically closed when the block exits.

# ========================================
# Explanation and Insights
# ---------------------------------
# 1. Descriptive variable names enhance the maintainability of code, especially in large projects.
# 2. Constants prevent accidental modification of critical values and indicate which variables are intended to remain unchanged.
# 3. Context managers are a Pythonic way to manage resources (e.g., files, network connections) and prevent resource leaks.
# ========================================

def common_pitfalls():
    """Demonstrates common pitfalls when working with variables."""

    # Pitfall 1: Using mutable default arguments
    def add_item(item, items=[]):  # Dangerous! Avoid using mutable default arguments.
        items.append(item)
        return items

    # When you call the function multiple times, the list `items` persists across calls:
    print(add_item(1))  # Output: [1]
    print(add_item(2))  # Output: [1, 2] - Unexpected! The same list is reused.

    # Correct way: Use `None` as the default value and create a new list inside the function.
    def add_item_safe(item, items=None):
        if items is None:  # Only creates a new list if `items` was not provided.
            items = []
        items.append(item)
        return items

    # Pitfall 2: Variable shadowing
    x = 10  # This is a global variable.

    def func():
        x = 20  # This creates a new local variable `x`, shadowing the global `x`.
        print(f"Local x: {x}")  # Output: Local x: 20

    func()
    print(f"Global x: {x}")  # Output: Global x: 10, because the global `x` was never modified.

# ========================================
# Explanation and Insights
# ---------------------------------
# 1. Mutable default arguments can lead to unintended side effects because they persist across function calls.
#    Always use `None` as the default value for mutable arguments and initialize them within the function.
# 2. Variable shadowing occurs when a variable in a local scope has the same name as one in an outer scope,
#    potentially leading to confusion and bugs. Be cautious about reusing variable names.
# ========================================

def advanced_tips():
    """Provides advanced tips for working with variables."""

    # Using `__slots__` for memory efficiency
    class Point:
        __slots__ = ['x', 'y']  # Restricts the attributes that instances of Point can have, reducing memory usage.
        def __init__(self, x, y):
            self.x = x
            self.y = y

    # Explanation: `__slots__` avoids the overhead of a dynamic dictionary (`__dict__`) for storing attributes,
    # making it memory-efficient. It's beneficial when you have many instances of a class with a fixed set of attributes.
    # However, using `__slots__` limits flexibility (e.g., you cannot add new attributes dynamically).

    # Advanced Tip: Use weak references for cache-like structures
    import weakref
    class Cache:
        def __init__(self):
            self._cache = weakref.WeakValueDictionary()  # Stores objects weakly, allowing them to be garbage-collected.

    # Explanation: `weakref.WeakValueDictionary` holds references to objects without preventing their garbage collection.
    # This is useful for caches where you want objects to be automatically removed when no longer in use.

    # Using descriptors for managed attributes
    class Positive:
        def __set_name__(self, owner, name):
            self._name = name  # Store the attribute name

        def __get__(self, obj, type=None):
            return getattr(obj, f"_{self._name}")

        def __set__(self, obj, value):
            if value <= 0:
                raise ValueError(f"{self._name} must be positive")
            setattr(obj, f"_{self._name}", value)

    class Product:
        price = Positive()  # Uses the `Positive` descriptor for managed access to 'price'
        quantity = Positive()  # Uses the `Positive` descriptor for managed access to 'quantity'

        def __init__(self, name, price, quantity):
            self.name = name  # Direct attribute assignment
            self.price = price  # Triggers the `Positive` descriptor logic
            self.quantity = quantity  # Triggers the `Positive` descriptor logic

    # Explanation: Descriptors provide fine-grained control over attribute access, making them powerful for validation,
    # computed properties, or lazy loading. They allow you to define how attributes are accessed and modified.

# ========================================
# Best Practices and Insights
# ---------------------------------
# 1. `__slots__` is useful for optimizing memory usage in classes where attribute names are fixed. 
#    However, use it sparingly, as it limits the ability to add attributes dynamically or use multiple inheritance.
# 2. Weak references (`weakref`) are ideal for building caches, preventing memory leaks by allowing objects to be 
#    garbage-collected when no longer in use.
# 3. Descriptors offer a high degree of control over attribute access and modification, making them essential for
#    scenarios requiring validation, data encapsulation, or complex attribute management.
# ========================================

# ========================================
# 4. Integration and Real-World Applications
# ---------------------------------
def real_world_example():
    """Demonstrates a real-world application using variables and constants, simulating temperature recordings."""
    import random  # Required for generating random temperature values
    from datetime import datetime, timedelta  # Provides date manipulation capabilities

    # Constants: Defining realistic temperature ranges and simulation parameters
    MIN_TEMPERATURE = -20  # Minimum temperature in Celsius (example: cold winter)
    MAX_TEMPERATURE = 40   # Maximum temperature in Celsius (example: hot summer)
    SIMULATION_DAYS = 7    # Number of days to simulate weather data for

    class WeatherStation:
        """
        Represents a weather station that records temperatures for a specific location.
        
        Attributes:
            location (str): Name of the location where the station is based.
            temperatures (list): List of recorded temperature values.
        """
        def __init__(self, location: str):
            self.location = location  # Store the location name
            self.temperatures = []  # Initialize an empty list for temperature recordings

        def record_temperature(self, temp: float):
            """Records a temperature value for the current day."""
            self.temperatures.append(temp)  # Add the temperature to the list

        def average_temperature(self) -> float:
            """
            Calculates the average temperature recorded by the station.
            
            Returns:
                float: The average temperature.
                
            Pitfall: Ensure `self.temperatures` is not empty before calling this method to avoid a ZeroDivisionError.
            """
            return sum(self.temperatures) / len(self.temperatures)  # Compute the average

    def simulate_weather(station: WeatherStation):
        """Simulates weather data for a given WeatherStation over a defined period."""
        start_date = datetime.now()  # Capture the current date as the simulation start date
        
        # Loop through the number of simulation days
        for day in range(SIMULATION_DAYS):
            date = start_date + timedelta(days=day)  # Calculate the date for each simulation day
            temp = random.uniform(MIN_TEMPERATURE, MAX_TEMPERATURE)  # Generate a random temperature
            station.record_temperature(temp)  # Record the generated temperature
            print(f"{date.date()}: {temp:.2f}°C")  # Display the recorded temperature with two decimal precision

        # Display the average temperature for the period
        print(f"Average temperature: {station.average_temperature():.2f}°C")

    # Usage Example: Simulating weather data for a station in Berlin
    berlin_station = WeatherStation("Berlin")
    simulate_weather(berlin_station)

# ========================================
# Insights:
# 1. The use of constants (`MIN_TEMPERATURE`, `MAX_TEMPERATURE`, `SIMULATION_DAYS`) promotes maintainability 
#    and clarity, making it easy to adjust parameters.
# 2. Employing object-oriented principles (`WeatherStation` class) makes the code modular, reusable, 
#    and easy to extend for different locations or data types.
# 3. Potential Pitfall: `average_temperature()` assumes at least one temperature entry; ensure `record_temperature()` 
#    is called before attempting to access it.
# ========================================

# ========================================
# 5. Advanced Concepts and Emerging Trends
# ---------------------------------
def advanced_concepts():
    """Explores advanced concepts and emerging trends in Python variables and type handling."""
    
    # Type hinting with generics (Python 3.9+)
    from typing import TypeVar, Generic

    T = TypeVar('T')  # Type variable to support generic class definitions

    class Box(Generic[T]):
        """
        A generic container that can hold any type of content.
        
        Attributes:
            content (T): The content stored within the box.
        """
        def __init__(self, content: T):
            self.content = content  # Store the content with the specified type

    # Instantiate Box objects with different types
    int_box = Box   # A box holding an integer
    str_box = Box[str]("Hello")  # A box holding a string

    # Advanced Insight: Generics enhance code flexibility and maintainability by allowing type-safe 
    # reuse of classes/functions, akin to C++ templates or Java generics.

    # Pattern matching (Python 3.10+)
    def describe_type(obj: Any) -> str:
        """
        Describes the type of the given object using pattern matching.
        
        Returns:
            str: A message describing the object's type.
        """
        match obj:
            case int():
                return "It's an integer"
            case str():
                return "It's a string"
            case list():
                return "It's a list"
            case _:
                return "It's something else"

    print(describe_type(42))  # Outputs: "It's an integer"
    print(describe_type("Hello"))  # Outputs: "It's a string"

    # Structural Pattern Matching (Python 3.10+)
    def http_error(status: int) -> str:
        """
        Provides a description for HTTP status codes using structural pattern matching.
        
        Returns:
            str: A human-readable error description based on the status code.
        """
        match status:
            case 400:
                return "Bad request"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case _:
                return "Something's wrong with the internet"

    print(http_error(418))  # Outputs: "I'm a teapot"

# ========================================
# Advanced Insights:
# 1. `TypeVar` and `Generic` facilitate strong type-checking, enhancing code robustness and maintainability.
# 2. Pattern matching (`match-case`) is a powerful feature inspired by languages like Scala and Rust, 
#    enabling more expressive and readable conditional logic.
# 3. A common pitfall with `match-case` is overlooking exhaustive checking; ensure all potential cases are handled 
#    to avoid unintended behavior, especially for complex structures.
# 4. The `_` wildcard in `match` serves as a catch-all for unmatched cases, ensuring the code doesn't break on unexpected input.
# ========================================


# ========================================
# 6. FAQs and Troubleshooting
# ---------------------------------
def faqs_and_troubleshooting():
    """Addresses common questions and issues related to variables and constants."""

    # Q: How do I create a true constant in Python?
    # A: Python doesn't have built-in support for true constants. 
    #    The conventional approach is to use UPPERCASE variable names (e.g., `PI = 3.14`) 
    #    to indicate that they should not be modified, though this relies on developer discipline.

    # Q: What's the difference between '==' and 'is'?
    # A: '==' compares the values or data equality of two objects, while 'is' checks if both objects
    #    point to the same memory address (identity comparison). This distinction is critical in cases
    #    involving mutable objects like lists or dictionaries.

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    # 'a' and 'b' have the same contents but reside at different memory addresses.
    print(f"a == b: {a == b}")  # True, since the values are equal
    print(f"a is b: {a is b}")  # False, because they are distinct objects in memory
    print(f"a is c: {a is c}")  # True, 'c' is just another reference to 'a'

    # Q: How do I handle circular imports when using variables?
    # A: Circular imports occur when two modules attempt to import each other, causing an import loop.
    #    To prevent this, consider importing within functions/methods or refactoring code to break 
    #    the circular dependency. Alternatively, use "import module" instead of "from module import ..."

    # Debugging tip: Use the `id()` function to inspect object identities.
    # Advanced Insight: `id()` is especially useful when debugging mutable vs immutable objects.
    x = [1, 2, 3]
    y = x  # y points to the same list as x
    print(f"id(x): {id(x)}, id(y): {id(y)}")  # Both will have the same id, indicating shared memory reference

# ========================================
# 7. Recommended Tools, Libraries, and Resources
# ---------------------------------

"""
Recommended tools and libraries for working with variables and constants:

1. mypy: Static type checker for Python
   pip install mypy
   # mypy helps catch type-related errors during development, which is crucial in large codebases where dynamic typing might lead to subtle bugs.

2. pylint: Code analysis tool for detecting errors and enforcing coding standards
   pip install pylint
   # Pylint ensures your code adheres to PEP 8 (Python's style guide) and helps identify potential issues, leading to cleaner, more maintainable code.

3. black: Code formatter to ensure consistent style
   pip install black
   # Black is an uncompromising code formatter that ensures consistency across your codebase. By automatically formatting your code, it reduces the time spent on style debates.

4. dataclasses: Built-in module for creating classes with automatically added special methods
   from dataclasses import dataclass
   # Introduced in Python 3.7, `dataclasses` simplify the creation of classes by auto-generating `__init__`, `__repr__`, `__eq__`, etc. This reduces boilerplate and enhances code readability.

5. typing: Built-in module for support with type hints
   from typing import List, Dict, Optional
   # The `typing` module is essential for adding type annotations, which improves code clarity and enables better static analysis when used with tools like mypy.

Resources for further learning:
- Official Python Documentation: https://docs.python.org/3/
- "Fluent Python" by Luciano Ramalho
- "Effective Python" by Brett Slatkin
- Real Python website: https://realpython.com/
"""

# ========================================
# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques."""
    import timeit  # Measures execution time of small code snippets
    import sys  # Provides access to system-specific parameters and functions

    def memory_usage(obj):
        """Returns the memory usage of an object in bytes."""
        return sys.getsizeof(obj)  # Uses getsizeof to measure memory footprint; works well for built-in types

    # Comparing list comprehension vs. loop
    def list_comp():
        # Efficiently creates a list of squares using list comprehension
        return [i**2 for i in range(1000)]

    def loop():
        # Uses a traditional loop to create a list of squares
        result = []
        for i in range(1000):
            result.append(i**2)
        return result

    # Performance measurement of list comprehension vs. loop
    print("Time for list comprehension:", timeit.timeit(list_comp, number=1000))
    print("Time for loop:", timeit.timeit(loop, number=1000))

    # Memory usage of different data types
    int_var = 42  # Integer example; memory-efficient as Python handles small integers optimally
    float_var = 3.14  # Float example; typically takes up more memory than integers
    string_var = "Hello, World!"  # String example; note that strings are immutable in Python
    list_var = [1, 2, 3, 4, 5]  # List example; lists are dynamic but have more memory overhead than arrays

    print(f"Memory usage of int: {memory_usage(int_var)} bytes")
    print(f"Memory usage of float: {memory_usage(float_var)} bytes")
    print(f"Memory usage of string: {memory_usage(string_var)} bytes")
    print(f"Memory usage of list: {memory_usage(list_var)} bytes")

# ========================================
# Advanced Tips:
# - List comprehensions are generally faster than traditional loops for simple operations because they're implemented as C loops in Python.
# - However, avoid using list comprehensions for complex logic; it reduces readability and could introduce bugs.
# - Use `sys.getsizeof` with caution for nested objects, as it doesn't account for memory taken up by objects referenced within the container.
# - Consider using `memory_profiler` for more comprehensive memory analysis, especially for larger and more complex data structures.
# ========================================

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
    asyncio.run(asynchronous_variables())  # Using `asyncio.run()` is the recommended way to execute coroutines since Python 3.7.

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
    # The use of `if __name__ == "__main__":` is a best practice for code modularity. 
    # It ensures that the `main()` function only runs when this script is executed directly, 
    # not when imported as a module.

# ========================================
# Contribution Guidelines:
# ----------------------------------------
"""
9. How to Contribute
--------------------
To contribute to this note sheet:
1. Fork the repository containing this file.
2. Make your changes or additions.
3. Ensure all code examples are correct and follow the established style.
4. Add comments explaining new concepts or functions.
5. Update the Table of Contents if necessary.
6. Submit a pull request with a clear description of your changes.

Guidelines for contributions:
- Maintain the current format and style.
- Provide working code examples for new concepts.
- Include performance considerations for new functions.
- Add relevant references or citations for advanced topics.

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of the 're' module and regular expressions in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

"""

# Contributors:
# - Sabbir Hossain
# ========================================

# End of cheat sheet
# ========================================
