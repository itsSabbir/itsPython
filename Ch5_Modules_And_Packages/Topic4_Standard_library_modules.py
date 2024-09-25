# Modules and Packages - Standard Library Modules - in the Python Programming Language
# Author: Sabbir Hossain
# Last Updated: September 21, 2024

"""
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
"""

import sys
import os
import time
import datetime
import math
import random
import json
import csv
import sqlite3
import logging
import unittest
import asyncio
from typing import List, Dict, Any
from collections import defaultdict, Counter
from functools import wraps

# 1. Overview and Historical Context

"""
The Python Standard Library is a collection of modules and packages that come bundled with Python.
These modules provide a wide range of functionality, from basic operations to complex tasks,
without the need for external dependencies.

Historical Context:
- The concept of a standard library dates back to the early days of Python (1991).
- Major additions and changes have been made with each Python version.
- Python 2.0 (2000) introduced many modules that are still fundamental today.
- Python 3.0 (2008) made significant changes and improvements to the standard library.

Significance in Modern Software Development:
- Provides a consistent, cross-platform set of tools for common tasks.
- Reduces the need for external dependencies, improving security and maintainability.
- Sets a standard for code quality and API design in the Python ecosystem.

Comparison with Other Languages:
- More extensive than many other languages' standard libraries (e.g., JavaScript).
- Similar in concept to Java's standard library, but with a broader range of functionality.
- Emphasizes "batteries included" philosophy, unlike some minimalist languages.
"""

# 2. Syntax, Key Concepts, and Code Examples

def demonstrate_basic_modules():
    """Demonstrates usage of basic standard library modules."""
    
    # Math operations
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")
    
    # Random number generation
    print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
    
    # Date and time operations
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    print(f"One week from now: {now + datetime.timedelta(weeks=1)}")

