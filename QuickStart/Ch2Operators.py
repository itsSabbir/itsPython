#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Notes Sheet: Operators
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#===============================================================================
# 1. Arithmetic Operators
#===============================================================================

# Assigning values 10 and 3 to variables a and b
a, b = 10, 3

# Addition: Adds the values of a and b
# Basic operation but crucial in many algorithms, especially in accumulative sums
print(f"a + b = {a + b}")  # Output: 13

# Subtraction: Subtracts b from a
# Frequently used in algorithms to determine differences or deltas between values
print(f"a - b = {a - b}")  # Output: 7

# Multiplication: Multiplies a by b
# Foundational in scaling, area calculations, or when working with coefficients in equations
print(f"a * b = {a * b}")  # Output: 30

# Division: Divides a by b, always returns a float, even if a and b are integers
# Be cautious with division as it may introduce floating-point inaccuracies due to precision limits
print(f"a / b = {a / b}")  # Output: 3.3333333333333335

# Floor Division: Divides a by b and returns the largest integer less than or equal to the result
# Useful when an exact integer quotient is required (e.g., splitting items into groups)
# Common pitfall: Forgetting it truncates towards negative infinity, not zero, which affects results with negative numbers
print(f"a // b = {a // b}")  # Output: 3

# Modulus: Returns the remainder when a is divided by b
# Handy for determining if a number is even/odd (num % 2), or implementing cyclical behavior (e.g., circular arrays)
print(f"a % b = {a % b}")  # Output: 1

# Exponentiation: Raises a to the power of b
# Extremely important in mathematical, scientific calculations, and in algorithmic growth analysis (e.g., O(n^2))
# Be cautious with large exponents as they can quickly lead to overflow errors in certain data types
print(f"a ** b = {a ** b}")  # Output: 1000

# Negation: Changes the sign of a
# Often used in algorithms to reverse direction, apply transformations, or handle debts/negative values in financial calculations
print(f"-a = {-a}")  # Output: -10

# Tip: Use parentheses to control the order of operations
# Without parentheses, multiplication/division have higher precedence than addition/subtraction
# Here, (a + b) ensures the addition happens first, then multiplies by 2
print(f"(a + b) * 2 = {(a + b) * 2}")  # Output: 26

# Additional Examples

# Multiplication combined with addition, showcasing operation precedence
print(f"a * b + 5 = {a * b + 5}")  # Output: 35
# Note: Multiplication executes before addition

# Division by zero scenario: Uncommenting will raise a ZeroDivisionError
# Always validate or handle division to avoid runtime errors
# print(f"a / 0 = {a / 0}")  # Raises ZeroDivisionError

# Working with negative numbers
c = -5
print(f"b + c = {b + c}")  # Output: -2
# When combining positive and negative numbers, ensure to track signs carefully, especially in financial or physics calculations

# Complex operations combining several arithmetic operators
print(f"a * b - c / b + a % b = {a * b - c / b + a % b}")  # Output: 32.333333333333336
# Key points: Multiplication and division have higher precedence, so they are executed before addition/subtraction

# Floating-point precision example: Small inaccuracies may arise with floats
d = 0.1 + 0.2
print(f"0.1 + 0.2 = {d}")  # Output might be 0.30000000000000004 instead of 0.3
# Advanced Insight: This occurs due to the binary representation of floating-point numbers; always be aware of this when high precision is crucial

#===============================================================================
# 2. Comparison Operators
#===============================================================================

# Here, two variables x and y are assigned the values 5 and 10 respectively.
x, y = 5, 10

# '==' checks if the values of x and y are equal.
# This is a strict comparison: both values and types must be identical.
# Advanced tip: This operation is fundamental but can lead to subtle issues
# in cases where type coercion occurs in dynamically typed languages (not in Python).
print(f"x == y: {x == y}")  # Output: False, because 5 is not equal to 10

