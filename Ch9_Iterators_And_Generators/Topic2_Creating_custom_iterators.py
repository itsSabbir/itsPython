"""
Iterators and Generators - Creating custom iterators - in the Python Programming Language
=========================================================================================

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
Iterators and generators are fundamental concepts in Python that provide a memory-efficient way to work with sequences of data. Custom iterators allow developers to define their own iterable objects, enabling fine-grained control over iteration behavior.

Historical context:
- Iterators were introduced in Python 2.2 (2001) as part of PEP 234.
- Generators, a special type of iterator, were introduced in Python 2.3 (2003) with PEP 255.
- The 'yield from' syntax for generators was added in Python 3.3 (2012) with PEP 380.

Significance:
- Iterators provide a uniform interface for traversing different types of collections.
- They enable lazy evaluation, improving memory efficiency for large datasets.
- Custom iterators allow for the creation of complex iteration patterns and infinite sequences.

Common use cases:
- Processing large datasets without loading everything into memory
- Implementing custom data structures with specific iteration behavior
- Creating pipelines for data processing and transformation
- Generating sequences on-the-fly, including infinite sequences

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

# Required imports
from typing import Iterator, Any
import time
import random

def main():
    """
    Main function to demonstrate custom iterators and their applications.
    """
    print("1. Basic Custom Iterator")
    for item in CountDown(5):
        print(item)
    
    print("\n2. Fibonacci Sequence Iterator")
    fib = FibonacciIterator(10)
    print(list(fib))
    
    print("\n3. Infinite Prime Number Generator")
    prime_gen = PrimeGenerator()
    for _ in range(10):
        print(next(prime_gen))
    
    print("\n4. Custom Range Iterator with Step")
    for num in CustomRange(1, 10, 2):
        print(num)
    
    print("\n5. Asynchronous Iterator Example")
    import asyncio
    asyncio.run(async_iterator_example())

class CountDown:
    """
    A simple custom iterator that counts down from a given number to 1.
    
    This class demonstrates the basic implementation of the iterator protocol.
    """
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

class FibonacciIterator:
    """
    An iterator that generates Fibonacci numbers up to a specified limit.
    
    This class showcases a more complex iterator with internal state management.
    """
    def __init__(self, limit):
        self.limit = limit
        self.previous = 0
        self.current = 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        
        result = self.previous
        self.previous, self.current = self.current, self.previous + self.current
        self.count += 1
        return result

class PrimeGenerator:
    """
    An infinite iterator that generates prime numbers.
    
    This class demonstrates how to create an infinite sequence using an iterator.
    """
    def __init__(self):
        self.current = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.is_prime(self.current):
                result = self.current
                self.current += 1
                return result
            self.current += 1
    
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

class CustomRange:
    """
    A custom range iterator that supports a step parameter.
    
    This class showcases how to implement a more flexible version of the built-in range function.
    """
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        result = self.current
        self.current += self.step
        return result

class AsyncCounter:
    """
    An asynchronous iterator that counts up to a specified limit with a delay between iterations.
    
    This class demonstrates how to implement the asynchronous iterator protocol.
    """
    def __init__(self, limit, delay):
        self.limit = limit
        self.delay = delay
        self.current = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.limit:
            raise StopAsyncIteration
        
        await asyncio.sleep(self.delay)
        self.current += 1
        return self.current

async def async_iterator_example():
    """
    Demonstrates the usage of an asynchronous iterator.
    """
    async_counter = AsyncCounter(5, 0.5)
    async for count in async_counter:
        print(f"Async count: {count}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------

Best Practices:
1. Use the iterator protocol (__iter__ and __next__ methods) for custom iterators.
2. Implement __iter__ to return self for iterators, allowing them to be used in for loops.
3. Raise StopIteration when the iteration is complete.
4. Use generators for simple iterators to reduce boilerplate code.
5. Consider using the collections.abc.Iterator base class for type hinting and interface consistency.

Common Pitfalls:
1. Forgetting to raise StopIteration, leading to infinite loops.
2. Modifying the iterable during iteration, which can lead to unexpected behavior.
3. Assuming that an iterator can be reset or reused after it's exhausted.
4. Not properly handling exceptions in __next__, potentially breaking the iteration prematurely.

Advanced Tips:
1. Use the itertools module for advanced iterator manipulation and combination.
2. Implement __reversed__ for reversible iterators when applicable.
3. Consider using @staticmethod or @classmethod decorators for methods that don't require instance state.
4. Use generator expressions for simple, one-time use iterators.
5. Implement the __length_hint__ method to provide an estimated length of the iterator.

Performance Considerations:
1. Use iterators for large datasets to conserve memory.
2. Avoid unnecessary computations in __next__ method; defer work until it's needed.
3. Use caching or memoization for expensive computations in iterators.
4. Consider using __slots__ to reduce memory footprint for iterator objects.

Edge Cases:
1. Handle empty sequences gracefully in custom iterators.
2. Consider thread safety for iterators used in multi-threaded environments.
3. Properly handle potential overflow in numeric iterators (e.g., Fibonacci sequence).

Testing:
Here's an example of how to write unit tests for a custom iterator:
"""

