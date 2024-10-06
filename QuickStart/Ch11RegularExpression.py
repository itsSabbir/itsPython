#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Regular Expressions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Regular expressions (regex) are a powerful tool for matching patterns in text.
# The 're' module in Python provides various functions to work with regular expressions.
# Understanding how to use regex can significantly enhance your ability to manipulate strings.

import re  # Importing the regular expression module

# Example 1: Basic Pattern Matching
# The 're.match()' function checks for a match only at the beginning of the string.
pattern = r"\d+"  # Regex pattern to match one or more digits
text = "123 abc"
match = re.match(pattern, text)  # Check if the string starts with digits

if match:
    print(f"Match found: {match.group()}")  # Outputs: Match found: 123
else:
    print("No match found")

# Use case:
# This can be useful for validating input where the beginning of a string is critical,
# such as numeric codes or identifiers.

# Example 2: Searching Within a String
# The 're.search()' function scans through the string and returns the first match.
text = "abc 123 def"
search = re.search(pattern, text)  # Look for digits anywhere in the string

if search:
    print(f"Search found: {search.group()}")  # Outputs: Search found: 123
else:
    print("No search match found")

# Example 3: Finding All Matches
# The 're.findall()' function returns a list of all non-overlapping matches.
text = "abc 123 def 456 ghi 789"
all_matches = re.findall(pattern, text)  # Find all sequences of digits

print(f"All matches found: {all_matches}")  # Outputs: All matches found: ['123', '456', '789']

# Use case:
# This is particularly useful when extracting multiple occurrences of a pattern,
# such as email addresses or phone numbers from a document.

# Example 4: Replacing Patterns
# The 're.sub()' function replaces occurrences of a pattern with a specified replacement.
text = "abc 123 def 456 ghi"
replaced_text = re.sub(pattern, "NUM", text)  # Replace digits with the word "NUM"

print(f"Replaced text: {replaced_text}")  # Outputs: Replaced text: abc NUM def NUM ghi

# Example 5: Using Character Classes
# Character classes allow for more complex matching, such as sets of characters.
pattern = r"[aeiou]"  # Regex to match any vowel
text = "hello world"
vowels = re.findall(pattern, text)  # Find all vowels in the text

print(f"Vowels found: {vowels}")  # Outputs: Vowels found: ['e', 'o', 'o']

# Advanced tip:
# Combining character classes with quantifiers allows for sophisticated patterns.
# For example, r"[aeiou]{2,}" would match any sequence of two or more vowels.

# Example 6: Anchors
# Anchors such as '^' and '$' are used to match the start and end of a string, respectively.
pattern_start = r"^hello"  # Matches if 'hello' is at the start of the string
pattern_end = r"world$"    # Matches if 'world' is at the end of the string
text_start = "hello world"
text_end = "goodbye world"

if re.match(pattern_start, text_start):
    print("Starts with hello")  # Outputs: Starts with hello

if re.search(pattern_end, text_end):
    print("Ends with world")  # Outputs: Ends with world

# Example 7: Groups and Capturing
# Parentheses are used to define groups and capture parts of the match.
pattern = r"(\d+)-(\d+)-(\d+)"  # Matches a date in the format 'MM-DD-YYYY'
date_text = "Today is 10-02-2024"

match = re.search(pattern, date_text)
if match:
    print(f"Matched date: {match.group()}")  # Outputs: Matched date: 10-02-2024
    print(f"Month: {match.group(1)}, Day: {match.group(2)}, Year: {match.group(3)}")  
    # Outputs: Month: 10, Day: 02, Year: 2024

# Example 8: Non-capturing Groups
# Non-capturing groups can be defined with '(?:...)' and are useful for structuring patterns without creating a group.
pattern_non_capturing = r"(?:\d{3})-\d{2}-\d{4}"  # Matches a SSN format but does not capture the area code
ssn_text = "SSN: 123-45-6789"

if re.search(pattern_non_capturing, ssn_text):
    print("SSN format matched")  # Outputs: SSN format matched

# Example 9: Flags for Modifiers
# The 'flags' argument can modify regex behavior, such as ignoring case sensitivity.
pattern_case_insensitive = r"hello"
text_case_sensitive = "Hello World"

if re.search(pattern_case_insensitive, text_case_sensitive, re.IGNORECASE):
    print("Match found (case insensitive)")  # Outputs: Match found (case insensitive)

# Potential pitfalls:
# Regular expressions can become complex and hard to read. 
# It's important to keep patterns as simple as possible while meeting requirements.
# Use comments or raw string notation (r"") to avoid escape sequence confusion.
# Always test regex patterns thoroughly with various input cases to ensure expected behavior.

# In summary, regular expressions are a powerful feature in Python for text processing.
# Mastering their syntax and usage can lead to more efficient and readable string manipulation.


#===============================================================================
# 1. Basic Patterns and Character Classes
#===============================================================================

# Regular expressions (regex) are powerful tools for pattern matching and text processing.
# This section covers basic matching and character classes.

import re  # Import the re module for regex operations

