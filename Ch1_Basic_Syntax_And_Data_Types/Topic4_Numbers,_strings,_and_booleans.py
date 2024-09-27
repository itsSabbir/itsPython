"""
Expert-Level Cheat Sheet: Basic Syntax and Data Types - Numbers, strings, and booleans - in the Python Programming Language

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization

This cheat sheet serves as a comprehensive guide to numbers, strings, and booleans in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Sabbir
Date: September 18, 2024
Python Version: 3.11+
"""

# Imports
import sys  # Provides access to system-specific parameters and functions
import math  # Offers access to mathematical functions like sqrt(), sin(), cos(), etc.
import decimal  # Enables precise decimal arithmetic, useful for financial calculations where float precision isn't enough
import fractions  # Facilitates operations with rational numbers (fractions), ideal when exact values are required
import itertools  # Contains efficient looping constructs for combinatorial operations, permutations, and more
import re  # Provides regular expression matching operations, a powerful tool for string searching and manipulation
import timeit  # Useful for timing the execution of small code snippets, aiding in performance optimization
from typing import Union, List, Dict  # Provides type hints, enhancing code readability and maintainability
import unittest  # Offers a built-in testing framework, crucial for maintaining code quality through unit testing

# 1. Overview and Historical Context
"""
Numbers, strings, and booleans are fundamental data types in Python, essential for representing
and manipulating data in programs.

**Historical Context:**
- Numbers: Python has supported integers and floating-point numbers since its inception.
  Complex numbers were added in Python 1.4 (1996).
- Strings: Initially only supported ASCII. Unicode support was added in Python 2.0 (2000).
  In Python 3, all strings are Unicode by default.
- Booleans: Introduced as a separate type in Python 2.3 (2003). Before that, 0 and empty containers
  were considered false, while all other values were true.

**Relevance in Modern Software Development:**
- Data processing and analysis: Numbers are used extensively in data analytics, finance, and statistics.
- Text manipulation and natural language processing (NLP): Strings are the foundation of NLP, web scraping, and more.
- Logical operations and control flow: Booleans control program logic, enabling decision-making.
- Mathematical and scientific computing: Widely used in engineering, physics simulations, and machine learning.

**Comparison to Other Languages:**
- Python's dynamic typing allows for more flexible use of these types compared to statically-typed languages.
- Python's string handling is generally more user-friendly than in languages like C.
- Python's boolean type is more explicit than in languages like C, where integers are used for boolean logic.
"""

# Advanced Insights and Tips:
# - The `decimal` module is ideal when you need exact decimal representation, avoiding issues common with binary floating-point arithmetic.
# - The `fractions` module is beneficial in cases requiring exact ratios; it prevents the inaccuracies introduced by floats, especially in scientific calculations.
# - `itertools` is invaluable for efficient looping, with constructs like `product`, `permutations`, and `combinations` that can drastically reduce code complexity.
# - `re` provides unparalleled power for text processing, but remember that regular expressions can become complex and difficult to maintain if overused. Always keep them as simple as possible.

# Best Practices:
# - Use `decimal.Decimal` for monetary calculations to avoid floating-point inaccuracies.
# - Leverage `fractions.Fraction` when exact arithmetic is essential, especially in domains like geometry or physics.
# - Utilize `itertools` for cleaner, more Pythonic code when handling combinations, permutations, or infinite iterators.
# - Regular expressions (`re`) should be used judiciously. Always compile patterns (`re.compile()`) for better performance, especially in loops.
# - Unittesting is a fundamental practice for maintaining code quality. Use `unittest` to write and execute test cases regularly.

# Pitfalls:
# - Be cautious of floating-point arithmetic inaccuracies: `0.1 + 0.2 != 0.3` due to precision errors.
# - Complex regular expressions can be hard to debug. Test them thoroughly, and document them for future reference.
# - Overusing `itertools` with large data sets can lead to memory and performance issues. Opt for generators to handle large datasets efficiently.


# ========================================
# 2. Syntax, Key Concepts, and Code Examples
# -----------------------------------------
# Demonstrating the syntax, key concepts, and practical examples of Python's basic data types and operations.
# ========================================

def number_basics():
    """Demonstrates basic concepts related to numbers in Python."""
    
    # Integer
    x = 10  # Integer assignment; integers are whole numbers without a fractional part
    print(f"Integer: {x}, Type: {type(x)}")  # type(x) returns <class 'int'>
    
    # Float
    y = 3.14  # Float assignment; floats are real numbers with a decimal point
    print(f"Float: {y}, Type: {type(y)}")  # type(y) returns <class 'float'>
    
    # Complex
    z = 1 + 2j  # Complex number assignment; 'j' represents the imaginary unit (equivalent to i in mathematics)
    print(f"Complex: {z}, Type: {type(z)}")  # type(z) returns <class 'complex'>
    
    # Boolean (subclass of int)
    b = True  # Boolean values are either True or False; internally represented as 1 (True) or 0 (False)
    print(f"Boolean: {b}, Type: {type(b)}")  # type(b) returns <class 'bool'>
    
    # Basic arithmetic
    # Arithmetic operations work intuitively, but attention should be paid to operator precedence
    print(f"Addition: {x + y}")  # Adds x and y
    print(f"Subtraction: {x - y}")  # Subtracts y from x
    print(f"Multiplication: {x * y}")  # Multiplies x by y
    print(f"Division: {x / y}")  # Always returns a float, even if x and y are both integers
    print(f"Floor Division: {x // y}")  # // performs floor division, discarding the fractional part
    print(f"Modulo: {x % 3}")  # Modulo operator returns the remainder of the division
    print(f"Exponentiation: {x ** 2}")  # Raises x to the power of 2 (x squared)
    
    # Pitfall: Division by zero will raise a ZeroDivisionError.
    # Advanced Tip: Use 'math.isclose()' to compare floating-point numbers instead of '==' due to precision issues.

