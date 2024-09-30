"""
Operators and Expressions - Bitwise operators - in the Python Programming Language
=================================================================================

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
=================================
Bitwise operators in Python are special operators used to perform operations on 
individual bits of binary numbers. These operators work directly with the binary 
representations of integers, allowing for efficient low-level operations.

Historical context:
- Bitwise operations have been a fundamental part of computer science since the 
  early days of computing, dating back to the 1940s and 1950s.
- They were introduced in Python from its inception in the early 1990s, 
  recognizing their importance in systems programming and low-level operations.
- While high-level languages often abstract away the need for direct bit 
  manipulation, Python retained these operators for their efficiency and 
  usefulness in certain domains.

Relevance in modern software development:
- Crucial for systems programming, embedded systems, and hardware interfacing.
- Used in cryptography, data compression, and network protocols.
- Essential for optimizing memory usage and performance in resource-constrained 
  environments.

Comparison to other languages:
- Python's bitwise operators are similar to those in C and Java, making them 
  familiar to developers coming from these backgrounds.
- Unlike some low-level languages, Python abstracts away the need to consider 
  integer sizes in most cases, simplifying their use.

"""

# ========================================
# 2. Syntax, Key Concepts, and Code Examples
# ==========================================
"""
Python provides six bitwise operators:

1. & (AND) - Performs a bit-by-bit AND operation.
2. | (OR) - Performs a bit-by-bit OR operation.
3. ^ (XOR) - Performs a bit-by-bit exclusive OR operation.
4. ~ (NOT) - Performs a bitwise negation (inverts all bits).
5. << (Left shift) - Shifts bits to the left by a specified number of positions.
6. >> (Right shift) - Shifts bits to the right by a specified number of positions.

These operators are fundamental in low-level programming, such as systems programming, graphics, cryptography, and optimization tasks. 
They work directly on the binary representation of integers.
"""

import time  # Provides various time-related functions
import random  # Used for generating random numbers

def bitwise_and_demo():
    """
    Demonstrates the bitwise AND operator (&).
    This operator compares each bit of its operands. If both bits are 1, the resulting bit is 1; otherwise, it is 0.
    """
    a = 60  # 0011 1100 in binary
    b = 13  # 0000 1101 in binary
    result = a & b  # Bitwise AND operation between 'a' and 'b'
    
    # Explanation:
    # 60 in binary: 0011 1100
    # 13 in binary: 0000 1101
    # ----------------------
    # Result       : 0000 1100 (which is 12 in decimal)

    print(f"Bitwise AND of {a} and {b}: {result}")  # Expected output: 12
    print(f"Binary representation: {bin(result)}")  # bin() converts the result to its binary form, e.g., '0b1100'
    
    # Advanced use: Checking if a number is even
    # ------------------------------------------
    # In binary, even numbers always have a 0 as their least significant bit (LSB). By performing 'num & 1', we can 
    # check if this bit is 0 (meaning the number is even) or 1 (odd).
    num = 42  # 42 in binary is 101010
    is_even = num & 1 == 0  # Evaluates to True because the LSB is 0
    print(f"Is {num} even? {is_even}")

    # Pitfall: Using the bitwise AND (&) on signed integers can yield unexpected results due to two's complement representation.
    # Always be cautious when performing bitwise operations on negative integers.

def bitwise_or_demo():
    """
    Demonstrates the bitwise OR operator (|).
    This operator compares each bit of its operands. If at least one of the bits is 1, the resulting bit is set to 1.
    """
    a = 60  # 0011 1100 in binary
    b = 13  # 0000 1101 in binary
    result = a | b  # Bitwise OR operation between 'a' and 'b'
    
    # Explanation:
    # 60 in binary: 0011 1100
    # 13 in binary: 0000 1101
    # ----------------------
    # Result       : 0011 1101 (which is 61 in decimal)

    print(f"Bitwise OR of {a} and {b}: {result}")  # Expected output: 61
    print(f"Binary representation: {bin(result)}")  # Outputs '0b111101', representing 61 in binary

    # Advanced use: Setting a specific bit
    # ------------------------------------
    # This technique is commonly used in low-level programming, such as enabling specific features/settings in 
    # hardware registers or manipulating individual bits in a flag variable.
    num = 64  # Binary: 0100 0000
    bit_position = 2  # Refers to the bit we want to set (counting from the right, starting at position 0)
    
    # To set a specific bit, we use (1 << bit_position) to create a mask where only the desired bit is set.
    # Example: (1 << 2) results in 0000 0100
    num_with_bit_set = num | (1 << bit_position)  # Performs the bitwise OR to set the desired bit
    
    # Explanation:
    # 64 in binary    : 0100 0000
    # Bitmask (1 << 2): 0000 0100
    # ---------------------------
    # Result          : 0100 0100 (which is 68 in decimal)

    print(f"Setting bit {bit_position} in {num}: {num_with_bit_set}")  # Outputs: 68

    # Pitfall: Ensure the bit position is within valid bounds (0 to the number of bits in the datatype). 
    # Shifting a bit beyond the maximum bit length results in undefined behavior or errors.

