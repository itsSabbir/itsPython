"""
Expert-Level Cheat Sheet: Operators and Expressions - Arithmetic operators - in the Python Programming Language

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

This cheat sheet serves as a comprehensive guide to arithmetic operators in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Python Experts
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import math
import operator
import timeit
from decimal import Decimal
from fractions import Fraction
import unittest
from typing import Union, List, Tuple

# 1. Overview and Historical Context
"""
Arithmetic operators in Python are fundamental tools for performing mathematical operations.
They are essential for numerical computations, data analysis, and algorithm implementation.

Historical Context:
- Python's arithmetic operators have been part of the language since its inception in 1991.
- The '//' operator for floor division was introduced in Python 2.2 (2001) to address
  the ambiguity of the '/' operator between float and integer division.
- Python 3.0 (2008) changed the behavior of '/' to always perform float division,
  while '//' retained the floor division functionality.

In modern software development, arithmetic operators are crucial for:
- Scientific computing and data analysis
- Financial calculations and modeling
- Game development and physics simulations
- Algorithm implementation and optimization

Compared to other languages:
- Python's arithmetic operators are similar to those in languages like C and Java.
- Python provides the '//' operator for floor division, which is not common in many other languages.
- Python supports operator overloading, allowing custom objects to define their own arithmetic behavior.
"""

# 2. Syntax, Key Concepts, and Code Examples

def basic_arithmetic():
    """Demonstrates basic arithmetic operations in Python."""
    a, b = 10, 3
    
    # Addition
    sum_result = a + b
    print(f"Addition: {a} + {b} = {sum_result}")
    
    # Subtraction
    difference = a - b
    print(f"Subtraction: {a} - {b} = {difference}")
    
    # Multiplication
    product = a * b
    print(f"Multiplication: {a} * {b} = {product}")
    
    # Division (float)
    quotient = a / b
    print(f"Division (float): {a} / {b} = {quotient}")
    
    # Floor Division
    floor_quotient = a // b
    print(f"Floor Division: {a} // {b} = {floor_quotient}")
    
    # Modulus (remainder)
    remainder = a % b
    print(f"Modulus: {a} % {b} = {remainder}")
    
    # Exponentiation
    power = a ** b
    print(f"Exponentiation: {a} ** {b} = {power}")

def advanced_arithmetic():
    """Demonstrates more advanced arithmetic operations and concepts."""
    # Integer division vs float division
    print(f"Integer division: 5 // 2 = {5 // 2}")
    print(f"Float division: 5 / 2 = {5 / 2}")
    
    # Modulo with negative numbers
    print(f"Modulo with negative numbers: -5 % 3 = {-5 % 3}")
    
    # Exponentiation with negative and fractional exponents
    print(f"Negative exponent: 2 ** -3 = {2 ** -3}")
    print(f"Fractional exponent: 8 ** (1/3) = {8 ** (1/3)}")
    
    # Operator precedence
    result = 2 + 3 * 4 ** 2 - 6 / 2
    print(f"2 + 3 * 4 ** 2 - 6 / 2 = {result}")
    
    # Using parentheses to change precedence
    result_with_parentheses = ((2 + 3) * 4 ** 2 - 6) / 2
    print(f"((2 + 3) * 4 ** 2 - 6) / 2 = {result_with_parentheses}")

def arithmetic_with_different_types():
    """Demonstrates arithmetic operations with different numeric types."""
    # Integer and float
    int_float_sum = 5 + 3.14
    print(f"Integer + Float: 5 + 3.14 = {int_float_sum}")
    
    # Complex numbers
    complex_sum = (1 + 2j) + (3 + 4j)
    print(f"Complex addition: (1 + 2j) + (3 + 4j) = {complex_sum}")
    
    # Decimal for precise decimal arithmetic
    from decimal import Decimal
    decimal_sum = Decimal('0.1') + Decimal('0.2')
    print(f"Decimal addition: 0.1 + 0.2 = {decimal_sum}")
    
    # Fraction for rational number arithmetic
    from fractions import Fraction
    fraction_sum = Fraction(1, 3) + Fraction(1, 6)
    print(f"Fraction addition: 1/3 + 1/6 = {fraction_sum}")

def operator_overloading_example():
    """Demonstrates operator overloading for custom objects."""
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
        
        def __str__(self):
            return f"Vector({self.x}, {self.y})"
    
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(f"Vector addition: {v1} + {v2} = {v3}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def best_practices():
    """Demonstrates best practices for using arithmetic operators."""
    # Use parentheses for clarity, even when not strictly necessary
    result = (a + b) * c  # More readable than a + b * c
    
    # Be aware of integer division vs float division
    average = sum(numbers) / len(numbers)  # Use / for float division
    
    # Use augmented assignment operators for conciseness
    x += 5  # Equivalent to x = x + 5
    
    # Use math functions for complex calculations
    import math
    hypotenuse = math.sqrt(a**2 + b**2)
    
    # Use decimal.Decimal for financial calculations
    from decimal import Decimal, getcontext
    getcontext().prec = 2
    tax_rate = Decimal('0.07')
    price = Decimal('10.00')
    tax = price * tax_rate

def common_pitfalls():
    """Highlights common pitfalls when working with arithmetic operators."""
    # Integer division in Python 2 vs Python 3
    print(f"5 / 2 in Python 3: {5 / 2}")  # 2.5 in Python 3, would be 2 in Python 2
    
    # Floating-point precision issues
    print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False due to floating-point imprecision
    
    # Modulo with negative numbers
    print(f"-5 % 3: {-5 % 3}")  # 1, not -2 as some might expect
    
    # Integer overflow (not applicable in Python 3, but worth mentioning)
    large_num = 2**1000
    print(f"2^1000 can be represented: {large_num}")

def advanced_tips():
    """Provides advanced tips for working with arithmetic operators."""
    # Using operator module for functional programming
    import operator
    numbers = [1, 2, 3, 4, 5]
    product = 1
    for num in numbers:
        product = operator.mul(product, num)
    print(f"Product using operator.mul: {product}")
    
    # Using math.prod for efficient product calculation (Python 3.8+)
    import math
    print(f"Product using math.prod: {math.prod(numbers)}")
    
    # Handling very large numbers
    factorial_50 = math.factorial(50)
    print(f"50! has {len(str(factorial_50))} digits")
    
    # Using Decimal for arbitrary precision arithmetic
    from decimal import Decimal, getcontext
    getcontext().prec = 50
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    result = pi * Decimal('2')
    print(f"High precision pi * 2: {result}")

def write_testable_code():
    """Demonstrates how to write testable code for arithmetic operations."""
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide two numbers, raising ValueError if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    class TestArithmeticOperations(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)
            self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        
        def test_divide(self):
            self.assertEqual(divide(6, 3), 2)
            self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)
            with self.assertRaises(ValueError):
                divide(1, 0)
    
    # Run the tests
    unittest.main(argv=[''], exit=False)

# 4. Integration and Real-World Applications

def financial_calculation_example():
    """Demonstrates arithmetic operators in financial calculations."""
    from decimal import Decimal, getcontext
    
    # Set precision for financial calculations
    getcontext().prec = 6
    
    def calculate_compound_interest(principal: Decimal, rate: Decimal, time: int, compounds_per_year: int) -> Decimal:
        """Calculate compound interest."""
        return principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
    
    principal = Decimal('1000.00')
    rate = Decimal('0.05')  # 5% annual interest rate
    time = 5  # 5 years
    compounds_per_year = 12  # compounds monthly
    
    final_amount = calculate_compound_interest(principal, rate, time, compounds_per_year)
    print(f"Final amount after {time} years: ${final_amount:.2f}")

def scientific_computation_example():
    """Demonstrates arithmetic operators in scientific computations."""
    import math
    
    def calculate_orbital_period(semi_major_axis: float, central_mass: float) -> float:
        """Calculate the orbital period of a satellite using Kepler's Third Law."""
        G = 6.67430e-11  # Gravitational constant
        return 2 * math.pi * math.sqrt(semi_major_axis**3 / (G * central_mass))
    
    # Example: Calculate the orbital period of the International Space Station
    iss_altitude = 408000  # m
    earth_radius = 6371000  # m
    earth_mass = 5.97e24  # kg
    
    semi_major_axis = iss_altitude + earth_radius
    orbital_period = calculate_orbital_period(semi_major_axis, earth_mass)
    
    print(f"Orbital period of the ISS: {orbital_period:.2f} seconds")

