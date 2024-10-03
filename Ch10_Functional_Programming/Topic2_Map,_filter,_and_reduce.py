"""
Functional Programming - Map, filter, and reduce - in the Python Programming Language
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
Map, filter, and reduce are fundamental concepts in functional programming, providing powerful tools for data transformation and analysis. These higher-order functions allow for concise, expressive code that operates on iterables without explicit loops.

Historical context:
- The concepts of map, filter, and reduce originated in Lisp, one of the earliest functional programming languages, in the 1960s.
- Python introduced these functions in version 1.0 (1994) as part of its functional programming support.
- In Python 3.0 (2008), map and filter were changed to return iterators instead of lists for improved memory efficiency.
- The reduce function was moved to the functools module in Python 3.0 to declutter the built-in namespace.

Significance:
- These functions promote a declarative programming style, focusing on what to do rather than how to do it.
- They encourage immutability and pure functions, leading to more predictable and testable code.
- Map, filter, and reduce are fundamental building blocks for more complex functional programming patterns.

Common use cases:
- Map: Applying a function to each element in an iterable (e.g., data transformation).
- Filter: Selecting elements from an iterable based on a predicate function.
- Reduce: Aggregating elements of an iterable into a single value (e.g., sum, product).

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from functools import reduce
from typing import List, Callable, Any, TypeVar, Iterable
import time
import random

T = TypeVar('T')
U = TypeVar('U')

def demonstrate_map(numbers: List[int]) -> List[int]:
    """
    Demonstrate the usage of the map function.
    
    Args:
    numbers (List[int]): A list of integers to be squared.
    
    Returns:
    List[int]: A new list with each number squared.
    """
    # Using map with a lambda function
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers: {squared}")
    
    # Using map with a named function
    def cube(x: int) -> int:
        return x**3
    
    cubed = list(map(cube, numbers))
    print(f"Cubed numbers: {cubed}")
    
    return squared

def demonstrate_filter(numbers: List[int]) -> List[int]:
    """
    Demonstrate the usage of the filter function.
    
    Args:
    numbers (List[int]): A list of integers to be filtered.
    
    Returns:
    List[int]: A new list containing only the even numbers.
    """
    # Using filter with a lambda function
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Using filter with a named function
    def is_positive(x: int) -> bool:
        return x > 0
    
    positives = list(filter(is_positive, numbers))
    print(f"Positive numbers: {positives}")
    
    return evens

def demonstrate_reduce(numbers: List[int]) -> int:
    """
    Demonstrate the usage of the reduce function.
    
    Args:
    numbers (List[int]): A list of integers to be reduced.
    
    Returns:
    int: The product of all numbers in the list.
    """
    # Using reduce to calculate the product of all numbers
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of numbers: {product}")
    
    # Using reduce with a named function to find the maximum
    def max_value(x: int, y: int) -> int:
        return x if x > y else y
    
    maximum = reduce(max_value, numbers)
    print(f"Maximum value: {maximum}")
    
    return product

def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Compose multiple functions into a single function.
    
    Args:
    *funcs: Variable number of functions to be composed.
    
    Returns:
    Callable: A new function that applies all the input functions in reverse order.
    """
    def composition(x: Any) -> Any:
        for func in reversed(funcs):
            x = func(x)
        return x
    return composition

def demonstrate_function_composition(numbers: List[int]) -> List[int]:
    """
    Demonstrate function composition using map, filter, and reduce.
    
    Args:
    numbers (List[int]): A list of integers to be processed.
    
    Returns:
    List[int]: The result of applying the composed functions to the input list.
    """
    # Define individual functions
    square = lambda x: x**2
    is_even = lambda x: x % 2 == 0
    sum_list = lambda x, y: x + y
    
    # Compose functions: square the numbers, filter even ones, and sum them
    processed = reduce(sum_list, filter(is_even, map(square, numbers)))
    print(f"Sum of squares of even numbers: {processed}")
    
    # Using the compose function for a more complex operation
    complex_operation = compose(
        lambda x: list(filter(lambda y: y < 50, x)),
        lambda x: list(map(lambda y: y * 3, x)),
        lambda x: reduce(lambda a, b: a + b, x)
    )
    
    result = complex_operation(numbers)
    print(f"Result of complex operation: {result}")
    
    return result

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use map, filter, and reduce for their intended purposes to improve code readability.
2. Prefer list comprehensions for simple operations when working with lists.
3. Use generator expressions instead of map and filter for memory efficiency when dealing with large datasets.
4. Keep lambda functions simple; use named functions for complex operations.
5. Use type hints to improve code clarity and catch potential errors early.

