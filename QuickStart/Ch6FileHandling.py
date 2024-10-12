#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: File Handling
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python provides a variety of modules to work with file handling, covering a wide range of file types
# and use cases including text files, binary files, compressed files, and even memory-mapped files.

# The following imports cover some of the most commonly used file handling libraries:

import os          # os module provides functions to interact with the operating system. 
                   # It is often used to handle file paths, directories, and environment variables.

import json        # json module is used for reading and writing JSON (JavaScript Object Notation) data.
                   # It's especially useful for serializing and deserializing complex data structures.

import csv         # csv module allows reading from and writing to CSV (Comma-Separated Values) files.
                   # CSV is a simple, widely supported file format for tabular data.

import pickle      # pickle is used for serializing and deserializing Python objects (serialization converts objects into byte streams).
                   # This module is useful when you want to save Python objects to a file and retrieve them later.

import shutil      # shutil module provides high-level file operations such as copying, moving, and removing files and directories.
                   # It's helpful when managing files across directories or creating backups.

import tempfile    # tempfile module is used for creating temporary files and directories.
                   # Useful in situations where you need a file for short-term use and want to avoid managing cleanup manually.

import mmap        # mmap module allows memory-mapping of files, enabling efficient file access without loading the entire file into memory.
                   # Useful for large files where random access is required, such as databases or large datasets.

import gzip        # gzip module is used to read and write files in .gz compressed format.
                   # It allows handling of compressed files transparently, making it easier to work with large datasets.

import zipfile     # zipfile module enables reading and writing of ZIP compressed files.
                   # ZIP files can contain multiple files, and this module provides an easy way to manage them.

import io          # io module provides tools for working with streams (such as file streams, in-memory streams, etc.).
                   # It allows for advanced file handling and manipulation of in-memory file-like objects.


# Here is an overview of what these modules allow you to do:

# 1. os: Interact with the operating system for low-level file operations
#    - os.path.join, os.path.exists, os.remove, os.rename are common methods.
#    - Use cases: Ensuring portability across OS (Windows, Linux, macOS) when working with file paths.

# Example:
file_path = os.path.join("folder", "file.txt")  # Combines folder and file names in an OS-independent manner.
if os.path.exists(file_path):  # Checks if the file exists
    os.remove(file_path)       # Deletes the file if it exists.

# Advanced Tip:
# Use os.scandir() or os.walk() to efficiently traverse directories, especially when dealing with large directory trees.

# 2. json: Work with JSON data, which is commonly used for data exchange.
#    - json.dumps() and json.loads() handle in-memory serialization/deserialization.
#    - json.dump() and json.load() handle file-based serialization/deserialization.

# Example:
data = {"name": "John", "age": 30, "city": "New York"}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)  # Write data to a file in JSON format.

# Potential Pitfall:
# JSON only supports certain data types (like strings, numbers, lists, and dictionaries).
# If you try to serialize custom objects, you'll need a custom serialization method or consider pickle.

# 3. csv: Handle CSV files, commonly used for tabular data storage.
#    - csv.reader() and csv.writer() allow easy manipulation of CSV files.
#    - csv.DictReader and csv.DictWriter provide a dictionary interface for working with CSV files.

# Example:
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])  # Write header row
    writer.writerow(["John", 30, "New York"])  # Write data row

# Advanced Tip:
# Use csv.DictReader to work directly with CSV data as dictionaries, improving readability and usability.

# 4. pickle: Serialize and deserialize Python objects, which allows you to save any Python object.
#    - pickle.dump() serializes data into a file.
#    - pickle.load() reads it back from the file.

# Example:
my_object = {"foo": "bar", "baz": [1, 2, 3]}
with open('data.pkl', 'wb') as pkl_file:
    pickle.dump(my_object, pkl_file)  # Save the object in binary format.

# Potential Pitfall:
# Pickle files are Python-specific. Use JSON for cross-language compatibility.
# Be cautious with untrusted pickle files as they can execute arbitrary code during deserialization.

# 5. shutil: Perform high-level file operations, such as copying files or entire directories.
#    - shutil.copy(), shutil.move(), shutil.rmtree() are commonly used methods.
#    - Useful for backups or batch processing of files across directories.

# Example:
shutil.copy('source.txt', 'destination.txt')  # Copies the file from source to destination.

# Advanced Tip:
# shutil.make_archive() can create compressed archives (like ZIP files) directly from directories.

# 6. tempfile: Create temporary files and directories. These are automatically cleaned up when closed.
#    - tempfile.NamedTemporaryFile() creates a file that you can reference by name.
#    - tempfile.TemporaryDirectory() creates a temporary directory.

# Example:
with tempfile.TemporaryDirectory() as tmpdirname:
    print('Created temporary directory', tmpdirname)  # This directory will be automatically deleted when the context exits.

# Use case:
# Helpful in testing environments or when you need a scratch directory that doesn't need manual cleanup.

# 7. mmap: Efficiently access large files by mapping them into memory.
#    - This is particularly useful for random access to large files without loading the entire file into memory.
#    - Common in database applications and large file processing.

# Example:
with open('largefile.txt', 'r+b') as f:
    mmapped_file = mmap.mmap(f.fileno(), 0)
    print(mmapped_file.read(10))  # Read the first 10 bytes of the file.

# 8. gzip: Work with .gz compressed files, reading and writing data without needing to manually compress/decompress.
#    - gzip.open() allows reading and writing compressed files as if they were regular files.

# Example:
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(b'Compressed data')

# 9. zipfile: Handle ZIP files, which can contain multiple compressed files.
#    - zipfile.ZipFile() allows for creation, reading, and writing of ZIP archives.

# Example:
with zipfile.ZipFile('my_archive.zip', 'w') as myzip:
    myzip.write('file.txt')

# 10. io: Provides the building blocks for working with streams and in-memory file-like objects.
#    - You can create an in-memory stream using io.StringIO() (for text) or io.BytesIO() (for binary data).

# Example:
memory_file = io.StringIO()
memory_file.write('Hello World!')
print(memory_file.getvalue())  # Retrieves the content of the in-memory file.

# Summary:
# These modules offer powerful tools to interact with files and directories, catering to various needs like text/binary data,
# file compression, serialization, and more. Depending on your task, choosing the right module can simplify file management significantly.

# Advanced Tip:
# When working with file handling in Python, always ensure proper resource management.
# Using the 'with' statement guarantees that files are properly closed after their block of code finishes,
# even if an error occurs, preventing resource leakage.


#===============================================================================
# 1. Reading and Writing Text Files
#===============================================================================

# Basic file opening and reading example:
# This snippet demonstrates how to open a text file in read mode ('r') and read its contents.
# The variable 'file_path' holds the path to the file to be read.
file_path = 'example.txt'

