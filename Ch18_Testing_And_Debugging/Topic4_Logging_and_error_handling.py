# Testing and Debugging - Logging and error handling - in the Python Programming Language
# =======================================================================================

# Table of Contents:
# 1. Overview and Historical Context
# 2. Syntax, Key Concepts, and Code Examples
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# 4. Integration and Real-World Applications
# 5. Advanced Concepts and Emerging Trends
# 6. FAQs and Troubleshooting
# 7. Recommended Tools, Libraries, and Resources
# 8. Performance Analysis and Optimization
# 9. How to Contribute

# Author: Sabbir Hossain

import logging
import sys
import traceback
import time
from typing import Any, Dict, List
from contextlib import contextmanager

# 1. Overview and Historical Context
# ----------------------------------
# Logging and error handling are crucial aspects of software development, enabling
# developers to track program execution, diagnose issues, and gracefully manage
# unexpected situations.

# Historical context:
# - Logging has been a part of programming since the early days of computing.
# - Python's logging module was introduced in Python 2.3 (2003) to provide a flexible framework for generating log messages.
# - Error handling in Python is primarily done through exceptions, a feature present since Python's inception.

# Significance:
# - Logging provides a way to understand the flow of a program and to diagnose problems in production environments.
# - Error handling allows programs to gracefully manage and recover from unexpected situations, improving reliability and user experience.

# Common use cases:
# - Debugging and troubleshooting
# - Monitoring application health and performance
# - Auditing and compliance
# - User activity tracking
# - Error reporting and analysis

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def basic_logging_example():
    """Demonstrate basic usage of the logging module."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

def advanced_logging_example():
    """Demonstrate more advanced logging techniques."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

def basic_error_handling():
    """Demonstrate basic error handling using try-except blocks."""
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")
    finally:
        print("This will always execute")

