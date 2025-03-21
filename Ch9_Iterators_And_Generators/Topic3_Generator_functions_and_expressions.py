"""
Iterators and Generators - Generator functions and expressions - in the Python Programming Language
===================================================================================================

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
Generator functions and expressions in Python provide a powerful and memory-efficient way to create iterators. They allow for lazy evaluation of sequences, which is particularly useful when dealing with large datasets or infinite sequences.

Historical context:
- Generator functions were introduced in Python 2.2 (2001) with PEP 255.
- Generator expressions were added in Python 2.4 (2004) with PEP 289.
- The 'yield from' statement was introduced in Python 3.3 (2012) with PEP 380.

Significance:
- Generators provide a simple way to create iterators without implementing the full iterator protocol.
- They enable lazy evaluation, improving memory efficiency for large datasets.
- Generators simplify the implementation of certain algorithms and data processing pipelines.

Common use cases:
- Processing large files or datasets without loading everything into memory
- Implementing infinite sequences
- Creating data pipelines and transformations
- Simulating co-routines and lightweight threads

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import itertools
import time
import sys

def main():
    """
    Main function to demonstrate generator functions and expressions.
    """
    print("1. Basic Generator Function")
    for num in countdown(5):
        print(num)
    
    print("\n2. Generator Expression")
    squares = (x**2 for x in range(10))
    print(list(squares))
    
    print("\n3. Infinite Sequence Generator")
    primes = prime_generator()
    for _, prime in zip(range(10), primes):
        print(prime, end=' ')
    print()
    
    print("\n4. Generator with 'yield from'")
    for item in flatten([[1, 2], [3, 4, 5], [6]]):
        print(item, end=' ')
    print()
    
    print("\n5. Memory Usage Comparison")
    compare_memory_usage()
    
    print("\n6. Asynchronous Generator Example")
    import asyncio
    asyncio.run(async_generator_example())

def countdown(n):
    """
    A simple generator function that counts down from n to 1.
    
    Args:
        n (int): The starting number for the countdown.
    
    Yields:
        int: The next number in the countdown sequence.
    """
    while n > 0:
        yield n
        n -= 1

def prime_generator():
    """
    An infinite generator that yields prime numbers.
    
    Yields:
        int: The next prime number in the sequence.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def flatten(nested_list):
    """
    A generator function that flattens a nested list using 'yield from'.
    
    Args:
        nested_list (list): A list that may contain nested lists.
    
    Yields:
        Any: Elements from the flattened list.
    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

def compare_memory_usage():
    """
    Compares memory usage between a list comprehension and a generator expression.
    """
    def get_memory_usage():
        return sys.getsizeof(list_comp), sys.getsizeof(gen_exp)
    
    n = 10**6
    list_comp = [i**2 for i in range(n)]
    gen_exp = (i**2 for i in range(n))
    
    list_size, gen_size = get_memory_usage()
    print(f"List comprehension size: {list_size} bytes")
    print(f"Generator expression size: {gen_size} bytes")
    print(f"Memory saved: {list_size - gen_size} bytes")

async def async_generator(n):
    """
    An asynchronous generator function that yields numbers with a delay.
    
    Args:
        n (int): The number of items to yield.
    
    Yields:
        int: Numbers from 1 to n with a delay between each yield.
    """
    for i in range(1, n + 1):
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation
        yield i

async def async_generator_example():
    """
    Demonstrates the usage of an asynchronous generator.
    """
    async for num in async_generator(5):
        print(f"Async generated number: {num}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------

Best Practices:
1. Use generators for large datasets to conserve memory.
2. Prefer generator expressions over list comprehensions when iterating once.
3. Use 'yield from' for delegating to sub-generators.
4. Close generators explicitly when they need cleanup using .close() method.
5. Use typing.Generator for type hinting generator functions.

Common Pitfalls:
1. Trying to reuse an exhausted generator (they can only be iterated once).
2. Forgetting that generators are lazy and won't start until iterated.
3. Using generators where eager evaluation is needed (e.g., when the sequence is used multiple times).
4. Overlooking the fact that generators can't be indexed or sliced directly.

Advanced Tips:
1. Use the send() method to communicate with generators (coroutine-like behavior).
2. Implement the __iter__() and __next__() methods for more control over iteration.
3. Use itertools for advanced generator manipulations (e.g., chain, islice).
4. Consider using yield from for better readability in recursive generators.

Performance Considerations:
1. Generators are generally more memory-efficient but may be slightly slower for small datasets.
2. Use profiling tools to measure the impact of generators vs. lists in your specific use case.
3. Consider caching generator results if they're used multiple times.

Edge Cases:
1. Handle StopIteration explicitly when calling next() on generators.
2. Be aware of the differences in exception handling between generator functions and regular functions.

Testing:
Here's an example of how to write unit tests for a generator function:
"""

