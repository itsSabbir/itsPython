#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Data Types and Variables
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#===============================================================================
# 1. Basic Data Types
#===============================================================================

# Python supports various basic data types, each serving a different purpose and having distinct characteristics.
# Understanding these data types is essential as they form the foundation of variable manipulation and logic control.

# Integer: Whole numbers (positive, negative, or zero)
integer_var = 42  # Assigning an integer value. Integers in Python are of arbitrary precision, allowing operations with very large numbers.
print(f"Integer: {integer_var}")  # Output: Integer: 42
# Advanced Insight: Python's 'int' type is implemented as 'long' in CPython. It dynamically expands based on the value, but be mindful of performance when handling extremely large integers.

# Float: Decimal numbers
float_var = 3.14159  # Assigning a floating-point number. Python's float is equivalent to a double in C (64-bit representation).
print(f"Float: {float_var}")  # Output: Float: 3.14159
# Best Practice: Avoid exact equality checks with floats due to potential floating-point precision errors.
# Advanced Tip: For precise decimal arithmetic, consider using the 'decimal.Decimal' module, especially when working with financial data.

# String: Sequence of characters
str_var = "Hello, Python!"  # Creating a string. Strings in Python are immutable, meaning once created, they cannot be altered.
print(f"String: {str_var}")  # Output: String: Hello, Python!
# Insight: Use triple quotes (''' or """) for multi-line strings or when the string contains both single and double quotes.

# Boolean: True or False
bool_var = True  # Boolean values in Python are a subclass of integers. 'True' is equivalent to 1 and 'False' is equivalent to 0.
print(f"Boolean: {bool_var}")  # Output: Boolean: True
# Pitfall: Be cautious when using booleans in arithmetic operations, as they can lead to unexpected results. E.g., 'True + 1' evaluates to 2.

# NoneType: Represents absence of a value
none_var = None  # None is a singleton object representing 'null' or 'no value'.
print(f"NoneType: {none_var}")  # Output: NoneType: None
# Best Practice: Always use 'is None' or 'is not None' for comparison instead of '==', as None is a unique singleton.

# Check the type of a variable
# 'type()' is a built-in function that returns the type of the object, which is useful for debugging and ensuring correct data handling.
print(type(integer_var))  # Output: <class 'int'>
print(type(float_var))    # Output: <class 'float'>
print(type(str_var))      # Output: <class 'str'>
print(type(bool_var))     # Output: <class 'bool'>
print(type(none_var))     # Output: <class 'NoneType'>
# Advanced Tip: For comprehensive type checking in complex projects, use 'isinstance()' instead of 'type()', as it supports inheritance and polymorphic checks.
# Example: isinstance(integer_var, int) is preferable to type(integer_var) == int.

# Additional insights:
# 1. Python dynamically types variables. You don't need to declare the data type, as Python infers it from the assigned value.
# 2. Variables in Python are references to objects in memory. Understanding this concept is crucial when working with mutable and immutable objects, as modifying mutable objects (e.g., lists) through multiple references can have side effects.

# Examples with print statements:

# Integer operations
int_var1 = 100
int_var2 = 3
int_division = int_var1 // int_var2  # Floor division: result is rounded down to the nearest integer
print(f"Integer Floor Division: {int_division}")  # Output: Integer Floor Division: 33
# Advanced Tip: The '//' operator is useful when you want integer division results, unlike '/' which always returns a float.

# Float precision
precise_sum = 0.1 + 0.2  # Floating-point arithmetic might lead to unexpected results
print(f"Float Sum: {precise_sum}")  # Output might not be exactly 0.3 due to precision issues
# Insight: Use round(precise_sum, 2) for rounding, but be aware that rounding might not always solve precision problems in critical calculations.

# String concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2  # Concatenating strings using the '+' operator
print(f"Concatenated String: {concatenated_str}")  # Output: Concatenated String: Hello World
# Best Practice: Use f-strings (formatted strings) for readability and efficiency in Python 3.6+.

# Boolean evaluation in expressions
print(f"True + True: {True + True}")  # Output: 2, because 'True' is treated as 1
print(f"False * 3: {False * 3}")  # Output: 0, since 'False' is treated as 0

# NoneType comparison
var = None
print(var is None)  # Output: True, preferred way to check for None

# Overall Summary:
# - Knowing the nuances of basic data types enables writing efficient and bug-free code.
# - As a developer progresses, understanding memory management, precision handling, and type compatibility becomes increasingly vital.
# - This knowledge forms a foundation for advanced topics like data structures, algorithm optimization, and complex software design.

#===============================================================================
# 2. Type Conversion and Casting
#===============================================================================

# Type conversion is crucial when handling mixed data types, ensuring that operations are compatible or extracting the right values.
# Python provides built-in functions like int(), float(), str(), and others for converting between data types.
# Understanding how these conversions work is essential for handling data gracefully, especially in real-world scenarios with diverse input.

# Example 1: String to Integer Conversion
# Using int() to convert a string containing numeric characters to an integer.
# This is a common use case when dealing with user input, which is often captured as strings.
str_to_int = int("123")
# Using f-strings to display the result along with its type, which confirms successful conversion to integer.
print(f"String to Integer: {str_to_int}, Type: {type(str_to_int)}")