def advanced_error_handling():
    """Demonstrate more advanced error handling techniques."""
    class CustomError(Exception):
        """A custom exception class."""
        pass

    def risky_operation(value):
        if value < 0:
            raise CustomError("Value cannot be negative")
        return 10 / value

    try:
        result = risky_operation(-5)
    except CustomError as ce:
        print(f"Caught custom error: {ce}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    else:
        print(f"Operation succeeded with result: {result}")
    finally:
        print("Cleanup code here")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

def logging_best_practices():
    """Demonstrate logging best practices."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Use parameterized logging
    user_id = 12345
    logger.info("User %s logged in", user_id)  # Preferred
    logger.info(f"User {user_id} logged in")  # Less efficient, especially if the log level is not met

    # Use appropriate log levels
    logger.debug("Detailed information, typically of interest only when diagnosing problems.")
    logger.info("Confirmation that things are working as expected.")
    logger.warning("An indication that something unexpected happened, or indicative of some problem in the near future.")
    logger.error("Due to a more serious problem, the software has not been able to perform some function.")
    logger.critical("A serious error, indicating that the program itself may be unable to continue running.")

@contextmanager
def error_logging_context(logger):
    """A context manager for error logging."""
    try:
        yield
    except Exception as e:
        logger.exception("An error occurred: %s", str(e))
        raise

def error_handling_best_practices():
    """Demonstrate error handling best practices."""
    logger = logging.getLogger(__name__)

    # Use specific exceptions
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        logger.error("The file was not found")
    except IOError:
        logger.error("An I/O error occurred")

    # Use context managers for resource management
    try:
        with open("example.txt", "w") as file:
            file.write("Hello, World!")
    except IOError:
        logger.error("Failed to write to file")

    # Use custom context managers for error logging
    with error_logging_context(logger):
        # Some operations that might raise exceptions
        pass

# 4. Integration and Real-World Applications
# ------------------------------------------

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.logger = logging.getLogger(__name__)

    def connect(self):
        self.logger.info("Connecting to database")
        # Simulate connection
        time.sleep(0.1)

    def execute_query(self, query):
        self.logger.debug("Executing query: %s", query)
        # Simulate query execution
        time.sleep(0.1)
        if "ERROR" in query.upper():
            raise ValueError("Invalid query")
        return [{"id": 1, "name": "John Doe"}]

    def close(self):
        self.logger.info("Closing database connection")
        # Simulate closing connection
        time.sleep(0.1)

def real_world_example():
    """Demonstrate a real-world scenario using logging and error handling."""
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    db = DatabaseConnection("mysql://localhost:3306/mydb")

    try:
        db.connect()
        result = db.execute_query("SELECT * FROM users")
        logger.info("Query result: %s", result)

        # This will raise an error
        db.execute_query("SELECT * FROM ERROR")
    except ValueError as ve:
        logger.error("Database query error: %s", str(ve))
    finally:
        db.close()

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

import asyncio

async def async_logging_example():
    """Demonstrate asynchronous logging."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    class AsyncHandler(logging.Handler):
        async def emit(self, record):
            # Simulate async operation (e.g., sending log to a remote service)
            await asyncio.sleep(0.1)
            print(f"Async log: {self.format(record)}")

    async_handler = AsyncHandler()
    logger.addHandler(async_handler)

    logger.info("This is an asynchronous log message")
    await asyncio.sleep(0.2)  # Give time for the log to be processed

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    # Q: How to log exceptions with traceback?
    # A: Use logger.exception() within an except block

    # Q: How to rotate log files?
    # A: Use RotatingFileHandler or TimedRotatingFileHandler

    # Q: How to handle concurrent logging in multi-threaded applications?
    # A: The logging module is thread-safe; no special handling is needed

    pass

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - loguru: A library that aims to bring enjoyable logging in Python
# - sentry-sdk: Real-time error tracking and performance monitoring
# - python-json-logger: Log formatter to output logs in JSON format

# Resources:
# - Python's official logging documentation: https://docs.python.org/3/library/logging.html
# - "Python Logging: A Stroll Through the Source Code" by Mario Corchero
# - Real Python's guide on logging: https://realpython.com/python-logging/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_logging():
    """Benchmark the performance impact of logging."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.NullHandler()
    logger.addHandler(handler)

    def function_with_logging():
        for i in range(1000):
            logger.info("Logging message %d", i)

    def function_without_logging():
        for i in range(1000):
            pass

    start_time = time.time()
    function_with_logging()
    with_logging_time = time.time() - start_time

    start_time = time.time()
    function_without_logging()
    without_logging_time = time.time() - start_time

    print(f"Time with logging: {with_logging_time:.4f} seconds")
    print(f"Time without logging: {without_logging_time:.4f} seconds")
    print(f"Logging overhead: {(with_logging_time - without_logging_time) / without_logging_time * 100:.2f}%")

# 9. How to Contribute
# --------------------
# To contribute to this note sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes or additions.
# 3. Ensure all code examples are correct and follow the established style.
# 4. Add comments explaining new concepts or functions.
# 5. Update the Table of Contents if necessary.
# 6. Submit a pull request with a clear description of your changes.

# Guidelines for contributions:
# - Maintain the current format and style.
# - Provide working code examples for new concepts.
# - Include performance considerations for new functions.
# - Add relevant references or citations for advanced topics.

def main():
    print("Basic Logging Example:")
    basic_logging_example()

    print("\nAdvanced Logging Example:")
    advanced_logging_example()

    print("\nBasic Error Handling:")
    basic_error_handling()

    print("\nAdvanced Error Handling:")
    advanced_error_handling()

    print("\nLogging Best Practices:")
    logging_best_practices()

    print("\nError Handling Best Practices:")
    error_handling_best_practices()

    print("\nReal-World Example:")
    real_world_example()

    print("\nAsynchronous Logging Example:")
    asyncio.run(async_logging_example())

    print("\nFAQ and Troubleshooting:")
    faq_and_troubleshooting()

    print("\nLogging Performance Benchmark:")
    benchmark_logging()

if __name__ == "__main__":
    main()