# Basic matching example
# Define a simple regex pattern to search for the exact string "hello"
pattern = r"hello"  # 'r' denotes a raw string, which prevents backslash escaping
text = "hello world"  # Sample text to search within

# Perform the search operation
match = re.search(pattern, text)  # Searches for the pattern in the text
if match:  # Check if a match was found
    print(f"Found: {match.group()}")  # Access the matched group using .group() method
    # Output: Found: hello

# Tip: Always use raw strings (r"...") for regex patterns to avoid the need to escape backslashes,
# as backslashes have special meanings in Python string literals.

# Character classes allow for more flexible matching of groups of characters.

# Define character class patterns
digit_pattern = r"\d+"  # Matches one or more digits (0-9)
word_pattern = r"\w+"   # Matches one or more word characters (alphanumeric + underscore)
space_pattern = r"\s+"  # Matches one or more whitespace characters (spaces, tabs, newlines)

# Sample text for character class matching
text = "The year is 2023, and the price is $19.99"

# Find all matches for digits in the text
print("Digits:", re.findall(digit_pattern, text))  # Output: ['2023', '19', '99']
# findall() returns all non-overlapping matches of the pattern in the string as a list.

# Find all matches for words in the text
print("Words:", re.findall(word_pattern, text))  # Output: ['The', 'year', 'is', '2023', 'and', 'the', 'price', 'is', '19', '99']
# This will capture every word, including numbers.

# Find all matches for whitespace in the text
print("Spaces:", re.findall(space_pattern, text))  # Output: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# This shows each instance of whitespace as separate matches.

# Custom character classes allow for specific character filtering.

# Define patterns for custom character classes
vowel_pattern = r"[aeiou]"  # Matches any single vowel
not_digit_pattern = r"[^\d]"  # Matches any character that is NOT a digit

# Find all vowels in the text (converted to lowercase for consistency)
print("Vowels:", re.findall(vowel_pattern, text.lower()))  # Output: ['e', 'e', 'a', 'i', 'a', 'e', 'i', 'e', 'i']
# Lowercasing ensures that the match is case-insensitive.

# Find all non-digit characters in the text
print("Non-digits:", re.findall(not_digit_pattern, text))  # Output: ['T', 'h', 'e', ' ', 'y', 'e', 'a', 'r', ' ', 'i', 's', ' ', ',', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'e', ' ', 'p', 'r', 'i', 'c', 'e', ' ', 'i', 's', ' ', '$', '.']
# This effectively filters out all numeric digits from the text.

# Tip: Use character classes to match specific types of characters efficiently.
# Character classes can dramatically simplify regex patterns, improve performance, 
# and make your code easier to understand and maintain.

#===============================================================================
# 2. Quantifiers
#===============================================================================

# In regular expressions, quantifiers specify the number of times a character or a group 
# can appear in a string. Understanding and using quantifiers effectively can enhance 
# pattern matching and string manipulation tasks.

text = "The quick brown fox jumps over the lazy dog"

# Zero or more: *
# The '*' quantifier matches zero or more occurrences of the preceding element.
# In this example, it looks for the letter 'o' in the text. It will return all segments 
# where 'o' appears, including empty strings for positions where 'o' does not appear.
print(re.findall(r"o*", text))  
# Output: ['', 'o', '', '', '', '', 'o', '', '', '', '', 'o', '', '', '', '', '', '', '', '', '', 'o', '', '', '', '', '', '', '', '', '', '', 'o', '']
# Explanation: The output contains empty strings indicating positions between letters where 
# 'o' is not present, as well as instances where 'o' is found.

# One or more: +
# The '+' quantifier matches one or more occurrences of the preceding element.
# Here, it finds all occurrences of 'o' that appear at least once.
print(re.findall(r"o+", text))  
# Output: ['o', 'o', 'o', 'o', 'o']
# Explanation: This output consists of only those instances where 'o' appears, omitting 
# the empty results from the previous example.

# Zero or one: ?
# The '?' quantifier matches zero or one occurrence of the preceding element.
# This example checks for the presence of 's' following the word 'jump'.
print(re.findall(r"jumps?", text))  
# Output: ['jumps']
# Explanation: Since 's' is present in 'jumps', it is captured. If 'jumps' were 
# replaced with 'jump', it would still match due to the '?' allowing for zero occurrences.

# Exactly n: {n}
# The '{n}' quantifier matches exactly n occurrences of the preceding element.
# This example finds words with exactly five letters.
print(re.findall(r"\w{5}", text))  
# Output: ['quick', 'brown', 'jumps']
# Explanation: Only words that contain exactly five letters are returned.

# n or more: {n,}
# The '{n,}' quantifier matches n or more occurrences of the preceding element.
# In this case, it finds words with at least four letters.
print(re.findall(r"\w{4,}", text))  
# Output: ['quick', 'brown', 'jumps', 'over', 'lazy']
# Explanation: All words with four or more letters are included in the output.

# Between n and m: {n,m}
# The '{n,m}' quantifier matches between n and m occurrences of the preceding element.
# Here, it captures words that have between three and five letters.
print(re.findall(r"\w{3,5}", text))  
# Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# Explanation: This output includes all words that fall within the specified length range.

