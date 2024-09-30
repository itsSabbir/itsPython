"""
File Handling - Working with CSV, JSON, and XML - in the Python Programming Language
====================================================================================

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
CSV (Comma-Separated Values), JSON (JavaScript Object Notation), and XML (eXtensible Markup Language) are widely used data formats for storing and exchanging structured information. Python provides robust built-in and third-party libraries for handling these formats efficiently.

Historical context:
- CSV: A simple, tabular data format that has been in use since the early days of computing.
- JSON: Introduced in the early 2000s as a lightweight data interchange format, gaining popularity with the rise of web APIs.
- XML: Developed in the late 1990s, it became a standard for representing structured data in a human-readable format.

Significance:
- CSV: Ideal for tabular data, widely supported by spreadsheet applications and databases.
- JSON: Lightweight, easy to read and write, and natively supported by JavaScript, making it popular for web applications and APIs.
- XML: Highly flexible and self-describing, suitable for complex data structures and document-oriented data.

Common use cases:
- CSV: Data export/import, simple databases, spreadsheet data.
- JSON: API responses, configuration files, data storage for web applications.
- XML: Configuration files, data exchange in enterprise systems, storing complex hierarchical data.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import csv
import json
import xml.etree.ElementTree as ET
from typing import List, Dict, Any
import asyncio
import aiofiles

# CSV Handling
def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Read a CSV file and return its contents as a list of dictionaries.
    
    This function assumes the CSV file has a header row.
    """
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_csv(file_path: str, data: List[Dict[str, Any]]) -> None:
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
        writer.writerows(data)

# JSON Handling
def read_json(file_path: str) -> Any:
    """
    Read a JSON file and return its contents as a Python object.
    """
    with open(file_path, 'r') as jsonfile:
        return json.load(jsonfile)

def write_json(file_path: str, data: Any) -> None:
    """
    Write a Python object to a JSON file.
    """
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

# XML Handling
def read_xml(file_path: str) -> ET.Element:
    """
    Read an XML file and return its contents as an ElementTree object.
    """
    tree = ET.parse(file_path)
    return tree.getroot()

def write_xml(file_path: str, root: ET.Element) -> None:
    """
    Write an ElementTree object to an XML file.
    """
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='unicode', xml_declaration=True)

def demonstrate_basic_usage():
    """Demonstrate basic usage of CSV, JSON, and XML handling."""
    # CSV example
    csv_data = [
        {'name': 'Alice', 'age': '30', 'city': 'New York'},
        {'name': 'Bob', 'age': '25', 'city': 'San Francisco'},
        {'name': 'Charlie', 'age': '35', 'city': 'London'}
    ]
    write_csv('people.csv', csv_data)
    read_csv_data = read_csv('people.csv')
    print("CSV Data:", read_csv_data)

    # JSON example
    json_data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        'interests': ['programming', 'music', 'sports']
    }
    write_json('person.json', json_data)
    read_json_data = read_json('person.json')
    print("JSON Data:", read_json_data)

    # XML example
    root = ET.Element('person')
    ET.SubElement(root, 'name').text = 'Jane Smith'
    ET.SubElement(root, 'age').text = '28'
    ET.SubElement(root, 'city').text = 'Paris'
    write_xml('person.xml', root)
    read_xml_data = read_xml('person.xml')
    print("XML Data:", ET.tostring(read_xml_data, encoding='unicode'))

# Asynchronous file handling
async def read_csv_async(file_path: str) -> List[Dict[str, str]]:
    """
    Read a CSV file asynchronously and return its contents as a list of dictionaries.
    """
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        reader = csv.DictReader(content.splitlines())
        return list(reader)

