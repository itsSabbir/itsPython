# Testing and Debugging - Pytest framework - in the Python Programming Language
# =============================================================================

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

import pytest
import sys
import io
from unittest.mock import patch, MagicMock
import asyncio
import time

# 1. Overview and Historical Context
# ----------------------------------
# Pytest is a powerful testing framework for Python that simplifies the process of
# writing and running tests. It provides a rich set of features for test discovery,
# parameterization, fixtures, and plugins.

# Historical context:
# - Pytest was created by Holger Krekel and first released in 2004.
# - It was designed to be an improvement over the built-in unittest module, offering
#   more Pythonic syntax and powerful features.
# - Over the years, it has become one of the most popular testing frameworks in the Python ecosystem.

# Significance:
# - Pytest simplifies test writing with its "assert" statement introspection.
# - It offers powerful fixture management for test setup and teardown.
# - The framework is highly extensible through its plugin system.
# - It provides excellent support for test parameterization and marking.

# Common use cases:
# - Unit testing of individual functions and classes
# - Integration testing of multiple components
# - Functional testing of entire applications
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

# Basic test functions
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(1, 0)

# Test class
class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add(self, calculator):
        calculator.add(5)
        assert calculator.get_result() == 5
        calculator.add(3)
        assert calculator.get_result() == 8

    def test_subtract(self, calculator):
        calculator.add(10)
        calculator.subtract(3)
        assert calculator.get_result() == 7

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use descriptive test names
# 2. Keep tests small and focused
# 3. Use fixtures for setup and teardown
# 4. Parameterize tests for multiple scenarios
# 5. Use markers to categorize tests

# Common Pitfalls:
# 1. Overusing fixtures, leading to complex test setups
# 2. Not cleaning up resources after tests
# 3. Writing tests that depend on each other
# 4. Ignoring test performance

# Advanced Tips:
# 1. Use pytest.mark to categorize and selectively run tests
# 2. Leverage parametrization for comprehensive test coverage
# 3. Create custom fixtures for complex setup scenarios
# 4. Use pytest plugins to extend functionality

# Example of test parameterization
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, -1, -2),
])
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected

# Example of custom marker
@pytest.mark.slow
def test_slow_operation():
    time.sleep(1)
    assert True

# 4. Integration and Real-World Applications
# ------------------------------------------

# Example of testing a database interaction with a mock
class TestDatabaseInteraction:
    @pytest.fixture
    def mock_db(self):
        return MagicMock()

    def test_insert_user(self, mock_db):
        user = {"name": "John Doe", "email": "john@example.com"}
        mock_db.insert_user.return_value = True
        assert mock_db.insert_user(user) == True
        mock_db.insert_user.assert_called_once_with(user)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Asynchronous testing
@pytest.mark.asyncio
async def test_async_function():
    async def async_add(a, b):
        await asyncio.sleep(0.1)
        return a + b

    result = await async_add(2, 3)
    assert result == 5

# Property-based testing with hypothesis
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    # Q: How to run tests with increased verbosity?
    # A: Use the -v flag: pytest -v

    # Q: How to run a specific test function?
    # A: Specify the file and function: pytest test_file.py::test_function

    # Q: How to debug a failing test?
    # A: Use the --pdb flag to drop into the debugger on failure

    pass

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - pytest-cov: For measuring code coverage
# - pytest-mock: For easy mocking in pytest
# - pytest-xdist: For running tests in parallel
# - pytest-asyncio: For testing asynchronous code

# Resources:
# - Pytest documentation: https://docs.pytest.org/
# - "Python Testing with pytest" by Brian Okken
# - Real Python's Pytest tutorials: https://realpython.com/pytest-python-testing/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_tests():
    """Benchmark the performance of running tests."""
    start_time = time.time()
    
    pytest.main(['-v', __file__])
    
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
    print("Running tests...")
    pytest.main(['-v', __file__])

    print("\nDemonstrating FAQ and troubleshooting:")
    faq_and_troubleshooting()

    print("\nBenchmarking tests:")
    benchmark_tests()

if __name__ == "__main__":
    main()