# Advanced Insights:
# - Bitwise operations are extremely efficient because they operate directly on binary representations at the CPU level.
# - They are often used in performance-critical applications, bit masking, toggling bits, and in areas where memory optimization is paramount.
# - However, always use them judiciously, as they can reduce code readability if overused or applied without clear context.

# Additional Advanced Tip:
# Python integers are unbounded (except by memory), meaning they can grow to an arbitrary size. However, it's crucial 
# to be aware that bitwise operations on very large integers can become computationally expensive, affecting performance.


# ========================================
# Bitwise Operations Demonstrations
# ---------------------------------------

def bitwise_xor_demo():
    """
    Demonstrates the bitwise XOR operator (^).
    The XOR (exclusive OR) operator performs a bit-by-bit comparison between two numbers.
    It returns '1' if the corresponding bits are different, and '0' if they are the same.
    This behavior makes it useful for tasks like toggling bits and certain algorithms.
    """

    # Basic Example: Bitwise XOR
    # -------------------------
    a = 60  # Binary representation: 0011 1100
    b = 13  # Binary representation: 0000 1101
    
    # The bitwise XOR operation compares each bit of 'a' and 'b':
    # 0011 1100 (a)
    # 0000 1101 (b)
    # ---------
    # 0011 0001 (result) = 49 in decimal

    result = a ^ b  # Performs the bitwise XOR operation
    print(f"Bitwise XOR of {a} and {b}: {result}")
    print(f"Binary representation: {bin(result)}")  # 'bin()' returns the binary string representation prefixed by '0b'

    # Advanced Use: Swapping two numbers without a temporary variable
    # --------------------------------------------------------------
    # Using the XOR swap algorithm, we can swap two variables' values without needing an extra temporary variable.
    # This method is efficient in terms of space but may be less readable than traditional swapping, hence 
    # often used to demonstrate bitwise operations rather than in production code.
    
    x, y = 10, 20  # Initialize x and y
    print(f"Before swap: x = {x}, y = {y}")

    # Swapping using XOR
    x ^= y  # Step 1: x now holds the XOR of x and y
    y ^= x  # Step 2: y now becomes the original x
    x ^= y  # Step 3: x now becomes the original y
    
    print(f"After swap: x = {x}, y = {y}")

    # Advanced Insight: Although this swapping method avoids using a temporary variable, it's not commonly used
    # in practice because it can be harder to understand and may lead to maintenance challenges.
    # It's also slower on modern processors than using a simple tuple swap (x, y = y, x) due to lack of readability
    # and potential issues with integer overflow in some languages (though not in Python).

def bitwise_not_demo():
    """
    Demonstrates the bitwise NOT operator (~).
    The bitwise NOT operator flips all the bits in a number, turning 1s to 0s and 0s to 1s.
    It effectively produces the binary complement of the given number.
    """

    # Basic Example: Bitwise NOT
    # -------------------------
    a = 60  # Binary representation: 0011 1100
    
    # The bitwise NOT operation flips all bits:
    # 0011 1100 (a)
    # ---------
    # 1100 0011 (result in a 32-bit system would be represented as -61 in two's complement form)

    result = ~a  # Performs the bitwise NOT operation
    print(f"Bitwise NOT of {a}: {result}")
    print(f"Binary representation: {bin(result & 0xFF)}")  # '& 0xFF' masks to display the last 8 bits
    
    # Explanation: Python uses signed integers, and the bitwise NOT operation (~) produces a negative result 
    # due to the two's complement representation. For example, ~60 results in -61 because:
    # - Original (unsigned 8-bit): 0011 1100 (60)
    # - Flipped: 1100 0011 -> In two's complement form, this represents -61.

    # Advanced Tip: Using 'result & 0xFF' masks the result to show only the last 8 bits, making it easier
    # to visualize and understand the bit manipulation in cases where you’re interested in a fixed-width
    # representation (e.g., working with bytes).

    # Advanced Use: Finding the Two's Complement
    # -----------------------------------------
    # The two's complement is a way of representing negative numbers in binary form, widely used in computing.
    # It can be obtained by inverting the bits using the NOT operator and then adding 1.

    num = 42  # Example positive integer
    twos_complement = ~num + 1  # Inverting all bits and adding 1 gives the two's complement

    print(f"Two's complement of {num}: {twos_complement}")

    # Explanation: The two's complement operation effectively gives the negative representation of 'num'.
    # In binary:
    # - num = 42 is '0010 1010'
    # - ~num = '1101 0101' (flipped bits)
    # - Adding 1: '1101 0110' represents -42 in two's complement form.

    # Advanced Insight: The two's complement system is widely used because it allows the same hardware to perform
    # addition and subtraction operations without requiring separate circuitry. This is why understanding bitwise
    # operations like NOT is crucial for low-level programming, embedded systems, and performance-critical applications.

