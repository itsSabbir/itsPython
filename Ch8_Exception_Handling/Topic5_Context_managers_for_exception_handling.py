"""
Exception Handling - Context managers for exception handling - in the Python Programming Language
================================================================================================

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
Context managers in Python provide a clean and efficient way to manage resources and handle exceptions. They are particularly useful for ensuring proper cleanup of resources, regardless of whether an exception occurs or not.

Historical context:
- The concept of context managers was introduced in Python 2.5 (2006) with PEP 343.
- The 'with' statement, which is used with context managers, was also introduced in Python 2.5.
- Context managers were inspired by similar concepts in other languages, such as the 'using' statement in C#.

Significance:
- Context managers simplify resource management and exception handling.
- They provide a clear and concise way to set up and tear down resources.
- Context managers help prevent resource leaks and ensure proper cleanup in both normal and exceptional cases.

Common use cases:
- File operations (automatically closing files)
- Database connections (ensuring connections are closed)
- Network operations (managing sockets and connections)
- Threading and concurrency (managing locks and synchronization primitives)
- Testing (setting up and tearing down test environments)

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import contextlib
from typing import Any, Generator, List, Dict
import time
import sqlite3

class CustomContextManager:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Entering the context: {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting the context: {self.name}")
        if exc_type is not None:
            print(f"An exception occurred: {exc_type.__name__} - {exc_value}")
        return False  # Propagate exceptions

def demonstrate_basic_usage():
    """Demonstrate basic usage of a context manager."""
    with CustomContextManager("Basic Example") as cm:
        print("Inside the with block")
        # Simulating an operation that might raise an exception
        if time.time() % 2 == 0:
            raise ValueError("Simulated error")
    print("After the with block")

@contextlib.contextmanager
def custom_context_generator(name: str) -> Generator[str, None, None]:
    """A context manager implemented as a generator."""
    print(f"Entering the context: {name}")
    try:
        yield name
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__} - {e}")
    finally:
        print(f"Exiting the context: {name}")

def demonstrate_contextlib_usage():
    """Demonstrate usage of contextlib.contextmanager decorator."""
    with custom_context_generator("ContextLib Example") as name:
        print(f"Inside the with block: {name}")
        # Simulating an operation that might raise an exception
        if time.time() % 2 == 0:
            raise ValueError("Simulated error")
    print("After the with block")

class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()
        return False  # Propagate exceptions

def demonstrate_database_context_manager():
    """Demonstrate a context manager for database operations."""
    try:
        with DatabaseConnection(":memory:") as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
            cursor.execute("INSERT INTO users (name) VALUES (?)", ("John Doe",))
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            print(f"Database operation result: {result}")
            # Uncomment the next line to simulate an error and trigger a rollback
            # raise ValueError("Simulated error to trigger rollback")
    except Exception as e:
        print(f"An error occurred: {e}")

@contextlib.contextmanager
def nested_contexts(*managers):
    """A context manager for managing multiple nested contexts."""
    exits = []
    values = []
    try:
        for manager in managers:
            value = manager.__enter__()
            exits.append(manager.__exit__)
            values.append(value)
        yield values
    finally:
        while exits:
            exit_func = exits.pop()
            try:
                exit_func(None, None, None)
            except Exception as e:
                print(f"Error during context exit: {e}")

def demonstrate_nested_contexts():
    """Demonstrate usage of nested context managers."""
    with nested_contexts(CustomContextManager("Outer"), CustomContextManager("Inner")) as (outer, inner):
        print(f"Inside nested contexts: {outer.name}, {inner.name}")
        # Simulating an operation that might raise an exception
        if time.time() % 2 == 0:
            raise ValueError("Simulated error in nested contexts")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use context managers for resource management and cleanup.
2. Implement __enter__ and __exit__ methods for custom context managers.
3. Use the contextlib module for simple context managers.
4. Handle exceptions appropriately in the __exit__ method.
5. Use nested context managers for managing multiple resources.

Common Pitfalls:
1. Forgetting to use 'with' statement when using context managers.
2. Improperly implementing __exit__ method, leading to unhandled exceptions.
3. Overusing context managers for simple operations.
4. Not considering the order of nested context managers.

Advanced Tips:
1. Use contextlib.ExitStack for dynamically managing an arbitrary number of context managers.
2. Implement asynchronous context managers for use with 'async with' statements.
3. Use contextlib.suppress to selectively ignore specific exceptions.
4. Create reusable context managers for common patterns in your codebase.
"""

import asyncio

class AsyncDatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None

    async def __aenter__(self):
        # Simulating an asynchronous connection
        await asyncio.sleep(0.1)
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()
        await asyncio.sleep(0.1)  # Simulating asynchronous cleanup
        return False  # Propagate exceptions