# Using 'with' statement for file handling (recommended approach):
# The 'with' statement is used to ensure that the file is properly closed after the operation is complete,
# even if an error occurs during the file operations. It eliminates the need to manually close the file.
with open(file_path, 'r') as file:  # 'r' mode opens the file in read-only mode
    content = file.read()  # Reads the entire content of the file into a single string
    print(f"File contents:\n{content}")  # Outputs the file's contents to the console

# Tip: Always use the 'with' statement when working with files.
# It handles file closing automatically, ensuring no file descriptors are left open,
# which is crucial for resource management and avoiding memory leaks in long-running applications.

# Writing to a file example:
# Now we'll open a file in write mode ('w'). This mode creates a new file if it doesn't exist,
# or overwrites the contents of the file if it does.
with open('output.txt', 'w') as file:  # 'w' mode opens the file in write mode, overwriting any existing content
    file.write('Hello, World!\n')  # Writes a string to the file, followed by a newline character
    file.write('This is a new line.')  # Appends another line to the file

# Tip: Be cautious with 'w' mode, as it overwrites the entire content of the file if it already exists.
# Use 'a' mode (append mode) if you want to add data to the existing content without erasing anything.

# Appending to a file example:
# This snippet demonstrates how to append new content to an existing file using 'a' mode.
# In this mode, data is written to the end of the file without affecting the existing content.
with open('output.txt', 'a') as file:  # 'a' mode opens the file in append mode
    file.write('\nThis line is appended.')  # Appends a new line to the existing content

# Reading lines from a file example:
# 'readlines()' reads all lines from the file and returns them as a list of strings.
# Each string represents a line from the file, including the newline characters at the end.
with open(file_path, 'r') as file:  # Opens the file in read mode again
    lines = file.readlines()  # Reads all lines into a list of strings
    for line in lines:  # Loops through each line in the list
        print(line.strip())  # Prints each line after stripping any leading/trailing whitespace

# Tip: 'readlines()' is suitable for small to moderately-sized files since it loads the entire file into memory.
# For large files, where memory usage might be a concern, iterating directly over the file object is a better choice.

# Reading line by line (memory-efficient) example:
# This approach is ideal for large files since it reads one line at a time, making it memory-efficient.
# It doesn't load the entire file into memory, which can be critical when working with large datasets.
with open(file_path, 'r') as file:  # Opens the file in read mode
    for line in file:  # Iterates over each line in the file, one by one
        print(line.strip())  # Prints each line after stripping any leading/trailing whitespace

# Tip: When working with large files, iterating over the file object itself is preferable to 'readlines()',
# as it processes each line individually, keeping memory usage low.

# Advanced tip:
# If you need to handle file encoding (especially for non-ASCII characters), you can specify the encoding parameter 
# when opening the file. For example, open(file_path, 'r', encoding='utf-8') ensures that UTF-8 encoding is used, 
# which is important for reading text files with special characters.
# Always handle exceptions such as FileNotFoundError or IOError to avoid runtime crashes in case the file path is incorrect.
# It's also good practice to verify file permissions when reading or writing, as permission errors can cause issues.

# Potential pitfall:
# Opening a file without specifying a mode defaults to 'r' (read-only mode). Attempting to write to the file
# without explicitly using 'w' or 'a' mode will raise an error. Always ensure the correct mode is used for your file operation.

#===============================================================================
# 2. File Modes and Encoding
#===============================================================================

# When opening a file in Python, you specify the mode in which the file is opened.
# The mode defines how the file will be accessed: read, write, append, etc.
# In addition to mode, you can specify the encoding (critical for handling non-ASCII text).

# Common file modes:
# 'r': Read mode (default) - Opens the file for reading. The file must already exist, or an error is raised.
# 'w': Write mode - Opens the file for writing. If the file already exists, it is truncated (i.e., its contents are deleted). If the file does not exist, it is created.
# 'a': Append mode - Opens the file for writing, but it appends to the end of the file instead of overwriting existing content. If the file does not exist, it is created.
# 'x': Exclusive creation mode - Opens the file for writing only if it does not exist. If the file exists, an error is raised. Useful for ensuring that an existing file is not overwritten.
# 'b': Binary mode - Opens the file in binary mode. This is used for non-text files such as images, audio, or executable files. When combined with other modes, it ensures the file is read or written in raw binary format rather than as text.
# '+': Read and write mode - Opens the file for both reading and writing. The '+' modifier can be combined with 'r', 'w', or 'a' to allow both reading and writing.

# In practice, the mode you choose depends on the operation you intend to perform.

# Example: Reading a file with specific encoding
# Always specify the encoding when dealing with text files, especially if the file contains non-ASCII characters.
# The default encoding is platform-dependent, and omitting it can cause issues when working with non-ASCII text (like characters with accents, Chinese, Arabic, etc.).
# UTF-8 is a widely accepted standard encoding that can handle a large range of characters and is a good default for most cases.

file_path = "example.txt"  # File path for the file we want to read
# Here, we open a file in read mode ('r') with UTF-8 encoding.
# The 'with' statement is used to open the file, ensuring that it is properly closed after the block is exited, even if an error occurs.
with open(file_path, 'r', encoding='utf-8') as file:
    # 'file.read()' reads the entire content of the file into memory as a string.
    content = file.read()
    print(content)  # Display the content

# Tip: Always specify the encoding to avoid issues with non-ASCII characters, especially when working in international environments or with text data containing special characters.

# Advanced tip:
# In real-world applications, reading large files with 'file.read()' could lead to memory issues as the entire file is loaded into memory.
# For large files, it is recommended to read the file line by line using a loop:
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # The 'strip()' method removes leading/trailing whitespace or newline characters.

# Use case:
# This approach is more memory-efficient and suitable for processing large text files, like logs or data dumps.

# Advanced tip (Binary files):
# If you're dealing with binary files (e.g., images, audio files), it's crucial to open the file in 'binary mode' using 'b' with other modes.
# Example: Open a file for binary reading.
# Note: No encoding is specified in binary mode because the content is raw binary data, not text.
with open("example_image.jpg", 'rb') as binary_file:
    binary_content = binary_file.read()
    # 'binary_content' holds the raw bytes of the image file, which can be processed or saved.

# Pitfalls:
# 1. Forgetting to specify 'encoding' when opening text files can lead to UnicodeDecodeError or corrupted characters, especially when working with international text.
# 2. Overwriting files unintentionally using 'w' mode can result in data loss. Always double-check before using 'w' mode if you don't want to overwrite existing content.
# 3. Using 'x' mode can prevent accidental overwriting of important files, but be prepared to handle the exception if the file already exists.

# Best practices:
# - Always use the 'with' statement to handle files. It automatically manages file closing, which prevents file corruption or locking issues.
# - Explicitly specify 'encoding' when working with text to ensure consistent behavior across different platforms.
# - Use binary mode ('b') for non-text files to avoid encoding-related issues.

