"""
Python Standard Library - re (regular expressions) module - in the Python Programming Language
==============================================================================================

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
----------------------------------
The 're' module in Python provides support for regular expressions (regex). Regular expressions are powerful tools for pattern matching and text manipulation. They allow developers to search, extract, and modify strings based on complex patterns.

Historical context:
- Regular expressions have roots in formal language theory and were first developed by mathematician Stephen Cole Kleene in the 1950s.
- The 're' module was introduced in Python 1.5 (1997) as a more powerful replacement for the earlier 'regex' module.
- It has undergone several improvements over the years, with significant updates in Python 3.x versions.

Significance:
- Regular expressions provide a concise and flexible means for matching strings of text.
- They are essential for tasks such as data validation, parsing, and text processing.
- The 're' module offers a Pythonic interface to work with regular expressions efficiently.

Common use cases:
- Validating input (e.g., email addresses, phone numbers)
- Parsing and extracting information from text
- Search and replace operations
- Text preprocessing in natural language processing tasks

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import re
import time
from typing import List, Tuple, Optional

def basic_regex_operations():
    """Demonstrate basic regex operations using the re module."""
    
    # Simple pattern matching
    pattern = r"python"
    text = "I love Python programming!"
    match = re.search(pattern, text, re.IGNORECASE)
    print(f"1. Simple match: {'Found' if match else 'Not found'}")
    
    # Using character classes
    pattern = r"[aeiou]"
    text = "Python"
    matches = re.findall(pattern, text, re.IGNORECASE)
    print(f"2. Vowels found: {matches}")
    
    # Using quantifiers
    pattern = r"\d+"
    text = "There are 123 apples and 456 oranges."
    matches = re.findall(pattern, text)
    print(f"3. Numbers found: {matches}")
    
    # Using groups
    pattern = r"(\w+)@(\w+)\.(\w+)"
    text = "Contact us at info@example.com or support@python.org"
    matches = re.findall(pattern, text)
    print(f"4. Email parts: {matches}")

def advanced_regex_operations():
    """Demonstrate advanced regex operations using the re module."""
    
    # Lookahead and lookbehind assertions
    pattern = r"(?<=@)\w+(?=\.com)"
    text = "user@example.com and admin@python.com"
    matches = re.findall(pattern, text)
    print(f"1. Domain names: {matches}")
    
    # Non-capturing groups
    pattern = r"(?:https?://)?(?:www\.)?([\w-]+)\.com"
    text = "Visit https://www.example.com or http://python.com"
    matches = re.findall(pattern, text)
    print(f"2. Extracted domains: {matches}")
    
    # Named groups
    pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
    text = "The event is on 2023-09-15"
    match = re.search(pattern, text)
    if match:
        print(f"3. Date parts: {match.groupdict()}")
    
    # Backreferences
    pattern = r"(\w+)\s+\1"
    text = "The the cat cat is is sleepy sleepy"
    matches = re.findall(pattern, text)
    print(f"4. Repeated words: {matches}")

def regex_compilation_and_flags():
    """Demonstrate regex compilation and the use of flags."""
    
    # Compiling a regex pattern
    pattern = re.compile(r"\b\w+\b", re.IGNORECASE)
    text = "Hello, World! How are you?"
    matches = pattern.findall(text)
    print(f"1. Words found: {matches}")
    
    # Using multiple flags
    pattern = re.compile(r"^python.*$", re.MULTILINE | re.IGNORECASE)
    text = """
    Python is great
    Java is also good
    But PYTHON is my favorite
    """
    matches = pattern.findall(text)
    print(f"2. Lines starting with 'python': {matches}")

def regex_substitution():
    """Demonstrate regex substitution operations."""
    
    # Simple substitution
    text = "The color of the sky is blue. The color of grass is green."
    pattern = r"color"
    replacement = "colour"
    new_text = re.sub(pattern, replacement, text)
    print(f"1. After substitution: {new_text}")
    
    # Substitution with backreferences
    text = "John Doe, Jane Smith, Bob Johnson"
    pattern = r"(\w+)\s+(\w+)"
    replacement = r"\2, \1"
    new_text = re.sub(pattern, replacement, text)
    print(f"2. Names reversed: {new_text}")
    
    # Substitution with a function
    def capitalize_group(match):
        return match.group(1).upper()
    
    text = "python java ruby"
    pattern = r"\b(\w+)\b"
    new_text = re.sub(pattern, capitalize_group, text)
    print(f"3. Capitalized words: {new_text}")

class EmailValidator:
    """A class to demonstrate real-world usage of regex for email validation."""
    
    EMAIL_PATTERN = re.compile(r"""
        ^                           # Start of string
        [\w\.-]+                    # Username (alphanumeric, dot, hyphen)
        @                           # @ symbol
        [\w\.-]+                    # Domain name
        \.                          # Dot
        [a-zA-Z]{2,}                # Top-level domain (at least 2 characters)
        $                           # End of string
    """, re.VERBOSE)
    
    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        """Validate an email address."""
        return bool(cls.EMAIL_PATTERN.match(email))
    
    @classmethod
    def extract_domain(cls, email: str) -> Optional[str]:
        """Extract the domain from a valid email address."""
        match = cls.EMAIL_PATTERN.match(email)
        if match:
            return match.group().split('@')[1]
        return None

def demonstrate_email_validation():
    """Demonstrate email validation using the EmailValidator class."""
    emails = [
        "user@example.com",
        "invalid.email@com",
        "another.user@sub.domain.co.uk",
        "not_an_email",
    ]
    
    for email in emails:
        is_valid = EmailValidator.is_valid_email(email)
        domain = EmailValidator.extract_domain(email) if is_valid else None
        print(f"Email: {email}")
        print(f"  Valid: {is_valid}")
        print(f"  Domain: {domain}")
        print()

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Compile regex patterns that are used frequently to improve performance.
2. Use raw strings (r"pattern") to avoid issues with backslashes.
3. Use verbose mode (re.VERBOSE) for complex patterns to improve readability.
4. Be specific with your patterns to avoid over-matching.
5. Use non-capturing groups (?:...) when you don't need the group content.

Common Pitfalls:
1. Greedy vs. non-greedy quantifiers: Use '?' after quantifiers for non-greedy matching.
2. Forgetting to escape special characters: Always escape metacharacters like '.', '*', '+'.
3. Overusing regex: For simple string operations, built-in string methods might be faster.
4. Catastrophic backtracking: Be careful with nested quantifiers that can lead to exponential time complexity.

Advanced Tips:
1. Use lookahead and lookbehind assertions for complex matching without consuming characters.
2. Leverage named groups for more readable and maintainable regex patterns.
3. Use the re.DEBUG flag to understand how your regex pattern is interpreted.
4. For large files, use re.finditer() instead of re.findall() to save memory.
"""