# Summary
# -------
# - Bitwise XOR (^) is useful for toggling bits and swapping values without temporary variables, but be cautious of readability.
# - Bitwise NOT (~) flips all bits, which is helpful for finding the two's complement and understanding binary representations.
# - Always consider the implications of bit-level operations, especially how Python's handling of integers differs from other languages.
# - These demonstrations are valuable for understanding how data is manipulated at a low level and are frequently used
#   in fields like cryptography, data compression, and performance optimization.

# These comprehensive comments provide insights into the bitwise operations from a beginner's understanding to advanced use cases,
# preparing the reader to tackle complex problems and optimize code in performance-critical scenarios.


def bitwise_shift_demo():
    """
    Demonstrates the bitwise shift operators (<< and >>).
    << shifts bits to the left, >> shifts bits to the right.
    """
    a = 60  # 0011 1100
    left_shift = a << 2
    right_shift = a >> 2
    print(f"Left shift of {a} by 2: {left_shift}")
    print(f"Right shift of {a} by 2: {right_shift}")
    
    # Advanced use: Efficient multiplication and division by powers of 2
    num = 10
    multiplied = num << 3  # Equivalent to num * 8
    divided = num >> 1     # Equivalent to num // 2
    print(f"{num} * 8 = {multiplied}")
    print(f"{num} // 2 = {divided}")

