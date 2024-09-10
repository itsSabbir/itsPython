# Python Cheat Sheet: Operators

# 1. Arithmetic Operators

a, b = 10, 3

# Addition
print(f"a + b = {a + b}")  # Output: 13

# Subtraction
print(f"a - b = {a - b}")  # Output: 7

# Multiplication
print(f"a * b = {a * b}")  # Output: 30

# Division (always returns a float)
print(f"a / b = {a / b}")  # Output: 3.3333333333333335

# Floor Division (returns the largest integer less than or equal to the result)
print(f"a // b = {a // b}")  # Output: 3

# Modulus (remainder)
print(f"a % b = {a % b}")  # Output: 1

# Exponentiation
print(f"a ** b = {a ** b}")  # Output: 1000

# Negation
print(f"-a = {-a}")  # Output: -10

# Tip: Use parentheses to control the order of operations
print(f"(a + b) * 2 = {(a + b) * 2}")  # Output: 26

# 2. Comparison Operators

x, y = 5, 10

# Equal to
print(f"x == y: {x == y}")  # Output: False

# Not equal to
print(f"x != y: {x != y}")  # Output: True

# Greater than
print(f"x > y: {x > y}")  # Output: False

# Less than
print(f"x < y: {x < y}")  # Output: True

# Greater than or equal to
print(f"x >= y: {x >= y}")  # Output: False

# Less than or equal to
print(f"x <= y: {x <= y}")  # Output: True

# Identity comparison (checks if objects are the same)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")  # Output: False
print(f"list1 is list3: {list1 is list3}")  # Output: True
print(f"list1 is not list2: {list1 is not list2}")  # Output: True

# 3. Logical Operators

p, q = True, False

# AND
print(f"p and q: {p and q}")  # Output: False

# OR
print(f"p or q: {p or q}")  # Output: True

# NOT
print(f"not p: {not p}")  # Output: False

# Example with multiple conditions
x = 5
print(f"0 < x < 10: {0 < x < 10}")  # Output: True

# Short-circuit evaluation
def true_func():
    print("This is executed")
    return True

def false_func():
    print("This is not executed")
    return False

result = true_func() or false_func()
print(f"Result of short-circuit OR: {result}")  # Output: True

result = false_func() and true_func()
print(f"Result of short-circuit AND: {result}")  # Output: False

# 4. Bitwise Operators

m, n = 60, 13  # 60 = 0011 1100, 13 = 0000 1101 in binary

# Bitwise AND
print(f"m & n: {m & n}")  # Output: 12 (0000 1100)

# Bitwise OR
print(f"m | n: {m | n}")  # Output: 61 (0011 1101)

# Bitwise XOR
print(f"m ^ n: {m ^ n}")  # Output: 49 (0011 0001)

# Bitwise NOT
print(f"~m: {~m}")  # Output: -61 (1100 0011)

# Left shift
print(f"m << 2: {m << 2}")  # Output: 240 (1111 0000)

# Right shift
print(f"m >> 2: {m >> 2}")  # Output: 15 (0000 1111)

# 5. Membership Operators

fruits = ["apple", "banana", "cherry"]

# in
print(f"'banana' in fruits: {'banana' in fruits}")  # Output: True

# not in
print(f"'grape' not in fruits: {'grape' not in fruits}")  # Output: True

# Membership operators work with strings, lists, tuples, and other sequences
print(f"'a' in 'apple': {'a' in 'apple'}")  # Output: True

# 6. Assignment Operators

a = 10

# Addition assignment
a += 5  # Equivalent to: a = a + 5
print(f"a after +=: {a}")  # Output: 15

# Subtraction assignment
a -= 3  # Equivalent to: a = a - 3
print(f"a after -=: {a}")  # Output: 12

# Multiplication assignment
a *= 2  # Equivalent to: a = a * 2
print(f"a after *=: {a}")  # Output: 24

# Division assignment
a /= 4  # Equivalent to: a = a / 4
print(f"a after /=: {a}")  # Output: 6.0

# Floor division assignment
a //= 2  # Equivalent to: a = a // 2
print(f"a after //=: {a}")  # Output: 3.0

# Modulus assignment
a %= 2  # Equivalent to: a = a % 2
print(f"a after %=: {a}")  # Output: 1.0

# Exponentiation assignment
a **= 3  # Equivalent to: a = a ** 3
print(f"a after **=: {a}")  # Output: 1.0

# Bitwise AND assignment
b = 60
b &= 13
print(f"b after &=: {b}")  # Output: 12

# Bitwise OR assignment
b |= 13
print(f"b after |=: {b}")  # Output: 13

# Bitwise XOR assignment
b ^= 60
print(f"b after ^=: {b}")  # Output: 49

# 7. Operator Precedence

# Python follows the PEMDAS rule (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
result = 2 + 3 * 4 ** 2 - 6 / 2
print(f"2 + 3 * 4 ** 2 - 6 / 2 = {result}")  # Output: 47.0

# Use parentheses to make your code more readable and to ensure the intended order of operations
result = ((2 + 3) * 4 ** 2) - (6 / 2)
print(f"((2 + 3) * 4 ** 2) - (6 / 2) = {result}")  # Output: 77.0

# 8. Ternary Operator (Conditional Expression)

x = 10
y = 20
max_value = x if x > y else y
print(f"Max value of {x} and {y} is: {max_value}")  # Output: 20

# Nested ternary operator (use sparingly for readability)
a, b, c = 3, 5, 1
max_of_three = a if a > b and a > c else (b if b > c else c)
print(f"Max of {a}, {b}, and {c} is: {max_of_three}")  # Output: 5

# 9. Walrus Operator := (Python 3.8+)

# The walrus operator := allows you to assign values to variables as part of a larger expression

# Without walrus operator
numbers = [1, 2, 3, 4, 5]
n = len(numbers)
if n > 2:
    print(f"The list has {n} items, which is more than 2")

# With walrus operator
if (n := len(numbers)) > 2:
    print(f"The list has {n} items, which is more than 2")

# Example in a while loop
while (user_input := input("Enter a number (or 'q' to quit): ")) != 'q':
    print(f"You entered: {user_input}")

# 10. Advanced Operator Usage

# Using operators with different types
print(f"'Na' * 2 + ' Batman!': {'Na' * 2 + ' Batman!'}")  # Output: NaNa Batman!

# List repetition
print(f"[1, 2] * 3: {[1, 2] * 3}")  # Output: [1, 2, 1, 2, 1, 2]

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"set1 | set2 (union): {set1 | set2}")
print(f"set1 & set2 (intersection): {set1 & set2}")
print(f"set1 - set2 (difference): {set1 - set2}")
print(f"set1 ^ set2 (symmetric difference): {set1 ^ set2}")

# Using 'in' with dictionaries
person = {'name': 'Alice', 'age': 30}
print(f"'name' in person: {'name' in person}")  # Output: True
print(f"'gender' in person: {'gender' in person}")  # Output: False

# This concludes the detailed Python Cheat Sheet for Operators