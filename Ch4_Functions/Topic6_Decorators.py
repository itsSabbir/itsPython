# Functions - Decorators - in the Python Programming Language
# Author: Sabbir Hossain
# Last Updated: September 19, 2024

"""
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
"""

import time
import functools
from typing import Any, Callable, TypeVar, cast
import asyncio

# Type variable for generic function type
F = TypeVar('F', bound=Callable[..., Any])

# 1. Overview and Historical Context
"""
Decorators in Python are a powerful way to modify or enhance functions or classes
without directly changing their source code. They allow for a clean separation of
concerns and promote code reuse.

Key aspects:
- Decorators are functions that take another function (or class) as an argument
- They return a new function (or class) that usually extends the behavior of the input
- Syntactically, decorators are denoted by the '@' symbol followed by the decorator name

Historical context:
- Introduced in Python 2.4 (2004) as part of PEP 318
- Inspired by Java annotations and similar concepts in other languages
- Initially only for functions, class decorators were added in Python 2.6 (2008)
- Significant enhancements in Python 3.x, including better integration with type hinting
- PEP 3129 (2007) introduced class decorators
- PEP 614 (2020) allowed more flexible decorator syntax in Python 3.9

Decorators align with Python's philosophy of providing powerful, expressive tools to developers.
They are widely used in modern Python development for various purposes, including
logging, authentication, memoization, and more.
"""

# 2. Syntax, Key Concepts, and Code Examples

# Basic function decorator
def simple_decorator(func: F) -> F:
    """
    A simple decorator that prints a message before and after the function call.
    
    Args:
        func (Callable): The function to be decorated.
    
    Returns:
        Callable: The wrapped function.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return cast(F, wrapper)

@simple_decorator
def greet(name: str) -> str:
    """A simple greeting function."""
    return f"Hello, {name}!"

# Decorator with arguments
def repeat(times: int) -> Callable[[F], F]:
    """
    A decorator that repeats the function call a specified number of times.
    
    Args:
        times (int): Number of times to repeat the function call.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return cast(F, wrapper)
    return decorator

@repeat(3)
def say_hello(name: str) -> None:
    """Says hello to the given name."""
    print(f"Hello, {name}!")

# Class decorator
def singleton(cls: type) -> type:
    """
    A decorator that ensures only one instance of a class is created.
    
    Args:
        cls (type): The class to be decorated.
    
    Returns:
        type: The modified class.
    """
    instances = {}
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    """A singleton database connection class."""
    def __init__(self) -> None:
        self.connection = "Connected to database"

# 3. Best Practices, Common Pitfalls, and Advanced Tips

"""
Best Practices:
1. Use functools.wraps to preserve metadata of the decorated function
2. Keep decorators simple and focused on a single responsibility
3. Use type hints to improve code readability and catch type-related errors
4. Consider making decorators optional by using default arguments

Common Pitfalls:
1. Forgetting to use @functools.wraps, which can lead to loss of function metadata
2. Overusing decorators, which can make code harder to understand
3. Not handling all possible arguments (*args, **kwargs) in the wrapper function
4. Modifying mutable arguments in decorators, leading to unexpected side effects

Advanced Tips:
1. Use classes as decorators for more complex scenarios
2. Implement decorators that can be used with or without arguments
3. Utilize decorators for aspect-oriented programming (e.g., logging, timing)
4. Combine multiple decorators to build complex behavior
"""