def number_advanced():
    """Demonstrates advanced concepts related to numbers in Python."""
    
    # Decimal for precise decimal representations
    from decimal import Decimal, getcontext  # Decimal offers precise control over floating-point arithmetic
    getcontext().prec = 6  # Setting the precision to 6 decimal places for all Decimal operations
    d = Decimal('1.1') + Decimal('2.2')  # Using strings to avoid floating-point inaccuracies
    print(f"Decimal: {d}")  # Outputs: 3.3 instead of the imprecise 3.3000000000000003 seen with floats

    # Best Practice: Always use Decimal for financial applications to avoid rounding errors.

    # Fraction for rational numbers
    from fractions import Fraction  # Fraction module handles rational numbers as exact fractions
    f = Fraction(1, 3) + Fraction(1, 6)  # Adding two fractions directly
    print(f"Fraction: {f}")  # Outputs: 1/2, retaining the exact fractional value
    
    # Bitwise operations (only applicable to integers)
    # These are low-level operations often used in systems programming, cryptography, or for optimizing certain calculations
    print(f"Bitwise AND: {5 & 3}")  # 5 (101 in binary) & 3 (011 in binary) = 1 (001)
    print(f"Bitwise OR: {5 | 3}")   # 5 | 3 = 7 (111 in binary)
    print(f"Bitwise XOR: {5 ^ 3}")  # 5 ^ 3 = 6 (110 in binary)
    print(f"Bitwise NOT: {~5}")     # ~5 = -6 (Inverts all bits, equivalent to -(n + 1))
    print(f"Left Shift: {5 << 1}")  # Shifts bits left by 1 position, effectively multiplying by 2
    print(f"Right Shift: {5 >> 1}") # Shifts bits right by 1 position, effectively dividing by 2
    
    # Advanced Tip: Bitwise operations can be used to optimize certain algorithms (e.g., multiplication/division by powers of 2).

def string_basics():
    """Demonstrates basic concepts related to strings in Python."""
    
    # String creation
    s1 = 'Single quotes'  # Using single quotes for string literals
    s2 = "Double quotes"  # Using double quotes (no functional difference in Python)
    s3 = '''Triple quotes for
    multiline strings'''  # Triple quotes allow for multi-line strings
    
    print(f"s1: {s1}\ns2: {s2}\ns3: {s3}")  # Demonstrating various string assignments
    
    # String operations
    s = "Hello, World!"  # Defining a sample string
    print(f"Length: {len(s)}")  # len() returns the length of the string
    print(f"Uppercase: {s.upper()}")  # Converts all characters to uppercase
    print(f"Lowercase: {s.lower()}")  # Converts all characters to lowercase
    print(f"Capitalize: {s.capitalize()}")  # Capitalizes the first character of the string
    print(f"Index of 'World': {s.index('World')}")  # Finds the starting index of the substring 'World'
    print(f"Replace: {s.replace('World', 'Python')}")  # Replaces 'World' with 'Python'

    # String formatting
    name = "Alice"
    age = 30
    print("Old style: %s is %d years old" % (name, age))  # Old-style formatting using '%' (C-style)
    print("New style: {} is {} years old".format(name, age))  # New-style formatting using str.format()
    print(f"f-string: {name} is {age} years old")  # f-strings (Python 3.6+) offer a more readable and efficient way to format strings
    
    # Advanced Tip: Use f-strings for better performance and readability over older formatting methods.
    # Potential Pitfall: Avoid using mutable sequences like lists within f-strings, as their state could change unexpectedly.

# ========================================
# Explanation and Insights
# ---------------------------------
# This segment offers a comprehensive look at Python's core data types, highlighting key differences, common pitfalls, 
# and advanced usage patterns that can help in writing efficient, maintainable code. 

# Important: Understanding how Python handles these basic data types lays the groundwork for mastering 
# more complex data structures and algorithms.
# ========================================

def string_advanced():
    """Demonstrates advanced concepts related to strings in Python."""
    
    # Regular expressions (regex) allow complex pattern matching and manipulation of strings.
    # `re` is the standard module for handling regex in Python.
    import re  # Importing the regular expression module
    
    text = "The quick brown fox jumps over the lazy dog"  # Sample string
    
    # Regex pattern explanation:
    # - `\b`: Word boundary, ensures we match whole words only.
    # - `\w{5}`: Matches exactly 5 word characters (alphanumeric + underscore).
    # Thus, the pattern captures words with exactly 5 characters.
    pattern = r'\b\w{5}\b'  
    matches = re.findall(pattern, text)  # Finds all occurrences matching the pattern
    
    # Printing words that have exactly 5 characters
    print(f"Words with 5 characters: {matches}")

    # ========================================================
    # Unicode and encoding: Demonstrating how Python handles Unicode strings
    # --------------------------------------------------------
    unicode_string = "Hello, 世界"  # A string containing both ASCII and non-ASCII characters
    
    # Encoding converts a string into bytes; UTF-8 is the most common encoding in Python
    utf8_encoded = unicode_string.encode('utf-8')
    
    # Displaying the UTF-8 encoded byte representation
    print(f"UTF-8 encoded: {utf8_encoded}")
    
    # Decoding converts bytes back to a string; this should match the original if correctly decoded
    print(f"Decoded back: {utf8_encoded.decode('utf-8')}")

    # Best Practice: Always specify encoding explicitly (e.g., `utf-8`) to avoid ambiguity, especially in
    # environments where the default encoding may differ.
    
    # ========================================================
    # String methods for data cleaning
    # --------------------------------------------------------
    dirty_string = "  Some\twhitespace\nand\nnewlines\t"  # Example string with inconsistent whitespace
    
    # `strip()` removes leading and trailing whitespace, including spaces, tabs (`\t`), and newlines (`\n`).
    # `replace()` is used here to replace tabs and newlines with single spaces for better readability.
    clean_string = dirty_string.strip().replace('\t', ' ').replace('\n', ' ')
    
    # Displaying the cleaned version of the string
    print(f"Cleaned string: '{clean_string}'")

    # Advanced Tip: Consider using `re.sub()` for more complex cleaning operations, as it provides regex
    # substitution capabilities, making it more powerful for intricate text transformations.
    
# ----------------------------------------

