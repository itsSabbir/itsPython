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

Author: Claude AI
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import math
import decimal
import fractions
import itertools
import re
import timeit
from typing import Union, List, Dict
import unittest

# 1. Overview and Historical Context
"""
Numbers, strings, and booleans are fundamental data types in Python, essential for representing
and manipulating data in programs.

Historical Context:
- Numbers: Python has supported integers and floating-point numbers since its inception.
  Complex numbers were added in Python 1.4 (1996).
- Strings: Initially only supported ASCII. Unicode support was added in Python 2.0 (2000).
  In Python 3, all strings are Unicode by default.
- Booleans: Introduced as a separate type in Python 2.3 (2003). Before that, 0 and empty containers
  were considered false, while all other values were true.

In modern software development, these types are crucial for:
- Data processing and analysis
- Text manipulation and natural language processing
- Logical operations and control flow
- Mathematical and scientific computing

Compared to other languages:
- Python's dynamic typing allows for more flexible use of these types compared to statically-typed languages.
- Python's string handling is generally more user-friendly than in languages like C.
- Python's boolean type is more explicit than in languages like C, where integers are used for boolean logic.
"""

# 2. Syntax, Key Concepts, and Code Examples

def number_basics():
    """Demonstrates basic concepts related to numbers in Python."""
    # Integer
    x = 10
    print(f"Integer: {x}, Type: {type(x)}")

    # Float
    y = 3.14
    print(f"Float: {y}, Type: {type(y)}")

    # Complex
    z = 1 + 2j
    print(f"Complex: {z}, Type: {type(z)}")

    # Boolean (subclass of int)
    b = True
    print(f"Boolean: {b}, Type: {type(b)}")

    # Basic arithmetic
    print(f"Addition: {x + y}")
    print(f"Subtraction: {x - y}")
    print(f"Multiplication: {x * y}")
    print(f"Division: {x / y}")  # Always returns a float
    print(f"Floor Division: {x // y}")  # Returns an int (or float if either operand is float)
    print(f"Modulo: {x % 3}")
    print(f"Exponentiation: {x ** 2}")

def number_advanced():
    """Demonstrates advanced concepts related to numbers in Python."""
    # Decimal for precise decimal representations
    from decimal import Decimal, getcontext
    getcontext().prec = 6
    d = Decimal('1.1') + Decimal('2.2')
    print(f"Decimal: {d}")

    # Fraction for rational numbers
    from fractions import Fraction
    f = Fraction(1, 3) + Fraction(1, 6)
    print(f"Fraction: {f}")

    # Bitwise operations
    print(f"Bitwise AND: {5 & 3}")
    print(f"Bitwise OR: {5 | 3}")
    print(f"Bitwise XOR: {5 ^ 3}")
    print(f"Bitwise NOT: {~5}")
    print(f"Left Shift: {5 << 1}")
    print(f"Right Shift: {5 >> 1}")

def string_basics():
    """Demonstrates basic concepts related to strings in Python."""
    # String creation
    s1 = 'Single quotes'
    s2 = "Double quotes"
    s3 = '''Triple quotes for
    multiline strings'''
    
    print(f"s1: {s1}\ns2: {s2}\ns3: {s3}")

    # String operations
    s = "Hello, World!"
    print(f"Length: {len(s)}")
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Capitalize: {s.capitalize()}")
    print(f"Index of 'World': {s.index('World')}")
    print(f"Replace: {s.replace('World', 'Python')}")

    # String formatting
    name = "Alice"
    age = 30
    print("Old style: %s is %d years old" % (name, age))
    print("New style: {} is {} years old".format(name, age))
    print(f"f-string: {name} is {age} years old")

def string_advanced():
    """Demonstrates advanced concepts related to strings in Python."""
    # Regular expressions
    import re
    text = "The quick brown fox jumps over the lazy dog"
    pattern = r'\b\w{5}\b'  # Words with exactly 5 characters
    matches = re.findall(pattern, text)
    print(f"Words with 5 characters: {matches}")

    # Unicode and encoding
    unicode_string = "Hello, 世界"
    utf8_encoded = unicode_string.encode('utf-8')
    print(f"UTF-8 encoded: {utf8_encoded}")
    print(f"Decoded back: {utf8_encoded.decode('utf-8')}")

    # String methods for data cleaning
    dirty_string = "  Some\twhitespace\nand\nnewlines\t"
    clean_string = dirty_string.strip().replace('\t', ' ').replace('\n', ' ')
    print(f"Cleaned string: '{clean_string}'")

