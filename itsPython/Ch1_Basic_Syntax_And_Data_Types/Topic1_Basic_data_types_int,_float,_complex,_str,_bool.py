"""
Expert-Level Cheat Sheet: Basic Syntax and Data Types - Basic data types (int, float, complex, str, bool) - in the Python Programming Language

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization
"""

# 1. Overview and Historical Context
# ---------------------------------
"""
Python's basic data types form the foundation of its type system. These types include integers (`int`), floating-point numbers (`float`), complex numbers (`complex`), strings (`str`), and booleans (`bool`). Understanding these types is crucial for effective Python programming.

**Brief history:**
- Python was created by Guido van Rossum and first released in 1991.
- Python 2.x introduced `bool` as a built-in type in version 2.3 (2003).
- Python 3.x (2008) made significant changes, including making all strings Unicode by default.

**Relevance in modern software development:**
Python's basic data types provide a solid foundation for data manipulation, scientific computing, web development, and more. Compared to other languages:
- Python's dynamic typing offers flexibility but requires careful type checking.
- Python's `int` has arbitrary precision, unlike fixed-size integers in languages like C or Java.
- Python's `complex` type is built-in, while many languages require separate libraries for complex numbers.
"""

# Imports
import sys
import time
import cmath
import decimal
from typing import Union, Any
import logging
from collections import Counter
import timeit
import array  # Standard library module; no installation required

# Attempt to import NumPy
try:
    import numpy as np
    numpy_available = True