# 5. Advanced Concepts and Emerging Trends

def advanced_concepts():
    """Explores advanced concepts and emerging trends related to arithmetic operators."""
    # Matrix multiplication (Python 3.5+)
    import numpy as np
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = A @ B  # Matrix multiplication
    print(f"Matrix multiplication result:\n{C}")
    
    # Operator overloading with protocols (Python 3.8+)
    from typing import Protocol
    
    class Addable(Protocol):
        def __add__(self, other): ...
    
    def add_twice(a: Addable, b: Addable) -> Addable:
        return a + b + b
    
    # Using Decimal for arbitrary-precision arithmetic
    from decimal import Decimal, getcontext
    getcontext().prec = 50
    
    sqrt_2 = Decimal('2').sqrt()
    print(f"Square root of 2 to 50 decimal places: {sqrt_2}")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to arithmetic operators."""
    # Q: Why does 0.1 + 0.2 != 0.3?
    print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")
    print("This is due to floating-point representation limitations.")
    print("Use decimal.Decimal for precise decimal arithmetic.")
    
    # Q: How do I perform integer division in Python 3?
    print(f"Integer division: 5 // 2 = {5 // 2}")
    
    # Q: How can I avoid division by zero errors?
    def safe_divide(a, b):
        return a / b if b != 0 else float('inf')
    
    print(f"Safe divide 5 by 0: {safe_divide(5, 0)}")
    
    # Q: How do I calculate the remainder and quotient simultaneously?
    quotient, remainder = divmod(10, 3)
    print(f"divmod(10, 3): quotient = {quotient}, remainder = {remainder}")

# 7. Recommended Tools, Libraries, and Resources

"""
Recommended tools and libraries for working with arithmetic operators:

1. NumPy: Efficient numerical computations
   pip install numpy

2. SymPy: Symbolic mathematics
   pip install sympy

3. Decimal: Precise decimal arithmetic (built-in)

4. math: Mathematical functions (built-in)

5. operator: Functional interface to Python's operators (built-in)

Resources for further learning:
- Python Official Documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- "Python for Data Analysis" by Wes McKinney
- "Numerical Python" by Robert Johansson
- Real Python tutorials: https://realpython.com/python-numbers/
- Python Scientific Lecture Notes: https://scipy-lectures.org/
"""

# 8. Performance Analysis and Optimization

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques for arithmetic operations."""
    import timeit
    import math
    
    # Compare different methods of calculating powers
    def power_operator(base, exponent):
        return base ** exponent
    
    def power_math_pow(base, exponent):
        return math.pow(base, exponent)
    
    base, exponent = 2, 1000
    
    time_operator = timeit.timeit(lambda: power_operator(base, exponent), number=10000)
    time_math_pow = timeit.timeit(lambda: power_math_pow(base, exponent), number=10000)
    
    print(f"Time using ** operator: {time_operator:.6f} seconds")
    print(f"Time using math.pow(): {time_math_pow:.6f} seconds")
    
    # Compare different methods of integer division
    def floor_division(a, b):
        return a // b
    
    def int_division(a, b):
        return int(a / b)
    
    a, b = 1000000, 7
    
    time_floor_division = timeit.timeit(lambda: floor_division(a, b), number=100000)
    time_int_division = timeit.timeit(lambda: int_division(a, b), number=100000)
    
    print(f"Time using // operator: {time_floor_division:.6f} seconds")
    print(f"Time using int(a / b): {time_int_division:.6f} seconds")
    
    # Demonstrate the performance impact of using Decimal for high-precision arithmetic
    from decimal import Decimal, getcontext
    
    def float_addition():
        return sum(0.1 for _ in range(1000000))
    
    def decimal_addition():
        getcontext().prec = 15
        return sum(Decimal('0.1') for _ in range(1000000))
    
    time_float = timeit.timeit(float_addition, number=10)
    time_decimal = timeit.timeit(decimal_addition, number=10)
    
    print(f"Time for float addition: {time_float:.6f} seconds")
    print(f"Time for Decimal addition: {time_decimal:.6f} seconds")
    print("Note: Decimal is slower but provides higher precision for financial calculations")