# Advanced tip: Be cautious with leading/trailing whitespaces; they need to be stripped before conversion to avoid ValueError.
# For example, int("  123  ") works fine, but int("123abc") will raise an error.

# Example 2: Float to Integer Conversion (Truncation)
# Converting a float to an integer using int(). This truncates the decimal part, effectively flooring towards zero.
float_to_int = int(56.78)
# Printing to observe how the conversion impacts precision by removing the decimal part.
print(f"Float to Integer: {float_to_int}, Type: {type(float_to_int)}")

# Insight: Be aware that int() does not round the number; it simply truncates. For negative values, int(-4.99) results in -4, not -5.
# If rounding is needed, use round(), math.ceil(), or math.floor() depending on your requirement.

# Example 3: Integer to Float Conversion
# Converting an integer to a float using float(). Straightforward conversion as every integer can be represented as a float.
int_to_float = float(100)
# Useful when precision is needed in calculations or when integrating with libraries requiring float inputs.
print(f"Integer to Float: {int_to_float}, Type: {type(int_to_float)}")

# Advanced note: This conversion might introduce floating-point representation issues in large numbers,
# so be cautious in high-precision calculations (e.g., scientific computing).

# Example 4: Integer to String Conversion
# Converting an integer to a string using str(). Commonly used in cases where numerical data needs to be included in text outputs.
int_to_str = str(2024)
# Essential for constructing dynamic messages, file names, or working with mixed data types.
print(f"Integer to String: {int_to_str}, Type: {type(int_to_str)}")

# Pro tip: Converting complex expressions to strings within f-strings is seamless, e.g., print(f"The year is {str(2024)}").
# This is handled automatically without needing explicit str() calls.

# Example 5: Float to String Conversion
# Converting a float to a string. Useful when presenting data in reports, logs, or user interfaces where numeric formatting is required.
float_to_str = str(9.81)
# Ensures the numeric value can be combined with other strings or stored as text.
print(f"Float to String: {float_to_str}, Type: {type(float_to_str)}")

# Precision insight: Converting floats with high precision (e.g., 0.3333333) might introduce representation quirks.
# Use formatting techniques (e.g., format(float, ".2f")) to control output precision.

# Example 6: Complex Number to String Conversion
# Converting a complex number to a string using str(). Complex numbers are represented as 'real+imaginary' in string form.
complex_to_str = str(4 + 3j)
print(f"Complex to String: {complex_to_str}, Type: {type(complex_to_str)}")

# Advanced note: While converting complex to int or float directly isn’t allowed (raises TypeError), extracting parts is possible:
# int((4 + 3j).real) or float((4 + 3j).imag).

# Example 7: Boolean to Integer Conversion
# Converting booleans to integers using int(). In Python, True converts to 1, and False converts to 0.
bool_to_int_true = int(True)
bool_to_int_false = int(False)
print(f"Boolean to Integer (True): {bool_to_int_true}, Type: {type(bool_to_int_true)}")
print(f"Boolean to Integer (False): {bool_to_int_false}, Type: {type(bool_to_int_false)}")

# Advanced application: This is particularly useful in calculations or as binary flags, e.g., sum([True, False, True]) results in 2.

# Example 8: Boolean to String Conversion
# Converting boolean values to strings. Useful when generating logs, error messages, or configuration files.
bool_to_str = str(True)
print(f"Boolean to String: {bool_to_str}, Type: {type(bool_to_str)}")

# Performance insight: Boolean to string conversions are computationally inexpensive,
# but excessive conversions in loops can impact performance in high-frequency tasks.

# Example 9: None to String Conversion
# Converting None to a string results in the literal string "None". Useful in logging or data serialization.
none_to_str = str(None)
print(f"None to String: {none_to_str}, Type: {type(none_to_str)}")

# Advanced tip: Converting None to other types (e.g., int(None)) will raise a TypeError, so handle such conversions with caution.

# Example 10: Chained Conversions
# Demonstrating multiple conversions: float to int to string
float_value = 45.678
chained_conversion = str(int(float_value))
print(f"Chained Conversion (Float -> Int -> String): {chained_conversion}, Type: {type(chained_conversion)}")

# Advanced insight: Chained conversions can be efficient but require awareness of how each step alters data.
# For instance, precision loss occurs from float to int before converting to string.

# Final Tip: Type conversion best practices involve checking data validity before conversion (using functions like isnumeric() for strings),
# and always considering edge cases like empty strings, None values, or large numbers.


#===============================================================================
# 3. Mutable vs Immutable Data Types
#===============================================================================

# In Python, data types can be categorized as mutable or immutable. 
# 'Mutable' means the object can be modified after creation, while 'immutable' means it cannot be changed.
# It's crucial to understand this concept as it affects memory usage, performance, and overall behavior
# of your code, especially in complex systems.

# Immutable Example: int, float, str, tuple

# Demonstrating immutability with a string
immutable_str = "Hello"  # A string is an example of an immutable data type.
try:
    immutable_str[0] = "h"  # Attempting to change the first character of the string
except TypeError as e:
    # This raises a TypeError because strings are immutable in Python.
    # Insight: Immutability means that the object's contents cannot be altered.
    # Internally, this property allows optimizations such as interning (reusing memory for identical strings),
    # which can enhance performance, especially when dealing with many repeated strings in a program.
    print(f"Error: {e}")  # Output: 'str' object does not support item assignment