def boolean_basics():
    """Demonstrates basic concepts related to booleans in Python."""
    # Boolean values
    t = True
    f = False
    print(f"t: {t}, f: {f}")

    # Logical operations
    print(f"AND: {t and f}")
    print(f"OR: {t or f}")
    print(f"NOT: {not t}")

    # Comparison operations
    x = 5
    y = 10
    print(f"Equal: {x == y}")
    print(f"Not Equal: {x != y}")
    print(f"Greater Than: {x > y}")
    print(f"Less Than: {x < y}")
    print(f"Greater Than or Equal: {x >= y}")
    print(f"Less Than or Equal: {x <= y}")

def boolean_advanced():
    """Demonstrates advanced concepts related to booleans in Python."""
    # Short-circuit evaluation
    def true_func():
        print("true_func called")
        return True

    def false_func():
        print("false_func called")
        return False

    print("Short-circuit AND:")
    result = false_func() and true_func()
    print(f"Result: {result}")

    print("\nShort-circuit OR:")
    result = true_func() or false_func()
    print(f"Result: {result}")

    # Boolean algebra
    from itertools import product
    def boolean_algebra_example():
        for p, q in product([False, True], repeat=2):
            print(f"p: {p}, q: {q}")
            print(f"  p AND q: {p and q}")
            print(f"  p OR q: {p or q}")
            print(f"  NOT p: {not p}")
            print(f"  p XOR q: {p ^ q}")
    
    boolean_algebra_example()

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def best_practices():
    """Demonstrates best practices for working with numbers, strings, and booleans."""
    # Use meaningful variable names
    user_age = 25  # Good
    a = 25  # Avoid single-letter names unless in very short scopes

    # Use f-strings for string formatting (Python 3.6+)
    name = "Alice"
    print(f"Hello, {name}!")

    # Use context managers for file operations
    with open('example.txt', 'w') as f:
        f.write('Hello, World!')

    # Use try-except for error handling
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")

    # Use in operator for membership testing
    fruits = ['apple', 'banana', 'cherry']
    if 'apple' in fruits:
        print("Apple is in the list")

def common_pitfalls():
    """Highlights common pitfalls when working with numbers, strings, and booleans."""
    # Floating point precision
    print(0.1 + 0.2 == 0.3)  # False, use math.isclose() instead

    # Mutable default arguments
    def append_to(element, lst=[]):  # Dangerous!
        lst.append(element)
        return lst

    print(append_to(1))  # [1]
    print(append_to(2))  # [1, 2], not [2]

    # String concatenation in loops
    def bad_string_concat(n):
        result = ""
        for i in range(n):
            result += str(i)  # Inefficient for large n
        return result

    def good_string_concat(n):
        return ''.join(str(i) for i in range(n))  # More efficient

    # Boolean trap
    def set_visibility(visible):  # Unclear at the call site
        pass

    def set_visibility_clear(is_visible: bool):  # Clear intention
        pass

def advanced_tips():
    """Provides advanced tips for working with numbers, strings, and booleans."""
    # Using decimal for financial calculations
    from decimal import Decimal, getcontext
    getcontext().prec = 2
    print(Decimal('0.1') + Decimal('0.2'))

    # String interning
    a = 'hello'
    b = 'hello'
    print(a is b)  # True, strings are interned

    # Custom string representations for objects
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self):
            return f"{self.name} ({self.age})"

        def __repr__(self):
            return f"Person('{self.name}', {self.age})"

    person = Person("Alice", 30)
    print(str(person))  # For end-users
    print(repr(person))  # For developers

    # Boolean as int
    print(True + True)  # 2
    print(False * 10)  # 0

def write_testable_code():
    """Demonstrates how to write testable code for numbers, strings, and booleans."""
    def is_palindrome(s: str) -> bool:
        """Check if a string is a palindrome."""
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]

    class TestPalindrome(unittest.TestCase):
        def test_palindrome(self):
            self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
            self.assertFalse(is_palindrome("hello"))
            self.assertTrue(is_palindrome(""))
            self.assertTrue(is_palindrome("Race a car"))

    unittest.main(argv=[''], exit=False)