# '!=' checks if the values of x and y are not equal.
# Advanced tip: In certain situations, refactoring multiple '==' checks into '!=' 
# can reduce code complexity and prevent hard-to-trace logic errors.
print(f"x != y: {x != y}")  # Output: True, because 5 is not equal to 10

# '>' checks if x is strictly greater than y.
# This comparison only evaluates the numeric values, not the type or identity.
# Pitfall: Be cautious when comparing objects that override these operators (like custom classes).
print(f"x > y: {x > y}")  # Output: False, since 5 is not greater than 10

# '<' checks if x is strictly less than y.
# This is an intuitive comparison for numerical values but can behave differently for other data types like strings.
# Advanced tip: When comparing strings or other iterable objects, '<' is based on lexicographical ordering.
print(f"x < y: {x < y}")  # Output: True, because 5 is less than 10

# '>=' checks if x is greater than or equal to y.
# Like '>', but it also accounts for equality.
# Best practice: Use '>=' instead of a combination of '>' and '==', as it's more concise and efficient.
print(f"x >= y: {x >= y}")  # Output: False, since 5 is neither greater than nor equal to 10

# '<=' checks if x is less than or equal to y.
# Similar to '<', but also includes equality.
# Advanced tip: This operator is helpful when dealing with ranges or boundaries in algorithms.
print(f"x <= y: {x <= y}")  # Output: True, since 5 is less than 10

# Identity comparison using 'is'. This checks whether two objects refer to the same memory location.
# Here, list1 and list2 are separate objects, despite having the same content.
# Best practice: Use 'is' to check identity when object uniqueness is crucial (e.g., Singleton pattern).
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# 'is' checks if both operands refer to the exact same object in memory.
# Pitfall: Even though list1 and list2 contain the same elements, they are different objects in memory.
print(f"list1 is list2: {list1 is list2}")  # Output: False, since they are two different objects

# list3 is assigned to list1, meaning both variables point to the same object.
# This makes 'is' return True because both point to the same memory address.
print(f"list1 is list3: {list1 is list3}")  # Output: True, because they refer to the same object

# 'is not' checks the opposite of 'is', verifying if two objects do not share the same identity.
# Since list1 and list2 are different objects, 'is not' will return True.
# Advanced insight: Use 'is not' judiciously to highlight intentional differences in object identity.
print(f"list1 is not list2: {list1 is not list2}")  # Output: True, because list1 and list2 are different objects

#===============================================================================
# 3. Logical Operators
#===============================================================================
# Logical operators are used to combine or manipulate boolean values (True, False). 
# They are essential for making decisions and controlling the flow of a program.
# Python includes three primary logical operators: AND, OR, and NOT.
# Logical operators also support "short-circuit" evaluation, where evaluation stops as soon as the result is determined.

# Defining two boolean variables p and q for use in logical expressions
p, q = True, False

# AND
# The 'and' operator returns True only if both operands are True.
# If either operand is False, the result is False.
# This is useful when all conditions must be satisfied for an expression to be True.
print(f"p and q: {p and q}")  # Output: False (because q is False)

# OR
# The 'or' operator returns True if at least one operand is True.
# It only returns False when both operands are False.
# This is useful when at least one condition being True satisfies the expression.
print(f"p or q: {p or q}")  # Output: True (because p is True)

# NOT
# The 'not' operator inverts the boolean value. 
# It returns True if the operand is False, and False if the operand is True.
# This is commonly used when we need to check if something is *not* true.
print(f"not p: {not p}")  # Output: False (because p is True, so not p is False)

# Example with multiple conditions
# Python allows chaining of comparison operators in a single expression.
# This is an elegant way to check if a value falls within a certain range.
# The expression "0 < x < 10" is equivalent to "0 < x and x < 10", 
# but more concise and easier to read.
x = 5
print(f"0 < x < 10: {0 < x < 10}")  # Output: True (because x is between 0 and 10)

