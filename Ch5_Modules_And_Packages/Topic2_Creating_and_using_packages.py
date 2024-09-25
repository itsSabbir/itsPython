# Modules and Packages - Creating and Using Packages - in the Python Programming Language
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

import os
import sys
import importlib
import time
from types import ModuleType
from typing import Any, Callable, List, Dict
from bestpractices import *
import unittest
import logging

# 1. Overview and Historical Context

"""
Packages in Python are a way of structuring the module namespace using "dotted module names".
They provide a hierarchical structure for organizing related modules, making it easier to
manage large codebases and avoid naming conflicts.

Historical Context:
- Packages were introduced in Python 1.5 (1997) to address the need for better code organization.
- The concept was inspired by Java's package system but adapted to fit Python's philosophy.
- PEP 328 (2003) introduced relative imports, enhancing package functionality.
- PEP 420 (Python 3.3, 2012) introduced namespace packages, allowing package splitting across multiple directories.

Significance in Modern Software Development:
- Essential for creating reusable and distributable libraries
- Crucial for managing dependencies in large-scale applications
- Fundamental to Python's ecosystem and package management tools like pip

Comparison with Other Languages:
- Similar to Java packages but more flexible (e.g., no strict correspondence between package names and directory structure)
- More hierarchical than C++'s namespaces
- More structured than JavaScript's module system (pre-ES6)
"""

# 2. Syntax, Key Concepts, and Code Examples

def create_basic_package():
    """Demonstrates creating a basic package structure."""
    package_structure = {
        'mypackage': {
            '__init__.py': '',
            'module1.py': 'def func1():\n    print("Function 1")',
            'module2.py': 'def func2():\n    print("Function 2")',
            'subpackage': {
                '__init__.py': '',
                'submodule.py': 'def subfunc():\n    print("Subpackage function")'
            }
        }
    }

    def create_files(structure, base_path='.'):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(content, path)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    create_files(package_structure)
    print("Basic package structure created.")

def demonstrate_package_usage():
    """Demonstrates how to use the created package."""
    # Ensure the package is in the Python path
    sys.path.append('.')

    # Importing and using modules from the package
    import mypackage.module1
    from mypackage.module2 import func2
    from mypackage.subpackage import submodule

    mypackage.module1.func1()
    func2()
    submodule.subfunc()

def demonstrate_init_file_usage():
    """Demonstrates the use of __init__.py files."""
    # Create a package with a non-empty __init__.py
    package_structure = {
        'advancedpackage': {
            '__init__.py': 'from .module1 import func1\nfrom .module2 import func2',
            'module1.py': 'def func1():\n    print("Advanced Function 1")',
            'module2.py': 'def func2():\n    print("Advanced Function 2")'
        }
    }

    def create_files(structure, base_path='.'):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(content, path)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    create_files(package_structure)
    sys.path.append('.')

    # Using the package
    import advancedpackage

    advancedpackage.func1()  # This works because func1 is imported in __init__.py
    advancedpackage.func2()  # This also works for the same reason

def demonstrate_relative_imports():
    """Demonstrates the use of relative imports in packages."""
    # This is a demonstration and won't run in this context.
    # It would be used within a package structure.

    # Example structure:
    # mypackage/
    #     __init__.py
    #     module1.py
    #     subpackage/
    #         __init__.py
    #         module2.py

    # In mypackage/subpackage/module2.py:
    # from .. import module1  # Relative import from parent directory
    # from . import submodule  # Relative import from same directory

    print("Relative imports demonstrated (see comments)")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def demonstrate_best_practices():
    """Demonstrates best practices for creating and using packages."""
    # 1. Use clear and descriptive names for packages and modules
    # 2. Keep __init__.py files minimal
    # 3. Use relative imports within a package
    # 4. Follow PEP 8 style guide
    # 5. Use __all__ to control what's imported with 'from package import *'

    package_structure = {
        'bestpractices': {
            '__init__.py': '__all__ = ["module1", "module2"]',
            'module1.py': 'def func1():\n    """Well-documented function"""\n    print("Function 1")',
            'module2.py': 'def func2():\n    """Another well-documented function"""\n    print("Function 2")'
        }
    }

    def create_files(structure, base_path='.'):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(content, path)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    create_files(package_structure)
    sys.path.append('.')

    # Using the package
    try:
        import bestpractices.module1 as module1
        import bestpractices.module2 as module2

        module1.func1()
        module2.func2()

        print("Demonstrating use of __all__:")
        
        print("Available modules:", ', '.join(__all__))
    except ImportError as e:
        print(f"Error importing bestpractices: {e}")
        print("This is expected if running the entire script at once.")
        print("To test this function, run it separately after creating the package structure.")
        print("\nBest Practices:")
        print("1. Use clear, descriptive names for packages and modules")
        print("2. Keep __init__.py files minimal")
        print("3. Use relative imports within a package")
        print("4. Follow PEP 8 style guide")
        print("5. Use __all__ to control what's imported with 'from package import *'")
        print("6. Avoid wildcard imports in functions or classes")
        print("7. Use absolute imports when importing from outside the current package")
        print("8. Document your modules, classes, and functions")




def demonstrate_common_pitfalls():
    """Demonstrates common pitfalls and how to avoid them."""
    # Pitfall 1: Circular imports
    print("Avoid circular imports by restructuring your code or using lazy imports.")

    # Pitfall 2: Overusing 'import *'
    print("Use specific imports instead of 'import *' to avoid namespace pollution.")

    # Pitfall 3: Hardcoding paths
    print("Use relative imports or sys.path manipulation instead of hardcoding paths.")

    # Pitfall 4: Naming conflicts
    print("Use unique names for packages and modules to avoid conflicts.")

