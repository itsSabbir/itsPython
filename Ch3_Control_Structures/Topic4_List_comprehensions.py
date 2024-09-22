"""
Control Structures - List comprehensions - in the Python Programming Language
=============================================================================

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization
9. How to Contribute

Author: Sabbir Hossain

1. Overview and Historical Context
----------------------------------
List comprehensions are a concise and powerful syntax for creating lists in Python.
They provide a way to generate new lists based on existing iterables or lists.

Key aspects:
- Introduced in Python 2.0 (2000)
- Inspired by set notation in mathematics
- Part of Python's effort to make code more readable and expressive

Historical context:
- Originated from Haskell's list comprehensions
- Adopted by Python to promote functional programming paradigms
- Evolved to include more complex forms (e.g., nested comprehensions)

Relevance in modern software development:
- Essential for data manipulation and transformation
- Widely used in data science and scientific computing
- Promotes functional programming style in Python

Comparison with other languages:
- Similar to list comprehensions in Haskell and Scala
- More concise than Java Streams or C# LINQ for simple operations
- Unique in its readability and integration with Python's syntax

List comprehensions have become an integral part of idiomatic Python, offering a 
balance between readability and conciseness for list creation and transformation tasks.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import time
import asyncio
from typing import List, Dict, Any
import random


def basic_list_comprehension():
    """
    Demonstrates basic list comprehension syntax and usage.
    """
    print("Basic list comprehension:")
    
    # Creating a list of squares
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")

    # Filtering even numbers
    even_numbers = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    # Combining operations
    odd_squares = [x**2 for x in range(10) if x % 2 != 0]
    print(f"Odd squares: {odd_squares}")

    print()


def nested_list_comprehension():
    """
    Demonstrates nested list comprehensions.
    """
    print("Nested list comprehension:")
    
    # Creating a 3x3 matrix
    matrix = [[i + 3*j for i in range(3)] for j in range(3)]
    print(f"3x3 Matrix: {matrix}")

    # Flattening a matrix
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")

    # Transpose of a matrix
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(f"Transposed matrix: {transposed}")

    print()


def list_comprehension_with_conditional_logic():
    """
    Demonstrates list comprehensions with complex conditional logic.
    """
    print("List comprehension with conditional logic:")
    
    # Using if-else in list comprehension
    numbers = [-4, -2, 0, 2, 4]
    abs_values = [x if x >= 0 else -x for x in numbers]
    print(f"Absolute values: {abs_values}")

    # Multiple conditions
    mixed = [1, 2, 'a', 3, 'b', 4]
    filtered = [x for x in mixed if isinstance(x, int) if x % 2 == 0]
    print(f"Even integers: {filtered}")

    # Nested conditions
    complex_list = [x if x % 2 == 0 else 
                    ('Even' if x % 3 == 0 else 'Odd') 
                    for x in range(10)]
    print(f"Complex conditional: {complex_list}")

    print()


def dict_and_set_comprehensions():
    """
    Demonstrates dictionary and set comprehensions.
    """
    print("Dictionary and set comprehensions:")
    
    # Dictionary comprehension
    squares_dict = {x: x**2 for x in range(5)}
    print(f"Squares dictionary: {squares_dict}")

    # Set comprehension
    unique_letters = {char for char in "hello world"}
    print(f"Unique letters: {unique_letters}")

    # Dictionary comprehension with conditional
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    print(f"Even squares dictionary: {even_squares}")

    print()


def generator_expressions():
    """
    Demonstrates generator expressions, a memory-efficient alternative to list comprehensions.
    """
    print("Generator expressions:")
    
    # Generator expression
    gen_squares = (x**2 for x in range(10))
    print(f"Generator object: {gen_squares}")
    print(f"Generated squares: {list(gen_squares)}")

    # Memory efficiency example
    import sys
    list_comp = [x for x in range(1000000)]
    gen_exp = (x for x in range(1000000))
    print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator expression size: {sys.getsizeof(gen_exp)} bytes")

    print()


def advanced_list_comprehension_patterns():
    """
    Demonstrates advanced patterns and use cases for list comprehensions.
    """
    print("Advanced list comprehension patterns:")
    
    # Handling exceptions in list comprehensions
    numbers = [1, 2, 0, 4, 5]
    reciprocals = [1/num if num != 0 else float('inf') for num in numbers]
    print(f"Reciprocals with exception handling: {reciprocals}")

    # List comprehension with enumerate
    indexed_squares = [(i, x**2) for i, x in enumerate(range(5))]
    print(f"Indexed squares: {indexed_squares}")

    # Combining multiple lists
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    combined = [(x, y) for x in list1 for y in list2]
    print(f"Combined lists: {combined}")

    print()


async def async_list_comprehension():
    """
    Demonstrates list comprehensions in an asynchronous context.
    """
    print("Asynchronous list comprehension:")
    
    async def fetch_data(x):
        await asyncio.sleep(0.1)  # Simulate an async operation
        return x * 2

    # Using list comprehension with async operations
    results = [await fetch_data(x) for x in range(5)]
    print(f"Async results: {results}")

    # Using asyncio.gather for concurrent execution
    results = await asyncio.gather(*[fetch_data(x) for x in range(5)])
    print(f"Concurrent async results: {results}")

    print()


def performance_comparison():
    """
    Compares performance of list comprehensions with alternative approaches.
    """
    print("Performance comparison:")
    
    # List comprehension vs for loop
    start_time = time.time()
    squares_comp = [x**2 for x in range(1000000)]
    comp_time = time.time() - start_time

    start_time = time.time()
    squares_loop = []
    for x in range(1000000):
        squares_loop.append(x**2)
    loop_time = time.time() - start_time

    print(f"List comprehension time: {comp_time:.6f} seconds")
    print(f"For loop time: {loop_time:.6f} seconds")
    print(f"List comprehension is {loop_time / comp_time:.2f}x faster")

    # Memory usage comparison
    import sys
    list_comp = [x for x in range(1000000)]
    gen_exp = (x for x in range(1000000))
    print(f"\nList comprehension size: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator expression size: {sys.getsizeof(gen_exp)} bytes")

    print()


def main():
    """
    Main function to demonstrate all concepts related to list comprehensions.
    """
    basic_list_comprehension()
    nested_list_comprehension()
    list_comprehension_with_conditional_logic()
    dict_and_set_comprehensions()
    generator_expressions()
    advanced_list_comprehension_patterns()
    asyncio.run(async_list_comprehension())
    performance_comparison()


if __name__ == "__main__":
    main()


"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use list comprehensions for simple, one-line operations.
2. Prefer readability over compactness; break complex comprehensions into multiple lines.
3. Use generator expressions for large datasets to conserve memory.
4. Avoid side effects in list comprehensions; keep them pure and functional.
5. Use meaningful variable names, even in short comprehensions.

Common Pitfalls:
1. Overusing list comprehensions, making code hard to read.
2. Creating nested comprehensions that are difficult to understand.
3. Using comprehensions for complex logic that would be clearer with a for loop.
4. Forgetting that comprehensions create new lists, potentially causing memory issues.

Advanced Tips:
1. Use walrus operator (:=) in Python 3.8+ for assignment expressions in comprehensions.
2. Combine comprehensions with the `zip()` function for parallel iteration.
3. Use `itertools` module functions within comprehensions for advanced operations.
4. Leverage type hinting for better code clarity and IDE support in comprehensions.

Testing List Comprehensions:
1. Use unit tests to verify the output of complex comprehensions.
2. Test edge cases, especially with conditional logic in comprehensions.
3. Use property-based testing (e.g., with the `hypothesis` library) for comprehensive tests.

Example unit test:
```python
import unittest

class TestListComprehensions(unittest.TestCase):
    def test_even_squares(self):
        result = [x**2 for x in range(10) if x % 2 == 0]
        self.assertEqual(result, [0, 4, 16, 36, 64])

    def test_empty_input(self):
        result = [x for x in [] if x > 0]
        self.assertEqual(result, [])

# Run the tests
unittest.main()
```

4. Integration and Real-World Applications
------------------------------------------
List comprehensions are widely used in various domains:

1. Data Science:
   - Data cleaning and transformation in pandas DataFrames
   - Feature engineering in machine learning pipelines

2. Web Development:
   - Parsing and transforming API responses
   - Generating HTML elements dynamically

3. System Administration:
   - File and directory operations
   - Log parsing and analysis

4. Financial Applications:
   - Calculating financial metrics for a series of transactions
   - Risk analysis and portfolio management

Example from Django ORM (simplified):
```python
active_users = [user for user in User.objects.all() if user.is_active]
```

5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous Comprehensions:
   - Introduced in Python 3.6 with PEP 530
   - Allows use of `async for` in comprehensions and generator expressions

2. Parallel Processing:
   - Using comprehensions with multiprocessing for parallel execution
   - Example: `results = [func(x) for x in Pool().map(process_item, data)]`

3. Integration with Other Python Features:
   - F-strings in comprehensions (Python 3.6+)
   - Type hinting in comprehensions (Python 3.6+)

4. Functional Programming Paradigms:
   - Combining comprehensions with `functools.reduce()` and `map()`
   - Using comprehensions in a point-free style programming

6. FAQs and Troubleshooting
---------------------------
Q: When should I use a list comprehension vs. a for loop?
A: Use list comprehensions for simple, one-line operations. For complex logic or when side effects are needed, use a for loop.

Q: How can I debug a list comprehension?
A: Break it down into a for loop, use print statements, or use Python's `pdb` debugger.

Q: Are list comprehensions always faster than for loops?
A: Generally yes, but for very simple operations, the difference is negligible. Always profile your code for performance-critical sections.

Troubleshooting:
- For `MemoryError`, consider using a generator expression instead.
- For unexpected results, check the logic and try breaking the comprehension into steps.
- Use `timeit` module to benchmark different implementations.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools:
- PyCharm: IDE with excellent support for refactoring and analyzing comprehensions
- Pylint: Static code analyzer that can help identify overly complex comprehensions

Libraries:
- itertools: Provides additional iteration-related tools
- more-itertools: Extended set of iteration utilities

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Effective Python" by Brett Slatkin
- Python official documentation: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

8. Performance Analysis and Optimization
----------------------------------------
- Use `timeit` module for accurate benchmarking of list comprehensions
- For large datasets, consider using generator expressions to reduce memory usage
- Profile memory usage using the `memory_profiler` library
- Consider using NumPy for numerical computations instead of list comprehensions for large datasets

Performance optimization strategies:
1. Use set comprehensions instead of list comprehensions when order doesn't matter and uniqueness is required
2. Avoid nested comprehensions for performance-critical code; use multiple steps instead
3. For very large datasets, consider using libraries like NumPy or Pandas which offer optimized operations

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
"""