# Short-circuit evaluation
# Python uses short-circuit evaluation for logical expressions involving 'and' and 'or'.
# This means the second operand is only evaluated if the first operand does not determine the result.
# This can be leveraged to avoid unnecessary computations or function calls.

# Defining two functions to demonstrate short-circuit behavior

# true_func always returns True and prints a message to show it was executed.
def true_func():
    print("This is executed")
    return True

# false_func always returns False and prints a message to show if it was executed.
def false_func():
    print("This is not executed")
    return False

# In 'or' expressions, if the first operand is True, the result is True regardless of the second operand.
# Therefore, the second function (false_func) is not called, optimizing performance.
result = true_func() or false_func()  # Short-circuit OR: false_func() is never called.
print(f"Result of short-circuit OR: {result}")  # Output: True (because true_func() returns True)

# In 'and' expressions, if the first operand is False, the result is False regardless of the second operand.
# Hence, the second function (true_func) is not called.
result = false_func() and true_func()  # Short-circuit AND: true_func() is never called.
print(f"Result of short-circuit AND: {result}")  # Output: False (because false_func() returns False)

# Advanced Tip: Short-circuit evaluation is especially useful in expressions that involve 
# expensive operations or functions with side effects, as it avoids unnecessary execution.
# However, be mindful when functions with side effects (like printing or I/O operations) are involved,
# since short-circuiting can prevent those operations from taking place if they are part of the skipped expression.

# 4. Bitwise Operators in Python

# The values of 'm' and 'n' are assigned integers 60 and 13 respectively.
# In binary, 60 is represented as 0011 1100 and 13 is represented as 0000 1101.
# Understanding binary representation is crucial in bitwise operations as they operate at the bit level.

m, n = 60, 13  # Initializing 'm' and 'n' with decimal values 60 and 13.

# Bitwise AND (&) - compares each bit of two numbers.
# It returns 1 only if both corresponding bits are 1, otherwise, it returns 0.
# Example: 60 (0011 1100) & 13 (0000 1101) results in 0000 1100, which is 12 in decimal.
# Common use case: Masking operations where you need to isolate certain bits.
print(f"m & n: {m & n}")  # Output will be 12, as only the last 4 bits are set in both numbers.

# Bitwise OR (|) - compares each bit of two numbers.
# It returns 1 if at least one of the corresponding bits is 1, otherwise, it returns 0.
# Example: 60 (0011 1100) | 13 (0000 1101) results in 0011 1101, which is 61 in decimal.
# Practical usage: Used to set specific bits in a number.
print(f"m | n: {m | n}")  # Output will be 61, since it combines the bits that are set in either number.

# Bitwise XOR (^) - compares each bit of two numbers.
# It returns 1 if only one of the corresponding bits is 1 (exclusive OR), otherwise, it returns 0.
# Example: 60 (0011 1100) ^ 13 (0000 1101) results in 0011 0001, which is 49 in decimal.
# Advanced tip: XOR is often used in cryptography or to swap values without a temporary variable.
print(f"m ^ n: {m ^ n}")  # Output will be 49, where bits differ between 'm' and 'n'.

# Bitwise NOT (~) - inverts all the bits of the number.
# It flips each bit: 0 becomes 1, and 1 becomes 0.
# The result is the two's complement of the original value, so ~60 (0011 1100) becomes -61 (in binary: 1100 0011).
# Pitfall: Be aware that bitwise NOT can produce negative numbers due to the way Python handles integers (using two's complement).
print(f"~m: {~m}")  # Output will be -61, as Python uses signed integers with two's complement representation.

# Left Shift (<<) - shifts the bits of the number to the left by a specified number of positions.
# Example: Shifting 60 (0011 1100) left by 2 positions results in 1111 0000, which is 240 in decimal.
# Shifting left by 'n' is equivalent to multiplying by 2^n. 
# Important: Ensure the shift count doesn’t exceed the number of bits in use, as this could lead to unexpected behavior in some languages (though Python handles this with arbitrary-length integers).
print(f"m << 2: {m << 2}")  # Output will be 240, shifting bits of 'm' (60) left by 2 positions.

