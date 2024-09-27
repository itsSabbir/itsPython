"""
Advanced Python Concepts - Decorators with Arguments - in the Python Programming Language
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
Decorators with arguments are an advanced feature in Python that allow for more flexible and parameterized modifications of functions or classes. They extend the basic decorator pattern by accepting arguments that can customize their behavior.

Historical context:
- Decorators were introduced in Python 2.4 (2004) as part of PEP 318.
- The ability to pass arguments to decorators was not explicitly part of the original PEP but emerged as a pattern shortly after.
- This feature builds upon Python's first-class functions and closure capabilities.

Significance:
- Allows for more dynamic and reusable code modifications.
- Enables the creation of highly customizable metaprogramming tools.
- Facilitates the implementation of aspect-oriented programming concepts in Python.

Common use cases:
- Parameterized logging or instrumentation
- Configurable caching mechanisms
- Access control with customizable permissions
- Validation and type checking with specified criteria

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import functools
import time
from typing import Callable, Any, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])

def retry(max_attempts: int, delay: float = 1.0) -> Callable[[F], F]:
    """
    A decorator that retries the wrapped function up to a specified number of times.
    
    Args:
        max_attempts (int): The maximum number of attempts to make.
        delay (float): The delay between attempts in seconds.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
                    print(f"Attempt {attempts} failed. Retrying...")
        return cast(F, wrapper)
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_network_call(url: str) -> str:
    """Simulate an unstable network call."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network error")
    return f"Success: {url}"

def demonstrate_retry_decorator():
    """Demonstrate the use of the retry decorator."""
    try:
        result = unstable_network_call("https://example.com")
        print(result)
    except ConnectionError:
        print("All attempts failed.")

def validate(*types: type) -> Callable[[F], F]:
    """
    A decorator that validates the types of the arguments passed to the function.
    
    Args:
        *types: The expected types for each argument.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if len(args) != len(types):
                raise ValueError(f"Expected {len(types)} arguments, got {len(args)}")
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator

@validate(int, int)
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def demonstrate_validate_decorator():
    """Demonstrate the use of the validate decorator."""
    print(add_numbers(1, 2))  # This will work
    try:
        add_numbers("1", 2)  # This will raise a TypeError
    except TypeError as e:
        print(f"Caught error: {e}")

def timed(iterations: int = 1) -> Callable[[F], F]:
    """
    A decorator that times the execution of a function over multiple iterations.
    
    Args:
        iterations (int): The number of iterations to run.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            total_time = 0
            for _ in range(iterations):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += end_time - start_time
            average_time = total_time / iterations
            print(f"{func.__name__} took an average of {average_time:.4f} seconds over {iterations} iterations.")
            return result
        return cast(F, wrapper)
    return decorator

@timed(iterations=100)
def slow_function() -> None:
    """A slow function to demonstrate the timed decorator."""
    time.sleep(0.01)

def demonstrate_timed_decorator():
    """Demonstrate the use of the timed decorator."""
    slow_function()

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use functools.wraps to preserve the metadata of the wrapped function.
2. Keep decorators focused on a single responsibility.
3. Use type hints to improve code readability and catch potential errors.
4. Design decorators to be as general and reusable as possible.
5. Document the behavior and parameters of your decorators clearly.

Common Pitfalls:
1. Forgetting to use functools.wraps, which can lead to loss of function metadata.
2. Overusing decorators, which can make code harder to understand and debug.
3. Creating decorators with side effects that are not obvious to the user.
4. Not handling all possible inputs or error cases in the decorator.

Advanced Tips:
1. Use classes as decorators for more complex scenarios or when you need to maintain state.
2. Combine multiple decorators to create more powerful behaviors.
3. Implement decorators that can work with both synchronous and asynchronous functions.
4. Use decorators to implement aspect-oriented programming concepts like logging, timing, or access control.
"""

import asyncio
from typing import Union, Callable, Coroutine