def demonstrate_advanced_techniques():
    """Demonstrates advanced package techniques."""
    # 1. Dynamic importing
    module_name = "math"
    module = importlib.import_module(module_name)
    print(f"Dynamically imported {module_name}")

    # 2. Lazy loading
    class LazyLoader:
        def __init__(self, module_name):
            self.module_name = module_name
            self.module = None

        def __getattr__(self, name):
            if self.module is None:
                self.module = importlib.import_module(self.module_name)
            return getattr(self.module, name)

    lazy_math = LazyLoader("math")
    print(f"Pi: {lazy_math.pi}")  # Only now is math actually imported

    # 3. Package namespacing
    print("Namespace packages allow package splitting across multiple directories.")
    # This is a conceptual example and won't run in this context

# 4. Integration and Real-World Applications

def demonstrate_real_world_usage():
    """Demonstrates real-world usage of packages."""
    # Example: Creating a simple logging package
    package_structure = {
        'mylogging': {
            '__init__.py': 'from .logger import Logger\nfrom .handlers import FileHandler, ConsoleHandler',
            'logger.py': '''
class Logger:
    def __init__(self, name):
        self.name = name
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def log(self, message):
        for handler in self.handlers:
            handler.emit(f"{self.name}: {message}")
''',
            'handlers.py': '''
class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def emit(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\\n')

class ConsoleHandler:
    def emit(self, message):
        print(message)
'''
        }
    }

    def create_files(structure, base_path='.'):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(content, path)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    create_files(package_structure)
    sys.path.append('.')

    # Using the logging package
    from mylogging import Logger, FileHandler, ConsoleHandler

    logger = Logger("MyApp")
    logger.add_handler(FileHandler("app.log"))
    logger.add_handler(ConsoleHandler())
    logger.log("Application started")

# 5. Advanced Concepts and Emerging Trends

def demonstrate_advanced_concepts():
    """Demonstrates advanced concepts and emerging trends in Python packaging."""
    # 1. Namespace packages (PEP 420)
    print("Namespace packages allow package splitting across multiple directories.")

    # 2. Editable installs (PEP 660)
    print("Editable installs allow developers to modify installed packages without reinstalling.")

    # 3. Python Packaging Authority (PyPA) and modern tools
    print("PyPA provides tools like poetry and flit for modern Python packaging.")

    # 4. Type hinting and stub packages
    print("Stub packages (*.pyi files) provide type information for untyped packages.")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Provides answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: How do I make my package installable via pip?": 
            "A: Create a setup.py or pyproject.toml file with package metadata.",
        "Q: What's the difference between a module and a package?":
            "A: A module is a single Python file, while a package is a directory of Python modules.",
        "Q: How do I handle package dependencies?":
            "A: List them in your setup.py or pyproject.toml file.",
        "Q: How can I debug import issues?":
            "A: Use sys.path to check the Python path and ensure your package is in a directory Python can find."
    }

    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources

def recommend_resources():
    """Recommends tools, libraries, and resources for working with Python packages."""
    resources = {
        "Tools": ["pip", "setuptools", "poetry", "flit", "twine"],
        "Libraries": ["importlib", "pkgutil", "pkg_resources"],
        "Documentation": [
            "Python Packaging User Guide (https://packaging.python.org/)",
            "PEP 8 - Style Guide for Python Code",
            "PEP 420 - Implicit Namespace Packages"
        ],
        "Books": [
            "Python Packages by Tomas Beuzen",
            "Python in a Nutshell by Alex Martelli et al."
        ]
    }

    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
        print()

# 8. Performance Analysis and Optimization

def analyze_package_performance():
    """Demonstrates how to analyze and optimize package performance."""
    def time_import(module_name: str) -> float:
        start_time = time.time()
        importlib.import_module(module_name)
        end_time = time.time()
        return end_time - start_time

    print(f"Time to import 'math': {time_import('math'):.6f} seconds")
    print(f"Time to import 'numpy': {time_import('numpy'):.6f} seconds")

    print("\nOptimization Tips:")
    print("1. Use lazy imports for modules not always needed")
    print("2. Minimize imports in __init__.py files")
    print("3. Use profiling tools like cProfile to identify slow imports")
    print("4. Consider using __slots__ for classes with many instances")

def main():
    """Main function to demonstrate all concepts."""
    print("1. Creating a Basic Package")
    create_basic_package()
    
    print("\n2. Using a Package")
    demonstrate_package_usage()
    
    print("\n3. Using __init__.py Files")
    demonstrate_init_file_usage()
    
    print("\n4. Relative Imports")
    demonstrate_relative_imports()
    
    print("\n5. Best Practices")
    demonstrate_best_practices()
    
    print("\n6. Common Pitfalls")
    demonstrate_common_pitfalls()
    
    print("\n7. Advanced Techniques")
    demonstrate_advanced_techniques()
    
    print("\n8. Real-World Usage")
    demonstrate_real_world_usage()
    
    print("\n9. Advanced Concepts and Emerging Trends")
    demonstrate_advanced_concepts()
    
    print("\n10. FAQs and Troubleshooting")
    faqs_and_troubleshooting()
    
    print("\n11. Recommended Resources")
    recommend_resources()
    
    print("\n12. Performance Analysis and Optimization")
    analyze_package_performance()

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