"""
File Handling - File and Directory Management - in the Python Programming Language
==================================================================================

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
File and directory management is a fundamental aspect of programming, allowing applications to interact with the file system. In Python, this functionality is primarily provided through the built-in 'os' and 'shutil' modules, along with the 'pathlib' module introduced in Python 3.4.

Historical context:
- The 'os' module has been part of Python since its early versions, providing a way to use operating system dependent functionality.
- The 'shutil' module was introduced to provide a higher-level interface for file operations.
- Python 3.4 (2014) introduced the 'pathlib' module, offering an object-oriented approach to file system paths.

Significance:
- Essential for any application that needs to read, write, or manipulate files and directories.
- Crucial for tasks such as data processing, log management, and configuration handling.
- Enables cross-platform development by abstracting OS-specific file system operations.

Common use cases:
- Creating, moving, copying, and deleting files and directories.
- Traversing directory structures and filtering files based on various criteria.
- Managing file permissions and metadata.
- Implementing file-based data storage and retrieval systems.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import os
import shutil
from pathlib import Path
import tempfile
import glob
from typing import List, Generator
import asyncio
import aiofiles

def basic_file_operations():
    """Demonstrate basic file operations using os and shutil modules."""
    # Create a new directory
    os.mkdir('example_dir')

    # Create a new file and write to it
    with open('example_dir/test.txt', 'w') as f:
        f.write('Hello, World!')

    # Read from the file
    with open('example_dir/test.txt', 'r') as f:
        content = f.read()
    print(f"File content: {content}")

    # Copy the file
    shutil.copy('example_dir/test.txt', 'example_dir/test_copy.txt')

    # Move/rename the file
    os.rename('example_dir/test_copy.txt', 'example_dir/test_moved.txt')

    # Delete the file
    os.remove('example_dir/test_moved.txt')

    # Delete the directory
    os.rmdir('example_dir')

def pathlib_operations():
    """Demonstrate file operations using the pathlib module."""
    # Create a Path object
    path = Path('example_dir')

    # Create a directory
    path.mkdir(exist_ok=True)

    # Create and write to a file
    file_path = path / 'test.txt'
    file_path.write_text('Hello, World!')

    # Read from the file
    content = file_path.read_text()
    print(f"File content: {content}")

    # Check if a file exists
    print(f"File exists: {file_path.exists()}")

    # Get file stats
    stats = file_path.stat()
    print(f"File size: {stats.st_size} bytes")

    # Delete the file
    file_path.unlink()

    # Delete the directory
    path.rmdir()

def traverse_directory(directory: str) -> Generator[str, None, None]:
    """
    Traverse a directory and yield all file paths.
    
    This function demonstrates how to recursively walk through a directory structure.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def filter_files_by_extension(directory: str, extension: str) -> List[str]:
    """
    Filter files in a directory by their extension.
    
    This function shows how to use glob to filter files based on patterns.
    """
    pattern = os.path.join(directory, f'*.{extension}')
    return glob.glob(pattern)

async def async_file_read(file_path: str) -> str:
    """
    Read a file asynchronously.
    
    This function demonstrates asynchronous file I/O operations.
    """
    async with aiofiles.open(file_path, mode='r') as file:
        return await file.read()

def demonstrate_file_operations():
    """Demonstrate various file and directory operations."""
    print("Basic file operations:")
    basic_file_operations()

    print("\nPathlib operations:")
    pathlib_operations()

    # Create a temporary directory for demonstration
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some sample files
        for i in range(5):
            with open(os.path.join(temp_dir, f'file{i}.txt'), 'w') as f:
                f.write(f'Content of file {i}')
        with open(os.path.join(temp_dir, 'example.py'), 'w') as f:
            f.write('print("Hello, World!")')

        print("\nTraversing directory:")
        for file_path in traverse_directory(temp_dir):
            print(file_path)

        print("\nFiltering files by extension:")
        py_files = filter_files_by_extension(temp_dir, 'py')
        print(f"Python files: {py_files}")

    print("\nAsynchronous file reading:")
    async def async_read_example():
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write("Async file content")
            temp_file_path = temp_file.name

        content = await async_file_read(temp_file_path)
        print(f"Async read content: {content}")

        os.unlink(temp_file_path)

    asyncio.run(async_read_example())

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use context managers (with statements) when working with files to ensure proper resource management.
2. Prefer pathlib over os.path for better readability and cross-platform compatibility.
3. Use tempfile for creating temporary files and directories to avoid naming conflicts and ensure cleanup.
4. Always handle exceptions when performing file operations.

