# Modules and Packages - Third-party Packages and pip - in the Python Programming Language
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
import subprocess
import venv
import site
import pkg_resources
from typing import List, Dict, Any
import unittest
import timeit

# 1. Overview and Historical Context

"""
Third-party packages in Python are external libraries and modules not included in the Python
standard library. They extend Python's functionality, allowing developers to leverage existing
code for various tasks. pip (Pip Installs Packages) is the standard package installer for Python.

Historical Context:
- The concept of third-party packages dates back to the early days of Python.
- The Python Package Index (PyPI) was established in 2003 to host third-party packages.
- pip was introduced in 2008 as part of the setuptools project.
- pip became the official package installer for Python with Python 3.4 in 2014.

Significance in Modern Software Development:
- Essential for rapid development and code reuse.
- Enables the Python ecosystem to thrive with a vast array of specialized libraries.
- Facilitates dependency management in complex projects.

Comparison with Other Languages:
- Similar to npm for JavaScript, gem for Ruby, and Maven/Gradle for Java.
- Python's pip and PyPI system is more centralized compared to some other languages.
- The "batteries included" philosophy of Python's standard library means fewer essential
  packages need to be installed separately compared to some other languages.
"""

# 2. Syntax, Key Concepts, and Code Examples

def demonstrate_pip_usage():
    """Demonstrates basic usage of pip."""
    print("Basic pip commands:")
    print("1. Install a package: pip install package_name")
    print("2. Uninstall a package: pip uninstall package_name")
    print("3. List installed packages: pip list")
    print("4. Show package info: pip show package_name")
    print("5. Install from requirements file: pip install -r requirements.txt")

    # Note: The following commands are commented out to prevent actual execution
    # subprocess.run(["pip", "install", "requests"])
    # subprocess.run(["pip", "list"])
    # subprocess.run(["pip", "show", "requests"])

def demonstrate_virtual_environments():
    """Demonstrates the use of virtual environments."""
    venv_path = "./my_venv"
    
    print(f"Creating a virtual environment at {venv_path}")
    venv.create(venv_path, with_pip=True)
    
    print("To activate the virtual environment:")
    print("On Windows: my_venv\\Scripts\\activate")
    print("On Unix or MacOS: source my_venv/bin/activate")
    
    print("\nVirtual environment created. You can now install packages in isolation.")

def demonstrate_package_usage():
    """Demonstrates how to use a third-party package (requests as an example)."""
    try:
        import requests
        
        response = requests.get("https://api.github.com")
        print(f"GitHub API Status Code: {response.status_code}")
        print(f"GitHub API Response: {response.json()}")
    except ImportError:
        print("requests package is not installed. Install it using: pip install requests")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def demonstrate_best_practices():
    """Demonstrates best practices for using third-party packages and pip."""
    
    print("Best Practices:")
    print("1. Always use virtual environments for project isolation.")
    print("2. Pin your dependencies using a requirements.txt file.")
    print("3. Use version specifiers to ensure compatibility.")
    print("4. Regularly update your packages for security and features.")
    print("5. Be cautious when installing packages from unknown sources.")
    
    # Example of a good requirements.txt file
    requirements = """
    requests==2.26.0
    numpy>=1.21.0,<2.0.0
    pandas~=1.3.0
    """
    with open("requirements.txt", "w") as f:
        f.write(requirements)
    print("\nExample requirements.txt file created.")

def demonstrate_common_pitfalls():
    """Demonstrates common pitfalls and how to avoid them."""
    
    print("Common Pitfalls:")
    print("1. Installing packages globally instead of in a virtual environment.")
    print("2. Not specifying version numbers, leading to compatibility issues.")
    print("3. Overlooking transitive dependencies.")
    print("4. Ignoring security vulnerabilities in third-party packages.")
    
    print("\nTo check for security vulnerabilities:")
    # Note: The following command is commented out to prevent actual execution
    # subprocess.run(["pip", "install", "safety"])
    # subprocess.run(["safety", "check"])

def demonstrate_advanced_tips():
    """Demonstrates advanced tips for package management."""
    
    print("Advanced Tips:")
    print("1. Use pip-tools for dependency pinning and compilation.")
    print("2. Leverage editable installs for local development.")
    print("3. Understand the difference between setup.py and requirements.txt.")
    print("4. Use constraints files for complex dependency resolution.")
    
    # Example of an editable install
    print("\nEditable install example:")
    print("pip install -e .")
    
    # Example of a constraints file
    constraints = """
    requests==2.26.0
    urllib3==1.26.7
    """
    with open("constraints.txt", "w") as f:
        f.write(constraints)
    print("\nExample constraints.txt file created.")
    print("Use with: pip install -c constraints.txt package_name")

# 4. Integration and Real-World Applications

