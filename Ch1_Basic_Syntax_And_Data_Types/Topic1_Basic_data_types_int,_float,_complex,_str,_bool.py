"""
Expert-Level Notes Sheet: Basic Syntax and Data Types - Basic data types (int, float, complex, str, bool) - in the Python Programming Language

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

# ========================================
# 1. Overview and Historical Context
# ---------------------------------

"""
Python's basic data types form the foundation of its type system. These types include integers (`int`), 
floating-point numbers (`float`), complex numbers (`complex`), strings (`str`), and booleans (`bool`). 
Understanding these types is crucial for effective Python programming.

Brief history:
- Python was created by Guido van Rossum and first released in 1991.
- Python 2.x introduced `bool` as a built-in type in version 2.3 (2003).
- Python 3.x (2008) made significant changes, including making all strings Unicode by default.

Relevance in modern software development:
Python's basic data types provide a solid foundation for data manipulation, scientific computing, 
web development, and more. Compared to other languages:
- Python's dynamic typing offers flexibility but requires careful type checking.
- Python's `int` has arbitrary precision, unlike fixed-size integers in languages like C or Java.
- Python's `complex` type is built-in, while many languages require separate libraries for complex numbers.
"""
# ========================================

# Imports
import sys  # Provides access to system-specific parameters and functions
import time  # Offers various time-related functions (e.g., time.sleep(), time.time())
import cmath  # Used for complex number operations; complements the 'math' module for real numbers
import decimal  # Facilitates decimal floating-point arithmetic for high precision calculations
from typing import Union, Any  # Typing utilities used for type hints, enhancing code readability and maintainability
import logging  # Allows for robust logging of events for debugging and auditing
from collections import Counter  # Efficient for counting hashable objects; alternative to manual counting with dictionaries
import timeit  # Used to measure execution time of small code snippets; helpful in performance analysis
import array  # Provides space-efficient storage of basic C-style data types

# Attempt to import NumPy (commonly used in scientific computing and data manipulation)
try:
    import numpy as np  # Widely used for numerical computations; provides multi-dimensional array objects
    numpy_available = True
except ImportError:
    # If NumPy isn't available, set a flag accordingly
    numpy_available = False

# Setting up logging configuration
logging.basicConfig(level=logging.INFO)  # Configures logging to show INFO-level messages and above
logger = logging.getLogger(__name__)  # Retrieves a logger object; __name__ ensures the logger is module-specific

# ========================================
# Explanation and Insights
# ---------------------------------
# 1. The use of `try-except` for NumPy ensures graceful degradation of functionality if the library isn't available.
#    This is a good practice in production code where dependencies might not always be present.
# 2. The `logging` module is preferred over print statements for real-world applications because it offers different 
#    levels of severity (DEBUG, INFO, WARNING, ERROR, CRITICAL) and can be configured to output to various destinations.
# 3. The `array` module is often underutilized but provides efficient memory storage for homogeneous data, 
#    especially compared to Python lists, which are dynamically typed and have greater memory overhead.
# ========================================

# Advanced Tip: Consider using `decimal.Decimal` over `float` when dealing with financial calculations or other applications
# requiring exact precision. Unlike `float`, `decimal` offers greater control over precision and avoids issues like 
# floating-point rounding errors.
#
# Example Pitfall: If you use floating-point arithmetic, be cautious of precision errors:
#     >>> 0.1 + 0.2 == 0.3
#     False
# This is due to the way floats are represented in binary, a common issue in many programming languages.


def main():
    """
    Main function to demonstrate and explore Python's basic data types and their usage in various contexts.

    This function serves as an entry point to a comprehensive analysis of data types, covering fundamental 
    concepts, advanced topics, best practices, real-world applications, and performance optimization techniques.

    Each function called within `main` represents a distinct area of focus, providing an opportunity to explore 
    Python's capabilities, common pitfalls, and advanced insights that can be applied in everyday programming 
    and complex systems alike.
    """
    # Demonstrates integer-related concepts: size, precision, and operations
    integer_examples()
    
    # Covers floating-point numbers, precision challenges, and decimal comparisons
    float_examples()
    
    # Introduces complex numbers, demonstrating Python's built-in support for mathematical operations
    complex_examples()
    
    # Explores strings: immutability, slicing, formatting, and common string operations
    string_examples()
    
    # Discusses booleans, truthy/falsey values, and boolean algebra
    boolean_examples()
    
    # Explains type conversions, implicit and explicit, and potential pitfalls (e.g., precision loss)
    type_conversion_examples()
    
    # Delves into more advanced and less common usages of data types, showcasing Python's versatility
    advanced_usage_examples()
    
    # Identifies best practices in working with data types and highlights potential pitfalls to avoid
    best_practices_and_pitfalls()
    
    # Illustrates how these data types are used in real-world applications, such as data processing and analysis
    real_world_applications()
    
    # Explores advanced concepts like type annotations, custom data types, and evolving trends in Python
    advanced_concepts_and_trends()
    
    # Provides answers to frequently asked questions, common misconceptions, and troubleshooting tips
    faqs_and_troubleshooting()
    
    # Recommends tools, libraries, and resources for further learning and mastery of Python's data types
    recommended_resources()
    
    # Examines performance considerations, such as computational efficiency and memory overhead
    performance_analysis_and_optimization()
    
    # Discusses memory management techniques, such as garbage collection and efficient data handling
    memory_management_and_resource_optimization()
    
    # Tackles handling edge cases, which is crucial in designing robust and fault-tolerant systems
    handling_edge_cases_in_complex_systems()

# ========================================
# Detailed Commentary on the Main Function
# ---------------------------------
# 1. The `main()` function is designed to be modular, calling separate functions that each handle a specific aspect of Python's data types.
#    This modular design follows the Single Responsibility Principle (SRP), ensuring that each function has a well-defined purpose.
#
# 2. This approach also aligns with best practices in software engineering, promoting code readability, maintainability, and testability.
#    As the codebase evolves, adding or modifying functionality becomes more manageable, reducing the risk of unintended side effects.
#
# 3. A potential pitfall to avoid is over-complicating the `main()` function. By keeping each component isolated, the code remains 
#    easier to debug and extend. For example, if an issue arises in handling floating-point numbers, you can isolate it to the `float_examples()` function.
#
# Advanced Tip: Consider passing parameters to each function (e.g., input data or configuration settings) instead of using global 
# variables. This enhances the testability of each component and promotes better encapsulation.
#
# Alternative Approach: Instead of calling all functions unconditionally, you could enhance `main()` to accept command-line arguments
# using Python's `argparse` module. This would allow selective execution of specific functions, improving flexibility and usability 
# in different contexts (e.g., running performance analysis only when needed).
# ========================================


# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def integer_examples():
    """
    Demonstrates integer operations and properties in Python.
    """
    print("Integer Examples:")

    # Basic arithmetic operations with integers
    a, b = 10, 3  # Assigning values to variables `a` and `b`
    
    # Arithmetic Operations
    print(f"Addition: {a} + {b} = {a + b}")  # Basic addition
    print(f"Subtraction: {a} - {b} = {a - b}")  # Basic subtraction
    print(f"Multiplication: {a} * {b} = {a * b}")  # Basic multiplication
    print(f"Division (float result): {a} / {b} = {a / b}")  # Regular division produces a float result
    print(f"Integer division: {a} // {b} = {a // b}")  # Floor division results in an integer
    print(f"Modulo: {a} % {b} = {a % b}")  # Remainder of division operation
    print(f"Exponentiation: {a} ** {b} = {a ** b}") # `a` raised to the power `b`

    # Best Practice: Prefer `//` over `/` when you need an integer result to avoid potential type issues.

    # Bitwise operations - low-level operations that directly manipulate bits
    print(f"Bitwise AND: {a} & {b} = {a & b}")  # AND operation - sets each bit to 1 if both bits are 1
    print(f"Bitwise OR: {a} | {b} = {a | b}")  # OR operation - sets each bit to 1 if one of the bits is 1
    print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")  # XOR operation - sets each bit to 1 if only one of the bits is 1
    print(f"Bitwise NOT: ~{a} = {~a}")  # NOT operation - inverts all bits (produces a two's complement)
    print(f"Left shift: {a} << 1 = {a << 1}")  # Shifts bits left by 1 position (equivalent to multiplying by 2)
    print(f"Right shift: {a} >> 1 = {a >> 1}")  # Shifts bits right by 1 position (equivalent to dividing by 2)

    # Advanced Tip: Bitwise operations are extremely fast and are often used in low-level programming, 
    # such as writing device drivers, optimizing mathematical algorithms, or handling binary protocols.

    # Arbitrary precision demonstration - Python's `int` has arbitrary precision (unlike fixed-size integers in C/C++)
    large_num = 2 ** 100  # Calculating a very large number
    print(f"Large number (2100): {large_num}")
    print(f"Digits in large number: {len(str(large_num))}")  # Converting to string to count digits

    # Potential Pitfall: While Python supports arbitrarily large integers, arithmetic operations on them 
    # can be slower than operations on standard integers due to additional overhead.

def float_examples():
    """
    Demonstrates float operations and properties in Python.
    """
    print("\nFloat Examples:")

    # Basic arithmetic operations with floats
    x, y = 3.14, 2.5  # Assigning float values to variables `x` and `y`
    
    # Arithmetic Operations
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")

    # Best Practice: Always be cautious with floating-point arithmetic due to potential precision issues.

    # Floating-point precision issues demonstration
    a = 0.1 + 0.2  # Expected result is 0.3
    b = 0.3
    print(f"0.1 + 0.2 == 0.3: {a == b}")  # This will be False due to precision limitations
    print(f"Actual sum: {a}")
    print(f"Difference: {abs(a - b)}")  # Shows the small difference due to floating-point representation

    # Advanced Tip: Floating-point numbers are represented in binary as per IEEE 754 standard, leading to potential precision loss. 
    # Always consider this when comparing floats and use a tolerance (epsilon) where necessary.

    # Using `decimal` module for precise arithmetic
    d1 = decimal.Decimal('0.1')
    d2 = decimal.Decimal('0.2')
    d3 = decimal.Decimal('0.3')
    print(f"Using Decimal: {d1} + {d2} == {d3}: {d1 + d2 == d3}")  # This will be True, unlike the float example

    # Insight: The `decimal` module is slower than native float operations but is crucial when precision is paramount 
    # (e.g., financial applications).

    # Special float values demonstration
    print(f"Infinity: {float('inf')}")  # Represents an infinite value
    print(f"Negative Infinity: {float('-inf')}")  # Represents negative infinity
    print(f"Not a Number (NaN): {float('nan')}")  # Represents an undefined or unrepresentable value

    # Pitfall: Be aware that `NaN` is not equal to itself (`float('nan') != float('nan')`). This can lead to 
    # unexpected behavior in comparisons or data analysis tasks.

def complex_examples():
    """
    Demonstrates complex number operations and properties.
    """
    print("\nComplex Number Examples:")
    
    # Creating complex numbers
    z1 = 3 + 4j  # Complex number: 3 is the real part, 4 is the imaginary part (j is used to denote the imaginary unit)
    z2 = complex(2, -1)  # Alternative way to create a complex number with real=2 and imaginary=-1 using the `complex()` constructor
    print(f"z1 = {z1}, z2 = {z2}")

    # Basic arithmetic operations with complex numbers
    # Note: Python supports direct arithmetic operations on complex numbers without any special libraries
    print(f"Addition: {z1} + {z2} = {z1 + z2}")  # Adds the real parts and the imaginary parts separately
    print(f"Subtraction: {z1} - {z2} = {z1 - z2}")  # Subtracts real and imaginary components accordingly
    print(f"Multiplication: {z1} * {z2} = {z1 * z2}")  # Distributes multiplication using (a+bi)(c+di) = (ac−bd) + (ad+bc)i
    print(f"Division: {z1} / {z2} = {z1 / z2}")  # Divides using (a+bi) / (c+di), which involves rationalizing the denominator

    # Accessing attributes and methods
    # In Python, complex numbers have built-in attributes for accessing their real and imaginary parts
    print(f"Real part of z1: {z1.real}")  # Accesses the real part of z1 using `.real` attribute
    print(f"Imaginary part of z1: {z1.imag}")  # Accesses the imaginary part using `.imag` attribute
    print(f"Conjugate of z1: {z1.conjugate()}")  # Computes the conjugate (flips the sign of the imaginary part)

    # Using cmath module for complex math operations
    # `cmath` is the counterpart of the `math` module, designed specifically for complex numbers
    print(f"Magnitude (absolute value) of z1: {abs(z1)}")  # Magnitude is the distance from the origin (0,0) to the point (real, imag), equivalent to sqrt(real^2 + imag^2)
    print(f"Phase (angle) of z1: {cmath.phase(z1)} radians")  # The angle in polar coordinates; calculated using atan(imag/real), result is in radians
    print(f"Square root of z1: {cmath.sqrt(z1)}")  # Computes the square root, handling both real and imaginary parts accurately

# ========================================
# Additional Insights:
# ---------------------------------
# 1. Complex Numbers in Python:
#    - Python's built-in `complex` type makes handling complex numbers seamless compared to many other languages 
#      where external libraries are necessary.
#    - Complex numbers are immutable, meaning any operation creates a new complex number rather than modifying the original.

# 2. Best Practice: 
#    - Use `cmath` for complex-specific functions, as it is optimized for such operations. Avoid using the standard `math` module 
#      since it only handles real numbers and will raise errors with complex inputs.

# 3. Pitfall:
#    - Attempting to use `math.sqrt()` on a negative real number will raise a `ValueError`. Use `cmath.sqrt()` instead, 
#      as it handles complex results correctly.

# 4. Advanced Tip:
#    - When working with polar coordinates, you can convert between polar and rectangular (Cartesian) using `cmath.polar()` 
#      and `cmath.rect()`. These methods are handy in applications like signal processing, control systems, or physics simulations.
#    - Example: `cmath.polar(z1)` returns a tuple (r, θ) representing the modulus and phase of the complex number.

# Example usage of conversion between polar and rectangular forms:
# polar_form = cmath.polar(z1)  # Converts to polar coordinates
# rectangular_form = cmath.rect(polar_form[0], polar_form[1])  # Converts back to rectangular coordinates

# 5. Performance Note:
#    - Although complex number arithmetic is generally efficient in Python, be cautious in performance-critical applications.
#      Libraries like NumPy can offer substantial performance improvements through vectorized operations if you are working 
#      with large arrays of complex numbers.


def string_examples():
    """
    Demonstrates string operations and properties in Python, offering insights into common string manipulations,
    best practices, and potential pitfalls.
    """
    print("\nString Examples:")
    
    # String creation and basic operations
    s1 = "Hello"  # Standard double-quoted string
    s2 = 'World'  # Standard single-quoted string (no functional difference from double quotes in Python)
    
    # Concatenation of strings using the `+` operator
    print(f"Concatenation: {s1} + ' ' + {s2} = {s1 + ' ' + s2}")
    # Advanced Tip: For more efficient concatenation of multiple strings, consider using `str.join()` or f-strings 
    # instead of repeated `+` operators, especially in loops, to avoid unnecessary memory overhead.
    
    # Repeating strings using the `*` operator
    print(f"Repetition: {s1} * 3 = {s1 * 3}")
    # Pitfall: Be cautious when using large repetition factors as it can lead to high memory usage.

    # String methods and manipulation
    s = "  Python Programming  "  # String with leading and trailing whitespaces
    print(f"Original string: '{s}'")
    print(f"Uppercase: '{s.upper()}'")  # Converts all characters to uppercase
    print(f"Lowercase: '{s.lower()}'")  # Converts all characters to lowercase
    print(f"Stripped (remove leading/trailing whitespace): '{s.strip()}'")  # Removes whitespace from both ends
    
    # Splitting the string into a list based on the delimiter ' ' (space) after stripping
    print(f"Split into list: {s.strip().split(' ')}")
    # Advanced Tip: Consider using `re.split()` from the `re` module for more complex splitting patterns (e.g., splitting on multiple delimiters).

    # String formatting techniques
    name = "Alice"
    age = 30
    # Using f-string formatting (Python 3.6+), the most modern and efficient way
    print(f"Using f-string: {name} is {age} years old")
    
    # Using the `format` method, useful for more complex scenarios
    print("Using format method: {} is {} years old".format(name, age))
    
    # Using the `%` operator, the older and less preferred method
    print("Using % operator: %s is %d years old" % (name, age))
    # Best Practice: Prefer f-strings for readability and performance in modern Python versions (3.6+).

    # String slicing
    text = "Python"
    print(f"Slicing [1:4] of '{text}': '{text[1:4]}'")  # Extracts a substring from index 1 to 3 ('yth')
    print(f"Reverse '{text}': '{text[::-1]}'")  # Reverses the string using slicing with a step of -1
    
    # Advanced Tip: Slicing is an O(n) operation, so avoid unnecessary slicing in performance-critical code.

    # Unicode support (Python 3 uses Unicode by default for all strings)
    unicode_string = "Здравствуй, мир! 你好，世界！"
    print(f"Unicode string: {unicode_string}")
    # Insight: Python 3's default Unicode support makes it ideal for working with internationalized text,
    # unlike Python 2, which required a separate `u''` syntax for Unicode strings.

def boolean_examples():
    """
    Demonstrates boolean operations and properties, with a focus on practical examples, best practices, and potential pitfalls.
    """
    print("\nBoolean Examples:")
    
    # Boolean values in Python
    t, f = True, False  # `True` and `False` are built-in constants
    print(f"True: {t}, False: {f}")
    
    # Logical operations (AND, OR, NOT)
    print(f"AND operation: {t} and {f} = {t and f}")  # Evaluates to False since both operands aren't True
    print(f"OR operation: {t} or {f} = {t or f}")  # Evaluates to True since at least one operand is True
    print(f"NOT operation: not {t} = {not t}, not {f} = {not f}")  # Inverts the boolean value
    
    # Comparison operations resulting in boolean outcomes
    x, y = 5, 10
    print(f"{x} < {y}: {x < y}")  # True
    print(f"{x} > {y}: {x > y}")  # False
    print(f"{x} == {y}: {x == y}")  # False
    print(f"{x} != {y}: {x != y}")  # True
    # Best Practice: Always use explicit comparisons (e.g., `x == y`) instead of implicit ones (e.g., `x is y`) 
    # for checking equality of values.

    # Demonstrating truthy and falsy values in Python
    print(f"bool(0): {bool(0)}")  # 0 is considered False
    print(f"bool(1): {bool(1)}")  # Non-zero integers are considered True
    print(f"bool(''): {bool('')}")  # Empty strings are considered False
    print(f"bool('text'): {bool('text')}")  # Non-empty strings are considered True
    print(f"bool([]): {bool([])}")  # Empty lists are considered False
    print(f"bool([1, 2]): {bool([1, 2])}")  # Non-empty lists are considered True

    # Pitfall: Be cautious with the use of `==` and `is`. While `==` checks for value equality, 
    # `is` checks for object identity (i.e., whether two variables point to the same object in memory).
    # Example:
    #     >>> a = [1, 2, 3]
    #     >>> b = [1, 2, 3]
    #     >>> a == b  # True (same content)
    #     >>> a is b  # False (different objects)

def type_conversion_examples():
    """
    Demonstrates type conversion between basic data types.
    """
    print("\nType Conversion Examples:")
    
    # Integer conversions
    print(f"int('100'): {int('100')}")  # Converts a numeric string to an integer. Raises ValueError if the string is non-numeric.
    print(f"int(3.14): {int(3.14)}")  # Truncates the decimal part; no rounding (e.g., 3.99 becomes 3).
    print(f"int(True): {int(True)}")  # Boolean to integer conversion; True = 1, False = 0. Common in logical operations.

    # Float conversions
    print(f"float('3.14'): {float('3.14')}")  # Converts a string to a float. Non-numeric strings will cause a ValueError.
    print(f"float(5): {float(5)}")  # Converts an integer to float. No precision is lost here.

    # Complex conversions
    print(f"complex(3, 4): {complex(3, 4)}")  # Creates a complex number with real part 3 and imaginary part 4.
    print(f"complex('3+4j'): {complex('3+4j')}")  # Parses a string into a complex number. Ensure the string is in the correct format.
    
    # String conversions
    print(f"str(123): '{str(123)}'")  # Converts an integer to string, making it easier to concatenate with other strings.
    print(f"str(3.14): '{str(3.14)}'")  # Converts a float to string, preserving precision in the representation.
    print(f"str(True): '{str(True)}'")  # Converts a boolean to string ('True'/'False').

    # Boolean conversions
    print(f"bool(1): {bool(1)}")  # Any non-zero integer converts to True.
    print(f"bool(0): {bool(0)}")  # Zero is always False.
    print(f"bool('False'): {bool('False')}")  # Any non-empty string evaluates to True, even if it's 'False'.

    # Potential Pitfall: Be cautious with `int()` or `float()` conversions when input data may not be in the expected format.
    # Always handle exceptions to avoid runtime errors in production environments.
    #
    # Advanced Tip: Use `ast.literal_eval` for safer type conversion when handling unknown input. It evaluates strings 
    # containing Python literals (e.g., numbers, booleans) and avoids the security risks associated with `eval()`.
 
def advanced_usage_examples():
    """
    Demonstrates advanced usage of basic data types.
    """
    print("\nAdvanced Usage Examples:")
    
    # Using sys.getsizeof to check memory usage
    print(f"Size of int(0): {sys.getsizeof(0)} bytes")  # Size can vary across platforms; useful for understanding memory footprint.
    print(f"Size of int(1000000): {sys.getsizeof(1000000)} bytes")  # Demonstrates Python's ability to handle large integers.

    # Timing operations using time.perf_counter()
    def time_operation(op):
        start = time.perf_counter()  # High-resolution timer suitable for measuring short durations.
        result = op()
        end = time.perf_counter()
        return result, end - start
    
    # Compare integer and float multiplication performance
    int_result, int_time = time_operation(lambda: 123456789 * 987654321)
    float_result, float_time = time_operation(lambda: 123456789.0 * 987654321.0)
    print(f"Integer multiplication time: {int_time:.6f} seconds")
    print(f"Float multiplication time: {float_time:.6f} seconds")
    
    # Advanced Insight: Integer operations are often faster than floating-point due to hardware optimizations.
    # However, floats may be preferable when working with fractional values or requiring scientific notation.

    # String interning demonstration
    s1 = "python"
    s2 = "python"
    s3 = "".join(["p", "y", "t", "h", "o", "n"])  # Constructs a new string object.
    print(f"s1 is s2: {s1 is s2}")  # Likely True: String literals may be interned (memory optimization by Python).
    print(f"s1 is s3: {s1 is s3}")  # Likely False: Interning doesn't apply to dynamically constructed strings.

    # Pitfall: String interning behavior can be unpredictable in complex scenarios. Never rely solely on `is` for string comparison.

    # Using frozenset for immutable sets
    fs = frozenset([1, 2, 3, 4, 5])
    print(f"Frozenset (immutable set): {fs}")
    
    # Advanced Tip: Frozensets can be used as dictionary keys or elements of other sets due to immutability, unlike regular sets.

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
    
    # Insight: The use of Union and Any enhances code readability and helps with static type checking using tools like `mypy`.
    # It makes the code more maintainable, especially in larger projects with multiple contributors.

# Note: Always use built-in functions or modules (like `time`, `sys`, `logging`) where applicable, 
# as they are optimized and provide consistent functionality across Python versions.
# Using these advanced practices ensures code robustness, maintainability, and optimized performance.


# ========================================
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------
def best_practices_and_pitfalls():
    """
    Discusses best practices, common pitfalls, and advanced tips in using Python's basic data types effectively.
    """
    print("\nBest Practices and Common Pitfalls:")
    
    # Best Practice: Use meaningful, descriptive variable names
    # Meaningful variable names improve code readability and maintainability.
    total_price = 100.0  # Represents the total price before discount
    discount_rate = 0.1  # Represents the discount rate (10%)
    discounted_price = total_price * (1 - discount_rate)  # Calculate the price after applying discount
    print(f"Discounted Price: {discounted_price}")  # Outputs: Discounted Price: 90.0

    # Common Pitfall: Floating-point precision issues
    # -------------------------------------------------
    # Floating-point arithmetic can lead to precision errors because of the way numbers are represented in binary.
    a = 0.1 + 0.2
    print(f"0.1 + 0.2 == 0.3: {a == 0.3}")  # Outputs: False due to precision error
    print(f"Actual sum: {a}")  # Outputs: Actual sum: 0.30000000000000004
    
    # Advanced Tip: Solution to precision issues
    # -------------------------------------------
    # When precise calculations are necessary (e.g., financial applications), use the `decimal` module.
    from decimal import Decimal
    a = Decimal('0.1') + Decimal('0.2')  # Using strings ensures exact representation
    print(f"Using Decimal: Decimal('0.1') + Decimal('0.2') == Decimal('0.3'): {a == Decimal('0.3')}")  # Outputs: True

    # Advanced Tip: Use f-strings for efficient string formatting (introduced in Python 3.6)
    # -------------------------------------------------
    # f-strings are faster and more readable than other formatting methods (e.g., `%` or `str.format()`).
    name = "Bob"
    age = 25
    print(f"{name} is {age} years old.")  # Outputs: Bob is 25 years old.
    
    # Alternative approach for earlier Python versions:
    # print("{} is {} years old.".format(name, age))  # Works but is less efficient and harder to read

# ========================================
# Explanation and Insights
# ---------------------------------
# 1. Using f-strings is considered best practice in modern Python for cleaner, more readable code.
# 2. The `decimal` module effectively addresses floating-point precision issues, especially important for use cases 
#    like financial calculations where even small inaccuracies can have significant impacts.
# ========================================

# ========================================
# 4. Integration and Real-World Applications
# ------------------------------------------

def real_world_applications():
    """
    Provides examples of how basic data types are utilized in real-world applications.
    """
    print("\nReal-World Applications:")

    # Data Science with NumPy (if available)
    if numpy_available:
        arr = np.array([1, 2, 3, 4, 5], dtype=float)  # Creating a NumPy array with float data type
        print(f"NumPy array: {arr}")  # Outputs: NumPy array: [1. 2. 3. 4. 5.]
    else:
        # Providing guidance when NumPy is unavailable
        print("NumPy is not available. Install it using 'pip install numpy' for numerical computing.")
    
    # Explanation: NumPy arrays are more efficient than Python lists for numerical computations, both in terms of 
    # speed and memory usage. They also offer a rich set of functionalities for data manipulation and analysis.

    # Web Development with Flask (conceptual example)
    # -------------------------------------------------
    # Python's basic types (e.g., strings, integers) are commonly used in web frameworks like Flask and Django 
    # for handling HTTP requests and responses.
    # Example: In Flask, request.args.get('param') returns a string representation of a query parameter.
    print("Web frameworks like Flask and Django use Python's basic types for handling requests and responses.")

    # Finance Calculations using Decimal for precise monetary values
    # -------------------------------------------------
    # Always use `decimal.Decimal` for financial applications to avoid floating-point inaccuracies.
    price = decimal.Decimal('19.99')  # Represents the price of an item
    quantity = 3  # The number of items purchased
    total = price * quantity  # Calculating the total price accurately
    print(f"Total price using Decimal: {total}")  # Outputs: Total price using Decimal: 59.97

    # System Administration scripting example
    # -------------------------------------------------
    # Basic data types are frequently used in system administration scripts for log parsing, system monitoring, etc.
    # Example: Checking system memory usage with `psutil` (if installed) or parsing logs for specific patterns.
    print("Using basic types in scripts for log parsing and system monitoring.")
    
# ========================================
# Explanation and Insights
# ---------------------------------
# 1. Integration with NumPy showcases the efficiency of Python's basic data types in high-performance computations.
# 2. Using `decimal.Decimal` in finance ensures calculations remain accurate, a critical requirement in this domain.
# 3. Familiarity with how basic types interface with libraries like Flask/Django or tools like `psutil` (for system 
#    monitoring) demonstrates their versatility across different real-world applications.
# ========================================


# ========================================
# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def advanced_concepts_and_trends():
    """
    Discusses advanced concepts and emerging trends in Python, including type hinting, JIT compilation, 
    and pattern matching. These concepts are crucial for writing modern, efficient, and maintainable Python code.
    """
    print("\nAdvanced Concepts and Emerging Trends:")
    
    # Type Hinting and Static Type Checking with mypy
    # ------------------------------------------------
    # Python introduced type hinting in PEP 484 (Python 3.5+), allowing developers to specify expected data types.
    # Although Python is dynamically typed, type hints improve code readability, maintenance, and enable static 
    # type checking using tools like `mypy`. This helps catch type-related bugs early in the development process.
    def greet(name: str) -> str:
        # `name: str` specifies that the argument should be a string.
        # `-> str` indicates that the function returns a string.
        return f"Hello, {name}"
    
    print(greet("Alice"))  # Expected output: "Hello, Alice"
    print("Type hints improve code readability and enable static type checking with tools like mypy.")
    
    # Best Practice Insight: While type hints are optional, they are highly recommended for projects involving 
    # multiple developers or when building large codebases. They also improve integration with IDEs by enabling 
    # advanced autocompletion and error detection.
    
    # Potential Pitfall: Type hints do not enforce type checking at runtime (they are ignored by the Python interpreter).
    # To leverage them fully, you must use a static type checker like `mypy`.

    # JIT Compilation with Numba (conceptual example)
    # ----------------------------------------------
    # Just-In-Time (JIT) Compilation with Numba:
    # Numba is a JIT compiler that translates a subset of Python and NumPy code into fast machine code at runtime.
    # This can drastically improve performance for numerical and scientific computing tasks. It integrates well
    # with NumPy, making it ideal for computational-heavy loops or array manipulations.
    print("Numba can be used to speed up numerical computations by compiling Python functions to machine code.")
    
    # Example (conceptual): Uncomment if Numba is installed
    # from numba import jit
    # @jit(nopython=True)
    # def add_numbers(a, b):
    #     return a + b
    # print(add_numbers(10, 20))
    
    # Advanced Tip: Numba works best with numerical computations and is not suitable for general-purpose Python code.
    # If you're working with complex data structures or non-numerical logic, Numba might not yield significant benefits.

    # Pattern Matching in Python 3.10+
    # -------------------------------
    version_info = sys.version_info  # Accesses Python version information
    if version_info.major >= 3 and version_info.minor >= 10:
        print("Pattern matching is available in Python 3.10 and later.")
        
        # Pattern Matching Overview:
        # Introduced in Python 3.10, pattern matching provides a more readable and expressive way to handle 
        # conditional logic based on the structure of data. It is conceptually similar to `switch` statements in 
        # other languages but far more powerful and versatile.
        
        # Example of pattern matching (commented out to maintain compatibility with earlier Python versions)
        # def http_error(status):
        #     match status:
        #         case 400:
        #             return "Bad request"
        #         case 404:
        #             return "Not found"
        #         case _:
        #             return "Other error"
        
        # Best Practice Insight: Use pattern matching for complex data structures or when handling multiple conditions.
        # It leads to cleaner, more maintainable code compared to nested `if-elif` statements.
        
        # Potential Pitfall: Be cautious when using pattern matching, as it is a relatively new feature. Ensure that 
        # all team members are familiar with it, and be mindful of compatibility issues if targeting older Python versions.
        
    else:
        print("Pattern matching is not available in your Python version.")
        # Note: If you're working with a Python version < 3.10, consider upgrading to leverage modern features 
        # and enhance code expressiveness and maintainability.

# ========================================
# Additional Expert Insights:
# ----------------------------------------
# 1. Type Hinting: Although Python remains dynamically typed, the inclusion of type hints signifies a move towards 
#    static type checking. This trend aligns Python more closely with statically typed languages like TypeScript, 
#    making it easier for developers transitioning from such languages.
#
# 2. JIT Compilation: The rise of JIT compilation (through tools like Numba, PyPy) reflects a growing emphasis on 
#    performance optimization in Python, especially in scientific computing and data science. Understanding how and 
#    when to use JIT compilation can dramatically improve the efficiency of heavy computations.
#
# 3. Pattern Matching: Pattern matching is not merely syntactic sugar; it represents a shift towards more declarative 
#    programming in Python. As this trend gains traction, expect to see it increasingly used in libraries and frameworks, 
#    making it an essential skill for Python developers moving forward.


# ========================================
# 6. FAQs and Troubleshooting
# ---------------------------
def faqs_and_troubleshooting():
    """
    Provides answers to common questions and troubleshooting tips related to Python's basic data types 
    and operations. These examples illustrate common issues and clarify misconceptions, making them 
    valuable for developers at all levels.
    """
    print("\nFAQs and Troubleshooting:")
    
    # Q: Why does 0.1 + 0.2 != 0.3?
    a = 0.1 + 0.2
    print(f"0.1 + 0.2 == 0.3: {a == 0.3}")
    print("A: This is due to floating-point precision errors in binary representation.")
    
    # Explanation:
    # - Floating-point numbers are represented in binary, leading to precision errors since 0.1 and 0.2 
    #   cannot be precisely expressed in binary.
    # - This results in a small rounding error, which is why 0.1 + 0.2 doesn't exactly equal 0.3.
    # Best Practice: When precise decimal arithmetic is needed (e.g., financial applications), use the `decimal` module.
    
    # Q: How to safely convert a string to an integer?
    s = "123"
    try:
        num = int(s)  # Converts a string to an integer if possible
        print(f"Converted '{s}' to integer: {num}")
    except ValueError:
        print(f"Cannot convert '{s}' to integer.")  # Catches conversion errors when `s` is not a valid integer string
    
    # Explanation:
    # - The `int()` function can raise a `ValueError` if the string cannot be converted (e.g., "abc").
    # - Using a try-except block ensures that the program handles such cases gracefully.
    # Advanced Tip: Consider using `str.isdigit()` before conversion if you expect only positive integers, 
    # but note that it doesn't handle negative numbers or non-numeric characters.

    # Q: Difference between '==' and 'is'
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    print(f"x == y: {x == y}")  # True: `==` checks for value equality
    print(f"x is y: {x is y}")  # True: `is` checks for object identity (i.e., same memory address)
    print(f"x == z: {x == z}")  # True: `==` checks if contents are the same
    print(f"x is z: {x is z}")  # False: `is` checks if they are the exact same object in memory

    # Explanation:
    # - `==` compares values/contents, whereas `is` compares object identity (memory location).
    # - This distinction is crucial when dealing with mutable objects like lists, dictionaries, or custom objects.
    # Advanced Tip: Use `is` only when checking against `None` (i.e., `if variable is None:`) or for identity checks.
    
# ========================================
# Explanation and Insights
# ---------------------------------
# 1. The `faqs_and_troubleshooting` function addresses common issues that Python developers face, emphasizing 
#    the importance of understanding fundamental differences like value equality vs. identity.
# 2. Including exception handling (`try-except`) and clarifying common misconceptions (floating-point arithmetic)
#    provides developers with practical knowledge that aids in debugging and troubleshooting.
# ========================================


# ========================================
# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
def recommended_resources():
    """
    Recommends tools, libraries, and resources to help developers expand their knowledge and improve their 
    coding practices in Python. These recommendations cater to both beginners and advanced developers.
    """
    print("\nRecommended Tools, Libraries, and Resources:")
    
    # Tool Recommendations
    print("- Tools:")
    print("  - mypy: Performs static type checking, helping catch type-related bugs before runtime.")
    # Insight: Static typing with `mypy` improves code reliability and maintainability, especially in large codebases.
    
    print("  - Black: A code formatter that enforces consistent code style, improving readability and reducing 'bikeshedding'.")
    # Advanced Tip: Integrate `Black` into your CI/CD pipeline to ensure code consistency across your team.

    # Library Recommendations
    print("- Libraries:")
    print("  - decimal: Ideal for precise decimal arithmetic, avoiding floating-point precision issues.")
    print("  - math: Provides a range of mathematical functions for complex calculations; complements Python's built-in operators.")
    # Advanced Tip: For scientific computing or data analysis, consider using `numpy` or `scipy` due to their optimized performance.

    # Resource Recommendations
    print("- Resources:")
    print("  - Python official documentation: https://docs.python.org/3/")
    # Explanation: The official docs are the most authoritative source of Python knowledge, regularly updated with the latest features.

    print("  - 'Fluent Python' by Luciano Ramalho: A comprehensive guide to writing idiomatic and effective Python code.")
    # Insight: 'Fluent Python' is an excellent resource for understanding Python's nuances, including data structures, concurrency, and metaprogramming.

    print("  - 'Effective Python' by Brett Slatkin: Offers 90+ actionable guidelines for writing better Python code.")
    # Advanced Tip: This book covers advanced techniques and design patterns that are crucial for developers aiming to become senior or principal engineers.

# ========================================
# Explanation and Insights
# ---------------------------------
# 1. The `recommended_resources` function offers valuable suggestions for tools, libraries, and resources that 
#    cater to different stages of a developer's journey, providing a well-rounded foundation for learning.
# 2. By recommending static type checkers (`mypy`) and code formatters (`Black`), this section encourages best practices 
#    in code quality, which is essential for larger projects and collaborative work.
# ========================================


# ========================================
# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis_and_optimization():
    """
    Includes a section on profiling and benchmarking code related to basic data types.
    Demonstrates how to use Python's `timeit` module to compare performance across different data types and operations.
    """
    print("\nPerformance Analysis and Optimization:")

    # Performance Comparison Example
    print("Performance Comparison:")

    # Setup for data generation
    setup = """