# Practical insight: Due to immutability, strings are inherently thread-safe,
# which makes them preferable for use in multi-threaded applications.

# Mutable Example: list, dict, set

# Demonstrating mutability with a list
mutable_list = [1, 2, 3]  # A list is an example of a mutable data type.
mutable_list[0] = 4  # Directly modifying the first element of the list.
# Unlike strings, lists can be modified in place, meaning that the elements can be changed without creating a new object.
# Advanced Insight: The memory address of the mutable object (e.g., the list) remains the same, even after modifications,
# which is efficient when frequent changes are needed, reducing overhead compared to creating new objects each time.
print(f"Modified list: {mutable_list}")  # Output: [4, 2, 3]

# Checking object identity
# Python assigns a unique identity to each object, and the id() function can be used to retrieve this identity.
# The id() function essentially provides the memory address of the object.

original_id = id(mutable_list)  # Capture the memory address (identity) of the mutable_list before modification
mutable_list.append(5)  # Appending an element to the mutable_list; this modifies the list in place
new_id = id(mutable_list)  # Capture the memory address after modification

# Since lists are mutable, the memory address (identity) remains unchanged even after modification.
print(f"List IDs same after modification: {original_id == new_id}")  # Output: True

# Best Practice: Use mutable types like lists when you need to perform frequent modifications,
# as this avoids the creation of new objects, making the code more memory-efficient.

# Now let's examine the behavior of an immutable type, such as a string:
original_id = id(immutable_str)  # Capture the memory address (identity) of the immutable_str
immutable_str += " World"  # Concatenating a string creates a new string object rather than modifying the existing one
new_id = id(immutable_str)  # Capture the memory address after concatenation

# Insight: Since strings are immutable, any operation that seems to modify them results in the creation of a new object.
print(f"String IDs same after modification: {original_id == new_id}")  # Output: False

# Advanced Insight: Although creating new objects might appear inefficient for immutable types,
# it has significant advantages, such as making the object hashable.
# Being hashable means they can be used as keys in dictionaries or as elements in sets,
# which require immutable and unique values.

# Demonstrating this with a dictionary:
sample_dict = {}
sample_tuple = (1, 2, 3)  # A tuple is immutable and hashable, making it a valid key for a dictionary.
sample_dict[sample_tuple] = "This is allowed"

try:
    sample_dict[mutable_list] = "This will cause an error"
except TypeError as e:
    # Lists are not hashable and hence cannot be used as dictionary keys.
    print(f"Error with mutable key: {e}")

# Best Practice: Choose immutable data types when you want data integrity and don't need modifications.
# This ensures that objects remain consistent and predictable throughout their lifecycle.

# Additional Example: Tuples and Lists for Function Arguments
def modify_elements(data):
    try:
        data[0] = 99
        print(f"Modified inside function: {data}")
    except TypeError as e:
        print(f"Cannot modify: {e}")

# Passing a mutable list
sample_list = [1, 2, 3]
modify_elements(sample_list)  # The list will be modified in place
print(f"List after function call: {sample_list}")  # Output: [99, 2, 3]

# Passing an immutable tuple
sample_tuple = (1, 2, 3)
modify_elements(sample_tuple)  # Will raise an error since tuples are immutable
print(f"Tuple after function call: {sample_tuple}")  # Output remains (1, 2, 3)

# Advanced Insight: Immutability and mutability also affect function argument passing.
# Mutable objects can be altered inside the function, while immutable objects cannot.
# This distinction is crucial when designing functions, as unintended modifications can lead to bugs,
# especially when passing mutable objects as arguments.

# Summary:
# - Use immutable types (e.g., str, tuple) for data that should remain constant and to ensure data integrity.
# - Use mutable types (e.g., list, dict) when frequent modifications are necessary.
# - Understanding the difference between mutable and immutable data types is fundamental
#   to writing efficient, predictable, and bug-free code.
# - Always be aware of the implications of mutability in multi-threaded environments, data structures, and function design.


#===============================================================================
# 4. Complex Numbers
#===============================================================================

# Initializing a complex number using the format a + bj, where 'a' is the real part and 'b' is the imaginary part.
# In Python, 'j' is used instead of 'i' (which is commonly used in mathematics) to represent the imaginary unit.
complex_var = 2 + 3j

# Printing the complex number using an f-string for clear and formatted output.
print(f"Complex: {complex_var}")  # Output: Complex: (2+3j)

# Extracting the real and imaginary parts of the complex number using the 'real' and 'imag' attributes.
# Note: These attributes are read-only properties, meaning you can access them but not modify them directly.
print(f"Real part: {complex_var.real}, Imaginary part: {complex_var.imag}")  
# Output: Real part: 2.0, Imaginary part: 3.0
# Insight: Real and imaginary parts are always returned as floats, even if the original values were integers.

# Example with a purely imaginary number
pure_imaginary = 0 + 5j
print(f"Purely imaginary: {pure_imaginary}, Real part: {pure_imaginary.real}, Imaginary part: {pure_imaginary.imag}")
# Output: Purely imaginary: 5j, Real part: 0.0, Imaginary part: 5.0
# Insight: Python handles real parts of purely imaginary numbers as 0.0, emphasizing that complex numbers always maintain a consistent real + imaginary format.