import unittest

class TestPrimeGenerator(unittest.TestCase):
    def test_first_five_primes(self):
        gen = prime_generator()
        first_five = [next(gen) for _ in range(5)]
        self.assertEqual(first_five, [2, 3, 5, 7, 11])
    
    def test_large_prime(self):
        gen = prime_generator()
        # 1000th prime number
        thousandth_prime = next(itertools.islice(gen, 999, 1000))
        self.assertEqual(thousandth_prime, 7919)

# Uncomment the following lines to run the tests
# if __name__ == '__main__':
#     unittest.main()

"""
4. Integration and Real-World Applications
------------------------------------------

1. Data Processing Pipelines:
   Generators are excellent for creating efficient data processing pipelines,
   allowing for lazy evaluation and memory-efficient processing of large datasets.

2. File Parsing:
   Generators are commonly used for reading and processing large files line by line,
   avoiding the need to load the entire file into memory.

3. Network Programming:
   Generators can be used to create efficient network protocols, streaming data
   as it becomes available rather than waiting for the entire payload.

4. Web Scraping:
   Generators are useful in web scraping to process and yield data as it's
   fetched, allowing for parallel processing and early termination if needed.

5. Game Development:
   Generators can be used to create game AI behaviors, level generation, or
   to simulate turn-based game logic.

Example: Using a generator in a data processing pipeline
"""

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def process_line(line):
    # Simulate some processing
    return line.upper()

def data_pipeline(file_path):
    for line in read_large_file(file_path):
        processed_line = process_line(line)
        yield processed_line

# Usage
# for processed_line in data_pipeline('large_file.txt'):
#     print(processed_line)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------

1. Asynchronous Generators (Python 3.6+):
   With the rise of asynchronous programming, asynchronous generators
   (using 'async def' and 'yield') are becoming more prevalent.

2. Generator-based Coroutines:
   Before the introduction of native coroutines (async/await), generators
   were used to implement coroutine-like behavior in Python.

3. Lazy Evaluation in Data Science:
   Libraries like Dask use generator-like constructs to enable lazy
   evaluation of large datasets that don't fit in memory.

4. Stream Processing:
   Generators are being used in stream processing frameworks to handle
   real-time data analysis efficiently.

5. Functional Programming Concepts:
   Generators align well with functional programming concepts like lazy
   evaluation and infinite sequences.

Example: Using an asynchronous generator for stream processing
"""

import asyncio

async def async_stream_processor(stream):
    async for chunk in stream:
        # Simulate some async processing
        await asyncio.sleep(0.1)
        yield chunk.upper()

async def async_stream_example():
    async def sample_stream():
        for i in range(5):
            await asyncio.sleep(0.5)  # Simulate delay in receiving data
            yield f"data chunk {i}"
    
    async for processed_chunk in async_stream_processor(sample_stream()):
        print(f"Processed: {processed_chunk}")

# Uncomment the following line to run the async example
# asyncio.run(async_stream_example())

"""
6. FAQs and Troubleshooting
---------------------------