except ImportError:
    numpy_available = False

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to demonstrate basic data types in Python.
    """
    integer_examples()
    float_examples()
    complex_examples()
    string_examples()
    boolean_examples()
    type_conversion_examples()
    advanced_usage_examples()
    best_practices_and_pitfalls()
    real_world_applications()
    advanced_concepts_and_trends()
    faqs_and_troubleshooting()
    recommended_resources()
    performance_analysis_and_optimization()
    memory_management_and_resource_optimization()
    handling_edge_cases_in_complex_systems()

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def integer_examples():
    """
    Demonstrates integer operations and properties.
    """
    print("Integer Examples:")
    
    # Basic arithmetic operations with integers
    a, b = 10, 3  # Assigning values to variables a and b
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division (float result): {a} / {b} = {a / b}")  # Result is a float
    print(f"Integer division: {a} // {b} = {a // b}")  # Floor division
    print(f"Modulo: {a} % {b} = {a % b}")  # Remainder of division
    print(f"Exponentiation: {a} ** {b} = {a ** b}")  # a raised to the power of b
    
    # Bitwise operations
    print(f"Bitwise AND: {a} & {b} = {a & b}")  # Binary AND operation
    print(f"Bitwise OR: {a} | {b} = {a | b}")  # Binary OR operation
    print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")  # Binary XOR operation
    print(f"Bitwise NOT: ~{a} = {~a}")  # Binary NOT operation
    print(f"Left shift: {a} << 1 = {a << 1}")  # Shift bits left by 1
    print(f"Right shift: {a} >> 1 = {a >> 1}")  # Shift bits right by 1
    
    # Arbitrary precision demonstration
    large_num = 2**100  # 2 raised to the 100th power
    print(f"Large number (2**100): {large_num}")
    print(f"Digits in large number: {len(str(large_num))}")  # Number of digits

def float_examples():
    """
    Demonstrates float operations and properties.
    """
    print("\nFloat Examples:")
    
    # Basic arithmetic operations with floats
    x, y = 3.14, 2.5  # Assigning float values to x and y
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    
    # Floating-point precision issues
    a = 0.1 + 0.2  # Expected to be 0.3
    b = 0.3
    print(f"0.1 + 0.2 == 0.3: {a == b}")  # This will be False
    print(f"Actual sum: {a}")
    print(f"Difference: {abs(a - b)}")  # Small difference due to precision
    
    # Using decimal module for precise decimal arithmetic
    d1 = decimal.Decimal('0.1')
    d2 = decimal.Decimal('0.2')
    d3 = decimal.Decimal('0.3')
    print(f"Using Decimal: {d1} + {d2} == {d3}: {d1 + d2 == d3}")  # True
    
    # Special float values
    print(f"Infinity: {float('inf')}")
    print(f"Negative Infinity: {float('-inf')}")
    print(f"Not a Number (NaN): {float('nan')}")

def complex_examples():
    """
    Demonstrates complex number operations and properties.
    """
    print("\nComplex Number Examples:")
    
    # Creating complex numbers
    z1 = 3 + 4j  # Complex number with real=3, imag=4
    z2 = complex(2, -1)  # Another complex number
    print(f"z1 = {z1}, z2 = {z2}")
    
    # Basic arithmetic operations with complex numbers
    print(f"Addition: {z1} + {z2} = {z1 + z2}")
    print(f"Subtraction: {z1} - {z2} = {z1 - z2}")
    print(f"Multiplication: {z1} * {z2} = {z1 * z2}")
    print(f"Division: {z1} / {z2} = {z1 / z2}")
    
    # Accessing attributes and methods
    print(f"Real part of z1: {z1.real}")
    print(f"Imaginary part of z1: {z1.imag}")
    print(f"Conjugate of z1: {z1.conjugate()}")
    
    # Using cmath module for complex math operations
    print(f"Magnitude (absolute value) of z1: {abs(z1)}")
    print(f"Phase (angle) of z1: {cmath.phase(z1)} radians")
    print(f"Square root of z1: {cmath.sqrt(z1)}")

def string_examples():
    """
    Demonstrates string operations and properties.
    """
    print("\nString Examples:")
    
    # String creation and basic operations
    s1 = "Hello"
    s2 = 'World'
    print(f"Concatenation: {s1} + ' ' + {s2} = {s1 + ' ' + s2}")
    print(f"Repetition: {s1} * 3 = {s1 * 3}")
    
    # String methods and manipulation
    s = "  Python Programming  "
    print(f"Original string: '{s}'")
    print(f"Uppercase: '{s.upper()}'")
    print(f"Lowercase: '{s.lower()}'")
    print(f"Stripped (remove leading/trailing whitespace): '{s.strip()}'")
    print(f"Split into list: {s.strip().split(' ')}")
    
    # String formatting techniques
    name = "Alice"
    age = 30
    print(f"Using f-string: {name} is {age} years old")
    print("Using format method: {} is {} years old".format(name, age))
    print("Using % operator: %s is %d years old" % (name, age))
    
    # String slicing
    text = "Python"
    print(f"Slicing [1:4] of '{text}': '{text[1:4]}'")  # 'yth'
    print(f"Reverse '{text}': '{text[::-1]}'")  # 'nohtyP'
    
    # Unicode support
    unicode_string = "Здравствуй, мир! 你好，世界！"
    print(f"Unicode string: {unicode_string}")

def boolean_examples():
    """
    Demonstrates boolean operations and properties.
    """
    print("\nBoolean Examples:")
    
    # Boolean values
    t, f = True, False
    print(f"True: {t}, False: {f}")
    
    # Logical operations
    print(f"AND operation: {t} and {f} = {t and f}")  # False
    print(f"OR operation: {t} or {f} = {t or f}")  # True
    print(f"NOT operation: not {t} = {not t}, not {f} = {not f}")
    
    # Comparison operations resulting in booleans
    x, y = 5, 10
    print(f"{x} < {y}: {x < y}")  # True
    print(f"{x} > {y}: {x > y}")  # False
    print(f"{x} == {y}: {x == y}")  # False
    print(f"{x} != {y}: {x != y}")  # True
    
    # Truthy and Falsy values in Python
    print(f"bool(0): {bool(0)}")  # False
    print(f"bool(1): {bool(1)}")  # True
    print(f"bool(''): {bool('')}")  # False
    print(f"bool('text'): {bool('text')}")  # True
    print(f"bool([]): {bool([])}")  # False
    print(f"bool([1, 2]): {bool([1, 2])}")  # True

def type_conversion_examples():
    """
    Demonstrates type conversion between basic data types.
    """
    print("\nType Conversion Examples:")
    
    # Integer conversions
    print(f"int('100'): {int('100')}")  # Converts string to integer
    print(f"int(3.14): {int(3.14)}")  # Truncates decimal part
    print(f"int(True): {int(True)}")  # True is converted to 1
    
    # Float conversions
    print(f"float('3.14'): {float('3.14')}")  # Converts string to float
    print(f"float(5): {float(5)}")  # Converts integer to float
    
    # Complex conversions
    print(f"complex(3, 4): {complex(3, 4)}")  # Creates complex number 3 + 4j
    print(f"complex('3+4j'): {complex('3+4j')}")  # Parses string to complex
    
    # String conversions
    print(f"str(123): '{str(123)}'")  # Converts integer to string
    print(f"str(3.14): '{str(3.14)}'")  # Converts float to string
    print(f"str(True): '{str(True)}'")  # Converts boolean to string
    
    # Boolean conversions
    print(f"bool(1): {bool(1)}")  # True
    print(f"bool(0): {bool(0)}")  # False
    print(f"bool('False'): {bool('False')}")  # Non-empty string is True

def advanced_usage_examples():
    """
    Demonstrates advanced usage of basic data types.
    """
    print("\nAdvanced Usage Examples:")
    
    # Using sys.getsizeof to check memory usage
    print(f"Size of int(0): {sys.getsizeof(0)} bytes")
    print(f"Size of int(1000000): {sys.getsizeof(1000000)} bytes")
    
    # Timing operations using time.perf_counter()
    def time_operation(op):
        start = time.perf_counter()
        result = op()
        end = time.perf_counter()
        return result, end - start
    
    # Compare integer and float multiplication performance
    int_result, int_time = time_operation(lambda: 123456789 * 987654321)
    float_result, float_time = time_operation(lambda: 123456789.0 * 987654321.0)
    print(f"Integer multiplication time: {int_time:.6f} seconds")
    print(f"Float multiplication time: {float_time:.6f} seconds")
    
    # String interning demonstration
    s1 = "python"
    s2 = "python"
    s3 = "".join(["p", "y", "t", "h", "o", "n"])
    print(f"s1 is s2: {s1 is s2}")  # Likely True due to interning
    print(f"s1 is s3: {s1 is s3}")  # Likely False; s3 is a new object
    
    # Using frozenset for immutable sets
    fs = frozenset([1, 2, 3, 4, 5])
    print(f"Frozenset (immutable set): {fs}")
    
    # Type hinting with Union and Any from typing module
    def process_data(value: Union[int, float, str]) -> Any:
        if isinstance(value, (int, float)):
            return value * 2
        elif isinstance(value, str):
            return value.upper()
        else:
            raise ValueError("Unsupported type")
    
    print(f"process_data(5): {process_data(5)}")  # Outputs 10
    print(f"process_data('hello'): {process_data('hello')}")  # Outputs 'HELLO'

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

def best_practices_and_pitfalls():
    """
    Discusses best practices and common pitfalls.
    """
    print("\nBest Practices and Common Pitfalls:")
    
    # Best Practice: Use meaningful variable names
    total_price = 100.0
    discount_rate = 0.1
    discounted_price = total_price * (1 - discount_rate)
    print(f"Discounted Price: {discounted_price}")
    
    # Common Pitfall: Floating-point precision issues
    a = 0.1 + 0.2
    print(f"0.1 + 0.2 == 0.3: {a == 0.3}")  # False due to precision error
    print(f"Actual sum: {a}")
    
    # Solution: Use decimal module for precise calculations
    from decimal import Decimal
    a = Decimal('0.1') + Decimal('0.2')
    print(f"Using Decimal: Decimal('0.1') + Decimal('0.2') == Decimal('0.3'): {a == Decimal('0.3')}")  # True
    
    # Advanced Tip: Use f-strings for efficient string formatting
    name = "Bob"
    age = 25
    print(f"{name} is {age} years old.")  # Cleaner and faster

# 4. Integration and Real-World Applications
# ------------------------------------------

def real_world_applications():
    """
    Examples of how basic data types are used in real-world scenarios.
    """
    print("\nReal-World Applications:")
    
    # Data Science with NumPy (if available)
    if numpy_available:
        arr = np.array([1, 2, 3, 4, 5], dtype=float)
        print(f"NumPy array: {arr}")
    else:
        print("NumPy is not available. Install it using 'pip install numpy' for numerical computing.")
    
    # Web Development with Flask (conceptual example)
    print("Web frameworks like Flask and Django use Python's basic types for handling requests and responses.")
    
    # Finance Calculations using Decimal for precise monetary values
    price = decimal.Decimal('19.99')
    quantity = 3
    total = price * quantity
    print(f"Total price using Decimal: {total}")
    
    # System Administration scripting example
    print("Using basic types in scripts for log parsing and system monitoring.")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def advanced_concepts_and_trends():
    """
    Discusses advanced concepts and emerging trends.
    """
    print("\nAdvanced Concepts and Emerging Trends:")
    
    # Type Hinting and Static Type Checking with mypy
    def greet(name: str) -> str:
        return f"Hello, {name}"
    
    print(greet("Alice"))
    print("Type hints improve code readability and enable static type checking with tools like mypy.")
    
    # JIT Compilation with Numba (conceptual example)
    print("Numba can be used to speed up numerical computations by compiling Python functions to machine code.")
    
    # Pattern Matching in Python 3.10+
    version_info = sys.version_info
    if version_info.major >= 3 and version_info.minor >= 10:
        print("Pattern matching is available in Python 3.10 and later.")
        # Example of pattern matching (commented out to maintain compatibility)
        # def http_error(status):
        #     match status:
        #         case 400:
        #             return "Bad request"
        #         case 404:
        #             return "Not found"
        #         case _:
        #             return "Other error"
    else:
        print("Pattern matching is not available in your Python version.")

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    """
    Provides answers to common questions and troubleshooting tips.
    """
    print("\nFAQs and Troubleshooting:")
    
    # Q: Why does 0.1 + 0.2 != 0.3?
    a = 0.1 + 0.2
    print(f"0.1 + 0.2 == 0.3: {a == 0.3}")
    print("A: This is due to floating-point precision errors in binary representation.")
    
    # Q: How to safely convert a string to an integer?
    s = "123"
    try:
        num = int(s)
        print(f"Converted '{s}' to integer: {num}")
    except ValueError:
        print(f"Cannot convert '{s}' to integer.")
    
    # Q: Difference between '==' and 'is'
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    print(f"x == y: {x == y}")  # True (values are equal)
    print(f"x is y: {x is y}")  # True (same object)
    print(f"x == z: {x == z}")  # True (values are equal)
    print(f"x is z: {x is z}")  # False (different objects)

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    """
    Recommends tools and resources for further learning.
    """
    print("\nRecommended Tools, Libraries, and Resources:")
    print("- Tools: mypy for static type checking, Black for code formatting")
    print("- Libraries: decimal for precise decimal arithmetic, math for mathematical functions")
    print("- Resources:")
    print("  - Python official documentation: https://docs.python.org/3/")
    print("  - 'Fluent Python' by Luciano Ramalho")
    print("  - 'Effective Python' by Brett Slatkin")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis_and_optimization():
    """
    Includes a section on profiling and benchmarking code related to basic data types.
    """
    print("\nPerformance Analysis and Optimization:")
    
    # Performance Comparison Example
    print("Performance Comparison:")
    
    # Setup for data generation
    setup = """