Common Pitfalls:
1. Forgetting to close file handles, leading to resource leaks.
2. Using hardcoded file paths, making the code less portable.
3. Not handling file system permissions correctly, especially in multi-user environments.
4. Inefficient file reading/writing for large files.

Advanced Tips:
1. Use mmap for memory-mapped file I/O when dealing with very large files.
2. Implement custom context managers for complex file operations.
3. Use fcntl (on Unix systems) for file locking in concurrent environments.
4. Leverage asyncio and aiofiles for non-blocking file I/O in asynchronous applications.
"""

import mmap
import fcntl
import struct

def read_large_file_mmap(file_path: str) -> List[str]:
    """
    Read a large file using memory-mapped I/O.
    
    This method is extremely efficient for large files, especially when
    random access is needed.
    """
    with open(file_path, 'r') as file:
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmap_obj:
            return mmap_obj.read().decode('utf-8').splitlines()

def file_lock_example(file_path: str):
    """
    Demonstrate file locking using fcntl.
    
    This is useful in multi-process environments to ensure exclusive access to a file.
    """
    with open(file_path, 'w') as file:
        try:
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            file.write('Writing with exclusive lock')
            fcntl.flock(file, fcntl.LOCK_UN)
        except IOError:
            print("Could not obtain lock")

def demonstrate_advanced_techniques():
    """Demonstrate advanced file handling techniques."""
    # Memory-mapped file reading
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write('Line 1\nLine 2\nLine 3\n')
        temp_file_path = temp_file.name

    lines = read_large_file_mmap(temp_file_path)
    print(f"Memory-mapped read: {lines}")

    # File locking
    file_lock_example(temp_file_path)

    os.unlink(temp_file_path)

"""
4. Integration and Real-World Applications
------------------------------------------
File and directory management is integral to many Python applications and frameworks:

1. Web frameworks: Django and Flask use file operations for handling static files and uploads.
2. Data processing: Libraries like pandas rely heavily on file I/O for data import and export.
3. Configuration management: Many applications use file-based configurations (e.g., .ini, .yaml files).
4. Logging: The logging module writes log messages to files.

Real-world example: A simple backup system
"""

import datetime
import zipfile

def create_backup(source_dir: str, backup_dir: str):
    """
    Create a backup of a directory.
    
    This function demonstrates a practical application of file and directory management.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)

    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

    print(f"Backup created: {backup_path}")

def demonstrate_real_world_application():
    """Demonstrate a real-world application of file and directory management."""
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as backup_dir:
        # Create some sample files
        for i in range(3):
            with open(os.path.join(source_dir, f'file{i}.txt'), 'w') as f:
                f.write(f'Content of file {i}')

        create_backup(source_dir, backup_dir)

        # List the contents of the backup directory
        print("Backup directory contents:")
        for item in os.listdir(backup_dir):
            print(item)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Virtual file systems: Abstracting file operations to work with cloud storage or in-memory file systems.
2. Improved async file I/O: Enhanced support for asynchronous file operations in Python.
3. File system events: Monitoring file system changes using libraries like watchdog.
4. Object storage integration: Seamless integration with object storage systems like S3.
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File {event.src_path} has been modified')