# 4. Integration and Real-World Applications

def data_analysis_example():
    """Demonstrates use of numbers, strings, and booleans in data analysis."""
    import statistics

    # Sample data
    data = [
        {"name": "Alice", "age": 25, "salary": 50000},
        {"name": "Bob", "age": 30, "salary": 60000},
        {"name": "Charlie", "age": 35, "salary": 70000},
    ]

    # Calculate average age and total salary
    ages = [person["age"] for person in data]
    salaries = [person["salary"] for person in data]

    avg_age = statistics.mean(ages)
    total_salary = sum(salaries)

    print(f"Average age: {avg_age:.2f}")
    print(f"Total salary: ${total_salary:,}")

    # Find people with salary > 55000
    high_earners = [person["name"] for person in data if person["salary"] > 55000]
    print(f"High earners: {', '.join(high_earners)}")

def web_scraping_example():
    """Simulates web scraping using numbers, strings, and booleans."""
    import re

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

    # Extract product information
    pattern = r'<h2>(.*?)</h2>.*?<p class="price">\$(.*?)</p>.*?<p class="stock">(.*?)</p>'
    matches = re.findall(pattern, html_content, re.DOTALL)

    for name, price, stock in matches:
        price = float(price)
        in_stock = stock.lower() == "in stock"
        print(f"Product: {name}, Price: ${price:.2f}, In Stock: {in_stock}")

# 5. Advanced Concepts and Emerging Trends

def advanced_concepts():
    """Explores advanced concepts and emerging trends related to numbers, strings, and booleans."""
    # F-strings with '=' for debugging (Python 3.8+)
    x = 10
    y = 20
    print(f"{x=}, {y=}")

    # Walrus operator := (Python 3.8+)
    if (n := len([1, 2, 3])) > 2:
        print(f"List has {n} items")

    # Math and statistics modules
    import math
    import statistics

    numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {math.fsum(numbers)}")
    print(f"Median: {statistics.median(numbers)}")

    # String methods for handling whitespace
    text = "  hello   world  "
    print(f"Stripped: '{text.strip()}'")
    print(f"Left stripped: '{text.lstrip()}'")
    print(f"Right stripped: '{text.rstrip()}'")

    # Advanced string formatting
    person = {'name': 'Alice', 'age': 30}
    print("Name: {name}, Age: {age}".format(**person))

  # Boolean operations with any() and all()
    numbers = [1, 2, 3, 4, 5]
    print(f"Any number > 3: {any(n > 3 for n in numbers)}")
    print(f"All numbers > 0: {all(n > 0 for n in numbers)}")

    # Advanced string operations
    import textwrap
    long_text = "This is a very long string that we want to wrap to multiple lines without breaking words."
    wrapped_text = textwrap.fill(long_text, width=30)
    print(f"Wrapped text:\n{wrapped_text}")

    # Unicode normalization
    import unicodedata
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(f"s1 == s2: {s1 == s2}")
    print(f"Normalized s1 == s2: {unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2)}")

    # Advanced numeric operations
    import cmath  # for complex number operations
    z = 1 + 2j
    print(f"Phase of {z}: {cmath.phase(z)}")
    print(f"Polar coordinates of {z}: {cmath.polar(z)}")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to numbers, strings, and booleans."""
    
    # Q: Why does 0.1 + 0.2 != 0.3?
    print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")
    print("This is due to floating-point arithmetic limitations. Use Decimal for precise calculations.")

    # Q: How do I convert between number types?
    x = 10
    print(f"Int to float: {float(x)}")
    y = 3.14
    print(f"Float to int: {int(y)}  # Note: This truncates, not rounds")

    # Q: How do I handle encoding issues with strings?
    try:
        text = "Hello, 世界".encode('ascii')
    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")
        print("Solution: Use UTF-8 encoding for non-ASCII characters")
        text = "Hello, 世界".encode('utf-8')
    print(f"Encoded text: {text}")

    # Q: How do I check if a string contains only specific types of characters?
    s = "Hello123"
    print(f"Is alphanumeric: {s.isalnum()}")
    print(f"Is alphabetic: {s.isalpha()}")
    print(f"Is numeric: {s.isnumeric()}")

    # Q: How do I handle division by zero?
    try:
        result = 1 / 0
    except ZeroDivisionError:
        print("Caught division by zero error")
        result = float('inf')  # or handle it another way
    print(f"Result: {result}")

# 7. Recommended Tools, Libraries, and Resources

"""
Recommended tools and libraries for working with numbers, strings, and booleans:

