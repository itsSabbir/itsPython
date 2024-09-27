"""
Advanced Python Concepts - Context Managers - in the Python Programming Language
================================================================================

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
Context managers in Python provide a clean and efficient way to manage resources, ensuring proper acquisition and release. They are particularly useful for handling operations that require setup and cleanup, such as file I/O, database connections, and lock management.

Historical context:
- Introduced in Python 2.5 (2006) with PEP 343, which defined the 'with' statement and context manager protocol.
- Further refined in Python 3.1 (2009) with the introduction of the contextlib module, providing additional utilities for working with context managers.
- Async context managers were introduced in Python 3.5 (2015) with PEP 492, extending the concept to asynchronous programming.

Significance:
- Simplifies resource management and reduces the risk of resource leaks.
- Enhances code readability and maintainability by clearly delineating resource lifecycles.
- Provides a standardized way to implement cleanup actions, improving consistency across different APIs.

Common use cases:
- File handling: Automatically closing files after use.
- Database connections: Ensuring connections are properly closed.
- Thread synchronization: Managing locks and semaphores.
- Temporary state changes: Modifying and restoring system state.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import contextlib
import time
from typing import Generator, Any, ContextManager

class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Returning False allows exceptions to propagate
        return False

@contextlib.contextmanager
def timer() -> Generator[None, None, None]:
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start} seconds")

class DatabaseConnection:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.connection = None

    def __enter__(self):
        # Simulate opening a database connection
        print(f"Opening connection to {self.db_url}")
        self.connection = "DatabaseConnection"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Simulate closing a database connection
        print(f"Closing connection to {self.db_url}")
        self.connection = None

    def query(self, sql: str) -> str:
        if not self.connection:
            raise RuntimeError("No active database connection")
        return f"Query result: {sql}"

@contextlib.contextmanager
def temporary_attribute(obj: Any, name: str, value: Any) -> Generator[None, None, None]:
    if hasattr(obj, name):
        old_value = getattr(obj, name)
        setattr(obj, name, value)
        try:
            yield
        finally:
            setattr(obj, name, old_value)
    else:
        setattr(obj, name, value)
        try:
            yield
        finally:
            delattr(obj, name)

def demonstrate_basic_usage():
    """Demonstrate basic usage of context managers."""
    # Using a class-based context manager
    with FileManager("example.txt", "w") as file:
        file.write("Hello, Context Managers!")

    # Using a generator-based context manager
    with timer():
        time.sleep(1)

    # Using multiple context managers
    with FileManager("input.txt", "r") as input_file, FileManager("output.txt", "w") as output_file:
        content = input_file.read()
        output_file.write(content.upper())

def demonstrate_database_connection():
    """Demonstrate using a context manager for database connections."""
    with DatabaseConnection("postgresql://localhost/mydb") as db:
        result = db.query("SELECT * FROM users")
        print(result)

class MyClass:
    def __init__(self):
        self.original_attribute = "original"

def demonstrate_temporary_attribute():
    """Demonstrate using a context manager to temporarily modify an object's attribute."""
    obj = MyClass()
    print(f"Before: {obj.original_attribute}")
    
    with temporary_attribute(obj, "original_attribute", "temporary"):
        print(f"Inside context manager: {obj.original_attribute}")
    
    print(f"After: {obj.original_attribute}")

    with temporary_attribute(obj, "new_attribute", "new"):
        print(f"New attribute: {obj.new_attribute}")
    
    print("New attribute no longer exists:", not hasattr(obj, "new_attribute"))

@contextlib.contextmanager
def nested_contexts(*managers: ContextManager) -> Generator[tuple, None, None]:
    """A context manager that manages multiple context managers."""
    exits = []
    values = []
    try:
        for manager in managers:
            value = manager.__enter__()
            exits.append(manager.__exit__)
            values.append(value)
        yield tuple(values)
    finally:
        while exits:
            exit_func = exits.pop()
            try:
                exit_func(None, None, None)
            except Exception as e:
                print(f"Error during exit: {e}")

def demonstrate_nested_contexts():
    """Demonstrate using a custom context manager to manage multiple contexts."""
    with nested_contexts(FileManager("file1.txt", "w"), FileManager("file2.txt", "w"), timer()) as (file1, file2, _):
        file1.write("Content for file 1")
        file2.write("Content for file 2")
        time.sleep(0.5)

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use context managers for resource management to ensure proper cleanup.
2. Prefer the @contextlib.contextmanager decorator for simple context managers.
3. Implement __enter__ and __exit__ methods for more complex scenarios.
4. Use type hints to improve code readability and catch potential errors.
5. Handle exceptions appropriately in the __exit__ method.

