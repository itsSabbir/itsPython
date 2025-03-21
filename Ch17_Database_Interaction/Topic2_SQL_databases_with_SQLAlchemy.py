# Database Interaction - SQL databases with SQLAlchemy - in the Python Programming Language
# =========================================================================================

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

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
import time
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
import unittest
from sqlalchemy import event

# 1. Overview and Historical Context
# ----------------------------------
# SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
# It provides a full suite of well-known enterprise-level persistence patterns, designed for
# efficient and high-performing database access.

# Historical context:
# - SQLAlchemy was first released in 2006 by Mike Bayer.
# - It was designed to bridge the gap between database and application, providing a Pythonic
#   interface to relational databases.
# - Over the years, it has become the de facto standard for database interaction in Python.

# Significance:
# - SQLAlchemy provides both high-level ORM and low-level SQL expression language.
# - It supports a wide range of database backends, including PostgreSQL, MySQL, SQLite, and Oracle.
# - The library offers great flexibility, allowing developers to work at their preferred level of abstraction.

# Common use cases:
# - Building database-driven web applications
# - Data analysis and scientific computing
# - Enterprise application development
# - Microservices and distributed systems

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', user_id={self.user_id})>"

def create_database():
    """Create the database and tables."""
    engine = create_engine('sqlite:///example.db', echo=True)
    Base.metadata.create_all(engine)
    return engine

def insert_data(engine):
    """Insert sample data into the database."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create users
        user1 = User(name="Alice", email="alice@example.com")
        user2 = User(name="Bob", email="bob@example.com")
        session.add_all([user1, user2])
        session.flush()  # Flush to get the user IDs

        # Create posts
        post1 = Post(title="First Post", content="Hello, World!", user_id=user1.id)
        post2 = Post(title="Second Post", content="SQLAlchemy is great!", user_id=user2.id)
        session.add_all([post1, post2])

        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

def query_data(engine):
    """Perform various queries on the database."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Simple select query
        users = session.query(User).all()
        print("All users:", users)

        # Query with filter
        alice = session.query(User).filter_by(name="Alice").first()
        print("User Alice:", alice)

        # Join query
        posts_with_authors = session.query(Post, User).join(User).all()
        for post, user in posts_with_authors:
            print(f"Post '{post.title}' by {user.name}")

        # Aggregate query
        post_count = session.query(func.count(Post.id)).scalar()
        print(f"Total number of posts: {post_count}")

    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

@contextmanager
def session_scope(engine):
    """Provide a transactional scope around a series of operations."""
    session = sessionmaker(bind=engine)()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def demonstrate_best_practices(engine):
    """Demonstrate best practices for using SQLAlchemy."""

    # Use context manager for session handling
    with session_scope(engine) as session:
        new_user = User(name="Charlie", email="charlie@example.com")
        session.add(new_user)
        print("New user added:", new_user)

    # Demonstrate eager loading to avoid N+1 query problem
    with session_scope(engine) as session:
        users_with_posts = session.query(User).options(sqlalchemy.orm.joinedload(User.posts)).all()
        for user in users_with_posts:
            print(f"{user.name} has {len(user.posts)} posts")

def common_pitfalls(engine):
    """Demonstrate common pitfalls and how to avoid them."""

    with session_scope(engine) as session:
        # Pitfall: Using entities outside of session
        user = session.query(User).first()

    # This will raise an error because the session is closed
    try:
        print(user.posts)
    except SQLAlchemyError as e:
        print(f"Error accessing user.posts outside session: {e}")

    # Solution: Use joined loading or refresh the object in a new session
    with session_scope(engine) as session:
        user = session.query(User).options(sqlalchemy.orm.joinedload(User.posts)).first()
        print(f"User {user.name} has {len(user.posts)} posts")

# 4. Integration and Real-World Applications
# ------------------------------------------

class UserRepository:
    def __init__(self, session):
        self.session = session

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter_by(id=user_id).first()

    def update_user(self, user_id: int, name: str = None, email: str = None) -> User:
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            self.session.commit()
        return user

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