def boolean_basics():
    """Demonstrates basic concepts related to booleans in Python."""
    
    # Boolean values in Python
    # `True` and `False` are the two boolean literals, representing truth values.
    t = True  # Boolean true
    f = False  # Boolean false
    
    # Displaying basic boolean values
    print(f"t: {t}, f: {f}")

    # ========================================================
    # Logical operations: Core operations that form the basis of boolean logic
    # --------------------------------------------------------
    # AND operation: True only if both operands are true
    print(f"AND: {t and f}")  # Expected output: False
    
    # OR operation: True if at least one operand is true
    print(f"OR: {t or f}")  # Expected output: True
    
    # NOT operation: Inverts the boolean value
    print(f"NOT: {not t}")  # Expected output: False
    
    # Note: Logical operations are short-circuiting in Python, meaning evaluation stops as soon as the result is determined.
    # E.g., in `t or f`, since `t` is True, Python doesn't evaluate `f`.

    # ========================================================
    # Comparison operations: Used to compare values and yield boolean results
    # --------------------------------------------------------
    x = 5
    y = 10
    
    # Equality check
    print(f"Equal: {x == y}")  # False, as 5 is not equal to 10
    
    # Inequality check
    print(f"Not Equal: {x != y}")  # True, as 5 is not equal to 10
    
    # Greater than comparison
    print(f"Greater Than: {x > y}")  # False, as 5 is not greater than 10
    
    # Less than comparison
    print(f"Less Than: {x < y}")  # True, as 5 is less than 10
    
    # Greater than or equal comparison
    print(f"Greater Than or Equal: {x >= y}")  # False, as 5 is not greater or equal to 10
    
    # Less than or equal comparison
    print(f"Less Than or Equal: {x <= y}")  # True, as 5 is indeed less than or equal to 10

    # Advanced Insight: 
    # - All objects in Python have an inherent truthiness; e.g., empty sequences (like `[]`, `''`) and `None` are `False`.
    # - Non-zero numbers and non-empty sequences are `True`. Understanding this can aid in writing more idiomatic Python.
    
    # Example: Using a list's truthiness
    example_list = []
    if example_list:
        print("List is not empty")
    else:
        print("List is empty")  # This will execute since `example_list` is an empty list and evaluates to False.
    
    # Performance Tip: Using direct comparisons (e.g., `if len(list) > 0`) is slower and less Pythonic compared to relying
    # on the truthiness of objects. Prefer `if example_list:` over `if len(example_list) > 0` when checking for non-emptiness.


def boolean_advanced():
    """Demonstrates advanced concepts related to booleans in Python."""

    # Short-circuit evaluation
    # ------------------------
    # Short-circuiting is a fundamental concept in Boolean logic that optimizes code execution:
    # - For the `and` operator: If the left operand evaluates to False, Python doesn't evaluate the right operand since the overall expression is already False.
    # - For the `or` operator: If the left operand evaluates to True, Python skips evaluating the right operand since the entire expression will be True.
    
    def true_func():
        print("true_func called")  # This function prints a message when called, demonstrating that it gets invoked.
        return True  # Always returns True
    
    def false_func():
        print("false_func called")  # This function prints a message when called, demonstrating that it gets invoked.
        return False  # Always returns False
    
    # Demonstrating Short-circuit AND
    print("Short-circuit AND:")
    result = false_func() and true_func()
    print(f"Result: {result}")
    
    # Explanation:
    # - `false_func()` returns False, and due to short-circuiting, `true_func()` is never called.
    # - This behavior optimizes performance and prevents unnecessary computations.
    
    # Demonstrating Short-circuit OR
    print("\nShort-circuit OR:")
    result = true_func() or false_func()
    print(f"Result: {result}")
    
    # Explanation:
    # - `true_func()` returns True, and as a result, `false_func()` is never called.
    # - The `or` expression short-circuits, skipping further evaluation.

    # Boolean Algebra Example
    # -----------------------
    # Boolean algebra forms the foundation of logic gates in computer science, crucial for building complex logical expressions.
    from itertools import product  # Importing `product` from itertools to generate Cartesian product of inputs (True/False pairs)

    def boolean_algebra_example():
        # Iterate over all combinations of p and q using product, which creates all possible pairs of (False, True)
        for p, q in product([False, True], repeat=2):
            print(f"p: {p}, q: {q}")  # Display the current pair (p, q)
            print(f"  p AND q: {p and q}")  # Logical AND: True only if both p and q are True
            print(f"  p OR q: {p or q}")  # Logical OR: True if either p or q is True
            print(f"  NOT p: {not p}")  # Logical NOT: Inverts the value of p
            print(f"  p XOR q: {p ^ q}")  # Exclusive OR (XOR): True if p and q are different
    
    # Calling the boolean algebra demonstration function
    boolean_algebra_example()

# ========================================
# Advanced Tips and Insights:
# ---------------------------------
# 1. Short-circuiting isn't just an optimization technique; it can be a powerful tool to prevent errors:
#    Example: `if divisor != 0 and numerator / divisor > 1:` 
#    Here, `divisor != 0` ensures that the division by zero never occurs due to short-circuit evaluation.
#
# 2. Avoid side effects in Boolean expressions:
#    If the function has side effects (e.g., modifying global state or performing I/O), using them in short-circuit logic 
#    can make code harder to understand and debug.
#
# 3. XOR (`p ^ q`) is often less familiar to newcomers but extremely useful in scenarios where you want to enforce
#    "one or the other, but not both" conditions. It's also foundational in cryptography and parity checks.
#
# Potential Pitfalls:
# -------------------
# - Using functions with side effects in Boolean operations can introduce bugs if short-circuiting alters expected behavior.
# - Overusing `not` can make conditions harder to read. Consider rewriting `not (p and q)` as `not p or not q` using De Morgan's law.
#
# Alternative Approaches:
# -----------------------
# - For more complex Boolean logic, consider using `operator` module functions (`operator.and_`, `operator.or_`) for clarity
#   or if you need to pass these operations as first-class functions.
# - In contexts requiring many Boolean evaluations, like large datasets, NumPy's vectorized operations offer significant
#   performance improvements over native Python.
# ========================================


# ========================================
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# ---------------------------------
import unittest  # Standard library module used for unit testing; essential for writing maintainable, testable code

