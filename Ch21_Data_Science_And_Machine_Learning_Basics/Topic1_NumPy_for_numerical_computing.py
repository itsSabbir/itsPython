# Data Science and Machine Learning Basics - NumPy for numerical computing - in the Python Programming Language
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

import numpy as np
import time
import matplotlib.pyplot as plt
from typing import List, Tuple, Union
import unittest

# 1. Overview and Historical Context
# ----------------------------------
# NumPy (Numerical Python) is a fundamental library for scientific computing in Python.
# It provides support for large, multi-dimensional arrays and matrices, along with a
# collection of mathematical functions to operate on these arrays efficiently.

# Historical context:
# - NumPy was created by Travis Oliphant in 2005, building on the earlier Numeric library.
# - It evolved from the need for efficient numerical computations in Python, which was
#   lacking in the standard library.
# - NumPy 1.0 was released in 2006, marking a significant milestone in Python's scientific ecosystem.

# Significance:
# - NumPy provides a powerful N-dimensional array object, making it the foundation for
#   many scientific and machine learning libraries in Python.
# - It offers vectorized operations, which are much faster than equivalent Python loops.
# - NumPy's broadcasting feature allows operations on arrays of different shapes.

# Common use cases:
# - Scientific computing and data analysis
# - Image and signal processing
# - Linear algebra operations
# - Machine learning model implementation
# - Numerical simulations

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def numpy_basics():
    """Demonstrate basic NumPy operations and array creation."""
    # Creating arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.zeros((3, 3))
    c = np.ones((2, 2))
    d = np.eye(3)
    e = np.arange(10)
    f = np.linspace(0, 1, 5)
    
    print("Basic arrays:")
    print(f"a: {a}")
    print(f"b:\n{b}")
    print(f"c:\n{c}")
    print(f"d:\n{d}")
    print(f"e: {e}")
    print(f"f: {f}")
    
    # Array operations
    g = a + 2
    h = a * 2
    i = np.sin(a)
    j = np.exp(a)
    
    print("\nArray operations:")
    print(f"g (a + 2): {g}")
    print(f"h (a * 2): {h}")
    print(f"i (sin(a)): {i}")
    print(f"j (exp(a)): {j}")
    
    # Array indexing and slicing
    k = a[1:4]
    l = b[0, :]
    m = c[:, 1]
    
    print("\nArray indexing and slicing:")
    print(f"k (a[1:4]): {k}")
    print(f"l (b[0, :]): {l}")
    print(f"m (c[:, 1]): {m}")

def numpy_advanced():
    """Demonstrate advanced NumPy operations."""
    # Reshaping arrays
    a = np.arange(12).reshape(3, 4)
    print("Reshaped array:")
    print(a)
    
    # Broadcasting
    b = np.array([1, 2, 3, 4])
    c = a + b
    print("\nBroadcasting result:")
    print(c)
    
    # Linear algebra operations
    d = np.array([[1, 2], [3, 4]])
    e = np.linalg.inv(d)
    f = np.dot(d, e)
    print("\nLinear algebra:")
    print(f"Original matrix:\n{d}")
    print(f"Inverse matrix:\n{e}")
    print(f"Identity (dot product):\n{f}")
    
    # Random number generation
    g = np.random.rand(3, 3)
    h = np.random.normal(0, 1, (3, 3))
    print("\nRandom arrays:")
    print(f"Uniform distribution:\n{g}")
    print(f"Normal distribution:\n{h}")

