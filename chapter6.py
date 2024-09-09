# Python Cheat Sheet: File Handling
import os
import json
import csv
import pickle
import shutil
import tempfile
import mmap
import gzip
import zipfile
import io

# 1. Reading and Writing Text Files

# Basic file opening and reading
file_path = 'example.txt'

# Using 'with' statement (recommended for automatic file closing)
with open(file_path, 'r') as file:
    content = file.read()
    print(f"File contents:\n{content}")

# Tip: Always use 'with' statements to ensure proper file handling and resource management

# Writing to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')

# Tip: 'w' mode overwrites existing content. Use 'a' for appending

# Appending to a file
with open('output.txt', 'a') as file:
    file.write('\nThis line is appended.')

# Reading lines
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes leading/trailing whitespace

# Tip: Use readlines() for small files. For large files, iterate directly over the file object

# Reading line by line (memory-efficient for large files)
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())

# Tip: This method is more memory-efficient for large files as it doesn't load the entire file into memory

# 2. File Modes and Encoding

# 'r': Read (default)
# 'w': Write (overwrites)
# 'a': Append
# 'x': Exclusive creation
# 'b': Binary mode
# '+': Read and write

# Specifying encoding (important for non-ASCII text)
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Tip: Always specify the encoding to avoid issues with non-ASCII characters

# 3. Working with Binary Files

# Writing binary data
data = bytes([0, 1, 2, 3, 4, 5])
with open('binary_file.bin', 'wb') as file:
    file.write(data)

# Reading binary data
with open('binary_file.bin', 'rb') as file:
    binary_data = file.read()
    print(f"Binary data: {binary_data}")

# Tip: Use 'rb' and 'wb' modes for working with binary files like images or compiled files

# 4. Working with Different File Formats

# CSV Files
# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Tip: Use newline='' to ensure consistent line endings across platforms

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Tip: For more control, use csv.DictReader and csv.DictWriter

# JSON Files
# Writing JSON
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Tip: Use indent for pretty-printing JSON, making it more readable

# Reading JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(f"Loaded JSON data: {loaded_data}")

# Tip: json.loads() and json.dumps() work with strings instead of file objects

# Pickle (for serializing Python objects)
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# Writing pickle
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Reading pickle
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
    print(f"Loaded pickle data: {loaded_data}")

# Tip: Pickle is Python-specific and can be a security risk if loading untrusted data

# 5. File and Directory Operations

# Current working directory
print(f"Current working directory: {os.getcwd()}")

# Changing directory
os.chdir('/path/to/new/directory')

# Listing directory contents
print(f"Directory contents: {os.listdir('.')}")

# Creating a new directory
os.mkdir('new_directory')

# Creating nested directories
os.makedirs('nested/directory/structure', exist_ok=True)

# Tip: use exist_ok=True to avoid raising an error if the directory already exists

# Removing a file
os.remove('file_to_delete.txt')

# Removing an empty directory
os.rmdir('empty_directory')

# Removing a directory and its contents
shutil.rmtree('directory_to_delete')

# Tip: Be cautious with shutil.rmtree() as it deletes everything without confirmation

# Renaming files or directories
os.rename('old_name.txt', 'new_name.txt')

# Moving files or directories
shutil.move('source.txt', 'destination/source.txt')

# Copying files
shutil.copy('source.txt', 'destination.txt')

# Copying directories
shutil.copytree('source_dir', 'destination_dir')

# 6. Working with Paths

# Joining path components (cross-platform)
path = os.path.join('folder', 'subfolder', 'file.txt')
print(f"Joined path: {path}")

# Absolute path
abs_path = os.path.abspath('relative_path.txt')
print(f"Absolute path: {abs_path}")

# Directory and file name of a path
dir_name = os.path.dirname(path)
file_name = os.path.basename(path)
print(f"Directory: {dir_name}, File: {file_name}")

# Splitting path into directory and file
dir_name, file_name = os.path.split(path)

# Tip: os.path functions work with strings and don't check actual file existence

# Check if a path exists
print(f"Path exists: {os.path.exists(path)}")

# Check if it's a file or directory
print(f"Is file: {os.path.isfile(path)}")
print(f"Is directory: {os.path.isdir(path)}")

# File extension
_, extension = os.path.splitext(file_name)
print(f"File extension: {extension}")

# 7. Advanced File Operations

# Using fileinput to edit files in-place
import fileinput

# Replacing a string in multiple files
files_to_search = ['file1.txt', 'file2.txt', 'file3.txt']
with fileinput.input(files=files_to_search, inplace=True) as f:
    for line in f:
        print(line.replace('old_string', 'new_string'), end='')

# Tip: fileinput is great for processing multiple files or stdin

# Memory-mapped files
with open('large_file.bin', 'rb') as f:
    mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(f"First 10 bytes: {mmapped_file[0:10]}")
    mmapped_file.close()

# Tip: Memory-mapped files can be more efficient for large files

# 8. Working with Compressed Files

# Writing to a gzip file
with gzip.open('data.txt.gz', 'wt') as f:
    f.write('This content will be compressed')

# Reading from a gzip file
with gzip.open('data.txt.gz', 'rt') as f:
    content = f.read()
    print(f"Decompressed content: {content}")

# Working with ZIP files
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted_folder')

# Tip: Use zipfile.ZipFile with 'with' statement for proper cleanup

# 9. Temporary Files and Directories

# Create a temporary file
with tempfile.NamedTemporaryFile(mode='w+') as temp:
    temp.write('This is temporary content')
    temp.seek(0)
    print(f"Temp file content: {temp.read()}")

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Created temporary directory: {temp_dir}")

# Tip: Temporary files and directories are automatically cleaned up when the context manager exits

# 10. File-like Objects

# StringIO for working with strings as files
string_io = io.StringIO()
string_io.write('Hello, StringIO!')
string_io.seek(0)
print(f"StringIO content: {string_io.read()}")
string_io.close()

# BytesIO for working with bytes as files
bytes_io = io.BytesIO(b'Hello, BytesIO!')
print(f"BytesIO content: {bytes_io.getvalue()}")
bytes_io.close()

# Tip: StringIO and BytesIO are useful for testing or when you need file-like behavior without actual files

# 11. Context Managers for File Handling

# Custom context manager for file handling
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using the custom context manager
with FileManager('example.txt', 'r') as f:
    content = f.read()
    print(f"File content: {content}")

# Tip: Custom context managers can add extra functionality like logging or error handling

# 12. Best Practices and Tips

# 1. Always use 'with' statements for file operations to ensure proper closing
# 2. Specify file encoding explicitly to avoid platform-dependent behavior
# 3. Use appropriate modes ('r', 'w', 'a', 'b') based on your needs
# 4. For large files, read line-by-line instead of loading the entire file into memory
# 5. Use os.path functions for cross-platform path handling
# 6. Be cautious with file deletion operations, especially when using wildcards
# 7. Handle exceptions properly, especially IOError and OSError for file operations
# 8. Use tempfile module for creating temporary files and directories
# 9. Consider using mmap for efficient handling of very large files
# 10. Use csv, json, and pickle modules for working with specific file formats
# 11. Remember that pickle can be a security risk if loading untrusted data
# 12. Use io.StringIO and io.BytesIO for working with file-like objects in memory

# This concludes the enhanced detailed Python Cheat Sheet for File Handling