def best_practices():
    """Demonstrates best practices for working with numbers, strings, and booleans."""
    
    # Use meaningful variable names to improve code readability and maintainability.
    # This is crucial in larger codebases, where single-letter variable names can cause confusion.
    user_age = 25  # Good: descriptive variable name that conveys its purpose
    a = 25  # Avoid: non-descriptive, hard to understand in larger scopes

    # Use f-strings (formatted string literals) for string formatting (Python 3.6+).
    # They are more readable, efficient, and less error-prone compared to older methods like `%` or `str.format()`.
    name = "Alice"
    print(f"Hello, {name}!")  # f-strings offer clearer syntax and improved performance

    # Use context managers (`with` statement) for handling file operations.
    # Ensures proper resource management by automatically closing the file, even if an error occurs within the block.
    with open('example.txt', 'w') as f:
        f.write('Hello, World!')  # The file is properly closed after this block, reducing the risk of file corruption

    # Always use `try-except` blocks for error handling in situations where exceptions are anticipated.
    # This prevents the program from crashing and allows for graceful error recovery.
    try:
        result = 10 / 0  # Attempting to divide by zero
    except ZeroDivisionError:
        print("Cannot divide by zero")  # Properly handles the error instead of causing a program crash

    # Use the `in` operator for membership testing instead of iterating through lists.
    # This is both more efficient and more readable.
    fruits = ['apple', 'banana', 'cherry']
    if 'apple' in fruits:  # Efficient O(n) operation; use sets for O(1) average time complexity if needed
        print("Apple is in the list")

# ================================================================
# Potential Pitfall: Directly iterating through elements without `in`
# can be inefficient, especially for larger data structures.
# When working with larger datasets, consider using sets for O(1) 
# membership tests instead of lists, which have O(n) complexity.
# ================================================================

def common_pitfalls():
    """Highlights common pitfalls when working with numbers, strings, and booleans."""
    
    # Floating-point precision issues:
    # Due to how floating-point numbers are represented in memory, the result may not be exact.
    # This is a common issue across many programming languages, not just Python.
    print(0.1 + 0.2 == 0.3)  # False, even though mathematically expected to be True

    # Solution: Use `math.isclose()` for comparisons involving floating-point numbers
    import math
    print(math.isclose(0.1 + 0.2, 0.3))  # True; preferred way to handle floating-point precision comparisons

    # Mutable default arguments: One of the most infamous Python pitfalls
    # Lists (and other mutable objects) used as default arguments retain their state between function calls.
    def append_to(element, lst=[]):  # Dangerous! The default list persists across calls
        lst.append(element)
        return lst

    print(append_to(1))  # Output: [1]
    print(append_to(2))  # Output: [1, 2], not [2] as might be expected

    # Best Practice: Use `None` as the default argument and initialize inside the function
    def append_to_safe(element, lst=None):
        if lst is None:
            lst = []
        lst.append(element)
        return lst

    # String concatenation in loops
    # Inefficient method: Using `+=` creates new string objects on each iteration, leading to O(n^2) time complexity
    def bad_string_concat(n):
        result = ""
        for i in range(n):
            result += str(i)  # Inefficient; strings are immutable
        return result

    # Efficient method: Using `str.join()` for concatenation, which has O(n) complexity
    def good_string_concat(n):
        return ''.join(str(i) for i in range(n))

# ================================================================
# Advanced Tip: When dealing with large collections of strings, 
# consider using `io.StringIO` for even greater efficiency.
# ================================================================

def advanced_tips():
    """Provides advanced tips for working with numbers, strings, and booleans."""
    
    # Using `decimal.Decimal` for financial calculations to avoid floating-point precision issues
    from decimal import Decimal, getcontext
    getcontext().prec = 2  # Set precision to 2 decimal places for all Decimal operations
    print(Decimal('0.1') + Decimal('0.2'))  # Accurate financial calculation

    # String interning: Python automatically interns some strings (e.g., small strings or those with only ASCII letters)
    # Interning means reusing objects for identical strings, thus improving memory efficiency
    a = 'hello'
    b = 'hello'
    print(a is b)  # True: Points to the same object in memory

    # Custom string representations for objects
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self):
            return f"{self.name} ({self.age})"  # User-friendly string representation

        def __repr__(self):
            return f"Person('{self.name}', {self.age})"  # Developer-friendly, unambiguous representation

    person = Person("Alice", 30)
    print(str(person))  # End-user-friendly output: "Alice (30)"
    print(repr(person))  # Developer output: "Person('Alice', 30)"

    # Boolean as int: In Python, `True` and `False` can be used in arithmetic expressions (1 and 0 respectively)
    print(True + True)  # Output: 2
    print(False * 10)   # Output: 0

def write_testable_code():
    """Demonstrates how to write testable code for numbers, strings, and booleans."""

    def is_palindrome(s: str) -> bool:
        """Check if a string is a palindrome."""
        s = ''.join(c.lower() for c in s if c.isalnum())  # Removes non-alphanumeric characters and converts to lowercase
        return s == s[::-1]  # Compares string to its reverse

    class TestPalindrome(unittest.TestCase):
        def test_palindrome(self):
            # Test cases to ensure the function behaves correctly
            self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))  # Classic palindrome example
            self.assertFalse(is_palindrome("hello"))  # Not a palindrome
            self.assertTrue(is_palindrome(""))  # Edge case: empty string
            self.assertFalse(is_palindrome("Race a car"))  # Case insensitive check

    # Running unit tests, keeping `unittest.main` call compatible with Jupyter notebooks and scripts
    unittest.main(argv=[''], exit=False)

# ========================================
# Advanced Tip: Always aim for high test coverage, especially for edge cases. 
# Testing ensures code reliability and robustness, which is crucial as you advance toward senior/principal engineer roles.
# ========================================


# ========================================
# 4. Integration and Real-World Applications
# -----------------------------------------
# This section demonstrates how Python's basic data types (numbers, strings, booleans) can be
# integrated into real-world applications such as data analysis and web scraping.
# These examples provide practical insights into how foundational data types are used 
# in more complex operations.
# ========================================

