"""
File Handling - Reading and Writing Text Files - in the Python Programming Language
===================================================================================

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
File handling, particularly reading and writing text files, is a fundamental concept in Python programming. It allows developers to interact with the file system, persist data, and process large amounts of information efficiently.

Historical context:
- File I/O operations have been a part of Python since its inception in 1991.
- Python 2.5 (2006) introduced the 'with' statement, simplifying resource management for file operations.
- Python 3.0 (2008) made significant changes to file I/O, including making all strings Unicode by default.

Significance:
- File handling is crucial for data persistence, configuration management, and data processing.
- It serves as a foundation for more complex I/O operations and database interactions.
- Efficient file handling is essential for building scalable and performant applications.

Common use cases:
- Reading and writing configuration files
- Processing large datasets
- Logging application events
- Importing and exporting data in various formats (CSV, JSON, etc.)

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import os
import io
import csv
import json
from typing import List, Dict, Any
import asyncio

def read_file_basic(file_path: str) -> str:
    """
    Read the entire contents of a file using the basic file open method.
    
    This function demonstrates the most straightforward way to read a file,
    but it's not suitable for very large files as it loads the entire content into memory.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file_basic(file_path: str, content: str) -> None:
    """
    Write content to a file using the basic file open method.
    
    This function overwrites the existing file content or creates a new file if it doesn't exist.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def read_file_line_by_line(file_path: str) -> List[str]:
    """
    Read a file line by line, which is more memory-efficient for large files.
    
    This method is useful when processing files that are too large to fit in memory.
    """
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())  # strip() removes leading/trailing whitespace
    return lines

def append_to_file(file_path: str, content: str) -> None:
    """
    Append content to the end of an existing file.
    
    This function is useful for logging or adding new data without overwriting existing content.
    """
    with open(file_path, 'a') as file:
        file.write(content + '\n')  # Add a newline for better formatting

def read_csv_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read a CSV file and return its contents as a list of dictionaries.
    
    This function assumes the CSV file has a header row.
    """
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_csv_file(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Write a list of dictionaries to a CSV file.
    
    This function assumes all dictionaries in the list have the same keys.
    """
    if not data:
        return

    fieldnames = data[0].keys()
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def read_json_file(file_path: str) -> Any:
    """
    Read a JSON file and return its contents as a Python object.
    
    This function can handle any JSON-serializable data structure.
    """
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data

def write_json_file(file_path: str, data: Any) -> None:
    """
    Write a Python object to a JSON file.
    
    This function can handle any JSON-serializable data structure.
    """
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)  # indent for pretty-printing

async def read_file_async(file_path: str) -> str:
    """
    Read a file asynchronously using aiofiles.
    
    This function demonstrates how to perform file I/O in an asynchronous context.
    Note: This requires the 'aiofiles' package to be installed.
    """
    import aiofiles  # Make sure to install this package: pip install aiofiles
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
    return content

def demonstrate_file_operations():
    """Demonstrate various file handling operations."""
    # Basic read and write
    write_file_basic('example.txt', 'Hello, World!')
    content = read_file_basic('example.txt')
    print(f"Basic read: {content}")

    # Line by line reading
    write_file_basic('multiline.txt', 'Line 1\nLine 2\nLine 3')
    lines = read_file_line_by_line('multiline.txt')
    print(f"Line by line read: {lines}")

    # Appending to a file
    append_to_file('log.txt', 'Log entry 1')
    append_to_file('log.txt', 'Log entry 2')
    log_content = read_file_basic('log.txt')
    print(f"Log file content: {log_content}")

    # CSV operations
    csv_data = [
        {'name': 'Alice', 'age': '30'},
        {'name': 'Bob', 'age': '25'},
        {'name': 'Charlie', 'age': '35'}
    ]
    write_csv_file('people.csv', csv_data)
    read_csv = read_csv_file('people.csv')
    print(f"CSV read: {read_csv}")

    # JSON operations
    json_data = {'key1': 'value1', 'key2': [1, 2, 3], 'key3': {'nested': 'dict'}}
    write_json_file('data.json', json_data)
    read_json = read_json_file('data.json')
    print(f"JSON read: {read_json}")

    # Asynchronous file reading
    async def async_read():
        content = await read_file_async('example.txt')
        print(f"Async read: {content}")

    asyncio.run(async_read())

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Always use the 'with' statement for file operations to ensure proper resource management.
2. Use appropriate encoding (e.g., 'utf-8') when dealing with non-ASCII text.
3. Handle exceptions properly, especially FileNotFoundError and PermissionError.
4. Use binary mode ('rb', 'wb') when dealing with non-text files.
5. Prefer built-in modules like csv and json for structured data instead of parsing manually.

Common Pitfalls:
1. Forgetting to close files when not using 'with' statement.
2. Assuming the default encoding is suitable for all text files.
3. Not handling file system permissions or disk space issues.
4. Reading entire large files into memory instead of processing them in chunks.
5. Using text mode for binary files, leading to data corruption.

Advanced Tips:
1. Use mmap for memory-mapped file I/O when dealing with very large files.
2. Implement custom context managers for complex file operations.
3. Use tempfile module for creating and managing temporary files securely.
4. Leverage asyncio and aiofiles for non-blocking file I/O in asynchronous applications.
5. Use io.StringIO and io.BytesIO for in-memory file-like objects.
"""

import mmap
import tempfile
from contextlib import contextmanager

def read_large_file_mmap(file_path: str) -> List[str]:
    """
    Read a large file using memory-mapped I/O.
    
    This method is extremely efficient for large files, especially when
    random access is needed.
    """
    with open(file_path, 'r') as file:
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmap_obj:
            return mmap_obj.read().decode('utf-8').splitlines()

@contextmanager
def atomic_write(file_path: str, mode='w'):
    """
    A context manager for atomic file writes.
    
    This ensures that the file is only updated if all write operations succeed.
    """
    temp_path = file_path + '.tmp'
    with open(temp_path, mode) as file:
        yield file
    os.rename(temp_path, file_path)

def demonstrate_advanced_techniques():
    """Demonstrate advanced file handling techniques."""
    # Memory-mapped file reading
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
        temp.write('Line 1\nLine 2\nLine 3\n')
        temp_path = temp.name

    lines = read_large_file_mmap(temp_path)
    print(f"Memory-mapped read: {lines}")
    os.unlink(temp_path)

    # Atomic write
    with atomic_write('atomic_file.txt') as file:
        file.write('This write is atomic\n')
    
    content = read_file_basic('atomic_file.txt')
    print(f"Atomic write result: {content}")

    # In-memory file-like object
    with io.StringIO() as string_io:
        string_io.write('In-memory text\n')
        string_io.seek(0)
        content = string_io.read()
    print(f"In-memory file content: {content}")

"""
4. Integration and Real-World Applications
------------------------------------------
File handling is integral to many Python applications and frameworks:

1. Configuration management: Libraries like configparser use file I/O for .ini files.
2. Web frameworks: Django and Flask often use file operations for template rendering and static file serving.
3. Data processing: Pandas heavily relies on file I/O for reading and writing various data formats.
4. Logging: The logging module writes log messages to files.

Real-world example: A simple logging system with rotation
"""

import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file: str, max_size: int, backup_count: int):
    """
    Set up a rotating log system.
    
    This function demonstrates a practical application of file handling in a logging context.
    """
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

