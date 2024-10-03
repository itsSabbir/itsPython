"""
Functional Programming - Partial functions - in the Python Programming Language
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
Partial functions are a powerful concept in functional programming that allows for the creation of new functions by fixing a subset of arguments of an existing function. This technique, also known as partial application, enhances code reusability and enables more expressive and concise programming.

Historical context:
- The concept of partial functions originates from lambda calculus and combinatory logic, fundamental theories in computer science developed in the 1930s.
- In Python, partial functions were introduced with the functools module in Python 2.5 (2006).
- The implementation in Python was inspired by similar concepts in functional programming languages like Haskell and ML.

Significance:
- Partial functions allow for function specialization, creating more specific functions from general ones.
- They promote code reuse by allowing the creation of new functions without duplicating code.
- Partial functions are a key component in function composition and currying, advanced functional programming techniques.

Common use cases:
- Configuring functions with default parameters for specific use cases.
- Callback functions in event-driven programming.
- Creating families of related functions with shared behavior.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from functools import partial
from typing import Callable, Any, List, Dict
import time

def demonstrate_basic_partial():
    """Demonstrate basic usage of partial functions."""
    
    def power(base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent."""
        return base ** exponent
    
    # Create a partial function for squaring numbers
    square = partial(power, exponent=2)
    
    print(f"Square of 5: {square(5)}")
    print(f"Square of 10: {square(10)}")
    
    # Create a partial function for cubing numbers
    cube = partial(power, exponent=3)
    
    print(f"Cube of 3: {cube(3)}")
    print(f"Cube of 4: {cube(4)}")

def demonstrate_partial_with_multiple_args():
    """Demonstrate partial functions with multiple arguments."""
    
    def greet(greeting: str, name: str, punctuation: str) -> str:
        """Generate a personalized greeting."""
        return f"{greeting}, {name}{punctuation}"
    
    # Create partial functions with different greetings
    hello = partial(greet, greeting="Hello")
    goodbye = partial(greet, greeting="Goodbye")
    
    print(hello(name="Alice", punctuation="!"))
    print(goodbye(name="Bob", punctuation="."))
    
    # Create a more specific partial function
    casual_hello = partial(greet, greeting="Hey", punctuation="!")
    
    print(casual_hello(name="Charlie"))

