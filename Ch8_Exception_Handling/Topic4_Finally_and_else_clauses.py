"""
Exception Handling - Finally and else clauses - in the Python Programming Language
==================================================================================

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
Finally and else clauses are integral parts of Python's exception handling mechanism. They provide additional control and flexibility in managing the flow of code execution during and after exception handling.

Historical context:
- The try-except statement has been a part of Python since its early versions.
- The finally clause was introduced in Python 2.0 (2000) to provide a way to specify cleanup actions that must be executed under all circumstances.
- The else clause in exception handling was also introduced in Python 2.0, allowing for code execution when no exception occurs.

Significance:
- Finally clauses ensure that cleanup code is executed regardless of whether an exception occurred or not.
- Else clauses provide a clean way to separate the code that might raise an exception from the code that should run only if no exception occurred.
- Both clauses enhance the readability and maintainability of exception handling code.

Common use cases:
- Finally: Resource cleanup (e.g., closing files, network connections, or database connections)
- Else: Executing code that should only run if no exception occurred, without mixing it with the try block

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import sys
from typing import Any, List, Dict
import time

def demonstrate_basic_finally():
    """Demonstrate basic usage of the finally clause."""
    try:
        print("Trying to perform an operation...")
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError!")
    finally:
        print("This will always execute, regardless of exceptions.")

    print("This line will not be reached if an unhandled exception occurs.")

def demonstrate_basic_else():
    """Demonstrate basic usage of the else clause in exception handling."""
    try:
        print("Trying to perform an operation...")
        result = 10 / 2
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError!")
    else:
        print(f"Operation successful. Result: {result}")
        # This block only executes if no exception was raised in the try block
    
    print("This line will always be reached if no unhandled exception occurs.")

class Resource:
    """A mock resource class to demonstrate resource management."""
    def __init__(self, name: str):
        self.name = name
        print(f"Resource {self.name} acquired.")
    
    def use(self):
        print(f"Using resource {self.name}.")
        if self.name == "faulty":
            raise ValueError(f"Error while using resource {self.name}")
    
    def close(self):
        print(f"Closing resource {self.name}.")

def use_resource(name: str) -> None:
    """
    Demonstrate the use of finally for resource cleanup.
    
    Args:
        name (str): Name of the resource to use.
    """
    resource = Resource(name)
    try:
        resource.use()
    except ValueError as e:
        print(f"Caught an error: {e}")
    finally:
        resource.close()

def process_data(data: List[int]) -> Dict[str, Any]:
    """
    Process a list of integers, demonstrating the use of else clause.
    
    Args:
        data (List[int]): List of integers to process.
    
    Returns:
        Dict[str, Any]: A dictionary containing the processing results.
    """
    results = {}
    try:
        total = sum(data)
        average = total / len(data)
    except ZeroDivisionError:
        print("Error: Empty data list")
        results["error"] = "Empty data list"
    except TypeError:
        print("Error: Invalid data type in list")
        results["error"] = "Invalid data type"
    else:
        results["total"] = total
        results["average"] = average
        print("Data processed successfully")
    finally:
        results["timestamp"] = time.time()
    
    return results

def demonstrate_advanced_usage():
    """Demonstrate more advanced usage of finally and else clauses."""
    print("Using a non-faulty resource:")
    use_resource("good")
    
    print("\nUsing a faulty resource:")
    use_resource("faulty")
    
    print("\nProcessing valid data:")
    result = process_data([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    
    print("\nProcessing empty data:")
    result = process_data([])
    print(f"Result: {result}")
    
    print("\nProcessing invalid data:")
    result = process_data([1, 2, "3", 4, 5])
    print(f"Result: {result}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use finally for cleanup code that must be executed regardless of exceptions.
2. Use else for code that should only execute if no exception occurred in the try block.
3. Keep the code in try blocks as minimal as possible to pinpoint the source of exceptions.
4. Avoid raising exceptions in finally blocks unless absolutely necessary.

Common Pitfalls:
1. Overusing try-except blocks, leading to difficulty in debugging.
2. Catching too broad exceptions (e.g., bare except clauses).
3. Forgetting that finally blocks execute even if a return, break, or continue statement is encountered.
4. Assuming that the else block will always execute if no exception is explicitly raised in the try block.

Advanced Tips:
1. Use context managers (with statements) for resource management when possible.
2. Combine finally with else to separate normal execution flow from cleanup code.
3. Be aware of how finally interacts with return statements in the try and except blocks.
4. Use sys.exc_info() in finally blocks to check if an exception occurred.
"""

