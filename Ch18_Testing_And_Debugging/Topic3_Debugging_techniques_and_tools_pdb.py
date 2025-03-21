# Testing and Debugging - Debugging techniques and tools (pdb) - in the Python Programming Language
# =================================================================================================

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

import pdb
import sys
import traceback
import time
from typing import List, Any

# 1. Overview and Historical Context
# ----------------------------------
# Debugging is the process of finding and resolving defects or problems within a computer program.
# The Python Debugger (pdb) is an interactive source code debugger for Python programs.

# Historical context:
# - Debugging as a concept dates back to the early days of computing.
# - The term "bug" was popularized by Grace Hopper in 1947 when an actual moth caused a problem in the Harvard Mark II computer.
# - pdb has been part of Python's standard library since its early versions.
# - Over time, pdb has evolved to include more features and better integration with Python's language features.

# Significance:
# - Debugging is crucial for developing reliable and maintainable software.
# - pdb provides a powerful way to inspect program state and control execution flow during runtime.
# - It allows developers to step through code line by line, set breakpoints, and examine variables.

# Common use cases:
# - Tracking down logical errors in code
# - Understanding complex program flow
# - Investigating unexpected behavior or exceptions
# - Analyzing performance bottlenecks

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def buggy_function(a, b):
    """A function with a deliberate bug for demonstration purposes."""
    result = a / b  # Potential division by zero
    return result

def demonstrate_basic_pdb():
    """Demonstrate basic usage of pdb."""
    a, b = 10, 0
    pdb.set_trace()  # This will start the debugger
    result = buggy_function(a, b)
    print(f"Result: {result}")

# Key pdb commands:
# - n (next): Execute the next line
# - s (step): Step into a function call
# - c (continue): Continue execution until the next breakpoint
# - p <expression>: Print the value of an expression
# - l (list): List the current location in the code
# - q (quit): Quit the debugger

def demonstrate_pdb_commands():
    """Demonstrate various pdb commands."""
    x = 5
    y = 0
    pdb.set_trace()
    for i in range(3):
        y += x
        x += 1
    print(f"Final values: x = {x}, y = {y}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use meaningful variable names to make debugging easier
# 2. Keep functions small and focused for easier debugging
# 3. Use logging in addition to debugging for long-term issue tracking
# 4. Use assertions to catch issues early

# Common Pitfalls:
# 1. Forgetting to remove debugging statements before committing code
# 2. Over-relying on debugging instead of writing testable code
# 3. Ignoring warning messages and only debugging errors

# Advanced Tips:
# 1. Use conditional breakpoints for complex scenarios
# 2. Utilize post-mortem debugging for uncaught exceptions
# 3. Leverage pdb's ability to modify variables during runtime
# 4. Use custom debugging functions for repetitive tasks

def debug_example():
    """An example function to demonstrate advanced debugging techniques."""
    data = [1, 2, 3, 4, 5]
    total = 0
    for item in data:
        if item % 2 == 0:
            total += item
        # Conditional breakpoint example
        if item == 3:
            pdb.set_trace()
    return total

def custom_debug_function(locals_dict):
    """A custom function to print specific debug information."""
    print("Custom debug info:")
    print(f"data: {locals_dict['data']}")
    print(f"total: {locals_dict['total']}")
    print(f"item: {locals_dict['item']}")

# 4. Integration and Real-World Applications
# ------------------------------------------

class ComplexSystem:
    def __init__(self):
        self.data = []

    def process_data(self, input_data):
        for item in input_data:
            try:
                processed = self._complex_operation(item)
                self.data.append(processed)
            except Exception as e:
                print(f"Error processing item {item}: {e}")
                pdb.post_mortem()  # Start post-mortem debugging

    def _complex_operation(self, item):
        # Simulate a complex operation that might raise an exception
        if isinstance(item, dict):
            return item['value'] * 2
        else:
            raise ValueError("Invalid input")

def demonstrate_real_world_debugging():
    """Demonstrate debugging in a more complex, real-world scenario."""
    system = ComplexSystem()
    input_data = [{'value': 1}, {'value': 2}, 'invalid', {'value': 3}]
    system.process_data(input_data)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

import threading

def threaded_function(arg):
    """A function to be run in a separate thread."""
    pdb.set_trace()
    print(f"Running in thread with argument: {arg}")

def demonstrate_multi_threaded_debugging():
    """Demonstrate debugging in a multi-threaded environment."""
    threads = []
    for i in range(3):
        t = threading.Thread(target=threaded_function, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    # Q: How to start pdb from the command line?
    # A: Use python -m pdb script.py

    # Q: How to set a breakpoint in code without modifying it?
    # A: Use python -m pdb -c "b script.py:10" script.py

    # Q: How to debug a script that's run as a module?
    # A: Use python -m pdb -m module_name

    pass

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - ipdb: An enhanced version of pdb with features like tab completion
# - pudb: A full-screen, console-based visual debugger for Python
# - remote-pdb: A remote debugger based on pdb

# Resources:
# - Python's official pdb documentation: https://docs.python.org/3/library/pdb.html
# - "Python Debugging with Pdb" by Maryam Hanif
# - Real Python's guide on Python debugging: https://realpython.com/python-debugging-pdb/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_debugging():
    """Benchmark the performance impact of using pdb."""
    def function_without_pdb():
        total = 0
        for i in range(1000000):
            total += i
        return total

    def function_with_pdb():
        pdb.set_trace()
        total = 0
        for i in range(1000000):
            total += i
        return total

    start_time = time.time()
    function_without_pdb()
    without_pdb_time = time.time() - start_time

    start_time = time.time()
    function_with_pdb()  # Note: You'll need to manually continue execution in pdb
    with_pdb_time = time.time() - start_time

    print(f"Time without pdb: {without_pdb_time:.4f} seconds")
    print(f"Time with pdb: {with_pdb_time:.4f} seconds")
    print(f"Performance overhead: {(with_pdb_time - without_pdb_time) / without_pdb_time * 100:.2f}%")

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
    print("Basic pdb demonstration:")
    demonstrate_basic_pdb()

    print("\npdb commands demonstration:")
    demonstrate_pdb_commands()

    print("\nAdvanced debugging example:")
    debug_example()

    print("\nReal-world debugging scenario:")
    demonstrate_real_world_debugging()

    print("\nMulti-threaded debugging demonstration:")
    demonstrate_multi_threaded_debugging()

    print("\nFAQ and troubleshooting:")
    faq_and_troubleshooting()

    print("\nDebugging performance benchmark:")
    benchmark_debugging()

if __name__ == "__main__":
    main()