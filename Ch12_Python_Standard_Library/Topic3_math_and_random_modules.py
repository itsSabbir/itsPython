"""
Python Standard Library - math and random modules - in the Python Programming Language
======================================================================================

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

Author: Sabbir Hossain

1. Overview and Historical Context
----------------------------------
The math and random modules are core components of Python's standard library, providing essential functionalities for mathematical operations and random number generation, respectively.

Historical context:
- The math module has been part of Python since its early versions, offering mathematical functions and constants.
- The random module was introduced to provide pseudorandom number generation capabilities.
- Both modules have undergone significant improvements over the years, with Python 3.x versions introducing new features and optimizations.

Significance:
- math module: Provides functions for mathematical operations and constants with C-like double precision.
- random module: Offers a suite of functions for generating random numbers, making selections, and shuffling sequences.

Common use cases:
- Scientific computing and data analysis
- Simulations and modeling
- Game development
- Cryptography and security applications

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import math
import random
import statistics
from typing import List, Tuple

def demonstrate_math_basics():
    """Demonstrate basic usage of the math module."""
    # Constants
    print(f"Pi: {math.pi}")
    print(f"Euler's number: {math.e}")
    
    # Basic functions
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"5 to the power of 3: {math.pow(5, 3)}")
    
    # Trigonometric functions
    print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")
    print(f"Cosine of 60 degrees: {math.cos(math.radians(60))}")
    
    # Logarithmic functions
    print(f"Natural log of 10: {math.log(10)}")
    print(f"Log base 2 of 8: {math.log2(8)}")
    
    # Rounding functions
    print(f"Ceiling of 3.7: {math.ceil(3.7)}")
    print(f"Floor of 3.7: {math.floor(3.7)}")

def demonstrate_random_basics():
    """Demonstrate basic usage of the random module."""
    # Generate a random float between 0 and 1
    print(f"Random float: {random.random()}")
    
    # Generate a random integer in a range
    print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
    
    # Choose a random element from a sequence
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Random fruit: {random.choice(fruits)}")
    
    # Shuffle a list in place
    numbers = list(range(10))
    random.shuffle(numbers)
    print(f"Shuffled numbers: {numbers}")
    
    # Generate a random sample without replacement
    print(f"Random sample of 3 fruits: {random.sample(fruits, 3)}")

def monte_carlo_pi_estimation(n: int) -> float:
    """
    Estimate the value of pi using the Monte Carlo method.
    
    Args:
        n (int): Number of random points to generate.
    
    Returns:
        float: Estimated value of pi.
    """
    inside_circle = 0
    total_points = n
    
    for _ in range(total_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside_circle += 1
    
    pi_estimate = 4 * inside_circle / total_points
    return pi_estimate

def demonstrate_monte_carlo():
    """Demonstrate the Monte Carlo method for estimating pi."""
    iterations = [1000, 10000, 100000, 1000000]
    for n in iterations:
        estimated_pi = monte_carlo_pi_estimation(n)
        print(f"Pi estimate with {n} iterations: {estimated_pi}")
        print(f"Difference from math.pi: {abs(estimated_pi - math.pi)}")

def custom_random_generator(seed: int = 42) -> Tuple[int, callable]:
    """
    Implement a simple linear congruential generator.
    
    Args:
        seed (int): Starting seed for the generator.
    
    Returns:
        Tuple[int, callable]: Current state and next() function.
    """
    a, c, m = 1664525, 1013904223, 2**32
    state = seed
    
    def next_int():
        nonlocal state
        state = (a * state + c) % m
        return state
    
    return state, next_int

def demonstrate_custom_random():
    """Demonstrate usage of a custom random number generator."""
    _, next_int = custom_random_generator()
    
    print("Generated random numbers:")
    for _ in range(5):
        print(next_int() % 100)  # Generate numbers between 0 and 99

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use math.isclose() for comparing floating-point numbers instead of direct equality checks.
2. Set a fixed seed with random.seed() for reproducibility in simulations and testing.
3. Use random.SystemRandom() for cryptographically secure random number generation.
4. Prefer math module functions over custom implementations for better performance and accuracy.

Common Pitfalls:
1. Forgetting that random.randrange() excludes the stop value, unlike random.randint().
2. Using random.random() * n to generate integers, which can lead to bias.
3. Relying on the default random generator for security-sensitive applications.
4. Not considering the limitations of floating-point arithmetic in mathematical computations.

Advanced Tips:
1. Use math.fsum() for more accurate floating-point summation.
2. Leverage the statistics module for advanced statistical functions.
3. Use random.getrandbits() for efficient generation of large random integers.
4. Implement custom probability distributions using random.random() and inverse transform sampling.
"""

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques with math and random modules."""
    # Accurate floating-point summation
    numbers = [0.1] * 10
    print(f"Sum using math.fsum: {math.fsum(numbers)}")
    print(f"Sum using built-in sum: {sum(numbers)}")
    
    # Using statistics module
    data = [random.gauss(0, 1) for _ in range(1000)]
    print(f"Mean: {statistics.mean(data)}")
    print(f"Median: {statistics.median(data)}")
    print(f"Standard deviation: {statistics.stdev(data)}")
    
    # Generate large random integer
    large_random = random.getrandbits(64)
    print(f"Large random integer: {large_random}")
    
    # Custom probability distribution (exponential distribution)
    def random_exponential(lambd: float) -> float:
        return -math.log(1 - random.random()) / lambd
    
    exp_samples = [random_exponential(0.5) for _ in range(1000)]
    print(f"Mean of exponential samples: {statistics.mean(exp_samples)}")

"""
4. Integration and Real-World Applications
------------------------------------------
The math and random modules are fundamental in many Python applications and frameworks:

1. NumPy: Extends Python's math capabilities for large-scale numerical computing.
2. SciPy: Builds on NumPy for scientific and technical computing.
3. Matplotlib: Uses math functions for data visualization and plotting.

Real-world example: A simple Monte Carlo simulation for option pricing
"""

import math
import random

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the Black-Scholes price of a European call option.
    
    Args:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to expiration (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the stock
    
    Returns:
        float: Option price
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    return S * math.erf(d1 / math.sqrt(2)) - K * math.exp(-r * T) * math.erf(d2 / math.sqrt(2))

def monte_carlo_option_pricing(S: float, K: float, T: float, r: float, sigma: float, num_simulations: int) -> float:
    """
    Price a European call option using Monte Carlo simulation.
    
    Args:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to expiration (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the stock
        num_simulations (int): Number of simulations to run
    
    Returns:
        float: Estimated option price
    """
    option_payoffs = []
    for _ in range(num_simulations):
        ST = S * math.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * random.gauss(0, 1))
        payoff = max(ST - K, 0)
        option_payoffs.append(payoff)
    
    option_price = math.exp(-r * T) * statistics.mean(option_payoffs)
    return option_price

def demonstrate_option_pricing():
    """Demonstrate option pricing using Black-Scholes and Monte Carlo methods."""
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    
    bs_price = black_scholes_call(S, K, T, r, sigma)
    print(f"Black-Scholes price: {bs_price:.4f}")
    
    num_simulations = 100000
    mc_price = monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations)
    print(f"Monte Carlo price: {mc_price:.4f}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Sympy: A symbolic mathematics library that extends Python's mathematical capabilities.
2. Cython: Allows for C-level performance for numerical computations in Python.
3. Quantum random number generators: Emerging technology for true randomness.
"""

try:
    import sympy
    import cython
except ImportError:
    print("Sympy and/or Cython not installed. Skipping advanced demonstrations.")
else:
    def demonstrate_advanced_libraries():
        """Demonstrate usage of advanced mathematical libraries."""
        # Sympy for symbolic mathematics
        x = sympy.Symbol('x')
        expr = sympy.sin(x) ** 2 + sympy.cos(x) ** 2
        print(f"Simplified expression: {expr.simplify()}")
        
        # Solve an equation symbolically
        equation = sympy.Eq(x**2 - 4, 0)
        solution = sympy.solve(equation)
        print(f"Solution to x^2 - 4 = 0: {solution}")
        
        # Note: Cython demonstration would require a separate .pyx file and compilation

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I seed the random number generator for reproducibility?
A: Use random.seed(x) where x is any hashable object. For best results, use an integer.

Q: Why don't my random numbers look random?
A: The random module uses a pseudorandom number generator. For true randomness, consider using random.SystemRandom() or external sources of entropy.

Q: How can I generate random numbers from a specific probability distribution?
A: Use the specific functions provided by the random module (e.g., random.gauss() for normal distribution) or implement custom distributions using inverse transform sampling.

Troubleshooting:
1. Issue: Getting different results on different runs of a randomized algorithm
   Solution: Set a fixed seed at the beginning of your script using random.seed().

2. Issue: Floating-point inaccuracies in mathematical computations
   Solution: Use math.isclose() for comparisons and math.fsum() for summations.

3. Issue: Slow performance for large-scale random number generation
   Solution: Consider using NumPy's random module for improved performance with large arrays.
"""

def demonstrate_troubleshooting():
    """Demonstrate common troubleshooting scenarios."""
    # Setting a fixed seed for reproducibility
    random.seed(42)
    print("Random numbers with fixed seed:")
    for _ in range(3):
        print(random.random())
    
    # Dealing with floating-point inaccuracies
    a = 0.1 + 0.2
    b = 0.3
    print(f"0.1 + 0.2 == 0.3: {a == b}")
    print(f"math.isclose(0.1 + 0.2, 0.3): {math.isclose(a, b)}")
    
    # Accurate summation
    numbers = [0.1] * 10
    print(f"Accurate sum: {math.fsum(numbers)}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. NumPy: Fundamental package for scientific computing in Python.
2. SciPy: Library for mathematics, science, and engineering.
3. Sympy: Library for symbolic mathematics.
4. Matplotlib: Plotting library for creating static, animated, and interactive visualizations.

Resources:
- "Python for Data Analysis" by Wes McKinney (O'Reilly)
- "Numerical Python" by Robert Johansson (Apress)
- Python's official documentation on math module: https://docs.python.org/3/library/math.html
- Python's official documentation on random module: https://docs.python.org/3/library/random.html
- Real Python's guide on Python's math module: https://realpython.com/python-math-module/

8. Performance Analysis and Optimization
----------------------------------------
When working with mathematical computations and random number generation, performance can be critical, especially for large-scale applications.
"""

import timeit

def performance_comparison():
    """Compare the performance of different mathematical and random operations."""
    
    def using_math_pow():
        return math.pow(2, 10)
    
    def using_operator():
        return 2 ** 10
    
    def generate_random_list():
        return [random.random() for _ in range(10000)]
    
    def generate_random_list_comprehension():
        return list(random.random() for _ in range(10000))
    
    # Measure execution times
    math_pow_time = timeit.timeit(using_math_pow, number=100000)
    operator_time = timeit.timeit(using_operator, number=100000)
    random_list_time = timeit.timeit(generate_random_list, number=100)
    random_list_comp_time = timeit.timeit(generate_random_list_comprehension, number=100)
    
    print(f"math.pow(2, 10): {math_pow_time:.6f} seconds")
    print(f"math.pow(2, 10): {math_pow_time:.6f} seconds")
    print(f"2 ** 10: {operator_time:.6f} seconds")
    print(f"Generate random list: {random_list_time:.6f} seconds")
    print(f"Generate random list (comprehension): {random_list_comp_time:.6f} seconds")

"""
Performance Considerations:
1. Math operations are generally fast, but can become bottlenecks in tight loops.
2. Random number generation can be slow for large quantities of numbers.
3. Some math functions (e.g., pow, exp) have both Python and C implementations.

Optimization Strategies:
1. Use built-in operators (**, //, %) instead of math functions for simple operations.
2. Pre-compute values when possible, especially for constants or frequently used values.
3. Use NumPy for large-scale numerical operations and random number generation.
4. Consider using Cython for performance-critical mathematical computations.
"""

def optimized_monte_carlo_pi(n: int) -> float:
    """
    An optimized version of the Monte Carlo pi estimation.
    
    Args:
        n (int): Number of points to generate.
    
    Returns:
        float: Estimated value of pi.
    """
    inside_circle = sum(
        (random.random()**2 + random.random()**2) <= 1
        for _ in range(n)
    )
    return 4 * inside_circle / n

def demonstrate_optimized_code():
    """Demonstrate optimized code for mathematical and random operations."""
    # Optimized Monte Carlo pi estimation
    n = 1000000
    start_time = time.perf_counter()
    pi_estimate = optimized_monte_carlo_pi(n)
    end_time = time.perf_counter()
    
    print(f"Optimized Monte Carlo pi estimate: {pi_estimate}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    
    # Pre-computing values
    start_time = time.perf_counter()
    sqrt_2 = math.sqrt(2)
    results = [x * sqrt_2 for x in range(1000000)]
    end_time = time.perf_counter()
    
    print(f"Time for pre-computed multiplication: {end_time - start_time:.6f} seconds")
    
    # Without pre-computing
    start_time = time.perf_counter()
    results = [x * math.sqrt(2) for x in range(1000000)]
    end_time = time.perf_counter()
    
    print(f"Time without pre-computing: {end_time - start_time:.6f} seconds")

"""
9. How to Contribute
--------------------
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

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of math and random modules in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to math and random modules.
    """
    print("Demonstrating math basics:")
    demonstrate_math_basics()
    
    print("\nDemonstrating random basics:")
    demonstrate_random_basics()
    
    print("\nDemonstrating Monte Carlo pi estimation:")
    demonstrate_monte_carlo()
    
    print("\nDemonstrating custom random number generator:")
    demonstrate_custom_random()
    
    print("\nDemonstrating advanced techniques:")
    demonstrate_advanced_techniques()
    
    print("\nDemonstrating option pricing:")
    demonstrate_option_pricing()
    
    try:
        print("\nDemonstrating advanced libraries:")
        demonstrate_advanced_libraries()
    except NameError:
        print("Skipping advanced libraries demonstration due to import issues.")
    
    print("\nDemonstrating troubleshooting scenarios:")
    demonstrate_troubleshooting()
    
    print("\nPerformance comparison of mathematical and random operations:")
    performance_comparison()
    
    print("\nDemonstrating optimized code:")
    demonstrate_optimized_code()

if __name__ == "__main__":
    main()