#===============================================================================
# 3. Working with Binary Files
#===============================================================================

# Binary files store data in a raw binary format, unlike text files that store data as characters.
# When dealing with binary files, we use specific modes: 'wb' (write binary) and 'rb' (read binary).
# This is essential when handling non-text data such as images, audio files, or compiled executables.
# Below are examples of writing and reading binary data in Python.

# Example 1: Writing binary data to a file
# First, we create a byte sequence using the 'bytes()' function. This converts a list of integers (ranging from 0 to 255) into binary format.
# In this case, the byte sequence is [0, 1, 2, 3, 4, 5], which translates directly into binary form.
data = bytes([0, 1, 2, 3, 4, 5])  # 'bytes' takes an iterable of integers and returns a bytes object (immutable sequence of bytes)

# We open a file named 'binary_file.bin' in 'wb' mode (write binary mode).
# 'wb' ensures the file is opened in binary mode, where the data written to the file is not encoded or decoded into text.
# Binary mode is crucial when working with data that isn't character-based.
with open('binary_file.bin', 'wb') as file:
    file.write(data)  # Write the byte sequence directly to the binary file

# Important note: 
# Always ensure the file is opened in 'wb' mode when writing binary data. Using 'w' (text mode) may corrupt the binary content 
# because text mode may interpret or alter the raw binary data during the write process (e.g., converting line endings).

# Example 2: Reading binary data from a file
# To read the data back, we open the same file in 'rb' mode (read binary).
# 'rb' mode reads the binary data without attempting to decode it into characters.
# This is particularly important when working with non-text files, as they may contain data that cannot be properly decoded as text.
with open('binary_file.bin', 'rb') as file:
    binary_data = file.read()  # Read the binary content of the file. The data is returned as a bytes object.
    print(f"Binary data: {binary_data}")  # Print the raw binary data as a bytes object (e.g., b'\x00\x01\x02\x03\x04\x05')

# Output: Binary data: b'\x00\x01\x02\x03\x04\x05'
# The binary data is displayed in its raw format. Each byte is represented by its hexadecimal value.

# Advanced Tip:
# When reading binary files that store structured data (like images or protocol data), 
# you might need to manually unpack the binary data into a usable form using the 'struct' module, which allows for interpreting bytes
# according to specific format codes. This is particularly useful when dealing with binary formats with fixed data structures (e.g., headers, metadata).
# Example: Using struct.unpack() to extract fields from binary data.

# Use case:
# Binary file handling is common in many real-world applications like reading/writing image files (e.g., .jpg, .png), 
# sound files (e.g., .mp3, .wav), and handling network packets or working with low-level system interfaces.

# Potential pitfalls:
# 1. Forgetting to use 'rb' or 'wb' mode when working with binary files can lead to incorrect data interpretation, especially on systems where
#    text mode can alter binary data (e.g., newline character handling in Windows).
# 2. When manipulating binary data, you must be aware of the encoding format or file structure. Directly reading or writing binary files without understanding 
#    their format can lead to corrupt or unusable data. Always consult the file format specification if available.

# Another good practice: 
# Always handle file operations within a 'with' block (context manager) to ensure that files are closed properly after operations, 
# even if an error occurs. This ensures no data corruption or file locking issues.

#===============================================================================
# 4. Working with Different File Formats
#===============================================================================

# In this section, we cover how to work with CSV, JSON, and Pickle file formats in Python.
# Each format has its own advantages and is used in different scenarios depending on the nature of the data.
# Python provides built-in libraries for handling these formats, ensuring ease of use for reading and writing data.

# Import necessary libraries
import csv
import json
import pickle

#==============================
# CSV Files
#==============================

# CSV (Comma-Separated Values) is a widely used format for tabular data.
# Each line in a CSV file represents a row, with values separated by commas or other delimiters.

# Example 1: Writing CSV data
# 'writerows()' method writes multiple rows at once from the 'data' list.
# 'newline=""' ensures that Python writes the CSV file with the correct line endings across all platforms (Windows, Linux, etc.).
data = [
    ['Name', 'Age', 'City'],  # Header row defining the fields
    ['Alice', '30', 'New York'],  # Data row
    ['Bob', '25', 'Los Angeles']  # Another data row
]

# Open a file in write mode ('w') with 'newline=""' to ensure proper line endings across platforms
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)  # Create a CSV writer object
    writer.writerows(data)  # Write all rows at once from the 'data' list

# Tip: Use 'newline=""' when writing CSV files to prevent writing extra blank lines, especially on Windows.
# Without this, you may experience additional blank lines in the output file.

# Example 2: Reading CSV data
# 'csv.reader()' reads the file row by row, which you can iterate over.
# Each row is returned as a list of strings.
with open('data.csv', 'r') as file:
    reader = csv.reader(file)  # Create a CSV reader object
    for row in reader:  # Iterate over each row in the file
        print(row)  # Print each row, which is represented as a list of values

# Tip: If you need more control over the field names, consider using 'csv.DictReader()' and 'csv.DictWriter()'.
# These classes allow you to work with rows as dictionaries, making the code more readable and manageable,
# especially when dealing with complex CSV files where columns are referred to by name.

#==============================
# JSON Files
#==============================

# JSON (JavaScript Object Notation) is a lightweight data-interchange format.
# It is used widely for APIs, configuration files, and data serialization because of its simplicity and language-independence.

# Example 3: Writing JSON data
# 'json.dump()' serializes the Python dictionary into a JSON-formatted string and writes it to a file.
# 'indent=4' is used for pretty-printing, making the file more human-readable by adding indentation.
data = {
    'name': 'Alice',  # String field
    'age': 30,  # Integer field
    'city': 'New York'  # Another string field
}

# Open a file in write mode ('w') and write the dictionary as a JSON object
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # 'indent=4' formats the JSON for readability

# Tip: Pretty-printing JSON (using the 'indent' parameter) is particularly useful when creating configuration files
# or logs that humans might read. It makes it easier to inspect and debug.

# Example 4: Reading JSON data
# 'json.load()' parses the JSON data from a file and returns it as a Python object (typically a dictionary).
with open('data.json', 'r') as file:
    loaded_data = json.load(file)  # Load the JSON data from the file into a Python object
    print(f"Loaded JSON data: {loaded_data}")  # Display the loaded data

# Tip: 'json.loads()' is used to load JSON data from a string instead of a file.
# Similarly, 'json.dumps()' is used to convert a Python object to a JSON-formatted string for use in code, rather than writing to a file.

#==============================
# Pickle Files
#==============================

# Pickle is Python's way of serializing (converting) Python objects to a byte stream that can be written to a file.
# Unlike JSON, Pickle can handle more complex Python objects, such as sets, tuples, and even user-defined classes.

