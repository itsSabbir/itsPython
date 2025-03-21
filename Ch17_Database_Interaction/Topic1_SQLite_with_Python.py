# Database Interaction - SQLite with Python - in the Python Programming Language
# ==============================================================================

# Table of Contents:
# 1. Overview and Historical Context
# 2. Syntax, Key Concepts, and Code Examples
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# 4. Integration and Real-World Applications
# 5. Advanced Concepts and Emerging Trends
# 6. FAQs and Troubleshooting
# 7. Recommended Tools, Libraries, and Resources
# 8. Performance Analysis and Optimization
# 9. How to Contribute

# Author: Sabbir Hossain

import sqlite3
import os
import time
from typing import List, Tuple, Any, Optional
import asyncio
import aiosqlite
import unittest
from contextlib import contextmanager

# 1. Overview and Historical Context
# ----------------------------------
# SQLite is a lightweight, serverless, and self-contained relational database engine.
# Python's built-in sqlite3 module provides a simple interface for interacting with SQLite databases.

# Historical context:
# - SQLite was first released in 2000 by D. Richard Hipp.
# - Python's sqlite3 module was added to the standard library in Python 2.5 (2006).
# - SQLite has become one of the most widely deployed database engines, used in various applications and mobile devices.

# Significance:
# - SQLite provides a simple, efficient way to store and retrieve structured data without the need for a separate database server.
# - It's ideal for embedded applications, prototypes, and small to medium-sized projects.
# - SQLite databases are stored as single files, making them easy to transfer and manage.

# Common use cases:
# - Local data storage for desktop and mobile applications
# - Temporary data storage for web applications
# - Testing and development environments
# - Data analysis and scientific computing

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def create_database():
    """Create a new SQLite database and table."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_data():
    """Insert data into the database."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Insert a single row
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                   ("Alice", "alice@example.com", 30))
    
    # Insert multiple rows
    users = [
        ("Bob", "bob@example.com", 25),
        ("Charlie", "charlie@example.com", 35),
    ]
    cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users)
    
    conn.commit()
    conn.close()

def query_data():
    """Query data from the database."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Simple select query
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    print("All users:", all_users)
    
    # Query with a WHERE clause
    cursor.execute("SELECT name, age FROM users WHERE age > ?", (30,))
    older_users = cursor.fetchall()
    print("Users older than 30:", older_users)
    
    conn.close()

def update_data():
    """Update data in the database."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
    conn.commit()
    
    print("Rows affected:", cursor.rowcount)
    
    conn.close()

def delete_data():
    """Delete data from the database."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users WHERE name = ?", ("Charlie",))
    conn.commit()
    
    print("Rows deleted:", cursor.rowcount)
    
    conn.close()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

@contextmanager
def get_db_connection():
    """Context manager for database connections."""
    conn = sqlite3.connect('example.db')
    try:
        yield conn
    finally:
        conn.close()

def use_context_manager():
    """Demonstrate the use of a context manager for database connections."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print("Users fetched using context manager:", users)

def parameterized_queries():
    """Demonstrate the use of parameterized queries to prevent SQL injection."""
    user_input = "Alice'; DROP TABLE users; --"
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Bad practice (vulnerable to SQL injection):
        # cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
        
        # Good practice (using parameterized query):
        cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
        result = cursor.fetchall()
        print("Result of parameterized query:", result)

def transaction_management():
    """Demonstrate proper transaction management."""
    with get_db_connection() as conn:
        try:
            conn.execute("BEGIN TRANSACTION")
            conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                         ("David", "david@example.com", 40))
            conn.execute("UPDATE users SET age = ? WHERE name = ?", (32, "Alice"))
            conn.commit()
            print("Transaction committed successfully")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"An error occurred, transaction rolled back: {e}")

# 4. Integration and Real-World Applications
# ------------------------------------------

class UserDatabase:
    def __init__(self, db_name: str):
        self.db_name = db_name
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
        finally:
            conn.close()
    
    def create_user(self, name: str, email: str, age: int) -> int:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                           (name, email, age))
            conn.commit()
            return cursor.lastrowid
    
    def get_user(self, user_id: int) -> Optional[Tuple[int, str, str, int]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return cursor.fetchone()
    
    def update_user(self, user_id: int, name: str, email: str, age: int) -> bool:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?",
                           (name, email, age, user_id))
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_user(self, user_id: int) -> bool:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0