def regex_best_practices():
    """Demonstrate regex best practices and advanced techniques."""
    
    # Using verbose mode for complex patterns
    pattern = re.compile(r"""
        \b                  # Word boundary
        (?P<area>\d{3})     # Area code
        [-.]?               # Optional separator
        (?P<prefix>\d{3})   # Prefix
        [-.]?               # Optional separator
        (?P<line>\d{4})     # Line number
        \b                  # Word boundary
    """, re.VERBOSE)
    
    phone_numbers = [
        "123-456-7890",
        "987.654.3210",
        "1234567890",
        "123-4567",  # Invalid
    ]
    
    for number in phone_numbers:
        match = pattern.match(number)
        if match:
            print(f"Valid number: {number}")
            print(f"  Parts: {match.groupdict()}")
        else:
            print(f"Invalid number: {number}")
        print()
    
    # Demonstrating lookahead
    pattern = re.compile(r"\b\w+(?=ing\b)")
    text = "I enjoy running and swimming but not falling."
    matches = pattern.findall(text)
    print(f"Words before 'ing': {matches}")

def regex_pitfalls():
    """Demonstrate common regex pitfalls and how to avoid them."""
    
    # Greedy vs. non-greedy matching
    text = "<p>First paragraph</p><p>Second paragraph</p>"
    greedy_pattern = r"<p>.*</p>"
    non_greedy_pattern = r"<p>.*?</p>"
    
    print("Greedy matching:")
    print(re.findall(greedy_pattern, text))
    print("Non-greedy matching:")
    print(re.findall(non_greedy_pattern, text))
    
    # Catastrophic backtracking example
    def measure_time(func):
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result
    
    text = "a" * 25 + "!"
    bad_pattern = re.compile(r"(a+)+!")
    good_pattern = re.compile(r"a+!")
    
    print("\nCatastrophic backtracking:")
    measure_time(lambda: bad_pattern.match(text))
    
    print("\nOptimized pattern:")
    measure_time(lambda: good_pattern.match(text))

"""
4. Integration and Real-World Applications
------------------------------------------
Regular expressions are widely used in various Python libraries and frameworks:

1. Django: Form validation, URL routing
2. Flask: Route definitions
3. Pandas: String methods for data cleaning and manipulation
4. Beautiful Soup: Advanced HTML parsing
5. Natural Language Toolkit (NLTK): Text processing and tokenization

Real-world example: Log parsing and analysis
"""

import csv
from collections import Counter

def parse_log_file(file_path: str) -> List[Tuple[str, str, str]]:
    """Parse a log file and extract timestamp, log level, and message."""
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)")
    parsed_logs = []
    
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                parsed_logs.append(match.groups())
    
    return parsed_logs