# Example 5: Writing Pickle data
# 'pickle.dump()' serializes the data and writes it to the file in binary mode ('wb').
# Pickle is ideal for saving Python-specific data structures that can't easily be converted to other formats.
data = {'a': [1, 2.0, 3, 4+6j],  # List with complex number
        'b': ('string', u'Unicode string'),  # Tuple with Unicode string
        'c': None}  # NoneType

# Open a file in binary write mode ('wb') and write the pickled data
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)  # Serialize the 'data' dictionary and write it to the file

# Example 6: Reading Pickle data
# 'pickle.load()' reads the binary data and deserializes it back into a Python object.
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)  # Load and deserialize the data from the binary file
    print(f"Loaded pickle data: {loaded_data}")  # Display the loaded data

# Tip: Pickle is Python-specific and can be a security risk if loading untrusted data.
# Avoid using Pickle to deserialize data from untrusted sources, as it can execute arbitrary code during the loading process.
# Always sanitize or validate input when using Pickle with external data.
# For cross-language compatibility, consider using JSON or another more portable format.

# Summary:
# - CSV is useful for tabular data, especially when exchanging data between different programs or platforms.
# - JSON is a widely-used format for structured data, with strong support for human readability and interoperability.
# - Pickle allows you to serialize Python objects, but be cautious about its security risks when working with untrusted data.

#===============================================================================
# 5. File and Directory Operations
#===============================================================================

# This section demonstrates how to perform basic file and directory operations using the os and shutil modules.
# These operations are essential for interacting with the filesystem, automating tasks, or managing data.

import os  # Importing the os module to interact with the operating system
import shutil  # Importing shutil for high-level file and directory operations

# Example 1: Getting the current working directory
# os.getcwd() returns the absolute path of the current working directory.
# This is useful to know the context in which the program is operating.
print(f"Current working directory: {os.getcwd()}")  # Prints the current working directory

# Example 2: Changing the current directory
# os.chdir() changes the current working directory to the specified path.
# The path should be valid, otherwise it will raise a FileNotFoundError.
# Useful for scripts that need to operate within specific directories.
os.chdir('/path/to/new/directory')  # Change to a new directory (ensure the path exists)

# Example 3: Listing contents of the current directory
# os.listdir() lists all files and directories in the specified directory.
# By passing '.' (dot), it refers to the current directory.
# Useful for viewing available files or directories to automate operations like processing files in batches.
print(f"Directory contents: {os.listdir('.')}")  # Prints the content of the current directory

# Example 4: Creating a new directory
# os.mkdir() creates a new directory at the specified path.
# If the directory already exists, it raises a FileExistsError unless handled.
# Best for creating single-level directories.
os.mkdir('new_directory')  # Creates a directory named 'new_directory'

# Example 5: Creating nested directories
# os.makedirs() creates multiple levels of directories in one go.
# If the directory structure already exists, it raises an error unless exist_ok=True is set.
# Very useful when you need to ensure a deep directory structure is created.
os.makedirs('nested/directory/structure', exist_ok=True)  
# 'exist_ok=True' prevents an error if the directories already exist.

# Tip: Using exist_ok=True ensures that if the directories already exist, no exception will be raised.
# Without this flag, the operation would throw a FileExistsError if any part of the structure already exists.

# Example 6: Removing a file
# os.remove() deletes a file at the specified path.
# Ensure that the file exists and is not open elsewhere, or an error will be raised.
# This is useful when managing temporary files, logs, or cleanup tasks.
os.remove('file_to_delete.txt')  # Deletes a file named 'file_to_delete.txt'

# Example 7: Removing an empty directory
# os.rmdir() removes an empty directory.
# It will fail with an OSError if the directory contains any files or other directories.
# This function is useful for simple directory cleanup when you know the directory is empty.
os.rmdir('empty_directory')  # Removes an empty directory named 'empty_directory'

# Example 8: Removing a directory and all its contents
# shutil.rmtree() deletes a directory and all its contents (files and subdirectories).
# This is a powerful function and should be used with caution as it does not prompt for confirmation.
shutil.rmtree('directory_to_delete')  # Deletes 'directory_to_delete' along with its entire contents

# Tip: Be cautious when using shutil.rmtree(), as it will irreversibly delete everything in the directory, including subdirectories and files. 
# There is no confirmation, so ensure the target directory is correct.

# Example 9: Renaming files or directories
# os.rename() renames a file or directory.
# If the target name already exists, it will overwrite it unless otherwise handled.
# This is useful for organizing or managing files, such as renaming temporary files.
os.rename('old_name.txt', 'new_name.txt')  # Renames 'old_name.txt' to 'new_name.txt'

# Example 10: Moving files or directories
# shutil.move() moves a file or directory from one location to another.
# It automatically handles both file and directory movement.
# Useful for relocating files or creating structured directories by moving content.
shutil.move('source.txt', 'destination/source.txt')  # Moves 'source.txt' to the destination directory

# Example 11: Copying files
# shutil.copy() copies a file from one location to another.
# It does not copy directory trees—use shutil.copytree() for that.
# Useful for making backups or duplicating files without altering the original.
shutil.copy('source.txt', 'destination.txt')  # Copies 'source.txt' to 'destination.txt'

# Example 12: Copying entire directory trees
# shutil.copytree() recursively copies an entire directory tree (including all subdirectories and files).
# The destination must not already exist.
# This is useful when you need to create a full backup of a directory or replicate its structure.
shutil.copytree('source_dir', 'destination_dir')  # Copies the entire 'source_dir' to 'destination_dir'

# Important note: shutil.copytree() requires that the destination does not exist.
# If you want to overwrite an existing directory, you must handle that manually by first removing the destination (with shutil.rmtree()).

# Advanced Tip:
# For handling a large number of files or directories, consider using os.scandir() instead of os.listdir().
# os.scandir() returns an iterator that yields directory entries as os.DirEntry objects, offering better performance for large directories,
# especially when you need to access file attributes such as file size, type, or modification time.

#===============================================================================
# 6. Working with Paths
#===============================================================================

# Python's os.path module offers utility functions for interacting with file system paths.
# These functions are cross-platform, ensuring code runs on Windows, macOS, Linux, etc.
# Here, we explore common os.path methods for manipulating paths.

import os  # Importing the os module, which provides os.path for path manipulations

# Example 1: Joining path components (cross-platform)
# os.path.join ensures that paths are correctly joined, regardless of the operating system.
# On Windows, it uses backslashes ('\'), while on Unix-based systems, it uses forward slashes ('/').
# This is critical for writing cross-platform compatible code.
path = os.path.join('folder', 'subfolder', 'file.txt')
print(f"Joined path: {path}")
# Output (on Windows): Joined path: folder\subfolder\file.txt
# Output (on Unix-based OS): Joined path: folder/subfolder/file.txt