def demonstrate_real_world_usage():
    """Demonstrates real-world usage of third-party packages."""
    
    print("Real-World Usage Examples:")
    print("1. Web Development with Django or Flask")
    print("2. Data Analysis with pandas and numpy")
    print("3. Machine Learning with scikit-learn or TensorFlow")
    print("4. API Development with FastAPI")
    print("5. Task Automation with Celery")
    
    # Example: Simple data analysis with pandas (if installed)
    try:
        import pandas as pd
        
        data = {'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [25, 30, 35],
                'City': ['New York', 'Paris', 'London']}
        df = pd.DataFrame(data)
        print("\nSample pandas DataFrame:")
        print(df)
    except ImportError:
        print("\npandas is not installed. Install it using: pip install pandas")

# 5. Advanced Concepts and Emerging Trends

def demonstrate_advanced_concepts():
    """Demonstrates advanced concepts and emerging trends in package management."""
    
    print("Advanced Concepts and Emerging Trends:")
    print("1. Poetry: Modern dependency management and packaging")
    print("2. Pipenv: Combines pip and virtualenv")
    print("3. Conda: Package management system for any language")
    print("4. Docker: Containerization for consistent environments")
    print("5. pyproject.toml: New standard for Python project metadata")
    
    # Example pyproject.toml content
    pyproject_content = """
    [tool.poetry]
    name = "my-project"
    version = "0.1.0"
    description = "A sample Python project"
    authors = ["Sabbir Hossain <sabbir@example.com>"]

    [tool.poetry.dependencies]
    python = "^3.9"
    requests = "^2.26.0"

    [build-system]
    requires = ["poetry-core>=1.0.0"]
    build-backend = "poetry.core.masonry.api"
    """
    with open("pyproject.toml", "w") as f:
        f.write(pyproject_content)
    print("\nExample pyproject.toml file created.")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Provides answers to common questions and troubleshooting tips."""
    
    faqs = {
        "Q: How do I resolve package conflicts?": 
            "A: Use virtual environments, specify exact versions, and consider using tools like pip-tools.",
        "Q: What's the difference between pip and conda?":
            "A: pip is Python-specific and installs from PyPI, while conda is language-agnostic and has its own package repository.",
        "Q: How can I create a reproducible environment?":
            "A: Use virtual environments and pin your dependencies in a requirements.txt or pyproject.toml file.",
        "Q: How do I install a package from a GitHub repository?":
            "A: Use pip install git+https://github.com/user/repo.git"
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")
    
    print("Troubleshooting Tips:")
    print("1. Check your Python and pip versions")
    print("2. Verify your virtual environment is activated")
    print("3. Clear pip cache if facing weird issues: pip cache purge")
    print("4. Use verbose output for more info: pip install -v package_name")

# 7. Recommended Tools, Libraries, and Resources

def recommend_resources():
    """Recommends tools, libraries, and resources for working with third-party packages and pip."""
    
    resources = {
        "Documentation": [
            "Python Packaging User Guide (https://packaging.python.org/)",
            "pip documentation (https://pip.pypa.io/)",
            "PyPI (https://pypi.org/)"
        ],
        "Tools": [
            "pipenv - Dependency management tool",
            "poetry - Dependency management and packaging made easy",
            "pip-tools - Set of tools for managing Python packages"
        ],
        "Books": [
            "Python Packages by Tomas Beuzen",
            "Distributing Python Modules by Python Software Foundation"
        ],
        "Courses": [
            "Python Packaging and Virtual Environments on Pluralsight",
            "Managing Python Dependencies on LinkedIn Learning"
        ]
    }
    
    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
        print()

# 8. Performance Analysis and Optimization

def analyze_performance():
    """Demonstrates performance analysis and optimization techniques for package management."""
    
    print("Performance Analysis and Optimization:")
    print("1. Use pip's download cache to speed up repeated installations")
    print("2. Leverage wheel distributions for faster installation")
    print("3. Use pip's --no-deps option to skip dependency checks when appropriate")
    print("4. Consider using compiled extensions for performance-critical code")
    
    # Example: Measuring installation time
    def time_install(package):
        command = f"pip install {package}"
        return timeit.timeit(f"subprocess.run('{command}', shell=True, check=True)", 
                             setup="import subprocess", number=1)
    
    packages = ["requests", "numpy"]
    for pkg in packages:
        time = time_install(pkg)
        print(f"Time to install {pkg}: {time:.2f} seconds")
    
    print("\nOptimization Tip: Use 'pip install --only-binary=:all: package_name' for wheel-only installations")

def main():
    """Main function to demonstrate all concepts."""
    print("1. Basic pip Usage")
    demonstrate_pip_usage()
    
    print("\n2. Virtual Environments")
    demonstrate_virtual_environments()
    
    print("\n3. Using Third-Party Packages")
    demonstrate_package_usage()
    
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