# --- Complex number operations ---

# Defining another complex number to demonstrate arithmetic operations.
complex_var2 = 1 - 2j

# Addition of two complex numbers
# The addition operation works component-wise: (a + bj) + (c + dj) = (a + c) + (b + d)j
print(f"Addition: {complex_var + complex_var2}")  
# Output: (3+1j)
# Advanced insight: Addition is commutative and associative for complex numbers, meaning the order of addition does not affect the result.

# Multiplication of two complex numbers
# The multiplication follows the distributive property: (a + bj) * (c + dj) = (ac - bd) + (ad + bc)j
print(f"Multiplication: {complex_var * complex_var2}")  
# Output: (8+1j)
# Tip: This result aligns with the FOIL (First, Outside, Inside, Last) method used for binomials in algebra.
# Advanced insight: Complex multiplication includes both rotation and scaling in the complex plane, a concept that's fundamental in fields like signal processing.

# Subtraction of complex numbers
# The subtraction operation: (a + bj) - (c + dj) = (a - c) + (b - d)j
print(f"Subtraction: {complex_var - complex_var2}")
# Output: (1+5j)
# Insight: This operation is similar to vector subtraction, reinforcing the connection between complex numbers and 2D vectors.

# Division of two complex numbers
# Formula: (a + bj) / (c + dj) = [(ac + bd) + (bc - ad)j] / (c^2 + d^2)
# Note: Division can be trickier due to potential floating-point precision issues.
print(f"Division: {complex_var / complex_var2}")
# Output: (-0.4+1.4j)
# Advanced insight: Division involves multiplying by the conjugate of the denominator, making it essential to understand conjugate pairs in more advanced contexts.

# Absolute value (magnitude) of a complex number
# The absolute value |z| of a complex number z = a + bj is calculated as sqrt(a^2 + b^2).
# This represents the Euclidean distance from the origin (0, 0) to the point (a, b) in the complex plane.
print(f"Absolute value: {abs(complex_var)}")  
# Output: 3.605551275463989
# Advanced insight: The absolute value operation is analogous to finding the modulus in polar coordinates, which can be crucial when converting between rectangular (Cartesian) and polar forms.
# Note: The 'abs()' function is highly optimized in Python, ensuring that calculations for complex numbers are efficient.

# Complex conjugate
# The conjugate of a complex number z = a + bj is defined as a - bj. This flips the sign of the imaginary part.
print(f"Conjugate of {complex_var}: {complex_var.conjugate()}")  
# Output: (2-3j)
# Insight: Conjugates are particularly useful in rationalizing denominators during division and in various physics/engineering applications.

# Additional examples demonstrating complex number behavior:
# Multiplying a complex number by its conjugate results in a real number equal to the square of its magnitude.
print(f"Multiplication with conjugate: {complex_var * complex_var.conjugate()}")
# Output: (13+0j)
# Advanced insight: This property is frequently used in signal processing and physics to isolate the magnitude of a complex signal.

# Example of Python's built-in complex() function:
# This function can construct complex numbers from two floats, offering an alternative to using the 'a + bj' syntax.
constructed_complex = complex(4, -5)
print(f"Constructed complex: {constructed_complex}")
# Output: (4-5j)
# Tip: Use complex() when programmatically generating complex numbers, as it improves readability and maintains consistency in your code.

# Exploring the built-in isinstance() function for complex number checking:
# Useful for type validation in complex mathematical algorithms.
print(isinstance(complex_var, complex))  # Output: True
# Insight: This ensures that your code can differentiate between complex and real numbers, aiding in error prevention.

# Potential pitfalls:
# - Attempting to perform certain operations with non-complex numeric types (like adding an integer to a complex number) may lead to unexpected behavior or implicit type conversions.
print(f"Adding int to complex: {complex_var + 5}")  # Output: (7+3j)
# Insight: This is valid, but always be aware of potential unintended results when working with mixed types.

# - Keep in mind that complex numbers don't support comparison operations like < or >, as they don't have a natural ordering.
# Attempting the following will raise a TypeError:
# print(complex_var > complex_var2)  # This will cause an error
# Insight: Python follows mathematical conventions here, as complex numbers exist in a plane rather than a one-dimensional line.

# Best practices summary:
# 1. Complex numbers are immutable in Python, so treat each operation as producing a new instance.
# 2. Always be cautious of precision errors, especially when performing arithmetic with other floating-point numbers.
# 3. Use built-in functions like abs(), complex(), and isinstance() to maximize code clarity and efficiency when handling complex numbers.

#===============================================================================
# 5. Variables and Assignment
#===============================================================================

# Dynamic typing: Python is a dynamically typed language, meaning that a variable can change its data type during execution.
# This provides flexibility but can introduce bugs if the type isn't managed correctly.
x = 5  # Here, x is initially assigned as an integer.
print(f"x is initially an integer: {x}")

# Python allows variables to change type seamlessly. This makes code concise but can lead to confusion in large projects
# where the variable's type isn't clear from the context. Good practice involves ensuring variables maintain expected types.
x = "Now I'm a string"  # x is now reassigned as a string.
print(f"x is now a string: {x}")