def data_analysis_example():
    """Demonstrates use of numbers, strings, and booleans in data analysis."""
    import statistics  # Standard library module for basic statistical operations (e.g., mean, median, mode)

    # Sample data
    data = [
        {"name": "Alice", "age": 25, "salary": 50000},
        {"name": "Bob", "age": 30, "salary": 60000},
        {"name": "Charlie", "age": 35, "salary": 70000},
    ]
    
    # ========================================
    # Extracting ages and salaries for analysis
    # ----------------------------------------
    # Here, we extract the ages and salaries using list comprehensions, a Pythonic way to transform
    # collections. This approach is both efficient and concise.
    # ========================================
    
    ages = [person["age"] for person in data]  # Extracts ages from each dictionary in the list
    salaries = [person["salary"] for person in data]  # Extracts salaries similarly

    # Calculate average age and total salary
    avg_age = statistics.mean(ages)  # Using `statistics.mean` for clarity and precision
    total_salary = sum(salaries)  # Using built-in `sum()` for performance and readability

    # Output the results using formatted strings
    print(f"Average age: {avg_age:.2f}")  # `:.2f` ensures the average age is formatted to 2 decimal places
    print(f"Total salary: ${total_salary:,}")  # `:,` adds commas as thousand separators, enhancing readability

    # ========================================
    # Identifying high earners
    # ----------------------------------------
    # This demonstrates the use of conditional logic (boolean expressions) within a list comprehension.
    # Advanced Tip: List comprehensions are often faster than traditional loops due to internal optimizations.
    # ========================================
    high_earners = [person["name"] for person in data if person["salary"] > 55000]
    print(f"High earners: {', '.join(high_earners)}")  # Joining names into a comma-separated string for display

    # ========================================
    # Best Practices and Potential Pitfalls:
    # ----------------------------------------
    # - List comprehensions are not only concise but often more performant than equivalent `for` loops.
    # - Always validate data before processing in real-world scenarios. Here, it's assumed all data is valid.
    # - Use `statistics.mean` over manually computing the average (`sum / len`) for improved readability and error handling.
    # ========================================

# -----------------------------------------
# Web Scraping Example
# -----------------------------------------
# This function simulates a basic web scraping scenario where product details are extracted from HTML content.
# It showcases how regular expressions (`re` module) and basic data types work together for parsing.
# ========================================

def web_scraping_example():
    """Simulates web scraping using numbers, strings, and booleans."""
    import re  # Regular expressions are powerful for pattern matching, although they can be complex and error-prone if misused

    # Simulated HTML content
    html_content = """
    <div class="product">
        <h2>Laptop X</h2>
        <p class="price">$999.99</p>
        <p class="stock">In stock</p>
    </div>
    <div class="product">
        <h2>Smartphone Y</h2>
        <p class="price">$599.99</p>
        <p class="stock">Out of stock</p>
    </div>
    """

    # ========================================
    # Regular Expression Pattern
    # ----------------------------------------
    # The `re.findall` method is used here to extract all matching patterns. The `.*?` is a non-greedy match,
    # meaning it matches the shortest possible string that fits the pattern. This is essential for parsing HTML.
    # ========================================
    pattern = r'<h2>(.*?)</h2>.*?<p class="price">\$(.*?)</p>.*?<p class="stock">(.*?)</p>'
    matches = re.findall(pattern, html_content, re.DOTALL)  # `re.DOTALL` allows `.` to match newlines as well

    # Processing the extracted product information
    for name, price, stock in matches:
        price = float(price)  # Convert the extracted string price to a float for numerical operations
        in_stock = stock.lower() == "in stock"  # Converts stock status to a boolean value for logical checks
        print(f"Product: {name}, Price: ${price:.2f}, In Stock: {in_stock}")  # Displaying the parsed data

    # ========================================
    # Best Practices and Potential Pitfalls:
    # ----------------------------------------
    # - Regular expressions are powerful but can become unreadable for complex patterns. Commenting patterns or
    #   using verbose mode (`re.VERBOSE`) can improve readability.
    # - HTML is inherently hierarchical; using libraries like BeautifulSoup or lxml is often more robust for
    #   complex scraping tasks.
    # - Always handle edge cases: e.g., missing or malformed HTML elements can cause unexpected behavior.
    #   Consider adding error handling or validation.
    # 
    # Advanced Tip: Use `try-except` blocks around `float(price)` to handle potential conversion errors gracefully.
    # - Example: What if the price contains non-numeric characters or is empty?
    # ========================================