import unittest

class TestCustomRange(unittest.TestCase):
    def test_positive_step(self):
        self.assertEqual(list(CustomRange(1, 5)), [1, 2, 3, 4])
    
    def test_negative_step(self):
        self.assertEqual(list(CustomRange(5, 1, -1)), [5, 4, 3, 2])
    
    def test_empty_range(self):
        self.assertEqual(list(CustomRange(1, 1)), [])
    
    def test_single_element(self):
        self.assertEqual(list(CustomRange(1, 2)), [1])

# Uncomment the following lines to run the tests
# if __name__ == '__main__':
#     unittest.main()

"""
4. Integration and Real-World Applications
------------------------------------------

1. Data Processing Pipelines:
   Custom iterators can be used to create efficient data processing pipelines,
   allowing for lazy evaluation and memory-efficient processing of large datasets.

2. Database Cursors:
   Database APIs often use iterator-like objects (cursors) to fetch results efficiently.
   Custom iterators can wrap these cursors to provide additional functionality.

3. File Parsing:
   Iterators are excellent for parsing large files line by line or in chunks,
   allowing for efficient memory usage.

4. Infinite Sequences:
   Custom iterators can generate infinite sequences, useful in simulations,
   mathematical computations, or generating test data.

5. Pagination:
   Iterators can be used to implement pagination in web applications,
   allowing for efficient retrieval and display of large datasets.

Example: Using a custom iterator in a data processing pipeline
"""

class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source
    
    def __iter__(self):
        return self
    
    def __next__(self):
        raw_data = next(self.data_source)
        # Process the raw data
        processed_data = self.process(raw_data)
        return processed_data
    
    @staticmethod
    def process(data):
        # Simulate data processing
        return data.upper()

def data_pipeline_example():
    # Simulating a data source (e.g., file reader, database cursor)
    data_source = iter(['apple', 'banana', 'cherry'])
    
    processor = DataProcessor(data_source)
    
    for item in processor:
        print(f"Processed item: {item}")

# Uncomment the following line to run the example
# data_pipeline_example()

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------

1. Asynchronous Iterators (Python 3.5+):
   With the rise of asynchronous programming, asynchronous iterators and
   generators (using 'async for' and 'async with') are becoming more prevalent.

2. Itertools and More-Itertools:
   The itertools module provides a collection of fast, memory-efficient tools
   for working with iterators. The third-party more-itertools package extends
   this with additional utilities.

3. Lazy Evaluation in Data Science:
   Libraries like Dask and Vaex use custom iterators and lazy evaluation
   techniques to handle datasets larger than memory.

4. Iterator Fusion:
   Techniques to optimize chains of iterator operations by fusing them
   into a single loop, improving performance.

5. Type Hinting for Iterators (Python 3.5+):
   The typing module provides support for type hinting iterators and
   generators, improving code clarity and enabling better static analysis.

Example: Using type hints with custom iterators
"""

from typing import Iterator, TypeVar

T = TypeVar('T')

class TypedFibonacciIterator(Iterator[int]):
    def __init__(self, limit: int):
        self.limit = limit
        self.previous = 0
        self.current = 1
        self.count = 0
    
    def __next__(self) -> int:
        if self.count >= self.limit:
            raise StopIteration
        
        result = self.previous
        self.previous, self.current = self.current, self.previous + self.current
        self.count += 1
        return result

def process_items(items: Iterator[T]) -> Iterator[T]:
    for item in items:
        yield item * 2  # type: ignore

# Example usage
typed_fib = TypedFibonacciIterator(5)
processed_fib = process_items(typed_fib)
print(list(processed_fib))

"""
6. FAQs and Troubleshooting
---------------------------

Q: What's the difference between an iterable and an iterator?
A: An iterable is an object that can be iterated over (e.g., lists, strings).
   An iterator is an object that defines __next__ to return the next item in the sequence.

Q: How do I reset an iterator?
A: Iterators are generally not resettable. To start over, you need to create a new iterator instance.

Q: Why use iterators instead of lists?
A: Iterators are memory-efficient for large datasets and allow for lazy evaluation.

Q: How can I debug an infinite loop in my custom iterator?
A: Implement a safety counter or use debugging tools to set breakpoints in your __next__ method.

Troubleshooting Guide:
1. Iterator exhausts too quickly:
   - Check if StopIteration is raised prematurely in __next__.
   - Ensure the iteration condition is correct.

2. Memory usage grows unexpectedly:
   - Look for accidental storage of all items in memory.
   - Use memory profiling tools to identify the source of the leak.