def demonstrate_file_system_monitoring():
    """Demonstrate file system monitoring using watchdog."""
    path = tempfile.mkdtemp()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        print(f"Monitoring directory: {path}")
        print("Modify a file in this directory (Ctrl+C to stop)...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    shutil.rmtree(path)

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I handle file paths across different operating systems?
A: Use os.path.join() or pathlib.Path to create portable file paths.

Q: What's the best way to read a large file without loading it entirely into memory?
A: Use a generator to read the file line by line, or use mmap for random access.

Q: How can I safely write to a file to avoid data corruption in case of a crash?
A: Use a temporary file for writing and then atomically replace the original file.

Troubleshooting:
1. PermissionError: Check file system permissions and whether the file is in use by another process.
2. FileNotFoundError: Ensure the file path is correct and the file exists.
3. disk full errors: Check available disk space and implement proper error handling.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- pathlib: For object-oriented file system path handling.
- shutil: For high-level file operations.
- watchdog: For monitoring file system events.
- PyFilesystem: For working with virtual file systems.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Effective Python" by Brett Slatkin
- Python's official documentation on File and Directory Access: https://docs.python.org/3/library/filesys.html
- Real Python's guide on Python File I/O: https://realpython.com/read-write-files-python/
- PEP 519 - Adding a file system path protocol: https://www.python.org/dev/peps/pep-0519/

8. Performance Analysis and Optimization
----------------------------------------
When working with file I/O, performance can be critical, especially for large files or high-frequency operations.
"""

import time
import cProfile
import pstats
from io import StringIO

def benchmark_file_operations(file_path: str, num_operations: int = 1000):
    """
    Benchmark different file reading and writing methods.
    
    This function compares the performance of various file I/O techniques.
    """
    def timed_operation(operation, *args):
        start_time = time.time()
        for _ in range(num_operations):
            operation(*args)
        return time.time() - start_time

    # Write benchmarking
    write_time = timed_operation(lambda: open(file_path, 'w').write('test'))
    print(f"Simple write time: {write_time:.4f} seconds")

    write_time_with = timed_operation(lambda: open(file_path, 'w').__enter__().write('test'))
    print(f"Write time with context manager: {write_time_with:.4f} seconds")

    # Read benchmarking
    read_time = timed_operation(lambda: open(file_path, 'r').read())
    print(f"Simple read time: {read_time:.4f} seconds")

    read_time_with = timed_operation(lambda: open(file_path, 'r').__enter__().read())
    print(f"Read time with context manager: {read_time_with:.4f} seconds")

def profile_directory_traversal(directory: str):
    """
    Profile directory traversal to identify performance bottlenecks.
    """
    profiler = cProfile.Profile()
    profiler.enable()
    
    for _ in traverse_directory(directory):
        pass
    
    profiler.disable()
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

"""
Performance Considerations (continued):
4. Be aware of the performance implications of file system operations on different storage types (e.g., SSD vs HDD).
5. Use asynchronous I/O for I/O-bound operations in concurrent applications.

Optimization Strategies:
1. Batch file operations to reduce the number of system calls.
2. Use line-oriented file reading for large text files instead of reading the entire file into memory.
3. Implement caching mechanisms for frequently accessed files or directories.
4. Use appropriate compression algorithms for storing large amounts of data.
5. Consider using specialized file formats (e.g., HDF5 for scientific data) for domain-specific optimizations.

Example of optimizing directory traversal:
"""

import os
from collections import deque

def optimized_directory_traversal(directory: str) -> Generator[str, None, None]:
    """
    An optimized version of directory traversal using a deque for better performance.
    
    This method is more efficient for deep directory structures.
    """
    queue = deque([directory])
    while queue:
        current_dir = queue.popleft()
        try:
            with os.scandir(current_dir) as it:
                for entry in it:
                    if entry.is_file():
                        yield entry.path
                    elif entry.is_dir():
                        queue.append(entry.path)
        except PermissionError:
            print(f"Permission denied: {current_dir}")

def demonstrate_optimization():
    """Demonstrate optimized file and directory operations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a sample directory structure
        for i in range(5):
            subdir = os.path.join(temp_dir, f'subdir{i}')
            os.mkdir(subdir)
            for j in range(10):
                with open(os.path.join(subdir, f'file{j}.txt'), 'w') as f:
                    f.write(f'Content of file {j}')

        print("Optimized directory traversal:")
        for file_path in optimized_directory_traversal(temp_dir):
            print(file_path)

        print("\nBenchmarking optimized vs. standard traversal:")
        start_time = time.time()
        list(traverse_directory(temp_dir))
        standard_time = time.time() - start_time
        
        start_time = time.time()
        list(optimized_directory_traversal(temp_dir))
        optimized_time = time.time() - start_time
        
        print(f"Standard traversal time: {standard_time:.4f} seconds")
        print(f"Optimized traversal time: {optimized_time:.4f} seconds")

"""
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
- Relevance to the main topic of file and directory management in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to file and directory management.
    """
    print("1. Basic File and Directory Operations:")
    demonstrate_file_operations()

    print("\n2. Advanced Techniques:")
    demonstrate_advanced_techniques()

    print("\n3. Real-World Application (Backup System):")
    demonstrate_real_world_application()

    print("\n4. File System Monitoring:")
    demonstrate_file_system_monitoring()

    print("\n5. Performance Benchmarking:")
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    benchmark_file_operations(temp_file_path)
    os.unlink(temp_file_path)

    print("\n6. Directory Traversal Profiling:")
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some sample files and directories
        for i in range(5):
            os.mkdir(os.path.join(temp_dir, f'dir{i}'))
            for j in range(10):
                open(os.path.join(temp_dir, f'dir{i}', f'file{j}.txt'), 'w').close()
        profile_directory_traversal(temp_dir)

    print("\n7. Optimization Demonstration:")
    demonstrate_optimization()

if __name__ == "__main__":
    main()