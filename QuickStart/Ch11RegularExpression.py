#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Regular Expressions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re

# 1. Basic Patterns and Character Classes

# Basic matching
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")  # Output: Found: hello

# Tip: Use raw strings (r"...") for regex patterns to avoid escaping backslashes

# Character classes
digit_pattern = r"\d+"  # Matches one or more digits
word_pattern = r"\w+"  # Matches one or more word characters
space_pattern = r"\s+"  # Matches one or more whitespace characters

text = "The year is 2023, and the price is $19.99"
print("Digits:", re.findall(digit_pattern, text))  # Output: ['2023', '19', '99']
print("Words:", re.findall(word_pattern, text))   # Output: ['The', 'year', 'is', '2023', 'and', 'the', 'price', 'is', '19', '99']
print("Spaces:", re.findall(space_pattern, text)) # Output: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Custom character classes
vowel_pattern = r"[aeiou]"
not_digit_pattern = r"[^\d]"

print("Vowels:", re.findall(vowel_pattern, text.lower()))  # Output: ['e', 'e', 'a', 'i', 'a', 'e', 'i', 'e', 'i']
print("Non-digits:", re.findall(not_digit_pattern, text))  # Output: ['T', 'h', 'e', ' ', 'y', 'e', 'a', 'r', ' ', 'i', 's', ' ', ',', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'e', ' ', 'p', 'r', 'i', 'c', 'e', ' ', 'i', 's', ' ', '$', '.']

# Tip: Use character classes to match specific types of characters efficiently

# 2. Quantifiers

text = "The quick brown fox jumps over the lazy dog"

# Zero or more: *
print(re.findall(r"o*", text))  # Output: ['', 'o', '', '', '', '', 'o', '', '', '', '', 'o', '', '', '', '', '', '', '', '', '', 'o', '', '', '', '', '', '', '', '', '', '', 'o', '']

# One or more: +
print(re.findall(r"o+", text))  # Output: ['o', 'o', 'o', 'o', 'o']

# Zero or one: ?
print(re.findall(r"jumps?", text))  # Output: ['jumps']

# Exactly n: {n}
print(re.findall(r"\w{5}", text))  # Output: ['quick', 'brown', 'jumps']

# n or more: {n,}
print(re.findall(r"\w{4,}", text))  # Output: ['quick', 'brown', 'jumps', 'over', 'lazy']

# Between n and m: {n,m}
print(re.findall(r"\w{3,5}", text))  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# Tip: Use quantifiers to specify the number of occurrences of a pattern

# 3. Anchors and Boundaries

# Start of string: ^
print(re.findall(r"^The", text))  # Output: ['The']

# End of string: $
print(re.findall(r"dog$", text))  # Output: ['dog']

# Word boundary: \b
print(re.findall(r"\bfox\b", text))  # Output: ['fox']

# Tip: Use anchors to match patterns at specific positions in the text

# 4. Grouping and Capturing

# Basic grouping
pattern = r"(\d+)-(\d+)-(\d+)"
text = "Date: 2023-06-27"
match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
# Output: Year: 2023, Month: 06, Day: 27

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, text)
if match:
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")
# Output: Year: 2023, Month: 06, Day: 27

# Non-capturing groups
pattern = r"(?:Mr|Mrs|Ms)\s(\w+)"
text = "Mr Smith and Mrs Johnson"
matches = re.findall(pattern, text)
print(matches)  # Output: ['Smith', 'Johnson']

# Backreferences
pattern = r"(\w+)\s+\1"
text = "hello hello world world"
matches = re.findall(pattern, text)
print(matches)  # Output: ['hello', 'world']

# Tip: Use grouping for extracting specific parts of matched patterns and for creating more complex patterns

# 5. Lookahead and Lookbehind Assertions

# Positive lookahead
pattern = r"\d+(?=\s*dollars)"
text = "I have 50 dollars and 20 euros"
matches = re.findall(pattern, text)
print(matches)  # Output: ['50']

# Negative lookahead
pattern = r"\d+(?!\s*dollars)"
matches = re.findall(pattern, text)
print(matches)  # Output: ['20']

# Positive lookbehind
pattern = r"(?<=price:\s)\d+"
text = "The price: 100 dollars"
match = re.search(pattern, text)
if match:
    print(match.group())  # Output: 100

# Negative lookbehind
pattern = r"(?<!@)\b\w+\b"
text = "user@example.com and johndoe"
matches = re.findall(pattern, text)
print(matches)  # Output: ['and', 'johndoe']

# Tip: Use lookahead and lookbehind assertions for complex pattern matching without including the assertion in the match

# 6. Flags and Options

# Case-insensitive matching
pattern = re.compile(r"python", re.IGNORECASE)
print(pattern.search("PYTHON is awesome").group())  # Output: PYTHON

# Multiline mode
text = "Start\nEnd"
pattern = re.compile(r"^End", re.MULTILINE)
print(pattern.search(text).group())  # Output: End

# Verbose mode for readable patterns
phone_pattern = re.compile(r"""
    (\d{3})  # Area code
    [-.\s]?  # Optional separator
    (\d{3})  # First 3 digits
    [-.\s]?  # Optional separator
    (\d{4})  # Last 4 digits
    """, re.VERBOSE)