def bitwise_operations_benchmark():
    """
    Benchmarks bitwise operations against their arithmetic counterparts.
    """
    def time_operation(operation, n=1000000):
        start = time.time()
        for _ in range(n):
            operation()
        end = time.time()
        return end - start

    # Generate random numbers for testing
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)

    # Benchmark multiplication vs left shift
    mult_time = time_operation(lambda: a * 2)
    shift_time = time_operation(lambda: a << 1)
    print(f"Multiplication time: {mult_time:.6f}s")
    print(f"Left shift time: {shift_time:.6f}s")
    print(f"Left shift is {mult_time/shift_time:.2f}x faster")

    # Benchmark division vs right shift
    div_time = time_operation(lambda: a // 2)
    rshift_time = time_operation(lambda: a >> 1)
    print(f"Division time: {div_time:.6f}s")
    print(f"Right shift time: {rshift_time:.6f}s")
    print(f"Right shift is {div_time/rshift_time:.2f}x faster")

    # Benchmark modulo vs bitwise AND
    mod_time = time_operation(lambda: a % 2)
    and_time = time_operation(lambda: a & 1)
    print(f"Modulo time: {mod_time:.6f}s")
    print(f"Bitwise AND time: {and_time:.6f}s")
    print(f"Bitwise AND is {mod_time/and_time:.2f}x faster")

def main():
    print("Bitwise Operators in Python - Expert-Level Note Sheet")
    print("====================================================")
    
    bitwise_and_demo()
    print("\n" + "="*50 + "\n")
    
    bitwise_or_demo()
    print("\n" + "="*50 + "\n")
    
    bitwise_xor_demo()
    print("\n" + "="*50 + "\n")
    
    bitwise_not_demo()
    print("\n" + "="*50 + "\n")
    
    bitwise_shift_demo()
    print("\n" + "="*50 + "\n")
    
    print("Performance Benchmarking:")
    bitwise_operations_benchmark()

if __name__ == "__main__":
    main()

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
=====================================================

Best Practices:
1. Use meaningful variable names to clarify the purpose of bitwise operations.
2. Comment your code extensively when using bitwise operators, as their purpose 
   may not be immediately clear to other developers.
3. Use parentheses to clarify the order of operations when combining bitwise 
   operators with other operators.
4. When working with specific bit patterns, consider using named constants to 
   improve readability.

Common Pitfalls:
1. Forgetting that negative numbers are represented in two's complement form, 
   which can lead to unexpected results with bitwise operations.
2. Neglecting to account for the sign bit when performing right shifts on 
   signed integers.
3. Assuming that integers in Python have a fixed size (they don't - Python uses 
   arbitrary-precision integers).
4. Overusing bitwise operations where higher-level constructs would be more 
   readable and maintainable.

Advanced Tips:
1. Use the bitwise AND operation with a mask to extract specific bits from an 
   integer:

   def extract_bits(number, start, length):
       mask = (1 << length) - 1
       return (number >> start) & mask

2. Implement fast modulo operations for powers of 2 using bitwise AND:

   def fast_modulo_power_of_two(number, divisor):
       return number & (divisor - 1)

3. Use XOR for in-place swapping of values without using a temporary variable:

   a ^= b
   b ^= a
   a ^= b

4. Implement efficient multiplication and division by powers of 2 using left 
   and right shifts:

   def multiply_by_power_of_two(number, power):
       return number << power

   def divide_by_power_of_two(number, power):
       return number >> power

5. Use bitwise operations for efficient state management in games or simulations:

   class GameState:
       def __init__(self):
           self.state = 0

       def set_flag(self, flag):
           self.state |= (1 << flag)

       def clear_flag(self, flag):
           self.state &= ~(1 << flag)

       def toggle_flag(self, flag):
           self.state ^= (1 << flag)

       def check_flag(self, flag):
           return bool(self.state & (1 << flag))

6. Implement a circular bit rotation:

   def circular_rotate_left(number, shift, bit_size=32):
       return ((number << shift) | (number >> (bit_size - shift))) & ((1 << bit_size) - 1)

   def circular_rotate_right(number, shift, bit_size=32):
       return ((number >> shift) | (number << (bit_size - shift))) & ((1 << bit_size) - 1)

7. Use bitwise operations for efficient memory usage in data structures:

   class CompactBooleanArray:
       def __init__(self, size):
           self.data = bytearray((size + 7) // 8)
           self.size = size

       def __setitem__(self, index, value):
           if index < 0 or index >= self.size:
               raise IndexError("Index out of range")
           byte_index, bit_offset = divmod(index, 8)
           if value:
               self.data[byte_index] |= (1 << bit_offset)
           else:
               self.data[byte_index] &= ~(1 << bit_offset)

       def __getitem__(self, index):
           if index < 0 or index >= self.size:
               raise IndexError("Index out of range")
           byte_index, bit_offset = divmod(index, 8)
           return bool(self.data[byte_index] & (1 << bit_offset))

4. Integration and Real-World Applications
==========================================
Bitwise operators are used in various real-world applications:

1. Network Programming:
   - IP address and subnet mask calculations
   - Packet header manipulation
   - Protocol implementations (e.g., TCP/IP stack)

2. Graphics Programming:
   - Color manipulation (e.g., RGB color mixing)
   - Image processing algorithms

3. Cryptography:
   - Implementing encryption algorithms
   - Secure hashing functions

4. Data Compression:
   - Huffman coding
   - Run-length encoding

5. Embedded Systems:
   - Device driver development
   - Hardware register manipulation

6. Game Development:
   - Collision detection using bitmasks
   - Tile-based map systems

7. Database Systems:
   - Bitmap indexing
   - Query optimization

Example: Using bitwise operations for RGB color manipulation

def blend_colors(color1, color2, alpha):
    r1, g1, b1 = color1 >> 16 & 0xFF, color1 >> 8 & 0xFF, color1 & 0xFF
    r2, g2, b2 = color2 >> 16 & 0xFF, color2 >> 8 & 0xFF, color2 & 0xFF
    
    r = int(r1 * (1 - alpha) + r2 * alpha)
    g = int(g1 * (1 - alpha) + g2 * alpha)
    b = int(b1 * (1 - alpha) + b2 * alpha)
    
    return (r << 16) | (g << 8) | b

# Usage
red = 0xFF0000
blue = 0x0000FF
purple = blend_colors(red, blue, 0.5)
print(f"Blended color: #{purple:06X}")

5. Advanced Concepts and Emerging Trends
========================================
1. Quantum Computing:
   As quantum computing evolves, new bitwise operations are being developed to 
   work with qubits instead of classical bits.

2. DNA Computing:
   Researchers are exploring the use of bitwise operations in DNA-based 
   computations for tasks like pattern matching in genomic data.

3. Machine Learning:
   Bitwise operations are being used to optimize neural network architectures 
   and reduce the memory footprint of AI models.

4. Homomorphic Encryption:
   Advanced cryptographic techniques are leveraging bitwise operations to 
   perform computations on encrypted data without decrypting it.

5. Post-Quantum Cryptography:
   New cryptographic algorithms resistant to quantum attacks are being 
   developed, often relying heavily on bitwise operations.

6. FAQs and Troubleshooting
===========================
Q: Why does ~0 equal -1 in Python?
A: In Python, integers are represented using two's complement. The bitwise NOT 
   of 0 (all bits 0) results in all bits being 1, which is the two's complement 
   representation of -1.

Q: How can I perform bitwise operations on large integers efficiently?
A: Python's built-in integers have arbitrary precision, so bitwise operations 
   are generally efficient even for large numbers. For extremely large numbers, 
   consider using specialized libraries like gmpy2.

Q: Are bitwise operations thread-safe?
A: Yes, bitwise operations on immutable integers are thread-safe in Python. 
   However, if you're modifying a shared mutable object using bitwise 
   operations, you should use appropriate synchronization mechanisms.

Troubleshooting:


1. Unexpected results with negative numbers:
   Problem: Bitwise operations on negative numbers yield unexpected results.
   Solution: Remember that Python uses two's complement for negative numbers. 
   Always consider the sign when performing bitwise operations.

   Example:
   def print_binary(n):
       return f"{n:032b}" if n >= 0 else f"{n & 0xffffffff:032b}"

   num = -5
   print(f"Binary representation of {num}: {print_binary(num)}")
   print(f"After right shift by 1: {print_binary(num >> 1)}")

2. Incorrect masking:
   Problem: Failing to use the correct mask when extracting bits.
   Solution: Ensure your mask covers exactly the bits you want to extract.

   Example:
   def extract_bits(number, start, length):
       mask = (1 << length) - 1
       return (number >> start) & mask

   num = 0b11001010
   print(f"Extracted bits 2-4: {bin(extract_bits(num, 2, 3))}")

3. Overflowing when shifting:
   Problem: Left-shifting beyond the integer size causes unexpected results.
   Solution: Be aware of the maximum integer size on your system and use 
   appropriate data types or libraries for larger numbers.

   Example:
   def safe_left_shift(number, shift):
       if shift >= number.bit_length():
           return 0
       return number << shift

   num = 1 << 63  # On a 64-bit system
   print(f"Safe left shift by 1: {safe_left_shift(num, 1)}")
   print(f"Safe left shift by 64: {safe_left_shift(num, 64)}")

4. Forgetting operator precedence:
   Problem: Unexpected results due to incorrect operator precedence.
   Solution: Use parentheses to explicitly define the order of operations.

   Example:
   a = 5
   b = 3
   c = 2
   result1 = a | b & c  # Incorrect: & has higher precedence than |
   result2 = (a | b) & c  # Correct: use parentheses to specify order
   print(f"Without parentheses: {result1}")
   print(f"With parentheses: {result2}")

7. Recommended Tools, Libraries, and Resources
==============================================
Tools and Libraries:
1. bitstring: A Python module for creation and analysis of binary data
   (https://github.com/scott-griffiths/bitstring)
2. bitarray: Efficient arrays of booleans
   (https://github.com/ilanschnell/bitarray)
3. gmpy2: Multiprecision arithmetic
   (https://github.com/aleaxit/gmpy)
4. NumPy: For efficient bitwise operations on arrays
   (https://numpy.org/)

Resources:
1. Python documentation on Bitwise Operators:
   https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
2. "Bit Twiddling Hacks" by Sean Eron Anderson:
   https://graphics.stanford.edu/~seander/bithacks.html
3. "Hacker's Delight" by Henry S. Warren Jr. (Book)
4. "Python Cookbook" by David Beazley and Brian K. Jones (Book)

8. Performance Analysis and Optimization
========================================
Profiling bitwise operations:

import timeit

def profile_bitwise_vs_arithmetic():
    setup = "import random; a = random.randint(1, 1000000)"
    
    bitwise_and = timeit.timeit("a & 1", setup=setup, number=1000000)
    modulo = timeit.timeit("a % 2", setup=setup, number=1000000)
    
    bitwise_shift = timeit.timeit("a >> 1", setup=setup, number=1000000)
    division = timeit.timeit("a // 2", setup=setup, number=1000000)
    
    print(f"Bitwise AND vs Modulo:")
    print(f"Bitwise AND: {bitwise_and:.6f} seconds")
    print(f"Modulo: {modulo:.6f} seconds")
    print(f"Speedup: {modulo/bitwise_and:.2f}x\n")
    
    print(f"Bitwise Shift vs Division:")
    print(f"Bitwise Shift: {bitwise_shift:.6f} seconds")
    print(f"Division: {division:.6f} seconds")
    print(f"Speedup: {division/bitwise_shift:.2f}x")

profile_bitwise_vs_arithmetic()

Optimization strategies:
1. Use bitwise operations instead of arithmetic operations when possible, 
   especially for powers of 2.
2. Combine multiple bitwise operations into a single operation when possible.
3. Use lookup tables for complex bit manipulations that are frequently performed.
4. Consider using NumPy for large-scale bitwise operations on arrays.

Example of optimizing a popcount (count of set bits) function:

def popcount_naive(n):
    return bin(n).count('1')

def popcount_optimized(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def popcount_lookup(n):
    lookup = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    count = 0
    while n:
        count += lookup[n & 0xF]
        n >>= 4
    return count

import timeit

n = 0xFFFFFFFF  # 32-bit all ones

naive_time = timeit.timeit(lambda: popcount_naive(n), number=100000)
optimized_time = timeit.timeit(lambda: popcount_optimized(n), number=100000)
lookup_time = timeit.timeit(lambda: popcount_lookup(n), number=100000)

print(f"Naive implementation: {naive_time:.6f} seconds")
print(f"Optimized implementation: {optimized_time:.6f} seconds")
print(f"Lookup table implementation: {lookup_time:.6f} seconds")

9. How to Contribute
====================
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

When adding new sections or expanding existing ones, consider:
- The relevance to bitwise operations in Python
- The depth of explanation required for expert-level understanding
- The practical applications of the concept in real-world scenarios
- The potential impact on performance and optimization

Your contributions will help keep this note sheet up-to-date and valuable for 
Python developers at all levels. Thank you for your interest in improving this 
resource!
"""

# This is the main function that demonstrates the usage of bitwise operators
def main():
    print("Bitwise Operators in Python - Expert-Level Note Sheet")
    print("====================================================")
    
    # Call the demonstration functions
    bitwise_and_demo()
    bitwise_or_demo()
    bitwise_xor_demo()
    bitwise_not_demo()
    bitwise_shift_demo()
    
    print("\nPerformance Benchmarking:")
    bitwise_operations_benchmark()
    
    print("\nTroubleshooting Examples:")
    # Unexpected results with negative numbers
    num = -5
    print(f"Binary representation of {num}: {num:032b}")
    print(f"After right shift by 1: {num >> 1:032b}")
    
    # Incorrect masking
    num = 0b11001010
    print(f"Extracted bits 2-4: {bin(extract_bits(num, 2, 3))}")
    
    # Overflowing when shifting
    num = 1 << 63  # On a 64-bit system
    print(f"Safe left shift by 1: {safe_left_shift(num, 1)}")
    print(f"Safe left shift by 64: {safe_left_shift(num, 64)}")
    
    # Forgetting operator precedence
    a, b, c = 5, 3, 2
    print(f"Without parentheses: {a | b & c}")
    print(f"With parentheses: {(a | b) & c}")
    
    print("\nPerformance Analysis:")
    profile_bitwise_vs_arithmetic()
    
    print("\nPopcount Optimization:")
    n = 0xFFFFFFFF  # 32-bit all ones
    naive_time = timeit.timeit(lambda: popcount_naive(n), number=100000)
    optimized_time = timeit.timeit(lambda: popcount_optimized(n), number=100000)
    lookup_time = timeit.timeit(lambda: popcount_lookup(n), number=100000)
    print(f"Naive implementation: {naive_time:.6f} seconds")
    print(f"Optimized implementation: {optimized_time:.6f} seconds")
    print(f"Lookup table implementation: {lookup_time:.6f} seconds")

if __name__ == "__main__":
    main()