import random
data = [random.random() for _ in range(1000000)]
"""
    
    # Test 1: Standard Python list summation
    list_test = """
result = sum(data)
"""
    list_time = timeit.timeit(list_test, setup=setup, number=10)
    print(f"Python list sum time: {list_time:.6f} seconds")
    
    # Test 2: Array module summation
    array_test = """
arr = array.array('d', data)
result = sum(arr)
"""
    array_time = timeit.timeit(array_test, setup=setup + "import array", number=10)
    print(f"Array module sum time: {array_time:.6f} seconds")
    
    # Test 3: NumPy array summation (if available)
    if numpy_available:
        numpy_test = """
np_arr = np.array(data)
result = np.sum(np_arr)
"""
        numpy_time = timeit.timeit(numpy_test, setup=setup + "import numpy as np", number=10)
        print(f"NumPy array sum time: {numpy_time:.6f} seconds")
    else:
        print("NumPy is not available for performance comparison. Install it using 'pip install numpy'.")
    
    # String concatenation comparison
    print("\nString Concatenation Comparison:")
    
    setup_str = """
words = ['python'] * 10000
"""
    
    concat_test = """
result = ''
for word in words:
    result += word
"""
    concat_time = timeit.timeit(concat_test, setup=setup_str, number=100)
    print(f"String concatenation with '+=' time: {concat_time:.6f} seconds")
    
    join_test = """