def analyze_logs(logs: List[Tuple[str, str, str]]) -> None:
    """Analyze parsed logs and print summary statistics."""
    log_levels = Counter(log[1] for log in logs)
    print("Log level distribution:")
    for level, count in log_levels.items():
        print(f"  {level}: {count}")
    
    error_logs = [log for log in logs if log[1] == 'ERROR']
    print(f"\nTotal ERROR logs: {len(error_logs)}")
    
    if error_logs:
        print("Sample ERROR messages:")
        for log in error_logs[:5]:
            print(f"  {log[0]}: {log[2][:50]}...")

def demonstrate_log_analysis():
    """Demonstrate log file parsing and analysis."""
    # Create a sample log file
    sample_logs = [
        "2023-09-15 10:30:15 - INFO - Application started",
        "2023-09-15 10:31:22 - DEBUG - Processing user request",
        "2023-09-15 10:32:01 - ERROR - Database connection failed",
        "2023-09-15 10:32:45 - WARNING - High memory usage detected",
        "2023-09-15 10:33:10 - INFO - User logged in: john_doe",
        "2023-09-15 10:34:30 - ERROR - Invalid API key: XYZ123",
    ]
    
    with open('sample.log', 'w') as file:
        for log in sample_logs:
            file.write(log + '\n')
    
    # Parse and analyze logs
    parsed_logs = parse_log_file('sample.log')
    analyze_logs(parsed_logs)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Regex engines: Understanding different regex engines (NFA vs. DFA) and their performance characteristics.
2. Unicode support: Handling international text and special characters in regex patterns.
3. Fuzzy matching: Implementing approximate string matching using regex libraries like `regex`.
4. Machine learning integration: Using regex features for feature extraction in text classification tasks.
"""

def demonstrate_unicode_regex():
    """Demonstrate regex operations with Unicode characters."""
    text = "Python est génial! 🐍 是很棒的编程语言。"
    
    # Match non-ASCII words
    pattern = r'\b\w+\b'
    matches = re.findall(pattern, text, re.UNICODE)
    print(f"1. All words: {matches}")
    
    # Match specific Unicode ranges (e.g., Chinese characters)
    pattern = r'[\u4e00-\u9fff]+'
    matches = re.findall(pattern, text)
    print(f"2. Chinese characters: {matches}")
    
    # Match emojis
    pattern = r'[\U0001F300-\U0001F5FF]'
    matches = re.findall(pattern, text)
    print(f"3. Emojis: {matches}")

"""
6. FAQs and Troubleshooting
---------------------------
Q1: How do I match a literal dot (.) in a regex pattern?
A1: Use a backslash to escape the dot: \. or use re.escape() for any string.


Q2: What's the difference between re.match() and re.search()?
A2: re.match() checks for a match only at the beginning of the string, while re.search() scans the entire string for a match.

Q3: How can I make my regex case-insensitive?
A3: Use the re.IGNORECASE flag or (?i) inline flag.

Q4: Why is my regex pattern matching more than I expected?
A4: This could be due to greedy quantifiers. Try using non-greedy quantifiers by adding a ? after *, +, or {}.

Q5: How can I improve the performance of my regex operations?
A5: Compile frequently used patterns with re.compile(), use more specific patterns, and avoid excessive backtracking.

Troubleshooting guide:
1. Regex not matching as expected:
   - Double-check your pattern for errors
   - Use raw strings (r"pattern") to avoid issues with backslashes
   - Test your regex using online tools like regex101.com

2. Slow regex performance:
   - Look for nested quantifiers that might cause catastrophic backtracking
   - Use more specific patterns to reduce the search space
   - Consider alternative non-regex solutions for simple string operations

3. Unicode-related issues:
   - Ensure you're using the re.UNICODE flag or inline flag (?u)
   - For Python 3.x, 'str' objects are already Unicode, so this is less of an issue

4. Capturing groups not working:
   - Make sure you're using parentheses () for capturing groups
   - Check that you're not using non-capturing groups (?:...) unintentionally