# Tip: Use quantifiers to specify the number of occurrences of a pattern
# Quantifiers are powerful tools in regular expressions that can help refine your searches.
# They enable precise matching based on occurrence requirements, making them essential 
# for text parsing, validation, and manipulation tasks.

#===============================================================================
# 3. Anchors and Boundaries
#===============================================================================

# Regular expressions in Python provide powerful tools for pattern matching in strings.
# Anchors and boundaries are special characters that specify where a match must occur within the string.

# Example 1: Start of string anchor (^)
# The caret (^) asserts that the following pattern must occur at the beginning of the string.
# In this case, we search for the word 'The' at the start of the 'text'.
text = "The quick brown fox jumps over the lazy dog."
print(re.findall(r"^The", text))  # Output: ['The']
# This output confirms that 'The' is indeed at the start of the string.

# Use case: 
# Anchors like ^ are useful when validating input formats or ensuring certain prefixes, 
# such as checking if a username starts with a letter.

# Example 2: End of string anchor ($)
# The dollar sign ($) asserts that the preceding pattern must be at the end of the string.
# Here, we search for 'dog' at the end of 'text'.
print(re.findall(r"dog$", text))  # Output: ['dog']
# This output shows that 'dog' is at the end of the string.

# Use case:
# The end anchor is commonly used to validate formats where certain strings must appear as suffixes, 
# like file extensions (e.g., .txt, .jpg).

# Example 3: Word boundary (\b)
# The backslash 'b' represents a word boundary, ensuring that 'fox' appears as a whole word.
# This means 'fox' must not be part of a larger word (e.g., 'foxes' or 'unfoxed').
print(re.findall(r"\bfox\b", text))  # Output: ['fox']
# The output confirms that 'fox' appears as a distinct word in 'text'.

# Use case:
# Word boundaries are crucial when searching for whole words in text, especially in 
# natural language processing tasks or when validating keywords.

# Tip: 
# Using anchors is a best practice for matching patterns at specific positions within strings.
# They provide clarity in regex patterns and help avoid unintended matches. 
# When crafting regular expressions, it's essential to understand the context of the data 
# being analyzed to choose the right anchors effectively.

# Advanced insight:
# Anchors can be combined with other regex elements for more complex patterns.
# For instance, you could check if a string starts with 'The' and ends with 'dog' using:
# print(re.findall(r"^The.*dog$", text))  # Matches if 'text' starts with 'The' and ends with 'dog'.
# This demonstrates how anchors can enhance the specificity of matches.

# Potential pitfalls:
# Misunderstanding anchors can lead to unexpected matches. For example, 
# searching for a pattern without anchors might yield partial matches within words,
# which could lead to incorrect assumptions about the data.

#===============================================================================
# 4. Grouping and Capturing
#===============================================================================

# Grouping in regular expressions allows you to extract specific parts of a string 
# that match a pattern. This is fundamental for data extraction and manipulation tasks.

import re  # Importing the re module for regular expression operations

# Example 1: Basic grouping
# This pattern matches a date in the format YYYY-MM-DD.
# The parentheses create capturing groups for year, month, and day.
pattern = r"(\d+)-(\d+)-(\d+)"  # \d+ matches one or more digits
text = "Date: 2023-06-27"  # The text containing the date
match = re.search(pattern, text)  # Searching for the pattern in the text

if match:  # Check if a match is found
    year, month, day = match.groups()  # Extracting the matched groups
    print(f"Year: {year}, Month: {month}, Day: {day}")  # Output the captured values
# Output: Year: 2023, Month: 06, Day: 27
# Use case: Extracting date information from a larger text for processing or validation.

# Example 2: Named groups
# Named groups improve code readability by allowing you to access matched groups by name.
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"  # Named groups for year, month, day
match = re.search(pattern, text)  # Searching for the date pattern

if match:  # Check if a match is found
    # Accessing the groups by their names instead of index positions
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")
# Output: Year: 2023, Month: 06, Day: 27
# Tip: Named groups facilitate code maintenance, especially when dealing with multiple groups.

# Example 3: Non-capturing groups
# Non-capturing groups (?:...) are used when you want to group patterns without creating 
# a capturing group for that part of the regex.
pattern = r"(?:Mr|Mrs|Ms)\s(\w+)"  # Matches titles without capturing them
text = "Mr Smith and Mrs Johnson"  # Example text with names
matches = re.findall(pattern, text)  # Find all matches in the text
print(matches)  # Output: ['Smith', 'Johnson']
# Use case: Extracting names while ignoring the titles to simplify the result set.

# Example 4: Backreferences
# Backreferences allow you to match the same text as previously matched by a capturing group.
pattern = r"(\w+)\s+\1"  # Matches any word followed by the same word again
text = "hello hello world world"  # Example text with repeated words
matches = re.findall(pattern, text)  # Find all backreference matches
print(matches)  # Output: ['hello', 'world']
# Use case: Identifying duplicates in a text, such as repeated phrases in sentences.

# Tip: Use grouping for extracting specific parts of matched patterns 
# and for creating more complex patterns. Grouping enhances the power of regex, 
# allowing for more sophisticated text processing.