def demonstrate_real_world_application():
    """Demonstrate a real-world application of file handling in logging."""
    logger = setup_logging('app.log', 1024 * 1024, 3)  # 1MB file size, 3 backups
    
    for i in range(1000):
        logger.info(f"Log message {i}")
    
    print("Check app.log and rotated logs (app.log.1, app.log.2, etc.) in the current directory.")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous I/O: Growing support for async file operations with libraries like aiofiles.
2. Object storage: Interfacing with cloud storage services (e.g., S3) using file-like abstractions.
3. Memory-mapped I/O: Increased use of mmap for high-performance file access.
4. Structured file formats: Growing popularity of formats like Apache Parquet for big data applications.
5. Type hints: Improved static type checking for file operations with tools like mypy.
"""

from typing import AsyncIterator

async def aiter_file(file_path: str) -> AsyncIterator[str]:
    """
    Asynchronously iterate over file lines.
    
    This function demonstrates an emerging pattern for async file processing.
    Note: This requires the 'aiofiles' package to be installed.
    """
    import aiofiles  # Make sure to install this package: pip install aiofiles
    async with aiofiles.open(file_path, mode='r') as file:
        async for line in file:
            yield line.strip()

async def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts in file handling."""
    # Write some sample data
    with open('async_sample.txt', 'w') as f:
        f.write('Line 1\nLine 2\nLine 3\n')
    
    print("Asynchronous file iteration:")
    async for line in aiter_file('async_sample.txt'):
        print(line)

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I handle different line endings (CRLF vs LF) in text files?
A: Use the 'newline' parameter in open(). Set it to None to enable universal newlines mode.

