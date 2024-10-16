# Data Structures in Python - Arrays and NumPy basics - in the Python Programming Language
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

import numpy as np
import time
import sys
from typing import List, Any, Union

# 1. Overview and Historical Context
# ----------------------------------
# Arrays are fundamental data structures in Python, providing a way to store and manipulate
# collections of elements. While Python's built-in list type is often used as a dynamic array,
# the NumPy library offers a more efficient and feature-rich array implementation for numerical computing.

# Historical context:
# - Python lists have been part of the language since its inception in 1991.
# - NumPy was first released in 2005, evolving from earlier numerical Python libraries.
# - NumPy arrays provide a more memory-efficient and performant alternative to Python lists for numerical operations.

# Significance:
# - Arrays form the basis for many higher-level data structures and algorithms.
# - NumPy arrays are essential for scientific computing, data analysis, and machine learning in Python.
# - Understanding array operations is crucial for efficient data manipulation and computation.

# Common use cases:
# - Storing and manipulating collections of numerical data
# - Implementing mathematical and statistical operations on large datasets
# - Serving as a foundation for more complex data structures like matrices and tensors

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def create_and_manipulate_lists():
    # Python lists as dynamic arrays
    numbers = [1, 2, 3, 4, 5]
    print("Original list:", numbers)

    # Appending elements
    numbers.append(6)
    print("After appending 6:", numbers)

    # Inserting elements
    numbers.insert(0, 0)
    print("After inserting 0 at index 0:", numbers)

    # Removing elements
    numbers.remove(3)
    print("After removing 3:", numbers)

    # Slicing
    print("Slice [1:4]:", numbers[1:4])

    # List comprehension
    squares = [x**2 for x in numbers]
    print("Squares using list comprehension:", squares)

def numpy_array_basics():
    # Creating NumPy arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    print("1D NumPy array:", arr1)

    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D NumPy array:\n", arr2)

    # Array attributes
    print("Shape of arr2:", arr2.shape)
    print("Dimensions of arr2:", arr2.ndim)
    print("Data type of arr2:", arr2.dtype)

    # Array operations
    print("Element-wise addition:", arr1 + 10)
    print("Element-wise multiplication:", arr1 * 2)

    # Broadcasting
    arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Broadcasting example:\n", arr3 + np.array([10, 20, 30]))

def array_indexing_and_slicing():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print("Original array:\n", arr)

    # Indexing
    print("Element at (1, 2):", arr[1, 2])

    # Slicing
    print("First two rows, last two columns:\n", arr[:2, 2:])

    # Boolean indexing
    mask = arr > 5
    print("Elements greater than 5:\n", arr[mask])

    # Fancy indexing
    indices = np.array([0, 2])
    print("First and third rows:\n", arr[indices])

def array_operations():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])

    # Element-wise operations
    print("Element-wise addition:", arr1 + arr2)
    print("Element-wise multiplication:", arr1 * arr2)

    # Statistical operations
    print("Mean of arr1:", np.mean(arr1))
    print("Standard deviation of arr2:", np.std(arr2))

    # Linear algebra operations
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    print("Matrix multiplication:\n", np.dot(matrix1, matrix2))

def array_reshaping_and_stacking():
    arr = np.arange(12)
    print("Original array:", arr)

    # Reshaping
    reshaped = arr.reshape(3, 4)
    print("Reshaped to 3x4:\n", reshaped)

    # Flattening
    flattened = reshaped.flatten()
    print("Flattened array:", flattened)

    # Stacking
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    vertical_stack = np.vstack((arr1, arr2))
    horizontal_stack = np.hstack((arr1, arr2))
    print("Vertical stack:\n", vertical_stack)
    print("Horizontal stack:", horizontal_stack)

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------
# Best Practices:
# 1. Use NumPy arrays instead of Python lists for numerical computations.
# 2. Leverage broadcasting to simplify operations on arrays of different shapes.
# 3. Use vectorized operations instead of explicit loops for better performance.
# 4. Be mindful of memory usage when working with large arrays.

# Common Pitfalls:
# 1. Forgetting that NumPy array slices are views, not copies.
# 2. Ignoring the difference between integer division in Python 2 vs Python 3.
# 3. Not considering the performance impact of frequent array resizing.

# Advanced Tips:
# 1. Use np.einsum for efficient Einstein summation notation.
# 2. Leverage np.ufunc for creating custom universal functions.
# 3. Use np.memmap for working with arrays that don't fit in memory.