# Use case:
# Use os.path.join instead of manual concatenation to avoid platform-specific path separators.
# It reduces bugs when the code is deployed on different operating systems.

# Example 2: Absolute path
# os.path.abspath returns the absolute path for a relative path.
# It converts a given relative path into an absolute path by prefixing it with the current working directory.
# This is useful when you need to resolve relative paths to their full, system-specific path.
abs_path = os.path.abspath('relative_path.txt')
print(f"Absolute path: {abs_path}")
# Output (on any OS): Absolute path: /current/working/directory/relative_path.txt
# The absolute path starts from the root directory of the file system.

# Advanced tip:
# Be cautious when using absolute paths, as hardcoding them makes the code less flexible.
# Prefer relative paths in portable projects and use absolute paths only when necessary for locating resources.

# Example 3: Directory and file name of a path
# os.path.dirname extracts the directory component from a full path.
# os.path.basename extracts the file name component (the last part of the path).
# This helps when you need to separate the folder path from the file name for processing.
dir_name = os.path.dirname(path)  # Gets the directory part of the path
file_name = os.path.basename(path)  # Gets the file name part of the path
print(f"Directory: {dir_name}, File: {file_name}")
# Output: Directory: folder/subfolder, File: file.txt
# Note: Path separators vary depending on the platform, so the output may differ.

# Example 4: Splitting path into directory and file
# os.path.split is another way to separate the directory and file name.
# It returns a tuple containing both parts (directory, file).
dir_name, file_name = os.path.split(path)
print(f"Directory: {dir_name}, File: {file_name}")
# Output: Directory: folder/subfolder, File: file.txt
# Functionally similar to using os.path.dirname and os.path.basename, but in one step.

# Tip:
# The os.path functions do not check if the file or directory actually exists; they only work with the string representation of paths.
# Always check for the existence of files or directories with the appropriate functions if needed.

# Example 5: Check if a path exists
# os.path.exists checks whether a path exists on the filesystem.
# It's useful before performing file or directory operations to avoid errors (e.g., FileNotFoundError).
print(f"Path exists: {os.path.exists(path)}")
# Output: Path exists: False
# If the path exists, it returns True; otherwise, False.

# Example 6: Check if it's a file or directory
# os.path.isfile checks if the given path points to a file.
# os.path.isdir checks if the given path points to a directory.
# These functions are crucial when distinguishing between files and folders.
print(f"Is file: {os.path.isfile(path)}")  # False because 'path' is just a string, no file exists
print(f"Is directory: {os.path.isdir(path)}")  # False because the directory doesn't exist either
# Output: Is file: False, Is directory: False
# These functions are helpful in recursive directory traversal or for file-type validation.

# Example 7: File extension
# os.path.splitext splits the filename into two parts: the root and the extension.
# This is useful when you need to check or modify the file extension (e.g., renaming files or ensuring correct file types).
_, extension = os.path.splitext(file_name)
print(f"File extension: {extension}")
# Output: File extension: .txt
# The function returns a tuple where the first part is the file name without the extension,
# and the second part is the extension (including the dot).

# Advanced tip:
# Be careful when working with file names that contain multiple dots (e.g., "archive.tar.gz").
# os.path.splitext will only split at the last dot, so use caution or custom logic for files with compound extensions.

# Potential pitfalls:
# When working with relative paths, ensure you are aware of the current working directory.
# Using os.getcwd() can help confirm the starting directory for resolving relative paths.
# For platform-specific operations, consider the pathlib module introduced in Python 3.4, which offers an object-oriented approach to path handling with more powerful abstractions.


#===============================================================================
# 7. Advanced File Operations
#===============================================================================

# In this section, we'll cover two advanced file operations in Python:
# 1. Using the 'fileinput' module for in-place file editing
# 2. Using 'mmap' for memory-mapped file handling, which is particularly useful for large files.

#===============================================================================
# Example 1: Using 'fileinput' to edit files in-place
#===============================================================================

# The 'fileinput' module is a powerful tool when you need to process multiple files, 
# allowing you to modify files directly without needing to open and close each one manually.
# The 'inplace=True' argument enables in-place editing, which means the changes are made directly to the original files.
# This can be especially useful when performing bulk find-and-replace operations across multiple files.

import fileinput

# List of files in which you want to search and replace a string
files_to_search = ['file1.txt', 'file2.txt', 'file3.txt']  # Modify this list with actual file names or paths
with fileinput.input(files=files_to_search, inplace=True) as f:
    # fileinput.input() handles opening, closing, and iterating over lines across multiple files.
    # 'inplace=True' allows direct modification of the files without creating temporary copies.
    for line in f:
        # Here, we use line.replace() to replace all occurrences of 'old_string' with 'new_string'
        # The 'end=""' ensures that no extra newline characters are added when printing the modified lines
        print(line.replace('old_string', 'new_string'), end='')

# Output: This script does not print output to the console. Instead, it modifies the files in place.

# Tip: The 'fileinput' module is great for processing multiple files or even stdin (standard input).
# It is especially useful when you need to make consistent changes across many files.
# Advanced use case: If you need to perform more complex operations, you can combine fileinput with regular expressions (re module).

# Advanced tip: Be cautious when using 'inplace=True' as this operation directly modifies the files.
# Consider backing up your files before performing in-place operations to avoid accidental data loss.
# Also, remember that using fileinput in place of manually managing file handles can make the code more concise and readable.

# Potential pitfall: Be aware that if the original files are large, using fileinput might not be the most memory-efficient approach.
# In cases where the files are large and you need more efficient file handling, consider using memory-mapped files (as discussed below).

#===============================================================================
# Example 2: Memory-mapped files using 'mmap'
#===============================================================================

# The 'mmap' module allows you to map a file into memory. This is extremely useful when working with large files.
# Instead of reading the entire file into memory (which can be inefficient for large files), 'mmap' allows you to work with parts of the file.
# This technique is often used when the file size exceeds available memory.

import mmap  # mmap needs to be imported to handle memory-mapped files

# Open a binary file ('large_file.bin') in read-only mode
with open('large_file.bin', 'rb') as f:  # 'rb' means read as binary
    # Memory-map the file using mmap.mmap(), which allows direct access to parts of the file.
    # f.fileno() provides the file descriptor, and '0' means we want to map the entire file.
    # mmap.ACCESS_READ allows read-only access to the memory-mapped file.
    mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # Example: Reading the first 10 bytes from the memory-mapped file
    # Instead of loading the whole file into memory, we just access the part we need.
    print(f"First 10 bytes: {mmapped_file[0:10]}")

    # Always remember to close the memory-mapped file when done
    mmapped_file.close()

# Output: This will print the first 10 bytes of the file, represented as a byte string.
# Example Output: First 10 bytes: b'\x89PNG\r\n\x1a\n\x00\x00'

