# Modules and Packages - Importing and Packages - in the Python Programming Language
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
import importlib
import time
from types import ModuleType
from typing import Any, Callable

# 1. Overview and Historical Context

"""
Modules and packages are fundamental concepts in Python for organizing and structuring code.
They allow developers to break down large programs into smaller, manageable files and 
provide a mechanism for code reuse and namespace management.

A module is a single Python file containing Python definitions and statements. The file name
is the module name with the suffix .py added. Modules have been part of Python since its 
inception in 1991, introduced by Guido van Rossum to promote code organization and reusability.

Packages, introduced in Python 1.5 (1997), are a way of structuring Python's module namespace
by using "dotted module names". A package is a directory containing Python files and a special
__init__.py file, which tells Python that the directory should be treated as a package.

The import system in Python has evolved significantly over time:
- Python 2.7 introduced relative imports.
- Python 3.1 added the importlib module, providing a flexible API for implementing custom importers.
- Python 3.3 brought namespace packages, allowing package directories without __init__.py files.
- Python 3.4 introduced the pathlib module, offering object-oriented filesystem paths.

In modern software development, modules and packages are crucial for:
- Code organization and maintenance
- Encapsulation and information hiding
- Dependency management
- Creating reusable libraries and frameworks

Compared to other languages:
- Python's import system is similar to Java's package system but more flexible.
- Unlike C++'s #include, Python's import is a runtime operation, allowing for dynamic importing.
- Python's packages are conceptually similar to namespaces in C++ but with different implementation details.
"""

# 2. Syntax, Key Concepts, and Code Examples

def demonstrate_basic_import():
    """Demonstrates basic import syntax and usage."""
    import math  # Standard library module

    def calculate_circle_area(radius: float) -> float:
        """Calculate the area of a circle."""
        return math.pi * radius ** 2

    print(f"Area of circle with radius 5: {calculate_circle_area(5):.2f}")

    # From ... import ... syntax
    from random import randint

    print(f"Random integer between 1 and 10: {randint(1, 10)}")

def demonstrate_package_import():
    """Demonstrates importing from packages."""
    # Assuming a package structure:
    # mypackage/
    #     __init__.py
    #     module1.py
    #     subpackage/
    #         __init__.py
    #         module2.py

    # Import a module from a package
    from mypackage import module1

    # Import a specific function from a module in a package
    from mypackage.subpackage.module2 import some_function

    # Use the imported function
    result = some_function()
    print(f"Result from some_function: {result}")

def demonstrate_relative_import():
    """Demonstrates relative import syntax."""
    # Note: This is a demonstration and won't run in this context.
    # It would be used within a package structure.

    # from . import module_in_same_directory
    # from .. import module_in_parent_directory
    # from ..sibling_package import module_in_sibling_package

    print("Relative imports demonstrated (see comments)")

def demonstrate_dynamic_import():
    """Demonstrates dynamic importing of modules."""
    module_name = "math"
    math_module = importlib.import_module(module_name)
    
    print(f"Dynamically imported {module_name}")
    print(f"Pi from dynamically imported module: {math_module.pi}")

def demonstrate_lazy_import():
    """Demonstrates lazy importing for performance optimization."""
    class LazyImport:
        def __init__(self, module_name):
            self.module_name = module_name
            self.module = None

        def __getattr__(self, name):
            if self.module is None:
                self.module = importlib.import_module(self.module_name)
            return getattr(self.module, name)

    # Usage
    np = LazyImport("numpy")
    # numpy is not imported until we actually use it
    print(f"NumPy version: {np.__version__}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def demonstrate_best_practices():
    """Demonstrates best practices for imports."""
    # Standard library imports
    import os
    import sys

    # Third-party imports
    import numpy as np
    import pandas as pd

    # Local application/library specific imports
    from mypackage import mymodule

    # Avoid wildcard imports
    # from module import *  # This is generally discouraged

    # Use aliases for long module names
    import very_long_module_name as long_mod

    print("Best practices for imports demonstrated")

def demonstrate_circular_import_problem():
    """Demonstrates the circular import problem and a solution."""
    # This is a common pitfall. Suppose we have two modules:
    # module_a.py
    # from module_b import func_b
    # def func_a():
    #     print("Function A")
    #     func_b()

    # module_b.py
    # from module_a import func_a
    # def func_b():
    #     print("Function B")
    #     func_a()

    # This creates a circular import. To solve this:
    # 1. Restructure your code to avoid circular dependencies
    # 2. Move the import inside the function where it's needed
    # 3. Use import statements at the end of the module

    print("Circular import problem demonstrated (see comments)")

def demonstrate_import_hooks():
    """Demonstrates using import hooks for advanced importing behavior."""
    class PrintingImporter:
        def __init__(self, path):
            self.path = path

        def find_module(self, fullname, path=None):
            print(f"Searching for module: {fullname}")
            return None  # Let regular import mechanism handle the actual import

    # Register the import hook
    sys.meta_path.append(PrintingImporter(sys.path))

    # Now, when we import, it will print a message
    import math

    print("Import hook demonstrated")

# 4. Integration and Real-World Applications

def demonstrate_plugin_system():
    """Demonstrates a simple plugin system using dynamic imports."""
    plugin_dir = "./plugins"
    sys.path.append(plugin_dir)

    def load_plugins():
        plugins = []
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]  # Remove .py extension
                module = importlib.import_module(module_name)
                if hasattr(module, "run"):
                    plugins.append(module)
        return plugins

    # Usage
    plugins = load_plugins()
    for plugin in plugins:
        plugin.run()

    print("Plugin system demonstrated")