3. Iterator seems to skip items:
   - Check if __next__ is incrementing counters correctly.
   - Ensure no items are being discarded unintentionally.

4. Performance issues with large datasets:
   - Use profiling tools to identify bottlenecks.
   - Consider optimizing the __next__ method or using caching techniques.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------

Tools and Libraries:
1. itertools: Built-in module for iterator operations
2. more-itertools: Extended set of iterator tools
3. yield-from: Simplifies delegation to sub-generators
4. tqdm: Adds progress bars to iterators
5. hypothesis: Property-based testing for iterators

Resources:
1. "Fluent Python" by Luciano Ramalho - Chapters on iterators and generators
2. "Python Cookbook" by David Beazley and Brian K. Jones - Recipes for iterators
3. PEP 234 - Iterators: https://www.python.org/dev/peps/pep-0234/
4. PEP 255 - Simple Generators: https://www.python.org/dev/peps/pep-0255/
5. "Generator Tricks for Systems Programmers" by David Beazley: http://www.dabeaz.com/generators/

8. Performance Analysis and Optimization
----------------------------------------

Profiling iterators:
Use the cProfile module or line_profiler to identify performance bottlenecks.

Example of profiling an iterator:
"""

import cProfile

def profile_fibonacci():
    fib = FibonacciIterator(1000)
    list(fib)  # Force evaluation of the entire sequence

cProfile.run('profile_fibonacci()')

"""
Optimization strategies:
1. Memoization for expensive computations
2. Lazy evaluation of complex operations
3. Using __slots__ to reduce memory footprint
4. Implementing __length_hint__ for better memory allocation

Example of memoization in an iterator:
"""

from functools import lru_cache

class MemoizedFibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        result = self.fibonacci(self.count)
        self.count += 1
        return result
    
    @staticmethod
    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n < 2:
            return n
        return MemoizedFibonacciIterator.fibonacci(n-1) + MemoizedFibonacciIterator.fibonacci(n-2)

# Usage
memoized_fib = MemoizedFibonacciIterator(100)
print(list(memoized_fib))

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
Custom iterators in Python provide a powerful tool for efficient data processing, memory management, and the implementation of complex iteration patterns. By mastering the iterator protocol and understanding the nuances of creating custom iterators, developers can write more efficient and expressive code.

As the Python language continues to evolve, so too will the patterns and best practices surrounding iterators. Stay informed about new developments in the Python community, and don't hesitate to experiment with innovative uses of iterators in your projects.

Thank you for using this expert-level note sheet on creating custom iterators in Python. Happy coding!
"""

# Additional examples and advanced concepts

class LazyRange:
    """
    A lazy implementation of range that generates values on-demand.
    This class demonstrates how to create a memory-efficient alternative to the built-in range function.
    """
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        result = self.start
        self.start += self.step
        return result

def lazy_range_example():
    """
    Demonstrates the usage and memory efficiency of LazyRange compared to built-in range.
    """
    import sys

    print("Memory usage comparison:")
    print(f"Built-in range: {sys.getsizeof(range(1000000))} bytes")
    print(f"LazyRange: {sys.getsizeof(LazyRange(1000000))} bytes")

    print("\nFirst 10 elements of LazyRange(0, 100, 2):")
    lazy_even = LazyRange(0, 100, 2)
    for i, num in enumerate(lazy_even):
        if i >= 10:
            break
        print(num, end=' ')
    print()

class InfiniteSequence:
    """
    An example of an infinite sequence generator using the iterator protocol.
    This class demonstrates how to create an iterator that never raises StopIteration.
    """
    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(1, 100)

def infinite_sequence_example():
    """
    Demonstrates the usage of an infinite sequence iterator.
    """
    inf_seq = InfiniteSequence()
    print("Generating 10 random numbers from InfiniteSequence:")
    for _, num in zip(range(10), inf_seq):
        print(num, end=' ')
    print()

class NestedIterator:
    """
    An iterator that flattens nested iterables.
    This class demonstrates a more complex iterator that can handle recursive structures.
    """
    def __init__(self, nested_iterable):
        self.stack = [iter(nested_iterable)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
                if isinstance(item, (list, tuple)):
                    self.stack.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.stack.pop()
        raise StopIteration

def nested_iterator_example():
    """
    Demonstrates the usage of NestedIterator to flatten a complex nested structure.
    """
    nested_data = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
    flattened = NestedIterator(nested_data)
    print("Flattened nested structure:")
    print(list(flattened))

def main():
    """
    Main function to demonstrate various custom iterator examples.
    """
    print("1. LazyRange Example")
    lazy_range_example()
    
    print("\n2. InfiniteSequence Example")
    infinite_sequence_example()
    
    print("\n3. NestedIterator Example")
    nested_iterator_example()

if __name__ == "__main__":
    main()

# Uncomment the following lines to run the unit tests
# import unittest
# unittest.main(argv=[''], exit=False)