# Example of a class-based decorator
class Timer:
    """A class-based decorator for timing function execution."""
    def __init__(self, print_result: bool = True) -> None:
        self.print_result = print_result

    def __call__(self, func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if self.print_result:
                print(f"{func.__name__} took {execution_time:.4f} seconds to execute.")
            return result
        return cast(F, wrapper)

@Timer()
def slow_function() -> None:
    """A function that simulates a time-consuming operation."""
    time.sleep(1)

# 4. Integration and Real-World Applications

"""
Real-world applications of decorators:

1. Web Frameworks:
   - Route definition in Flask and Django
   - Authentication and authorization checks

2. ORM (Object-Relational Mapping):
   - Defining relationships between database tables

3. Caching:
   - Memoization of expensive function calls

4. Logging and Monitoring:
   - Automatic logging of function calls and performance metrics

5. API Development:
   - Rate limiting and request validation

Example: A simple caching decorator
"""

def memoize(func: F) -> F:
    """
    A decorator that caches the results of a function.
    
    Args:
        func (Callable): The function to be memoized.
    
    Returns:
        Callable: The memoized function.
    """
    cache = {}
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return cast(F, wrapper)

@memoize
def fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 5. Advanced Concepts and Emerging Trends

"""
Advanced Concepts:
1. Decorator factories for creating customizable decorators
2. Using decorators with asynchronous functions (async/await)
3. Implementing decorators that work with both functions and classes
4. Leveraging decorators for dependency injection

Emerging Trends:
1. Enhanced integration with type hinting systems (PEP 612)
2. Use of decorators in data validation and schema definition
3. Application of decorators in metaprogramming and code generation
"""

# Example of a decorator for async functions
def async_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator for timing asynchronous function execution.
    
    Args:
        func (Callable): The async function to be timed.
    
    Returns:
        Callable: The wrapped async function.
    """
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@async_timer
async def async_slow_function() -> None:
    """An async function that simulates a time-consuming operation."""
    await asyncio.sleep(1)

# 6. FAQs and Troubleshooting

"""
Q1: Can decorators be applied to methods within a class?
A1: Yes, decorators can be applied to methods, including static and class methods.

Q2: How can I create a decorator that takes optional arguments?
A2: Use a decorator factory that returns the actual decorator based on the arguments.

Q3: Can multiple decorators be applied to a single function?
A3: Yes, multiple decorators can be stacked. They are applied from bottom to top.

Troubleshooting:
1. Lost function metadata:
   Solution: Use @functools.wraps in your decorator implementation.

2. Decorator changing function signature:
   Solution: Ensure your wrapper function accepts *args and **kwargs.

3. Decorators not working with async functions:
   Solution: Implement async-aware decorators using 'async def' and 'await'.
"""

# 7. Recommended Tools, Libraries, and Resources

"""
Tools and Libraries:
1. functools: Provides utilities for working with functions and decorators
2. wrapt: A library for building decorators with advanced features
3. decorator: Simplifies the creation of signature-preserving decorators
4. PyContracts: Uses decorators for runtime contract checking

Resources:
1. "Fluent Python" by Luciano Ramalho
2. "Effective Python" by Brett Slatkin
3. Python Documentation: https://docs.python.org/3/reference/compound_stmts.html#function
4. Real Python tutorial: https://realpython.com/primer-on-python-decorators/
"""

# 8. Performance Analysis and Optimization

def benchmark(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Benchmarks the execution time of a function.
    
    Args:
        func (Callable): The function to benchmark.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    
    Returns:
        float: The execution time in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# Example of optimizing a decorator
def optimized_memoize(func: F) -> F:
    """
    An optimized version of the memoize decorator using lru_cache.
    
    Args:
        func (Callable): The function to be memoized.
    
    Returns:
        Callable: The memoized function.
    """
    @functools.lru_cache(maxsize=None)
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return cast(F, wrapper)

@optimized_memoize
def optimized_fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number using optimized memoization."""
    if n < 2:
        return n
    return optimized_fibonacci(n-1) + optimized_fibonacci(n-2)

# Main function to demonstrate concepts
async def main() -> None:
    print("1. Basic decorator usage:")
    print(greet("Alice"))

    print("\n2. Decorator with arguments:")
    say_hello("Bob")

    print("\n3. Class decorator (Singleton):")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"db1 is db2: {db1 is db2}")

    print("\n4. Class-based decorator (Timer):")
    slow_function()

    print("\n5. Memoization decorator:")
    start_time = time.time()
    result = fibonacci(30)
    end_time = time.time()
    print(f"Fibonacci(30) = {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

    print("\n6. Async decorator:")
    await async_slow_function()

    print("\n7. Performance comparison:")
    normal_time = benchmark(fibonacci, 30)
    optimized_time = benchmark(optimized_fibonacci, 30)
    print(f"Normal memoized fibonacci time: {normal_time:.4f} seconds")
    print(f"Optimized memoized fibonacci time: {optimized_time:.4f} seconds")
    print(f"Speedup factor: {normal_time / optimized_time:.2f}x")

if __name__ == "__main__":
    asyncio.run(main())

"""
Conclusion:

This comprehensive guide covers the intricacies of decorators in Python. Decorators
provide a powerful and flexible way to modify or enhance functions and classes without
altering their source code. Key takeaways include:

1. Decorators offer a clean and reusable approach to extending functionality.
2. They are widely used in modern Python development for various purposes, including
   logging, authentication, and performance optimization.
3. Understanding best practices and potential pitfalls is crucial for effective usage.
4. Advanced decorator techniques can lead to more maintainable and efficient code.
5. Decorators integrate well with other Python features, including asynchronous programming
   and type hinting.

As Python continues to evolve, decorators remain a fundamental feature, enabling developers
to write more modular, readable, and maintainable code. Mastering decorators is essential
for writing pythonic code and leveraging advanced programming techniques in Python.

Remember to use decorators judiciously, always prioritizing code readability and maintainability.
When used effectively, decorators can significantly enhance the structure and functionality of
your Python projects.

By mastering decorators, you'll have a powerful tool in your Python programming toolkit,
enabling you to write more elegant, efficient, and modular code.

Happy coding!
"""

# 9. How to Contribute

"""
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

Your contributions help keep this resource up-to-date and valuable for the Python community.
Thank you for your support!
"""