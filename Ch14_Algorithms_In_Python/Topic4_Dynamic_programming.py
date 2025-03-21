# Algorithms in Python - Dynamic Programming - in the Python Programming Language
# ===============================================================================

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
import functools
from typing import List, Dict, Tuple, Callable
import random

# 1. Overview and Historical Context
# ----------------------------------
# Dynamic Programming (DP) is an algorithmic paradigm that solves complex problems
# by breaking them down into simpler subproblems. It is applicable to problems
# exhibiting the properties of overlapping subproblems and optimal substructure.

# Historical context:
# - The term "Dynamic Programming" was coined by Richard Bellman in the 1950s.
# - Bellman's work on optimal control theory laid the foundation for DP.
# - Early applications included resource allocation and operations research.

# Significance:
# - DP provides efficient solutions to many optimization problems.
# - It reduces time complexity from exponential to polynomial in many cases.
# - DP is widely used in various fields, including computer science, economics, and bioinformatics.

# Common use cases:
# - Shortest path problems
# - Resource allocation and optimization
# - Sequence alignment in bioinformatics
# - Natural language processing tasks

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Key Concepts:
# 1. Optimal Substructure: The optimal solution to a problem contains optimal solutions to its subproblems.
# 2. Overlapping Subproblems: The same subproblems are solved multiple times.
# 3. Memoization: Storing results of expensive function calls to avoid redundant computations.
# 4. Tabulation: Bottom-up approach to fill a table with subproblem solutions.

# Example 1: Fibonacci Sequence (Simple Recursion vs. DP)

def fibonacci_recursive(n: int) -> int:
    """
    Compute the nth Fibonacci number using simple recursion.
    Time Complexity: O(2^n)
    Space Complexity: O(n) due to recursive call stack
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dp_memoization(n: int, memo: Dict[int, int] = None) -> int:
    """
    Compute the nth Fibonacci number using DP with memoization.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_dp_memoization(n - 1, memo) + fibonacci_dp_memoization(n - 2, memo)
    return memo[n]

def fibonacci_dp_tabulation(n: int) -> int:
    """
    Compute the nth Fibonacci number using DP with tabulation.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example 2: Longest Common Subsequence (LCS)

def lcs_recursive(X: str, Y: str, m: int, n: int) -> int:
    """
    Compute the length of the Longest Common Subsequence using recursion.
    Time Complexity: O(2^(m+n))
    Space Complexity: O(m+n) due to recursive call stack
    """
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    else:
        return max(lcs_recursive(X, Y, m-1, n), lcs_recursive(X, Y, m, n-1))

def lcs_dp(X: str, Y: str) -> int:
    """
    Compute the length of the Longest Common Subsequence using DP.
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    """
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[m][n]

# Example 3: 0/1 Knapsack Problem

def knapsack_recursive(W: int, wt: List[int], val: List[int], n: int) -> int:
    """
    Solve the 0/1 Knapsack problem using recursion.
    Time Complexity: O(2^n)
    Space Complexity: O(n) due to recursive call stack
    """
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack_recursive(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack_recursive(W-wt[n-1], wt, val, n-1),
                   knapsack_recursive(W, wt, val, n-1))

def knapsack_dp(W: int, wt: List[int], val: List[int]) -> int:
    """
    Solve the 0/1 Knapsack problem using DP.
    Time Complexity: O(nW)
    Space Complexity: O(nW)
    """
    n = len(val)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    return K[n][W]

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Identify the optimal substructure and overlapping subproblems.
# 2. Choose between top-down (memoization) and bottom-up (tabulation) approaches based on the problem.
# 3. Use appropriate data structures for efficient storage and retrieval of subproblem solutions.
# 4. Optimize space usage by using rolling arrays when possible.

# Common Pitfalls:
# 1. Incorrectly defining the recurrence relation or base cases.
# 2. Forgetting to return memoized results in recursive implementations.
# 3. Not handling edge cases properly.
# 4. Unnecessarily using DP for problems that don't require it.

# Advanced Tips:
# 1. Use functools.lru_cache for automatic memoization in Python.
# 2. Implement iterative DP solutions for better space efficiency.
# 3. Use bit manipulation techniques to optimize space in certain DP problems.
# 4. Apply divide-and-conquer optimization for certain DP problems to improve time complexity.

# Example: Using functools.lru_cache for automatic memoization

@functools.lru_cache(maxsize=None)
def fibonacci_lru_cache(n: int) -> int:
    """
    Compute the nth Fibonacci number using automatic memoization.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)