def numpy_vectorization(x: np.ndarray) -> np.ndarray:
    """
    Demonstrate NumPy vectorization vs Python loops.
    
    Args:
        x (np.ndarray): Input array
    
    Returns:
        np.ndarray: Processed array
    """
    def python_loop(x):
        result = np.zeros_like(x)
        for i in range(len(x)):
            result[i] = np.sin(x[i]) ** 2 + np.cos(x[i]) ** 2
        return result
    
    def numpy_vectorized(x):
        return np.sin(x) ** 2 + np.cos(x) ** 2
    
    start_time = time.time()
    result_loop = python_loop(x)
    loop_time = time.time() - start_time
    
    start_time = time.time()
    result_vectorized = numpy_vectorized(x)
    vectorized_time = time.time() - start_time
    
    print(f"Python loop time: {loop_time:.6f} seconds")
    print(f"NumPy vectorized time: {vectorized_time:.6f} seconds")
    print(f"Speedup: {loop_time / vectorized_time:.2f}x")
    
    return result_vectorized

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use vectorized operations whenever possible for better performance.
# 2. Avoid unnecessary copies of large arrays to save memory.
# 3. Use appropriate dtypes to optimize memory usage and performance.
# 4. Leverage broadcasting for efficient operations on arrays of different shapes.
# 5. Use NumPy's built-in functions instead of writing your own implementations.

# Common Pitfalls:
# 1. Mixing 1D and 2D arrays unintentionally, leading to broadcasting errors.
# 2. Forgetting that NumPy operations return new arrays, not modifying in-place.
# 3. Using Python loops instead of vectorized operations, resulting in poor performance.
# 4. Ignoring the differences between views and copies of arrays.
# 5. Not handling potential overflow or underflow in numerical computations.

def demonstrate_best_practices():
    """Demonstrate NumPy best practices and common pitfalls."""
    # Best practice: Use appropriate dtypes
    a = np.array([1, 2, 3], dtype=np.int8)
    print(f"Array with int8 dtype: {a}")
    print(f"Memory usage: {a.nbytes} bytes")
    
    # Common pitfall: Mixing 1D and 2D arrays
    b = np.array([1, 2, 3])
    c = np.array([[1, 2, 3]])
    try:
        result = b + c
    except ValueError as e:
        print(f"Error when adding 1D and 2D arrays: {e}")
    
    # Best practice: Use broadcasting
    d = np.array([[1, 2, 3], [4, 5, 6]])
    e = np.array([1, 2, 3])
    result = d + e
    print(f"\nBroadcasting result:\n{result}")
    
    # Common pitfall: Forgetting that operations return new arrays
    f = np.array([1, 2, 3])
    g = f
    f += 1
    print(f"\nOriginal array: {f}")
    print(f"Reference to original array: {g}")
    
    # Best practice: Use NumPy's built-in functions
    h = np.array([1, 2, 3, 4, 5])
    mean = np.mean(h)
    std = np.std(h)
    print(f"\nMean: {mean}, Standard deviation: {std}")

# Advanced Tips:
def advanced_numpy_tips():
    """Demonstrate advanced NumPy tips and techniques."""
    # 1. Using np.einsum for efficient tensor operations
    a = np.random.rand(3, 4, 5)
    b = np.random.rand(4, 5, 6)
    c = np.einsum('ijk,jkl->il', a, b)
    print("Einsum result shape:", c.shape)
    
    # 2. Memory-efficient operations with np.memmap
    filename = 'memmapped_array.dat'
    memmapped_array = np.memmap(filename, dtype='float64', mode='w+', shape=(1000, 1000))
    memmapped_array[:] = np.random.random((1000, 1000))
    print("Memmapped array shape:", memmapped_array.shape)
    
    # 3. Structured arrays for heterogeneous data
    dtype = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
    structured_array = np.array([('Alice', 25, 55.0), ('Bob', 30, 70.5), ('Charlie', 35, 65.2)], dtype=dtype)
    print("\nStructured array:")
    print(structured_array)
    
    # 4. Using np.ufunc for custom vectorized operations
    def custom_operation(x, y):
        return x * y + np.sin(x)
    
    vectorized_op = np.frompyfunc(custom_operation, 2, 1)
    result = vectorized_op(np.array([1, 2, 3]), np.array([4, 5, 6]))
    print("\nCustom ufunc result:", result)

# 4. Integration and Real-World Applications
# ------------------------------------------