# ========================================
# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
def advanced_concepts():
    """Explores advanced concepts and emerging trends related to numbers, strings, and booleans."""

    # F-strings with '=' for debugging (Python 3.8+)
    # --------------------------------------------------------
    x = 10
    y = 20
    # The syntax `f"{x=}"` is an enhanced feature of f-strings introduced in Python 3.8.
    # It displays both the variable name and its value, making it extremely useful for debugging.
    # Output: 'x=10, y=20'
    print(f"{x=}, {y=}")

    # Advanced Tip: F-strings are faster and more readable than other string formatting methods
    # like `%` or `.format()`, and they should be preferred whenever possible.

    # The Walrus operator (:=) introduced in Python 3.8+
    # --------------------------------------------------------
    # The Walrus operator allows assignment and evaluation in a single expression, making the code more concise.
    # This can be particularly beneficial in situations where you want to avoid repeated calculations.
    if (n := len([1, 2, 3])) > 2:
        # Here, `n` is assigned the length of the list, and the expression is immediately evaluated in the `if` condition.
        # Output: 'List has 3 items'
        print(f"List has {n} items")

    # Caution: Overusing the Walrus operator can make code less readable, especially for complex expressions.
    # Use it judiciously to avoid compromising code clarity.

    # Math and statistics modules
    # --------------------------------------------------------
    import math
    import statistics

    numbers = [1, 2, 3, 4, 5]
    # `math.fsum` provides a more precise floating-point summation, ideal for summing large lists of floats
    # where precision is crucial. It avoids precision loss that can occur with the built-in `sum`.
    print(f"Sum: {math.fsum(numbers)}")

    # `statistics.median` computes the median, providing an accurate measure of central tendency for data.
    # Output: 'Median: 3'
    print(f"Median: {statistics.median(numbers)}")

    # Best Practice: Use `math` and `statistics` modules instead of implementing mathematical functions manually
    # to leverage built-in optimizations and ensure accuracy.

    # String methods for handling whitespace
    # --------------------------------------------------------
    text = "  hello   world  "
    # `strip()`, `lstrip()`, and `rstrip()` handle leading/trailing whitespace removal effectively.
    # They are faster and more readable than using regex for simple whitespace handling.
    print(f"Stripped: '{text.strip()}'")      # Removes leading and trailing spaces
    print(f"Left stripped: '{text.lstrip()}'")  # Removes leading spaces only
    print(f"Right stripped: '{text.rstrip()}'") # Removes trailing spaces only

    # Potential Pitfall: These methods only remove whitespace (or specified characters), not internal spaces.
    # To remove all extra spaces, consider using `split()` followed by `join()`:
    # Example: ' '.join(text.split())

    # Advanced string formatting
    # --------------------------------------------------------
    person = {'name': 'Alice', 'age': 30}
    # The `.format(**person)` syntax allows unpacking of dictionaries for string formatting.
    # It improves readability when dealing with multiple variables.
    print("Name: {name}, Age: {age}".format(**person))

    # Advanced Tip: Use f-strings for even more concise and efficient formatting in Python 3.6+:
    # e.g., `print(f"Name: {person['name']}, Age: {person['age']}")`

    # Boolean operations with any() and all()
    # --------------------------------------------------------
    numbers = [1, 2, 3, 4, 5]
    # `any()` returns True if at least one element in the iterable evaluates to True.
    print(f"Any number > 3: {any(n > 3 for n in numbers)}")  # Output: True

    # `all()` returns True only if all elements in the iterable evaluate to True.
    print(f"All numbers > 0: {all(n > 0 for n in numbers)}")  # Output: True

    # Best Practice: Use `any()` and `all()` for efficient membership testing and logical checks
    # rather than using manual loops for better readability and performance.

    # Advanced string operations
    # --------------------------------------------------------
    import textwrap
    long_text = "This is a very long string that we want to wrap to multiple lines without breaking words."
    # `textwrap.fill()` wraps the text to the specified width, ensuring that words aren't split.
    wrapped_text = textwrap.fill(long_text, width=30)
    print(f"Wrapped text:\n{wrapped_text}")

    # Best Practice: Use `textwrap` for cleanly formatting long strings, especially in text-based UIs or reports.

    # Unicode normalization
    # --------------------------------------------------------
    import unicodedata
    s1 = 'café'          # Directly typed string with an accent
    s2 = 'cafe\u0301'    # Unicode representation with 'e' + combining acute accent

    # Although visually identical, these two strings are different due to different Unicode representations.
    print(f"s1 == s2: {s1 == s2}")  # Output: False

    # Normalizing strings to a canonical form (NFC) makes them directly comparable.
    print(f"Normalized s1 == s2: {unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2)}")
    # Output: True

    # Advanced Tip: Always normalize Unicode strings in applications that require consistent text comparison,
    # like database keys or user input validation, to avoid subtle bugs.

    # Advanced numeric operations
    # --------------------------------------------------------
    import cmath  # For complex number operations; complements `math` for handling real numbers
    z = 1 + 2j    # Define a complex number; `j` is the imaginary unit in Python

    # `cmath.phase(z)` returns the phase angle (in radians) of the complex number `z`.
    print(f"Phase of {z}: {cmath.phase(z)}")  # Output: Phase angle of the complex number in radians

    # `cmath.polar(z)` converts the complex number to polar coordinates (r, theta).
    print(f"Polar coordinates of {z}: {cmath.polar(z)}")  # Output: (r, theta) where r is the magnitude

    # Advanced Tip: Complex number operations are efficient with `cmath`. In contrast, languages like Java
    # or C++ require external libraries for complex arithmetic, demonstrating Python's strength in scientific computing.


# ========================================
# 6. FAQs and Troubleshooting
# ---------------------------------
def faqs_and_troubleshooting():
    """Addresses common questions and issues related to numbers, strings, and booleans with detailed explanations."""
    
    # --------------------------------------------------------------
    # Q: Why does 0.1 + 0.2 != 0.3?
    # --------------------------------------------------------------
    # Explanation:
    # This is one of the most well-known issues with floating-point arithmetic in Python (and many other languages).
    # Floating-point numbers are represented in binary, which cannot precisely represent some decimal fractions.
    # As a result, calculations like 0.1 + 0.2 yield a small error, leading to unexpected results.
    # Note: This is due to IEEE 754 standard, which defines the representation of floating-point numbers.

    result = 0.1 + 0.2
    print(f"0.1 + 0.2 == 0.3: {result == 0.3}")  # Expected: False
    print(f"Actual result of 0.1 + 0.2: {result}")  # Displays the actual result

    # Best Practice: Use the `decimal.Decimal` type when precision is required, especially for financial calculations.
    from decimal import Decimal
    precise_result = Decimal('0.1') + Decimal('0.2')
    print(f"Using Decimal for precise calculations: {precise_result == Decimal('0.3')} (Actual: {precise_result})")
    
    # --------------------------------------------------------------
    # Q: How do I convert between number types?
    # --------------------------------------------------------------
    x = 10  # Integer
    print(f"Int to float: {float(x)}")  # Converts integer to float (result: 10.0)

    y = 3.14  # Float
    print(f"Float to int: {int(y)}  # Note: This truncates, not rounds")  # Converts float to int (result: 3)

    # Advanced Tip: Converting with `int()` truncates towards zero. For proper rounding, use `round(y)` instead.
    print(f"Rounded float to int: {round(y)}")  # Output: 3

    # Potential Pitfall: Conversions to `int` from float always truncate, even for negative numbers.
    neg_y = -3.14
    print(f"Truncated negative float to int: {int(neg_y)}")  # Result: -3 (not -4)

    # --------------------------------------------------------------
    # Q: How do I handle encoding issues with strings?
    # --------------------------------------------------------------
    # Explanation:
    # By default, Python uses Unicode for strings (str type), which can represent a wide variety of characters.
    # However, encoding issues arise when converting these strings to bytes, especially if the encoding doesn't
    # support certain characters (e.g., ASCII cannot represent '世界').

    try:
        text = "Hello, 世界".encode('ascii')
    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")  # Expected: 'ascii' codec can't encode characters in position 7-8
        print("Solution: Use UTF-8 encoding for non-ASCII characters")  # UTF-8 supports all Unicode characters
        text = "Hello, 世界".encode('utf-8')
    
    print(f"Encoded text (UTF-8): {text}")

    # Advanced Tip: When dealing with external data sources, always specify encoding explicitly (e.g., `open(file, encoding='utf-8')`).
    # This prevents issues across different platforms with different default encodings.

    # --------------------------------------------------------------
    # Q: How do I check if a string contains only specific types of characters?
    # --------------------------------------------------------------
    s = "Hello123"
    print(f"Is alphanumeric: {s.isalnum()}")  # True, as the string contains only letters and numbers
    print(f"Is alphabetic: {s.isalpha()}")  # False, since digits are present
    print(f"Is numeric: {s.isnumeric()}")  # False, since it contains letters

    # Advanced Tip: `str.isdigit()` differs from `str.isnumeric()`:
    # - `isdigit()` returns True only if all characters are decimal digits.
    # - `isnumeric()` includes additional numeric characters like fractions or superscripts.
    
    # Potential Pitfall: `isnumeric()` and `isdigit()` may behave differently for non-Latin digits, e.g., Arabic numerals.

    # --------------------------------------------------------------
    # Q: How do I handle division by zero?
    # --------------------------------------------------------------
    # Explanation:
    # Division by zero raises a `ZeroDivisionError`, which is common when working with user input or unpredictable data.
    try:
        result = 1 / 0  # This will raise an exception
    except ZeroDivisionError:
        print("Caught division by zero error")
        result = float('inf')  # `float('inf')` is a convention to represent infinity in numerical calculations.
    
    print(f"Result: {result}")

    # Best Practice: Always validate denominators before performing division to avoid such errors.
    # For instance: if denominator != 0: perform division

    # Advanced Tip: Consider using the `math.isfinite()` function to handle infinities and NaN (Not-a-Number) values robustly.
    import math
    print(f"Is the result finite? {math.isfinite(result)}")  # Will return False for infinity

