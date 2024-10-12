"""
Python Standard Library - os and sys modules - in the Python Programming Language
=================================================================================

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
The os and sys modules are core components of Python's standard library, providing essential functionalities for interacting with the operating system and the Python interpreter itself.

Historical context:
- Both modules have been part of Python since its early versions.
- The os module was introduced to provide a portable way of using operating system-dependent functionality.
- The sys module was created to provide access to some variables used or maintained by the Python interpreter.

Significance:
- os module: Provides a portable way of using operating system-dependent functionality.
- sys module: Offers access to some variables and functions that interact strongly with the interpreter.

Common use cases:
- File and directory operations (os)
- Environment variables manipulation (os)
- Command-line arguments processing (sys)
- Python interpreter information and control (sys)

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import os
import sys
import shutil
from typing import List, Dict, Any

def demonstrate_os_basics():
    """Demonstrate basic usage of the os module."""
    # Current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # List directory contents
    print(f"Contents of current directory: {os.listdir()}")
    
    # Create a new directory
    os.makedirs("test_dir", exist_ok=True)
    print("Created 'test_dir' directory")
    
    # Change current working directory
    os.chdir("test_dir")
    print(f"Changed working directory to: {os.getcwd()}")
    
    # Create a file
    with open("test_file.txt", "w") as f:
        f.write("Hello, os module!")
    
    # Get file information
    file_stat = os.stat("test_file.txt")
    print(f"File size: {file_stat.st_size} bytes")
    
    # Rename a file
    os.rename("test_file.txt", "renamed_file.txt")
    print("Renamed 'test_file.txt' to 'renamed_file.txt'")
    
    # Remove a file
    os.remove("renamed_file.txt")
    print("Removed 'renamed_file.txt'")
    
    # Go back to the original directory
    os.chdir("..")
    
    # Remove the test directory
    os.rmdir("test_dir")
    print("Removed 'test_dir' directory")

def demonstrate_os_path():
    """Demonstrate usage of os.path module."""
    file_path = os.path.join("folder", "subfolder", "file.txt")
    print(f"Joined path: {file_path}")
    
    print(f"Base name: {os.path.basename(file_path)}")
    print(f"Directory name: {os.path.dirname(file_path)}")
    
    absolute_path = os.path.abspath(file_path)
    print(f"Absolute path: {absolute_path}")
    
    print(f"Is absolute path? {os.path.isabs(absolute_path)}")
    
    print(f"Does path exist? {os.path.exists(file_path)}")

def demonstrate_sys_basics():
    """Demonstrate basic usage of the sys module."""
    # Python version
    print(f"Python version: {sys.version}")
    
    # Platform
    print(f"Platform: {sys.platform}")
    
    # Command-line arguments
    print(f"Command-line arguments: {sys.argv}")
    
    # Module search path
    print("Python module search path:")
    for path in sys.path:
        print(f"  {path}")
    
    # Get size of an object
    sample_list = [1, 2, 3, 4, 5]
    print(f"Size of sample_list: {sys.getsizeof(sample_list)} bytes")

def process_command_line_args(args: List[str]) -> Dict[str, Any]:
    """Process command-line arguments."""
    result = {}
    for arg in args[1:]:  # Skip the script name
        if arg.startswith("--"):
            key, value = arg[2:].split("=")
            result[key] = value
    return result

def demonstrate_env_variables():
    """Demonstrate working with environment variables."""
    # Get an environment variable
    path = os.environ.get("PATH", "PATH not found")
    print(f"PATH environment variable: {path[:50]}...")  # Print first 50 characters
    
    # Set a new environment variable
    os.environ["MY_VAR"] = "Hello, Environment!"
    print(f"MY_VAR environment variable: {os.environ.get('MY_VAR')}")
    
    # Remove an environment variable
    os.environ.pop("MY_VAR", None)
    print(f"MY_VAR after removal: {os.environ.get('MY_VAR', 'Not found')}")

def demonstrate_file_operations():
    """Demonstrate advanced file operations."""
    # Create a temporary directory
    temp_dir = "temp_test_dir"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create some files
    for i in range(5):
        with open(os.path.join(temp_dir, f"file_{i}.txt"), "w") as f:
            f.write(f"Content of file {i}")
    
    # Walk through the directory
    print("Walking through the directory:")
    for root, dirs, files in os.walk(temp_dir):
        print(f"Root: {root}")
        print(f"Directories: {dirs}")
        print(f"Files: {files}")
    
    # Use shutil for advanced file operations
    shutil.copytree(temp_dir, "temp_test_dir_copy")
    print("Copied directory tree")
    
    shutil.rmtree(temp_dir)
    shutil.rmtree("temp_test_dir_copy")
    print("Removed directory trees")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use os.path functions for path manipulations to ensure cross-platform compatibility.
2. Prefer pathlib over os.path for more object-oriented path manipulations in Python 3.4+.
3. Use context managers (with statement) when working with files to ensure proper closure.
4. Use shutil for high-level file operations like copying or moving directory trees.

Common Pitfalls:
1. Hardcoding path separators instead of using os.path.join.
2. Not handling file not found or permission errors when working with files and directories.
3. Modifying sys.path directly instead of using proper Python packaging.
4. Relying on the current working directory (os.getcwd()) in scripts meant to be run from different locations.

Advanced Tips:
1. Use os.scandir() for faster directory iteration in Python 3.5+.
2. Leverage os.replace() for atomic file replacements.
3. Use sys.exit() for proper script termination with status codes.
4. Utilize sys.modules to inspect or modify loaded modules at runtime.
"""

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques with os and sys modules."""
    # Fast directory iteration with os.scandir()
    print("Iterating directory with os.scandir():")
    with os.scandir(".") as entries:
        for entry in entries:
            print(f"Name: {entry.name}, Is File: {entry.is_file()}, Is Dir: {entry.is_dir()}")
    
    # Atomic file replacement
    with open("temp_file.txt", "w") as f:
        f.write("Original content")
    
    with open("new_temp_file.txt", "w") as f:
        f.write("New content")
    
    os.replace("new_temp_file.txt", "temp_file.txt")
    print("Performed atomic file replacement")
    
    with open("temp_file.txt", "r") as f:
        print(f"Content after replacement: {f.read()}")
    
    os.remove("temp_file.txt")
    
    # Inspecting loaded modules
    print("\nLoaded modules:")
    for module_name, module in sys.modules.items():
        if "os" in module_name or "sys" in module_name:
            print(f"  {module_name}: {module}")

"""
4. Integration and Real-World Applications
------------------------------------------
The os and sys modules are fundamental in many Python applications and frameworks:

1. Web frameworks like Django use os for file handling and path management.
2. Data processing scripts often use sys.argv for command-line argument parsing.
3. System administration tools heavily rely on os for file system operations.

Real-world example: A simple backup script
"""

import datetime
import zipfile

def create_backup(source_dir: str, backup_dir: str) -> None:
    """Create a backup of the source directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = os.path.join(backup_dir, f"backup_{timestamp}.zip")
    
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    
    print(f"Backup created: {zip_filename}")

def demonstrate_real_world_application():
    """Demonstrate a real-world application using os and sys modules."""
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_dir> <backup_dir>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    backup_dir = sys.argv[2]
    
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        sys.exit(1)
    
    os.makedirs(backup_dir, exist_ok=True)
    
    create_backup(source_dir, backup_dir)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous file operations: Using asyncio with os module for non-blocking file I/O.
2. OS-specific optimizations: Leveraging os.sendfile() for efficient file copying on Unix.
3. Enhanced path handling: The pathlib module as a more powerful alternative to os.path.
"""

import asyncio
import aiofiles

async def async_file_read(filename: str) -> str:
    """Asynchronously read a file."""
    async with aiofiles.open(filename, mode='r') as file:
        return await file.read()

def demonstrate_sendfile():
    """Demonstrate the use of os.sendfile for efficient file copying."""
    if hasattr(os, 'sendfile'):
        with open('source.txt', 'wb') as src:
            src.write(b'Hello, sendfile!')
        
        with open('source.txt', 'rb') as src, open('dest.txt', 'wb') as dst:
            os.sendfile(dst.fileno(), src.fileno(), 0, os.fstat(src.fileno()).st_size)
        
        print("File copied using os.sendfile()")
        os.remove('source.txt')
        os.remove('dest.txt')
    else:
        print("os.sendfile() is not available on this platform")

from pathlib import Path

def demonstrate_pathlib():
    """Demonstrate the use of pathlib as an alternative to os.path."""
    current_file = Path(__file__)
    print(f"Current file: {current_file}")
    print(f"Parent directory: {current_file.parent}")
    print(f"Is file? {current_file.is_file()}")
    print(f"File stem: {current_file.stem}")
    print(f"File suffix: {current_file.suffix}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I handle file paths across different operating systems?
A: Use os.path.join() for path construction and os.path.normpath() to normalize paths. For more advanced path handling, consider using the pathlib module.

Q: How can I safely delete a file or directory?
A: Use os.remove() for files and os.rmdir() for empty directories. For recursive directory deletion, use shutil.rmtree(), but be cautious as it's irreversible.

Q: How do I modify the Python module search path?
A: You can append to sys.path, but it's generally better to use PYTHONPATH environment variable or create proper Python packages.

Troubleshooting:
1. Issue: PermissionError when trying to access or modify files
   Solution: Check file permissions and ensure your script has the necessary access rights.

2. Issue: Files not found when using relative paths
   Solution: Use os.path.abspath() or os.path.realpath() to get the full path, or ensure your script is run from the expected directory.

3. Issue: Errors when working with Unicode filenames
   Solution: Ensure you're using Python 3, which has better Unicode support. Use sys.getfilesystemencoding() to check the file system encoding if issues persist.
"""