Common Pitfalls:
1. Forgetting to use the 'with' statement when working with context managers.
2. Improperly implementing the __exit__ method, leading to unhandled exceptions.
3. Using context managers for operations that don't require resource management.
4. Nesting too many context managers, which can reduce code readability.

Advanced Tips:
1. Use contextlib.ExitStack for dynamically managing an arbitrary number of context managers.
2. Implement async context managers for use with asynchronous code.
3. Utilize contextlib.suppress for selectively ignoring specific exceptions.
4. Create reusable context managers to encapsulate common patterns in your codebase.
"""

import asyncio
from contextlib import AsyncExitStack, asynccontextmanager, ExitStack, suppress

@asynccontextmanager
async def async_timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Async execution time: {end - start} seconds")

async def demonstrate_async_context_manager():
    """Demonstrate using an async context manager."""
    async with async_timer():
        await asyncio.sleep(1)

def demonstrate_exit_stack():
    """Demonstrate using ExitStack for dynamic context management."""
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname, "w")) for fname in filenames]
        for i, file in enumerate(files, 1):
            file.write(f"This is file {i}")

def demonstrate_suppress():
    """Demonstrate using contextlib.suppress to ignore specific exceptions."""
    with suppress(FileNotFoundError):
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    print("Execution continues even if the file doesn't exist.")

"""
4. Integration and Real-World Applications
------------------------------------------
Context managers are widely used in various Python libraries and frameworks:

1. SQLAlchemy: Uses context managers for managing database sessions and transactions.
2. Requests: Employs context managers for handling HTTP connections.
3. Threading: Utilizes context managers for lock management in multithreaded applications.

Real-world example: A context manager for profiling code sections
"""

import cProfile
import pstats
import io

@contextlib.contextmanager
def profiler(sortby: str = "cumulative", lines: int = 10) -> Generator[None, None, None]:
    """A context manager for profiling code sections."""
    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats(lines)
    print(s.getvalue())

def complex_operation():
    """A function to demonstrate profiling."""
    return sum(i * i for i in range(10**6))

def demonstrate_profiler():
    """Demonstrate using a profiler context manager."""
    with profiler():
        result = complex_operation()
    print(f"Result: {result}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Context Variables: Introduced in Python 3.7 (PEP 567) for managing context-local state.
2. Asynchronous Generators as Context Managers: Combining async generators with context management.
3. Type Hints for Context Managers: Improved static type checking for context managers.
"""

from contextvars import ContextVar
from typing import AsyncIterator

# Context variable example
request_id: ContextVar[str] = ContextVar("request_id", default="default")

def set_request_id(new_id: str):
    request_id.set(new_id)

def get_request_id() -> str:
    return request_id.get()

# Asynchronous generator as a context manager
@asynccontextmanager
async def async_resource_manager() -> AsyncIterator[str]:
    resource = "AsyncResource"
    print(f"Acquiring {resource}")
    try:
        yield resource
    finally:
        print(f"Releasing {resource}")

async def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts with context managers."""
    # Context variables
    print(f"Default request ID: {get_request_id()}")
    set_request_id("user123")
    print(f"New request ID: {get_request_id()}")

    # Async generator as context manager
    async with async_resource_manager() as resource:
        print(f"Using {resource}")
        await asyncio.sleep(0.1)

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use a class-based context manager vs. a generator-based one?
A: Use class-based context managers for more complex scenarios that require maintaining state or when you need fine-grained control over the enter and exit processes. Use generator-based context managers (with @contextlib.contextmanager) for simpler cases where you just need to wrap a piece of code with setup and teardown operations.

Q: How do I handle exceptions in a context manager?
A: In a class-based context manager, you can handle exceptions in the __exit__ method. The method receives the exception type, value, and traceback as arguments. Return True from __exit__ to suppress the exception, or False (or None) to let it propagate. In a generator-based context manager, you can use a try-except block around the yield statement.

Q: Can I use multiple context managers in a single with statement?
A: Yes, you can use multiple context managers in a single with statement by separating them with commas. They will be processed from left to right when entering the context, and from right to left when exiting.

Troubleshooting:
1. Issue: Resource not being released properly
   Solution: Ensure that the __exit__ method (or the code after yield in generator-based context managers) is correctly implemented to release resources, even in the case of exceptions.

2. Issue: Unexpected exception suppression
   Solution: Check the return value of the __exit__ method. Returning True will suppress exceptions, which might not always be desirable.

3. Issue: Context manager not working with async code
   Solution: For asynchronous code, use async context managers defined with @contextlib.asynccontextmanager or by implementing __aenter__ and __aexit__ methods.

"""

