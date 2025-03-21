# Performance Optimization - Cython for performance-critical parts - in the Python Programming Language
# ===================================================================================================

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

import time
import numpy as np
from typing import List, Tuple

# Note: To use Cython, you need to install it: pip install cython
# For this note sheet, we'll use comments to represent Cython code, as it can't be directly executed in a Python file.

# 1. Overview and Historical Context
# ----------------------------------
# Cython is an optimizing static compiler that extends the Python programming language with additional
# syntax to enable the compilation of Python code to C, allowing for significant performance improvements
# in performance-critical parts of Python applications.

# Historical context:
# - Cython was first released in 2007 as a fork of the Pyrex project.
# - It was developed by Stefan Behnel, Robert Bradshaw, and others.
# - Cython has become an essential tool for scientific computing in Python, being used extensively in libraries like NumPy and SciPy.

# Significance:
# - Allows for easy integration of C code with Python
# - Provides a way to optimize performance-critical parts of Python code
# - Enables the use of static typing for improved performance
# - Facilitates the creation of Python extensions in a Python-like language

# Common use cases:
# - Numerical computations and scientific computing
# - Performance-critical parts of large Python applications
# - Wrapping external C libraries for use in Python

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Example 1: Basic Cython usage
def python_function(n: int) -> int:
    """A simple Python function to compare with Cython."""
    result = 0
    for i in range(n):
        result += i
    return result

# Cython equivalent (represented as a comment):
"""
# cython: language_level=3
def cython_function(int n):
    cdef int result = 0
    cdef int i
    for i in range(n):
        result += i
    return result
"""

# Example 2: Using C data types
"""
# cython: language_level=3
def cython_primes(int n):
    cdef int i, j
    cdef int[1000] primes
    cdef int count = 0
    
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            if count < 1000:
                primes[count] = i
                count += 1
    
    return [primes[i] for i in range(count)]
"""

def python_primes(n: int) -> List[int]:
    """Python equivalent of the Cython primes function."""
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

# Example 3: Working with NumPy arrays
"""
# cython: language_level=3
import numpy as np
cimport numpy as np

def cython_matrix_multiply(np.ndarray[np.float64_t, ndim=2] a, np.ndarray[np.float64_t, ndim=2] b):
    cdef int i, j, k
    cdef int m = a.shape[0]
    cdef int n = a.shape[1]
    cdef int p = b.shape[1]
    cdef np.ndarray[np.float64_t, ndim=2] result = np.zeros((m, p), dtype=np.float64)
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += a[i, k] * b[k, j]
    
    return result
"""

def python_matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Python equivalent of the Cython matrix multiplication function."""
    m, n = a.shape
    p = b.shape[1]
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += a[i, k] * b[k, j]
    return result

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Profile your code to identify performance bottlenecks before using Cython
# 2. Use static typing for variables and function arguments when possible
# 3. Minimize Python object creation and manipulation in performance-critical loops
# 4. Use memoryviews for efficient array access
# 5. Leverage C libraries and functions when appropriate

# Common Pitfalls:
# 1. Overusing Cython for non-performance-critical parts of the code
# 2. Neglecting to release acquired resources, leading to memory leaks
# 3. Incorrect use of nogil, potentially leading to race conditions
# 4. Forgetting to declare variables as cdef, reducing potential performance gains
# 5. Inefficient use of Python objects in tight loops

# Advanced Tips:
# 1. Use typed memoryviews for efficient array manipulation
# 2. Leverage parallel computation with prange and nogil
# 3. Use Cython's pure Python mode for easier debugging
# 4. Implement proper exception handling in Cython code
# 5. Utilize Cython's inline and cdivision directives for further optimizations

# Example: Using typed memoryviews and prange
"""
# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
from cython.parallel import prange

def parallel_sum(double[:] arr):
    cdef Py_ssize_t i
    cdef double total = 0.0
    cdef Py_ssize_t n = arr.shape[0]
    
    for i in prange(n, nogil=True):
        total += arr[i]
    
    return total
"""

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Optimizing a numerical integration function
def python_integrate(f, a: float, b: float, n: int) -> float:
    """Numerical integration using the trapezoidal rule."""
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

"""
# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
cimport cython
from libc.math cimport sin, cos, exp

ctypedef double (*func_t)(double) nogil

cdef double integrate(func_t f, double a, double b, int n) nogil:
    cdef double h = (b - a) / n
    cdef double s = 0.5 * (f(a) + f(b))
    cdef int i
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def cython_integrate(str func_name, double a, double b, int n):
    cdef func_t f
    if func_name == 'sin':
        f = sin
    elif func_name == 'cos':
        f = cos
    elif func_name == 'exp':
        f = exp
    else:
        raise ValueError("Unsupported function")
    
    return integrate(f, a, b, n)