def image_processing_example():
    """Demonstrate NumPy in image processing."""
    # Create a simple image (grayscale)
    image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    
    # Apply a blur filter
    kernel = np.ones((5, 5)) / 25  # 5x5 averaging filter
    blurred = np.zeros_like(image)
    for i in range(2, image.shape[0] - 2):
        for j in range(2, image.shape[1] - 2):
            blurred[i, j] = np.sum(image[i-2:i+3, j-2:j+3] * kernel)
    
    # Plot the original and blurred images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(image, cmap='gray')
    ax1.set_title('Original Image')
    ax2.imshow(blurred, cmap='gray')
    ax2.set_title('Blurred Image')
    plt.show()

def machine_learning_example():
    """Demonstrate NumPy in a simple machine learning task."""
    # Generate synthetic data
    np.random.seed(0)
    X = np.random.rand(100, 1)
    y = 2 * X + 1 + np.random.randn(100, 1) * 0.1
    
    # Implement linear regression
    X_b = np.c_[np.ones((100, 1)), X]  # Add bias term
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    # Make predictions
    X_new = np.array([[0], [1]])
    X_new_b = np.c_[np.ones((2, 1)), X_new]
    y_predict = X_new_b.dot(theta)
    
    # Plot results
    plt.scatter(X, y)
    plt.plot(X_new, y_predict, 'r-')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression with NumPy')
    plt.show()
    
    print(f"Estimated parameters: intercept = {theta[0][0]:.2f}, slope = {theta[1][0]:.2f}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def demonstrate_advanced_concepts():
    """Demonstrate advanced NumPy concepts and emerging trends."""
    # 1. Masked arrays
    data = np.array([1, 2, -999, 4, 5])
    masked_data = np.ma.masked_values(data, -999)
    print("Masked array:", masked_data)
    print("Mean of masked array:", np.ma.mean(masked_data))
    
    # 2. Structured arrays with datetime support
    dates = np.array(['2021-01-01', '2021-01-02', '2021-01-03'], dtype='datetime64')
    values = np.random.rand(3)
    structured_data = np.zeros(3, dtype=[('date', 'datetime64[D]'), ('value', 'f8')])
    structured_data['date'] = dates
    structured_data['value'] = values
    print("\nStructured array with datetime:", structured_data)
    
    # 3. GPU acceleration with CuPy (simulated)
    print("\nGPU acceleration (simulated):")
    cpu_array = np.random.rand(1000000)
    start_time = time.time()
    cpu_result = np.sum(np.exp(cpu_array))
    cpu_time = time.time() - start_time
    print(f"CPU time: {cpu_time:.6f} seconds")
    
    # Simulate GPU acceleration (actually just using NumPy)
    start_time = time.time()
    gpu_result = np.sum(np.exp(cpu_array))
    gpu_time = time.time() - start_time
    print(f"GPU time (simulated): {gpu_time:.6f} seconds")
    print(f"Speedup: {cpu_time / gpu_time:.2f}x")

# 6. FAQs and Troubleshooting
# ---------------------------

def numpy_faqs():
    """Address common NumPy FAQs and provide troubleshooting tips."""
    print("NumPy FAQs and Troubleshooting:")
    
    # Q: How do I create an array of evenly spaced numbers?
    print("\nQ: How do I create an array of evenly spaced numbers?")
    print("A: Use np.linspace() or np.arange():")
    print(np.linspace(0, 1, 5))
    print(np.arange(0, 1, 0.25))
    
    # Q: How do I reshape an array?
    print("\nQ: How do I reshape an array?")
    print("A: Use the reshape() method or np.reshape():")
    a = np.arange(12)
    print(a.reshape(3, 4))
    print(np.reshape(a, (4, 3)))
                         
    # Q: How do I handle NaN values in NumPy arrays?
    print("\nQ: How do I handle NaN values in NumPy arrays?")
    print("A: Use np.isnan(), np.nanmean(), np.nansum(), etc.:")
    b = np.array([1, 2, np.nan, 4, 5])
    print(f"Array with NaN: {b}")
    print(f"Sum ignoring NaN: {np.nansum(b)}")
    print(f"Mean ignoring NaN: {np.nanmean(b)}")
    
    # Q: How do I save and load NumPy arrays?
    print("\nQ: How do I save and load NumPy arrays?")
    print("A: Use np.save() and np.load():")
    c = np.array([1, 2, 3, 4, 5])
    np.save('array.npy', c)
    loaded_array = np.load('array.npy')
    print(f"Loaded array: {loaded_array}")

def numpy_troubleshooting():
    """Provide troubleshooting tips for common NumPy issues."""
    print("NumPy Troubleshooting Tips:")
    
    # Issue: Broadcasting errors
    print("\nIssue: Broadcasting errors")
    print("Tip: Ensure array shapes are compatible for broadcasting:")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([1, 2])
    try:
        result = a + b
    except ValueError as e:
        print(f"Error: {e}")
        print("Solution: Reshape b to (2, 1) for proper broadcasting")
        result = a + b.reshape(2, 1)
        print(f"Result:\n{result}")
    
    # Issue: Memory errors with large arrays
    print("\nIssue: Memory errors with large arrays")
    print("Tip: Use appropriate dtypes and consider using np.memmap for very large arrays")
    print("Example:")
    small_dtype_array = np.arange(1000000, dtype=np.int8)
    large_dtype_array = np.arange(1000000, dtype=np.int64)
    print(f"Memory usage (int8): {small_dtype_array.nbytes} bytes")
    print(f"Memory usage (int64): {large_dtype_array.nbytes} bytes")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def numpy_resources():
    """Provide recommended tools, libraries, and resources for NumPy."""
    print("Recommended Tools, Libraries, and Resources for NumPy:")
    
    print("\nTools and Libraries:")
    print("1. Matplotlib: For visualizing NumPy arrays and data")
    print("2. Pandas: For working with structured data alongside NumPy")
    print("3. SciPy: For advanced scientific computing capabilities")
    print("4. Numba: For just-in-time compilation of NumPy operations")
    print("5. CuPy: For GPU acceleration of NumPy-like operations")
    
    print("\nResources:")
    print("1. NumPy Official Documentation: https://numpy.org/doc/")
    print("2. 'Python for Data Analysis' by Wes McKinney")
    print("3. 'From Python to NumPy' by Nicolas P. Rougier")
    print("4. NumPy GitHub Repository: https://github.com/numpy/numpy")
    print("5. NumPy Tutorials: https://numpy.org/numpy-tutorials/")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_numpy_operations(n: int = 1000000):
    """
    Benchmark various NumPy operations and compare with pure Python.
    
    Args:
        n (int): Size of the arrays to use in benchmarking.
    """
    print(f"Benchmarking NumPy operations with array size {n}:")
    
    # Generate data
    np_array = np.random.rand(n)
    py_list = np_array.tolist()
    
    # Benchmark sum operation
    start_time = time.time()
    np_sum = np.sum(np_array)
    np_time = time.time() - start_time
    
    start_time = time.time()
    py_sum = sum(py_list)
    py_time = time.time() - start_time
    
    print(f"\nSum operation:")
    print(f"NumPy time: {np_time:.6f} seconds")
    print(f"Python time: {py_time:.6f} seconds")
    print(f"Speedup: {py_time / np_time:.2f}x")
    
    # Benchmark element-wise operations
    start_time = time.time()
    np_result = np.exp(np_array) + np.sqrt(np_array)
    np_time = time.time() - start_time
    
    start_time = time.time()
    py_result = [math.exp(x) + math.sqrt(x) for x in py_list]
    py_time = time.time() - start_time
    
    print(f"\nElement-wise operations (exp + sqrt):")
    print(f"NumPy time: {np_time:.6f} seconds")
    print(f"Python time: {py_time:.6f} seconds")
    print(f"Speedup: {py_time / np_time:.2f}x")

def optimize_numpy_code():
    """Demonstrate optimization techniques for NumPy code."""
    print("NumPy Code Optimization Techniques:")
    
    # 1. Use vectorized operations
    print("\n1. Use vectorized operations:")
    x = np.random.rand(1000000)
    
    def slow_function(x):
        result = np.zeros_like(x)
        for i in range(len(x)):
            result[i] = np.sin(x[i]) + np.cos(x[i])
        return result
    
    def fast_function(x):
        return np.sin(x) + np.cos(x)
    
    start_time = time.time()
    slow_result = slow_function(x)
    slow_time = time.time() - start_time
    
    start_time = time.time()
    fast_result = fast_function(x)
    fast_time = time.time() - start_time
    
    print(f"Slow function time: {slow_time:.6f} seconds")
    print(f"Fast function time: {fast_time:.6f} seconds")
    print(f"Speedup: {slow_time / fast_time:.2f}x")
    
    # 2. Use appropriate dtypes
    print("\n2. Use appropriate dtypes:")
    large_dtype = np.arange(1000000, dtype=np.float64)
    small_dtype = np.arange(1000000, dtype=np.int32)
    print(f"Memory usage (float64): {large_dtype.nbytes} bytes")
    print(f"Memory usage (int32): {small_dtype.nbytes} bytes")
    
    # 3. Avoid unnecessary copies
    print("\n3. Avoid unnecessary copies:")
    def inefficient_function(x):
        y = x.copy()
        return y + 1
    
    def efficient_function(x):
        return x + 1
    
    x = np.random.rand(1000000)
    
    start_time = time.time()
    inefficient_result = inefficient_function(x)
    inefficient_time = time.time() - start_time
    
    start_time = time.time()
    efficient_result = efficient_function(x)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient function time: {inefficient_time:.6f} seconds")
    print(f"Efficient function time: {efficient_time:.6f} seconds")
    print(f"Speedup: {inefficient_time / efficient_time:.2f}x")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    """Provide guidelines for contributing to this note sheet."""
    print("How to Contribute to this NumPy Note Sheet:")
    print("1. Fork the repository containing this file.")
    print("2. Make your changes or additions.")
    print("3. Ensure all code examples are correct and follow the established style.")
    print("4. Add comments explaining new concepts or functions.")
    print("5. Update the Table of Contents if necessary.")
    print("6. Submit a pull request with a clear description of your changes.")
    
    print("\nGuidelines for contributions:")
    print("- Maintain the current format and style.")
    print("- Provide working code examples for new concepts.")
    print("- Include performance considerations for new functions.")
    print("- Add relevant references or citations for advanced topics.")
    
    print("\nWhen adding new sections or expanding existing ones, consider the following:")
    print("- Relevance to the main topic of NumPy in data science and machine learning.")
    print("- Clarity and depth of explanations.")
    print("- Practical applicability of examples and tips.")
    print("- Up-to-date information on NumPy features and best practices.")

# Main function to demonstrate various concepts
def main():
    """
    Main function to demonstrate various concepts related to NumPy.
    """
    print("NumPy for Numerical Computing in Python")
    print("=======================================")
    
    numpy_basics()
    numpy_advanced()
    
    x = np.linspace(0, 10, 1000000)
    numpy_vectorization(x)
    
    demonstrate_best_practices()
    advanced_numpy_tips()
    
    image_processing_example()
    machine_learning_example()
    
    demonstrate_advanced_concepts()
    
    numpy_faqs()
    numpy_troubleshooting()
    
    numpy_resources()
    
    benchmark_numpy_operations()
    optimize_numpy_code()
    
    how_to_contribute()

# Unit tests for NumPy functions
class TestNumPyFunctions(unittest.TestCase):
    def test_numpy_basics(self):
        a = np.array([1, 2, 3, 4, 5])
        self.assertEqual(a.shape, (5,))
        self.assertEqual(a.dtype, np.int64)
    
    def test_numpy_advanced(self):
        a = np.arange(12).reshape(3, 4)
        self.assertEqual(a.shape, (3, 4))
        self.assertEqual(np.sum(a), 66)
    
    def test_numpy_vectorization(self):
        x = np.linspace(0, 1, 100)
        result = numpy_vectorization(x)
        self.assertEqual(result.shape, (100,))
        self.assertTrue(np.allclose(result, 1.0))

if __name__ == "__main__":
    main()
    unittest.main(argv=[''], exit=False)