# Right Shift (>>) - shifts the bits of the number to the right by a specified number of positions.
# Example: Shifting 60 (0011 1100) right by 2 positions results in 0000 1111, which is 15 in decimal.
# Shifting right by 'n' is equivalent to dividing by 2^n and flooring the result.
# Pitfall: With negative numbers, right shifts preserve the sign bit (arithmetic shift), which can lead to unexpected results when dealing with signed integers.
print(f"m >> 2: {m >> 2}")  # Output will be 15, shifting bits of 'm' (60) right by 2 positions.

# Summary:
# Bitwise operators are fast, low-level operations that are useful for tasks like data encoding, cryptography, or performance-critical systems.
# Advanced tip: In applications where performance is crucial (like embedded systems or high-performance computing), bitwise operations are preferred because of their efficiency.

#===============================================================================
# 5. Membership Operators
#===============================================================================

# Membership operators (`in`, `not in`) are used to check if a value exists within a sequence like a list, tuple, or string.
# These operators return a boolean value (`True` or `False`) based on whether the value is found.
# They are often used for conditions and are more readable than manually iterating through the sequence.

fruits = ["apple", "banana", "cherry"]  # Example list of fruits, containing 3 items.

# The `in` operator checks if a value is present in the sequence (in this case, the list of fruits).
# If 'banana' exists in the `fruits` list, this will return `True`.
print(f"'banana' in fruits: {'banana' in fruits}")  # Output: True
# Advanced note: Under the hood, this operation performs a linear search (O(n)) through the list, 
# meaning the time complexity grows as the list becomes larger. However, for short lists, this is usually efficient enough.

# The `not in` operator checks if a value is *not* present in the sequence.
# In this case, since 'grape' is not part of the `fruits` list, it will return `True`.
print(f"'grape' not in fruits: {'grape' not in fruits}")  # Output: True
# Advanced tip: Just like `in`, `not in` also performs a linear search. 
# For performance-critical applications, especially with large datasets, consider using sets or dictionaries 
# where membership tests are significantly faster (average time complexity O(1)).

# Membership operators can also be used with strings to check if a substring exists within a string.
# Here, we check if the character 'a' is present in the string 'apple'. Since 'a' exists in 'apple', it returns `True`.
print(f"'a' in 'apple': {'a' in 'apple'}")  # Output: True
# Advanced insight: For strings, membership testing with `in` or `not in` operates similarly to list searches, 
# but it searches the characters in sequence. Python's string implementation optimizes this for short strings,
# but longer or more complex string searches might benefit from regular expressions for flexibility.

# Best practice: While membership operators are convenient, be cautious about their use in performance-sensitive
# code, especially when dealing with very large sequences. For frequently accessed large collections, using sets
# or dicts for membership testing provides constant-time lookups instead of linear-time lookups in lists.

#===============================================================================
# 6. Assignment Operators
#===============================================================================

# These operators allow for modifying variables in place,
# reducing code verbosity and improving readability. They work by performing the operation
# on the right-hand side and assigning the result back to the left-hand side variable.
# Useful for concise code when applying repetitive operations.

# Initialize a variable with an integer value
a = 10  # `a` is assigned the value 10.

# Addition assignment
a += 5  # Equivalent to: a = a + 5. Increments `a` by 5.
print(f"a after +=: {a}")  # Output: 15. Efficient for adding a value to `a` in place.

# Subtraction assignment
a -= 3  # Equivalent to: a = a - 3. Decreases `a` by 3.
print(f"a after -=: {a}")  # Output: 12. Preferred for quick decrement operations.

# Multiplication assignment
a *= 2  # Equivalent to: a = a * 2. Multiplies `a` by 2.
print(f"a after *=: {a}")  # Output: 24. Can handle large values but watch for overflow in constrained environments.