import contextlib

@contextlib.contextmanager
def managed_resource(name: str):
    """A context manager for resource management."""
    resource = Resource(name)
    try:
        yield resource
    finally:
        resource.close()

def demonstrate_context_manager():
    """Demonstrate the use of a context manager for resource management."""
    try:
        with managed_resource("context_managed") as resource:
            resource.use()
            print("Resource used successfully")
    except ValueError as e:
        print(f"Caught an error: {e}")

def complex_finally_behavior() -> int:
    """Demonstrate complex behavior with return statements and finally."""
    try:
        return 1
    finally:
        return 2  # This return will override the return in the try block

def check_exception_in_finally():
    """Demonstrate checking for exceptions in a finally block."""
    try:
        raise ValueError("An error occurred")
    finally:
        if sys.exc_info()[0] is not None:
            print(f"An exception occurred: {sys.exc_info()[0].__name__}")
        else:
            print("No exception occurred")

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques with finally and else clauses."""
    print("Using a context manager:")
    demonstrate_context_manager()
    
    print("\nComplex finally behavior:")
    result = complex_finally_behavior()
    print(f"Result: {result}")  # This will print 2, not 1
    
    print("\nChecking for exceptions in finally:")
    check_exception_in_finally()

"""
4. Integration and Real-World Applications
------------------------------------------
Finally and else clauses are widely used in various Python libraries and frameworks:

1. Database connection management in SQLAlchemy and other ORMs.
2. File handling in standard library modules like csv and json.
3. Network programming with sockets and requests library.

Real-world example: A simplified version of a database connection pool.
"""

import random
from typing import Any, Callable

class DatabaseConnection:
    """A mock database connection class."""
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.is_open = False
    
    def open(self):
        print(f"Opening connection to {self.db_name}")
        self.is_open = True
    
    def close(self):
        print(f"Closing connection to {self.db_name}")
        self.is_open = False
    
    def execute(self, query: str) -> List[Dict[str, Any]]:
        if not self.is_open:
            raise ValueError("Connection is not open")
        print(f"Executing query: {query}")
        # Simulate query execution
        return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

class ConnectionPool:
    """A simple database connection pool."""
    def __init__(self, db_name: str, pool_size: int = 5):
        self.db_name = db_name
        self.pool = [DatabaseConnection(db_name) for _ in range(pool_size)]
        self.available = set(self.pool)
    
    def get_connection(self) -> DatabaseConnection:
        if not self.available:
            raise RuntimeError("No available connections")
        return self.available.pop()
    
    def release_connection(self, conn: DatabaseConnection):
        self.available.add(conn)

def execute_query(pool: ConnectionPool, query: str) -> List[Dict[str, Any]]:
    """Execute a query using a connection from the pool."""
    connection = pool.get_connection()
    try:
        connection.open()
        return connection.execute(query)
    except ValueError as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        connection.close()
        pool.release_connection(connection)

def demonstrate_real_world_application():
    """Demonstrate a real-world application of finally and else clauses in a database connection pool."""
    pool = ConnectionPool("example_db")
    
    # Successful query execution
    result = execute_query(pool, "SELECT * FROM users")
    print(f"Query result: {result}")
    
    # Simulate a connection error
    def faulty_execute(query: str) -> List[Dict[str, Any]]:
        raise ValueError("Simulated connection error")
    
    original_execute = DatabaseConnection.execute
    DatabaseConnection.execute = faulty_execute
    
    result = execute_query(pool, "SELECT * FROM users")
    print(f"Query result after error: {result}")
    
    # Restore original execute method
    DatabaseConnection.execute = original_execute

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous exception handling: Using finally and else clauses with async/await syntax.
2. Context-dependent exception handling: Implementing exception handling that behaves differently based on the context.
3. Exception chaining: Using the `raise ... from ...` syntax to provide additional context when re-raising exceptions.
"""