# Advanced insight:
# When designing complex regex patterns, consider using a tool like regex101.com 
# for testing and visualizing the regex, including how groups are captured.
# This can help refine your patterns and avoid common pitfalls related to 
# greedy versus non-greedy matching (e.g., using .*? for non-greedy captures).

#===============================================================================
# 5. Lookahead and Lookbehind Assertions
#===============================================================================

# Lookahead and lookbehind assertions are powerful features in regular expressions 
# that allow for more complex pattern matching without consuming characters in the string.

# Positive lookahead
# The pattern r"\d+(?=\s*dollars)" searches for one or more digits followed by 
# optional whitespace and the word "dollars". The lookahead assertion (?=\s*dollars) 
# ensures that "dollars" must follow the digits but does not include it in the match.
import re  # Importing the 're' module for regular expressions

pattern = r"\d+(?=\s*dollars)"  # Pattern to find digits followed by "dollars"
text = "I have 50 dollars and 20 euros"  # Sample text for matching
matches = re.findall(pattern, text)  # Find all matches in the text
print(matches)  # Output: ['50']
# Here, '50' is matched because it is followed by "dollars".

# Use case:
# This can be useful in financial applications where you need to extract amounts 
# that are specifically tied to certain currencies or items.

# Negative lookahead
# The pattern r"\d+(?!\s*dollars)" looks for digits that are NOT followed by 
# optional whitespace and the word "dollars". This helps in excluding certain matches.
pattern = r"\d+(?!\s*dollars)"  # Pattern to find digits not followed by "dollars"
matches = re.findall(pattern, text)  # Find all matches in the text
print(matches)  # Output: ['20']
# In this case, '20' is matched because it is not followed by "dollars".

# Use case:
# Negative lookahead can be useful in scenarios where you want to filter out 
# certain patterns from your results, such as excluding specific items in a list.

# Positive lookbehind
# The pattern r"(?<=price:\s)\d+" finds one or more digits that are preceded by 
# the string "price: " (including a space). The lookbehind assertion (?<=price:\s) 
# confirms that "price: " must precede the digits, but it does not include it in the match.
pattern = r"(?<=price:\s)\d+"  # Pattern to find digits after "price: "
text = "The price: 100 dollars"  # Sample text for matching
match = re.search(pattern, text)  # Search for the pattern in the text
if match:  # Check if a match is found
    print(match.group())  # Output: 100
# The matched group returns '100' as it follows "price: ".

# Use case:
# Positive lookbehind is useful in structured text processing where you need 
# to extract values based on specific preceding text or markers.

# Negative lookbehind
# The pattern r"(?<!@)\b\w+\b" matches whole words (defined by \b) that are 
# NOT preceded by the '@' symbol. The negative lookbehind assertion (?<!@) ensures 
# that words preceded by '@' are excluded.
pattern = r"(?<!@)\b\w+\b"  # Pattern to find words not preceded by '@'
text = "user@example.com and johndoe"  # Sample text for matching
matches = re.findall(pattern, text)  # Find all matches in the text
print(matches)  # Output: ['and', 'johndoe']
# Here, 'and' and 'johndoe' are matched as they are not preceded by '@'.

# Use case:
# Negative lookbehind can be particularly useful in email parsing or data 
# validation where you need to extract valid usernames while excluding 
# parts of an email address.

# Tip: Use lookahead and lookbehind assertions for complex pattern matching 
# without including the assertion in the match. This allows for cleaner 
# and more efficient pattern searches by maintaining the integrity of the 
# surrounding text while still isolating desired matches.

#===============================================================================
# 6. Flags and Options
#===============================================================================

# In this section, we explore the use of flags in regular expressions (regex) in Python.
# Flags allow you to modify the behavior of the regex engine, enabling more flexible pattern matching.

import re  # Import the 're' module for working with regular expressions

# Example 1: Case-insensitive matching
# The re.IGNORECASE flag allows for case-insensitive matching of patterns.
# In this example, we compile a pattern that matches the string "python" regardless of its case.
pattern = re.compile(r"python", re.IGNORECASE)  # 'r' denotes a raw string, preventing escape sequence interpretation
# The search method scans the string for the first occurrence of the pattern.
print(pattern.search("PYTHON is awesome").group())  # Output: PYTHON
# This demonstrates that the search finds "PYTHON" and returns it, highlighting the effectiveness of the flag.

# Use case:
# Case-insensitive matching is especially useful in scenarios where user input can vary in case,
# such as searching in databases or user-provided content.

# Example 2: Multiline mode
# The re.MULTILINE flag allows patterns to match at the start (^) and end ($) of each line within a multiline string.
text = "Start\nEnd"  # A string containing multiple lines
# Here, we compile a pattern that checks for the word "End" at the start of a line.
pattern = re.compile(r"^End", re.MULTILINE)
# The search method looks for the pattern "End" at the beginning of any line in the text.
print(pattern.search(text).group())  # Output: End
# This shows that "End" is matched successfully because it's at the beginning of the second line.

# Tip:
# Use the MULTILINE flag when working with block text or when line breaks matter,
# such as when parsing logs or formatted documents.