import random  # Importing random module for generating random floating-point numbers
data = [random.random() for _ in range(1000000)]  # Creating a list of 1,000,000 random floats
"""

    # Test 1: Standard Python list summation
    list_test = """
result = sum(data)  # Summing all elements in the list using built-in sum()
"""
    list_time = timeit.timeit(list_test, setup=setup, number=10)  # Repeating the test 10 times to get a more reliable measure
    print(f"Python list sum time: {list_time:.6f} seconds")

    # Advanced Insight:
    # The `sum()` function is optimized for Python lists, but it could be slower compared to specialized libraries for larger datasets.

    # Test 2: Array module summation
    array_test = """
arr = array.array('d', data)  # Creating an array of doubles (float64) from the list of data
result = sum(arr)  # Summing elements in the array
"""
    array_time = timeit.timeit(array_test, setup=setup + "import array", number=10)
    print(f"Array module sum time: {array_time:.6f} seconds")

    # Performance Insight:
    # Using `array.array` can be more memory efficient than lists for homogeneous data types. 
    # This is because `array.array` stores data in a more compact, C-style format.
    # However, `sum()` may still be slower than specialized numerical libraries like NumPy for large data sets.

    # Test 3: NumPy array summation (if available)
    if numpy_available:
        numpy_test = """