# Example: Space-optimized Fibonacci using rolling array

def fibonacci_space_optimized(n: int) -> int:
    """
    Compute the nth Fibonacci number using constant space.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world applications of Dynamic Programming:

# 1. Bioinformatics:
#    - Sequence alignment (e.g., DNA, protein sequences)
#    - RNA secondary structure prediction

# 2. Natural Language Processing:
#    - Speech recognition
#    - Machine translation

# 3. Computer Graphics:
#    - Seam carving for content-aware image resizing

# 4. Finance:
#    - Portfolio optimization
#    - Option pricing (Black-Scholes model)

# 5. Operations Research:
#    - Resource allocation
#    - Supply chain optimization

# Example: Seam Carving for image resizing

def seam_carving(image: List[List[int]], num_pixels: int) -> List[List[int]]:
    """
    Implement seam carving algorithm for vertical resizing.
    Time Complexity: O(w * h * num_pixels), where w and h are image width and height
    Space Complexity: O(w * h)
    """
    height, width = len(image), len(image[0])
    
    for _ in range(num_pixels):
        # Compute energy map
        energy_map = [[sum(abs(image[i][j] - image[i][j+1]) for j in range(width-1)) +
                       sum(abs(image[i][j] - image[i+1][j]) for j in range(width))
                       for j in range(width)] for i in range(height-1)]
        energy_map.append([0] * width)
        
        # Compute cumulative energy map
        for i in range(height - 2, -1, -1):
            for j in range(width):
                energy_map[i][j] += min(energy_map[i+1][max(0, j-1):min(width, j+2)])
        
        # Find seam with minimum energy
        seam = [0] * height
        seam[0] = energy_map[0].index(min(energy_map[0]))
        for i in range(1, height):
            j = seam[i-1]
            if j > 0 and energy_map[i][j-1] == min(energy_map[i][max(0, j-1):min(width, j+2)]):
                seam[i] = j - 1
            elif j < width - 1 and energy_map[i][j+1] == min(energy_map[i][max(0, j-1):min(width, j+2)]):
                seam[i] = j + 1
            else:
                seam[i] = j
        
        # Remove seam
        for i in range(height):
            image[i] = image[i][:seam[i]] + image[i][seam[i]+1:]
        width -= 1
    
    return image

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# 1. Approximate Dynamic Programming:
#    - Used for solving large-scale optimization problems
#    - Combines DP with simulation and machine learning techniques

# 2. Reinforcement Learning:
#    - Extension of DP to handle stochastic environments
#    - Applications in robotics, game playing, and autonomous systems

# 3. Parallelization of DP Algorithms:
#    - Exploiting parallel computing architectures for faster DP solutions
#    - Challenges in handling dependencies between subproblems

# 4. DP in Quantum Computing:
#    - Exploring quantum algorithms for DP problems
#    - Potential for exponential speedup in certain cases

# Example: Simple Q-learning (a form of Reinforcement Learning)

def q_learning(num_episodes: int, learning_rate: float, discount_factor: float, epsilon: float) -> Dict[Tuple[int, int], float]:
    """
    Implement Q-learning for a simple grid world environment.
    """
    # Define the environment (4x4 grid world)
    num_states = 16
    num_actions = 4  # Up, Right, Down, Left
    goal_state = 15
    
    # Initialize Q-table
    Q = {(s, a): 0 for s in range(num_states) for a in range(num_actions)}
    
    def get_next_state(state: int, action: int) -> int:
        if action == 0:  # Up
            return max(state - 4, state)
        elif action == 1:  # Right
            return state + 1 if state % 4 < 3 else state
        elif action == 2:  # Down
            return min(state + 4, state)
        else:  # Left
            return state - 1 if state % 4 > 0 else state
    
    for _ in range(num_episodes):
        state = 0  # Start state
        while state != goal_state:
            # Epsilon-greedy action selection
            if random.random() < epsilon:
                action = random.randint(0, 3)
            else:
                action = max(range(num_actions), key=lambda a: Q[(state, a)])
            
            next_state = get_next_state(state, action)
            reward = 1 if next_state == goal_state else 0
            
            # Q-value update
            best_next_action = max(range(num_actions), key=lambda a: Q[(next_state, a)])
            Q[(state, action)] += learning_rate * (reward + discount_factor * Q[(next_state, best_next_action)] - Q[(state, action)])
            
            state = next_state
    
    return Q

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: How do I know if a problem can be solved using Dynamic Programming?
# A: A problem can be solved using DP if it has:
#    1. Optimal substructure: The optimal solution can be constructed from optimal solutions of its subproblems.
#    2. Overlapping subproblems: The same subproblems are solved multiple times.

# Q: What's the difference between top-down and bottom-up DP approaches?
# A: 
# - Top-down (Memoization): Starts with the main problem and recursively breaks it down, storing results for reuse.
# - Bottom-up (Tabulation): Starts with the smallest subproblems and iteratively builds up to the main problem.

# Q: How can I optimize the space complexity of DP solutions?
# A:
# 1. Use rolling arrays: Keep only the last few rows/columns of the DP table.
# 2. Reuse the input array if possible.
# 3. Use bit manipulation techniques for certain problems.

# Q: How do I debug DP solutions?
# A:
# 1. Start with small inputs and verify the results manually.
# 2. Print intermediate states of the DP table to understand how it's being filled.
# 3. Use a debugger to step through the code and examine subproblem solutions.
# 4. Implement a recursive solution first, then convert it to DP to ensure correctness.

# Q: How can I improve the time complexity of my DP solution?
# A:
# 1. Identify and eliminate unnecessary computations.
# 2. Use more efficient data structures (e.g., heaps for certain problems).
# 3. Apply problem-specific optimizations (e.g., Knuth's optimization for certain matrix chain multiplication problems).
# 4. Consider using divide-and-conquer DP techniques for certain problems.

# Example: Debugging a DP solution
def debug_lcs_dp(X: str, Y: str) -> int:
    """
    Debug version of Longest Common Subsequence DP solution.
    Prints the DP table at each step for visualization.
    """
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
            
            # Print current state of DP table
            print(f"After considering X[{i-1}]={X[i-1]} and Y[{j-1}]={Y[j-1]}:")
            for row in L:
                print(row)
            print()
    
    return L[m][n]

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. NumPy: Efficient array operations for DP table manipulation
#    pip install numpy

# 2. Numba: JIT compilation for faster DP computations
#    pip install numba

# 3. PyDP: Python library for Differential Privacy, which can be used in conjunction with DP algorithms
#    pip install python-dp

# 4. PuLP: Linear Programming library, useful for certain DP problems
#    pip install pulp

# 5. NetworkX: Graph algorithms library, helpful for graph-based DP problems
#    pip install networkx

# Resources:
# 1. "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein (CLRS)
# 2. "Dynamic Programming for Coding Interviews" by Meenakshi and Kamal Rawat
# 3. "Algorithms" by Robert Sedgewick and Kevin Wayne
# 4. MIT OpenCourseWare: Introduction to Algorithms (https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
# 5. Stanford's Coursera course on Algorithms: (https://www.coursera.org/specializations/algorithms)

# Online Resources:
# 1. GeeksforGeeks DP Problems: https://www.geeksforgeeks.org/dynamic-programming/
# 2. LeetCode DP Problem Set: https://leetcode.com/tag/dynamic-programming/
# 3. Topcoder DP Tutorial: https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/
# 4. Codeforces DP Tutorial: https://codeforces.com/blog/entry/43256

# 8. Performance Analysis and Optimization
# ----------------------------------------

import timeit
import numpy as np
from numba import jit

def benchmark_fibonacci(n: int, implementations: Dict[str, Callable]):
    results = {}
    for name, func in implementations.items():
        start_time = timeit.default_timer()
        result = func(n)
        end_time = timeit.default_timer()
        results[name] = (result, end_time - start_time)
    return results

# Numba-optimized Fibonacci
@jit(nopython=True)
def fibonacci_numba(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def optimize_knapsack_dp(W: int, wt: List[int], val: List[int]) -> int:
    """
    Optimized 0/1 Knapsack problem using DP with NumPy.
    Time Complexity: O(nW)
    Space Complexity: O(W)
    """
    n = len(val)
    dp = np.zeros(W + 1, dtype=int)
    
    for i in range(n):
        dp[wt[i]:] = np.maximum(dp[wt[i]:], val[i] + dp[:-wt[i]])
    
    return dp[W]

def demonstrate_performance_analysis():
    print("Fibonacci Performance Analysis:")
    implementations = {
        "Recursive": fibonacci_recursive,
        "DP Memoization": fibonacci_dp_memoization,
        "DP Tabulation": fibonacci_dp_tabulation,
        "Space Optimized": fibonacci_space_optimized,
        "LRU Cache": fibonacci_lru_cache,
        "Numba Optimized": fibonacci_numba
    }
    
    n = 30
    results = benchmark_fibonacci(n, implementations)
    
    for name, (result, time) in results.items():
        print(f"{name}: Result = {result}, Time = {time:.6f} seconds")
    
    print("\nKnapsack Performance Analysis:")
    W = 1000
    n = 500
    wt = [random.randint(1, 100) for _ in range(n)]
    val = [random.randint(1, 1000) for _ in range(n)]
    
    start_time = timeit.default_timer()
    result_dp = knapsack_dp(W, wt, val)
    dp_time = timeit.default_timer() - start_time
    
    start_time = timeit.default_timer()
    result_optimized = optimize_knapsack_dp(W, wt, val)
    optimized_time = timeit.default_timer() - start_time
    
    print(f"Standard DP: Result = {result_dp}, Time = {dp_time:.6f} seconds")
    print(f"Optimized DP: Result = {result_optimized}, Time = {optimized_time:.6f} seconds")

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

# When adding new sections or expanding existing ones, consider the following:
# - Relevance to the main topic of Dynamic Programming in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

def main():
    # Demonstrate Fibonacci implementations
    n = 10
    print(f"Fibonacci({n}):")
    print(f"Recursive: {fibonacci_recursive(n)}")
    print(f"DP Memoization: {fibonacci_dp_memoization(n)}")
    print(f"DP Tabulation: {fibonacci_dp_tabulation(n)}")
    print(f"Space Optimized: {fibonacci_space_optimized(n)}")
    print(f"LRU Cache: {fibonacci_lru_cache(n)}")
    
    # Demonstrate Longest Common Subsequence
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(f"\nLongest Common Subsequence of '{X}' and '{Y}':")
    print(f"Recursive: {lcs_recursive(X, Y, len(X), len(Y))}")
    print(f"DP: {lcs_dp(X, Y)}")
    
    # Demonstrate Knapsack Problem
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    print("\nKnapsack Problem:")
    print(f"Recursive: {knapsack_recursive(W, wt, val, len(val))}")
    print(f"DP: {knapsack_dp(W, wt, val)}")
    
    # Demonstrate Seam Carving
    image = [[random.randint(0, 255) for _ in range(10)] for _ in range(10)]
    print("\nSeam Carving:")
    print("Original image:")
    for row in image:
        print(row)
    resized_image = seam_carving(image, 3)
    print("Resized image:")
    for row in resized_image:
        print(row)
    
    # Demonstrate Q-learning
    print("\nQ-learning:")
    q_table = q_learning(1000, 0.1, 0.99, 0.1)
    print("Q-table:")
    for state in range(16):
        print(f"State {state}: {[q_table[(state, a)] for a in range(4)]}")
    
    # Demonstrate Performance Analysis
    demonstrate_performance_analysis()

if __name__ == "__main__":
    main()