# Tip: Memory-mapped files are more efficient when dealing with large files, especially when random access is needed.
# You can access parts of the file directly, as if it were a list, which minimizes memory usage.

# Use case: Ideal for processing large binary files, such as images or videos, where you only need to work with small parts of the file at a time.
# This is also useful in scientific computing and handling large datasets where reading the whole file into memory would be impractical.

# Advanced tip: You can also memory-map only specific parts of the file by passing an appropriate offset and length to mmap().
# This can further improve performance if only a subset of the file is required for processing.

# Potential pitfalls:
# 1. If you try to write to a memory-mapped file opened in read-only mode (ACCESS_READ), it will raise an exception.
# 2. The mmap object must be closed after use, or it can lead to resource leaks.
# 3. Not all file systems support memory-mapped files, so it’s good to verify compatibility when working in different environments.

# As a best practice, consider using 'mmap' for files that are larger than your system’s memory but require frequent access to specific sections.
# For smaller files, traditional file I/O might be simpler and sufficient.

#===============================================================================
# 8. Working with Compressed Files
#===============================================================================

# Working with compressed files like gzip and zip is common when handling large datasets
# or when trying to optimize disk space usage. Python provides built-in libraries like 
# 'gzip' and 'zipfile' to easily work with such files.
# We'll explore both writing to and reading from compressed files (gzip and zip formats).
# The 'with' statement is used here for handling file operations to ensure proper resource management
# (automatic closing of files and cleanup).

import gzip  # Import the gzip module for working with gzip compressed files
import zipfile  # Import the zipfile module for working with zip archives

# Example 1: Writing to a gzip file
# Here, we are opening a gzip file in write text mode ('wt').
# 'gzip.open' allows you to open and write to a gzip-compressed file.
# The 'with' statement ensures that the file is closed properly after writing.
with gzip.open('data.txt.gz', 'wt') as f:
    # Writing text content into the gzip file
    # The data will be automatically compressed when written
    f.write('This content will be compressed')  # Writing the string into the gzip file

# Best Practice:
# Always use 'with' when opening files, especially compressed files,
# because it ensures that the file is properly closed and avoids potential resource leaks.
# This is especially important for compressed files since failing to close them properly
# could result in corrupted or incomplete files.

# Example 2: Reading from a gzip file
# Here, we open a gzip file in read text mode ('rt').
# The content of the gzip file is automatically decompressed as we read it.
with gzip.open('data.txt.gz', 'rt') as f:
    # Reading the decompressed content from the gzip file
    content = f.read()  # Reading the entire content of the file into the 'content' variable
    print(f"Decompressed content: {content}")  # Output the decompressed content

# Advanced Tip:
# When working with binary data in gzip files (e.g., images or other non-text formats), 
# use 'wb' (write binary) and 'rb' (read binary) modes instead of 'wt' and 'rt'.
# Text modes are only appropriate when dealing with text-based data.
# Be mindful of mode selection based on the type of data being written/read.

# Example 3: Writing to a ZIP file
# The 'zipfile' module provides an easy way to create, write, and manage zip archives.
# We use 'zipfile.ZipFile' to open an archive in write mode ('w'), and add files to it.
# Here, we are writing 'file1.txt' and 'file2.txt' into a new zip archive called 'archive.zip'.
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    # Writing two files into the zip archive
    zipf.write('file1.txt')  # Adding 'file1.txt' to the archive
    zipf.write('file2.txt')  # Adding 'file2.txt' to the archive

# The 'zipfile.write()' method takes a filename as input and compresses it into the archive.
# If the file does not exist in the directory, an error will be raised, so ensure the files are present.

# Example 4: Extracting from a ZIP file
# Opening an existing zip archive ('archive.zip') in read mode ('r') to extract its contents.
# 'extractall()' extracts all files into the specified directory ('extracted_folder' here).
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    # Extracting all files from the zip archive to the specified directory
    zipf.extractall('extracted_folder')  # Extract all contents into 'extracted_folder'

# Advanced Tip:
# 'zipfile.ZipFile' supports various compression modes, such as ZIP_DEFLATED (default), ZIP_STORED, and ZIP_BZIP2, which can be useful
# when handling large or complex files. Choosing the right compression mode affects both file size and speed.
# Be cautious of extraction security vulnerabilities like "zip slip" (ensure safe file paths when extracting).
# The 'extract()' method can be used instead of 'extractall()' to extract individual files if needed.

# Best Practice:
# Always use the 'with' statement when working with 'zipfile.ZipFile'. This ensures the file is properly closed
# even if an exception occurs during the operation. This reduces the risk of file corruption or incomplete writes.

# Potential Pitfalls:
# When working with large files, remember that both gzip and zip compression can be CPU-intensive.
# For real-time applications, consider trade-offs between compression level and performance.
# Additionally, avoid reading large files all at once (as done in the gzip example above) if memory constraints are a concern.
# Instead, use chunked reads with 'readline()' or process the file in blocks.

#===============================================================================
# 9. Temporary Files and Directories
#===============================================================================

# The tempfile module in Python provides utilities for creating temporary files and directories.
# These are particularly useful when you need to store data temporarily during execution
# and ensure that it is automatically cleaned up afterward.
# The 'with' statement ensures that the resources are properly managed, leveraging Python's context manager capabilities.

import tempfile  # Importing the tempfile module to work with temporary files and directories

# Example 1: Creating a temporary file using NamedTemporaryFile
# The 'NamedTemporaryFile' creates a temporary file on the filesystem, 
# which will be automatically deleted when the 'with' block exits.
with tempfile.NamedTemporaryFile(mode='w+') as temp:
    # 'mode' is set to 'w+' to allow both writing and reading in text mode.
    # 'w+' opens the file for both reading and writing.
    
    temp.write('This is temporary content')  # Writing some content to the temporary file
    
    temp.seek(0)  # Resetting the file pointer to the beginning of the file to read its contents
    print(f"Temp file content: {temp.read()}")  # Reading and printing the content we just wrote

    # As soon as the 'with' block is exited, the temporary file is deleted automatically.
    # The operating system handles the cleanup, ensuring no file remnants persist.
    
# Output (example): Temp file content: This is temporary content

# Use case:
# Temporary files are commonly used in testing, where you need to mock file I/O operations
# without creating permanent files that need manual cleanup. It's also useful in scenarios
# where the data is transient and should not persist after execution.

# Example 2: Creating a temporary directory using TemporaryDirectory
# 'TemporaryDirectory' works similarly to NamedTemporaryFile, but it creates an entire directory
# that can hold multiple files. Like temporary files, the directory and its contents are
# automatically cleaned up when the 'with' block is exited.
with tempfile.TemporaryDirectory() as temp_dir:
    # 'temp_dir' holds the path of the created temporary directory
    
    print(f"Created temporary directory: {temp_dir}")  # Displaying the path of the temporary directory

    # You can create files, subdirectories, or perform operations within 'temp_dir'
    # During execution, 'temp_dir' acts like any regular directory but is guaranteed to be temporary.
    
