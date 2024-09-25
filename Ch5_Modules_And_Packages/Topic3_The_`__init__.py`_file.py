# Modules and Packages - The __init__.py file - in the Python Programming Language
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
from controlledpackage import *
import unittest
import logging

# 1. Overview and Historical Context

"""
The __init__.py file is a crucial component in Python packages. Its primary purposes are:
1. To indicate that a directory should be treated as a Python package.
2. To initialize package-level variables and execute package-level code.
3. To define what should be imported when 'from package import *' is used.

Historical Context:
- Introduced in Python 1.5 (1997) along with the package system.
- Initially required for all packages, even if empty.
- Python 3.3 (PEP 420, 2012) introduced implicit namespace packages, allowing packages without __init__.py.

Significance in Modern Software Development:
- Crucial for structuring large Python projects and libraries.
- Essential for controlling the public API of a package.
- Important for package initialization and configuration.

Comparison with Other Languages:
- Similar to Java's package-info.java, but more versatile.
- More explicit than JavaScript's index.js convention.
- Provides functionality similar to C#'s namespaces, but with more flexibility.
"""

# 2. Syntax, Key Concepts, and Code Examples

def demonstrate_basic_init():
    """Demonstrates the basic usage of __init__.py."""
    package_structure = {
        'mypackage': {
            '__init__.py': '# This file is intentionally left empty',
            'module1.py': 'def func1():\n    print("Function 1")',
            'module2.py': 'def func2():\n    print("Function 2")'
        }
    }

    create_package_structure(package_structure)
    
    # Using the package
    import mypackage.module1
    mypackage.module1.func1()

def demonstrate_init_with_imports():
    """Demonstrates __init__.py with imports."""
    package_structure = {
        'advancedpackage': {
            '__init__.py': 'from .module1 import func1\nfrom .module2 import func2',
            'module1.py': 'def func1():\n    print("Advanced Function 1")',
            'module2.py': 'def func2():\n    print("Advanced Function 2")'
        }
    }

    create_package_structure(package_structure)
    
    # Using the package
    import advancedpackage
    advancedpackage.func1()
    advancedpackage.func2()

def demonstrate_init_with_all():
    """Demonstrates __init__.py with __all__ definition."""
    package_structure = {
        'controlledpackage': {
            '__init__.py': '__all__ = ["func1"]\nfrom .module1 import func1\nfrom .module2 import func2',
            'module1.py': 'def func1():\n    print("Controlled Function 1")',
            'module2.py': 'def func2():\n    print("Controlled Function 2")'
        }
    }

    create_package_structure(package_structure)
    
    
    func1()  # This works
    try:
        func2()  # This will raise a NameError
    except NameError:
        print("func2 is not imported due to __all__ definition")