Common Pitfalls:
1. Overusing map, filter, and reduce can lead to less readable code, especially with complex operations.
2. Forgetting that map and filter return iterators in Python 3, which may need to be converted to lists.
3. Using reduce for operations that have simpler built-in alternatives (e.g., sum, max, min).
4. Modifying the iterable being processed within the function passed to map, filter, or reduce.

Advanced Tips:
1. Use functools.partial to create partially applied functions for use with map, filter, and reduce.
2. Combine map, filter, and reduce for more complex data transformations.
3. Utilize the itertools module for additional functional programming tools.
4. Implement lazy evaluation using generator expressions with map and filter for improved performance.
"""

from functools import partial
from itertools import accumulate, groupby

def demonstrate_advanced_techniques(numbers: List[int]) -> None:
    """
    Demonstrate advanced techniques using map, filter, reduce, and related concepts.
    
    Args:
    numbers (List[int]): A list of integers to be processed.
    """
    # Using partial application
    def power(base: int, exponent: int) -> int:
        return base ** exponent
    
    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    
    squared_numbers = list(map(square, numbers))
    cubed_numbers = list(map(cube, numbers))
    print(f"Squared numbers: {squared_numbers}")
    print(f"Cubed numbers: {cubed_numbers}")
    
    # Using itertools.accumulate (similar to reduce, but returns intermediate results)
    running_sum = list(accumulate(numbers))
    print(f"Running sum: {running_sum}")
    
    # Using itertools.groupby for more complex grouping operations
    sorted_numbers = sorted(numbers, key=lambda x: x % 2)  # Sort by even/odd
    grouped = {k: list(v) for k, v in groupby(sorted_numbers, key=lambda x: x % 2)}
    print(f"Grouped by even/odd: {grouped}")
    
    # Lazy evaluation with generator expressions
    large_dataset = range(1000000)
    lazy_squares = (x**2 for x in large_dataset if x % 2 == 0)
    print(f"First 10 even squares: {list(next(lazy_squares) for _ in range(10))}")

"""
4. Integration and Real-World Applications
------------------------------------------
Map, filter, and reduce are widely used in various Python libraries and frameworks:

1. Pandas: These functions are often used in conjunction with DataFrame operations for data manipulation.
2. PySpark: The map and reduce paradigm is fundamental to distributed computing frameworks like Apache Spark.
3. NumPy: While NumPy has its own vectorized operations, map and filter concepts are still applicable for certain tasks.

Real-world example: Data Processing Pipeline
"""

import csv
from datetime import datetime
from typing import Dict, List

def load_data(file_path: str) -> List[Dict[str, str]]:
    """Load data from a CSV file."""
    with open(file_path, 'r') as f:
        return list(csv.DictReader(f))

def process_sales_data(sales_data: List[Dict[str, str]]) -> Dict[str, float]:
    """Process sales data using map, filter, and reduce."""
    # Convert string dates to datetime objects
    sales_data = list(map(lambda x: {**x, 'date': datetime.strptime(x['date'], '%Y-%m-%d')}, sales_data))
    
    # Filter sales from the year 2023
    sales_2023 = list(filter(lambda x: x['date'].year == 2023, sales_data))
    
    # Calculate total sales per product
    def aggregate_sales(acc: Dict[str, float], sale: Dict[str, Any]) -> Dict[str, float]:
        product = sale['product']
        amount = float(sale['amount'])
        acc[product] = acc.get(product, 0) + amount
        return acc
    
    total_sales = reduce(aggregate_sales, sales_2023, {})
    
    return total_sales

def demonstrate_real_world_application():
    """Demonstrate a real-world application of map, filter, and reduce in a data processing pipeline."""
    # Simulate loading data from a CSV file
    sales_data = [
        {'date': '2023-01-15', 'product': 'A', 'amount': '100.50'},
        {'date': '2023-02-20', 'product': 'B', 'amount': '200.75'},
        {'date': '2023-03-10', 'product': 'A', 'amount': '150.25'},
        {'date': '2022-12-05', 'product': 'C', 'amount': '300.00'},
    ]
    
    total_sales = process_sales_data(sales_data)
    print("Total sales per product in 2023:")
    for product, amount in total_sales.items():
        print(f"{product}: ${amount:.2f}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Monads: A more advanced functional programming concept that's gaining traction in Python (e.g., the 'returns' library).
2. Property-based testing: Libraries like Hypothesis use functional concepts for generating test cases.
3. Functional reactive programming: Libraries like RxPY bring reactive programming paradigms to Python.
4. Type theory and dependent types: Advanced type systems that allow for more expressive functional programming patterns.
"""

