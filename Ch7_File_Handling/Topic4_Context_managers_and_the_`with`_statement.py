"""
File Handling - Context Managers and the 'with' Statement - in the Python Programming Language
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
Context managers and the 'with' statement in Python provide a clean and efficient way to manage resources, particularly in file handling operations. They ensure proper acquisition and release of resources, even in the face of exceptions.

Historical context:
- The 'with' statement was introduced in Python 2.5 (2006) through PEP 343.
- Context managers, implemented via the __enter__ and __exit__ methods, were formalized alongside the 'with' statement.
- These features were inspired by similar concepts in other languages, such as 'using' in C#.

Significance:
- Simplifies resource management, reducing boilerplate code and potential for resource leaks.
- Ensures proper cleanup of resources, even when exceptions occur.
- Enhances code readability and maintainability by clearly delineating resource lifecycles.

Common use cases:
- File I/O operations (opening and closing files automatically)
- Database connections (ensuring connections are properly closed)
- Lock acquisition and release in threading
- Network socket management

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import contextlib
from typing import Any, Generator

class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'FileManager':
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False to propagate exceptions, True to suppress them
        return False

    def read(self) -> str:
        return self.file.read()

    def write(self, text: str):
        self.file.write(text)

def basic_file_operations():
    """Demonstrate basic usage of context managers with file operations."""
    # Using the built-in open function as a context manager
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')

    # Reading the file content
    with open('example.txt', 'r') as file:
        content = file.read()
        print(f"File content: {content}")

    # Using our custom FileManager class
    with FileManager('custom_example.txt', 'w') as fm:
        fm.write('Custom file manager example')

    with FileManager('custom_example.txt', 'r') as fm:
        content = fm.read()
        print(f"Custom file manager content: {content}")

@contextlib.contextmanager
def tempfile(filename: str) -> Generator[str, None, None]:
    """A context manager that creates a temporary file and ensures it's deleted."""
    try:
        with open(filename, 'w') as f:
            yield filename
    finally:
        import os
        os.remove(filename)

def demonstrate_contextlib_usage():
    """Demonstrate usage of contextlib for creating context managers."""
    with tempfile('temp.txt') as filename:
        with open(filename, 'w') as f:
            f.write('Temporary content')
        print(f"Temporary file created: {filename}")
    print("Temporary file has been deleted")

class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database {self.db_name}")
        # Simulate database connection
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to database {self.db_name}")
        # Simulate closing database connection
        return False

    def query(self, sql: str) -> str:
        return f"Executing query: {sql}"

def demonstrate_database_connection():
    """Demonstrate context manager usage with a simulated database connection."""
    with DatabaseConnection("example_db") as db:
        result = db.query("SELECT * FROM users")
        print(result)

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Always use context managers for resource management when possible.
2. Implement __enter__ and __exit__ methods for custom context managers.
3. Use the contextlib module for creating simple context managers.
4. Handle exceptions appropriately in the __exit__ method.

Common Pitfalls:
1. Forgetting to return False in __exit__ method, which can suppress exceptions.
2. Using context managers for operations that don't require resource management.
3. Nesting too many with statements, which can reduce readability.

Advanced Tips:
1. Use contextlib.ExitStack for managing multiple context managers dynamically.
2. Implement asynchronous context managers using __aenter__ and __aexit__ methods.
3. Use contextlib.suppress for ignoring specific exceptions.
4. Leverage context managers for transaction management in databases.
"""

import asyncio

class AsyncFileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    async def __aenter__(self):
        self.file = await asyncio.to_thread(open, self.filename, self.mode)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.to_thread(self.file.close)

    async def read(self) -> str:
        return await asyncio.to_thread(self.file.read)

    async def write(self, text: str):
        await asyncio.to_thread(self.file.write, text)

async def demonstrate_async_context_manager():
    """Demonstrate usage of an asynchronous context manager."""
    async with AsyncFileManager('async_example.txt', 'w') as afm:
        await afm.write('Async file writing example')

    async with AsyncFileManager('async_example.txt', 'r') as afm:
        content = await afm.read()
        print(f"Async file content: {content}")

def demonstrate_exitstack():
    """Demonstrate usage of ExitStack for managing multiple context managers."""
    with contextlib.ExitStack() as stack:
        file1 = stack.enter_context(open('file1.txt', 'w'))
        file2 = stack.enter_context(open('file2.txt', 'w'))
        file1.write('Content for file 1')
        file2.write('Content for file 2')
    print("Both files have been written and closed")

"""
4. Integration and Real-World Applications
------------------------------------------
Context managers are widely used in various Python libraries and frameworks:

1. SQLAlchemy: Uses context managers for transaction management.
2. threading.Lock: Implements context manager protocol for lock acquisition and release.
3. unittest.mock.patch: Uses context managers for mocking objects during testing.

