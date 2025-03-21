"""
Iterators and Generators - Iterable objects and iterators - in the Python Programming Language
==============================================================================================

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
Iterators and iterable objects are fundamental concepts in Python that provide a unified way to access elements of a collection sequentially. They form the backbone of Python's "for" loops and many built-in functions.

Historical context:
- Iterators were introduced in Python 2.2 (2001) as part of the Python Enhancement Proposal (PEP) 234.
- The 'yield' statement, which simplifies the creation of iterators, was introduced in Python 2.2 with PEP 255.
- In Python 3.0 (2008), the 'next()' function was introduced, replacing the '.next()' method for iterators.

Significance:
- Iterators provide a memory-efficient way to process large datasets.
- They allow for lazy evaluation, where values are computed only when needed.
- Iterators provide a consistent interface for traversing different types of collections.

Common use cases:
- Traversing large datasets without loading everything into memory.
- Implementing custom sequence types.
- Creating data pipelines for processing streams of data.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from typing import List, Iterator, Iterable, Any
import itertools
import time

class CustomIterable:
    """A custom iterable class that generates a sequence of squares."""
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    
    def __iter__(self) -> Iterator[int]:
        """Return an iterator object."""
        return CustomIterator(self.start, self.end)

class CustomIterator:
    """A custom iterator class that generates squares of numbers."""
    
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end
    
    def __iter__(self) -> 'CustomIterator':
        """Return self as this is already an iterator."""
        return self
    
    def __next__(self) -> int:
        """Return the next value in the sequence."""
        if self.current > self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

def demonstrate_basic_usage():
    """Demonstrate basic usage of iterables and iterators."""
    # Using a built-in iterable (list)
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num, end=" ")
    print("\n")
    
    # Using our custom iterable
    squares = CustomIterable(1, 5)
    for square in squares:
        print(square, end=" ")
    print("\n")
    
    # Manual iteration using an iterator
    iterator = iter(CustomIterable(1, 3))
    print(next(iterator))  # 1
    print(next(iterator))  # 4
    print(next(iterator))  # 9
    try:
        print(next(iterator))
    except StopIteration:
        print("Iteration complete")

def fibonacci() -> Iterator[int]:
    """A generator function that yields Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def demonstrate_generator():
    """Demonstrate the use of a generator function."""
    fib = fibonacci()
    for _ in range(10):
        print(next(fib), end=" ")
    print("\n")

def batch_processor(data: Iterable[Any], batch_size: int) -> Iterator[List[Any]]:
    """Process data in batches using itertools."""
    iterator = iter(data)
    return iter(lambda: list(itertools.islice(iterator, batch_size)), [])