# Division assignment
a /= 4  # Equivalent to: a = a / 4. Divides `a` by 4.
print(f"a after /=: {a}")  # Output: 6.0. Converts `a` to a float, as `/` returns a float type.

# Floor division assignment
a //= 2  # Equivalent to: a = a // 2. Performs integer (floor) division.
print(f"a after //=: {a}")  # Output: 3.0. Keeps `a` as a float since it was a float previously.

# Modulus assignment
a %= 2  # Equivalent to: a = a % 2. Computes the remainder of `a` divided by 2.
print(f"a after %=: {a}")  # Output: 1.0. Useful for determining if `a` is even or odd.

# Exponentiation assignment
a **= 3  # Equivalent to: a = a ** 3. Raises `a` to the power of 3.
print(f"a after **=: {a}")  # Output: 1.0. Efficient for repeated multiplication. Watch for very large numbers with high exponents.

# Now switching to bitwise assignment operators, often used in low-level programming and optimizations:

# Bitwise AND assignment
# `b` is initialized with a value of 60 (binary: 111100)
b = 60

# Bitwise AND operation: 60 & 13 (binary: 00001101)
b &= 13  # Equivalent to: b = b & 13. The result is 12 (binary: 00001100).
print(f"b after &=: {b}")  # Output: 12. Keeps only bits set in both `b` and 13.

# Bitwise OR assignment
# OR operation between 12 (binary: 00001100) and 13 (binary: 00001101)
b |= 13  # Equivalent to: b = b | 13. The result is 13 (binary: 00001101).
print(f"b after |=: {b}")  # Output: 13. Sets bits that are in `b` or 13.

# Bitwise XOR assignment
# XOR between 13 (binary: 00001101) and 60 (binary: 111100)
b ^= 60  # Equivalent to: b = b ^ 60. The result is 49 (binary: 00110001).
print(f"b after ^=: {b}")  # Output: 49. Sets bits that are different between `b` and 60.

# Advanced Notes:
# 1. Compound assignment operators are not just syntactic sugar—they can be more efficient.
#    Some operations use less memory or require fewer steps when used with assignments.
# 2. Be cautious when using `/=` with integer values, as it will convert the type to float, which might lead to unexpected results.
# 3. In bitwise operations, understand binary representations to predict outcomes. Bitwise AND (`&`), OR (`|`), and XOR (`^`) have distinct uses:
#    - AND (`&`) clears bits.
#    - OR (`|`) sets bits.
#    - XOR (`^`) toggles bits.

#===============================================================================
# 7. Operator Precedence
#===============================================================================

# Python follows the PEMDAS rule (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
result = 2 + 3 * 4 ** 2 - 6 / 2
print(f"2 + 3 * 4 ** 2 - 6 / 2 = {result}")  # Output: 47.0

# Use parentheses to make your code more readable and to ensure the intended order of operations
result = ((2 + 3) * 4 ** 2) - (6 / 2)
print(f"((2 + 3) * 4 ** 2) - (6 / 2) = {result}")  # Output: 77.0

#===============================================================================
# 8. Ternary Operator (Conditional Expression)
#===============================================================================

# Example 1: Basic Ternary Operator Usage
x = 10
y = 20

# The ternary operator is a compact way of writing an if-else statement.
# Here, the condition checks if x is greater than y. If the condition is true, 
# 'x' is assigned to max_value; otherwise, 'y' is assigned.
max_value = x if x > y else y

# Best practice: Ternary operators are useful for concise, simple conditions.
# However, they can hurt readability if overused or nested too deeply.
# In this case, we print the maximum value between x and y.
print(f"Max value of {x} and {y} is: {max_value}")  # Output: 20

# Advanced insight:
# For larger, more complex conditions, it's better to use standard if-else 
# blocks for clarity. Ternary operators should be used in cases where the logic
# is simple and fits within one line without compromising readability.

#===============================================================================
# Example 2: Nested Ternary Operator (Use Sparingly for Readability)
#===============================================================================