def demonstrate_init_with_code():
    """Demonstrates __init__.py with executable code."""
    package_structure = {
        'configuredpackage': {
            '__init__.py': 'print("Initializing configuredpackage")\nPACKAGE_VERSION = "1.0.0"',
            'module.py': 'def get_version():\n    from . import PACKAGE_VERSION\n    return PACKAGE_VERSION'
        }
    }

    create_package_structure(package_structure)
    
    # Using the package
    import configuredpackage.module
    print(f"Package version: {configuredpackage.module.get_version()}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def demonstrate_best_practices():
    """Demonstrates best practices for __init__.py files."""
    package_structure = {
        'bestpractices': {
            '__init__.py': '''
# bestpractices/__init__.py

__version__ = "1.0.0"
__author__ = "Sabbir Hossain"

from .core import main_function
from .utils import helper_function

__all__ = ['main_function', 'helper_function']
''',
            'core.py': 'def main_function():\n    print("Main function")',
            'utils.py': 'def helper_function():\n    print("Helper function")'
        }
    }

    create_package_structure(package_structure)
    
    # Using the package
    import bestpractices
    print(f"Version: {bestpractices.__version__}")
    print(f"Author: {bestpractices.__author__}")
    bestpractices.main_function()
    bestpractices.helper_function()

def demonstrate_common_pitfalls():
    """Demonstrates common pitfalls with __init__.py files."""
    # Pitfall 1: Circular imports
    package_structure = {
        'circularpkg': {
            '__init__.py': 'from .module_a import func_a',
            'module_a.py': 'from .module_b import func_b\ndef func_a():\n    print("Function A")\n    func_b()',
            'module_b.py': 'from .module_a import func_a\ndef func_b():\n    print("Function B")\n    func_a()'
        }
    }

    create_package_structure(package_structure)
    
    try:
        import circularpkg
    except ImportError as e:
        print(f"Circular import detected: {e}")

    # Pitfall 2: Side effects in __init__.py
    package_structure = {
        'sideeffectpkg': {
            '__init__.py': 'print("This print statement is a side effect")',
            'module.py': 'def func():\n    print("Function")'
        }
    }

    create_package_structure(package_structure)
    
    print("Importing package with side effects:")
    import sideeffectpkg

def demonstrate_advanced_techniques():
    """Demonstrates advanced techniques with __init__.py files."""
    # Lazy loading
    package_structure = {
        'lazypackage': {
            '__init__.py': '''
import importlib

def __getattr__(name):
    if name == 'heavy_module':
        return importlib.import_module('.heavy_module', __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
''',
            'heavy_module.py': '''
print("Heavy module loaded")
def heavy_function():
    print("Heavy function executed")
'''
        }
    }

    create_package_structure(package_structure)
    
    import lazypackage
    print("Package imported, heavy module not loaded yet")
    lazypackage.heavy_module.heavy_function()

# 4. Integration and Real-World Applications

def demonstrate_real_world_usage():
    """Demonstrates real-world usage of __init__.py files."""
    # Example: A simple logging package
    package_structure = {
        'mylogging': {
            '__init__.py': '''
from .logger import Logger
from .handlers import FileHandler, ConsoleHandler

__all__ = ['Logger', 'FileHandler', 'ConsoleHandler']

# Package-level logger configuration
import logging
logging.basicConfig(level=logging.INFO)
''',
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

    create_package_structure(package_structure)
    
    # Using the logging package
    from mylogging import Logger, FileHandler, ConsoleHandler

    logger = Logger("MyApp")
    logger.add_handler(FileHandler("app.log"))
    logger.add_handler(ConsoleHandler())
    logger.log("Application started")

# 5. Advanced Concepts and Emerging Trends

def demonstrate_advanced_concepts():
    """Demonstrates advanced concepts and emerging trends related to __init__.py."""
    # Namespace packages (PEP 420)
    print("Namespace packages allow package splitting across multiple directories.")
    print("They don't require an __init__.py file.")

    # Implicit namespace packages
    package_structure = {
        'implicit_pkg': {
            'module1.py': 'def func1():\n    print("Implicit package function")'
        }
    }

    create_package_structure(package_structure)
    
    sys.path.append('.')
    from implicit_pkg import module1
    module1.func1()

    # Type hinting in __init__.py (PEP 561)
    package_structure = {
        'typed_pkg': {
            '__init__.py': '''
from typing import List

def typed_function(x: int) -> List[int]:
    return [x, x*2, x*3]

__all__ = ['typed_function']
'''
        }
    }

    create_package_structure(package_structure)
    
    from typed_pkg import typed_function
    result = typed_function(5)
    print(f"Typed function result: {result}")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Provides answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: Do I always need an __init__.py file?": 
            "A: Not always. Since Python 3.3, implicit namespace packages don't require __init__.py.",
        "Q: Can I use 'from module import *' in __init__.py?":
            "A: Yes, but it's generally discouraged due to potential namespace pollution.",
        "Q: How can I prevent certain modules from being imported with 'from package import *'?":
            "A: Define __all__ in your __init__.py to explicitly list allowed imports.",
        "Q: My imports in __init__.py are causing circular dependencies. How can I fix this?":
            "A: Consider using lazy imports or restructuring your package to avoid circular dependencies."
    }

    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources

def recommend_resources():
    """Recommends tools, libraries, and resources for working with __init__.py files."""
    resources = {
        "Tools": [
            "pyflakes - for detecting unused imports",
            "isort - for sorting imports",
            "pylint - for detecting issues in __init__.py files"
        ],
        "Libraries": [
            "importlib - for dynamic imports",
            "typing - for type hinting in __init__.py"
        ],
        "Documentation": [
            "PEP 8 - Style Guide for Python Code",
            "PEP 420 - Implicit Namespace Packages",
            "PEP 561 - Distributing and Packaging Type Information"
        ],
        "Books": [
            "Python Packaging User Guide by Python Packaging Authority",
            "Python in a Nutshell by Alex Martelli et al."
        ]
    }

    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
        print()

# 8. Performance Analysis and Optimization

def analyze_init_performance():
    """Demonstrates how to analyze and optimize __init__.py performance."""
    def time_import(package_name: str) -> float:
        start_time = time.time()
        importlib.import_module(package_name)
        end_time = time.time()
        return end_time - start_time

    # Create packages with different __init__.py contents
    package_structures = {
        'empty_init': {
            '__init__.py': '',
            'module.py': 'def func():\n    pass'
        },
        'simple_init': {
            '__init__.py': 'from .module import func',
            'module.py': 'def func():\n    pass'
        },
        'complex_init': {
            '__init__.py': '''
import time
time.sleep(0.1)  # Simulate some initialization work
from .module import func
''',
            'module.py': 'def func():\n    pass'
        }
    }

    for pkg_name, structure in package_structures.items():
        create_package_structure({pkg_name: structure})

    sys.path.append('.')

    for pkg_name in package_structures.keys():
        import_time = time_import(pkg_name)
        print(f"Time to import {pkg_name}: {import_time:.6f} seconds")

    print("\nOptimization Tips:")
    print("1. Keep __init__.py files as small as possible")
    print("2. Use lazy imports for modules not always needed")
    print("3. Avoid time-consuming operations in __init__.py")
    print("4. Use profiling tools to identify slow imports")

# Helper function to create package structures
def create_package_structure(structure, base_path='.'):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_package_structure(content, path)
        else:
            with open(path, 'w') as f:
                f.write(content)

def main():
    """Main function to demonstrate all concepts."""
    print("1. Basic __init__.py Usage")
    demonstrate_basic_init()
    
    print("\n2. __init__.py with Imports")
    demonstrate_init_with_imports()
    
    print("\n3. __init__.py with __all__")
    demonstrate_init_with_all()
    
    print("\n4. __init__.py with Executable Code")
    demonstrate_init_with_code()
    
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
    analyze_init_performance()

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