# Performance Optimization - Profiling Python code - in the Python Programming Language
# =====================================================================================

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

import cProfile
import pstats
import io
import time
import random
import asyncio
from memory_profiler import profile
from line_profiler import LineProfiler
import timeit

# 1. Overview and Historical Context
# ----------------------------------
# Profiling is the process of analyzing a program's performance to identify bottlenecks
# and optimize code execution. It is crucial for developing efficient and scalable software.

# Historical context:
# - Profiling has been a part of software development since the early days of computing.
# - Python's cProfile module, part of the standard library, was introduced in Python 2.5 (2006).
# - Third-party profiling tools like line_profiler and memory_profiler emerged to provide more detailed insights.

# Significance:
# - Profiling helps identify performance bottlenecks in code.
# - It enables data-driven optimization decisions.
# - Profiling is essential for maintaining performance as codebases grow.

# Common use cases:
# - Optimizing time-critical applications
# - Reducing memory usage in resource-constrained environments
# - Improving scalability of web applications
# - Enhancing user experience in interactive programs

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def profile_function(func, *args, **kwargs):
    """Profile a function using cProfile."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())
    return result

def demonstrate_cprofile():
    """Demonstrate the use of cProfile."""
    print("Profiling fibonacci(30):")
    profile_function(fibonacci, 30)

@profile
def memory_intensive_function():
    """A function that consumes a significant amount of memory."""
    return [random.random() for _ in range(1000000)]

def demonstrate_memory_profiler():
    """Demonstrate the use of memory_profiler."""
    print("Profiling memory usage:")
    memory_intensive_function()

def time_consuming_function():
    """A function that takes a considerable amount of time to execute."""
    time.sleep(0.1)
    return sum(range(1000000))

def demonstrate_line_profiler():
    """Demonstrate the use of line_profiler."""
    print("Line-by-line profiling:")
    profiler = LineProfiler()
    profiler_wrapper = profiler(time_consuming_function)
    profiler_wrapper()
    profiler.print_stats()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

def optimize_fibonacci(n, memo={}):
    """An optimized version of the Fibonacci function using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = optimize_fibonacci(n-1, memo) + optimize_fibonacci(n-2, memo)
    return memo[n]

def demonstrate_optimization():
    """Demonstrate the impact of optimization."""
    print("Profiling original fibonacci(30):")
    profile_function(fibonacci, 30)
    print("\nProfiling optimized fibonacci(30):")
    profile_function(optimize_fibonacci, 30)

def common_pitfalls():
    """Demonstrate common profiling pitfalls."""
    # Pitfall 1: Profiling small functions
    def small_function():
        return 1 + 1

    print("Profiling a small function (may produce unreliable results):")
    profile_function(small_function)

    # Pitfall 2: Not considering the overhead of profiling
    def overhead_sensitive_function():
        for _ in range(1000000):
            pass

    print("\nProfiling a function sensitive to profiling overhead:")
    profile_function(overhead_sensitive_function)

# 4. Integration and Real-World Applications
# ------------------------------------------

class DataProcessor:
    def __init__(self, data_size):
        self.data = [random.random() for _ in range(data_size)]

    def process_data(self):
        return sorted(self.data)

    def analyze_data(self):
        return sum(self.data) / len(self.data)

def real_world_profiling_example():
    """Demonstrate profiling in a more realistic scenario."""
    processor = DataProcessor(1000000)
    
    print("Profiling data processing:")
    profile_function(processor.process_data)
    
    print("\nProfiling data analysis:")
    profile_function(processor.analyze_data)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_function():
    await asyncio.sleep(0.1)
    return sum(range(1000000))

async def profile_async_function():
    """Profile an asynchronous function."""
    print("Profiling asynchronous function:")
    profiler = cProfile.Profile()
    profiler.enable()
    result = await async_function()
    profiler.disable()
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())
    return result

def demonstrate_async_profiling():
    """Demonstrate profiling of asynchronous code."""
    asyncio.run(profile_async_function())

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    # Q: How to profile memory usage over time?
    # A: Use the memory_profiler's mprof command-line tool

    # Q: How to reduce the overhead of profiling?
    # A: Use sampling profilers or profile specific parts of the code

    # Q: How to profile multi-threaded applications?
    # A: Use thread-aware profilers like cProfile with threading support

    pass

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - cProfile: Built-in profiling module
# - line_profiler: Line-by-line profiling
# - memory_profiler: Memory usage profiling
# - pyinstrument: Low-overhead profiler
# - Scalene: High-performance CPU and memory profiler

# Resources:
# - Python's official profilers documentation: https://docs.python.org/3/library/profile.html
# - "High Performance Python" by Micha Gorelick and Ian Ozsvald
# - Real Python's guide on profiling: https://realpython.com/python-profiling/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_profiling_overhead():
    """Benchmark the overhead of different profiling methods."""
    def function_to_profile():
        return sum(range(10000))

    # No profiling
    start_time = time.time()
    for _ in range(1000):
        function_to_profile()
    no_profile_time = time.time() - start_time

    # cProfile
    profiler = cProfile.Profile()
    start_time = time.time()
    for _ in range(1000):
        profiler.runcall(function_to_profile)
    cprofile_time = time.time() - start_time

    # line_profiler
    lp = LineProfiler()
    lp_wrapper = lp(function_to_profile)
    start_time = time.time()
    for _ in range(1000):
        lp_wrapper()
    line_profile_time = time.time() - start_time

    print(f"No profiling: {no_profile_time:.4f} seconds")
    print(f"cProfile: {cprofile_time:.4f} seconds")
    print(f"line_profiler: {line_profile_time:.4f} seconds")

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
    print("1. Demonstrating cProfile:")
    demonstrate_cprofile()

    print("\n2. Demonstrating memory_profiler:")
    demonstrate_memory_profiler()

    print("\n3. Demonstrating line_profiler:")
    demonstrate_line_profiler()

    print("\n4. Demonstrating optimization impact:")
    demonstrate_optimization()

    print("\n5. Demonstrating common pitfalls:")
    common_pitfalls()

    print("\n6. Real-world profiling example:")
    real_world_profiling_example()

    print("\n7. Demonstrating async profiling:")
    demonstrate_async_profiling()

    print("\n8. FAQ and troubleshooting:")
    faq_and_troubleshooting()

    print("\n9. Benchmarking profiling overhead:")
    benchmark_profiling_overhead()

if __name__ == "__main__":
    main()