a, b, c = 3, 5, 1

# This nested ternary operator finds the maximum value among three numbers (a, b, and c).
# First, it checks if 'a' is greater than both 'b' and 'c'. If true, 'a' is assigned
# as max_of_three. If false, it checks if 'b' is greater than 'c'. If true, 'b' is assigned,
# otherwise 'c' is assigned as the maximum.
max_of_three = a if a > b and a > c else (b if b > c else c)

# This is a compact way of finding the maximum of three values, but it comes at the cost 
# of readability due to the nested ternary operator.
print(f"Max of {a}, {b}, and {c} is: {max_of_three}")  # Output: 5

# Best practice:
# Nested ternary operators can be difficult to read and maintain. In most cases, 
# using a more explicit if-else structure improves clarity, especially for beginners 
# or in teams where code readability is highly valued.

# Advanced insight:
# Python's built-in 'max()' function is typically more readable and efficient for 
# determining the maximum of multiple values.
# For example, the above expression can be rewritten as:
# max_of_three = max(a, b, c)

# While nested ternary operators are syntactically valid, they can obscure logic 
# and increase cognitive load. Refactoring into a clearer form is usually preferred, 
# particularly in complex projects.


#===============================================================================
# 9. Walrus Operator := (Python 3.8+)
#===============================================================================

# The walrus operator := was introduced in Python 3.8 and is a new syntax feature that allows 
# assignments to occur within expressions, which can help to make code more concise and readable.
# It can be especially useful in scenarios where a variable is needed in both an expression 
# and later in the code. 

# This operator can often reduce redundancy, particularly when the same expression 
# would otherwise need to be computed twice. It combines assignment and evaluation 
# in a single line, but should be used judiciously to maintain readability.

# A common mistake when using the walrus operator is that it can reduce code clarity 
# if overused or applied in complex expressions. Readability is still a key principle 
# in Pythonic code, so it's important to ensure that the walrus operator isn't over-applied 
# in situations where it might obscure the flow of logic.

# Below are examples showing both without and with the walrus operator.

# Without walrus operator
numbers = [1, 2, 3, 4, 5]  # A simple list of numbers
n = len(numbers)  # 'len()' is used to get the length of the list and assign it to 'n'
if n > 2:  # Standard comparison; check if 'n' is greater than 2
    print(f"The list has {n} items, which is more than 2")  
    # Output the result, using 'n' directly

# With walrus operator
if (n := len(numbers)) > 2:  # The walrus operator allows assignment within the 'if' condition
    print(f"The list has {n} items, which is more than 2")  
    # This prints the same result, but here 'n' is assigned and evaluated in a single step
    # The advantage is that 'len(numbers)' is only called once, reducing redundancy in the code

# Example in a while loop
# A more typical use case for the walrus operator is in loops, especially 'while' loops,
# where an expression is evaluated repeatedly. Here, we reduce redundancy by capturing the
# value from 'input()' directly in the loop condition, avoiding the need for a separate line.

# This loop will continue until the user types 'q' to quit
while (user_input := input("Enter a number (or 'q' to quit): ")) != 'q':
    # The 'input()' function is assigned to 'user_input' and evaluated in the same line.
    # If 'user_input' equals 'q', the loop will exit.
    print(f"You entered: {user_input}")
    # This prints what the user entered. The use of the walrus operator here simplifies
    # the code by avoiding an additional line of 'user_input = input()'.

# Advanced Insights:
# 1. Performance: The walrus operator can improve performance slightly by reducing redundant
#    calculations. For example, if 'len()' is expensive (in large datasets), the walrus operator
#    ensures it's called once instead of multiple times.

# 2. Common Pitfall: While the walrus operator can make code more concise, avoid using it in 
#    overly complex expressions. This can lead to code that's difficult to read and debug,
#    violating the principle of readability. Python's focus is on being explicit rather than implicit.