"""

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Example: Using Cython with NumPy ufuncs
"""
# cython: language_level=3
cimport numpy as np
import numpy as np
from libc.math cimport sqrt

cdef double euclidean_distance(double x1, double y1, double x2, double y2) nogil:
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def vectorized_distance(np.ndarray[double, ndim=1] x1,
                        np.ndarray[double, ndim=1] y1,
                        np.ndarray[double, ndim=1] x2,
                        np.ndarray[double, ndim=1] y2):
    return np.frompyfunc(euclidean_distance, 4, 1)(x1, y1, x2, y2)
"""

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    """Provide answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: When should I use Cython instead of pure Python?":
        "A: Use Cython for performance-critical parts of your code, especially for CPU-bound tasks involving numerical computations or tight loops.",
        
        "Q: How do I compile Cython code?":
        "A: You can use setuptools to compile Cython code. Create a setup.py file and run 'python setup.py build_ext --inplace'.",
        
        "Q: Can I use Cython with NumPy?":
        "A: Yes, Cython has excellent support for NumPy arrays, offering significant speedups for numerical computations.",
        
        "Q: How do I debug Cython code?":
        "A: You can use Cython's pure Python mode for easier debugging, or use gdb for debugging the generated C code.",
        
        "Q: What's the difference between def, cdef, and cpdef in Cython?":
        "A: 'def' creates a Python-callable function, 'cdef' creates a C function (faster but not Python-callable), and 'cpdef' creates both (a compromise between speed and flexibility)."
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    """Provide recommended tools, libraries, and resources for Cython optimization in Python."""
    resources = {
        "Tools": [
            "Cython - The Cython compiler",
            "setuptools - For building Cython extensions",
            "pyximport - For on-the-fly Cython compilation during development",
            "Cython debugger - For debugging Cython code"
        ],
        "Libraries": [
            "NumPy - For efficient numerical computations",
            "SciPy - Scientific computing library with many Cython-optimized routines",
            "Pandas - Data manipulation library with some Cython-optimized operations",
            "Scikit-learn - Machine learning library using Cython for performance-critical parts"
        ],
        "Resources": [
            "Cython documentation: https://cython.readthedocs.io/",
            "Cython: A Guide for Python Programmers by Kurt W. Smith",
            "High Performance Python by Micha Gorelick and Ian Ozsvald (chapters on Cython)",
            "Cython tutorial on Real Python: https://realpython.com/cython-python-performance/",
            "Scipy Lecture Notes on Cython: https://scipy-lectures.org/advanced/optimizing/index.html"
        ]
    }
    
    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"- {item}")
        print()

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark(func, *args, **kwargs):
    """Benchmark a function's execution time."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
    return result

def compare_python_cython():
    """Compare Python and Cython implementations (simulated for Cython)."""
    n = 10**7
    
    print("Comparing sum calculation:")
    benchmark(python_function, n)
    # In a real scenario, you would call the Cython function here
    print("Cython version would be significantly faster")
    
    print("\nComparing prime number calculation:")
    benchmark(python_primes, 10000)
    print("Cython version would be faster, especially for larger n")
    
    print("\nComparing matrix multiplication:")
    a = np.random.rand(500, 500)
    b = np.random.rand(500, 500)
    benchmark(python_matrix_multiply, a, b)
    print("Cython version would be much faster, especially for larger matrices")

# 9. How to Contribute
# --------------------
# (The contribution guidelines would typically be placed here, but for brevity, they are omitted in this code example.)

def main():
    """Main function to demonstrate various concepts related to Cython optimization in Python."""
    print("Demonstrating Cython concepts for performance optimization in Python")
    print("\n1. Basic usage (simulated):")
    print("Python version:")
    benchmark(python_function, 10**7)
    print("Cython version would be significantly faster")
    
    print("\n2. Prime number calculation:")
    print("Python version:")
    benchmark(python_primes, 10000)
    print("Cython version would be faster, especially for larger n")
    
    print("\n3. Matrix multiplication:")
    a = np.random.rand(500, 500)
    b = np.random.rand(500, 500)
    print("Python version:")
    benchmark(python_matrix_multiply, a, b)
    print("Cython version would be much faster, especially for larger matrices")
    
    print("\n4. Numerical integration (Python version):")
    benchmark(python_integrate, np.sin, 0, np.pi, 10**6)
    print("Cython version would offer significant speedup")
    
    print("\nFAQs and Troubleshooting:")
    faqs_and_troubleshooting()
    
    print("\nRecommended Resources:")
    recommended_resources()
    
    print("\nPerformance Comparison:")
    compare_python_cython()

if __name__ == "__main__":
    main()