result = ''.join(words)
"""
    join_time = timeit.timeit(join_test, setup=setup_str, number=100)
    print(f"String concatenation with 'join()' time: {join_time:.6f} seconds")
    print("Using ''.join() is generally faster and more memory-efficient.")

def memory_management_and_resource_optimization():
    """
    Discusses memory management and resource optimization techniques.
    """
    print("\nMemory Management and Resource Optimization:")
    
    # Using generators for large datasets
    gen_exp = (x**2 for x in range(1000000))
    print(f"Generator expression created for large dataset to save memory.")
    
    # Using __slots__ in classes to reduce memory overhead
    class Point:
        __slots__ = ['x', 'y']  # Restricts attributes to reduce memory
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    p = Point(1, 2)
    print(f"Point created with x={p.x}, y={p.y}")
    
    # Using weak references to prevent memory leaks
    print("Using weak references for memory optimization.")
    import weakref
    class MyClass:
        pass
    obj = MyClass()
    r = weakref.ref(obj)
    print(f"Weak reference created: {r}")
    print(f"Object referenced: {r()}")
    
    # Using context managers to manage resources
    class FileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
    
    # Example usage of context manager
    with FileManager('example.txt', 'w') as f:
        f.write('Hello, World!')
    print("File written using custom context manager.")

def handling_edge_cases_in_complex_systems():
    """
    Discusses handling edge cases in complex systems.
    """
    print("\nHandling Edge Cases in Complex Systems:")
    
    # Using try-except blocks for exception handling
    def safe_divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Division by zero!")
            result = None
        except TypeError:
            print("Error: Invalid types for division!")
            result = None
        return result
    
    print(f"safe_divide(10, 0): {safe_divide(10, 0)}")
    print(f"safe_divide(10, 'a'): {safe_divide(10, 'a')}")
    
    # Input validation to prevent edge cases
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        return age
    
    try:
        validate_age(200)
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Using assert statements for debugging
    def calculate_average(numbers):
        assert len(numbers) > 0, "List cannot be empty"
        return sum(numbers) / len(numbers)
    
    try:
        calculate_average([])
    except AssertionError as e:
        print(f"Assertion error: {e}")
    
    # Implementing logging for monitoring
    def perform_calculation(data):
        # Simulated calculation function
        return sum(data)
    
    def process_data(data):
        if not data:
            logger.warning("Empty data received")
            return None
        
        try:
            result = perform_calculation(data)
            logger.info(f"Processing result: {result}")
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            result = None
        
        return result
    
    print(f"Process data result: {process_data([1, 2, 3])}")
    print(f"Process data with empty list: {process_data([])}")

if __name__ == "__main__":
    main()