def demonstrate_partial_in_higher_order_functions():
    """Demonstrate the use of partial functions in higher-order functions."""
    
    def apply_operation(operation: Callable[[int, int], int], x: int, y: int) -> int:
        """Apply a binary operation to two integers."""
        return operation(x, y)
    
    def arithmetic_operation(operator: str, x: int, y: int) -> int:
        """Perform an arithmetic operation based on the operator string."""
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b
        }
        return operations[operator](x, y)
    
    # Create partial functions for specific arithmetic operations
    add = partial(arithmetic_operation, '+')
    subtract = partial(arithmetic_operation, '-')
    multiply = partial(arithmetic_operation, '*')
    divide = partial(arithmetic_operation, '/')
    
    print(f"Addition: {apply_operation(add, 10, 5)}")
    print(f"Subtraction: {apply_operation(subtract, 10, 5)}")
    print(f"Multiplication: {apply_operation(multiply, 10, 5)}")
    print(f"Division: {apply_operation(divide, 10, 5)}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use partial functions to create specialized versions of more general functions.
2. Prefer partial over lambda for creating simple function variations.
3. Use meaningful names for partial functions to enhance code readability.
4. Consider using partial for callback functions to avoid creating many similar small functions.

Common Pitfalls:
1. Overusing partial functions, leading to code that's hard to understand.
2. Forgetting that partial functions are objects, not the original function.
3. Inadvertently modifying mutable default arguments in partial functions.
4. Not considering the performance implications of creating many partial functions.

Advanced Tips:
1. Combine partial functions with decorators for powerful function transformations.
2. Use partial functions in method definitions for class customization.
3. Leverage partial functions for dependency injection in complex systems.
4. Utilize partial functions in combination with map, filter, and reduce for data processing pipelines.
"""

def demonstrate_advanced_partial_techniques():
    """Demonstrate advanced techniques using partial functions."""
    
    def retry(func: Callable[..., Any], max_attempts: int, delay: float) -> Callable[..., Any]:
        """A decorator that retries a function with a delay between attempts."""
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    
    @retry(max_attempts=3, delay=1)
    def unreliable_network_call(url: str) -> str:
        """Simulate an unreliable network call."""
        if random.random() < 0.7:
            raise ConnectionError("Network error")
        return f"Data from {url}"
    
    # Create a partial function for a specific API endpoint
    get_user_data = partial(unreliable_network_call, url="https://api.example.com/user")
    
    try:
        result = get_user_data()
        print(f"User data: {result}")
    except ConnectionError:
        print("Failed to retrieve user data after multiple attempts")

"""
4. Integration and Real-World Applications
------------------------------------------
Partial functions are widely used in various Python libraries and frameworks:

1. Django: For creating reusable view functions with pre-set parameters.
2. Scikit-learn: In machine learning pipelines for parameter fixing in estimators.
3. Asyncio: For creating callback functions with pre-defined event loop and context.

Real-world example: Configurable Data Processing Pipeline
"""

def process_data(data: List[Dict[str, Any]], operations: List[Callable[[Dict[str, Any]], Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """Process data through a series of operations."""
    for operation in operations:
        data = [operation(item) for item in data]
    return data

def filter_by_field(item: Dict[str, Any], field: str, value: Any) -> Dict[str, Any]:
    """Filter data based on a field value."""
    return item if item.get(field) == value else {}

def transform_field(item: Dict[str, Any], field: str, func: Callable[[Any], Any]) -> Dict[str, Any]:
    """Transform a field in the data item."""
    if field in item:
        item[field] = func(item[field])
    return item

def demonstrate_real_world_application():
    """Demonstrate a real-world application of partial functions in a data processing pipeline."""
    
    data = [
        {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
        {"id": 2, "name": "Bob", "age": 25, "city": "Los Angeles"},
        {"id": 3, "name": "Charlie", "age": 35, "city": "New York"},
        {"id": 4, "name": "David", "age": 28, "city": "Chicago"}
    ]
    
    # Create partial functions for specific data operations
    filter_by_city = partial(filter_by_field, field="city", value="New York")
    increment_age = partial(transform_field, field="age", func=lambda x: x + 1)
    uppercase_name = partial(transform_field, field="name", func=str.upper)
    
    # Define the data processing pipeline
    pipeline = [
        filter_by_city,
        increment_age,
        uppercase_name
    ]
    
    # Process the data
    processed_data = process_data(data, pipeline)
    
    print("Processed data:")
    for item in processed_data:
        if item:  # Filter out empty dictionaries
            print(item)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Currying: A technique closely related to partial application, where a function with multiple arguments is transformed into a sequence of functions, each with a single argument.
2. Function composition: Combining partial functions to create more complex operations.
3. Monads: Advanced functional programming concept that can leverage partial functions for powerful abstractions.
4. Type hinting for partial functions: Ongoing improvements in static type checking for partial functions in Python.
"""

from typing import TypeVar, Callable

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

def compose(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    """Compose two functions."""
    return lambda x: f(g(x))

def demonstrate_advanced_concepts():
    """Demonstrate advanced functional programming concepts related to partial functions."""
    
    def add(x: int, y: int) -> int:
        return x + y
    
    def multiply(x: int, y: int) -> int:
        return x * y
    
    # Currying
    def curry(func: Callable[[T, U], V]) -> Callable[[T], Callable[[U], V]]:
        def curried(x: T) -> Callable[[U], V]:
            return lambda y: func(x, y)
        return curried
    
    curried_add = curry(add)
    add_5 = curried_add(5)
    print(f"Curried add: 5 + 3 = {add_5(3)}")
    
    # Function composition with partial functions
    times_2 = partial(multiply, 2)
    plus_3 = partial(add, 3)
    
    composed_func = compose(times_2, plus_3)
    print(f"Composed function: (3 + 3) * 2 = {composed_func(3)}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do partial functions differ from default arguments?
A: Partial functions create new function objects, allowing for more flexibility and dynamic creation of specialized functions. Default arguments are fixed at function definition.

Q: Can I use partial functions with instance methods?
A: Yes, but you need to be careful with the 'self' parameter. Use `partial(Class.method, instance)` or `partial(instance.method)` depending on your needs.

Q: How do I handle errors in partial functions?
A: Errors in partial functions are generally handled the same way as in the original function. However, be aware that errors in argument binding will occur when creating the partial function, not when calling it.

Troubleshooting:
1. If a partial function is not behaving as expected, check the order and naming of arguments in both the original function and the partial application.
2. For performance issues, consider whether creating many partial functions is necessary, or if a different approach might be more efficient.
3. When using partial functions with mutable default arguments, be aware of potential side effects and unexpected behavior.
"""

def troubleshooting_examples():
    """Demonstrate solutions to common issues with partial functions."""
    
    class Example:
        def method(self, x: int, y: int) -> int:
            return x + y
    
    instance = Example()
    
    # Correct way to create a partial method
    partial_method = partial(Example.method, instance, 10)
    print(f"Partial method result: {partial_method(5)}")
    
    # Handling mutable default arguments
    def append_to_list(x: int, lst: List[int] = []) -> List[int]:
        lst.append(x)
        return lst
    
    # Incorrect way (shared list among all calls)
    partial_append = partial(append_to_list, 1)
    print(f"Incorrect partial append: {partial_append()}")
    print(f"Incorrect partial append (second call): {partial_append()}")
    
    # Correct way (new list for each call)
    partial_append_correct = partial(append_to_list, 1, lst=[])
    print(f"Correct partial append: {partial_append_correct()}")
    print(f"Correct partial append (second call): {partial_append_correct()}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. functools: Built-in Python module containing the partial function and other functional programming tools.
2. toolz: A library for functional programming in Python, which includes advanced partial application utilities.
3. fn.py: A library for functional programming in Python that provides additional utilities for working with partial functions.
4. PyMonad: A library implementing monadic concepts in Python, which can be combined with partial functions for powerful abstractions.

Resources:
- "Functional Programming in Python" by David Mertz
- "Python Cookbook" by David Beazley and Brian K. Jones (Chapter on metaprogramming and partial functions)
- Python's official documentation on functools.partial: https://docs.python.org/3/library/functools.html#functools.partial
- Real Python's guide on partial functions: https://realpython.com/python-functools-module/#partial-functions
- "Learn Functional Python in 10 Minutes" by Christophe Leys on Medium

8. Performance Analysis and Optimization
----------------------------------------
When working with partial functions, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def performance_comparison():
    """Compare performance of partial functions vs. regular functions."""
    
    def regular_func(x: int, y: int) -> int:
        return x + y
    
    partial_func = partial(regular_func, 10)
    
    def regular_call():
        return regular_func(10, 5)
    
    def partial_call():
        return partial_func(5)
    
    regular_time = timeit.timeit(regular_call, number=1000000)
    partial_time = timeit.timeit(partial_call, number=1000000)
    
    print(f"Regular function time: {regular_time:.6f} seconds")
    print(f"Partial function time: {partial_time:.6f} seconds")
    print(f"Overhead: {(partial_time - regular_time) / regular_time * 100:.2f}%")

"""
Performance Considerations:
1. Creating a partial function has a small overhead, which can add up if done frequently.
2. Partial functions can be slightly slower than regular function calls due to the additional function call and attribute lookups.
3. The memory footprint of partial functions should be considered when creating many specialized functions.

Optimization Strategies:
1. Create partial functions outside of loops or frequently called functions to avoid repeated creation.
2. Use `__slots__` in custom partial function implementations to reduce memory usage.
3. Consider using `lru_cache` from functools to memoize partial functions for expensive computations.
4. For performance-critical code, compare the performance of partial functions with alternative implementations.

Example of optimizing partial functions:
"""

from functools import lru_cache

def optimize_partial_functions():
    """Demonstrate optimization techniques for partial functions."""
    
    @lru_cache(maxsize=None)
    def expensive_computation(x: int, y: int) -> int:
        """Simulate an expensive computation."""
        time.sleep(0.1)  # Simulate computation time
        return x ** y
    
    # Create a partial function for squaring numbers
    square = partial(expensive_computation, y=2)
    
    # Measure time for multiple calls
    start_time = time.time()
    for i in range(10):
        square(i)
    end_time = time.time()
    
    print(f"Time taken for 10 calls: {end_time - start_time:.2f} seconds")
    
    # Subsequent calls will be much faster due to caching
    start_time = time.time()
    for i in range(10):
        square(i)
    end_time = time.time()
    
    print(f"Time taken for 10 cached calls: {end_time - start_time:.2f} seconds")

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
- Relevance to the main topic of partial functions in Python's functional programming paradigm.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to partial functions.
    """
    print("Basic Partial Function Usage:")
    demonstrate_basic_partial()
    
    print("\nPartial Functions with Multiple Arguments:")
    demonstrate_partial_with_multiple_args()
    
    print("\nPartial Functions in Higher-Order Functions:")
    demonstrate_partial_in_higher_order_functions()
    
    print("\nAdvanced Partial Function Techniques:")
    demonstrate_advanced_partial_techniques()
    
    print("\nReal-World Application of Partial Functions:")
    demonstrate_real_world_application()
    
    print("\nAdvanced Functional Programming Concepts:")
    demonstrate_advanced_concepts()
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Comparison:")
    performance_comparison()
    
    print("\nOptimizing Partial Functions:")
    optimize_partial_functions()

if __name__ == "__main__":
    main()