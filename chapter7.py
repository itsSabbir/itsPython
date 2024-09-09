# Python Cheat Sheet: Exception Handling (Enhanced Detailed Version)

# 1. Basic Try-Except Block

def basic_try_except():
    try:
        x = 1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Cannot divide by zero!")

basic_try_except()  # Output: Cannot divide by zero!

# Tip: Always catch specific exceptions rather than using a bare except clause

# 2. Catching the Exception Object

def catch_exception_object():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")
        print(f"Error type: {type(e).__name__}")

catch_exception_object()
# Output:
# An error occurred: division by zero
# Error type: ZeroDivisionError

# Tip: Use 'as e' to get more information about the exception

# 3. Catching Multiple Exceptions

def multiple_exceptions():
    try:
        # This could raise different types of exceptions
        x = int(input("Enter a number: "))
        result = 10 / x
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

# Uncomment to test:
# multiple_exceptions()

# Tip: Order matters! Put more specific exceptions before general ones

# 4. Catching Multiple Exceptions in One Line

def multiple_exceptions_one_line():
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"An error occurred: {type(e).__name__} - {e}")

# Uncomment to test:
# multiple_exceptions_one_line()

# Tip: Use this when you want to handle multiple exceptions in the same way

# 5. Catching All Exceptions (use sparingly)

def catch_all():
    try:
        # Some risky operation
        x = 1 / 0
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")
    
catch_all()
# Output: An unexpected error occurred: ZeroDivisionError - division by zero

# Tip: Avoid using bare 'except:'. Always specify Exception or a more specific error

# 6. Else Clause

def try_except_else():
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"The result is: {result}")  # This runs if no exception occurs

# Uncomment to test:
# try_except_else()

# Tip: Use 'else' for code that should run only if no exception was raised

# 7. Finally Clause

def try_except_finally():
    try:
        f = open("example.txt", "r")
        # Perform some operations with the file
    except FileNotFoundError:
        print("The file was not found.")
    finally:
        try:
            f.close()
        except NameError:
            print("File was not opened successfully.")

try_except_finally()

# Tip: Use 'finally' for cleanup code that should always run, regardless of exceptions

# 8. Combining Else and Finally

def full_exception_handling():
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
        print("Execution completed.")

# Uncomment to test:
# full_exception_handling()

# Tip: This structure allows for complete control over the execution flow

# 9. Raising Exceptions

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 120:
        raise ValueError("Age is too high.")
    return age

def raising_exceptions():
    try:
        validate_age(150)
    except ValueError as e:
        print(f"Invalid age: {e}")

raising_exceptions()  # Output: Invalid age: Age is too high.

# Tip: Raise exceptions when you encounter invalid conditions in your functions

# 10. Re-raising Exceptions

def re_raising_exceptions():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Caught an error, re-raising...")
        raise  # Re-raises the last exception

try:
    re_raising_exceptions()
except ZeroDivisionError:
    print("Caught re-raised exception")

# Tip: Use this to handle an exception partially and let it propagate

# 11. Custom Exceptions

class CustomError(Exception):
    """A custom exception class"""
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def raise_custom_error():
    raise CustomError("This is a custom error", 500)

try:
    raise_custom_error()
except CustomError as e:
    print(f"Caught custom error: {e.message} (Error code: {e.error_code})")

# Tip: Create custom exceptions for application-specific error conditions

# 12. Exception Hierarchy

def exception_hierarchy():
    try:
        # Trying different exceptions
        # 1 / 0  # ZeroDivisionError
        # int('a')  # ValueError
        # open('nonexistent.txt')  # FileNotFoundError
        raise KeyboardInterrupt
    except ArithmeticError:
        print("Caught an arithmetic error")
    except ValueError:
        print("Caught a value error")
    except IOError:
        print("Caught an I/O error")
    except KeyboardInterrupt:
        print("Caught a keyboard interrupt")

exception_hierarchy()  # Output: Caught a keyboard interrupt

# Tip: Understanding the exception hierarchy helps in structuring your except blocks

# 13. Using assert Statements

def calculate_average(numbers):
    assert len(numbers) > 0, "List is empty"
    return sum(numbers) / len(numbers)

try:
    result = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Tip: Use assertions for debugging and to check conditions that should never occur

# 14. Context Managers for Exception Handling

from contextlib import contextmanager

@contextmanager
def managed_resource():
    try:
        # Resource acquisition
        print("Resource acquired")
        yield "Resource"
    except Exception as e:
        # Exception handling
        print(f"An error occurred: {e}")
    finally:
        # Resource release
        print("Resource released")

with managed_resource() as resource:
    print(f"Using {resource}")
    raise ValueError("Something went wrong")

# Tip: Context managers are great for resource management and cleanup

# 15. Chaining Exceptions (Python 3.3+)

def chain_exceptions():
    try:
        try:
            1 / 0
        except ZeroDivisionError as e:
            raise ValueError("Invalid operation") from e
    except ValueError as e:
        print(f"Caught: {e}")
        print(f"Original exception: {e.__cause__}")

chain_exceptions()

# Tip: Use exception chaining to provide more context about errors

# 16. Suppressing Exceptions (Python 3.3+)

def suppress_exception():
    try:
        try:
            1 / 0
        except ZeroDivisionError:
            raise ValueError("Invalid operation") from None
    except ValueError as e:
        print(f"Caught: {e}")
        print(f"Original exception: {e.__cause__}")

suppress_exception()

# Tip: Use 'from None' to suppress the original exception when raising a new one

# 17. Exception Groups (Python 3.11+)

from exceptiongroup import ExceptionGroup

def process_data(data):
    errors = []
    for item in data:
        try:
            # Process item
            if item < 0:
                raise ValueError(f"Negative value: {item}")
        except ValueError as e:
            errors.append(e)
    
    if errors:
        raise ExceptionGroup("Processing errors", errors)

try:
    process_data([1, -2, 3, -4])
except* ValueError as eg:
    print(f"Caught {len(eg.exceptions)} ValueError(s):")
    for i, e in enumerate(eg.exceptions, 1):
        print(f"  {i}. {e}")

# Tip: Exception groups are useful for handling multiple exceptions at once

# 18. Best Practices and Tips

# 1. Be specific with your exception handling. Catch specific exceptions, not just Exception.
# 2. Use finally for cleanup code that must always run.
# 3. Don't catch exceptions you can't handle properly.
# 4. Use else clause for code that should only run if no exception occurred.
# 5. Raise exceptions early, catch them late.
# 6. Use custom exceptions for application-specific errors.
# 7. Use context managers (with statements) for resource management.
# 8. Don't use exceptions for flow control in normal operations.
# 9. Log exceptions for debugging purposes.
# 10. Use exception chaining to provide more context about errors.
# 11. Use assertions for debugging and internal checks, not for data validation.
# 12. Be aware of the performance impact of try/except blocks in critical loops.

# 19. Debugging with pdb

import pdb

def buggy_function():
    x = 5
    y = 0
    pdb.set_trace()  # This will start the debugger
    result = x / y
    return result

# Uncomment to debug:
# buggy_function()

# Tip: Use pdb.set_trace() or breakpoint() (Python 3.7+) to set breakpoints in your code

# This concludes the enhanced detailed Python Cheat Sheet for Exception Handling