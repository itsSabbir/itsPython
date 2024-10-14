"""
Exception Handling - Try-except blocks - in the Python Programming Language
===========================================================================

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
Exception handling, particularly using try-except blocks, is a fundamental concept in Python for managing and responding to errors or exceptional situations that may occur during program execution.

Historical context:
- Exception handling has been a part of Python since its early versions.
- The try-except syntax was introduced in Python 1.5 (1997).
- Python 2.5 (2006) introduced the 'with' statement, which integrates well with exception handling.
- Python 3.0 (2008) made some changes to exception handling, such as making all exceptions inherit from BaseException.

Significance:
- Allows for graceful handling of errors and unexpected situations.
- Enhances program robustness and reliability.
- Provides a structured way to separate normal code from error-handling code.

Common use cases:
- Handling file I/O operations
- Network communications
- User input validation
- Database operations
- Resource management

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import sys
import logging
from typing import List, Any

def basic_try_except():
    """Demonstrate basic usage of try-except blocks."""
    try:
        x = 1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Caught a division by zero error")

def multiple_exceptions():
    """Handle multiple types of exceptions."""
    try:
        # This could raise different types of exceptions
        value = int(input("Enter a number: "))
        result = 10 / value
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def try_except_else_finally():
    """Demonstrate the use of else and finally clauses."""
    try:
        file = open("example.txt", "r")
    except FileNotFoundError:
        print("The file does not exist.")
    else:
        print("File opened successfully.")
        content = file.read()
        print(f"Content: {content}")
    finally:
        print("Executing finally clause.")
        if 'file' in locals():
            file.close()

def raise_custom_exception():
    """Demonstrate raising a custom exception."""
    class CustomError(Exception):
        pass

    try:
        raise CustomError("This is a custom error")
    except CustomError as e:
        print(f"Caught custom error: {e}")

def exception_chaining():
    """Demonstrate exception chaining."""
    try:
        try:
            1 / 0
        except ZeroDivisionError as e:
            raise ValueError("Invalid operation") from e
    except ValueError as e:
        print(f"Caught: {e}")
        print(f"Original exception: {e.__cause__}")

def context_manager_exception_handling():
    """Demonstrate exception handling with context managers."""
    class CustomContextManager:
        def __enter__(self):
            print("Entering the context")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting the context")
            if exc_type is not None:
                print(f"An exception occurred: {exc_type.__name__}: {exc_value}")
                return True  # Suppress the exception

    with CustomContextManager():
        print("Inside the context")
        raise ValueError("An error occurred")

    print("Execution continues")

async def async_exception_handling():
    """Demonstrate exception handling in asynchronous code."""
    import asyncio

    async def async_operation():
        await asyncio.sleep(1)
        raise ValueError("Async error")

    try:
        await async_operation()
    except ValueError as e:
        print(f"Caught async error: {e}")

def demonstrate_exception_handling():
    """Demonstrate various exception handling techniques."""
    print("1. Basic try-except:")
    basic_try_except()

    print("\n2. Handling multiple exceptions:")
    multiple_exceptions()

    print("\n3. Try-except-else-finally:")
    try_except_else_finally()

    print("\n4. Raising custom exceptions:")
    raise_custom_exception()

    print("\n5. Exception chaining:")
    exception_chaining()

    print("\n6. Context manager exception handling:")
    context_manager_exception_handling()

    print("\n7. Asynchronous exception handling:")
    import asyncio
    asyncio.run(async_exception_handling())

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Be specific in catching exceptions. Avoid bare except clauses.
2. Use finally for cleanup operations.
3. Log exceptions for debugging purposes.
4. Use context managers (with statement) for resource management.
5. Raise exceptions with meaningful error messages.

Common Pitfalls:
1. Catching and silencing all exceptions, which can hide bugs.
2. Using try-except blocks for flow control instead of error handling.
3. Not cleaning up resources properly in case of exceptions.
4. Reraising exceptions incorrectly, losing the original traceback.

Advanced Tips:
1. Use exception chaining to preserve context when reraising exceptions.
2. Implement custom exception classes for domain-specific errors.
3. Use sys.exc_info() for detailed exception information.
4. Utilize the traceback module for advanced stack trace handling.
"""

def log_exception(exception: Exception):
    """Log an exception with detailed information."""
    logging.exception("An error occurred:")