# Example 3: Verbose mode for readable patterns
# The re.VERBOSE flag allows you to write regex patterns that include whitespace and comments for better readability.
# This is particularly useful for complex patterns that would otherwise be hard to decipher.
phone_pattern = re.compile(r"""
    (\d{3})  # Area code
    [-.\s]?  # Optional separator (could be '-', '.', or whitespace)
    (\d{3})  # First 3 digits
    [-.\s]?  # Optional separator
    (\d{4})  # Last 4 digits
    """, re.VERBOSE)  # Using the VERBOSE flag to allow comments and formatting in the regex

# Example phone number to test against the pattern
phone = "123-456-7890"
match = phone_pattern.match(phone)  # The match method checks if the pattern matches from the start of the string
if match:
    print(match.groups())  # Output: ('123', '456', '7890')
# The 'match' object contains the captured groups, providing a structured output of the phone number components.

# Advanced tip:
# Use the VERBOSE flag to document complex patterns directly within the regex. This aids collaboration and maintenance,
# making it easier for other developers to understand the intent and structure of the regex without requiring separate documentation.

# Potential pitfalls:
# Overusing the VERBOSE flag can lead to confusion if not maintained properly. Always ensure that comments are clear
# and relevant to the parts of the regex they describe.
# Additionally, when using MULTILINE mode, ensure the input string is formatted correctly; otherwise, patterns may yield unexpected results.

#===============================================================================
# 7. Substitution and Splitting
#===============================================================================

# In this section, we explore text manipulation using regular expressions (regex) in Python.
# Regular expressions provide powerful capabilities for searching, matching, and modifying strings.

import re  # Import the re module, which contains functions and classes for working with regular expressions

# Example 1: Basic substitution
# In this example, we demonstrate simple text substitution.
# The 're.sub()' function replaces all occurrences of the first argument (a regex pattern) with the second argument.
text = "I love cats, but I'm allergic to cats."  # Original text containing the word 'cats'
new_text = re.sub(r"cats", "dogs", text)  # Replace 'cats' with 'dogs'
print(new_text)  # Output: I love dogs, but I'm allergic to dogs.
# This is useful for general text replacement, ensuring all instances of the matched pattern are updated.

# Use case:
# Basic substitution can be useful in various applications, such as updating user inputs, transforming log messages,
# or even modifying configuration files for compatibility with different systems.

# Example 2: Substitution with backreferences
# This example shows how to use backreferences in substitution.
# Backreferences allow you to refer to parts of the matched string in the replacement string.
text = "John Doe and Jane Doe"  # Text with names to be rearranged
# The pattern '(\w+) (\w+)' captures two groups: first name and last name.
# The replacement string r"\2, \1" uses the second captured group (last name) and the first captured group (first name).
new_text = re.sub(r"(\w+) (\w+)", r"\2, \1", text)  # Rearrange names to "Last, First" format
print(new_text)  # Output: Doe, John and Doe, Jane
# This is particularly powerful when processing structured data formats, allowing for flexible rearrangements.

# Use case:
# Substitution with backreferences is commonly used in text processing tasks such as formatting names, restructuring addresses,
# or transforming data before storage or analysis.

# Example 3: Splitting with regex
# This example illustrates how to split a string into a list using regex.
# The 're.split()' function allows you to specify a regex pattern as the delimiter for splitting.
text = "apple,banana;cherry:date"  # Comma, semicolon, and colon as delimiters
# The regex pattern '[,;:]' matches any of the specified characters.
# The text will be split wherever these delimiters occur.
print(re.split(r"[,;:]", text))  # Output: ['apple', 'banana', 'cherry', 'date']
# Splitting with regex is useful when dealing with structured data that may contain various delimiters.

# Use case:
# This approach is ideal for parsing CSV-like data formats, extracting tokens from log entries,
# or any situation where data may be separated by multiple types of delimiters.

# Tip: 
# Use substitution for text transformation to modify or enhance strings based on patterns,
# and splitting for parsing structured text into manageable components. Regular expressions can handle complex patterns,
# but ensure to test regex patterns thoroughly as they can lead to unexpected results if not properly defined.

#===============================================================================
# 8. Greedy vs. Non-Greedy Matching
#===============================================================================

# In regular expressions, the distinction between greedy and non-greedy (or lazy) matching
# is crucial for accurately capturing patterns in strings.
# Greedy matching attempts to match as much of the string as possible,
# while non-greedy matching captures the smallest possible string that satisfies the pattern.

# Example 1: Greedy matching
import re  # Import the regular expression module

# Sample text containing HTML-like tags
text = "<p>This is a <b>bold</b> paragraph</p>"

# Greedy pattern: <.*>
# The pattern <.*> matches the opening '<', followed by any character (.), zero or more times (*),
# and ends with the closing '>'.
# Since the quantifier '*' is greedy, it captures everything from the first '<' to the last '>'.
pattern = r"<.*>"
print(re.findall(pattern, text))  # Output: ['<p>This is a <b>bold</b> paragraph</p>']

# The output shows that the entire string is captured, which may not be the desired behavior
# when looking to extract individual tags.