1. NumPy: Efficient numerical computations
   pip install numpy

2. SymPy: Symbolic mathematics
   pip install sympy

3. Pandas: Data manipulation and analysis
   pip install pandas

4. Regex: Advanced regular expression operations
   Built-in 're' module, no installation needed

5. Decimal: Precise decimal arithmetic
   Built-in 'decimal' module, no installation needed

Resources for further learning:
- Python Official Documentation: https://docs.python.org/3/
- "Fluent Python" by Luciano Ramalho
- "Effective Python" by Brett Slatkin
- Real Python website: https://realpython.com/
- PyData conference talks on YouTube for advanced numerical operations
"""

# 8. Performance Analysis and Optimization

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques."""
    import timeit

    # String concatenation: '+' vs 'join'
    def concat_plus(n):
        s = ""
        for i in range(n):
            s += str(i)
        return s

    def concat_join(n):
        return ''.join(str(i) for i in range(n))

    n = 10000
    time_plus = timeit.timeit(lambda: concat_plus(n), number=100)
    time_join = timeit.timeit(lambda: concat_join(n), number=100)

    print(f"Time for '+' concatenation: {time_plus:.6f} seconds")
    print(f"Time for 'join' concatenation: {time_join:.6f} seconds")

    # Number operations: loop vs comprehension vs numpy
    import numpy as np

    def sum_loop(n):
        total = 0
        for i in range(n):
            total += i
        return total

    def sum_comprehension(n):
        return sum(i for i in range(n))

    def sum_numpy(n):
        return np.sum(np.arange(n))

    n = 1000000
    time_loop = timeit.timeit(lambda: sum_loop(n), number=10)
    time_comprehension = timeit.timeit(lambda: sum_comprehension(n), number=10)
    time_numpy = timeit.timeit(lambda: sum_numpy(n), number=10)

    print(f"Time for loop sum: {time_loop:.6f} seconds")
    print(f"Time for comprehension sum: {time_comprehension:.6f} seconds")
    print(f"Time for numpy sum: {time_numpy:.6f} seconds")

    # Boolean operations: all() vs loop
    def all_loop(iterable):
        for element in iterable:
            if not element:
                return False
        return True

    def all_builtin(iterable):
        return all(iterable)

    data = [True] * 1000000 + [False]
    time_loop = timeit.timeit(lambda: all_loop(data), number=100)
    time_builtin = timeit.timeit(lambda: all_builtin(data), number=100)

    print(f"Time for loop all(): {time_loop:.6f} seconds")
    print(f"Time for builtin all(): {time_builtin:.6f} seconds")

def main():
    """Main function to demonstrate various concepts."""
    print("1. Number Basics:")
    number_basics()

    print("\n2. Number Advanced:")
    number_advanced()

    print("\n3. String Basics:")
    string_basics()

    print("\n4. String Advanced:")
    string_advanced()

    print("\n5. Boolean Basics:")
    boolean_basics()

    print("\n6. Boolean Advanced:")
    boolean_advanced()

    print("\n7. Best Practices:")
    best_practices()

    print("\n8. Common Pitfalls:")
    common_pitfalls()

    print("\n9. Advanced Tips:")
    advanced_tips()

    print("\n10. Testable Code:")
    write_testable_code()

    print("\n11. Data Analysis Example:")
    data_analysis_example()

    print("\n12. Web Scraping Example:")
    web_scraping_example()

    print("\n13. Advanced Concepts:")
    advanced_concepts()

    print("\n14. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()

    print("\n15. Performance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()

# 9. How to Contribute

# To contribute to this cheat sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes or additions.
# 3. Ensure all code examples are correct and follow the established style.
# 4. Add comments explaining new concepts or functions.
# 5. Update the Table of Contents if necessary.
# 6. Submit a pull request with a clear description of your changes.

# Guidelines for contributions:
# - Maintain the current format and style.
# - Provide working code examples for new concepts.
# - Include performance considerations for new functions.
# - Add relevant references or citations for advanced topics.

# End of cheat sheet