async def write_csv_async(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Write a list of dictionaries to a CSV file asynchronously.
    """
    if not data:
        return

    fieldnames = data[0].keys()
    async with aiofiles.open(file_path, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        await file.write(','.join(fieldnames) + '\n')
        for row in data:
            await file.write(','.join(str(row[field]) for field in fieldnames) + '\n')

async def demonstrate_async_usage():
    """Demonstrate asynchronous usage of CSV handling."""
    csv_data = [
        {'name': 'Alice', 'age': '30', 'city': 'New York'},
        {'name': 'Bob', 'age': '25', 'city': 'San Francisco'},
        {'name': 'Charlie', 'age': '35', 'city': 'London'}
    ]
    await write_csv_async('async_people.csv', csv_data)
    read_csv_data = await read_csv_async('async_people.csv')
    print("Async CSV Data:", read_csv_data)

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use the 'with' statement for file operations to ensure proper resource management.
2. Handle exceptions properly, especially when dealing with file I/O and parsing errors.
3. Use appropriate encoding (e.g., UTF-8) when working with files containing non-ASCII characters.
4. Validate input data before writing to files to ensure data integrity.

Common Pitfalls:
1. Assuming the default encoding is suitable for all text files.
2. Not handling quoting and escaping properly in CSV files.
3. Ignoring namespace information in XML files.
4. Failing to handle large files efficiently, leading to memory issues.

Advanced Tips:
1. Use the csv.Sniffer class to detect CSV dialects automatically.
2. Leverage JSON schema validation for complex JSON structures.
3. Use XML namespaces correctly to avoid naming conflicts.
4. Implement streaming parsers for handling very large files.
"""

import csv
from json import JSONDecoder
from xml.etree.ElementTree import iterparse

def detect_csv_dialect(file_path: str) -> csv.Dialect:
    """
    Detect the dialect of a CSV file using csv.Sniffer.
    """
    with open(file_path, 'r', newline='') as csvfile:
        sample = csvfile.read(1024)
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
    return dialect

def stream_json_parse(file_path: str) -> List[Any]:
    """
    Parse a JSON file in a streaming fashion to handle large files.
    """
    results = []
    with open(file_path, 'r') as jsonfile:
        decoder = JSONDecoder()
        buffer = ''
        for chunk in iter(lambda: jsonfile.read(4096), ''):
            buffer += chunk
            while buffer:
                try:
                    result, index = decoder.raw_decode(buffer)
                    results.append(result)
                    buffer = buffer[index:]
                except ValueError:
                    break
    return results

def stream_xml_parse(file_path: str, target_element: str) -> List[Dict[str, str]]:
    """
    Parse an XML file in a streaming fashion, extracting specific elements.
    """
    results = []
    for event, elem in iterparse(file_path, events=('end',)):
        if elem.tag == target_element:
            results.append({child.tag: child.text for child in elem})
            elem.clear()
    return results

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques for handling CSV, JSON, and XML."""
    # CSV dialect detection
    dialect = detect_csv_dialect('people.csv')
    print(f"Detected CSV dialect: delimiter='{dialect.delimiter}', quotechar='{dialect.quotechar}'")

    # Streaming JSON parsing
    large_json = [{"id": i, "value": f"item_{i}"} for i in range(10000)]
    write_json('large.json', large_json)
    streamed_json = stream_json_parse('large.json')
    print(f"Streamed JSON parsing result (first 5 items): {streamed_json[:5]}")

    # Streaming XML parsing
    root = ET.Element('data')
    for i in range(10000):
        item = ET.SubElement(root, 'item')
        ET.SubElement(item, 'id').text = str(i)
        ET.SubElement(item, 'value').text = f"item_{i}"
    write_xml('large.xml', root)
    streamed_xml = stream_xml_parse('large.xml', 'item')
    print(f"Streamed XML parsing result (first 5 items): {streamed_xml[:5]}")

"""
4. Integration and Real-World Applications
------------------------------------------
CSV, JSON, and XML formats are extensively used in various domains:

1. Data Analysis: Pandas library for handling CSV and JSON in data science workflows.
2. Web Development: JSON for API responses and data exchange in web applications.
3. Configuration Management: XML and JSON for application and system configurations.
4. Data Integration: All three formats for data import/export between different systems.

Real-world example: A data processing pipeline
"""

import pandas as pd
from typing import Dict, List

def process_sales_data(csv_path: str, config_path: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    Process sales data from a CSV file based on configuration from a JSON file.
    
    This function demonstrates a real-world scenario of combining CSV and JSON processing.
    """
    # Read configuration
    config = read_json(config_path)
    
    # Read and process CSV data
    df = pd.read_csv(csv_path)
    
    # Apply filters from configuration
    for filter_config in config['filters']:
        column = filter_config['column']
        condition = filter_config['condition']
        value = filter_config['value']
        if condition == 'greater_than':
            df = df[df[column] > value]
        elif condition == 'less_than':
            df = df[df[column] < value]
        elif condition == 'equals':
            df = df[df[column] == value]
    
    # Group data as specified in configuration
    grouped = df.groupby(config['group_by'])
    
    # Prepare result
    result = {}
    for name, group in grouped:
        result[name] = group.to_dict('records')
    
    return result

def demonstrate_real_world_application():
    """Demonstrate a real-world application of CSV and JSON processing."""
    # Create sample CSV data
    sales_data = [
        {'date': '2023-01-01', 'product': 'A', 'quantity': 100, 'price': 10},
        {'date': '2023-01-02', 'product': 'B', 'quantity': 50, 'price': 20},
        {'date': '2023-01-03', 'product': 'A', 'quantity': 75, 'price': 10},
        {'date': '2023-01-04', 'product': 'C', 'quantity': 30, 'price': 15},
    ]
    write_csv('sales.csv', sales_data)
    
    # Create sample JSON configuration
    config = {
        'filters': [
            {'column': 'quantity', 'condition': 'greater_than', 'value': 40}
        ],
        'group_by': 'product'
    }
    write_json('config.json', config)
    
    # Process data
    result = process_sales_data('sales.csv', 'config.json')
    print("Processed sales data:", result)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Schema validation: Using JSON Schema or XML Schema for data validation.
2. Binary formats: Protocol Buffers and MessagePack as alternatives to JSON for performance-critical applications.
3. Streaming parsers: SAX for XML and ijson for JSON to handle very large files.
4. Data serialization: Libraries like pickle for Python-specific object serialization.
"""

import jsonschema
from xml.etree.ElementTree import XMLSchema
import proto

def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """
    Validate JSON data against a JSON Schema.
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False

def validate_xml_schema(xml_path: str, xsd_path: str) -> bool:
    """
    Validate an XML file against an XSD schema.
    """
    xmlschema = XMLSchema(file=xsd_path)
    return xmlschema.is_valid(xml_path)

# Define a Protocol Buffer message
class Person(proto.Message):
    name = proto.Field(proto.STRING, number=1)
    age = proto.Field(proto.INT32, number=2)
    email = proto.Field(proto.STRING, number=3)

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts in data handling."""
    # JSON Schema validation
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer", "minimum": 0},
            "email": {"type": "string", "format": "email"}
        },
        "required": ["name", "age", "email"]
    }
    valid_data = {"name": "John Doe", "age": 30, "email": "john@example.com"}
    invalid_data = {"name": "Jane Doe", "age": -5, "email": "not_an_email"}
    
    print(f"Valid JSON data: {validate_json_schema(valid_data, schema)}")
    print(f"Invalid JSON data: {validate_json_schema(invalid_data, schema)}")
    
    # Protocol Buffers
    person = Person(name="Alice", age=25, email="alice@example.com")
    serialized = person.SerializeToString()
    deserialized = Person()
    deserialized.ParseFromString(serialized)
    print(f"Protocol Buffer serialization and deserialization: {deserialized}")
    
    # XML Schema validation
    # Note: This requires creating sample XML and XSD files
    write_xml('person.xml', ET.fromstring('<person><name>Bob</name><age>40</age></person>'))
    with open('person.xsd', 'w') as xsd_file:
        xsd_file.write('''
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
          <xs:element name="person">
            <xs:complexType>
              <xs:sequence>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="age" type="xs:positiveInteger"/>
              </xs:sequence>
            </xs:complexType>
          </xs:element>
        </xs:schema>
        ''')
    print(f"XML Schema validation result: {validate_xml_schema('person.xml', 'person.xsd')}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I handle CSV files with different delimiters?
A: Use the `delimiter` parameter in csv.reader() or csv.writer(), or detect the dialect using csv.Sniffer.

Q: What's the best way to handle large JSON files that don't fit in memory?
A: Use a streaming JSON parser like ijson or implement a custom parser using json.JSONDecoder.

Q: How can I preserve the order of elements in a JSON object?
A: Use collections.OrderedDict when loading JSON data to maintain key order.

Troubleshooting:
1. UnicodeDecodeError when reading CSV: Specify the correct encoding (e.g., utf-8) when opening the file.
2. XML parsing errors: Ensure the XML is well-formed and consider using a more robust parser like lxml.
3. JSON decoding errors: Validate the JSON structure and handle potential formatting issues.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- pandas: Powerful data manipulation library with support for CSV, JSON, and more.
- lxml: Fast and feature-rich library for processing XML and HTML.
- jsonschema: JSON Schema validation for Python.
- protobuf: Google's data serialization format implementation for Python.

Resources:
- "Python for Data Analysis" by Wes McKinney
- "Mastering Object-oriented Python" by Steven F. Lott
- CSV format specification: https://tools.ietf.org/html/rfc4180
- JSON specification: https://www.json.org/json-en.html
- XML specification: https://www.w3.org/TR/xml/

8. Performance Analysis and Optimization
----------------------------------------
When working with CSV, JSON, and XML, performance can be critical, especially for large datasets.
"""

import time
import cProfile
import pstats
from io import StringIO

def benchmark_file_operations(file_path: str, num_iterations: int = 1000):
    """
    Benchmark different file reading methods for CSV, JSON, and XML.
    
    This function compares the performance of various file reading techniques.
    """
    def timed_operation(operation, *args):
        start_time = time.time()
        for _ in range(num_iterations):
            operation(*args)
        return time.time() - start_time

    # CSV benchmarking
    csv_time = timed_operation(read_csv, file_path + '.csv')
    print(f"CSV read time: {csv_time:.4f} seconds")

    # JSON benchmarking
    json_time = timed_operation(read_json, file_path + '.json')
    print(f"JSON read time: {json_time:.4f} seconds")

    # XML benchmarking
    xml_time = timed_operation(read_xml, file_path + '.xml')
    print(f"XML read time: {xml_time:.4f} seconds")

def profile_xml_parsing(file_path: str):
    """
    Profile XML parsing to identify performance bottlenecks.
    """
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Perform XML parsing
    root = read_xml(file_path)
    for elem in root.iter():
        # Simulate some processing
        elem.tag.upper()
    
    profiler.disable()
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

"""
Performance Considerations:
1. CSV parsing is generally faster than JSON or XML for simple, tabular data.
2. JSON parsing can be faster than XML for complex, nested structures.
3. Streaming parsers are crucial for handling very large files efficiently.

Optimization Strategies:
1. Use appropriate data types (e.g., pandas for large CSV files).
2. Implement caching for frequently accessed data.
3. Consider using more efficient serialization formats like Protocol Buffers for performance-critical applications.
4. Optimize XML parsing by using SAX or iterparse for large files.

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
- Relevance to the main topic of CSV, JSON, and XML handling in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to CSV, JSON, and XML handling.
    """
    print("1. Basic Usage:")
    demonstrate_basic_usage()

    print("\n2. Asynchronous Usage:")
    asyncio.run(demonstrate_async_usage())

    print("\n3. Advanced Techniques:")
    demonstrate_advanced_techniques()

    print("\n4. Real-World Application:")
    demonstrate_real_world_application()

    print("\n5. Advanced Concepts:")
    demonstrate_advanced_concepts()

    print("\n6. Performance Benchmarking:")
    # Create sample files for benchmarking
    sample_data = [{'id': i, 'value': f'item_{i}'} for i in range(1000)]
    write_csv('benchmark.csv', sample_data)
    write_json('benchmark.json', sample_data)
    root = ET.Element('data')
    for item in sample_data:
        elem = ET.SubElement(root, 'item')
        ET.SubElement(elem, 'id').text = str(item['id'])
        ET.SubElement(elem, 'value').text = item['value']
    write_xml('benchmark.xml', root)

    benchmark_file_operations('benchmark')

    print("\n7. XML Parsing Profiling:")
    profile_xml_parsing('benchmark.xml')

    # Clean up benchmark files
    import os
    for ext in ['csv', 'json', 'xml']:
        os.remove(f'benchmark.{ext}')

if __name__ == "__main__":
    main()