def custom_exception_handler(exc_type, exc_value, exc_traceback):
    """Custom exception handler for sys.excepthook."""
    logging.error("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))

def demonstrate_advanced_techniques():
    """Demonstrate advanced exception handling techniques."""
    # Set up logging
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    # Custom exception handler
    sys.excepthook = custom_exception_handler

    # Exception logging
    try:
        1 / 0
    except ZeroDivisionError as e:
        log_exception(e)

    # Using traceback
    import traceback
    try:
        raise ValueError("A value error occurred")
    except ValueError:
        print("Traceback:")
        traceback.print_exc()

"""
4. Integration and Real-World Applications
------------------------------------------
Exception handling is crucial in many real-world applications:

1. Web servers: Handling network errors and malformed requests.
2. Database operations: Managing connection issues and query errors.
3. API integrations: Dealing with timeouts and response parsing errors.
4. File processing: Handling I/O errors and data format issues.

Real-world example: A function to safely read and process a JSON file
"""

import json

def process_json_file(file_path: str) -> List[dict]:
    """
    Safely read and process a JSON file.

    This function demonstrates exception handling in a real-world scenario.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("JSON root must be an array")

        processed_data = []
        for item in data:
            try:
                processed_item = {
                    'id': int(item['id']),
                    'name': str(item['name']),
                    'value': float(item['value'])
                }
                processed_data.append(processed_item)
            except (KeyError, ValueError) as e:
                logging.warning(f"Skipping invalid item: {item}. Error: {e}")

        return processed_data

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in {file_path}: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error processing {file_path}")

    return []

def demonstrate_real_world_application():
    """Demonstrate a real-world application of exception handling."""
    # Create a sample JSON file
    sample_data = [
        {"id": "1", "name": "Item 1", "value": "10.5"},
        {"id": "2", "name": "Item 2", "value": "invalid"},
        {"id": "3", "name": "Item 3", "value": "30.0"}
    ]
    with open('sample.json', 'w') as f:
        json.dump(sample_data, f)

    # Process the file
    result = process_json_file('sample.json')
    print("Processed data:", result)

    # Clean up
    import os
    os.remove('sample.json')

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Exception Groups: Python 3.11 introduced Exception Groups for handling multiple exceptions simultaneously.
2. Structural Pattern Matching: Python 3.10 introduced pattern matching, which can be used with exception handling.
3. Async exception handling: Improved support for exception handling in asynchronous code.
4. Type hints for exception handling: Enhanced static type checking for exception-related code.
"""

def demonstrate_advanced_concepts():
    """Demonstrate advanced exception handling concepts."""
    # Exception Groups (Python 3.11+)
    if sys.version_info >= (3, 11):
        try:
            raise ExceptionGroup("group", [ValueError("error 1"), TypeError("error 2")])
        except* ValueError as e:
            print(f"Caught ValueError: {e}")
        except* TypeError as e:
            print(f"Caught TypeError: {e}")

    # Structural Pattern Matching (Python 3.10+)
    if sys.version_info >= (3, 10):
        def handle_error(error):
            match error:
                case ValueError():
                    print("Handling ValueError")
                case TypeError():
                    print("Handling TypeError")
                case _:
                    print("Handling unknown error")

        try:
            raise ValueError("An error")
        except Exception as e:
            handle_error(e)

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use a bare except clause?
A: Generally, it's best to avoid bare except clauses. If you must use one, consider catching Exception instead of BaseException.

Q: How can I get more information about an exception?
A: Use sys.exc_info() or the traceback module for detailed exception information.

Q: Should I always define custom exceptions for my applications?
A: Custom exceptions are useful for domain-specific errors, but it's not always necessary. Use built-in exceptions when they adequately describe the error.

Troubleshooting:
1. If exceptions are not being caught as expected, check the exception hierarchy and ensure you're catching the correct type.
2. For hard-to-debug exceptions, use logging and consider using a debugger to step through the code.
3. If resources are not being properly released, ensure you're using finally clauses or context managers correctly.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- traceback: Built-in module for working with stack traces.
- logging: Built-in module for flexible event logging.
- pytest: Testing framework with good support for testing exception handling.
- better_exceptions: Library for pretty-printing exception information.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Effective Python" by Brett Slatkin
- Python's official documentation on Exceptions: https://docs.python.org/3/tutorial/errors.html
- Real Python's guide on Exception Handling: https://realpython.com/python-exceptions/
- PEP 3134 - Exception Chaining and Embedded Tracebacks: https://www.python.org/dev/peps/pep-3134/

8. Performance Analysis and Optimization
----------------------------------------
Exception handling can have performance implications, especially when used incorrectly or excessively.
"""

import time
import cProfile
import pstats
from io import StringIO

def benchmark_exception_handling(num_iterations: int = 100000):
    """
    Benchmark different approaches to handling potential exceptions.
    """
    def with_try_except():
        try:
            "abc" + 123
        except TypeError:
            pass

    def with_type_checking():
        if isinstance("abc", str) and isinstance(123, int):
            pass
        else:
            pass

    # Benchmark try-except
    start_time = time.time()
    for _ in range(num_iterations):
        with_try_except()
    try_except_time = time.time() - start_time

    # Benchmark type checking
    start_time = time.time()
    for _ in range(num_iterations):
        with_type_checking()
    type_check_time = time.time() - start_time

    print(f"Try-except time: {try_except_time:.4f} seconds")
    print(f"Type checking time: {type_check_time:.4f} seconds")

def profile_exception_handling():
    """
    Profile exception handling to identify performance bottlenecks.
    """
    def function_with_exceptions():
        for i in range(1000):
            try:
                if i % 2 == 0:
                    raise ValueError("Even number")
                else:
                    raise TypeError("Odd number")
            except ValueError:
                pass
            except TypeError:
                pass

    profiler = cProfile.Profile()
    profiler.enable()
    function_with_exceptions()
    profiler.disable()
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

"""
Performance Considerations:
1. Exception handling is generally slower than regular code execution.
2. Using exceptions for flow control can lead to performance issues in tight loops.
3. Catching specific exceptions is faster than catching general exceptions.

Optimization Strategies:
1. Use exceptions for exceptional cases, not for regular flow control.
2. When possible, use type checking or other validation methods instead of relying solely on exception handling.
3. Be specific when catching exceptions to avoid unnecessary exception handling overhead.
4. Consider using a 'look before you leap' (LBYL) approach instead of 'easier to ask forgiveness than permission' (EAFP) in performance-critical sections.

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
- Relevance to the main topic of exception handling and try-except blocks in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to exception handling and try-except blocks.
    """
    print("1. Basic Exception Handling Techniques:")
    demonstrate_exception_handling()

    print("\n2. Advanced Exception Handling Techniques:")
    demonstrate_advanced_techniques()

    print("\n3. Real-World Application:")
    demonstrate_real_world_application()

    print("\n4. Advanced Concepts:")
    demonstrate_advanced_concepts()

    print("\n5. Performance Benchmarking:")
    benchmark_exception_handling()

    print("\n5. Performance Benchmarking:")
    benchmark_exception_handling()

    print("\n6. Profiling Exception Handling:")
    profile_exception_handling()

if __name__ == "__main__":
    main()