async def demonstrate_async_context_manager():
    """Demonstrate an asynchronous context manager."""
    try:
        async with AsyncDatabaseConnection(":memory:") as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
            cursor.execute("INSERT INTO users (name) VALUES (?)", ("Jane Doe",))
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            print(f"Async database operation result: {result}")
    except Exception as e:
        print(f"An error occurred in async context: {e}")

def demonstrate_exit_stack():
    """Demonstrate usage of ExitStack for managing multiple context managers."""
    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(f"file{i}.txt", "w")) for i in range(3)]
        for file in files:
            file.write("Hello, World!")
        # ExitStack will automatically close all files, even if an exception occurs
        if time.time() % 2 == 0:
            raise ValueError("Simulated error in ExitStack example")

@contextlib.contextmanager
def custom_suppress(*exceptions):
    """A custom implementation of contextlib.suppress."""
    try:
        yield
    except exceptions:
        pass

def demonstrate_custom_suppress():
    """Demonstrate usage of a custom suppress context manager."""
    with custom_suppress(ValueError, TypeError):
        print("Before raising ValueError")
        raise ValueError("This error will be suppressed")
        print("This line will not be executed")
    print("After the suppressed error")

"""
4. Integration and Real-World Applications
------------------------------------------
Context managers are widely used in various Python libraries and frameworks:

1. SQLAlchemy's session management for database operations.
2. requests library's Session objects for managing HTTP connections.
3. threading module's Lock and RLock objects for synchronization.

Real-world example: A context manager for profiling code execution time.
"""

import time
from functools import wraps

class Profiler:
    def __init__(self, name: str):
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"Profiler '{self.name}': Execution time = {execution_time:.6f} seconds")
        return False  # Propagate exceptions

def profile(func):
    """A decorator that uses the Profiler context manager."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Profiler(func.__name__):
            return func(*args, **kwargs)
    return wrapper

@profile
def slow_function():
    """A function to demonstrate the profiling context manager."""
    time.sleep(0.5)
    return "Slow function completed"

def demonstrate_real_world_application():
    """Demonstrate a real-world application of context managers for profiling."""
    with Profiler("Manual profiling"):
        result = slow_function()
        print(result)

    # Using the profiler as a decorator
    result = slow_function()
    print(result)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous context managers and the 'async with' statement (introduced in Python 3.5).
2. Type hinting for context managers using the typing.ContextManager generic type.
3. Context variables (contextvars module) for managing state in asynchronous code.
4. Integration of context managers with other language features like decorators and generators.
"""

import contextvars
from typing import ContextManager, AsyncContextManager

# Context variable example
request_id = contextvars.ContextVar('request_id', default=None)

@contextlib.asynccontextmanager
async def set_request_id(id: str) -> AsyncContextManager[None]:
    """An async context manager that sets a context variable."""
    token = request_id.set(id)
    try:
        yield
    finally:
        request_id.reset(token)

async def process_request():
    """A function that uses the request_id context variable."""
    print(f"Processing request: {request_id.get()}")

async def demonstrate_context_variables():
    """Demonstrate usage of context variables with async context managers."""
    async with set_request_id("12345"):
        await process_request()
    print(f"After context: {request_id.get()}")

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts and emerging trends in context managers."""
    asyncio.run(demonstrate_context_variables())

"""
6. FAQs and Troubleshooting
---------------------------
Q1: When should I use a context manager instead of try-finally?
A1: Use a context manager when you have a common setup and teardown pattern, especially for resource management. Context managers are more readable and less error-prone than try-finally blocks.

Q2: Can I use multiple context managers in a single with statement?
A2: Yes, you can use multiple context managers in a single with statement by separating them with commas:
    with open('file1.txt') as f1, open('file2.txt') as f2:
        # operations with f1 and f2

Q3: How do I create a context manager that suppresses specific exceptions?
A3: You can create a context manager that suppresses specific exceptions by handling them in the __exit__ method and returning True:

class SuppressExceptions:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return isinstance(exc_value, self.exceptions)

Q4: Can I use context managers in asynchronous code?
A4: Yes, you can use asynchronous context managers with the 'async with' statement in asynchronous code. Implement __aenter__ and __aexit__ methods for asynchronous context managers.

Troubleshooting Guide:
1. Context manager not cleaning up resources:
   - Ensure that the __exit__ method properly handles resource cleanup.
   - Check if exceptions are being properly caught and handled in __exit__.

2. Exceptions not propagating from context managers:
   - Make sure the __exit__ method returns False for exceptions you want to propagate.

3. Nested context managers not working as expected:
   - Check the order of context managers and ensure they are properly nested.
   - Consider using contextlib.ExitStack for complex nesting scenarios.

4. Context manager causing unexpected delays:
   - Profile the __enter__ and __exit__ methods to identify performance bottlenecks.
   - Consider using asynchronous context managers for I/O-bound operations.