def demonstrate_repository_pattern(engine):
    """Demonstrate the use of the repository pattern with SQLAlchemy."""
    Session = sessionmaker(bind=engine)
    session = Session()

    user_repo = UserRepository(session)

    # Create a new user
    new_user = user_repo.create_user("David", "david@example.com")
    print("Created user:", new_user)

    # Update the user
    updated_user = user_repo.update_user(new_user.id, name="Dave")
    print("Updated user:", updated_user)

    # Delete the user
    deleted = user_repo.delete_user(new_user.id)
    print("User deleted:", deleted)

    session.close()

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_sqlalchemy_example():
    """Demonstrate asynchronous SQLAlchemy operations."""
    engine = create_async_engine("sqlite+aiosqlite:///example.db", echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        new_user = User(name="Eve", email="eve@example.com")
        session.add(new_user)
        await session.commit()

        result = await session.execute(select(User).where(User.name == "Eve"))
        eve = result.scalar_one()
        print("Async query result:", eve)

    await engine.dispose()

# 6. FAQs and Troubleshooting
# ---------------------------

def handle_sqlalchemy_errors(engine):
    """Demonstrate handling of common SQLAlchemy errors."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Attempt to insert a duplicate unique value
        duplicate_user = User(name="Alice", email="alice@example.com")
        session.add(duplicate_user)
        session.commit()
    except SQLAlchemyError as e:
        print(f"Integrity Error: {e}")
        session.rollback()

    try:
        # Attempt to query a non-existent table
        result = session.execute("SELECT * FROM non_existent_table")
        print(result.fetchall())
    except SQLAlchemyError as e:
        print(f"Operational Error: {e}")

    session.close()

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - Alembic: Database migration tool for SQLAlchemy
# - SQLAlchemy-Utils: Various utility functions for SQLAlchemy
# - Flask-SQLAlchemy: Flask extension that adds SQLAlchemy support to Flask

# Resources:
# - SQLAlchemy Documentation: https://docs.sqlalchemy.org/
# - "Essential SQLAlchemy" by Jason Myers and Rick Copeland
# - "SQLAlchemy: Database Access Using Python" by Packt Publishing
# - SQLAlchemy Tutorials on Real Python: https://realpython.com/tutorials/sqlalchemy/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_queries(engine):
    """Benchmark different query approaches."""
    Session = sessionmaker(bind=engine)
    session = Session()

    # Prepare test data
    for i in range(1000):
        user = User(name=f"User{i}", email=f"user{i}@example.com")
        session.add(user)
    session.commit()

    # Benchmark individual inserts
    start_time = time.time()
    for i in range(100):
        post = Post(title=f"Post{i}", content="Content", user_id=1)
        session.add(post)
        session.commit()
    individual_insert_time = time.time() - start_time
    print(f"Individual inserts time: {individual_insert_time:.4f} seconds")

    # Benchmark bulk insert
    start_time = time.time()
    posts = [Post(title=f"BulkPost{i}", content="Content", user_id=1) for i in range(100)]
    session.bulk_save_objects(posts)
    session.commit()
    bulk_insert_time = time.time() - start_time
    print(f"Bulk insert time: {bulk_insert_time:.4f} seconds")

    # Benchmark query without index
    start_time = time.time()
    result = session.query(User).filter(User.name.like("User5%")).all()
    query_without_index_time = time.time() - start_time
    print(f"Query without index time: {query_without_index_time:.4f} seconds")

    # Create index
    engine.execute("CREATE INDEX idx_users_name ON users (name)")

    # Benchmark query with index
    start_time = time.time()
    result = session.query(User).filter(User.name.like("User5%")).all()
    query_with_index_time = time.time() - start_time
    print(f"Query with index time: {query_with_index_time:.4f} seconds")

    session.close()

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
    # Create the database and insert sample data
    engine = create_database()
    insert_data(engine)

    print("\nQuerying data:")
    query_data(engine)

    print("\nDemonstrating best practices:")
    demonstrate_best_practices(engine)

    print("\nDemonstrating common pitfalls:")
    common_pitfalls(engine)

    print("\nDemonstrating repository pattern:")
    demonstrate_repository_pattern(engine)

    print("\nDemonstrating asynchronous SQLAlchemy:")
    asyncio.run(async_sqlalchemy_example())

    print("\nHandling SQLAlchemy errors:")
    handle_sqlalchemy_errors(engine)

    print("\nBenchmarking queries:")
    benchmark_queries(engine)

if __name__ == "__main__":
    main()