# Call the function to demonstrate FAQ examples
# faqs_and_troubleshooting()


# ========================================
# 7. Recommended Tools, Libraries, and Resources
# ---------------------------------

"""
Recommended tools and libraries for working with numbers, strings, and booleans:

1. NumPy: Efficient numerical computations
   - `pip install numpy`
   - Highly optimized for numerical operations involving large datasets, provides support for multi-dimensional arrays.
   - Ideal for tasks requiring vectorized operations, which are significantly faster than standard Python loops.

2. SymPy: Symbolic mathematics
   - `pip install sympy`
   - Excellent for tasks requiring symbolic computation, such as algebraic manipulations, calculus, and solving equations.
   - Useful for educational purposes or when working with mathematical models that require symbolic representation.

3. Pandas: Data manipulation and analysis
   - `pip install pandas`
   - Built on top of NumPy, it offers high-level data structures (DataFrame) and tools for data analysis and manipulation.
   - A go-to library for data analysis, time series, and handling structured data efficiently.

4. Regex (Regular Expressions): Advanced pattern matching
   - Built-in `re` module, no installation needed.
   - Provides powerful capabilities for string pattern matching, parsing, and text processing.
   - Commonly used for input validation, data extraction, and text manipulation.

5. Decimal: Precise decimal arithmetic
   - Built-in `decimal` module, no installation needed.
   - Ensures precision in arithmetic operations, making it highly suitable for financial applications where floating-point inaccuracies are unacceptable.
   - Configurable precision and rounding strategies, allowing control over arithmetic operations.

Resources for further learning:
- Python Official Documentation: https://docs.python.org/3/
  - The ultimate reference for Python's syntax, libraries, and features.
- "Fluent Python" by Luciano Ramalho
  - A comprehensive guide on Python's advanced features, best practices, and idiomatic usage.
- "Effective Python" by Brett Slatkin
  - Offers insights into writing high-quality, maintainable Python code with practical tips and techniques.
- Real Python website: https://realpython.com/
  - Provides tutorials, articles, and videos on various Python topics, ranging from beginner to advanced levels.
- PyData conference talks on YouTube
  - Covers advanced numerical operations, data analysis, and best practices in Python.

Advanced Tip: When working with numerical data, always prefer NumPy or Pandas over built-in data structures due to their optimized performance. Additionally, leverage vectorized operations (e.g., element-wise addition) instead of loops for better efficiency.
"""


# ================================================================
# 8. Performance Analysis and Optimization
# ---------------------------------------------------------------
def performance_analysis():
    """Demonstrates performance analysis and optimization techniques using various examples."""

    import timeit  # 'timeit' is a powerful tool for measuring execution time of code snippets

    # ========================================
    # Comparing String Concatenation Methods
    # --------------------------------------
    
    # '+' Concatenation: Common but inefficient for repeated operations due to immutable nature of strings.
    def concat_plus(n):
        s = ""
        for i in range(n):
            s += str(i)  # Each iteration creates a new string, leading to O(n^2) time complexity.
        return s

    # Best Practice: Use 'join' for concatenating strings in a loop.
    def concat_join(n):
        return ''.join(str(i) for i in range(n))  # Efficient O(n) time complexity since 'join' preallocates memory.

    n = 10000  # Number of iterations
    time_plus = timeit.timeit(lambda: concat_plus(n), number=100)  # Measures execution time for 100 runs
    time_join = timeit.timeit(lambda: concat_join(n), number=100)  # Measures execution time for 100 runs

    # Output the comparison results
    print(f"Time for '+' concatenation: {time_plus:.6f} seconds")
    print(f"Time for 'join' concatenation: {time_join:.6f} seconds")

    # ========================================
    # Insights:
    # - Using '+' for concatenation in loops can lead to significant performance degradation due to the immutability of strings.
    # - 'join()' is much faster for large-scale concatenation tasks because it efficiently allocates memory beforehand.

    # ========================================
    # Comparing Number Operations
    # --------------------------------------

    import numpy as np  # NumPy provides highly optimized numerical operations

    # Summation using a loop (imperative approach)
    def sum_loop(n):
        total = 0
        for i in range(n):
            total += i  # Incrementally adds, resulting in O(n) time complexity.
        return total

    # Summation using a comprehension (functional approach)
    def sum_comprehension(n):
        return sum(i for i in range(n))  # More Pythonic and can be faster than a manual loop.

    # NumPy-based summation (vectorized operation)
    def sum_numpy(n):
        return np.sum(np.arange(n))  # Highly optimized due to internal C-based implementation.

    n = 1000000  # Large number of iterations to measure performance
    time_loop = timeit.timeit(lambda: sum_loop(n), number=10)
    time_comprehension = timeit.timeit(lambda: sum_comprehension(n), number=10)
    time_numpy = timeit.timeit(lambda: sum_numpy(n), number=10)

    # Output the comparison results
    print(f"Time for loop sum: {time_loop:.6f} seconds")
    print(f"Time for comprehension sum: {time_comprehension:.6f} seconds")
    print(f"Time for numpy sum: {time_numpy:.6f} seconds")

    # ========================================
    # Insights:
    # - NumPy is significantly faster due to its use of vectorized operations and optimized C libraries.
    # - Use NumPy for numerical computations when handling large datasets to achieve substantial performance gains.

    # ========================================
    # Boolean Operations Performance
    # --------------------------------------

    # Manual loop to check if all elements are True
    def all_loop(iterable):
        for element in iterable:
            if not element:
                return False  # Early exit if any element is False
        return True

    # Built-in all() function: Python's optimized method for this task
    def all_builtin(iterable):
        return all(iterable)  # Efficient and implemented in C for better performance

    data = [True] * 1000000 + [False]  # Create a large dataset with mostly True values
    time_loop = timeit.timeit(lambda: all_loop(data), number=100)
    time_builtin = timeit.timeit(lambda: all_builtin(data), number=100)

    # Output the comparison results
    print(f"Time for loop all(): {time_loop:.6f} seconds")
    print(f"Time for builtin all(): {time_builtin:.6f} seconds")

    # ========================================
    # Insights:
    # - Python's built-in functions like 'all()' are typically optimized and faster than manually written loops.
    # - Whenever possible, leverage built-in functions to benefit from performance optimizations provided by the language's core implementation.
