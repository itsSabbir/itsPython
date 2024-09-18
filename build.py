import os

# Define the chapter titles as per "TestingTheText" method (assuming it's lowercase with underscores)
content_testing_method = {
    "basic_syntax_and_data_types": [
        "Basic data types (int, float, complex, str, bool)", 
        "Variables and constants", 
        "Type conversion and casting", 
        "Numbers, strings, and booleans", 
        "Lists, tuples, sets, and dictionaries"
    ],
    "operators_and_expressions": [
        "Arithmetic operators", 
        "Comparison operators", 
        "Logical operators", 
        "Bitwise operators", 
        "Identity and membership operators", 
        "Operator precedence"
    ],
    "control_structures": [
        "if-elif-else statements", 
        "for and while loops", 
        "break, continue, and pass statements", 
        "List comprehensions", 
        "Generator expressions"
    ],
    "functions": [
        "Function definition and calling", 
        "Parameters and return values", 
        "Default and keyword arguments", 
        "Variable-length arguments (*args and **kwargs)", 
        "Lambda functions", 
        "Decorators"
    ],
    "modules_and_packages": [
        "Importing modules", 
        "Creating and using packages", 
        "The `__init__.py` file", 
        "Standard library modules", 
        "Third-party packages and pip"
    ],
    "object_oriented_programming": [
        "Classes and objects", 
        "Inheritance and polymorphism", 
        "Encapsulation and abstraction", 
        "Magic methods (dunder methods)", 
        "Property decorators", 
        "Class and static methods"
    ],
    "file_handling": [
        "Reading and writing text files", 
        "Working with CSV, JSON, and XML", 
        "File and directory management", 
        "Context managers and the `with` statement"
    ],
    "exception_handling": [
        "Try-except blocks", 
        "Raising exceptions", 
        "Custom exception classes", 
        "Finally and else clauses", 
        "Context managers for exception handling"
    ],
    "iterators_and_generators": [
        "Iterable objects and iterators", 
        "Creating custom iterators", 
        "Generator functions and expressions", 
        "The `yield` statement", 
        "Coroutines and asynchronous generators"
    ],
    "functional_programming": [
        "Higher-order functions", 
        "Map, filter, and reduce", 
        "Partial functions", 
        "Closures", 
        "Recursion in Python"
    ],
    "advanced_python_concepts": [
        "Metaclasses", 
        "Descriptors", 
        "Context managers", 
        "Decorators with arguments", 
        "Abstract base classes"
    ],
    "python_standard_library": [
        "os and sys modules", 
        "datetime and time modules", 
        "math and random modules", 
        "re (regular expressions) module", 
        "collections module"
    ],
    "data_structures_in_python": [
        "Advanced list operations", 
        "Dictionaries and OrderedDict", 
        "Arrays and NumPy basics", 
        "Stacks, queues, and deques", 
        "Heapq module for priority queues"
    ],
    "algorithms_in_python": [
        "Sorting algorithms (e.g., merge sort, quicksort)", 
        "Searching algorithms (e.g., binary search)", 
        "Graph algorithms", 
        "Dynamic programming"
    ],
    "concurrency_and_parallelism": [
        "Threading and the Global Interpreter Lock (GIL)", 
        "Multiprocessing", 
        "Asynchronous I/O with asyncio", 
        "Concurrent.futures module"
    ],
    "network_programming": [
        "Socket programming", 
        "HTTP requests with requests library", 
        "Creating web servers with Flask or Django basics", 
        "Working with APIs"
    ],
    "database_interaction": [
        "SQLite with Python", 
        "SQL databases with SQLAlchemy", 
        "NoSQL databases (e.g., MongoDB with PyMongo)", 
        "Object-Relational Mapping (ORM)"
    ],
    "testing_and_debugging": [
        "Unit testing with unittest", 
        "Pytest framework", 
        "Debugging techniques and tools (pdb)", 
        "Logging and error handling"
    ],
    "performance_optimization": [
        "Profiling Python code", 
        "Optimizing algorithms and data structures", 
        "Cython for performance-critical parts", 
        "Numba for just-in-time compilation"
    ],
    "web_scraping_and_automation": [
        "Beautiful Soup and lxml", 
        "Selenium for browser automation", 
        "Scrapy framework basics", 
        "Automating tasks with Python scripts"
    ],
    "data_science_and_machine_learning_basics": [
        "NumPy for numerical computing", 
        "Pandas for data manipulation", 
        "Matplotlib and Seaborn for data visualization", 
        "Scikit-learn for machine learning basics"
    ],
    "python_for_devops": [
        "Scripting for system administration", 
        "Configuration management (e.g., Ansible basics)", 
        "Docker and containerization with Python", 
        "CI/CD pipelines and Python"
    ],
    "best_practices_and_code_quality": [
        "PEP 8 style guide", 
        "Code linting (pylint, flake8)", 
        "Type hinting and mypy", 
        "Design patterns in Python"
    ],
    "advanced_project_structure": [
        "Creating distributable packages", 
        "Virtual environments and dependency management", 
        "Documentation with Sphinx", 
        "Continuous Integration for Python projects"
    ]
}

# Recreate the folder structure with the "Ch#Title" format, ensuring chapter titles start with capital letters.
base_dir_python_convention_capital = "itsPython"

# Recreate the folder structure with the "Ch#Title" format and capitalized chapter names
for index, (chapter, topics) in enumerate(content_testing_method.items(), start=1):
    # Capitalize the chapter title after "Ch#" using Python naming convention
    chapter_title = chapter.replace('_', ' ').title().replace(' ', '_')
    chapter_folder_name = f"Ch{index}_{chapter_title}"
    chapter_folder = os.path.join(base_dir_python_convention_capital, chapter_folder_name)
    os.makedirs(chapter_folder, exist_ok=True)
    
    # Create topic files within each chapter folder
    for i, topic in enumerate(topics, start=1):
        topic_file = os.path.join(chapter_folder, f"Topic{i}_{topic.replace(' ', '_').replace('/', '').replace('*', '').replace('-', '').replace('(', '').replace(')', '')}.py")
        with open(topic_file, 'w') as f:
            f.write(f"# {topic}\n\n# Content goes here.")

print(f"Files and folders created successfully with 'Ch#Title' format, capitalized chapter titles, in the 'itsPython' directory!")