# Multiple assignment: Python allows unpacking multiple values into multiple variables in a single line.
# This technique is more concise than individual assignments and is particularly useful in returning multiple values from functions.
a, b, c = 1, 2, 3  # a is assigned 1, b is assigned 2, c is assigned 3 in one line.
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Swapping variables: Python offers a syntactically elegant way to swap values between two variables without needing a temporary placeholder.
# This approach is both time and space efficient. In other languages, this would typically require an extra variable.
a, b = b, a  # Values of a and b are swapped in a single step.
print(f"After swapping: a={a}, b={b}")

# Augmented assignment operators: Python supports augmented assignments, which provide a shorthand way to update variable values.
# For example, x += 5 is equivalent to x = x + 5. This approach can enhance code readability and performance, as it often optimizes in-place.
x = 10  # x is initialized with the value 10.
x += 5  # Equivalent to x = x + 5; this modifies x in place to 15.
print(f"Augmented assignment: x += 5 results in x = {x}")

# Additional examples to demonstrate variables and assignment nuances:

# Example 1: Assigning the same value to multiple variables in one line.
p = q = r = 42  # All three variables are set to 42. This is commonly used for initializing multiple variables with the same value.
print(f"Same value assignment: p={p}, q={q}, r={r}")

# Example 2: Changing a mutable object via multiple assignments.
# When working with mutable objects (e.g., lists), assigning multiple variables to the same object can lead to unexpected changes.
list1 = [1, 2, 3]
list2 = list1  # Both list1 and list2 now refer to the same list object in memory.
list2.append(4)  # Modifying list2 will also affect list1.
print(f"After appending to list2, list1 is now: {list1}")
# Insight: This happens because Python handles mutable objects by reference. Always use list2 = list1.copy() if a separate copy is needed.

# Example 3: Unpacking a string into variables
str_example = "ab"
first, second = str_example  # Each character of the string is unpacked into respective variables.
print(f"Unpacked string: first={first}, second={second}")

# Example 4: Using augmented assignments with different data types
y = "Hello"
y += " World"  # This concatenates " World" to the existing string.
print(f"String concatenation with augmented assignment: {y}")

z = [1, 2, 3]
z += [4, 5]  # This extends the list by appending [4, 5] to the original list.
print(f"List extension with augmented assignment: {z}")

# Potential pitfall: Attempting to unpack more or fewer variables than elements will cause a ValueError.
# Uncomment the line below to see the error in action.
# x, y = [1, 2, 3]  # ValueError: too many values to unpack (expected 2)

# Advanced Tip: Be mindful of variable shadowing in larger scopes, where a variable defined in an inner scope
# might override one from an outer scope, potentially causing unintended behavior.
outer_var = 10

def example_function():
    outer_var = 20  # This shadows the outer_var defined outside, making the original inaccessible within this function.
    print(f"Inner scope variable: {outer_var}")

example_function()
print(f"Outer scope variable: {outer_var}")  # This prints the original value, showing how scope isolation works in Python.

#===============================================================================
# 6. Constants
#===============================================================================

# Python doesn't have a built-in mechanism for defining true constants. 
# However, it's a widely accepted convention to name constant values in uppercase.
# By using all uppercase letters, we're signaling to other developers that these values should remain unchanged throughout the program.
# Keep in mind that despite this convention, Python doesn't enforce immutability; you can still modify these values.
# Therefore, it's crucial for code maintainers to respect this convention for code clarity and maintainability.

PI = 3.14159  # Represents the mathematical constant π (Pi) up to five decimal places.
# Advanced Tip: For more precision, use Python's math library (e.g., from math import pi).
# This could be especially important in scientific or financial applications requiring high precision.

MAX_SIZE = 100  # An example constant representing a maximum allowable size or limit.
# Best Practice: Use constants like MAX_SIZE when you have a fixed value that might be used multiple times.
# This makes the code easier to modify and understand since changing it in one place updates it everywhere it's referenced.

# Using f-strings for formatted printing is more efficient and readable compared to older methods (e.g., using % or .format()).
# It allows you to directly embed expressions inside the curly braces.
print(f"PI: {PI}")  # Outputs: PI: 3.14159
# Novice Insight: f-strings are a concise way to construct strings, available from Python 3.6 onwards.
# Intermediate Insight: f-strings evaluate expressions within them at runtime, so they can be more versatile than static strings.
# Advanced Insight: If you're working with debugging or need complex formatting, f-strings can also handle expressions directly, 
# such as f"{PI:.2f}" for rounding.

print(f"MAX_SIZE: {MAX_SIZE}")  # Outputs: MAX_SIZE: 100
# Common Pitfall: If MAX_SIZE were to change in multiple places, it's easy to miss an occurrence. 
# Defining it as a constant and using it throughout the code prevents such issues and avoids magic numbers, 
# i.e., using hardcoded values without context or explanation.

# Additional examples showcasing the use of constants

# Defining multiple constants at once (not recommended for long or complex values for readability):
WIDTH, HEIGHT = 800, 600
print(f"Screen dimensions: {WIDTH}x{HEIGHT}")

