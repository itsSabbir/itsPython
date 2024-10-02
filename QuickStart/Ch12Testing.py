#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Python Cheat Sheet: Testing
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import unittest
import pytest
import doctest
import mock
from unittest.mock import patch, MagicMock
import asyncio
import asynctest

# 1. Unit Testing with unittest

# Sample function to test
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
    
    def test_add_strings(self):
        with self.assertRaises(TypeError):
            add("2", "3")

# Running tests
if __name__ == '__main__':
    unittest.main()

# Tip: Use assertAlmostEqual for floating-point comparisons to avoid precision issues

# Test fixtures
class TestWithSetupAndTeardown(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test.txt', 'w')
    
    def tearDown(self):
        self.test_file.close()
    
    def test_write_to_file(self):
        self.test_file.write("Hello, World!")
        self.test_file.seek(0)
        content = self.test_file.read()
        self.assertEqual(content, "Hello, World!")

# Tip: Use setUp and tearDown for common setup and cleanup operations

# Parameterized tests
class TestParameterized(unittest.TestCase):
    def test_odd_even(self):
        test_cases = [
            (3, "odd"),
            (4, "even"),
            (0, "even"),
            (-1, "odd"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual("odd" if num % 2 else "even", expected)

# Tip: Use subTest for parameterized tests to get granular test results

# 2. Mocking

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

def greet_user(user):
    return f"Hello, {user.get_name()}!"

class TestGreetUser(unittest.TestCase):
    @patch('__main__.User')
    def test_greet_user(self, MockUser):
        mock_user = MockUser()
        mock_user.get_name.return_value = "Alice"
        
        result = greet_user(mock_user)
        self.assertEqual(result, "Hello, Alice!")
        mock_user.get_name.assert_called_once()

# Tip: Use mock objects to isolate the code being tested from its dependencies

# 3. pytest

# pytest automatically discovers test functions prefixed with "test_"
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

# Parameterized tests with pytest
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Fixtures in pytest
@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello, World!")
    return file

def test_read_file(sample_file):
    content = sample_file.read_text()
    assert content == "Hello, World!"

# Tip: pytest fixtures are more powerful and flexible than unittest setUp/tearDown

# Marking tests
@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(2)
    assert True

# Run only slow tests: pytest -v -m slow

# Monkeypatching
def get_os_name():
    import os
    return os.name

def test_get_os_name(monkeypatch):
    monkeypatch.setattr('os.name', 'test_os')
    assert get_os_name() == 'test_os'

# Tip: Use monkeypatch for modifying behavior during tests

# 4. Doctests

def multiply(a, b):
    """
    Multiply two numbers.

    >>> multiply(2, 3)
    6
    >>> multiply(-1, 4)
    -4
    """
    return a * b

# Run with: python -m doctest filename.py

# Tip: Doctests are great for ensuring that your documentation stays up to date with your code

# 5. Property-based testing with Hypothesis

from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)

# Tip: Property-based testing helps discover edge cases you might not think of

# 6. Testing asynchronous code

async def async_add(a, b):
    await asyncio.sleep(0.1)
    return a + b

class TestAsyncAdd(asynctest.TestCase):
    async def test_async_add(self):
        result = await async_add(2, 3)
        self.assertEqual(result, 5)

# Run with: python -m asynctest filename.py

# Tip: Use asynctest for testing asynchronous code to handle coroutines properly

# 7. Test Coverage

# Install coverage: pip install coverage

# Run tests with coverage:
# coverage run -m pytest
# coverage report
# coverage html  # for detailed HTML report

# Tip: Aim for high test coverage, but remember that 100% coverage doesn't guarantee bug-free code

# 8. Tox for testing across multiple Python versions

# tox.ini
"""
[tox]
envlist = py36,py37,py38,py39

[testenv]
deps = pytest
commands = pytest
"""

# Run with: tox

# Tip: Use tox to ensure your code works across different Python versions

# 9. Continuous Integration

# .travis.yml for Travis CI
"""
language: python
python:
  - "3.6"
  - "3.7"
  - "3.8"
  - "3.9"
install:
  - pip install -r requirements.txt
script:
  - pytest
"""

# Tip: Set up CI to automatically run tests on every commit

# 10. Best Practices

# 1. Write tests before writing code (Test-Driven Development)
# 2. Keep tests small, focused, and independent
# 3. Use descriptive test names that explain the expected behavior
# 4. Don't test implementation details, test behavior
# 5. Aim for fast tests to encourage running them frequently
# 6. Use appropriate assertions (e.g., assertEqual, assertTrue, assertRaises)
# 7. Don't use print statements in tests, use assertions
# 8. Separate unit tests from integration and end-to-end tests
# 9. Use continuous integration to run tests automatically
# 10. Regularly review and update tests as code changes
# 11. Mock external dependencies to isolate the code being tested
# 12. Use parameterized tests to cover multiple scenarios
# 13. Test edge cases and boundary conditions
# 14. Maintain a balance between test coverage and development speed
# 15. Document your test suite and how to run it in your project README

# This concludes the enhanced detailed Python Cheat Sheet for Testing