def demonstrate_batch_processing():
    """Demonstrate batch processing using an iterator-based approach."""
    data = range(15)
    for batch in batch_processor(data, 4):
        print(f"Processing batch: {batch}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use generators for large or infinite sequences to save memory.
2. Implement the __iter__ and __next__ methods for custom iterables.
3. Use the built-in iter() and next() functions instead of calling __iter__() and __next__() directly.
4. Utilize the itertools module for efficient iterator algebra.

Common Pitfalls:
1. Trying to reuse exhausted iterators.
2. Accidentally creating a list from a large iterator, defeating the purpose of lazy evaluation.
3. Forgetting to raise StopIteration when the iteration is complete.
4. Modifying a collection while iterating over it.

Advanced Tips:
1. Use itertools.tee() to create multiple independent iterators from a single iterable.
2. Implement __iter__ in container classes to make them iterable.
3. Use the yield from statement to delegate to a sub-iterator.
4. Utilize the send() method of generators for coroutine-style programming.
"""

from collections.abc import Iterable as IterableABC

def flatten(items: Iterable[Any]) -> Iterator[Any]:
    """Flatten a nested structure of iterables."""
    for item in items:
        if isinstance(item, IterableABC) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques with iterators and generators."""
    # Flattening nested structures
    nested = [1, [2, 3, [4, 5]], 6, [7, 8]]
    print("Flattened structure:", list(flatten(nested)))
    
    # Using itertools.tee()
    numbers = [1, 2, 3, 4, 5]
    iter1, iter2 = itertools.tee(numbers)
    print("First 3 from iter1:", list(itertools.islice(iter1, 3)))
    print("All from iter2:", list(iter2))
    
    # Coroutine-style generator
    def averager():
        total = 0
        count = 0
        average = None
        while True:
            value = yield average
            total += value
            count += 1
            average = total / count
    
    avg = averager()
    next(avg)  # Prime the coroutine
    print("Running average:")
    for i in range(1, 6):
        print(f"Sending {i}, average: {avg.send(i)}")

"""
4. Integration and Real-World Applications
------------------------------------------
Iterators and generators are widely used in various Python libraries and frameworks:

1. Django's QuerySet: Lazy evaluation of database queries.
2. Pandas' DataFrame iterating methods: Efficient data processing.
3. Asyncio library: Asynchronous iterators and generators.

Real-world example: A data processing pipeline using iterators.
"""

import csv
from typing import Dict, Iterator

def read_csv(filename: str) -> Iterator[Dict[str, str]]:
    """Read a CSV file and yield each row as a dictionary."""
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        yield from reader

def process_row(row: Dict[str, str]) -> Dict[str, Any]:
    """Process a single row of data."""
    return {
        'name': row['name'],
        'age': int(row['age']),
        'salary': float(row['salary'])
    }

def filter_adults(data: Iterator[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """Filter out non-adults from the data."""
    return filter(lambda x: x['age'] >= 18, data)

def calculate_average_salary(data: Iterator[Dict[str, Any]]) -> float:
    """Calculate the average salary from the data."""
    total_salary = 0
    count = 0
    for row in data:
        total_salary += row['salary']
        count += 1
    return total_salary / count if count > 0 else 0

def demonstrate_real_world_application():
    """Demonstrate a real-world application of iterators in a data processing pipeline."""
    # Note: This assumes a 'data.csv' file exists with columns: name, age, salary
    data = read_csv('data.csv')
    processed_data = map(process_row, data)
    adult_data = filter_adults(processed_data)
    average_salary = calculate_average_salary(adult_data)
    print(f"Average salary of adults: ${average_salary:.2f}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous Iterators: Introduced in Python 3.5 with PEP 492.
2. Yield from expression: Introduced in Python 3.3, simplifying delegation to sub-generators.
3. Data Classes with __iter__: Simplifying the creation of iterable data structures.
"""

import asyncio
from dataclasses import dataclass
from typing import AsyncIterator

async def async_range(start: int, stop: int, delay: float) -> AsyncIterator[int]:
    """An asynchronous generator that yields numbers with a delay."""
    for i in range(start, stop):
        await asyncio.sleep(delay)
        yield i

@dataclass
class IterablePoint:
    x: float
    y: float
    z: float
    
    def __iter__(self):
        return iter((self.x, self.y, self.z))

async def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts and emerging trends with iterators."""
    print("Asynchronous Iterator:")
    async for num in async_range(1, 5, 0.5):
        print(num, end=" ")
    print("\n")
    
    print("Iterable Data Class:")
    point = IterablePoint(1.0, 2.0, 3.0)
    for coord in point:
        print(coord, end=" ")
    print("\n")

"""
6. FAQs and Troubleshooting
---------------------------
Q1: What's the difference between an iterable and an iterator?
A1: An iterable is an object that can be iterated over, while an iterator is an object that keeps track of the current position in a sequence.

Q2: How can I create a custom iterator?
A2: Implement the __iter__() and __next__() methods in your class. The __iter__() method should return self, and __next__() should return the next item or raise StopIteration.

Q3: When should I use a generator instead of a regular function?
A3: Use generators when you need to generate a sequence of values over time, especially for large datasets, to save memory and improve performance.

Q4: How can I iterate over multiple iterables in parallel?
A4: Use the zip() function or itertools.zip_longest() if the iterables have different lengths.

Troubleshooting Guide:
1. Iterator raises StopIteration unexpectedly:
   - Check if the iterator is being exhausted prematurely.
   - Ensure that StopIteration is raised at the correct point in custom iterators.

2. Memory usage grows unexpectedly:
   - Avoid converting large iterators to lists unnecessarily.
   - Use itertools functions for efficient chaining and processing of iterators.

3. Infinite loop in custom iterator:
   - Ensure that the __next__() method has a proper termination condition.

4. Slow iteration over large datasets:
   - Consider using generator expressions or itertools functions for better performance.
"""

def troubleshooting_examples():
    """Demonstrate common troubleshooting scenarios."""
    
    # Reusing an exhausted iterator
    numbers = iter([1, 2, 3])
    print("Exhausting iterator:")
    for num in numbers:
        print(num, end=" ")
    print("\nTrying to reuse:")
    for num in numbers:
        print(num, end=" ")  # This won't print anything
    print("\n")
    
    # Memory-efficient processing of large datasets
    def process_large_dataset(data):
        return sum(x * 2 for x in data)  # Using generator expression
    
    large_data = range(1000000)
    result = process_large_dataset(large_data)
    print(f"Result of processing large dataset: {result}")
    
    # Parallel iteration
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. itertools: Standard library module for iterator building blocks.
2. more-itertools: Third-party library extending itertools.
3. yield-from: A library that backports Python 3's 'yield from' to Python 2.
4. pypeln: Library for creating concurrent data pipelines using iterators.

Resources:
- "Fluent Python" by Luciano Ramalho (Chapter 14: Iterables, Iterators, and Generators)
- "Python Cookbook" by David Beazley and Brian K. Jones (Chapter 4: Iterators and Generators)
- Python's official documentation on Iterators: https://docs.python.org/3/tutorial/classes.html#iterators
- Real Python's guide on Iterators and Iterables: https://realpython.com/python-iterators-iterables/
- PEP 234 – Iterators: https://www.python.org/dev/peps/pep-0234/

8. Performance Analysis and Optimization
----------------------------------------
When working with iterators and generators, it's important to consider their performance implications, especially for large datasets or time-critical operations.
"""

import timeit
import cProfile

def performance_analysis():
    """Analyze and compare performance of different iterator implementations."""
    
    # List comprehension vs Generator expression
    def list_squares(n):
        return [x**2 for x in range(n)]
    
    def gen_squares(n):
        return (x**2 for x in range(n))
    
    n = 1000000
    list_time = timeit.timeit(lambda: list_squares(n), number=1)
    gen_time = timeit.timeit(lambda: list(gen_squares(n)), number=1)
    
    print(f"Time to create and consume a list of {n} squares: {list_time:.4f} seconds")
    print(f"Time to create and consume a generator of {n} squares: {gen_time:.4f} seconds")
    print(f"Generator is {list_time/gen_time:.2f}x faster")
    
    # Memory usage analysis
    import tracemalloc
    
    tracemalloc.start()
    list_squares(n)
    list_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    tracemalloc.start()
    list(gen_squares(n))
    gen_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    print(f"\nPeak memory usage for list: {list_memory / 1024 / 1024:.2f} MB")
    print(f"Peak memory usage for generator: {gen_memory / 1024 / 1024:.2f} MB")
    print(f"Generator uses {list_memory / gen_memory:.2f}x less memory")
    
    # Profiling iterator operations
    def process_data(data):
        return sum(x for x in data if x % 2 == 0)
    
    cProfile.runctx('process_data(range(10000000))', globals(), locals(), 'Profile.prof')
    
    import pstats
    from pstats import SortKey
    
    p = pstats.Stats('Profile.prof')
    p.strip_dirs().sort_stats(SortKey.TIME).print_stats(10)

"""
Optimization Strategies:
1. Use generator expressions instead of list comprehensions for large datasets.
2. Leverage itertools functions for efficient chaining and processing of iterators.
3. Use 'yield from' for delegating to sub-generators in complex iterator pipelines.
4. Consider using third-party libraries like 'cytoolz' for performance-critical iterator operations.

Example of optimizing a data processing pipeline:
"""

from itertools import islice, chain
from cytoolz import partition_all, pipe

def optimized_data_processing(data: Iterable[int], chunk_size: int = 1000) -> Iterator[int]:
    """An optimized data processing pipeline using itertools and cytoolz."""
    return pipe(
        data,
        partition_all(chunk_size),  # Process data in chunks
        lambda chunks: chain.from_iterable(  # Flatten the chunks
            (x for x in chunk if x % 2 == 0)  # Filter even numbers
            for chunk in chunks
        ),
        lambda evens: (x ** 2 for x in evens),  # Square the even numbers
    )

def demonstrate_optimization():
    """Demonstrate the optimized data processing pipeline."""
    large_dataset = range(10000000)
    result = sum(islice(optimized_data_processing(large_dataset), 100))
    print(f"Sum of first 100 processed items: {result}")

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
- Relevance to the main topic of iterables and iterators in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to iterables and iterators.
    """
    print("Basic Usage of Iterables and Iterators:")
    demonstrate_basic_usage()
    
    print("\nGenerator Function Example:")
    demonstrate_generator()
    
    print("\nBatch Processing Example:")
    demonstrate_batch_processing()
    
    print("\nAdvanced Techniques:")
    demonstrate_advanced_techniques()
    
    print("\nReal-World Application:")
    demonstrate_real_world_application()
    
    print("\nAdvanced Concepts:")
    asyncio.run(demonstrate_advanced_concepts())
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Analysis:")
    performance_analysis()
    
    print("\nOptimized Data Processing:")
    demonstrate_optimization()

if __name__ == "__main__":
    main()