from typing import Callable, List, TypeVar

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

def compose2(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    """Compose two functions."""
    return lambda x: f(g(x))

def demonstrate_advanced_concepts():
    """Demonstrate some advanced functional programming concepts."""
    # Function composition with types
    def double(x: int) -> int:
        return x * 2
    
    def increment(x: int) -> int:
        return x + 1
    
    double_then_increment = compose2(increment, double)
    increment_then_double = compose2(double, increment)
    
    print(f"Double then increment: {double_then_increment(5)}")
    print(f"Increment then double: {increment_then_double(5)}")
    
    # Currying
    def curry2(f: Callable[[A, B], C]) -> Callable[[A], Callable[[B], C]]:
        return lambda x: lambda y: f(x, y)
    
    def add(x: int, y: int) -> int:
        return x + y
    
    curried_add = curry2(add)
    add_5 = curried_add(5)
    
    print(f"Curried add: {add_5(3)}")
    
    # Lazy sequences (similar to Haskell's infinite lists)
    def naturals():
        n = 1
        while True:
            yield n
            n += 1
    
    def take(n: int, iterable: Iterable[A]) -> List[A]:
        return list(next(iterable) for _ in range(n))
    
    print(f"First 10 natural numbers: {take(10, naturals())}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use map/filter vs. list comprehensions?
A: Use map and filter when working with functions or when chaining multiple operations. List comprehensions are often more readable for simple transformations on lists.

Q: How can I debug functional-style code?
A: Use the `functools.partial` to create intermediate functions for debugging. You can also convert iterators to lists at various stages to inspect intermediate results.

Q: Is functional programming in Python as efficient as imperative programming?
A: For most cases, the performance difference is negligible. However, for very large datasets or performance-critical code, imperative style might be faster. Always profile your code to make informed decisions.

Q: How do I handle exceptions in functional-style code?
A: You can wrap your functions in try-except blocks or use libraries like `toolz` that provide functional-style error handling.

Troubleshooting:
1. If map or filter seem to return empty results, remember they return iterators. Convert to a list or use a for loop to consume the iterator.
2. When using reduce, always provide an initial value to handle empty iterables and to clarify the operation's starting point.
3. If you're experiencing high memory usage, consider using generator expressions instead of map and filter for lazy evaluation.
"""

def troubleshooting_examples():
    """Demonstrate solutions to common issues with map, filter, and reduce."""
    # Problem: map returns an iterator, which might seem empty
    numbers = [1, 2, 3, 4, 5]
    squared = map(lambda x: x**2, numbers)
    print(f"Squared (as iterator): {squared}")
    print(f"Squared (as list): {list(squared)}")
    
    # Problem: reduce with no initial value can raise an error on empty iterables
    try:
        reduce(lambda x, y: x + y, [])
    except TypeError as e:
        print(f"Error with empty reduce: {e}")
    
    # Solution: Always provide an initial value
    sum_empty = reduce(lambda x, y: x + y, [], 0)
    print(f"Sum of empty list with initial value: {sum_empty}")
    
    # Problem: High memory usage with large datasets
    large_dataset = range(1000000)
    # This could consume a lot of memory:
    # squares = list(map(lambda x: x**2, large_dataset))
    
    # Solution: Use generator expressions for lazy evaluation
    lazy_squares = (x**2 for x in large_dataset)
    print(f"First 5 squares (lazy evaluation): {[next(lazy_squares) for _ in range(5)]}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. functools: Built-in module providing higher-order functions and operations on callable objects.
2. itertools: Built-in module with iterators for efficient looping.
3. toolz: A set of utility functions for iterators, functions, and dictionaries.
4. fn.py: Implement missing features to support functional programming in Python.
5. cytoolz: A Cython implementation of toolz for improved performance.

Resources:
- "Functional Programming in Python" by David Mertz
- "Python Functional Programming HOWTO" in the official Python documentation
- "Functional Programming HOWTO" by A. M. Kuchling
- "Learn Functional Python in 10 Minutes" by Christophe Leys on Medium
- Real Python's guide on Functional Programming in Python: https://realpython.com/python-functional-programming/

8. Performance Analysis and Optimization
----------------------------------------
When working with functional programming concepts like map, filter, and reduce, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def performance_comparison():
    """Compare performance of functional vs imperative approaches."""
    data = list(range(10000))
    
    def functional_approach():
        return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))
    
    def list_comprehension():
        return [x**2 for x in data if x % 2 == 0]
    
    def imperative_approach():
        result = []
        for x in data:
            if x % 2 == 0:
                result.append(x**2)
        return result
    
    functional_time = timeit.timeit(functional_approach, number=1000)
    comprehension_time = timeit.timeit(list_comprehension, number=1000)
    imperative_time = timeit.timeit(imperative_approach, number=1000)
    
    print(f"Functional approach time: {functional_time:.6f} seconds")
    print(f"List comprehension time: {comprehension_time:.6f} seconds")
    print(f"Imperative approach time: {imperative_time:.6f} seconds")

"""
Performance Considerations:
1. Map and filter return iterators, which can be more memory-efficient for large datasets.
2. Reduce can be less efficient than built-in functions for simple operations (e.g., sum, max, min).
3. List comprehensions are often faster than map and filter for simple operations on lists.
4. Lambda functions can be slightly slower than named functions due to their creation overhead.

Optimization Strategies:
1. Use built-in functions when possible (e.g., sum instead of reduce for summing numbers).
2. Consider using list comprehensions for simple operations on lists.
3. Use generator expressions for lazy evaluation when working with large datasets.
4. Profile your code to identify bottlenecks before optimizing.
"""

def optimize_reduce_operation(numbers):
    """Demonstrate optimization of a reduce operation."""
    print("Optimizing a reduce operation:")
    
    def slow_sum():
        return reduce(lambda x, y: x + y, numbers)
    
    def fast_sum():
        return sum(numbers)
    
    slow_time = timeit.timeit(slow_sum, number=10000)
    fast_time = timeit.timeit(fast_sum, number=10000)
    
    print(f"Slow sum (reduce) time: {slow_time:.6f} seconds")
    print(f"Fast sum (built-in) time: {fast_time:.6f} seconds")
    print(f"Speed improvement: {slow_time / fast_time:.2f}x")

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
- Relevance to the main topic of map, filter, and reduce in Python's functional programming.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to map, filter, and reduce.
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Basic demonstrations:")
    demonstrate_map(numbers)
    demonstrate_filter(numbers)
    demonstrate_reduce(numbers)
    
    print("\nFunction composition:")
    demonstrate_function_composition(numbers)
    
    print("\nAdvanced techniques:")
    demonstrate_advanced_techniques(numbers)
    
    print("\nReal-world application:")
    demonstrate_real_world_application()
    
    print("\nAdvanced concepts:")
    demonstrate_advanced_concepts()
    
    print("\nTroubleshooting examples:")
    troubleshooting_examples()
    
    print("\nPerformance comparison:")
    performance_comparison()
    
    print("\nOptimization example:")
    optimize_reduce_operation(numbers)

if __name__ == "__main__":
    main()