# Use case for greedy matching:
# Greedy matching can be useful when you want to retrieve large sections of text
# or when you are certain that the string will not contain nested patterns.

# Example 2: Non-greedy matching
# Non-greedy pattern: <.*?>
# The pattern <.*?> is similar to the greedy pattern, but the '?' following '*' makes it non-greedy.
# It matches the opening '<', followed by any character (.), zero or more times (*),
# but stops matching as soon as it finds the first '>' due to the '?'.
pattern = r"<.*?>"
print(re.findall(pattern, text))  # Output: ['<p>', '<b>', '</b>', '</p>']

# The output shows individual tags captured, demonstrating that non-greedy matching
# successfully extracts the smallest segments of interest.

# Use case for non-greedy matching:
# Non-greedy matching is especially useful when parsing HTML or XML,
# where you want to retrieve each tag without consuming the entire text content.

# Advanced tip:
# When dealing with complex nested structures, consider using libraries designed for parsing
# such as Beautiful Soup for HTML/XML. Regular expressions can become cumbersome
# and may not handle all edge cases properly.

# Potential pitfalls:
# Using greedy matching unintentionally can lead to unexpected results,
# especially in data extraction tasks. Always test patterns on sample data
# to ensure they yield the intended results. Additionally, be aware that overly complex
# regular expressions can impact performance, so keep them as simple and efficient as possible.

#===============================================================================
# 9. Advanced Techniques
#===============================================================================

# In this section, we explore advanced techniques in regular expressions (regex) that provide more control and efficiency 
# when performing pattern matching. Understanding these techniques can enhance your ability to solve complex text processing tasks.

# 1. Conditional patterns
# Conditional patterns allow you to specify alternate matching behaviors based on previous matches.
# In this example, we define a pattern to match a specific format of numbers, either a Social Security Number (SSN) or a simple sequence of digits.

import re

# Pattern explanation:
# - (\d{3}) captures the first three digits (e.g., area code).
# - (-?) captures an optional hyphen.
# - (?(\2)\d{2}-?\d{4}|\d{4}) is a conditional pattern:
#   - If the second captured group (the hyphen) matches (i.e., it's present), it expects two digits followed by an optional hyphen and then four digits (e.g., "123-45-6789").
#   - If not, it simply expects four digits (e.g., "1234567").
pattern = r"(\d{3})(-?)(?(\2)\d{2}-?\d{4}|\d{4})"

# Testing the pattern with two examples
print(re.match(pattern, "123-45-6789").group())  # Output: 123-45-6789
print(re.match(pattern, "1234567").group())      # Output: 1234567

# Use case:
# This technique is beneficial when validating formats with optional components or varying structures,
# such as validating user input where certain formats might depend on previous entries.

# 2. Atomic grouping
# Atomic grouping is used to create a portion of a regex that does not backtrack,
# which can improve performance by preventing the regex engine from re-evaluating previously matched groups.

# Pattern explanation:
# - a(?>bc|b)c: This pattern will match 'a', then either 'bc' or 'b' (but will not backtrack).
# If it matches 'b', it expects a 'c' immediately after, leading to no ambiguity.
pattern = r"a(?>bc|b)c"

# Testing the pattern with two examples
print(re.match(pattern, "abcc"))  # Output: None
# Here, it fails because after matching 'a' and 'b', 'c' is expected, but 'cc' follows.
print(re.match(pattern, "abc"))   # Output: <re.Match object; span=(0, 3), match='abc'>
# This matches because 'a' followed by 'bc' satisfies the pattern.

# Use case:
# Atomic grouping is particularly useful in performance-sensitive applications where backtracking could lead to exponential runtime.

# 3. Possessive quantifiers
# Possessive quantifiers are greedy but do not allow backtracking, meaning they will consume as much input as possible 
# without giving up any matched characters. This can lead to more efficient matches but can also cause failures 
# in patterns that require flexibility.

# Pattern explanation:
# - a++b: This pattern looks for 'a' followed by one or more 'a's and then 'b'.
# Since it's possessive, if the sequence doesn't end with 'b', it won't backtrack to try matching less.
pattern = r"a++b"

# Testing the pattern with an example
print(re.match(pattern, "aaab"))  # Output: None
# This fails because the possessive quantifier consumes all 'a's, and no 'b' follows immediately after them.

# Use case:
# Possessive quantifiers are useful when you're certain that the input will fit the pattern strictly without requiring flexibility,
# helping to reduce backtracking and improve matching efficiency.

# Tip: 
# These advanced techniques can be powerful tools for complex pattern matching and optimization. 
# However, they should be used judiciously; improper use can lead to confusion and harder-to-maintain code.
# Always validate regex patterns against a range of expected input to ensure they behave as intended.

#===============================================================================
# 10. Working with URLs
#===============================================================================

# In this section, we demonstrate how to work with URLs in Python using regular expressions.
# Regular expressions provide a powerful way to search for and manipulate string patterns.

import re  # Import the 're' module for regular expressions