import asyncio

async def async_resource(name: str):
    """An asynchronous context manager for resource management."""
    print(f"Acquiring resource {name}")
    try:
        yield f"Resource {name}"
    finally:
        print(f"Releasing resource {name}")

async def demonstrate_async_exception_handling():
    """Demonstrate exception handling in asynchronous code."""
    try:
        async with async_resource("async_example") as resource:
            print(f"Using {resource}")
            if random.random() < 0.5:
                raise ValueError("Simulated error in async code")
    except ValueError as e:
        print(f"Caught error in async code: {e}")
    else:
        print("Async operation completed successfully")

class CustomError(Exception):
    """A custom error class to demonstrate exception chaining."""
    pass

def demonstrate_exception_chaining():
    """Demonstrate exception chaining with the raise ... from ... syntax."""
    try:
        try:
            raise ValueError("Original error")
        except ValueError as e:
            raise CustomError("A custom error occurred") from e
    except CustomError as e:
        print(f"Caught custom error: {e}")
        print(f"Original error: {e.__cause__}")

async def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts and emerging trends in exception handling."""
    print("Asynchronous exception handling:")
    await demonstrate_async_exception_handling()
    
    print("\nException chaining:")
    demonstrate_exception_chaining()

"""
6. FAQs and Troubleshooting
---------------------------
Q1: When should I use `finally` instead of a simple `try`-`except` block?
A1: Use `finally` when you need to ensure that certain cleanup code is executed, regardless of whether an exception occurred or not. This is particularly useful for resource management, such as closing files or network connections.

Q2: What's the difference between putting code in the `else` clause versus at the end of the `try` block?
A2: Code in the `else` clause only executes if no exception was raised in the `try` block. This provides a clear separation between the code that might raise an exception and the code that should only run if no exception occurred. It also avoids accidentally catching exceptions from code that was meant to run after the potentially problematic operations.

Q3: Can I use `return` statements in `try`, `except`, and `finally` blocks?
A3: Yes, you can use `return` statements in all these blocks. However, be aware that a `return` statement in a `finally` block will override any `return` statements in the `try` or `except` blocks.

Q4: How do I properly chain exceptions?
A4: Use the `raise ... from ...` syntax to chain exceptions. This preserves the original exception as the `__cause__` of the new exception:

try:
    # Some operation that may raise an exception
    raise ValueError("Invalid value")
except ValueError as e:
    raise CustomError("A custom error occurred") from e

Troubleshooting Guide:
1. Unexpected exception not being caught:
   - Ensure you're catching the correct exception type.
   - Check if the exception is being raised in a different thread or async context.

2. Code in `else` block not executing:
   - Verify that no exception is being raised in the `try` block.
   - Check if there's a `return`, `break`, or `continue` statement in the `try` block.

3. `finally` block not executing:
   - This is rare, but can happen if the program is forcibly terminated (e.g., `os._exit()`).
   - Check for infinite loops or deadlocks that might prevent the `finally` block from being reached.

4. Resource leaks despite using `finally`:
   - Ensure that the cleanup code in the `finally` block is correct and complete.
   - Consider using context managers (`with` statements) for more robust resource management.