def demonstrate_troubleshooting():
    """Demonstrate common troubleshooting scenarios."""
    # Handling permission errors
    try:
        os.remove('/root/some_file.txt')
    except PermissionError:
        print("Permission denied. Try running the script with elevated privileges.")
    
    # Working with absolute paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.ini')
    print(f"Absolute path to config: {config_path}")
    
    # Checking file system encoding
    print(f"File system encoding: {sys.getfilesystemencoding()}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. pathlib: A more object-oriented approach to file system paths (built-in since Python 3.4).
2. shutil: High-level file operations, complementing os module functionalities.
3. glob: Unix style pathname pattern expansion.
4. tempfile: Generate temporary files and directories.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (O'Reilly)
- "Effective Python" by Brett Slatkin (Addison-Wesley)
- Python's official documentation on os module: https://docs.python.org/3/library/os.html
- Python's official documentation on sys module: https://docs.python.org/3/library/sys.html
- Real Python's guide on Python OS module: https://realpython.com/python-os-module/

8. Performance Analysis and Optimization
----------------------------------------
When working with file systems and system-level operations, performance can be critical, especially for large-scale operations.
"""

import timeit

def performance_comparison():
    """Compare the performance of different file listing methods."""
    
    def use_listdir():
        return os.listdir('.')
    
    def use_scandir():
        return [entry.name for entry in os.scandir('.')]
    
    def use_glob():
        import glob
        return glob.glob('*')
    
    def use_pathlib():
        return [p.name for p in Path('.').iterdir()]
    
    # Measure execution times
    listdir_time = timeit.timeit(use_listdir, number=1000)
    scandir_time = timeit.timeit(use_scandir, number=1000)
    glob_time = timeit.timeit(use_glob, number=1000)
    pathlib_time = timeit.timeit(use_pathlib, number=1000)
    
    print(f"os.listdir time: {listdir_time:.6f} seconds")
    print(f"os.scandir time: {scandir_time:.6f} seconds")
    print(f"glob.glob time: {glob_time:.6f} seconds")
    print(f"pathlib time: {pathlib_time:.6f} seconds")

"""
Performance Considerations:
1. File I/O operations are often the bottleneck in performance-critical applications.
2. Large directory traversals can be time-consuming, especially on network file systems.
3. Frequent system calls can introduce significant overhead.

Optimization Strategies:
1. Use os.scandir() instead of os.listdir() for faster directory iteration.
2. Leverage memory-mapped files (mmap) for large file operations.
3. Use buffered I/O operations when dealing with many small reads or writes.
4. Implement caching mechanisms for frequently accessed file information.
"""

import mmap

def demonstrate_mmap_usage():
    """Demonstrate the use of memory-mapped files for efficient I/O."""
    # Create a sample file
    with open('sample.bin', 'wb') as f:
        f.write(b'0' * 1024 * 1024)  # 1 MB of zeros
    
    def read_without_mmap():
        with open('sample.bin', 'rb') as f:
            return f.read().count(b'0')
    
    def read_with_mmap():
        with open('sample.bin', 'rb') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
                return m.read().count(b'0')
    
    # Compare performance
    without_mmap_time = timeit.timeit(read_without_mmap, number=100)
    with_mmap_time = timeit.timeit(read_with_mmap, number=100)
    
    print(f"Time without mmap: {without_mmap_time:.6f} seconds")
    print(f"Time with mmap: {with_mmap_time:.6f} seconds")
    
    # Clean up
    os.remove('sample.bin')

def demonstrate_buffered_io():
    """Demonstrate the performance difference between buffered and unbuffered I/O."""
    # Create a sample file
    with open('sample.txt', 'w') as f:
        f.write('x' * 1000000)
    
    def read_unbuffered():
        with open('sample.txt', 'r', buffering=0) as f:
            return sum(1 for _ in f)
    
    def read_buffered():
        with open('sample.txt', 'r') as f:
            return sum(1 for _ in f)
    
    # Compare performance
    unbuffered_time = timeit.timeit(read_unbuffered, number=10)
    buffered_time = timeit.timeit(read_buffered, number=10)
    
    print(f"Time with unbuffered I/O: {unbuffered_time:.6f} seconds")
    print(f"Time with buffered I/O: {buffered_time:.6f} seconds")
    
    # Clean up
    os.remove('sample.txt')

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
- Relevance to the main topic of os and sys modules in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to os and sys modules.
    """
    print("Demonstrating os module basics:")
    demonstrate_os_basics()
    
    print("\nDemonstrating os.path usage:")
    demonstrate_os_path()
    
    print("\nDemonstrating sys module basics:")
    demonstrate_sys_basics()
    
    print("\nDemonstrating environment variables:")
    demonstrate_env_variables()
    
    print("\nDemonstrating file operations:")
    demonstrate_file_operations()
    
    print("\nDemonstrating advanced techniques:")
    demonstrate_advanced_techniques()
    
    print("\nDemonstrating real-world application (backup script):")
    # Note: This would typically be run with command-line arguments
    # For demonstration, we'll use dummy arguments
    sys.argv = ['script.py', '.', 'backup']
    demonstrate_real_world_application()
    
    print("\nDemonstrating sendfile usage:")
    demonstrate_sendfile()
    
    print("\nDemonstrating pathlib usage:")
    demonstrate_pathlib()
    
    print("\nDemonstrating troubleshooting scenarios:")
    demonstrate_troubleshooting()
    
    print("\nPerformance comparison of file listing methods:")
    performance_comparison()
    
    print("\nDemonstrating mmap usage:")
    demonstrate_mmap_usage()
    
    print("\nDemonstrating buffered I/O performance:")
    demonstrate_buffered_io()

if __name__ == "__main__":
    main()