# Compile a regex pattern to match URLs with specific components:
url_pattern = re.compile(
    r"(?P<protocol>https?://)"  # Match the protocol: 'http://' or 'https://'
    r"(?P<domain>[\w.-]+)"      # Match the domain: includes alphanumeric characters, dots, and hyphens
    r"(?P<path>/[\w./]*)"       # Match the path: starts with '/', followed by alphanumeric characters, dots, or slashes
)

# Example URL to test against the regex pattern
url = "https://www.example.com/path/to/page.html"  # A valid HTTPS URL

# Attempt to match the URL against the compiled pattern
match = url_pattern.match(url)  # Returns a match object if the URL conforms to the pattern

if match:  # Check if a match was found
    # If the match is successful, extract the different components using named groups
    print(f"Protocol: {match.group('protocol')}")  # Output the protocol (http or https)
    print(f"Domain: {match.group('domain')}")      # Output the domain name
    print(f"Path: {match.group('path')}")          # Output the path in the URL

# Output:
# Protocol: https://
# Domain: www.example.com
# Path: /path/to/page.html

# Use case:
# This pattern is useful for parsing URLs in web scraping, API calls, or any application 
# where URL validation or extraction is necessary.

# Advanced tip:
# Consider using more comprehensive regex patterns to capture query strings, fragments, 
# or even port numbers, depending on the URL structure you expect. 
# For instance, you can enhance the pattern to capture a query string as follows:
url_pattern_with_query = re.compile(
    r"(?P<protocol>https?://)"
    r"(?P<domain>[\w.-]+)"
    r"(?P<path>/[\w./]*)"
    r"(?:\?(?P<query>[^#]*))?"  # Optional: match query string starting with '?' if present
)

# Example with a query string
url_with_query = "https://www.example.com/path/to/page.html?search=query"
match_with_query = url_pattern_with_query.match(url_with_query)

if match_with_query:
    print(f"Protocol: {match_with_query.group('protocol')}")
    print(f"Domain: {match_with_query.group('domain')}")
    print(f"Path: {match_with_query.group('path')}")
    print(f"Query: {match_with_query.group('query')}")  # Extract and print the query string if available

# Output for the example with a query string:
# Protocol: https://
# Domain: www.example.com
# Path: /path/to/page.html
# Query: search=query

# Potential pitfalls:
# Be cautious of overly complex regex patterns as they can become difficult to read and maintain.
# Also, ensure that the regex adequately covers the possible variations of the URLs you expect 
# to process, as missing edge cases can lead to incorrect parsing.

#===============================================================================
# 11. Email Validation
#===============================================================================

# Email validation is a common task in applications to ensure that user-provided email addresses are correctly formatted.
# Regular expressions (regex) offer a powerful way to validate the structure of email addresses.

# Here we compile a regex pattern to match valid email formats.
import re  # Importing the regex module to work with regular expressions

# Define a regex pattern for validating emails. The 're.VERBOSE' flag allows for multi-line regex with comments.
email_pattern = re.compile(r"""
    ^                   # Start of string
    [\w\.-]+            # Username: One or more word characters (alphanumeric + underscore), dots, or hyphens
    @                   # @ symbol separates username and domain
    [\w\.-]+            # Domain name: One or more word characters, dots, or hyphens
    \.                  # Dot that precedes the top-level domain (TLD)
    [a-zA-Z]{2,}        # Top-level domain: At least two alphabetic characters (e.g., .com, .co.uk)
    $                   # End of string
""", re.VERBOSE)

# List of example email addresses for validation
emails = ["user@example.com", "invalid.email@com", "another_user@sub.domain.co.uk"]

# Iterate through each email address to validate its format against the regex pattern
for email in emails:
    if email_pattern.match(email):  # Use 'match()' to check if the email conforms to the regex pattern
        print(f"Valid email: {email}")  # If valid, print the email
    else:
        print(f"Invalid email: {email}")  # If invalid, print a message indicating it's invalid

# Output:
# Valid email: user@example.com
# Invalid email: invalid.email@com
# Valid email: another_user@sub.domain.co.uk

# Use case:
# This email validation technique is useful in web forms where users are required to enter their email addresses.
# It helps prevent errors during email communication and ensures data integrity.

# Advanced tip:
# Consider expanding the regex pattern to cover edge cases, such as internationalized domain names (IDN) or specific TLDs.
# Additionally, using a dedicated email validation library (like 'validate_email') can handle more complex rules and improve accuracy.

# Potential pitfalls:
# Regex can sometimes produce false positives or negatives. For instance, the regex above might accept some invalid emails.
# Always keep in mind that the only definitive way to validate an email address is through a confirmation process (e.g., sending a verification email).
# Moreover, regex patterns can become complex and hard to read if not structured well. Maintaining clarity in regex is crucial for future modifications.

#===============================================================================
# 12. Performance Considerations
#===============================================================================

# Performance considerations are crucial when dealing with string searching and manipulation,
# especially when the input size is large. The following examples demonstrate how to measure 
# the performance of different string searching techniques using the timeit module.

import timeit  # Importing the timeit module for performance measurement

# Create a large text string consisting of one million 'a's followed by a single 'b'
text = "a" * 1000000 + "b"  

# Example 1: Using regex to search for 'b' in the text
def find_with_regex():
    # Using regex search to find 'b' in the text
    return re.search(r"b", text) is not None  # Returns True if 'b' is found