# Advanced Tip: When working with constants that have a logical grouping (e.g., RGB colors), 
# consider using named tuples, dataclasses, or dictionaries for better organization.
# This provides more structure and makes it clear how values are related, especially in larger codebases.

#===============================================================================
# 7. String Operations
#===============================================================================

# Concatenation: Combining multiple strings into one. The '+' operator performs string concatenation.
# Note that strings are immutable, so a new string is created in memory each time this operation is performed.
greeting = "Hello" + " " + "World"
print(f"Concatenation: {greeting}")  # Output: 'Hello World'

# Advanced insight: Although simple concatenation with '+' works well for a few strings,
# repeatedly concatenating many strings (e.g., in a loop) can be inefficient due to the
# creation of multiple intermediate strings. Consider using ''.join() in such cases.

# Repetition: The '*' operator repeats the string a specified number of times.
# This is useful for quickly creating repeated patterns or padding.
repeated = "Python " * 3
print(f"Repetition: {repeated}")  # Output: 'Python Python Python '

# Caution: Using very large multipliers can lead to high memory usage since a new, longer string is created.

# Indexing and Slicing
# Indexing: Accessing a specific character in the string. Indexing starts at 0 in Python.
# Negative indexing counts from the end, with -1 being the last character.
text = "Python"
print(f"First character: {text[0]}")  # Output: 'P'
print(f"Last character: {text[-1]}")  # Output: 'n'

# Slicing: Extracting a substring. The syntax is [start:end], where 'start' is inclusive, and 'end' is exclusive.
print(f"Slicing (1:4): {text[1:4]}")  # Output: 'yth' (starts at index 1, ends before index 4)

# Advanced slicing insight: Omitting 'start' or 'end' defaults to the beginning or end of the string, respectively.
# This is useful for quick extractions. For example, text[:3] extracts the first three characters.

# Reverse a string: The slice notation [::-1] uses a step of -1, effectively reversing the order.
print(f"Reverse: {text[::-1]}")  # Output: 'nohtyP'

# String methods: Built-in methods that provide various operations on strings.
# These do not modify the original string but return a new one since strings are immutable.

# Convert all characters to uppercase
print(f"Uppercase: {text.upper()}")  # Output: 'PYTHON'

# Convert all characters to lowercase
print(f"Lowercase: {text.lower()}")  # Output: 'python'

# Convert to title case (first letter of each word capitalized)
print(f"Title case: {'hello world'.title()}")  # Output: 'Hello World'

# Strip whitespace: Removes leading and trailing whitespace (spaces, tabs, etc.)
print(f"Strip whitespace: {'  spacey  '.strip()}")  # Output: 'spacey'

# Advanced insight: There are also lstrip() and rstrip() methods for stripping whitespace
# from the left or right side only, respectively. These methods can handle custom characters if specified.

# String formatting: Combining strings with variables/values in a readable, efficient manner.

# f-string (formatted string literals, Python 3.6+): Allows embedding expressions directly within curly braces.
# This is the most modern and recommended way to handle string formatting due to its readability and efficiency.
name = "Sabbir"
age = 30
print(f"{name} is {age} years old")  # Output: 'Sabbir is 30 years old'

# The .format() method (available since Python 2.7 and 3.0): Uses placeholders and can reorder or format values.
print("{} is {} years old".format(name, age))  # Output: 'Sabbir is 30 years old'

# Advanced tip: The .format() method provides more control, allowing for named placeholders like:
print("{name} is {age} years old".format(name=name, age=age))  # Output: 'Sabbir is 30 years old'

# %-formatting (older style): Inspired by C's printf syntax. Still works but is less recommended in modern code.
print("%s is %d years old" % (name, age))  # Output: 'Sabbir is 30 years old'

# Advanced insight: f-strings are generally faster than the .format() method and %-formatting due to their
# optimized implementation. However, %-formatting is still occasionally seen in older codebases or when 
# working with very old Python versions.

# Final Advanced Tip: When handling internationalization (i18n) and localization (l10n),
# consider using the built-in gettext module instead of basic string formatting,
# as it provides better support for translations.

#===============================================================================
# 8. Type Hints (Python 3.5+)
#===============================================================================

# Type hints are annotations that specify the expected data types of function parameters and return values.
# In this example, 'name' is expected to be of type 'str', and the function is expected to return a 'str'.
def greet(name: str) -> str:
    return f"Hello, {name}!"  # Constructs and returns a greeting message by embedding 'name' into the string.

# Note: Type hints provide several benefits:
# 1. They improve code readability by making the expected types clear.
# 2. They allow type-checking tools (e.g., mypy) to identify potential issues before runtime.
# 3. They assist with code auto-completion and documentation in IDEs, enhancing the development experience.

# Example of correct usage
print(greet("Sabbir"))  # Works fine because 'Sabbir' is of type 'str', which matches the expected input.

# Example of incorrect usage
print(greet(123))  # This will still execute without an error because Python does not enforce type hints at runtime.
# However, static type checkers like 'mypy' will flag this as a potential bug since 123 is an 'int', not a 'str'.

# Advanced tip: Type hints are purely advisory and don’t alter the runtime behavior of the program. 
# This makes them particularly useful in large codebases, where they help identify type-related bugs early on.
# However, developers must ensure that the type hints are kept up-to-date as the code evolves.