Real-world example: A simple database transaction manager
"""

class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        self.connection.begin_transaction()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
        else:
            self.connection.rollback()

def demonstrate_transaction_manager():
    """Demonstrate a real-world application of context managers in database transactions."""
    class MockDatabaseConnection:
        def begin_transaction(self):
            print("Beginning transaction")

        def commit(self):
            print("Committing transaction")

        def rollback(self):
            print("Rolling back transaction")

        def execute(self, query):
            print(f"Executing query: {query}")

    connection = MockDatabaseConnection()

    # Successful transaction
    with DatabaseTransaction(connection):
        connection.execute("INSERT INTO users (name) VALUES ('Alice')")
        connection.execute("UPDATE users SET status = 'active' WHERE name = 'Alice'")

    # Failed transaction
    try:
        with DatabaseTransaction(connection):
            connection.execute("INSERT INTO users (name) VALUES ('Bob')")
            raise ValueError("Simulated error")
    except ValueError:
        print("Transaction rolled back due to error")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous context managers in Python 3.5+ for use with async/await syntax.
2. Context manager factories using @contextmanager decorator for more dynamic context creation.
3. Integration with type hinting and static type checkers for better code analysis.
4. Use of context managers in resource management for cloud computing and distributed systems.
"""

from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource_manager():
    # Asynchronous resource acquisition
    print("Acquiring resource asynchronously")
    await asyncio.sleep(1)  # Simulate async operation
    try:
        yield "resource"
    finally:
        # Asynchronous resource release
        print("Releasing resource asynchronously")
        await asyncio.sleep(1)  # Simulate async operation

async def demonstrate_async_context_manager_factory():
    async with async_resource_manager() as resource:
        print(f"Using {resource}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: Can I use multiple context managers in a single with statement?
A: Yes, you can use comma-separated context managers: with open('file1.txt') as f1, open('file2.txt') as f2:

Q: How do I handle exceptions in a custom context manager?
A: Implement exception handling in the __exit__ method. Return True to suppress the exception or False to propagate it.

Q: Can I use context managers for things other than file handling?
A: Absolutely! Context managers are useful for any resource that needs to be managed, such as network connections, locks, and database transactions.

Troubleshooting:
1. If resources are not being released, ensure __exit__ method is correctly implemented.
2. For unexpected exception behavior, check the return value of __exit__ method.
3. If context managers are not working with async code, ensure you're using async context managers.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- contextlib: Built-in module for working with context managers.
- aiocontextvars: Library for managing context variables in asyncio applications.
- pytest: Testing framework with built-in support for testing context managers.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Effective Python" by Brett Slatkin
- Python's official documentation on context managers: https://docs.python.org/3/reference/datamodel.html#context-managers
- Real Python's guide on context managers: https://realpython.com/python-with-statement/
- PEP 343 - The "with" Statement: https://www.python.org/dev/peps/pep-0343/

8. Performance Analysis and Optimization
----------------------------------------
When working with context managers, performance considerations are often related to resource management efficiency.
"""

import time
import cProfile
import pstats
from io import StringIO

def benchmark_context_manager_vs_manual(num_iterations: int = 10000):
    """
    Benchmark context manager approach vs manual resource management.
    """
    def with_context_manager():
        with open('benchmark.txt', 'w') as f:
            f.write('test')

    def manual_approach():
        f = open('benchmark.txt', 'w')
        try:
            f.write('test')
        finally:
            f.close()

    # Benchmark context manager
    start_time = time.time()
    for _ in range(num_iterations):
        with_context_manager()
    cm_time = time.time() - start_time

    # Benchmark manual approach
    start_time = time.time()
    for _ in range(num_iterations):
        manual_approach()
    manual_time = time.time() - start_time

    print(f"Context Manager time: {cm_time:.4f} seconds")
    print(f"Manual approach time: {manual_time:.4f} seconds")

def profile_context_manager_usage():
    """
    Profile context manager usage to identify performance bottlenecks.
    """
    profiler = cProfile.Profile()
    profiler.enable()

    for _ in range(1000):
        with open('profile_test.txt', 'w') as f:
            f.write('profiling test')

    profiler.disable()
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

"""
Performance Considerations:
1. Context managers add a small overhead due to the __enter__ and __exit__ method calls.
2. For very frequent, short-lived operations, manual resource management might be marginally faster.
3. The readability and safety benefits of context managers often outweigh minor performance differences.

Optimization Strategies:
1. Reuse context managers for long-lived resources instead of creating new ones frequently.
2. Use contextlib.ExitStack for efficiently managing multiple context managers.
3. Implement __slots__ in custom context manager classes to reduce memory usage.
4. For performance-critical sections, consider manual resource management with careful exception handling.

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
- Relevance to the main topic of context managers and the 'with' statement in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to context managers and the 'with' statement.
    """
    print("1. Basic File Operations with Context Managers:")
    basic_file_operations()

    print("\n2. Contextlib Usage:")
    demonstrate_contextlib_usage()

    print("\n3. Database Connection Example:")
    demonstrate_database_connection()

    print("\n4. Asynchronous Context Manager:")
    asyncio.run(demonstrate_async_context_manager())

    print("\n5. ExitStack Usage:")
    demonstrate_exitstack()

    print("\n6. Database Transaction Manager:")
    demonstrate_transaction_manager()

    print("\n7. Asynchronous Context Manager Factory:")
    asyncio.run(demonstrate_async_context_manager_factory())

    print("\n8. Performance Benchmarking:")
    benchmark_context_manager_vs_manual()

    print("\n9. Profiling Context Manager Usage:")
    profile_context_manager_usage()

if __name__ == "__main__":
    main()