async def demonstrate_async_context_manager_exception_handling():
    """Demonstrate exception handling in async context managers."""
    @asynccontextmanager
    async def async_error_prone_resource():
        print("Entering async context")
        try:
            yield "AsyncResource"
        except Exception as e:
            print(f"Caught exception: {e}")
        finally:
            print("Exiting async context")

    try:
        async with async_error_prone_resource():
            raise ValueError("Simulated error")
    except ValueError:
        print("ValueError was not suppressed")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. contextlib: Standard library module providing utilities for working with context managers.
2. asyncio: Standard library module for writing asynchronous code, including async context managers.
3. contextvar: Standard library module for context variables (Python 3.7+).
4. pytest: Testing framework with built-in support for testing context managers.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (O'Reilly)
- "Fluent Python" by Luciano Ramalho (O'Reilly)
- PEP 343 - The "with" Statement: https://www.python.org/dev/peps/pep-0343/
- Python's official documentation on context managers: https://docs.python.org/3/reference/datamodel.html#context-managers
- Real Python's guide on context managers: https://realpython.com/python-with-statement/

8. Performance Analysis and Optimization
----------------------------------------
When working with context managers, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def performance_comparison():
    """Compare the performance of different context manager implementations."""
    
    # Class-based context manager
    class ClassTimer:
        def __enter__(self):
            self.start = time.perf_counter()
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.perf_counter()
            print(f"Class-based time: {self.end - self.start}")
    
    # Generator-based context manager
    @contextlib.contextmanager
    def generator_timer():
        start = time.perf_counter()
        yield
        end = time.perf_counter()
        print(f"Generator-based time: {end - start}")
    
    # Function using class-based context manager
    def use_class_timer():
        with ClassTimer():
            sum(i for i in range(10**6))
    
    # Function using generator-based context manager
    def use_generator_timer():
        with generator_timer():
            sum(i for i in range(10**6))
    
    # Measure execution times
    class_time = timeit.timeit(use_class_timer, number=100)
    generator_time = timeit.timeit(use_generator_timer, number=100)
    
    print(f"Total time for class-based: {class_time}")
    print(f"Total time for generator-based: {generator_time}")
    print(f"Ratio (class/generator): {class_time/generator_time}")

"""
Performance Considerations:
1. Overhead: Context managers introduce a small overhead due to the additional function calls (__enter__ and __exit__).
2. Implementation choice: Class-based context managers might have slightly more overhead than generator-based ones due to object instantiation.
3. Resource management: Properly implemented context managers can improve performance by ensuring timely release of resources.
4. Exception handling: The way exceptions are handled in __exit__ can impact performance, especially in error-prone code.

Optimization Strategies:
1. Use generator-based context managers for simple cases to reduce overhead.
2. Implement __slots__ in class-based context managers to reduce memory usage.
3. Minimize the work done in __enter__ and __exit__ methods to reduce context switching overhead.
4. Use contextlib.ExitStack for managing multiple context managers more efficiently.
5. Consider using async context managers for I/O-bound operations in asynchronous code.

Example of optimizing a frequently called context manager:
"""

class OptimizedFileManager:
    __slots__ = ('filename', 'mode', 'file')

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

def demonstrate_optimized_context_manager():
    """Demonstrate the use of an optimized context manager."""
    with OptimizedFileManager("example.txt", "w") as file:
        file.write("This is an optimized file write operation.")

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
- Relevance to the main topic of context managers in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to context managers.
    """
    demonstrate_basic_usage()
    demonstrate_database_connection()
    demonstrate_temporary_attribute()
    demonstrate_nested_contexts()
    demonstrate_exit_stack()
    demonstrate_suppress()
    demonstrate_profiler()
    asyncio.run(demonstrate_async_context_manager())
    asyncio.run(demonstrate_advanced_concepts())
    asyncio.run(demonstrate_async_context_manager_exception_handling())
    performance_comparison()
    demonstrate_optimized_context_manager()

if __name__ == "__main__":
    main()