def demonstrate_advanced_concepts():
    # Demonstrating view vs copy
    arr = np.array([1, 2, 3, 4])
    view = arr[:2]
    view[0] = 10
    print("Original array after modifying view:", arr)

    # Einstein summation notation
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    result = np.einsum('ij,jk->ik', a, b)
    print("Matrix multiplication using einsum:\n", result)

    # Custom universal function
    def custom_logistic(x):
        return 1 / (1 + np.exp(-x))

    logistic_ufunc = np.frompyfunc(custom_logistic, 1, 1)
    print("Custom logistic function applied:", logistic_ufunc([-2, -1, 0, 1, 2]))

# 4. Integration and Real-World Applications
# ------------------------------------------
# Arrays and NumPy are widely used in various fields:
# 1. Data Science: For data manipulation and analysis in pandas.
# 2. Machine Learning: As input for models in scikit-learn and TensorFlow.
# 3. Image Processing: For representing and manipulating images in libraries like Pillow and OpenCV.
# 4. Scientific Computing: In simulations and numerical methods with SciPy.

def image_processing_example():
    # Simulating an image as a 2D NumPy array
    image = np.random.randint(0, 256, size=(100, 100))
    print("Original image shape:", image.shape)

    # Applying a simple filter (blur)
    kernel = np.ones((3, 3)) / 9
    blurred = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            blurred[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * kernel)

    print("Blurred image shape:", blurred.shape)
    print("Average pixel value before blurring:", np.mean(image))
    print("Average pixel value after blurring:", np.mean(blurred))

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Dask: For working with larger-than-memory arrays and parallel computing.
# 2. CuPy: GPU-accelerated NumPy-compatible array library.
# 3. Sparse arrays: For efficient storage and computation on arrays with mostly zero elements.

def demonstrate_sparse_array():
    from scipy.sparse import csr_matrix

    # Create a sparse matrix
    dense = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    sparse = csr_matrix(dense)
    print("Dense matrix:\n", dense)
    print("Sparse matrix:\n", sparse)
    print("Sparse to dense:\n", sparse.toarray())

# 6. FAQs and Troubleshooting
# ---------------------------
def faqs_and_troubleshooting():
    print("Q: What's the difference between Python lists and NumPy arrays?")
    print("A: NumPy arrays are more memory-efficient and faster for numerical operations.")

    print("\nQ: How can I create an array of random numbers?")
    print("A: Use np.random.rand() for uniform distribution or np.random.randn() for normal distribution.")

    print("\nQ: How do I find the index of the maximum value in an array?")
    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    print("Array:", arr)
    print("Index of maximum value:", np.argmax(arr))

    print("\nQ: How can I remove NaN values from an array?")
    arr_with_nan = np.array([1, 2, np.nan, 4, 5])
    print("Array with NaN:", arr_with_nan)
    print("Array without NaN:", arr_with_nan[~np.isnan(arr_with_nan)])

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - NumPy: Essential for numerical computing in Python
# - Pandas: Built on top of NumPy, great for structured data
# - Matplotlib: For visualizing array data
# - SciPy: For scientific computing and advanced array operations

# Resources:
# - "Python for Data Analysis" by Wes McKinney
# - "From Python to NumPy" by Nicolas P. Rougier
# - NumPy official documentation: https://numpy.org/doc/
# - SciPy Lecture Notes: https://scipy-lectures.org/

# 8. Performance Analysis and Optimization
# ----------------------------------------
def performance_comparison():
    size = 1000000

    # Python list
    start = time.time()
    py_list = list(range(size))
    py_list = [x**2 for x in py_list]
    py_time = time.time() - start

    # NumPy array
    start = time.time()
    np_array = np.arange(size)
    np_array = np_array**2
    np_time = time.time() - start

    print(f"Python list time: {py_time:.4f} seconds")
    print(f"NumPy array time: {np_time:.4f} seconds")
    print(f"NumPy is {py_time/np_time:.2f}x faster")

    # Memory usage
    py_mem = sys.getsizeof(py_list) / (1024 * 1024)
    np_mem = np_array.nbytes / (1024 * 1024)
    print(f"Python list memory: {py_mem:.2f} MB")
    print(f"NumPy array memory: {np_mem:.2f} MB")
    print(f"NumPy uses {py_mem/np_mem:.2f}x less memory")

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
    print("Demonstrating Python Arrays and NumPy basics")
    create_and_manipulate_lists()
    numpy_array_basics()
    array_indexing_and_slicing()
    array_operations()
    array_reshaping_and_stacking()
    demonstrate_advanced_concepts()
    image_processing_example()
    demonstrate_sparse_array()
    faqs_and_troubleshooting()
    performance_comparison()

if __name__ == "__main__":
    main()