np_arr = np.array(data)  # Converting the list into a NumPy array for optimized performance
result = np.sum(np_arr)  # Using NumPy's sum() method, which is implemented in C for higher efficiency
"""
        numpy_time = timeit.timeit(numpy_test, setup=setup + "import numpy as np", number=10)
        print(f"NumPy array sum time: {numpy_time:.6f} seconds")
    else:
        print("NumPy is not available for performance comparison. Install it using 'pip install numpy'.")

    # Advanced Tip:
    # NumPy operations are typically faster because they are implemented in compiled C code and leverage SIMD (Single Instruction, Multiple Data)
    # instructions for parallel processing. This makes NumPy an excellent choice for numerical and scientific computing.

    # String concatenation comparison
    print("\nString Concatenation Comparison:")

    # Setup for string concatenation tests
    setup_str = """
words = ['python'] * 10000  # Create a list containing the word 'python' repeated 10,000 times
"""

    # Test 1: Concatenation using '+=' (inefficient)
    concat_test = """
result = ''
for word in words:
    result += word  # Appending each word to the result using '+='
"""
    concat_time = timeit.timeit(concat_test, setup=setup_str, number=100)
    print(f"String concatenation with '+=' time: {concat_time:.6f} seconds")

    # Performance Insight:
    # Using `+=` for string concatenation is inefficient in Python because strings are immutable. 
    # Each `+=` operation creates a new string object, which leads to higher memory usage and slower performance.

    # Test 2: Concatenation using 'join()' (efficient)
    join_test = """