phone = "123-456-7890"
match = phone_pattern.match(phone)
if match:
    print(match.groups())  # Output: ('123', '456', '7890')

# Tip: Use flags to modify the behavior of regex patterns for more flexible matching

# 7. Substitution and Splitting

# Basic substitution
text = "I love cats, but I'm allergic to cats."
new_text = re.sub(r"cats", "dogs", text)
print(new_text)  # Output: I love dogs, but I'm allergic to dogs.

# Substitution with backreferences
text = "John Doe and Jane Doe"
new_text = re.sub(r"(\w+) (\w+)", r"\2, \1", text)
print(new_text)  # Output: Doe, John and Doe, Jane

# Splitting with regex
text = "apple,banana;cherry:date"
print(re.split(r"[,;:]", text))  # Output: ['apple', 'banana', 'cherry', 'date']

# Tip: Use substitution for text transformation and splitting for parsing structured text

# 8. Greedy vs. Non-Greedy Matching

# Greedy matching
text = "<p>This is a <b>bold</b> paragraph</p>"
pattern = r"<.*>"
print(re.findall(pattern, text))  # Output: ['<p>This is a <b>bold</b> paragraph</p>']

# Non-greedy matching
pattern = r"<.*?>"
print(re.findall(pattern, text))  # Output: ['<p>', '<b>', '</b>', '</p>']

# Tip: Use non-greedy matching (adding ? after quantifiers) when you want to match the smallest possible pattern

# 9. Advanced Techniques

# Conditional patterns
pattern = r"(\d{3})(-?)(?(\2)\d{2}-?\d{4}|\d{4})"
print(re.match(pattern, "123-45-6789").group())  # Output: 123-45-6789
print(re.match(pattern, "1234567").group())      # Output: 1234567

# Atomic grouping
pattern = r"a(?>bc|b)c"
print(re.match(pattern, "abcc"))  # Output: None
print(re.match(pattern, "abc"))   # Output: <re.Match object; span=(0, 3), match='abc'>

# Possessive quantifiers
pattern = r"a++b"
print(re.match(pattern, "aaab"))  # Output: None

# Tip: These advanced techniques can be used for complex pattern matching and optimization

# 10. Working with URLs

url_pattern = re.compile(
    r"(?P<protocol>https?://)"  # http:// or https://
    r"(?P<domain>[\w.-]+)"      # domain name
    r"(?P<path>/[\w./]*)"       # path
)

url = "https://www.example.com/path/to/page.html"
match = url_pattern.match(url)
if match:
    print(f"Protocol: {match.group('protocol')}")
    print(f"Domain: {match.group('domain')}")
    print(f"Path: {match.group('path')}")

# Output:
# Protocol: https://
# Domain: www.example.com
# Path: /path/to/page.html

# 11. Email Validation

email_pattern = re.compile(r"""
    ^                   # Start of string
    [\w\.-]+            # Username
    @                   # @ symbol
    [\w\.-]+            # Domain name
    \.                  # Dot
    [a-zA-Z]{2,}        # Top-level domain
    $                   # End of string
""", re.VERBOSE)

emails = ["user@example.com", "invalid.email@com", "another_user@sub.domain.co.uk"]
for email in emails:
    if email_pattern.match(email):
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")

# Output:
# Valid email: user@example.com
# Invalid email: invalid.email@com
# Valid email: another_user@sub.domain.co.uk

# 12. Performance Considerations

import timeit

text = "a" * 1000000 + "b"

def find_with_regex():
    return re.search(r"b", text) is not None

def find_with_string():
    return "b" in text

print("Regex:", timeit.timeit(find_with_regex, number=100))
print("String:", timeit.timeit(find_with_string, number=100))

# Tip: For simple string matching, built-in string methods are often faster than regex

# Best Practices and Tips:

# 1. Use raw strings (r"...") for regex patterns to avoid escaping backslashes.
# 2. Compile regex patterns that are used multiple times for better performance.
# 3. Use named groups for better readability and easier access to matched groups.
# 4. Be careful with greedy quantifiers; use non-greedy versions when appropriate.
# 5. Use anchors and word boundaries to ensure precise matching.
# 6. Leverage lookahead and lookbehind assertions for complex matching requirements.
# 7. Use verbose mode (re.VERBOSE) for complex patterns to improve readability.
# 8. Be aware of the performance implications of complex regex patterns.
# 9. Test your regex patterns with various inputs, including edge cases.
# 10. Use online regex testers (like regex101.com) for debugging and visualization.
# 11. Remember that regex is powerful but not always the best solution; consider alternatives for simple string operations.
# 12. Use character classes and quantifiers to create more flexible patterns.
# 13. Understand the difference between match(), search(), and findall() methods.
# 14. Use flags like re.IGNORECASE and re.MULTILINE when needed for more flexible matching.
# 15. Be cautious with patterns that can lead to catastrophic backtracking.

# This concludes the enhanced detailed Python Cheat Sheet for Regular Expressions