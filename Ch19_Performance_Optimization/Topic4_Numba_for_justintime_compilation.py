# Performance Optimization - Numba for just-in-time compilation - in the Python Programming Language
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

import time
import numpy as np
from numba import jit, njit, vectorize, prange
from numba import float64, int64
from typing import List, Tuple

# 1. Overview and Historical Context
# ----------------------------------
# Numba is a just-in-time (JIT) compiler for Python that is specifically designed to compile
# numerical Python code. It allows Python functions to be compiled to native machine code at runtime,
# resulting in significant performance improvements for numerical and scientific computing tasks.

# Historical context:
# - Numba was first released in 2012 by Continuum Analytics (now Anaconda, Inc.)
# - It was developed to address the performance gap between Python and lower-level languages like C/C++
# - Numba has evolved to support a wide range of Python and NumPy features, as well as CUDA GPU acceleration

# Significance:
# - Enables near-C-speed performance for Python code without requiring users to write C extensions
# - Provides easy-to-use decorators for JIT compilation, making optimization accessible to Python developers
# - Supports both CPU and GPU acceleration, allowing for scalable performance improvements
# - Integrates well with the scientific Python ecosystem, particularly NumPy

# Common use cases:
# - Accelerating numerical algorithms and scientific simulations
# - Optimizing data processing pipelines in data science and machine learning workflows
# - Speeding up computationally intensive tasks in finance, physics, and other scientific domains

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Example 1: Basic Numba usage with @jit decorator
@jit(nopython=True)
def sum_of_squares(n: int) -> int:
    """Calculate the sum of squares from 0 to n-1 using Numba."""
    result = 0
    for i in range(n):
        result += i * i
    return result

# Python equivalent for comparison
def sum_of_squares_python(n: int) -> int:
    """Calculate the sum of squares from 0 to n-1 using pure Python."""
    return sum(i * i for i in range(n))

# Example 2: Using Numba with NumPy arrays
@njit
def numba_mean(arr: np.ndarray) -> float:
    """Calculate the mean of a NumPy array using Numba."""
    sum = 0.0
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)

# NumPy equivalent for comparison
def numpy_mean(arr: np.ndarray) -> float:
    """Calculate the mean of a NumPy array using NumPy."""
    return np.mean(arr)

# Example 3: Vectorization with Numba
@vectorize([float64(float64, float64)])
def numba_add(a: float, b: float) -> float:
    """Add two numbers using Numba vectorization."""
    return a + b

# Example 4: Parallel processing with Numba
@njit(parallel=True)
def parallel_sum_of_squares(n: int) -> int:
    """Calculate the sum of squares from 0 to n-1 using parallel processing."""
    result = 0
    for i in prange(n):
        result += i * i
    return result

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use the nopython=True option with @jit to ensure maximum performance
# 2. Prefer NumPy arrays over Python lists for numerical computations
# 3. Utilize Numba's parallel processing capabilities for suitable tasks
# 4. Profile your code to identify performance bottlenecks before applying Numba
# 5. Use static typing hints to help Numba generate more efficient code

# Common Pitfalls:
# 1. Trying to JIT-compile functions that use unsupported Python features
# 2. Neglecting to handle errors that may occur during compilation
# 3. Overusing Numba for non-performance-critical parts of the code
# 4. Assuming Numba will always provide significant speedups without proper profiling
# 5. Forgetting to warm up JIT-compiled functions before benchmarking

# Advanced Tips:
# 1. Use Numba's inspection tools to understand the compiled code
# 2. Leverage Numba's support for custom data types and structures
# 3. Utilize Numba's GPU acceleration capabilities for suitable algorithms
# 4. Combine Numba with other optimization techniques like vectorization and parallelization
# 5. Implement proper exception handling in Numba-compiled functions

# Example: Custom data type with Numba
from numba import types
from numba.experimental import jitclass

spec = [
    ('x', float64),
    ('y', float64)
]

@jitclass(spec)
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def distance(self, other: 'Point') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return np.sqrt(dx**2 + dy**2)

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Monte Carlo simulation for option pricing
@njit
def monte_carlo_option_pricing(S: float, K: float, T: float, r: float, sigma: float, num_simulations: int) -> float:
    """
    Price a European call option using Monte Carlo simulation.
    
    Parameters:
    S: Initial stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility of the underlying asset
    num_simulations: Number of Monte Carlo simulations
    
    Returns:
    Estimated option price
    """
    dt = T / 252  # Assuming 252 trading days in a year
    nudt = (r - 0.5 * sigma**2) * dt
    sidt = sigma * np.sqrt(dt)
    
    total_payoff = 0.0
    for _ in range(num_simulations):
        path = S * np.exp(np.cumsum(nudt + sidt * np.random.normal(0, 1, 252)))
        payoff = max(path[-1] - K, 0)
        total_payoff += payoff
    
    option_price = np.exp(-r * T) * (total_payoff / num_simulations)
    return option_price

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Example: Using Numba with CUDA for GPU acceleration
from numba import cuda

@cuda.jit
def cuda_sum_of_squares(n: int, result: np.ndarray):
    """Calculate the sum of squares from 0 to n-1 using CUDA."""
    i = cuda.grid(1)
    if i < n:
        cuda.atomic.add(result, 0, i * i)