"""

def demonstrate_faq_solutions():
    """Demonstrate solutions to common regex FAQs."""
    
    # Q1: Matching a literal dot
    text = "file.txt and file_doc.pdf"
    pattern = r'\b\w+\.\w+\b'
    matches = re.findall(pattern, text)
    print(f"1. Files with extensions: {matches}")
    
    # Q2: re.match() vs re.search()
    text = "Python is awesome. Python is powerful."
    print(f"2. re.match(): {'Python' if re.match('Python', text) else 'No match'}")
    print(f"   re.search(): {'awesome' if re.search('awesome', text) else 'No match'}")
    
    # Q3: Case-insensitive matching
    text = "PYTHON is awesome. python is powerful."
    pattern = re.compile(r'python', re.IGNORECASE)
    matches = pattern.findall(text)
    print(f"3. Case-insensitive matches: {matches}")
    
    # Q4: Greedy vs non-greedy matching
    text = "<p>First paragraph</p><p>Second paragraph</p>"
    greedy_pattern = r'<p>.*</p>'
    non_greedy_pattern = r'<p>.*?</p>'
    print(f"4. Greedy matching: {re.findall(greedy_pattern, text)}")
    print(f"   Non-greedy matching: {re.findall(non_greedy_pattern, text)}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. regex: A drop-in replacement for re with additional features
2. pyregex: GUI tool for testing Python regex patterns
3. regex101.com: Online regex tester and debugger
4. PyRegex: Another online Python regex tester
5. rexpy: Automatic regex generation from examples

Resources:
- "Mastering Regular Expressions" by Jeffrey Friedl
- "Regular Expression Cookbook" by Jan Goyvaerts and Steven Levithan
- Python's official documentation on the re module: https://docs.python.org/3/library/re.html
- Regular-Expressions.info: Comprehensive regex tutorial and reference
- RegexOne: Interactive regex tutorial
- Google's Python Class - Regular Expressions: https://developers.google.com/edu/python/regular-expressions

8. Performance Analysis and Optimization
----------------------------------------
When working with regular expressions, it's crucial to consider their performance implications, especially in performance-critical applications.
"""

def benchmark_regex_operations(text: str, pattern: str, iterations: int = 100000):
    """Benchmark regex operations."""
    compiled_pattern = re.compile(pattern)
    
    def test_search():
        return re.search(pattern, text)
    
    def test_compiled_search():
        return compiled_pattern.search(text)
    
    def test_findall():
        return re.findall(pattern, text)
    
    def test_compiled_findall():
        return compiled_pattern.findall(text)
    
    tests = [
        ("re.search", test_search),
        ("compiled search", test_compiled_search),
        ("re.findall", test_findall),
        ("compiled findall", test_compiled_findall),
    ]
    
    for name, test_func in tests:
        start_time = time.time()
        for _ in range(iterations):
            test_func()
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.4f} seconds")

def optimize_regex_pattern(text: str, patterns: List[str]) -> None:
    """Compare and optimize regex patterns."""
    for i, pattern in enumerate(patterns, 1):
        compiled_pattern = re.compile(pattern)
        start_time = time.time()
        matches = compiled_pattern.findall(text)
        end_time = time.time()
        print(f"Pattern {i}: {pattern}")
        print(f"  Matches: {len(matches)}")
        print(f"  Time: {end_time - start_time:.6f} seconds")
        print()

def demonstrate_performance_optimization():
    """Demonstrate performance analysis and optimization techniques."""
    print("Benchmarking regex operations:")
    text = "The quick brown fox jumps over the lazy dog" * 1000
    pattern = r'\b\w{4}\b'
    benchmark_regex_operations(text, pattern)
    
    print("\nOptimizing regex patterns:")
    text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!"
    patterns = [
        r'(a+)+!',  # Catastrophic backtracking
        r'a+!',     # Optimized version
    ]
    optimize_regex_pattern(text, patterns)

"""
Performance Considerations:
1. Compilation: Compiling patterns with re.compile() is more efficient for repeated use.
2. Anchoring: Using ^ and $ to anchor patterns can significantly improve performance.
3. Alternation: Order alternations from most to least specific (e.g., |foo|f| instead of |f|foo|).
4. Capturing: Use non-capturing groups (?:...) when you don't need the captured content.
5. Backtracking: Be cautious with patterns that can lead to excessive backtracking.

Optimization Strategies:
1. Use more specific patterns to reduce the search space.
2. Prefer character classes [] over alternation | when possible.
3. Use possessive quantifiers or atomic grouping to prevent unnecessary backtracking.
4. Consider using re.finditer() instead of re.findall() for large inputs to save memory.
5. For simple string operations, built-in string methods might be faster than regex.

9. How to Contribute
--------------------
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

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of the 're' module and regular expressions in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to the 're' module.
    """
    print("1. Basic Regex Operations:")
    basic_regex_operations()
    
    print("\n2. Advanced Regex Operations:")
    advanced_regex_operations()
    
    print("\n3. Regex Compilation and Flags:")
    regex_compilation_and_flags()
    
    print("\n4. Regex Substitution:")
    regex_substitution()
    
    print("\n5. Email Validation:")
    demonstrate_email_validation()
    
    print("\n6. Regex Best Practices:")
    regex_best_practices()
    
    print("\n7. Regex Pitfalls:")
    regex_pitfalls()
    
    print("\n8. Log Analysis:")
    demonstrate_log_analysis()
    
    print("\n9. Unicode Regex:")
    demonstrate_unicode_regex()
    
    print("\n10. FAQ Solutions:")
    demonstrate_faq_solutions()
    
    print("\n11. Performance Optimization:")
    demonstrate_performance_optimization()

if __name__ == "__main__":
    main()