# 3. Practical Use Case: The walrus operator is particularly useful in list comprehensions, 
#    where it can be used to both filter and assign a value in one go, reducing clutter.
#    For example, filtering and computing the length of strings in a list:
strings = ["apple", "banana", "kiwi", "pear"]
filtered_lengths = [length for string in strings if (length := len(string)) > 4]
print(filtered_lengths)  # This will output the lengths of strings that have more than 4 characters.

# Here, the 'length' of each string is calculated once and reused both in the filtering condition 
# and the result list, enhancing efficiency without extra lines of code.

# 4. Debugging Tip: If you're unsure about whether a walrus operator might obscure the logic 
#    of your program, try writing the code without it first. If the code becomes significantly 
#    more readable by introducing the walrus operator, then it’s likely appropriate. 
#    Otherwise, stick with traditional assignment.

    
#===============================================================================
# 10. Advanced Operator Usage
#===============================================================================

# Using operators with different types
# Here, we use the '*' operator to repeat a string. In this case, the string 'Na' is 
# repeated twice, which is then concatenated with ' Batman!' using the '+' operator.
# String repetition with '*' is useful for tasks like generating patterns or mock data.
print(f"'Na' * 2 + ' Batman!': {'Na' * 2 + ' Batman!'}")  # Output: NaNa Batman!
# Tip: String multiplication is very efficient as Python internally optimizes this.

# List repetition
# The '*' operator also works with lists to repeat elements. This repeats the list [1, 2] 
# three times, creating a new list with six elements. 
# Use Case: Can be used to quickly initialize a list with repeating values.
print(f"[1, 2] * 3: {[1, 2] * 3}")  # Output: [1, 2, 1, 2, 1, 2]
# Advanced Tip: Be cautious when multiplying lists of mutable objects (e.g., lists of lists), 
# as changes to one instance may affect all copies due to reference sharing.

# Set operations
# Python sets support common mathematical set operations, which can be performed using 
# operators like '|', '&', '-', and '^'. 
# Use Case: These operations are commonly used in tasks involving membership tests and 
# finding differences or similarities between data sets.

# Union (|)
# Combines both sets and removes any duplicates. This is analogous to a logical OR.
# Best Practice: Useful for merging distinct items from multiple data sources.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"set1 | set2 (union): {set1 | set2}")  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (&)
# Returns only the elements found in both sets. This is analogous to a logical AND.
# Use Case: Helpful in scenarios where you need to filter shared items across sets.
print(f"set1 & set2 (intersection): {set1 & set2}")  # Output: {3, 4}

# Difference (-)
# Returns elements from the first set that are not present in the second set.
# Advanced Insight: Set operations are often more performant than list comprehensions 
# or other data structures for large data comparisons.
print(f"set1 - set2 (difference): {set1 - set2}")  # Output: {1, 2}

# Symmetric Difference (^)
# Returns elements present in either set, but not both (like XOR).
# Use Case: Useful for finding non-overlapping items in two sets.
print(f"set1 ^ set2 (symmetric difference): {set1 ^ set2}")  # Output: {1, 2, 5, 6}

# Using 'in' with dictionaries
# The 'in' operator checks for the presence of a key in a dictionary, which is much faster 
# than manually searching for keys. This is a common operation in Python due to dictionary 
# lookups being optimized to constant time O(1) in average cases.

# Here, we're checking if 'name' is a key in the 'person' dictionary, which returns True.
person = {'name': 'Sabbir', 'age': 30}
print(f"'name' in person: {'name' in person}")  # Output: True
# Checking if a non-existent key 'gender' is present will return False.
print(f"'gender' in person: {'gender' in person}")  # Output: False
# Advanced Tip: If you're unsure whether a key exists and want to access its value, 
# consider using the `.get()` method to avoid KeyError exceptions in case the key is absent.

# This concludes the detailed Python Cheat Sheet for Operators
# Remember: Operator overloading in Python makes code concise but can introduce subtle bugs 
# if types are not managed properly. Always validate data types before applying operations.