# Example 2: Using string containment to search for 'b'
def find_with_string():
    # Simple containment check to see if 'b' is in the text
    return "b" in text  # Returns True if 'b' is present in the text

# Measuring the execution time for each search method
print("Regex:", timeit.timeit(find_with_regex, number=100))  # Time taken for regex search
print("String:", timeit.timeit(find_with_string, number=100))  # Time taken for string containment

# Tip: For simple string matching, built-in string methods are often faster than regex
# This demonstrates that regex can be more resource-intensive compared to straightforward string operations.

# Best Practices and Tips for Using Regular Expressions:

# 1. Use raw strings (r"...") for regex patterns to avoid escaping backslashes.
# Raw strings treat backslashes as literal characters, which prevents the need for double escaping.
pattern = r"\d+"  # Matches one or more digits without needing to escape the backslash

# 2. Compile regex patterns that are used multiple times for better performance.
# Compiling a regex pattern before using it multiple times can significantly improve speed.
compiled_pattern = re.compile(r"b")  # Precompiled regex pattern
print(compiled_pattern.search(text))  # Use the compiled pattern to search

# 3. Use named groups for better readability and easier access to matched groups.
# Named groups improve the clarity of regex patterns and allow accessing matches by name.
named_pattern = r"(?P<digit>\d+)"  # Named group 'digit'
match = re.search(named_pattern, "123abc")
print(match.group("digit"))  # Accessing matched group by name

# 4. Be careful with greedy quantifiers; use non-greedy versions when appropriate.
# Greedy quantifiers match as much as possible; non-greedy quantifiers match the least.
greedy_pattern = r"<.*>"  # Greedy
non_greedy_pattern = r"<.*?>"  # Non-greedy
text = "<tag>Content</tag>"
print(re.search(greedy_pattern, text).group())  # Matches: <tag>Content</tag>
print(re.search(non_greedy_pattern, text).group())  # Matches: <tag>

# 5. Use anchors and word boundaries to ensure precise matching.
# Anchors (^ and $) ensure that matches occur at the start or end of a string.
# Word boundaries (\b) ensure matches occur at the edges of words.
boundary_pattern = r"\bword\b"  # Matches the whole word 'word'
print(re.search(boundary_pattern, "A word is here.").group())  # Matches: word

# 6. Leverage lookahead and lookbehind assertions for complex matching requirements.
# Lookaheads and lookbehinds allow for matching based on conditions that come before or after the match.
lookahead_pattern = r"foo(?=bar)"  # Matches 'foo' only if followed by 'bar'
print(re.search(lookahead_pattern, "foobar"))  # Matches: foo

# 7. Use verbose mode (re.VERBOSE) for complex patterns to improve readability.
# Verbose mode allows adding whitespace and comments to regex patterns for better clarity.
verbose_pattern = r"""
    (?P<area>\d+)  # Area code
    -              # Separator
    (?P<number>\d+)  # Number
"""
print(re.search(verbose_pattern, "123-4567", re.VERBOSE).group())  # Matches: 123-4567

# 8. Be aware of the performance implications of complex regex patterns.
# Complex patterns can lead to slower performance and increased memory usage.
# Always evaluate if the complexity is necessary.

# 9. Test your regex patterns with various inputs, including edge cases.
# Thorough testing helps ensure patterns work as expected across different scenarios.
# Consider inputs with special characters, varying lengths, and formats.

# 10. Use online regex testers (like regex101.com) for debugging and visualization.
# These tools provide immediate feedback on regex behavior and help identify issues.

# 11. Remember that regex is powerful but not always the best solution; consider alternatives for simple string operations.
# For basic tasks, using string methods (like str.find()) can be more efficient and simpler.

# 12. Use character classes and quantifiers to create more flexible patterns.
# Character classes ([abc]) allow matching any character in the set; quantifiers (e.g., *, +, ?) define repetition.
char_class_pattern = r"[aeiou]+"  # Matches one or more vowels
print(re.search(char_class_pattern, "hello").group())  # Matches: e

# 13. Understand the difference between match(), search(), and findall() methods.
# - match() checks for a match only at the start of the string.
# - search() checks for a match anywhere in the string.
# - findall() returns all non-overlapping matches of the pattern in a string.
print(re.match(r"a", "apple"))  # Match at the start
print(re.search(r"e", "apple"))  # Search anywhere
print(re.findall(r"l", "apple"))  # Find all occurrences

# 14. Use flags like re.IGNORECASE and re.MULTILINE when needed for more flexible matching.
# Flags adjust how the regex engine processes patterns, allowing for case-insensitive or multi-line matches.
ignore_case_pattern = r"hello"
print(re.search(ignore_case_pattern, "HELLO", re.IGNORECASE).group())  # Matches: HELLO

# 15. Be cautious with patterns that can lead to catastrophic backtracking.
# Complex patterns with nested quantifiers can cause performance degradation and slow execution.
# Always analyze regex patterns for potential performance issues and optimize them where possible.

# This concludes the enhanced detailed Python Cheat Sheet for Regular Expressions