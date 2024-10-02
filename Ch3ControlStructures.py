#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Control Structures
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Control structures dictate the flow of execution within the program. 
# They enable the program to make decisions and execute certain sections of code conditionally.

#=================================================================================
# 1. Conditional Statements
#=================================================================================

# if statement
# A simple if statement evaluates the condition and executes the indented block only if the condition is True.
x = 10  # Here, x is assigned a positive integer value
if x > 0:  # Condition: Checks if x is greater than 0
    print("x is positive")  # Output: "x is positive" will be printed since the condition is True

# Key insight:
# - The condition in an if statement must return a boolean value (True or False).
# - If x was a non-numeric type like a list or string, ">" could raise a TypeError, so it's crucial to validate types in more complex logic.

# if-else statement
y = -5  # y is initialized with a negative value
if y > 0:  # Condition: Checks if y is greater than 0
    print("y is positive")  # This will not be executed because y is negative
else:
    print("y is non-positive")  # Output: "y is non-positive" since y is less than or equal to zero

# Advanced tip:
# - The else block is optional, but it's good practice to include it when handling edge cases.
# - Best practice: Ensure that both branches of the if-else structure are equally likely to be executed for code readability.

# if-elif-else statement
z = 0  # Assigning z a value of zero for this case
if z > 0:  # Condition: Checks if z is greater than 0
    print("z is positive")
elif z < 0:  # Condition: Only evaluated if the first condition is False
    print("z is negative")
else:  # The final condition that will execute if all previous conditions are False
    print("z is zero")  # Output: "z is zero" because z equals 0

# Insight:
# - The elif clause allows checking multiple conditions in sequence.
# - The first true condition will trigger its block, and the rest will be skipped.
# - If none of the conditions are True, the else block is executed (optional).

# Nested if statements
num = 15  # Assigning a positive integer to num
if num >= 0:  # First condition checks if num is non-negative
    if num == 0:  # Nested condition: checks if num is exactly zero
        print("num is zero")  # This block won't be executed
    else:
        print("num is positive")  # Output: "num is positive" because num is greater than zero
else:
    print("num is negative")  # Will not be executed as the outer condition is True

# Advanced tip:
# - While nesting if statements is possible, deeply nested structures can be hard to read and maintain.
# - Consider using elif instead of nested if statements for cleaner code when multiple exclusive conditions are checked.

# Ternary operator (conditional expression)
# A more concise way to handle simple if-else logic.
a = 5  # Variable a is set to a positive integer
result = "positive" if a > 0 else "non-positive"  # Conditional expression: evaluates the condition and assigns based on the result
print(result)  # Output: "positive" because a is greater than 0

# Insight:
# - This single-line form of if-else is known as a "ternary operator" in Python.
# - It's ideal for cases where you need a simple decision-making structure with two outcomes.
# - Avoid overusing this for complex conditions, as it may reduce code clarity.

# Multiple conditions using logical operators
# Logical operators like 'and', 'or', and 'not' can be used to combine multiple conditions.
x, y = 5, 10  # Assigning values to x and y
if x > 0 and y < 20:  # Both conditions need to be True for the block to execute
    print("Both conditions are true")  # Output: "Both conditions are true" because both conditions evaluate to True

# Best practice:
# - Logical operators are short-circuit operators. For 'and', Python stops evaluating as soon as one condition is False.
# - Similarly, for 'or', Python stops evaluating if the first condition is True.
# - This short-circuiting behavior can optimize performance for expensive condition checks.

#=================================================================================
# 2. Loops
#=================================================================================

# for loop with range
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()  # Newline

# for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")  # Output: apple banana cherry
print()  # Newline

# for loop with enumerate (to get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# while loop
count = 0
while count < 5:
    print(count, end=" ")
    count += 1  # Output: 0 1 2 3 4
print()  # Newline

# Infinite loop (be careful!)
# while True:
#     print("This will run forever unless broken")

# 3. Loop Control Statements

# break: exits the loop
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # Output: 0 1 2 3 4
print()  # Newline

# continue: skips the rest of the current iteration
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")  # Output: 0 1 3 4
print()  # Newline

# pass: does nothing, used as a placeholder
for i in range(3):
    pass  # This loop will run but do nothing

# Tip: 'pass' is often used when you need a syntactically correct statement but don't want to execute any code

# 4. Nested Loops

# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})", end=" ")
    print()  # Newline
# Output:
# (0, 0) (0, 1)
# (1, 0) (1, 1)
# (2, 0) (2, 1)

# 5. Comprehensions

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")  # Output: [0, 1, 4, 9, 16]

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")  # Output: [0, 4, 16, 36, 64]

# Set comprehension
unique_lengths = {len(fruit) for fruit in fruits}
print(f"Unique lengths: {unique_lengths}")  # Output: {5, 6}

# Dictionary comprehension
char_count = {char: fruits.count(char) for char in "abc"}
print(f"Character count: {char_count}")  # Output: {'a': 3, 'b': 1, 'c': 1}

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")  # Output: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# 6. else clause in loops

# for-else
for i in range(5):
    if i == 10:  # This condition is never true
        break
    print(i, end=" ")
else:
    print("Loop completed normally")
# Output: 0 1 2 3 4 Loop completed normally

# while-else
count = 0
while count < 3:
    print(count, end=" ")
    count += 1
else:
    print("While loop completed normally")
# Output: 0 1 2 While loop completed normally

# Tip: The else clause in loops is rarely used but can be helpful in certain scenarios

# 7. Switch-Case Alternative (Python 3.10+)

def check_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(check_status(200))  # Output: OK
print(check_status(404))  # Output: Not Found
print(check_status(500))  # Output: Internal Server Error
print(check_status(302))  # Output: Unknown Status

# More complex pattern matching
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Exiting program"
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Result: {float(x) + float(y)}"
        case _:
            return "Invalid command"

print(process_command("quit"))  # Output: Exiting program
print(process_command("hello Alice"))  # Output: Hello, Alice!
print(process_command("add 5 3"))  # Output: Result: 8.0
print(process_command("invalid"))  # Output: Invalid command

# 8. Exception Handling

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple except blocks
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching multiple exceptions in one line
try:
    # Some risky operation
    pass
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")

# try-except-else-finally
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The result is: {result}")
finally:
    print("This will always execute.")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 120:
        raise ValueError("Age is too high.")

try:
    validate_age(150)
except ValueError as e:
    print(f"Invalid age: {e}")

# Custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught custom error: {e}")

# 9. Context Managers (with statement)

# File handling with context manager
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Custom context manager
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    try:
        yield "Resource"
    finally:
        print("Releasing resource")

with managed_resource() as resource:
    print(f"Using {resource}")

# Output:
# Acquiring resource
# Using Resource
# Releasing resource

# 10. Advanced Control Flow Techniques

# Short-circuit evaluation
x = 5
y = 10
result = x < y and print("x is less than y")  # Output: x is less than y

# Walrus operator := (Python 3.8+)
numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print(f"List has {n} items, which is more than 3")

# Function as control flow
def perform_operation(operation, x, y):
    operations = {
        'add': lambda: x + y,
        'subtract': lambda: x - y,
        'multiply': lambda: x * y,
        'divide': lambda: x / y if y != 0 else "Cannot divide by zero"
    }
    return operations.get(operation, lambda: "Invalid operation")()

print(perform_operation('add', 5, 3))  # Output: 8
print(perform_operation('divide', 10, 2))  # Output: 5.0
print(perform_operation('power', 2, 3))  # Output: Invalid operation

# This concludes the detailed Python Cheat Sheet for Control Structures