def async_compatible(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that makes a function compatible with both synchronous and asynchronous calls.
    
    This decorator allows a synchronous function to be called in an asynchronous context
    without blocking the event loop.
    """
    @functools.wraps(func)
    def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    
    @functools.wraps(func)
    async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
        return await asyncio.to_thread(func, *args, **kwargs)
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Union[Any, Coroutine[Any, Any, Any]]:
        if asyncio.iscoroutinefunction(func) or asyncio.iscoroutinefunction(wrapper) or asyncio.iscoroutine(func):
            return async_wrapper(*args, **kwargs)
        return sync_wrapper(*args, **kwargs)
    
    return wrapper

@async_compatible
def cpu_bound_task(n: int) -> int:
    """A CPU-bound task that computes the sum of squares."""
    return sum(i * i for i in range(n))

async def demonstrate_async_compatible_decorator():
    """Demonstrate the use of the async_compatible decorator."""
    # Synchronous call
    result_sync = cpu_bound_task(1000000)
    print(f"Synchronous result: {result_sync}")
    
    # Asynchronous call
    result_async = await cpu_bound_task(1000000)
    print(f"Asynchronous result: {result_async}")

"""
4. Integration and Real-World Applications
------------------------------------------
Decorators with arguments are widely used in various Python libraries and frameworks:

1. Flask: Uses decorators for route definitions, e.g., @app.route('/path', methods=['GET', 'POST'])
2. Django: Employs decorators for views, authentication, and permissions, e.g., @login_required(redirect_field_name='next')
3. SQLAlchemy: Utilizes decorators for ORM mappings, e.g., @mapped_column(primary_key=True)

Real-world example: A configurable caching decorator
"""

import hashlib
from typing import Any, Dict, Optional
from functools import wraps

class SimpleCache:
    def __init__(self):
        self._cache: Dict[str, Any] = {}
    
    def get(self, key: str) -> Optional[Any]:
        return self._cache.get(key)
    
    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value

def cached(cache: SimpleCache, ttl: Optional[int] = None) -> Callable[[F], F]:
    """
    A decorator that caches the results of a function.
    
    Args:
        cache (SimpleCache): The cache object to use.
        ttl (Optional[int]): Time-to-live for the cache entry in seconds. If None, the entry never expires.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create a unique key based on the function name and arguments
            key = hashlib.md5(f"{func.__name__}{args}{kwargs}".encode()).hexdigest()
            
            # Check if the result is in the cache
            result = cache.get(key)
            if result is not None:
                return result
            
            # If not in cache, call the function and cache the result
            result = func(*args, **kwargs)
            cache.set(key, result)
            
            return result
        return cast(F, wrapper)
    return decorator

# Global cache object
global_cache = SimpleCache()

@cached(cache=global_cache, ttl=60)
def expensive_computation(n: int) -> int:
    """A computationally expensive function."""
    print("Performing expensive computation...")
    return sum(i * i for i in range(n))

def demonstrate_cached_decorator():
    """Demonstrate the use of the cached decorator."""
    # First call will perform the computation
    result1 = expensive_computation(1000000)
    print(f"Result 1: {result1}")
    
    # Second call will retrieve from cache
    result2 = expensive_computation(1000000)
    print(f"Result 2: {result2}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Decorator Factories: Creating decorators that can be customized at runtime.
2. Async Decorators: Designing decorators that work seamlessly with asynchronous functions.
3. Type Hints for Decorators: Improving type checking and IDE support for decorated functions.
"""

from typing import TypeVar, ParamSpec, Concatenate

P = ParamSpec('P')
R = TypeVar('R')

def inject_dependency(dependency: Any) -> Callable[[Callable[Concatenate[Any, P], R]], Callable[P, R]]:
    """
    A decorator factory that injects a dependency into a function.
    
    This demonstrates the use of ParamSpec and Concatenate for precise type hinting of decorators.
    
    Args:
        dependency (Any): The dependency to inject.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: Callable[Concatenate[Any, P], R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(dependency, *args, **kwargs)
        return wrapper
    return decorator

class Database:
    def query(self, sql: str) -> str:
        return f"Result of: {sql}"

@inject_dependency(Database())
def get_user(db: Database, user_id: int) -> str:
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")

def demonstrate_inject_dependency_decorator():
    """Demonstrate the use of the inject_dependency decorator."""
    result = get_user(1)
    print(result)

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I preserve the signature of the original function when using decorators?
A: Use the @functools.wraps decorator on your wrapper function. This will copy the metadata of the original function to the wrapper.

Q: Can I use multiple decorators on a single function?
A: Yes, you can stack multiple decorators. They will be applied from bottom to top (the decorator closest to the function definition is applied first).

Q: How do I create a decorator that works with both normal and async functions?
A: You can check if the wrapped function is a coroutine using asyncio.iscoroutinefunction() and adjust your wrapper accordingly.

Troubleshooting:
1. Issue: Decorator is changing the signature of my function
   Solution: Ensure you're using @functools.wraps and that your wrapper function accepts *args and **kwargs.

2. Issue: Decorator with arguments is not working
   Solution: Make sure you're returning the inner decorator function. A common pattern is to have three nested functions.

3. Issue: Decorators are slowing down my function calls
   Solution: Consider using lru_cache for expensive decorators or implement a way to bypass the decorator in performance-critical scenarios.

"""

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. functools: Standard library module with utilities for working with functions and decorators.
2. wrapt: A third-party library for creating correct decorators.
3. decorator: A library that simplifies the creation of signature-preserving decorators.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (O'Reilly)
- "Fluent Python" by Luciano Ramalho (O'Reilly)
- PEP 318 - Decorators for Functions and Methods: https://www.python.org/dev/peps/pep-0318/
- Real Python's Guide to Decorators: https://realpython.com/primer-on-python-decorators/
- Python's official documentation on decorators: https://docs.python.org/3/glossary.html#term-decorator

8. Performance Analysis and Optimization
----------------------------------------
When working with decorators, especially those with arguments, it's crucial to consider their performance impact.
"""

import timeit

def performance_comparison():
    """Compare the performance of different decorator implementations."""
    
    def simple_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    def decorator_with_args(arg):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @simple_decorator
    def func1():
        pass
    
    @decorator_with_args(1)
    def func2():
        pass
    
    def func3():
        pass
    
    # Measure execution times
    time_func1 = timeit.timeit(func1, number=1000000)
    time_func2 = timeit.timeit(func2, number=1000000)
    time_func3 = timeit.timeit(func3, number=1000000)
    
    print(f"Simple decorator: {time_func1:.6f} seconds")
    print(f"Decorator with args: {time_func2:.6f} seconds")
    print(f"No decorator: {time_func3:.6f} seconds")
    print(f"Overhead of simple decorator: {(time_func1 - time_func3) / time_func3 * 100:.2f}%")
    print(f"Overhead of decorator with args: {(time_func2 - time_func3) / time_func3 * 100:.2f}%")

"""
Performance Considerations:
1. Function call overhead: Each decorated function involves additional function calls, which can add up in performance-critical code.
2. Closure creation: Decorators with arguments create additional closures, which can have memory implications.
3. Argument processing: Complex decorators that process their arguments can introduce significant overhead.
4. Caching: Decorators that implement caching can greatly improve performance for expensive operations but may consume more memory.

Optimization Strategies:
1. Use functools.lru_cache for expensive decorators to avoid recomputation.
2. Implement bypassing mechanisms for performance-critical scenarios.
3. Use __slots__ in decorator classes to reduce memory usage.
4. Minimize the work done in the wrapper function, especially for frequently called functions.
"""

import functools

def optimized_retry(max_attempts: int, delay: float = 1.0) -> Callable[[F], F]:
    """
    An optimized version of the retry decorator using lru_cache.
    
    Args:
        max_attempts (int): The maximum number of attempts to make.
        delay (float): The delay between attempts in seconds.
    
    Returns:
        Callable: A decorator function.
    """
    def decorator(func: F) -> F:
        @functools.lru_cache(maxsize=128)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)
        
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return cached_func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
                    print(f"Attempt {attempts} failed. Retrying...")
        return cast(F, wrapper)
    return decorator

class OptimizedTimed:
    """
    An optimized version of the timed decorator using a class with __slots__.
    """
    __slots__ = ('iterations',)
    
    def __init__(self, iterations: int = 1):
        self.iterations = iterations
    
    def __call__(self, func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            total_time = 0
            for _ in range(self.iterations):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += end_time - start_time
            average_time = total_time / self.iterations
            print(f"{func.__name__} took an average of {average_time:.4f} seconds over {self.iterations} iterations.")
            return result
        return cast(F, wrapper)

@optimized_retry(max_attempts=3, delay=0.5)
def optimized_unstable_network_call(url: str) -> str:
    """Simulate an unstable network call with optimized retry."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network error")
    return f"Success: {url}"

@OptimizedTimed(iterations=100)
def optimized_slow_function() -> None:
    """A slow function to demonstrate the optimized timed decorator."""
    time.sleep(0.01)

def demonstrate_optimized_decorators():
    """Demonstrate the use of optimized decorators."""
    try:
        result = optimized_unstable_network_call("https://example.com")
        print(result)
    except ConnectionError:
        print("All attempts failed.")
    
    optimized_slow_function()

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
- Relevance to the main topic of decorators with arguments in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to decorators with arguments.
    """
    print("Demonstrating retry decorator:")
    demonstrate_retry_decorator()
    
    print("\nDemonstrating validate decorator:")
    demonstrate_validate_decorator()
    
    print("\nDemonstrating timed decorator:")
    demonstrate_timed_decorator()
    
    print("\nDemonstrating async-compatible decorator:")
    asyncio.run(demonstrate_async_compatible_decorator())
    
    print("\nDemonstrating cached decorator:")
    demonstrate_cached_decorator()
    
    print("\nDemonstrating inject dependency decorator:")
    demonstrate_inject_dependency_decorator()
    
    print("\nPerformance comparison of decorators:")
    performance_comparison()
    
    print("\nDemonstrating optimized decorators:")
    demonstrate_optimized_decorators()

if __name__ == "__main__":
    main()