# 5. Advanced Concepts and Emerging Trends

def demonstrate_namespace_packages():
    """Demonstrates namespace packages (Python 3.3+)."""
    # Namespace packages allow package directories without __init__.py files
    # This is useful for distributing a namespace package across multiple directories

    # Example structure:
    # /path/to/project1/mynamespace/module1.py
    # /path/to/project2/mynamespace/module2.py

    # Both can be imported as:
    # import mynamespace.module1
    # import mynamespace.module2

    print("Namespace packages demonstrated (see comments)")

# 6. FAQs and Troubleshooting

def faq_and_troubleshooting():
    """Provides answers to common questions and troubleshooting tips."""
    print("FAQs and Troubleshooting:")
    print("Q: Why is my import not working?")
    print("A: Check your PYTHONPATH and ensure the module is in a directory Python can find.")
    
    print("\nQ: How do I reload a module?")
    print("A: Use importlib.reload(module) to reload a module.")
    
    print("\nQ: How can I see where a module is being imported from?")
    print("A: Use print(module.__file__) to see the file path of an imported module.")

# 7. Recommended Tools, Libraries, and Resources

def recommend_resources():
    """Recommends tools, libraries, and resources for working with Python imports."""
    print("Recommended Resources:")
    print("1. importlib: Built-in library for implementing import")
    print("2. pip: Package installer for Python")
    print("3. virtualenv: Tool to create isolated Python environments")
    print("4. isort: Library to sort imports alphabetically and separate them into sections")
    print("5. Python Import System documentation: https://docs.python.org/3/reference/import.html")

# 8. Performance Analysis and Optimization

def analyze_import_performance():
    """Demonstrates how to analyze and optimize import performance."""
    def time_import(module_name: str) -> float:
        start_time = time.time()
        importlib.import_module(module_name)
        end_time = time.time()
        return end_time - start_time

    print(f"Time to import 'math': {time_import('math'):.6f} seconds")
    print(f"Time to import 'numpy': {time_import('numpy'):.6f} seconds")

    print("\nOptimization Tips:")
    print("1. Use lazy imports for modules not always needed")
    print("2. Consider using __all__ in your modules to restrict what's imported with 'from module import *'")
    print("3. Use profiling tools like cProfile to identify slow imports")

def main():
    """Main function to demonstrate all concepts."""
    print("1. Basic Import Demonstration")
    demonstrate_basic_import()
    
    print("\n2. Package Import Demonstration")
    # demonstrate_package_import()  # Commented out as it requires a specific package structure
    
    print("\n3. Relative Import Demonstration")
    demonstrate_relative_import()
    
    print("\n4. Dynamic Import Demonstration")
    demonstrate_dynamic_import()
    
    print("\n5. Lazy Import Demonstration")
    demonstrate_lazy_import()
    
    print("\n6. Best Practices Demonstration")
    demonstrate_best_practices()
    
    print("\n7. Circular Import Problem Demonstration")
    demonstrate_circular_import_problem()
    
    print("\n8. Import Hooks Demonstration")
    demonstrate_import_hooks()
    
    print("\n9. Plugin System Demonstration")
    # demonstrate_plugin_system()  # Commented out as it requires a specific directory structure
    
    print("\n10. Namespace Packages Demonstration")
    demonstrate_namespace_packages()
    
    print("\n11. FAQs and Troubleshooting")
    faq_and_troubleshooting()
    
    print("\n12. Recommended Resources")
    recommend_resources()
    
    print("\n13. Performance Analysis and Optimization")
    analyze_import_performance()

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