def optimize_large_scale_computations():
    """Demonstrates optimization techniques for large-scale computations."""
    import numpy as np
    import timeit
    
    # Generate a large list of numbers
    numbers = list(range(1000000))
    
    # Compare Python's built-in sum with NumPy's sum
    time_python_sum = timeit.timeit(lambda: sum(numbers), number=100)
    time_numpy_sum = timeit.timeit(lambda: np.sum(numbers), number=100)
    
    print(f"Time for Python's sum(): {time_python_sum:.6f} seconds")
    print(f"Time for NumPy's sum(): {time_numpy_sum:.6f} seconds")
    
    # Demonstrate vectorized operations with NumPy
    def python_square(numbers):
        return [x**2 for x in numbers]
    
    def numpy_square(numbers):
        return np.array(numbers)**2
    
    time_python_square = timeit.timeit(lambda: python_square(numbers), number=10)
    time_numpy_square = timeit.timeit(lambda: numpy_square(numbers), number=10)
    
    print(f"Time for Python list comprehension: {time_python_square:.6f} seconds")
    print(f"Time for NumPy vectorized operation: {time_numpy_square:.6f} seconds")

def memory_efficient_arithmetic():
    """Demonstrates memory-efficient arithmetic operations."""
    import sys
    
    # Compare memory usage of range vs list
    range_object = range(1000000)
    list_object = list(range(1000000))
    
    print(f"Memory usage of range object: {sys.getsizeof(range_object)} bytes")
    print(f"Memory usage of list object: {sys.getsizeof(list_object)} bytes")
    
    # Demonstrate generator expressions for memory-efficient computations
    def sum_squares_list(n):
        return sum([x**2 for x in range(n)])
    
    def sum_squares_generator(n):
        return sum(x**2 for x in range(n))
    
    n = 10000000
    
    # Measure memory usage
    import tracemalloc
    
    tracemalloc.start()
    sum_squares_list(n)
    list_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    tracemalloc.start()
    sum_squares_generator(n)
    gen_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    print(f"Peak memory usage (list comprehension): {list_memory} bytes")
    print(f"Peak memory usage (generator expression): {gen_memory} bytes")

def main():
    """Main function to demonstrate various concepts."""
    print("1. Basic Arithmetic:")
    basic_arithmetic()

    print("\n2. Advanced Arithmetic:")
    advanced_arithmetic()

    print("\n3. Arithmetic with Different Types:")
    arithmetic_with_different_types()

    print("\n4. Operator Overloading Example:")
    operator_overloading_example()

    print("\n5. Best Practices:")
    best_practices()

    print("\n6. Common Pitfalls:")
    common_pitfalls()

    print("\n7. Advanced Tips:")
    advanced_tips()

    print("\n8. Testable Code:")
    write_testable_code()

    print("\n9. Financial Calculation Example:")
    financial_calculation_example()

    print("\n10. Scientific Computation Example:")
    scientific_computation_example()

    print("\n11. Advanced Concepts:")
    advanced_concepts()

    print("\n12. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()

    print("\n13. Performance Analysis:")
    performance_analysis()

    print("\n14. Optimizing Large-Scale Computations:")
    optimize_large_scale_computations()

    print("\n15. Memory-Efficient Arithmetic:")
    memory_efficient_arithmetic()

if __name__ == "__main__":
    main()

# 9. How to Contribute

"""
To contribute to this cheat sheet:
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

# Contributors:
# - Sabbir Hossain, itsSabbir

# End of cheat sheet