"""

def troubleshooting_examples():
    """Demonstrate common troubleshooting scenarios."""
    
    class ResourceLeakContextManager:
        def __enter__(self):
            print("Acquiring resource")
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is None:
                print("Releasing resource")
            # Forgot to release resource on exception
    
    print("Resource leak example:")
    try:
        with ResourceLeakContextManager():
            raise ValueError("Simulated error")
    except ValueError:
        pass
    
    class FixedResourceContextManager:
        def __enter__(self):
            print("Acquiring resource")
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            print("Releasing resource")
            return False  # Propagate exceptions
    
    print("\nFixed resource management example:")
    try:
        with FixedResourceContextManager():
            raise ValueError("Simulated error")
    except ValueError:
        print("Exception propagated as expected")

"""
Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (Chapter 8: Classes and Objects)
- "Effective Python" by Brett Slatkin (Item 66: Consider contextlib and with Statements for Reusable try/finally Behavior)
- Python's official documentation on context managers: https://docs.python.org/3/reference/datamodel.html#context-managers
- Real Python's guide on context managers: https://realpython.com/python-with-statement/
- PEP 343 – The "with" Statement: https://www.python.org/dev/peps/pep-0343/

8. Performance Analysis and Optimization
----------------------------------------
When working with context managers, it's important to consider their performance implications, especially in performance-critical applications.

Performance Considerations:
1. Context managers add a small overhead due to the additional function calls (__enter__ and __exit__).
2. The performance impact is usually negligible for long-running operations or resource management.
3. Nested context managers can increase the overhead, especially if there are many layers.

Optimization Strategies:
1. Use context managers judiciously, focusing on resource management and error-prone operations.
2. Consider using contextlib.ExitStack for managing multiple context managers efficiently.
3. For very short operations, a try-finally block might be slightly faster than a context manager.
4. Use profiling tools to identify any performance bottlenecks related to context managers.

Example of performance analysis and optimization:
"""

import timeit
import contextlib

def performance_analysis():
    """Analyze and compare performance of different context manager implementations."""
    
    # Traditional try-finally approach
    def traditional_approach():
        resource = None
        try:
            resource = "Resource"
            # Simulate some work
            _ = resource.upper()
        finally:
            resource = None
    
    # Context manager approach
    class CMApproach:
        def __enter__(self):
            self.resource = "Resource"
            return self.resource
        
        def __exit__(self, exc_type, exc_value, traceback):
            self.resource = None
    
    def cm_approach():
        with CMApproach() as resource:
            # Simulate some work
            _ = resource.upper()
    
    # Contextlib approach
    @contextlib.contextmanager
    def contextlib_approach():
        resource = "Resource"
        try:
            yield resource
        finally:
            resource = None
    
    def use_contextlib():
        with contextlib_approach() as resource:
            # Simulate some work
            _ = resource.upper()
    
    # Performance comparison
    traditional_time = timeit.timeit(traditional_approach, number=1000000)
    cm_time = timeit.timeit(cm_approach, number=1000000)
    contextlib_time = timeit.timeit(use_contextlib, number=1000000)
    
    print(f"Traditional approach time: {traditional_time:.6f} seconds")
    print(f"Context manager approach time: {cm_time:.6f} seconds")
    print(f"Contextlib approach time: {contextlib_time:.6f} seconds")
    
    # Optimization example: Using ExitStack for multiple context managers
    def multiple_cm_approach():
        with CMApproach() as r1, CMApproach() as r2, CMApproach() as r3:
            _ = r1.upper() + r2.upper() + r3.upper()
    
    def exitstack_approach():
        with contextlib.ExitStack() as stack:
            r1 = stack.enter_context(CMApproach())
            r2 = stack.enter_context(CMApproach())
            r3 = stack.enter_context(CMApproach())
            _ = r1.upper() + r2.upper() + r3.upper()
    
    multiple_cm_time = timeit.timeit(multiple_cm_approach, number=100000)
    exitstack_time = timeit.timeit(exitstack_approach, number=100000)
    
    print(f"\nMultiple context managers time: {multiple_cm_time:.6f} seconds")
    print(f"ExitStack approach time: {exitstack_time:.6f} seconds")
    print(f"Performance improvement: {(multiple_cm_time - exitstack_time) / multiple_cm_time * 100:.2f}%")

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
- Relevance to the main topic of context managers for exception handling in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to context managers for exception handling.
    """
    print("Basic Context Manager Usage:")
    demonstrate_basic_usage()
    
    print("\nContextlib Usage:")
    demonstrate_contextlib_usage()
    
    print("\nDatabase Context Manager:")
    demonstrate_database_context_manager()
    
    print("\nNested Contexts:")
    demonstrate_nested_contexts()
    
    print("\nAsync Context Manager:")
    asyncio.run(demonstrate_async_context_manager())
    
    print("\nExitStack Usage:")
    demonstrate_exit_stack()
    
    print("\nCustom Suppress:")
    demonstrate_custom_suppress()
    
    print("\nReal-World Application (Profiling):")
    demonstrate_real_world_application()
    
    print("\nAdvanced Concepts:")
    demonstrate_advanced_concepts()
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()