def demonstrate_user_database():
    """Demonstrate the use of the UserDatabase class."""
    db = UserDatabase('example.db')
    
    # Create a new user
    new_user_id = db.create_user("Eve", "eve@example.com", 28)
    print(f"Created new user with ID: {new_user_id}")
    
    # Retrieve the user
    user = db.get_user(new_user_id)
    print(f"Retrieved user: {user}")
    
    # Update the user
    updated = db.update_user(new_user_id, "Eve Smith", "eve.smith@example.com", 29)
    print(f"User updated: {updated}")
    
    # Delete the user
    deleted = db.delete_user(new_user_id)
    print(f"User deleted: {deleted}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_query(query: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
    """Execute an asynchronous SQLite query."""
    async with aiosqlite.connect('example.db') as db:
        async with db.execute(query, params) as cursor:
            return await cursor.fetchall()

async def demonstrate_async_sqlite():
    """Demonstrate asynchronous SQLite operations."""
    results = await async_query("SELECT * FROM users WHERE age > ?", (30,))
    print("Async query results:", results)

def full_text_search():
    """Demonstrate SQLite's full-text search capabilities."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Enable full-text search
    cursor.execute("CREATE VIRTUAL TABLE IF NOT EXISTS users_fts USING fts5(name, email)")
    
    # Insert sample data
    cursor.executemany("INSERT INTO users_fts (name, email) VALUES (?, ?)",
                       [("John Doe", "john@example.com"),
                        ("Jane Smith", "jane@example.com")])
    
    # Perform a full-text search
    cursor.execute("SELECT * FROM users_fts WHERE users_fts MATCH ?", ("john",))
    results = cursor.fetchall()
    print("Full-text search results:", results)
    
    conn.close()

# 6. FAQs and Troubleshooting
# ---------------------------

def handle_sqlite_errors():
    """Demonstrate handling of common SQLite errors."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        # Attempt to insert a duplicate unique value
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                       ("Alice", "alice@example.com", 30))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    
    try:
        # Attempt to query a non-existent table
        cursor.execute("SELECT * FROM non_existent_table")
    except sqlite3.OperationalError as e:
        print(f"Operational Error: {e}")
    
    conn.close()

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - SQLite Browser: GUI tool for working with SQLite databases
# - aiosqlite: Asynchronous SQLite library for Python
# - SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library

# Resources:
# - SQLite Documentation: https://www.sqlite.org/docs.html
# - Python sqlite3 module documentation: https://docs.python.org/3/library/sqlite3.html
# - "SQLite Database System: Design and Implementation" by Sibsankar Haldar
# - "Using SQLite" by Jay A. Kreibich

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_queries():
    """Benchmark different query approaches."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Prepare test data
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value TEXT)")
    cursor.executemany("INSERT INTO test (value) VALUES (?)",
                       [(f"value{i}",) for i in range(10000)])
    conn.commit()
    
    # Benchmark individual inserts
    start_time = time.time()
    for i in range(1000):
        cursor.execute("INSERT INTO test (value) VALUES (?)", (f"benchmark{i}",))
    conn.commit()
    individual_insert_time = time.time() - start_time
    print(f"Individual inserts time: {individual_insert_time:.4f} seconds")
    
    # Benchmark bulk insert
    start_time = time.time()
    cursor.executemany("INSERT INTO test (value) VALUES (?)",
                       [(f"benchmark{i}",) for i in range(1000)])
    conn.commit()
    bulk_insert_time = time.time() - start_time
    print(f"Bulk insert time: {bulk_insert_time:.4f} seconds")
    
    # Benchmark query without index
    start_time = time.time()
    cursor.execute("SELECT * FROM test WHERE value LIKE 'value5%'")
    cursor.fetchall()
    query_without_index_time = time.time() - start_time
    print(f"Query without index time: {query_without_index_time:.4f} seconds")
    
    # Create index
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_test_value ON test (value)")
    conn.commit()
    
    # Benchmark query with index
    start_time = time.time()
    cursor.execute("SELECT * FROM test WHERE value LIKE 'value5%'")
    cursor.fetchall()
    query_with_index_time = time.time() - start_time
    print(f"Query with index time: {query_with_index_time:.4f} seconds")
    
    conn.close()

# 9. How to Contribute
# --------------------
# To contribute to this note sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes or additions.
# 3. Ensure all code examples are correct and follow the established style.
# 4. Add comments explaining new concepts or functions.
# 5. Update the Table of Contents if necessary.
# 6. Submit a pull request with a clear description of your changes.

# Guidelines for contributions:
# - Maintain the current format and style.
# - Provide working code examples for new concepts.
# - Include performance considerations for new functions.
# - Add relevant references or citations for advanced topics.

def main():
    # Ensure the database file doesn't exist before running the examples
    if os.path.exists('example.db'):
        os.remove('example.db')

    print("Creating database and table...")
    create_database()

    print("\nInserting data...")
    insert_data()

    print("\nQuerying data...")
    query_data()

    print("\nUpdating data...")
    update_data()

    print("\nDeleting data...")
    delete_data()

    print("\nDemonstrating context manager...")
    use_context_manager()

    print("\nDemonstrating parameterized queries...")
    parameterized_queries()

    print("\nDemonstrating transaction management...")
    transaction_management()

    print("\nDemonstrating UserDatabase class...")
    demonstrate_user_database()

    print("\nDemonstrating asynchronous SQLite operations...")
    asyncio.run(demonstrate_async_sqlite())

    print("\nDemonstrating full-text search...")
    full_text_search()

    print("\nDemonstrating error handling...")
    handle_sqlite_errors()

    print("\nBenchmarking queries...")
    benchmark_queries()

if __name__ == "__main__":
    main()