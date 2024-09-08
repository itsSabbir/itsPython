# Python Cheat Sheet: Control Structures

# 1. Conditional Statements

# if statement
x = 10
if x > 0:
    print("x is positive")  # Output: x is positive

# if-else statement
y = -5
if y > 0:
    print("y is positive")
else:
    print("y is non-positive")  # Output: y is non-positive

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")  # Output: z is zero

# Nested if statements
num = 15
if num >= 0:
    if num == 0:
        print("num is zero")
    else:
        print("num is positive")  # Output: num is positive
else:
    print("num is negative")

# Ternary operator (conditional expression)
a = 5
result = "positive" if a > 0 else "non-positive"
print(result)  # Output: positive

# Multiple conditions using logical operators
x, y = 5, 10
if x > 0 and y < 20:
    print("Both conditions are true")  # Output: Both conditions are true

# 2. Loops

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