"""

def troubleshooting_examples():
    """Demonstrate common troubleshooting scenarios."""
    
    def unexpected_exception():
        try:
            raise TypeError("Unexpected type error")
        except ValueError:
            print("This will not catch the TypeError")
    
    def else_not_executing():
        try:
            print("This will execute")
            return  # This prevents the else block from executing
        except ValueError:
            print("This will not execute")
        else:
            print("This will not execute due to the return statement")
    
    def finally_always_executes():
        try:
            print("In try block")
            raise ValueError("An error occurred")
        except ValueError:
            print("In except block")
            return  # This doesn't prevent finally from executing
        else:
            print("This will not execute")
        finally:
            print("This will always execute")

    print("Unexpected exception example:")
    try:
        unexpected_exception()
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    print("\nElse not executing example:")
    else_not_executing()

    print("\nFinally always executes example:")
    finally_always_executes()

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. pytest: Testing framework with excellent support for testing exception handling.
2. contextlib: Standard library module for creating and working with context managers.
3. logging: Standard library module for integrating exception handling with application logging.
4. traceback: Standard library module for working with stack traces.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (Chapter 14: Testing, Debugging, and Exceptions)
- "Effective Python" by Brett Slatkin (Item 66: Consider contextlib and with Statements for Reusable try/finally Behavior)
- Python's official documentation on Exceptions: https://docs.python.org/3/tutorial/errors.html
- Real Python's guide on Python exceptions: https://realpython.com/python-exceptions/
- PEP 341 – Unifying try-except and try-finally: https://www.python.org/dev/peps/pep-0341/

8. Performance Analysis and Optimization
----------------------------------------
When working with finally and else clauses, it's important to consider their performance implications, especially in performance-critical applications.

Performance Considerations:
1. Using try-except blocks can be slower than using if-else statements for flow control.
2. The finally clause always executes, which can impact performance in tight loops.
3. Complex exception handling can make code harder to optimize for the Python interpreter.

Optimization Strategies:
1. Use exception handling for exceptional cases, not for regular control flow.
2. Keep try blocks as small as possible to minimize performance impact.
3. Use else clauses to clearly separate exception-prone code from regular code, potentially allowing for better optimization.
4. Consider using context managers for resource management, as they can be more efficiently implemented by the Python interpreter.

Example of optimizing exception handling:
"""

import timeit

def demonstrate_performance_optimization():
    """Demonstrate performance optimization techniques for exception handling."""
    
    def division_with_exception_handling(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')
    
    def division_with_check(a, b):
        return a / b if b != 0 else float('inf')
    
    # Performance comparison
    exception_time = timeit.timeit(lambda: division_with_exception_handling(10, 0), number=100000)
    check_time = timeit.timeit(lambda: division_with_check(10, 0), number=100000)
    
    print(f"Time with exception handling: {exception_time:.6f} seconds")
    print(f"Time with explicit check: {check_time:.6f} seconds")
    print(f"Performance improvement: {(exception_time - check_time) / exception_time * 100:.2f}%")

    # Demonstrating the impact of finally in a loop
    def loop_with_finally():
        for i in range(1000):
            try:
                x = i * 2
            finally:
                pass  # Simulating some cleanup operation
    
    def loop_without_finally():
        for i in range(1000):
            x = i * 2
    
    finally_time = timeit.timeit(loop_with_finally, number=1000)
    no_finally_time = timeit.timeit(loop_without_finally, number=1000)
    
    print(f"\nTime with finally in loop: {finally_time:.6f} seconds")
    print(f"Time without finally in loop: {no_finally_time:.6f} seconds")
    print(f"Performance impact: {(finally_time - no_finally_time) / no_finally_time * 100:.2f}%")

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
- Relevance to the main topic of finally and else clauses in Python exception handling.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to finally and else clauses in exception handling.
    """
    print("Basic Finally Clause Demonstration:")
    demonstrate_basic_finally()
    
    print("\nBasic Else Clause Demonstration:")
    demonstrate_basic_else()
    
    print("\nAdvanced Usage Demonstration:")
    demonstrate_advanced_usage()
    
    print("\nAdvanced Techniques Demonstration:")
    demonstrate_advanced_techniques()
    
    print("\nReal-World Application Demonstration:")
    demonstrate_real_world_application()
    
    print("\nAdvanced Concepts Demonstration:")
    asyncio.run(demonstrate_advanced_concepts())
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Optimization Demonstration:")
    demonstrate_performance_optimization()

if __name__ == "__main__":
    main()