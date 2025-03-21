# Database Interaction - NoSQL databases (e.g., MongoDB with PyMongo) - in the Python Programming Language
# ======================================================================================================

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

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
from typing import List, Dict, Any, Optional
import time
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import unittest
from contextlib import contextmanager

# 1. Overview and Historical Context
# ----------------------------------
# NoSQL databases, like MongoDB, are non-relational databases designed for distributed data stores 
# with humongous data storage needs. PyMongo is the official MongoDB driver for Python.

# Historical context:
# - NoSQL concept emerged in the late 2000s to address limitations of relational databases for handling big data.
# - MongoDB was first released in 2009 by MongoDB Inc. (formerly 10gen).
# - PyMongo has been the official Python driver for MongoDB since its early days.

# Significance:
# - NoSQL databases offer flexibility in data models, horizontal scalability, and high performance.
# - MongoDB's document-oriented model allows for schema-less design and easy scalability.
# - PyMongo provides a Pythonic way to interact with MongoDB, making it accessible to Python developers.

# Common use cases:
# - Big Data and real-time analytics
# - Content Management Systems
# - Internet of Things (IoT) data storage
# - Mobile and Social Infrastructure
# - User Data Management

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def connect_to_mongodb():
    """Establish a connection to MongoDB."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['example_db']
    return db

def insert_document(db):
    """Insert a single document into a MongoDB collection."""
    users = db.users
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "created_at": datetime.datetime.utcnow()
    }
    result = users.insert_one(user_data)
    print(f"Inserted document ID: {result.inserted_id}")

def insert_multiple_documents(db):
    """Insert multiple documents into a MongoDB collection."""
    users = db.users
    user_data = [
        {"name": "Alice", "email": "alice@example.com", "age": 25},
        {"name": "Bob", "email": "bob@example.com", "age": 35},
        {"name": "Charlie", "email": "charlie@example.com", "age": 40}
    ]
    result = users.insert_many(user_data)
    print(f"Inserted document IDs: {result.inserted_ids}")

def query_documents(db):
    """Query documents from a MongoDB collection."""
    users = db.users
    
    # Find all users
    all_users = users.find()
    print("All users:")
    for user in all_users:
        print(user)

    # Find users with a specific condition
    young_users = users.find({"age": {"$lt": 30}})
    print("\nUsers younger than 30:")
    for user in young_users:
        print(user)

    # Find one specific user
    john = users.find_one({"name": "John Doe"})
    print("\nJohn Doe's details:", john)

def update_document(db):
    """Update a document in a MongoDB collection."""
    users = db.users
    result = users.update_one(
        {"name": "John Doe"},
        {"$set": {"age": 31, "updated_at": datetime.datetime.utcnow()}}
    )
    print(f"Modified {result.modified_count} document(s)")

def delete_document(db):
    """Delete a document from a MongoDB collection."""
    users = db.users
    result = users.delete_one({"name": "Charlie"})
    print(f"Deleted {result.deleted_count} document(s)")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

@contextmanager
def mongo_connection():
    """Context manager for MongoDB connections."""
    client = MongoClient('mongodb://localhost:27017/')
    try:
        yield client
    finally:
        client.close()

def demonstrate_best_practices():
    """Demonstrate best practices for using MongoDB with PyMongo."""
    with mongo_connection() as client:
        db = client['example_db']
        users = db.users

        # Use bulk operations for multiple inserts/updates
        bulk = users.initialize_unordered_bulk_op()
        for i in range(1000):
            bulk.insert({"name": f"User{i}", "score": i})
        result = bulk.execute()
        print(f"Bulk insert result: {result}")

        # Use projections to limit fields returned
        user = users.find_one({"name": "User500"}, projection={"name": 1, "score": 1, "_id": 0})
        print("User with limited fields:", user)

        # Use indexing for frequently queried fields
        users.create_index([("name", pymongo.ASCENDING)], background=True)
        print("Index created on 'name' field")

def common_pitfalls():
    """Demonstrate common pitfalls and how to avoid them."""
    with mongo_connection() as client:
        db = client['example_db']
        users = db.users

        # Pitfall: Not handling ObjectId correctly
        try:
            users.find_one({"_id": "507f1f77bcf86cd799439011"})  # This will fail
        except Exception as e:
            print(f"Error: {e}")
        
        # Correct way:
        user = users.find_one({"_id": ObjectId("507f1f77bcf86cd799439011")})
        print("User found:", user)

        # Pitfall: Not using $set in updates (overwrites entire document)
        users.update_one({"name": "User1"}, {"score": 1000})  # This will overwrite the entire document
        
        # Correct way:
        users.update_one({"name": "User1"}, {"$set": {"score": 1000}})
        print("User1 updated correctly")

# 4. Integration and Real-World Applications
# ------------------------------------------

class UserRepository:
    def __init__(self, db):
        self.collection = db.users

    def create_user(self, name: str, email: str, age: int) -> str:
        user = {
            "name": name,
            "email": email,
            "age": age,
            "created_at": datetime.datetime.utcnow()
        }
        result = self.collection.insert_one(user)
        return str(result.inserted_id)

    def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def update_user(self, user_id: str, update_data: Dict[str, Any]) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_user(self, user_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

def demonstrate_repository_pattern():
    """Demonstrate the use of the repository pattern with MongoDB."""
    with mongo_connection() as client:
        db = client['example_db']
        user_repo = UserRepository(db)

        # Create a new user
        user_id = user_repo.create_user("David", "david@example.com", 28)
        print(f"Created user with ID: {user_id}")

        # Get the user
        user = user_repo.get_user_by_id(user_id)
        print(f"Retrieved user: {user}")

        # Update the user
        updated = user_repo.update_user(user_id, {"age": 29})
        print(f"User updated: {updated}")

        # Delete the user
        deleted = user_repo.delete_user(user_id)
        print(f"User deleted: {deleted}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_mongodb_example():
    """Demonstrate asynchronous MongoDB operations using Motor."""
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client.example_db
    users = db.users

    # Insert a document
    result = await users.insert_one({"name": "Async User", "score": 100})
    print(f"Inserted document ID: {result.inserted_id}")

    # Find a document
    document = await users.find_one({"name": "Async User"})
    print(f"Found document: {document}")

    # Update a document
    result = await users.update_one({"name": "Async User"}, {"$set": {"score": 200}})
    print(f"Modified {result.modified_count} document(s)")

    # Delete a document
    result = await users.delete_one({"name": "Async User"})
    print(f"Deleted {result.deleted_count} document(s)")

# 6. FAQs and Troubleshooting
# ---------------------------

def handle_mongodb_errors():
    """Demonstrate handling of common MongoDB errors."""
    with mongo_connection() as client:
        db = client['example_db']
        users = db.users

        # Handling duplicate key error
        try:
            users.insert_one({"_id": "unique_id", "name": "Unique User"})
            users.insert_one({"_id": "unique_id", "name": "Duplicate User"})
        except pymongo.errors.DuplicateKeyError as e:
            print(f"Duplicate key error: {e}")

        # Handling connection errors
        try:
            invalid_client = MongoClient('mongodb://invalid_host:27017', serverSelectionTimeoutMS=2000)
            invalid_client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as e:
            print(f"Server selection error: {e}")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - MongoDB Compass: GUI for MongoDB
# - PyMODM: Object Document Mapper for MongoDB
# - MongoEngine: Object Document Mapper for MongoDB
# - Mongoengine-Goodjson: JSON serializer/deserializer for MongoEngine

# Resources:
# - MongoDB Documentation: https://docs.mongodb.com/
# - PyMongo Documentation: https://pymongo.readthedocs.io/
# - "MongoDB: The Definitive Guide" by Kristina Chodorow
# - "MongoDB in Action" by Kyle Banker

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_operations():
    """Benchmark different MongoDB operations."""
    with mongo_connection() as client:
        db = client['benchmark_db']
        collection = db.benchmark

        # Prepare test data
        test_data = [{"index": i, "data": "x" * 1000} for i in range(10000)]

        # Benchmark insert_many
        start_time = time.time()
        collection.insert_many(test_data)
        insert_time = time.time() - start_time
        print(f"Inserting 10,000 documents took {insert_time:.4f} seconds")

        # Benchmark find with and without index
        start_time = time.time()
        list(collection.find({"index": 5000}))
        find_without_index_time = time.time() - start_time
        print(f"Find without index took {find_without_index_time:.4f} seconds")

        collection.create_index([("index", pymongo.ASCENDING)])

        start_time = time.time()
        list(collection.find({"index": 5000}))
        find_with_index_time = time.time() - start_time
        print(f"Find with index took {find_with_index_time:.4f} seconds")

        # Benchmark update_many
        start_time = time.time()
        collection.update_many({}, {"$set": {"updated": True}})
        update_time = time.time() - start_time
        print(f"Updating 10,000 documents took {update_time:.4f} seconds")

        # Clean up
        collection.drop()

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
    db = connect_to_mongodb()
    
    print("Inserting a single document:")
    insert_document(db)

    print("\nInserting multiple documents:")
    insert_multiple_documents(db)

    print("\nQuerying documents:")
    query_documents(db)

    print("\nUpdating a document:")
    update_document(db)

    print("\nDeleting a document:")
    delete_document(db)

    print("\nDemonstrating best practices:")
    demonstrate_best_practices()

    print("\nDemonstrating common pitfalls:")
    common_pitfalls()

    print("\nDemonstrating repository pattern:")
    demonstrate_repository_pattern()

    print("\nDemonstrating asynchronous MongoDB operations:")
    asyncio.run(async_mongodb_example())

    print("\nHandling MongoDB errors:")
    handle_mongodb_errors()

    print("\nBenchmarking MongoDB operations:")
    benchmark_operations()

if __name__ == "__main__":
    main()