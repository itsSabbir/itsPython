"""
Iterators and Generators - The `yield` statement - in the Python Programming Language
=====================================================================================

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
The `yield` statement in Python is a fundamental component of generator functions, providing a powerful mechanism for creating iterators. It allows for the creation of lazy sequences, enabling efficient memory usage and elegant solutions to various programming problems.

Historical context:
- The `yield` statement was introduced in Python 2.2 (2001) with PEP 255.
- Generator expressions, a related concept, were added in Python 2.4 (2004) with PEP 289.
- The `yield from` statement was introduced in Python 3.3 (2012) with PEP 380.

Significance:
- `yield` enables the creation of memory-efficient iterators without implementing the full iterator protocol.
- It allows for lazy evaluation of sequences, which is crucial for handling large datasets.
- `yield` simplifies the implementation of certain algorithms and state machines.

Common use cases:
- Processing large files or datasets without loading everything into memory
- Implementing infinite sequences
- Creating data pipelines and transformations
- Simulating co-routines and lightweight concurrency

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import sys
import time
import asyncio
from typing import Generator, List, Any

def main():
    """
    Main function to demonstrate various uses of the `yield` statement.
    """
    print("1. Basic Generator Function")
    for num in countdown(5):
        print(num)
    
    print("\n2. Infinite Sequence Generator")
    fibonacci_gen = fibonacci()
    for _, fib in zip(range(10), fibonacci_gen):
        print(fib, end=' ')
    print()
    
    print("\n3. Generator with State")
    task_scheduler = task_scheduler_gen()
    next(task_scheduler)  # Start the scheduler
    task_scheduler.send("Task 1")
    task_scheduler.send("Task 2")
    task_scheduler.send("Task 3")
    task_scheduler.close()
    
    print("\n4. Using yield from")
    for item in flatten([1, [2, 3, [4, 5]], 6]):
        print(item, end=' ')
    print()
    
    print("\n5. Asynchronous Generator")
    asyncio.run(async_generator_example())

def countdown(n: int) -> Generator[int, None, None]:
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

def fibonacci() -> Generator[int, None, None]:
    """
    An infinite generator that yields Fibonacci numbers.
    
    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def task_scheduler_gen() -> Generator[None, str, None]:
    """
    A generator-based task scheduler that demonstrates maintaining state between yields.
    
    Yields:
        None
    
    Receives:
        str: Task descriptions sent to the generator.
    """
    tasks = []
    while True:
        task = yield
        if task is None:
            break
        tasks.append(task)
        print(f"Scheduled task: {task}")
        if len(tasks) >= 3:
            print(f"Executing tasks: {', '.join(tasks)}")
            tasks.clear()

def flatten(lst: List[Any]) -> Generator[Any, None, None]:
    """
    A generator function that flattens a nested list using 'yield from'.
    
    Args:
        lst (List[Any]): A potentially nested list.
    
    Yields:
        Any: Elements from the flattened list.
    """
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

async def async_counter(limit: int, delay: float) -> Generator[int, None, None]:
    """
    An asynchronous generator that counts up to a limit with a delay between yields.
    
    Args:
        limit (int): The upper bound of the counter.
        delay (float): The delay in seconds between yields.
    
    Yields:
        int: The next number in the sequence.
    """
    for i in range(1, limit + 1):
        await asyncio.sleep(delay)
        yield i