Q: What's the difference between 'r+' and 'w+' modes?
A: 'r+' opens for reading and writing but doesn't truncate the file. 'w+' truncates the file if it exists or creates a new file.

Q: How can I read a file in chunks to avoid memory issues with large files?
A: Use the read(size) method in a loop, or use itertools.islice() for line-based chunking.

Troubleshooting:
1. FileNotFoundError: Ensure the file path is correct and the file exists.
2. PermissionError: Check file system permissions.
3. UnicodeDecodeError: Specify the correct encoding when opening the file.
4. Memory errors with large files: Use chunked reading or memory-mapped files.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- aiofiles: For asynchronous file I/O operations.
- pyfiledir: A library for advanced file and directory operations.
- watchdog: For monitoring file system events.
- chardet: For detecting file encodings.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Fluent Python" by Luciano Ramalho
- Python's official documentation on File and Directory Access: https://docs.python.org/3/library/filesys.html
- Real Python's guide on reading and writing files: https://realpython.com/read-write-files-python/
- PEP 3116 - New I/O: https://www.python.org/dev/peps/pep-3116/

8. Performance Analysis and Optimization
----------------------------------------
When working with file I/O, performance can be critical, especially for large files or high-frequency operations.
"""

import time
import io

def benchmark_file_read_methods(file_path: str, num_reads: int = 1000):
    """
    Benchmark different file reading methods.
    
    This function compares the performance of various file reading techniques.
    """
    def timed_read(read_func):
        start_time = time.time()
        for _ in range(num_reads):
            read_func()
        return time.time() - start_time

    # Method 1: Read entire file
    def read_entire():
        with open(file_path, 'r') as f:
            f.read()

    # Method 2: Read line by line
    def read_lines():
        with open(file_path, 'r') as f:
            for line in f:
                pass

    # Method 3: Read in chunks
    def read_chunks():
        with open(file_path, 'r') as f:
            while True:
                chunk = f.read(4096)  # 4KB chunks
                if not chunk:
                    break

    # Method 4: Memory-mapped reading
    def read_mmap():
        with open(file_path, 'r') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
                m.read()

    results = {
        "Read Entire File": timed_read(read_entire),
        "Read Line by Line": timed_read(read_lines),
        "Read in Chunks": timed_read(read_chunks),
        "Memory-mapped Reading": timed_read(read_mmap)
    }

    for method, time_taken in results.items():
        print(f"{method}: {time_taken:.4f} seconds")

def optimize_write_performance(file_path: str, num_lines: int = 100000):
    """
    Demonstrate and compare different file writing optimization techniques.
    
    This function shows how to optimize file writing for large datasets.
    """
    data = "This is a line of text to write.\n" * num_lines

    def write_line_by_line():
        with open(file_path, 'w') as f:
            for line in data.splitlines():
                f.write(line + '\n')

    def write_with_writelines():
        with open(file_path, 'w') as f:
            f.writelines(data.splitlines(keepends=True))

    def write_with_buffer():
        with open(file_path, 'w', buffering=8192) as f:  # 8KB buffer
            f.write(data)

    def write_with_stringio():
        buffer = io.StringIO()
        buffer.write(data)
        with open(file_path, 'w') as f:
            f.write(buffer.getvalue())

    methods = [
        ("Line by Line", write_line_by_line),
        ("writelines()", write_with_writelines),
        ("Buffered Write", write_with_buffer),
        ("StringIO Buffer", write_with_stringio)
    ]

    for name, method in methods:
        start_time = time.time()
        method()
        elapsed_time = time.time() - start_time
        print(f"{name}: {elapsed_time:.4f} seconds")

"""
Performance Considerations:
1. Reading entire files is fastest for small files but can lead to memory issues with large files.
2. Line-by-line reading is memory-efficient but can be slower for large files.
3. Chunk-based reading balances memory usage and speed.
4. Memory-mapped files can be very fast, especially for random access patterns.