# After the 'with' block ends, the temporary directory, along with all its contents, is deleted.

# Tip:
# Temporary files and directories are automatically cleaned up when the context manager exits.
# This ensures that no manual deletion is required, making your code more reliable and less error-prone,
# especially in situations where unexpected exceptions or early terminations might occur.
# If not using the context manager, you'd need to manually delete the files/directories, which could lead to resource leaks.

# Advanced tip:
# You can control the location and prefix of temporary files and directories by passing additional arguments 
# to 'NamedTemporaryFile' and 'TemporaryDirectory'. For example, you can specify the 'dir' argument to place 
# the temporary file in a specific directory, or 'prefix' to add a custom prefix to the file or directory name.
# This is useful when working with systems that require files to be written to specific paths or devices.

# Pitfall:
# A common mistake is assuming the file or directory still exists outside the 'with' block.
# Since the files and directories are automatically removed when the block exits,
# any attempts to access them afterward will raise an error.
# Make sure to keep any data you need before the context manager ends.

#===============================================================================
# 10. File-like Objects
#===============================================================================

# Python provides in-memory file-like objects through the 'io' module, specifically StringIO and BytesIO.
# These are very useful when you need file-like behavior without the overhead of creating actual files on disk.
# They behave like regular file objects, allowing you to perform read, write, and seek operations, but work entirely in memory.
# This makes them especially useful for testing, buffering, or handling temporary data as if it were in a file.

import io  # Importing the 'io' module, which provides in-memory file-like objects

# Example 1: StringIO for working with strings as file-like objects
# StringIO allows you to treat a string as a file. You can write to it, seek to a specific position, and read from it.
string_io = io.StringIO()  # Creating an in-memory file-like object for string data
string_io.write('Hello, StringIO!')  # Writing a string to the in-memory 'file'
string_io.seek(0)  # Moving the file pointer back to the beginning of the 'file'
print(f"StringIO content: {string_io.read()}")  # Reading the entire content from the beginning
string_io.close()  # Closing the file-like object (optional but recommended, especially in real file objects)

# Output: StringIO content: Hello, StringIO!
# After writing 'Hello, StringIO!' to the StringIO object, we seek to the start (position 0) and read the content.

# Use case:
# StringIO is often used for manipulating string data in memory that would otherwise need to be written to a file.
# It's also helpful in unit tests, where you might want to simulate file-like behavior without creating actual files.

# Example 2: BytesIO for working with bytes as file-like objects
# Similar to StringIO, BytesIO works with binary data (bytes), instead of strings.
# This is useful when you need to handle binary data in memory, such as when working with images, byte streams, or encoded data.
bytes_io = io.BytesIO(b'Hello, BytesIO!')  # Creating an in-memory file-like object for byte data
print(f"BytesIO content: {bytes_io.getvalue()}")  # Retrieving the content as a bytes object directly
bytes_io.close()  # Closing the BytesIO object

# Output: BytesIO content: b'Hello, BytesIO!'
# In this example, the BytesIO object is initialized with byte data (b'Hello, BytesIO!'),
# and we use getvalue() to retrieve the entire byte content.

# Advanced tip:
# Both StringIO and BytesIO provide useful methods such as seek(), tell(), and truncate(),
# which are commonly available in file objects. 
# These can be leveraged for more advanced in-memory data handling, such as truncating content to a specific size or 
# reading from specific positions (via seek and tell).
# StringIO can only accept and manipulate string data, while BytesIO is exclusively for bytes.
# Mixing their usage (e.g., writing strings to BytesIO or bytes to StringIO) will raise an error.

# Advanced use case:
# BytesIO is frequently used when handling streams of binary data, such as when downloading a file in chunks 
# or encoding/decoding images or other multimedia content in-memory before saving it to disk or sending it over the network.

# Potential pitfalls:
# When using StringIO or BytesIO, it's essential to remember that you need to seek(0) if you plan to read the content
# after writing, as the file pointer will be at the end after writing. Forgetting to seek() can lead to confusion when reading returns an empty result.
# Also, don't forget to close these file-like objects when done to free up resources, although they don't hold onto system resources like real file objects do.

#===============================================================================
# 11. Context Managers for File Handling
#===============================================================================

# Context managers in Python are used to handle resource management, such as files, sockets, or database connections.
# The 'with' statement simplifies resource management by ensuring proper acquisition and release of resources.
# Even in the case of exceptions, the context manager guarantees the resource is properly closed or cleaned up.

# Custom context manager for file handling
# Here, we define a custom context manager using a class to manage file opening and closing.
# This is useful if you want to extend functionality beyond what the built-in 'with open()' statement provides,
# such as adding logging, error handling, or other operations when entering or exiting the context.

class FileManager:
    def __init__(self, filename, mode):
        # Initializer method to set the file name and mode (e.g., 'r' for reading, 'w' for writing)
        self.filename = filename  # The name of the file to be opened
        self.mode = mode  # The mode in which the file will be opened (e.g., 'r', 'w', 'a')
        self.file = None  # This will hold the file object once opened

    def __enter__(self):
        # The __enter__ method is called when entering the 'with' block
        # Here, we open the file and return the file object to be used within the 'with' block
        self.file = open(self.filename, self.mode)  # Open the file with the specified mode
        return self.file  # Return the opened file object so it can be assigned to a variable in the 'with' statement

    def __exit__(self, exc_type, exc_val, exc_tb):
        # The __exit__ method is called upon exiting the 'with' block, regardless of whether an exception occurred
        # exc_type, exc_val, and exc_tb represent exception type, value, and traceback respectively (if any occurred)
        if self.file:  # Ensure that the file was actually opened
            self.file.close()  # Properly close the file to release the resource
        # Returning False (or omitting return) means any exception will propagate and not be suppressed.
        # To suppress exceptions, return True, but be cautious when doing so, as it can mask potential issues.

# Using the custom context manager
# This 'with' block uses our custom FileManager class to open, read, and close the file automatically.
# The file is opened in read mode ('r'), and its content is printed. After exiting the 'with' block,
# the file is guaranteed to be closed, even if an exception is raised during reading.
with FileManager('example.txt', 'r') as f:
    content = f.read()  # Read the content of the file
    print(f"File content: {content}")  # Print the file content

# Tip: The custom context manager provides flexibility for adding additional functionality.
# For example, you could extend it to:
# - Log every time a file is opened or closed
# - Handle errors more gracefully by logging them in the __exit__ method

# Output: The content of 'example.txt' will be printed, followed by the file being automatically closed.

