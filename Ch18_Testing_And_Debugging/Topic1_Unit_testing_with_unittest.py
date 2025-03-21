# Testing and Debugging - Unit testing with unittest - in the Python Programming Language
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

import unittest
import sys
import io
from unittest.mock import patch, MagicMock
import asyncio
import time

# 1. Overview and Historical Context
# ----------------------------------
# Unit testing is a software testing method where individual units of source code are tested
# to determine if they are fit for use. In Python, the unittest module provides a rich set of
# tools for constructing and running tests.

# Historical context:
# - The unittest module was originally inspired by JUnit, a unit testing framework for Java.
# - It was introduced in Python 2.1 (2001) as part of the standard library.
# - Over the years, it has evolved to include more features and better integration with Python's language features.

# Significance:
# - Unit testing helps ensure code correctness and facilitates refactoring.
# - It serves as documentation for how code is intended to be used.
# - It promotes writing modular, loosely coupled code.

# Common use cases:
# - Testing individual functions and methods
# - Regression testing to catch reintroduced bugs
# - Test-Driven Development (TDD) workflows
# - Continuous Integration/Continuous Deployment (CI/CD) pipelines

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Sample code to be tested
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value

    def subtract(self, value):
        self.result -= value

    def get_result(self):
        return self.result

# Basic test case
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(1, 0)

# Test case with setup and teardown
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.calc.add(5)
        self.assertEqual(self.calc.get_result(), 5)
        self.calc.add(3)
        self.assertEqual(self.calc.get_result(), 8)

    def test_subtract(self):
        self.calc.add(10)
        self.calc.subtract(3)
        self.assertEqual(self.calc.get_result(), 7)

    def tearDown(self):
        del self.calc

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Write independent tests that can run in any order
# 2. Use descriptive test method names
# 3. Test both normal cases and edge cases
# 4. Use setUp and tearDown methods for common initialization and cleanup
# 5. Use assertRaises to test for expected exceptions

# Common Pitfalls:
# 1. Writing tests that depend on other tests
# 2. Testing implementation details instead of behavior
# 3. Neglecting to test edge cases and error conditions
# 4. Writing overly complex tests

# Advanced Tips:
# 1. Use parameterized tests for multiple input scenarios
# 2. Mock external dependencies to isolate the unit under test
# 3. Use test fixtures for complex setup scenarios
# 4. Measure code coverage to ensure comprehensive testing

# Example of parameterized tests
class TestParameterized(unittest.TestCase):
    @unittest.parameterized.expand([
        ("positive", 2, 3, 5),
        ("zero", 0, 0, 0),
        ("negative", -1, -1, -2),
    ])
    def test_add_parameterized(self, name, a, b, expected):
        self.assertEqual(add(a, b), expected)

# Example of mocking
class TestWithMock(unittest.TestCase):
    @patch('builtins.print')
    def test_print_mock(self, mock_print):
        print("Hello, World!")
        mock_print.assert_called_with("Hello, World!")

# 4. Integration and Real-World Applications
# ------------------------------------------

# Example of testing a database interaction
class TestDatabaseInteraction(unittest.TestCase):
    def setUp(self):
        self.db = MockDatabase()
        self.db.connect()

    def test_insert_user(self):
        user = {"name": "John Doe", "email": "john@example.com"}
        self.db.insert_user(user)
        saved_user = self.db.get_user_by_email("john@example.com")
        self.assertEqual(saved_user["name"], "John Doe")

    def tearDown(self):
        self.db.disconnect()

class MockDatabase:
    def __init__(self):
        self.users = {}

    def connect(self):
        pass

    def disconnect(self):
        pass

    def insert_user(self, user):
        self.users[user["email"]] = user

    def get_user_by_email(self, email):
        return self.users.get(email)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Asynchronous testing
class TestAsyncFunctions(unittest.TestCase):
    async def async_add(self, a, b):
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation
        return a + b

    def test_async_add(self):
        result = asyncio.run(self.async_add(2, 3))
        self.assertEqual(result, 5)

# Property-based testing
from hypothesis import given, strategies as st

class TestPropertyBased(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_add_commutative(self, a, b):
        self.assertEqual(add(a, b), add(b, a))

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    # Q: How to run a specific test method?
    # A: Use the -k option with the test method name:
    #    python -m unittest test_module.TestCase.test_method

    # Q: How to handle tests that need to access external resources?
    # A: Use mocking or create a test double for the external resource

    # Q: How to debug a failing test?
    # A: Use pdb or IDE debugger, add print statements, or use unittest.TestCase.debug()

    pass

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - pytest: A more advanced testing framework
# - coverage: A tool for measuring code coverage
# - mock: A library for creating mock objects (included in unittest.mock since Python 3.3)
# - tox: A tool for testing against multiple Python versions

# Resources:
# - Python's official unittest documentation: https://docs.python.org/3/library/unittest.html
# - "Python Testing with pytest" by Brian Okken
# - "Test-Driven Development with Python" by Harry Percival

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_tests():
    """Benchmark the performance of running tests."""
    start_time = time.time()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunctions)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    end_time = time.time()
    print(f"Test suite execution time: {end_time - start_time:.4f} seconds")

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
    # Run the test cases
    unittest.main(argv=[''], verbosity=2, exit=False)

    print("\nDemonstrating FAQ and troubleshooting:")
    faq_and_troubleshooting()

    print("\nBenchmarking tests:")
    benchmark_tests()

if __name__ == "__main__":
    main()