Q: What's the difference between a generator function and a generator expression?
A: A generator function is defined using 'def' and 'yield', while a generator
   expression is a one-line expression similar to a list comprehension but with
   parentheses instead of square brackets.

Q: Can I use a generator more than once?
A: No, once a generator is exhausted, it cannot be reused. You need to create
   a new generator object to iterate over the sequence again.

Q: How do I convert a generator to a list?
A: You can use the list() function: my_list = list(my_generator)

Q: Why does my generator seem to "hang" or not produce any output?
A: Remember that generators are lazy and won't produce values until iterated.
   Ensure you're actually iterating over the generator (e.g., using a for loop).

Troubleshooting Guide:
1. Generator exhausts too quickly:
   - Check if you're accidentally consuming the generator before the intended use.
   - Ensure your generator function doesn't have an early return statement.

2. Memory usage grows unexpectedly:
   - Look for accidental materialization of the entire generator (e.g., converting to a list).
   - Check if you're storing all generated values instead of processing them one at a time.

3. Unexpected StopIteration:
   - Ensure your generator function yields values for all expected iterations.
   - Check for off-by-one errors in your iteration logic.

4. Infinite loop in a generator:
   - Verify the exit condition in your generator function.
   - Use tools like `itertools.islice()` to limit iteration for testing.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------

Tools and Libraries:
1. itertools: Built-in module for working with iterators
2. more-itertools: Extended set of iterator tools
3. yield-from: Simplifies delegation to sub-generators
4. asyncio: For working with asynchronous generators
5. typing: For type hinting generators

Resources:
1. "Fluent Python" by Luciano Ramalho - Chapter on Iterators and Generators
2. "Python Cookbook" by David Beazley and Brian K. Jones - Recipes for Iterators and Generators
3. PEP 255 - Simple Generators: https://www.python.org/dev/peps/pep-0255/
4. PEP 289 - Generator Expressions: https://www.python.org/dev/peps/pep-0289/
5. "Generator Tricks for Systems Programmers" by David Beazley: http://www.dabeaz.com/generators/

8. Performance Analysis and Optimization
----------------------------------------

Profiling generators:
Use the cProfile module or line_profiler to identify performance bottlenecks.

Example of profiling a generator function:
"""

import cProfile

def profile_prime_generator():
    primes = prime_generator()
    list(itertools.islice(primes, 1000))  # Generate first 1000 primes

cProfile.run('profile_prime_generator()')

"""
Optimization strategies:
1. Use generator expressions instead of list comprehensions when possible
2. Implement caching for expensive computations within generators
3. Use `itertools` functions for efficient iterator operations
4. Consider using NumPy or Pandas for numerical operations on large datasets

Example of optimizing a generator with caching:
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def cached_expensive_computation(n):
    # Simulate an expensive computation
    time.sleep(0.1)
    return n * n

def optimized_generator(n):
    for i in range(n):
        yield cached_expensive_computation(i)

# Usage
# for value in optimized_generator(10):
#     print(value)

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
- Ensure compatibility with Python 3.6+ unless explicitly noted.
- Write clear, concise explanations for complex topics.
- Include unit tests for new functionality when applicable.

Remember, the goal is to keep this note sheet as an authoritative and up-to-date resource for Python developers of all skill levels.

Conclusion
----------
Generator functions and expressions are powerful tools in Python for creating memory-efficient iterators and implementing lazy evaluation. By mastering these concepts, developers can write more efficient and expressive code, especially when dealing with large datasets or complex iteration patterns.

As Python continues to evolve, so too will the patterns and best practices surrounding generators. Stay informed about new developments in the Python community, and don't hesitate to experiment with innovative uses of generators in your projects.

Thank you for using this expert-level note sheet on generator functions and expressions in Python. Happy coding!
"""

if __name__ == "__main__":
    main()

# Uncomment the following lines to run the unit tests
# import unittest
# unittest.main(argv=[''], exit=False)