# Advanced tip: 
# You can use 'contextlib' in Python for a more concise implementation of context managers without defining a full class.
# Example:
# from contextlib import contextmanager
#
# @contextmanager
# def file_manager(filename, mode):
#     f = open(filename, mode)
#     try:
#         yield f  # Yield the file object, allowing its use within the 'with' block
#     finally:
#         f.close()  # Ensure the file is closed after use
#
# With this approach, the functionality is similar but requires fewer lines of code.
# However, the class-based method offers more customization options (e.g., managing state or additional functionality).

# Potential pitfalls:
# - Forgetting to close a file manually can lead to resource leaks, which can be a serious issue, especially in large-scale systems.
#   The context manager pattern ensures that files are always closed, even if exceptions occur.
# - If using a custom context manager, make sure to understand the implications of returning True in __exit__, 
#   as this can suppress exceptions and lead to hard-to-debug issues.

#===============================================================================
# 12. Best Practices and Tips for File Operations in Python
#===============================================================================

# When working with files in Python, there are several best practices and tips 
# that will help you write cleaner, safer, and more efficient code. Here is a 
# breakdown of each recommendation, along with foundational and advanced insights.

# 1. Always use 'with' statements for file operations to ensure proper closing
# The 'with' statement automatically closes the file once the block of code is done.
# This eliminates the need to manually close files and reduces the risk of resource leaks.
# It also ensures files are closed properly, even if an exception is raised within the block.
with open('example.txt', 'r') as file:
    data = file.read()  # File is automatically closed after this block completes
# Best practice: Avoid manually calling file.close(), especially in large projects. 
# Using 'with' guarantees that the file is closed safely without errors.

# 2. Specify file encoding explicitly to avoid platform-dependent behavior
# Different platforms (Windows, macOS, Linux) may have different default encodings.
# Explicitly specifying an encoding ensures consistency across different environments.
with open('example.txt', 'r', encoding='utf-8') as file:
    data = file.read()
# 'utf-8' is the most commonly used encoding and should generally be your default choice unless you have specific needs.
# Tip: Be cautious with files from other systems that might use different encodings, such as 'ISO-8859-1'.

# 3. Use appropriate modes ('r', 'w', 'a', 'b') based on your needs
# File modes control how a file is accessed. Always use the right mode:
# - 'r' for reading (default mode), 'w' for writing (overwrites existing file),
# - 'a' for appending, 'b' for binary, and 'r+' for both reading and writing.
# Example:
with open('example.txt', 'w') as file:  # Opens for writing, truncates the file
    file.write("Hello, world!")
# Be careful: 'w' will overwrite any existing file, potentially leading to data loss.
# Use 'a' if you want to append to an existing file instead of overwriting it.

# 4. For large files, read line-by-line instead of loading the entire file into memory
# When working with very large files, it's more efficient to process them line-by-line.
# This prevents the entire file from being loaded into memory, which could be problematic for large files.
with open('largefile.txt', 'r') as file:
    for line in file:
        process(line)  # Replace with your own processing logic
# Advanced tip: This technique helps avoid memory-related issues in low-memory environments 
# or when dealing with extremely large datasets.

# 5. Use os.path functions for cross-platform path handling
# File paths are handled differently across platforms (Windows uses backslashes '\', while others use forward slashes '/').
# Using 'os.path' or 'pathlib' makes your code cross-platform compatible.
import os
file_path = os.path.join('directory', 'subdir', 'file.txt')  # Handles platform-specific path separators
# Advanced: Consider using 'pathlib.Path' (introduced in Python 3.4) for more modern and powerful path manipulations.
from pathlib import Path
file_path = Path('directory') / 'subdir' / 'file.txt'

# 6. Be cautious with file deletion operations, especially when using wildcards
# File deletion is permanent, and wildcards (like '*' or '?') can delete more than expected.
# Always validate file paths and use confirmation prompts or dry-runs before deleting.
import os
file_to_delete = 'important_file.txt'
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)  # Permanently deletes the file
# Advanced tip: For safety, consider implementing a "trash" functionality to recover accidentally deleted files.

# 7. Handle exceptions properly, especially IOError and OSError for file operations
# File operations can fail for many reasons (file not found, permission issues, etc.).
# Always handle potential errors using try-except blocks to improve the robustness of your code.
try:
    with open('nonexistent.txt', 'r') as file:
        data = file.read()
except (IOError, OSError) as e:
    print(f"Error handling file: {e}")
# Advanced tip: Use more specific exception handling to provide detailed error messages or fallback mechanisms.

# 8. Use tempfile module for creating temporary files and directories
# Temporary files are useful when you need to store data temporarily during program execution.
# The 'tempfile' module automatically handles cleanup when the file is no longer needed.
import tempfile
with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_file.write(b"Temporary data")
    temp_file.seek(0)
    print(temp_file.read())  # Use the temporary file for intermediate storage
# Advanced: Temporary files are especially useful in multi-threaded or parallel execution environments 
# where data isolation between threads is crucial.

# 9. Consider using mmap for efficient handling of very large files
# Memory-mapped files (using the 'mmap' module) allow you to work with large files as if they were in memory.
# This can provide significant performance improvements when handling extremely large datasets.
import mmap
with open('largefile.txt', 'r+b') as f:
    with mmap.mmap(f.fileno(), 0) as mm:
        print(mm.readline())  # Efficiently read a line from a large file
# Advanced tip: Use mmap when you need random access to file data or need to handle files larger than your available RAM.

# 10. Use csv, json, and pickle modules for working with specific file formats
# These modules provide specialized tools for reading and writing common data formats:
# - 'csv' for comma-separated values, 'json' for JavaScript Object Notation, and 'pickle' for Python-specific object serialization.
import csv, json, pickle
# Example: Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'occupation'])
    writer.writerow(['Alice', 30, 'Engineer'])
# Best practice: Use the appropriate module for the file format you're working with to avoid re-inventing the wheel.

# 11. Remember that pickle can be a security risk if loading untrusted data
# The 'pickle' module allows you to serialize and deserialize Python objects, but be cautious.
# Loading untrusted pickle data can execute arbitrary code and pose a security risk.
with open('data.pickle', 'wb') as file:
    pickle.dump({'key': 'value'}, file)
# Always validate or avoid loading pickle data from untrusted sources. If necessary, consider safer alternatives like 'json' for data exchange.

# 12. Use io.StringIO and io.BytesIO for working with file-like objects in memory
# The 'io' module provides StringIO (for text) and BytesIO (for binary data) that let you handle in-memory file-like objects.
# These are useful for testing, mocking file operations, or working with small chunks of data.
import io
memory_file = io.StringIO()
memory_file.write("This is in-memory text data.")
print(memory_file.getvalue())  # Retrieves the written content
# Advanced tip: This is particularly useful in scenarios where you want to avoid disk I/O for performance reasons 
# or when testing file operations in unit tests.

# This concludes the enhanced detailed Python Cheat Sheet for File Handling