result = ''.join(words)  # Using join() to concatenate all strings in the list
"""
    join_time = timeit.timeit(join_test, setup=setup_str, number=100)
    print(f"String concatenation with 'join()' time: {join_time:.6f} seconds")
    print("Using ''.join() is generally faster and more memory-efficient.")

    # Best Practice:
    # Always prefer `str.join()` for concatenating multiple strings, especially in loops or when working with large datasets.
    # This method performs a single pass over the data, minimizing memory overhead and significantly improving performance.


def memory_management_and_resource_optimization():
    """
    Discusses memory management and resource optimization techniques.
    """
    print("\nMemory Management and Resource Optimization:")
    
    # Using generators for large datasets
    # ------------------------------------------------------
    # A generator expression is used here to create an iterable sequence of squares
    # for a large range (up to 1,000,000). Unlike lists, generators produce items
    # on-the-fly, which significantly reduces memory usage, making them ideal for
    # processing large datasets.
    # Advanced Insight: Generators are an excellent choice for 'lazy evaluation' where
    # not all elements need to be stored in memory at once.
    gen_exp = (x**2 for x in range(1000000))
    print(f"Generator expression created for large dataset to save memory.")

    # Using __slots__ in classes to reduce memory overhead
    # ------------------------------------------------------
    # The `__slots__` declaration restricts attribute assignment to the listed attributes
    # ('x' and 'y' in this case). This prevents the creation of a default __dict__ for
    # each instance, thereby saving memory and improving access speed.
    # Best Practice: Use `__slots__` for memory efficiency when creating many instances
    # of lightweight classes, especially in high-performance applications.
    class Point:
        __slots__ = ['x', 'y']  # Restricts attributes to reduce memory overhead
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    p = Point(1, 2)
    print(f"Point created with x={p.x}, y={p.y}")
    
    # Using weak references to prevent memory leaks
    # ------------------------------------------------------
    # Weak references allow an object to be referenced without preventing it from being
    # garbage collected. This is useful for managing memory in cases where you want to
    # avoid circular references or cache objects without retaining them indefinitely.
    # Potential Pitfall: Weak references should be used carefully as the object can be
    # collected at any time once there are no strong references left.
    import weakref
    class MyClass:
        pass
    obj = MyClass()
    r = weakref.ref(obj)  # Creates a weak reference to 'obj'
    print(f"Weak reference created: {r}")
    print(f"Object referenced: {r()}")  # Access the object, or `None` if already collected
    
    # Using context managers to manage resources
    # ------------------------------------------------------
    # Context managers (using `__enter__` and `__exit__` methods) ensure that resources,
    # like file handles, are properly acquired and released. This helps prevent resource
    # leaks and ensures clean-up even if an error occurs.
    # Advanced Tip: Always use context managers for I/O operations (files, network
    # connections, etc.) to ensure efficient resource handling.
    class FileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            self.file = open(self.filename, self.mode)  # Opens the file
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()  # Ensures the file is closed even if an error occurs
    
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
    # ------------------------------------------------------
    # The `safe_divide` function handles division with appropriate exception handling.
    # This avoids crashes in case of invalid operations, ensuring the program can
    # handle unexpected input gracefully.
    # Best Practice: Use specific exceptions to handle errors; avoid generic 'except'
    # statements as they can obscure unexpected issues.
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
    # ------------------------------------------------------
    # The `validate_age` function checks for valid input using explicit type and range checks.
    # This practice prevents invalid states from propagating through the system.
    # Advanced Tip: Always validate inputs at the boundary (i.e., at the entry points of your
    # system or API) to catch errors early and reduce debugging complexity.
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
    # ------------------------------------------------------
    # The `calculate_average` function uses an assert statement to catch erroneous inputs.
    # This is effective during development for detecting logical errors or invalid assumptions.
    # Caution: Avoid leaving assert statements in production code as they can be disabled with
    # the `-O` (optimize) flag, leading to unintended behavior.
    def calculate_average(numbers):
        assert len(numbers) > 0, "List cannot be empty"
        return sum(numbers) / len(numbers)
    
    try:
        calculate_average([])
    except AssertionError as e:
        print(f"Assertion error: {e}")
    
    # Implementing logging for monitoring
    # ------------------------------------------------------
    # Logging provides a way to track the execution flow and capture essential information
    # about the program's state, helping with debugging and maintenance.
    # Advanced Tip: Use appropriate logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    # and consider using structured logging for complex systems to make log analysis easier.
    def perform_calculation(data):
        return sum(data)  # Simulated calculation function
    
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
    # Run main function to demonstrate all examples
    main()
    # Additional specialized demonstrations
    memory_management_and_resource_optimization()
    handling_edge_cases_in_complex_systems()