def demonstrate_file_operations():
    """Demonstrates file operations using standard library modules."""
    
    # Writing to a file
    with open('example.txt', 'w') as f:
        f.write("Hello, World!")
    
    # Reading from a file
    with open('example.txt', 'r') as f:
        content = f.read()
    print(f"File content: {content}")
    
    # JSON operations
    data = {'name': 'John', 'age': 30}
    json_string = json.dumps(data)
    print(f"JSON string: {json_string}")
    
    # CSV operations
    with open('example.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['John', 30])
    
    with open('example.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"CSV row: {row}")

def demonstrate_advanced_modules():
    """Demonstrates usage of more advanced standard library modules."""
    
    # Logging
    logging.basicConfig(level=logging.INFO)
    logging.info("This is an informational message")
    
    # SQLite database operations
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')
    c.execute("INSERT INTO stocks VALUES ('2024-09-21','BUY','AAPL',100,150.00)")
    conn.commit()
    
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
    
    conn.close()

    # Asynchronous operations
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def main():
        print(f"started at {time.strftime('%X')}")
        await say_after(1, 'hello')
        await say_after(2, 'world')
        print(f"finished at {time.strftime('%X')}")

    asyncio.run(main())

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def demonstrate_best_practices():
    """Demonstrates best practices when using standard library modules."""
    
    # Use context managers for resource management
    with open('example.txt', 'w') as f:
        f.write("Using context manager")
    
    # Use collections for efficient data structures
    d = defaultdict(int)
    words = ['apple', 'banana', 'apple', 'cherry']
    for word in words:
        d[word] += 1
    print(f"Word counts: {dict(d)}")
    
    # Use functools for higher-order functions
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.2f} seconds")
            return result
        return wrapper

    @timer
    def slow_function():
        time.sleep(1)

    slow_function()

def demonstrate_common_pitfalls():
    """Demonstrates common pitfalls and how to avoid them."""
    
    # Pitfall: Mutable default arguments
    def bad_append(item, lst=[]):
        lst.append(item)
        return lst

    print(bad_append(1))  # [1]
    print(bad_append(2))  # [1, 2] - Unexpected!

    # Correct way
    def good_append(item, lst=None):
        if lst is None:
            lst = []
        lst.append(item)
        return lst

    print(good_append(1))  # [1]
    print(good_append(2))  # [2]

    # Pitfall: Time zone awareness
    naive_time = datetime.datetime.now()
    aware_time = datetime.datetime.now(datetime.timezone.utc)
    print(f"Naive time: {naive_time}")
    print(f"Aware time: {aware_time}")

def demonstrate_advanced_tips():
    """Demonstrates advanced tips for using standard library modules."""
    
    # Using itertools for efficient iteration
    import itertools
    
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    print("First 10 Fibonacci numbers:")
    print(list(itertools.islice(fibonacci(), 10)))
    
    # Using functools.lru_cache for memoization
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    
    print(f"50th Fibonacci number: {fib(50)}")

# 4. Integration and Real-World Applications

def demonstrate_real_world_usage():
    """Demonstrates real-world usage of standard library modules."""
    
    # Web scraping with urllib
    from urllib.request import urlopen
    
    def get_python_zen():
        url = "https://www.python.org/dev/peps/pep-0020/"
        with urlopen(url) as response:
            html = response.read().decode('utf-8')
        import re
        pattern = r'<pre>(.*?)</pre>'
        match = re.search(pattern, html, re.DOTALL)
        if match:
            return match.group(1)
        return "Zen not found"
    
    print("The Zen of Python:")
    print(get_python_zen())
    
    # Data analysis with statistics
    import statistics
    
    data = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Mean: {statistics.mean(data)}")
    print(f"Median: {statistics.median(data)}")
    print(f"Mode: {statistics.mode(data)}")

# 5. Advanced Concepts and Emerging Trends

def demonstrate_advanced_concepts():
    """Demonstrates advanced concepts and emerging trends in standard library modules."""
    
    # Type hinting with typing module
    def greet(name: str) -> str:
        return f"Hello, {name}"
    
    print(greet("Python"))
    
    # Asynchronous context managers
    import asyncio
    import aiofiles  # Note: This is not in the standard library, but demonstrates the concept
    
    async def async_write():
        async with aiofiles.open('async_example.txt', 'w') as f:
            await f.write("Hello, Async World!")
    
    asyncio.run(async_write())
    
    # New string formatting with f-strings (Python 3.6+)
    name = "World"
    print(f"Hello, {name}!")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Provides answers to common questions and troubleshooting tips."""
    
    faqs = {
        "Q: How do I find which module to use for a specific task?": 
            "A: Check the Python Standard Library documentation or use the 'help()' function.",
        "Q: Why am I getting 'ImportError: No module named X'?":
            "A: Ensure the module is part of your Python version's standard library or installed separately.",
        "Q: How can I make my code work across different Python versions?":
            "A: Use the 'sys.version_info' to check the Python version and handle differences accordingly.",
        "Q: How do I handle deprecation warnings?":
            "A: Check the documentation for alternative modules or functions, and update your code accordingly."
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources

def recommend_resources():
    """Recommends tools, libraries, and resources for working with standard library modules."""
    
    resources = {
        "Documentation": [
            "Python Standard Library Documentation (https://docs.python.org/3/library/)",
            "Python Module of the Week (https://pymotw.com/3/)"
        ],
        "Books": [
            "Python Standard Library by Example by Doug Hellmann",
            "Fluent Python by Luciano Ramalho"
        ],
        "Tools": [
            "IDLE - Python's Integrated Development and Learning Environment",
            "IPython - Enhanced Interactive Python shell",
            "PyCharm - Professional IDE with excellent standard library integration"
        ],
        "Online Courses": [
            "Python for Everybody Specialization on Coursera",
            "Python Beyond the Basics on Pluralsight"
        ]
    }
    
    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
        print()

# 8. Performance Analysis and Optimization

def analyze_performance():
    """Demonstrates performance analysis and optimization techniques."""
    
    import timeit
    
    def slow_sum(n):
        return sum([i for i in range(n)])
    
    def fast_sum(n):
        return sum(range(n))
    
    n = 1000000
    
    slow_time = timeit.timeit(lambda: slow_sum(n), number=10)
    fast_time = timeit.timeit(lambda: fast_sum(n), number=10)
    
    print(f"Slow sum time: {slow_time:.4f} seconds")
    print(f"Fast sum time: {fast_time:.4f} seconds")
    print(f"Speed improvement: {slow_time / fast_time:.2f}x")
    
    # Memory usage optimization
    import sys
    
    list_comp = [i for i in range(1000000)]
    generator = (i for i in range(1000000))
    
    print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator size: {sys.getsizeof(generator)} bytes")

def main():
    """Main function to demonstrate all concepts."""
    print("1. Basic Standard Library Modules")
    demonstrate_basic_modules()
    
    print("\n2. File Operations with Standard Library")
    demonstrate_file_operations()
    
    print("\n3. Advanced Standard Library Modules")
    demonstrate_advanced_modules()
    
    print("\n4. Best Practices")
    demonstrate_best_practices()
    
    print("\n5. Common Pitfalls")
    demonstrate_common_pitfalls()
    
    print("\n6. Advanced Tips")
    demonstrate_advanced_tips()
    
    print("\n7. Real-World Usage")
    demonstrate_real_world_usage()
    
    print("\n8. Advanced Concepts and Emerging Trends")
    demonstrate_advanced_concepts()
    
    print("\n9. FAQs and Troubleshooting")
    faqs_and_troubleshooting()
    
    print("\n10. Recommended Resources")
    recommend_resources()
    
    print("\n11. Performance Analysis and Optimization")
    analyze_performance()

if __name__ == "__main__":
    main()

# 9. How to Contribute
"""
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
"""