# Using type hints with 'None' return
def greet_and_log(name: str) -> None:
    print(f"Greeting {name}!")  # Prints the greeting
    # The function returns 'None' because there's no explicit return statement, indicating that the function is used for side effects (e.g., logging).

greet_and_log("Charlie")  # Proper usage
# This example is useful in larger systems where the return type of 'None' explicitly informs the developer that there's no data being returned.

# Working with complex data types
from typing import List, Dict, Tuple

def process_user_data(usernames: List[str], details: Dict[str, Tuple[int, str]]) -> List[str]:
    # Function expects 'usernames' to be a list of strings
    # and 'details' to be a dictionary where each key is a string and each value is a tuple containing an integer and a string.
    processed_users = []
    for username in usernames:
        age, status = details.get(username, (0, "Unknown"))  # Fetches tuple details; defaults to (0, "Unknown") if the username isn't found.
        processed_users.append(f"{username} is {age} years old and {status}")
    return processed_users

usernames_list = ["Sabbir", "Bob"]
user_details = {
    "Sabbir": (30, "Active"),
    "Bob": (25, "Inactive")
}

print(process_user_data(usernames_list, user_details))  # Returns ['Sabbir is 30 years old and Active', 'Bob is 25 years old and Inactive']

# Uncommon insight: When working with nested or complex types (e.g., List[Dict[str, Tuple[int, str]]]),
# make sure your type hints reflect the structure accurately to prevent misunderstandings and potential logic errors.

# Edge case: Type hints for functions that accept any type
from typing import Any

def echo(value: Any) -> Any:
    # 'Any' is a special type hint that indicates 'value' can be of any data type, and the return type can also be anything.
    return value

print(echo("test"))  # Works with a string
print(echo(123))     # Works with an integer
print(echo([1, 2, 3]))  # Works with a list

# Using 'Any' can be practical when writing generic code, but overusing it can defeat the purpose of type hints.
# Best practice: Limit the use of 'Any' to scenarios where you genuinely expect varied data types.

# Type hints for functions with optional parameters
from typing import Optional

def optional_greeting(name: Optional[str] = None) -> str:
    # 'Optional[str]' means that 'name' can be a 'str' or 'None'.
    if name:
        return f"Hello, {name}!"
    return "Hello, stranger!"

print(optional_greeting("Eve"))  # Prints 'Hello, Eve!'
print(optional_greeting())       # Prints 'Hello, stranger!'

# Advanced note: 'Optional[str]' is a concise way to express 'Union[str, None]'.
# Type hints that combine 'Optional' with default values help indicate when an argument is truly optional, making the function's contract more explicit.

# Summarizing advanced type hints usage:
# 1. Use 'List', 'Dict', and 'Tuple' from the 'typing' module to hint at more complex data structures.
# 2. Utilize 'Optional' when a parameter or return value can be 'None', clarifying the function's intent.
# 3. 'Any' can be helpful for highly generic code but should be used judiciously to maintain type safety and code clarity.

#===============================================================================
# 9. Memory Management
#===============================================================================

import sys  # sys module provides access to system-specific parameters and functions

# Reference counting and garbage collection in Python
# Python uses automatic memory management with reference counting and garbage collection.
# An object's reference count determines when it can be freed from memory.

x = [1, 2, 3]  # A list object is created, and variable x now references it. The reference count is now 1.
y = x  # y references the same list object as x, hence the reference count increases to 2.

# id() returns the memory address of the object that x and y are pointing to
print(f"x id: {id(x)}, y id: {id(y)}")  # Both x and y should have the same id as they reference the same object.

del x  # The reference count to the list decreases by 1, but the list object still exists since y still references it.
# If no other variable referenced this object, Python's garbage collector would eventually free it from memory.

print(f"y after deleting x: {y}")  # The object is still accessible via y. This demonstrates Python’s garbage collection process.

# Key Insight:
# Python's garbage collection doesn't immediately reclaim memory when an object’s reference count drops to 0. 
# It also performs cycle detection to clean up circular references, though it's rare in practice.

# Checking memory size of various objects using sys.getsizeof()
# This function returns the memory size in bytes of the object including any overhead from Python’s internal bookkeeping.
int_var = 42  # An integer object, generally small and stored in a memory-efficient manner by Python's internal optimizations.
float_var = 3.14  # A float object, typically larger than an integer due to precision and representation.
list_var = [1, 2, 3]  # A list object. Lists in Python are dynamic arrays that manage capacity internally.
dict_var = {'a': 1, 'b': 2}  # A dictionary object. Dicts use a hash table under the hood, making them memory efficient but with some overhead.

# Printing the size of different data types
print(f"Size of int: {sys.getsizeof(int_var)} bytes")  # Generally small, often around 28 bytes (varies by Python version).
print(f"Size of float: {sys.getsizeof(float_var)} bytes")  # Larger than int, often around 24 bytes, due to additional floating-point representation.
print(f"Size of list: {sys.getsizeof(list_var)} bytes")  # Includes overhead for managing elements, typically 64 bytes + size of elements.
print(f"Size of dict: {sys.getsizeof(dict_var)} bytes")  # Contains overhead for hash tables, so expect a larger size even with few elements.

