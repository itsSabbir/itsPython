"""
Control Structures - Generator expressions - in the Python Programming Language
===============================================================================

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
Generator expressions are a concise and memory-efficient way to create iterators in Python.
They provide a way to generate values on-the-fly, without storing all values in memory at once.

Key aspects:
- Introduced in Python 2.4 (PEP 289)
- Designed to be a memory-efficient alternative to list comprehensions
- Part of Python's support for functional programming paradigms

Historical context:
- Inspired by generator functions, which were introduced in Python 2.2
- Developed to address memory usage issues with list comprehensions for large datasets
- Evolved alongside other functional programming features in Python

Relevance in modern software development:
- Essential for handling large datasets and streams
- Widely used in data processing pipelines
- Crucial for writing memory-efficient Python code

Comparison with other languages:
- Similar to lazy evaluation in functional languages like Haskell
- More concise than Java's Stream API for simple operations
- Unique in its integration with Python's iterator protocol

Generator expressions have become an integral part of idiomatic Python, offering a 
powerful tool for working with large or infinite sequences of data in a memory-efficient manner.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import time
import asyncio
from typing import List, Dict, Any, Generator
import sys
import itertools


def basic_generator_expression():
    """
    Demonstrates basic generator expression syntax and usage.
    """
    print("Basic generator expression:")
    
    # Creating a generator of squares
    squares_gen = (x**2 for x in range(10))
    print(f"Generator object: {squares_gen}")
    print(f"Generated squares: {list(squares_gen)}")

    # Using a generator expression in a function call
    sum_of_squares = sum(x**2 for x in range(10))
    print(f"Sum of squares: {sum_of_squares}")

    # Comparing with list comprehension
    squares_list = [x**2 for x in range(10)]
    print(f"List comprehension: {squares_list}")

    print()


def generator_expression_with_conditions():
    """
    Demonstrates generator expressions with conditions.
    """
    print("Generator expression with conditions:")
    
    # Filtering even numbers
    even_gen = (x for x in range(20) if x % 2 == 0)
    print(f"Even numbers: {list(even_gen)}")

    # Complex condition
    complex_gen = (x for x in range(100) if x % 3 == 0 and x % 5 == 0)
    print(f"Numbers divisible by 3 and 5: {list(complex_gen)}")

    # Ternary expression in generator
    sign_gen = ('Positive' if x > 0 else 'Negative' if x < 0 else 'Zero' for x in range(-5, 6))
    print(f"Sign of numbers: {list(sign_gen)}")

    print()


def nested_generator_expressions():
    """
    Demonstrates nested generator expressions.
    """
    print("Nested generator expressions:")
    
    # Creating a flattened generator from a nested structure
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_gen = (item for sublist in nested_list for item in sublist)
    print(f"Flattened list: {list(flattened_gen)}")

    # Creating a generator of generators
    matrix_gen = ((i + 3*j for i in range(3)) for j in range(3))
    print("Matrix generator:")
    for row in matrix_gen:
        print(list(row))

    print()


def generator_expression_vs_list_comprehension():
    """
    Compares generator expressions with list comprehensions.
    """
    print("Generator expression vs List comprehension:")
    
    # Memory usage comparison
    gen_exp = (x for x in range(1000000))
    list_comp = [x for x in range(1000000)]
    
    print(f"Generator expression size: {sys.getsizeof(gen_exp)} bytes")
    print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")

    # Execution time comparison
    start_time = time.time()
    sum(x for x in range(1000000))
    gen_time = time.time() - start_time

    start_time = time.time()
    sum([x for x in range(1000000)])
    list_time = time.time() - start_time

    print(f"Generator expression time: {gen_time:.6f} seconds")
    print(f"List comprehension time: {list_time:.6f} seconds")

    print()


def infinite_generator_expression():
    """
    Demonstrates an infinite generator expression.
    """
    print("Infinite generator expression:")
    
    # Creating an infinite sequence of even numbers
    even_numbers = (x for x in itertools.count(0, 2))
    
    print("First 10 even numbers:")
    for i, num in enumerate(even_numbers):
        if i >= 10:
            break
        print(num, end=" ")
    print("\n")


def generator_expression_with_function():
    """
    Demonstrates using generator expressions with functions.
    """
    print("Generator expression with function:")
    
    def process_item(x):
        return x * 2

    # Using a generator expression with map-like functionality
    processed_gen = (process_item(x) for x in range(10))
    print(f"Processed items: {list(processed_gen)}")

    # Using a generator expression in a function argument
    max_processed = max(process_item(x) for x in range(10))
    print(f"Maximum processed value: {max_processed}")

    print()


async def async_generator_expression():
    """
    Demonstrates an asynchronous generator expression.
    """
    print("Asynchronous generator expression:")
    
    async def async_process(x):
        await asyncio.sleep(0.1)
        return x * 2

    # Using an async generator expression
    async_gen = (await async_process(x) for x in range(5))
    
    results = []
    async for item in async_gen:
        results.append(item)
    
    print(f"Async processed results: {results}")
    print()


def performance_optimization():
    """
    Demonstrates performance optimization techniques with generator expressions.
    """
    print("Performance optimization:")
    
    # Using itertools for efficient generators
    efficient_gen = itertools.islice((x**2 for x in itertools.count()), 1000000)
    
    start_time = time.time()
    sum(efficient_gen)
    efficient_time = time.time() - start_time
    
    print(f"Efficient generator time: {efficient_time:.6f} seconds")

    # Memory-efficient processing of large datasets
    def process_large_dataset(data_gen):
        return sum(x for x in data_gen if x % 2 == 0)

    large_dataset = (x for x in range(10000000))
    result = process_large_dataset(large_dataset)
    print(f"Result of processing large dataset: {result}")

    print()


def main():
    """
    Main function to demonstrate all concepts related to generator expressions.
    """
    basic_generator_expression()
    generator_expression_with_conditions()
    nested_generator_expressions()
    generator_expression_vs_list_comprehension()
    infinite_generator_expression()
    generator_expression_with_function()
    asyncio.run(async_generator_expression())
    performance_optimization()


if __name__ == "__main__":
    main()


"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use generator expressions for large datasets to conserve memory.
2. Prefer generator expressions over list comprehensions when you only need to iterate once.
3. Use meaningful variable names, even in short generator expressions.
4. Combine generator expressions with built-in functions like sum(), max(), min() for efficiency.
5. Use generator expressions in function arguments to save memory and improve readability.

Common Pitfalls:
1. Trying to reuse a generator expression after it's been consumed.
2. Unnecessarily converting generator expressions to lists when iteration is sufficient.
3. Using generator expressions for small datasets where list comprehensions might be more appropriate.
4. Nesting generator expressions too deeply, leading to reduced readability.

Advanced Tips:
1. Use the `itertools` module in combination with generator expressions for powerful data processing.
2. Leverage `yield from` in generator functions to compose generator expressions.
3. Use `asyncio.as_completed()` with async generator expressions for concurrent processing.
4. Implement custom `__iter__()` methods in classes to make them work seamlessly with generator expressions.

Testing Generator Expressions:
1. Use `pytest` for testing generator expressions effectively.
2. Test both the generated values and the memory efficiency of your generator expressions.
3. Use `hypothesis` for property-based testing of generator expressions.

Example unit test:
```python
import pytest

def test_even_numbers_generator():
    even_gen = (x for x in range(10) if x % 2 == 0)
    assert list(even_gen) == [0, 2, 4, 6, 8]

def test_generator_memory_usage():
    import sys
    gen = (x for x in range(1000000))
    list_comp = [x for x in range(1000000)]
    assert sys.getsizeof(gen) < sys.getsizeof(list_comp)

# Run the tests
pytest.main([__file__])
```

4. Integration and Real-World Applications
------------------------------------------
Generator expressions are widely used in various domains:

1. Data Processing:
   - Efficiently processing large CSV files line by line
   - Transforming data streams in ETL (Extract, Transform, Load) pipelines

2. Web Development:
   - Paginating large result sets in web APIs
   - Streaming responses in web frameworks like Flask or Django

3. Scientific Computing:
   - Processing large datasets in chunks for machine learning models
   - Generating sequences of data for simulations

4. System Administration:
   - Monitoring log files in real-time
   - Efficiently searching through large file systems

Example from Django ORM (simplified):
```python
from django.db.models import Sum

total_sales = Sum(order.total for order in Order.objects.filter(status='completed'))
```

5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous Generator Expressions:
   - Introduced in Python 3.6 with PEP 525
   - Allows use of `async for` in generator expressions

2. Parallel Processing with Generator Expressions:
   - Using `multiprocessing` or `concurrent.futures` to process generator expressions in parallel
   - Example: `with ProcessPoolExecutor() as executor: results = executor.map(process_func, (x for x in large_dataset))`

3. Integration with Other Python Features:
   - Using generator expressions with `contextlib.ExitStack` for complex resource management
   - Combining generator expressions with `functools.partial` for partial function application

4. Functional Programming Paradigms:
   - Using generator expressions in a point-free style programming
   - Implementing lazy evaluation patterns using generator expressions

6. FAQs and Troubleshooting
---------------------------
Q: When should I use a generator expression instead of a list comprehension?
A: Use generator expressions when dealing with large datasets, when you only need to iterate once, or when memory efficiency is crucial.

Q: Can I reuse a generator expression?
A: No, generator expressions are consumed after one use. To reuse, you need to recreate the generator expression.

Q: How can I debug a generator expression?
A: Convert it to a list for small datasets, use the `pdb` debugger, or add print statements in the expression.

Troubleshooting:
- For `StopIteration` errors, ensure you're not trying to consume a generator expression more than once.
- For unexpected results, check the logic and try breaking the generator expression into steps.
- Use `itertools.islice()` to debug infinite generators by limiting the number of iterations.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools:
- PyCharm: IDE with excellent support for debugging generator expressions
- Memory Profiler: For analyzing memory usage of generator expressions

Libraries:
- itertools: Provides additional tools for working with iterators
- more-itertools: Extended set of iterator building blocks

Resources:
- "Fluent Python" by Luciano Ramalho
- "Python Cookbook" by David Beazley and Brian K. Jones
- Python official documentation: https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions

8. Performance Analysis and Optimization
----------------------------------------
- Use the `timeit` module for accurate benchmarking of generator expressions
- Profile memory usage using the `memory_profiler` library
- For large datasets, consider using `itertools.islice()` to limit the size of generator expressions during testing
- Use `itertools.chain()` to efficiently combine multiple generator expressions

Optimization strategies:
1. Use `itertools.tee()` to create multiple independent generators from a single generator expression
2. Implement caching mechanisms for frequently accessed generator results
3. Consider using NumPy or Pandas for numerical computations on large datasets instead of pure Python generator expressions

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