# ================================================================

# ========================================
# Main Function Entry Point
# ---------------------------------
# The `main()` function serves as the central point for running this script. It sequentially calls various 
# other functions that demonstrate different concepts related to Python's data types, best practices, 
# and advanced tips. This design promotes modularity, allowing each concept to be handled in its dedicated function.

def main():
    """Main function to demonstrate various concepts."""
    
    # Demonstrating Number Basics
    print("1. Number Basics:")  
    number_basics()  # Calls the function responsible for illustrating basic number operations and concepts
    
    # The `print` statements serve as clear separators between different sections when the script runs, 
    # improving readability in the console output. However, be aware that excessive use of `print` can 
    # clutter logs in larger projects. Consider structured logging for complex applications.
    
    # Demonstrating Advanced Number Concepts
    print("\n2. Number Advanced:")  
    number_advanced()  # Calls a more advanced exploration of number-related features
    
    # Demonstrating String Basics
    print("\n3. String Basics:")  
    string_basics()  # Calls the function that covers fundamental string operations
    
    # Demonstrating Advanced String Concepts
    print("\n4. String Advanced:")  
    string_advanced()  # Explores more complex string manipulations
    
    # Demonstrating Boolean Basics
    print("\n5. Boolean Basics:")  
    boolean_basics()  # Covers the fundamentals of Boolean data and logic
    
    # Demonstrating Advanced Boolean Concepts
    print("\n6. Boolean Advanced:")  
    boolean_advanced()  # Includes more intricate Boolean logic and operations
    
    # Presenting Best Practices
    print("\n7. Best Practices:")  
    best_practices()  # Highlights recommended practices for Python programming, which is critical for maintainability
    
    # Discussing Common Pitfalls
    print("\n8. Common Pitfalls:")  
    common_pitfalls()  # Details frequent mistakes developers encounter, helping to avoid them proactively
    
    # Providing Advanced Tips
    print("\n9. Advanced Tips:")  
    advanced_tips()  # Offers insights into more advanced, non-obvious techniques that elevate coding proficiency
    
    # Demonstrating Testable Code Principles
    print("\n10. Testable Code:")  
    write_testable_code()  # Illustrates principles of writing testable code, a cornerstone of reliable software development
    
    # Example of Data Analysis
    print("\n11. Data Analysis Example:")  
    data_analysis_example()  # Showcases data analysis in Python, likely leveraging libraries like pandas or NumPy
    
    # Example of Web Scraping
    print("\n12. Web Scraping Example:")  
    web_scraping_example()  # Demonstrates web scraping concepts, possibly using libraries like BeautifulSoup or Scrapy
    
    # Introducing Advanced Concepts
    print("\n13. Advanced Concepts:")  
    advanced_concepts()  # Discusses more sophisticated programming constructs or techniques
    
    # FAQs and Troubleshooting Section
    print("\n14. FAQs and Troubleshooting:")  
    faqs_and_troubleshooting()  # Addresses frequently asked questions and common troubleshooting techniques
    
    # Performance Analysis Example
    print("\n15. Performance Analysis:")  
    performance_analysis()  # Focuses on analyzing and optimizing code performance

# Advanced Insight:
# - The structure of `main()` serves as a Table of Contents, giving a clear, organized flow to the script's execution.
# - Each function encapsulates a different concept, demonstrating the importance of separation of concerns—a key principle 
#   in software engineering.
# - The script employs `if __name__ == "__main__": main()`, which ensures that `main()` is only executed when the script is run directly, 
#   not when imported as a module in another script. This is a best practice in Python and allows for the code to be reused 
#   and integrated into larger systems.
# ========================================

# Entry Point Check
if __name__ == "__main__":
    # The `if __name__ == "__main__":` construct acts as a safeguard. This conditional check ensures that the `main()` 
    # function is executed only when this script is run directly, not when imported elsewhere.
    # This is particularly useful for creating reusable modules that can serve both as standalone scripts and as 
    # libraries for other projects.
    main()
    
# ========================================
# Additional Best Practices:
# ---------------------------------
# 1. Modularization: Each section of functionality (number basics, string basics, etc.) is encapsulated in its 
#    own function, adhering to the Single Responsibility Principle (SRP). This makes the codebase easier to maintain, 
#    test, and extend.
#
# 2. Clarity in Output: Using `print("\nSection Name:")` before calling each function makes the output more readable 
#    when the script is run. In larger projects, consider using logging frameworks with different log levels (DEBUG, INFO, WARNING, etc.).
#
# 3. Scalability: This structure allows for easy expansion. For instance, new sections or concepts can be added 
#    without disrupting existing code, making the codebase more robust to change.
#
# Potential Pitfall:
# - Avoid hard-coding too many `print()` statements if this function becomes more complex. Instead, consider 
#   dynamically generating the output based on function names or using dictionaries to map section titles to functions.
# ========================================


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

# End of cheat sheet