Optimization Strategies:
1. Use appropriate buffer sizes when reading or writing large files.
2. Consider memory-mapped files for large files that need random access.
3. Use higher-level libraries (e.g., pandas) for structured data files, as they often implement optimized I/O.
4. When writing many small writes, use a buffer (like StringIO) to accumulate data before writing to disk.
5. For append-heavy workloads, consider using a database or append-optimized file format instead of text files.

Example of optimizing a file processing pipeline:
"""

import csv
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_large_csv(input_file: str, output_file: str, chunk_size: int = 10000):
    """
    Process a large CSV file efficiently using chunking and multithreading.
    
    This function demonstrates how to handle large datasets by processing
    them in chunks and utilizing multiple threads for improved performance.
    """
    def process_chunk(chunk: List[Dict]) -> List[Dict]:
        # Simulate some processing on each row
        return [{**row, 'processed': True} for row in chunk]

    with open(input_file, 'r', newline='') as infile, \
         open(output_file, 'w', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['processed']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        chunk = []
        with ThreadPoolExecutor() as executor:
            futures = []
            for row in reader:
                chunk.append(row)
                if len(chunk) >= chunk_size:
                    futures.append(executor.submit(process_chunk, chunk))
                    chunk = []
            
            if chunk:  # Process any remaining rows
                futures.append(executor.submit(process_chunk, chunk))
            
            for future in as_completed(futures):
                writer.writerows(future.result())

    print(f"Processed CSV saved to {output_file}")

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
- Relevance to the main topic of file handling in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to file handling.
    """
    print("1. Basic File Operations:")
    demonstrate_file_operations()

    print("\n2. Advanced Techniques:")
    demonstrate_advanced_techniques()

    print("\n3. Real-World Application (Logging):")
    demonstrate_real_world_application()

    print("\n4. Advanced Concepts (Async File I/O):")
    asyncio.run(demonstrate_advanced_concepts())

    print("\n5. Performance Benchmarking:")
    # Create a sample file for benchmarking
    with open('benchmark.txt', 'w') as f:
        f.write('Sample line\n' * 10000)

    benchmark_file_read_methods('benchmark.txt')
    
    print("\n6. Write Performance Optimization:")
    optimize_write_performance('write_benchmark.txt')

    print("\n7. Large CSV Processing:")
    # Create a sample large CSV file
    with open('large_input.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'data'])
        writer.writeheader()
        for i in range(100000):
            writer.writerow({'id': i, 'data': f'data_{i}'})

    process_large_csv('large_input.csv', 'large_output.csv')

    # Clean up benchmark files
    os.remove('benchmark.txt')
    os.remove('write_benchmark.txt')
    os.remove('large_input.csv')
    os.remove('large_output.csv')

if __name__ == "__main__":
    main()