def gpu_sum_of_squares(n: int) -> int:
    """Wrapper function to call the CUDA kernel."""
    result = np.zeros(1, dtype=np.int64)
    threads_per_block = 256
    blocks = (n + threads_per_block - 1) // threads_per_block
    cuda_sum_of_squares[blocks, threads_per_block](n, result)
    return result[0]

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    """Provide answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: When should I use Numba instead of pure Python or NumPy?":
        "A: Use Numba for computationally intensive tasks, especially those involving numerical calculations or loops that can't be easily vectorized with NumPy.",
        
        "Q: How do I know if Numba is actually improving my code's performance?":
        "A: Profile your code before and after applying Numba. Use the `timeit` module or more advanced profiling tools to measure execution time.",
        
        "Q: Can Numba work with all Python code?":
        "A: No, Numba works best with numerical computations and has limited support for Python's dynamic features. It works well with NumPy arrays and basic Python data types.",
        
        "Q: How do I debug Numba-compiled code?":
        "A: You can use print statements inside Numba functions for basic debugging. For more complex issues, you may need to use Numba's debugging options or fall back to pure Python code.",
        
        "Q: Can Numba be used with multiprocessing or multithreading?":
        "A: Yes, Numba provides parallelization features through the `parallel=True` option and the `prange` function. It can also be used with Python's multiprocessing module."
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    """Provide recommended tools, libraries, and resources for Numba optimization in Python."""
    resources = {
        "Tools": [
            "Numba - The core library for JIT compilation",
            "conda - Recommended package manager for installing Numba and its dependencies",
            "CUDA Toolkit - For GPU acceleration with Numba",
            "Python profilers (cProfile, line_profiler) - For identifying performance bottlenecks"
        ],
        "Libraries": [
            "NumPy - Essential for numerical computing, works well with Numba",
            "CuPy - GPU-accelerated array library compatible with NumPy",
            "Dask - For distributed computing, can be used with Numba for large-scale computations",
            "Matplotlib - For visualizing results of Numba-optimized computations"
        ],
        "Resources": [
            "Numba documentation: https://numba.pydata.org/numba-doc/latest/index.html",
            "High Performance Python by Micha Gorelick and Ian Ozsvald (chapters on Numba)",
            "Numba tutorials on Real Python: https://realpython.com/numba-python/",
            "Continuum Analytics blog posts on Numba: https://www.anaconda.com/blog/tag/numba",
            "Numba GitHub repository: https://github.com/numba/numba"
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

def compare_performance():
    """Compare performance of Python, NumPy, and Numba implementations."""
    n = 10**7
    arr = np.random.rand(n)
    
    print("Comparing sum of squares calculation:")
    benchmark(sum_of_squares_python, n)
    benchmark(sum_of_squares, n)
    benchmark(parallel_sum_of_squares, n)
    
    print("\nComparing mean calculation:")
    benchmark(numpy_mean, arr)
    benchmark(numba_mean, arr)
    
    print("\nComparing vectorized addition:")
    a = np.random.rand(n)
    b = np.random.rand(n)
    benchmark(np.add, a, b)
    benchmark(numba_add, a, b)
    
    print("\nComparing Monte Carlo option pricing:")
    benchmark(monte_carlo_option_pricing, 100, 100, 1, 0.05, 0.2, 10000)
    
    if cuda.is_available():
        print("\nComparing GPU-accelerated sum of squares:")
        benchmark(sum_of_squares, n)
        benchmark(gpu_sum_of_squares, n)

# 9. How to Contribute
# --------------------
# (The contribution guidelines would typically be placed here, but for brevity, they are omitted in this code example.)

def main():
    """Main function to demonstrate various concepts related to Numba optimization in Python."""
    print("Demonstrating Numba concepts for performance optimization in Python")
    
    print("\n1. Basic usage:")
    n = 10**7
    result_python = benchmark(sum_of_squares_python, n)
    result_numba = benchmark(sum_of_squares, n)
    assert result_python == result_numba, "Results don't match!"
    
    print("\n2. NumPy array operations:")
    arr = np.random.rand(n)
    result_numpy = benchmark(numpy_mean, arr)
    result_numba = benchmark(numba_mean, arr)
    np.testing.assert_almost_equal(result_numpy, result_numba, decimal=5)
    
    print("\n3. Vectorization:")
    a = np.random.rand(n)
    b = np.random.rand(n)
    result_numpy = benchmark(np.add, a, b)
    result_numba = benchmark(numba_add, a, b)
    np.testing.assert_almost_equal(result_numpy, result_numba)
    
    print("\n4. Parallel processing:")
    result_serial = benchmark(sum_of_squares, n)
    result_parallel = benchmark(parallel_sum_of_squares, n)
    assert result_serial == result_parallel, "Results don't match!"
    
    print("\n5. Real-world application (Monte Carlo option pricing):")
    option_price = benchmark(monte_carlo_option_pricing, 100, 100, 1, 0.05, 0.2, 10000)
    print(f"Estimated option price: {option_price:.4f}")
    
    if cuda.is_available():
        print("\n6. GPU acceleration:")
        result_cpu = benchmark(sum_of_squares, n)
        result_gpu = benchmark(gpu_sum_of_squares, n)
        assert result_cpu == result_gpu, "Results don't match!"
    else:
        print("\n6. GPU acceleration: CUDA not available on this system")
    
    print("\nFAQs and Troubleshooting:")
    faqs_and_troubleshooting()
    
    print("\nRecommended Resources:")
    recommended_resources()
    
    print("\nPerformance Comparison:")
    compare_performance()

if __name__ == "__main__":
    main()