async def async_generator_example():
    """
    Demonstrates the usage of an asynchronous generator.
    """
    async for num in async_counter(5, 0.1):
        print(f"Async generated number: {num}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------

Best Practices:
1. Use generators for large datasets to conserve memory.
2. Keep generator functions focused on a single task or transformation.
3. Use type hints to improve code readability and catch potential errors.
4. Consider using `yield from` for sub-generators to improve readability.
5. Close generators explicitly when they need cleanup using the .close() method.

Common Pitfalls:
1. Attempting to access generator values by index (generators don't support indexing).
2. Forgetting that generators are exhausted after a single iteration.
3. Overlooking the lazy evaluation nature of generators, leading to unexpected behavior.
4. Misusing `yield` in regular functions, causing them to become generators unintentionally.

Advanced Tips:
1. Use the `send()` method to communicate with generators (coroutine-like behavior).
2. Implement `__iter__()` and `__next__()` methods for more control over iteration.
3. Use `itertools` for advanced generator manipulations (e.g., `chain`, `islice`).
4. Consider using `yield from` for better readability in recursive generators.

Performance Considerations:
1. Generators are generally more memory-efficient but may have slightly higher CPU usage.
2. Use profiling tools to measure the impact of generators vs. lists in your specific use case.
3. Consider caching generator results if they're used multiple times.

Edge Cases:
1. Handle `StopIteration` explicitly when calling `next()` on generators.
2. Be aware of the differences in exception handling between generator functions and regular functions.

Testing:
Here's an example of how to write unit tests for a generator function:
"""

import unittest

class TestCountdownGenerator(unittest.TestCase):
    def test_countdown(self):
        gen = countdown(3)
        self.assertEqual(list(gen), [3, 2, 1])
    
    def test_empty_countdown(self):
        gen = countdown(0)
        self.assertEqual(list(gen), [])

# Uncomment the following lines to run the tests
# if __name__ == '__main__':
#     unittest.main()

"""
4. Integration and Real-World Applications
------------------------------------------

1. Data Processing Pipelines:
   Generators are excellent for creating efficient data processing pipelines,
   allowing for lazy evaluation and memory-efficient processing of large datasets.

2. Web Scraping:
   Generators can be used to create efficient web scrapers that process and yield
   data as it's fetched, allowing for parallel processing and early termination.

3. Infinite Sequences in Mathematics:
   Generators are useful for representing and working with infinite mathematical
   sequences, such as prime numbers or the Fibonacci sequence.

4. Streaming Data Processing:
   In scenarios involving real-time data streams, generators can be used to
   process incoming data on-the-fly without storing the entire stream in memory.

5. Memory-Efficient Data Transformations:
   When working with large datasets that require multiple transformations,
   generators can be chained to create memory-efficient transformation pipelines.

Example: Using generators in a data processing pipeline
"""

def read_large_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def process_line(line: str) -> str:
    # Simulate some processing
    return line.upper()

def data_pipeline(file_path: str) -> Generator[str, None, None]:
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
   Asynchronous generators combine the power of generators with asynchronous
   programming, allowing for efficient handling of I/O-bound tasks.

2. Generator-based Coroutines:
   Before the introduction of native coroutines (async/await), generators
   were used to implement coroutine-like behavior in Python.

3. Yield from in Context Managers:
   The `yield from` statement can be used to create reusable and composable
   context managers.

4. Generators in Functional Programming:
   Generators align well with functional programming concepts like lazy
   evaluation and infinite sequences, leading to more functional-style Python code.

5. Type Hinting for Generators (Python 3.6+):
   The `typing` module provides support for type hinting generators,
   improving code clarity and enabling better static analysis.

Example: Using an asynchronous generator for stream processing
"""

import asyncio

async def async_stream_processor(stream: Generator[str, None, None]) -> Generator[str, None, None]:
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

Q: What's the difference between `return` and `yield` in a function?
A: `return` exits the function and returns a value, while `yield` pauses the
   function's execution, remembers its state, and returns a value to the caller.

Q: Can I use both `yield` and `return` in the same function?
A: Yes, but `return` will terminate the generator. It's often used to signal
   the end of the generator or to return a final value.

Q: How do I convert a generator to a list?
A: You can use the `list()` function: `my_list = list(my_generator)`

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
4. PEP 342 - Coroutines via Enhanced Generators: https://www.python.org/dev/peps/pep-0342/
5. "Generator Tricks for Systems Programmers" by David Beazley: http://www.dabeaz.com/generators/

8. Performance Analysis and Optimization
----------------------------------------

Profiling generators:
Use the cProfile module or line_profiler to identify performance bottlenecks.

Example of profiling a generator function:
"""

import cProfile

def profile_fibonacci():
    fib = fibonacci()
    list(zip(range(1000), fib))  # Generate first 1000 Fibonacci numbers

cProfile.run('profile_fibonacci()')

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
def cached_expensive_computation(n: int) -> int:
    # Simulate an expensive computation
    time.sleep(0.1)
    return n * n

def optimized_generator(n: int) -> Generator[int, None, None]:
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
The `yield` statement is a powerful feature in Python that enables the creation of memory-efficient iterators and facilitates lazy evaluation. By mastering the use of `yield`, developers can write more efficient and expressive code, especially when dealing with large datasets or complex iteration patterns.

As Python continues to evolve, so too will the patterns and best practices surrounding generators and the `yield` statement. Stay informed about new developments in the Python community, and don't hesitate to experiment with innovative uses of `yield` in your projects.

Thank you for using this expert-level note sheet on the `yield` statement in Python. Happy coding!
"""

if __name__ == "__main__":
    main()

# Uncomment the following lines to run the unit tests
# import unittest
# unittest.main(argv=[''], exit=False)