# Advanced Insight:
# Python objects have a significant amount of overhead, especially for small objects. This is due to internal structures like reference counting, type information, etc.
# Thus, the actual memory usage of an object is often larger than the data it holds.
# When working with large data or performance-critical applications, consider alternative data structures like numpy arrays which are more memory efficient.

# Another example to illustrate reference counting:

a = 500  # Immutable integer object, stored in memory
b = a  # b now points to the same object as a, increasing its reference count
c = 500  # In Python, small integers (-5 to 256) are cached, but larger integers like 500 may be unique objects

print(f"a id: {id(a)}, b id: {id(b)}, c id: {id(c)}")  # a and b will have the same id, but c may have a different one

# Common Pitfall:
# Don't assume integers outside the range -5 to 256 will always be shared. The caching mechanism applies only to this range.
# This is because Python pre-allocates these integers for efficiency. However, larger integers may not be reused and will often have unique ids.

# Checking memory size of more complex objects
import numpy as np

# Creating a numpy array with the same elements as list_var
np_array = np.array([1, 2, 3])

print(f"Size of numpy array: {sys.getsizeof(np_array)} bytes")  # Typically smaller than a list of the same size due to more efficient memory management.

# Final Note:
# Be aware of Python’s memory model. Understanding reference counting, garbage collection, and the impact of data structures on memory size can greatly enhance performance optimization.
# This is particularly crucial when dealing with large datasets, high-performance applications, or low-level memory management.

#===============================================================================
# 10. Additional Data Types
#===============================================================================

# Tuples (immutable sequences):
# Tuples are ordered collections that cannot be changed (immutable). They can hold multiple data types, which makes them useful for read-only data.
# Once created, elements in a tuple cannot be added, removed, or modified. This immutability is a performance optimization compared to lists.
tuple_var = (1, 2, 3)  # Tuple containing three integer elements
print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")  
# Output: Tuple: (1, 2, 3), Type: <class 'tuple'>
# Advanced tip: Tuples are hashable, so they can be used as dictionary keys or elements of sets, unlike lists.

# Sets (unordered collections of unique elements):
# Sets store unique items without any particular order, which makes them ideal for removing duplicates or testing membership.
# Set elements must be immutable, but the set itself is mutable, allowing elements to be added or removed.
set_var = {1, 2, 3, 3, 2, 1}  # Duplicate elements (3 and 2) will be automatically discarded
print(f"Set: {set_var}, Type: {type(set_var)}")
# Output: Set: {1, 2, 3}, Type: <class 'set'>
# Best practice: Use sets for membership testing as it is generally faster (O(1) average time complexity) compared to lists (O(n) complexity).
# Pitfall: Since sets are unordered, they do not support indexing or slicing like lists or tuples.

# Dictionaries (key-value pairs):
# Dictionaries are mutable, unordered collections of key-value pairs, allowing for fast lookup, insertion, and deletion based on keys.
# Keys must be unique and immutable (e.g., strings, numbers, tuples), but values can be of any type and can be mutable.
dict_var = {'name': 'Sabbir', 'age': 30, 'city': 'New York'}  # Creating a dictionary with three key-value pairs
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")
# Output: Dictionary: {'name': 'Sabbir', 'age': 30, 'city': 'New York'}, Type: <class 'dict'>

# Accessing values in a dictionary using a key:
print(f"Accessing dictionary value: {dict_var['name']}")  # Accessing the value associated with the key 'name'
# Output: Accessing dictionary value: Sabbir
# Advanced tip: Use the dict.get(key, default) method instead of direct access to avoid KeyError if the key is not present.
# For example: dict_var.get('non_existent_key', 'Default Value')
# Best practice: If iterating over dictionary keys frequently, consider using collections.OrderedDict (Python <3.7) or note that dicts maintain insertion order (Python 3.7+).

# Bytes and Bytearray (working with binary data):
# Bytes are immutable sequences of bytes (8-bit values), often used for binary data such as images, files, or network protocols.
# Bytearray is similar to bytes but mutable, allowing modification of individual elements.
bytes_var = b'hello'  # Prefix 'b' indicates a byte literal, each character is represented as its ASCII value
print(f"Bytes: {bytes_var}, Type: {type(bytes_var)}")
# Output: Bytes: b'hello', Type: <class 'bytes'>

# Bytearray provides the same functionality but with the ability to modify the data:
bytearray_var = bytearray(b'hello')
print(f"Bytearray: {bytearray_var}, Type: {type(bytearray_var)}")
# Output: Bytearray: bytearray(b'hello'), Type: <class 'bytearray')
# Advanced insight: Bytearrays are especially useful for I/O operations where mutable sequences are required for performance.
# Example modification:
bytearray_var[0] = 72  # Changing the first byte from 'h' (ASCII 104) to 'H' (ASCII 72)
print(f"Modified Bytearray: {bytearray_var}")
# Output: Modified Bytearray: bytearray(b'Hello')
# Pitfall: Be cautious with encoding/decoding between strings and bytes, as incorrect handling can lead to data corruption.

# This concludes the detailed Python Cheat Sheet for Data Types and Variables
# Note: Each data type serves different use cases, so choosing the right one can greatly affect the performance and efficiency of your code.
