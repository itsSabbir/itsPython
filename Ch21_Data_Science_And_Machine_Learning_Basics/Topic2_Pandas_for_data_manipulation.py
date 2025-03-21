# Data Science and Machine Learning Basics - Pandas for data manipulation - in the Python Programming Language
# ===================================================================================================

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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Union
import time
import unittest
from io import StringIO

# 1. Overview and Historical Context
# ----------------------------------
# Pandas is a powerful open-source data manipulation and analysis library for Python.
# It provides high-performance, easy-to-use data structures and tools for working with
# structured data.

# Historical context:
# - Pandas was created by Wes McKinney in 2008 while working at AQR Capital Management.
# - The initial release (v0.1) was in December 2009.
# - Pandas became an integral part of the Python scientific computing stack alongside NumPy and Matplotlib.

# Significance:
# - Pandas simplifies the process of data cleaning, transformation, and analysis.
# - It provides data structures like DataFrame and Series that are well-suited for tabular data.
# - Pandas integrates well with other libraries in the Python data science ecosystem.

# Common use cases:
# - Data cleaning and preprocessing
# - Exploratory data analysis
# - Time series analysis
# - Merging and joining datasets
# - Data visualization (in conjunction with Matplotlib or Seaborn)

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def pandas_basics():
    """Demonstrate basic Pandas operations and data structures."""
    # Creating a DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    print("Basic DataFrame:")
    print(df)

    # Creating a Series
    ages = pd.Series([25, 30, 35, 28], name='Age')
    print("\nAge Series:")
    print(ages)

    # Basic operations
    print("\nBasic DataFrame operations:")
    print("Mean age:", df['Age'].mean())
    print("Oldest person:", df.loc[df['Age'].idxmax(), 'Name'])

    # Filtering
    print("\nPeople older than 30:")
    print(df[df['Age'] > 30])

    # Grouping and aggregation
    print("\nAverage age by city:")
    print(df.groupby('City')['Age'].mean())

def pandas_advanced():
    """Demonstrate advanced Pandas operations."""
    # Reading data from CSV
    csv_data = """
    Date,Open,High,Low,Close,Volume
    2023-05-01,150.5,152.0,149.5,151.0,1000000
    2023-05-02,151.2,153.5,150.8,152.5,1200000
    2023-05-03,152.8,154.0,152.0,153.5,1100000
    2023-05-04,153.2,155.5,152.5,154.8,1300000
    2023-05-05,155.0,156.5,154.2,156.0,1400000
    """
    df = pd.read_csv(StringIO(csv_data), parse_dates=['Date'])
    print("Stock price DataFrame:")
    print(df)

    # Time series operations
    df['Return'] = df['Close'].pct_change()
    print("\nDaily returns:")
    print(df['Return'])

    # Rolling window calculations
    df['MA5'] = df['Close'].rolling(window=5).mean()
    print("\n5-day moving average:")
    print(df['MA5'])

    # Resampling
    monthly_data = df.resample('M', on='Date').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })
    print("\nMonthly resampled data:")
    print(monthly_data)

def pandas_data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Demonstrate data cleaning techniques in Pandas.
    
    Args:
        df (pd.DataFrame): Input DataFrame
    
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    # Handling missing values
    df_cleaned = df.dropna()  # Remove rows with any missing values
    # or
    # df_cleaned = df.fillna(df.mean())  # Fill missing values with column mean

    # Removing duplicates
    df_cleaned = df_cleaned.drop_duplicates()

    # Handling outliers (example: removing values more than 3 std devs from mean)
    numeric_columns = df_cleaned.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        mean = df_cleaned[col].mean()
        std = df_cleaned[col].std()
        df_cleaned = df_cleaned[(df_cleaned[col] > mean - 3*std) & (df_cleaned[col] < mean + 3*std)]

    # Converting data types
    df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])
    df_cleaned['category_column'] = df_cleaned['category_column'].astype('category')

    return df_cleaned

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use vectorized operations instead of explicit loops for better performance.
# 2. Leverage Pandas' built-in methods for data manipulation and analysis.
# 3. Use appropriate data types (e.g., categories for categorical data) to optimize memory usage.
# 4. Chain operations using method chaining for cleaner and more readable code.
# 5. Use .loc and .iloc for explicit indexing to avoid SettingWithCopyWarning.

# Common Pitfalls:
# 1. Modifying a copy of a DataFrame instead of the original (SettingWithCopyWarning).
# 2. Inefficient use of memory when working with large datasets.
# 3. Ignoring data types, leading to unexpected behavior or performance issues.
# 4. Using .ix for indexing (deprecated since Pandas 0.20).
# 5. Forgetting to handle missing values appropriately.

def demonstrate_best_practices():
    """Demonstrate Pandas best practices and common pitfalls."""
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': range(1, 6),
        'B': range(10, 60, 10),
        'C': ['foo', 'bar', 'baz', 'qux', 'quux']
    })
    print("Original DataFrame:")
    print(df)

    # Best practice: Vectorized operations
    df['D'] = df['A'] * df['B']
    print("\nVectorized operation result:")
    print(df)

    # Best practice: Method chaining
    result = (df
              .groupby('C')
              .agg({'A': 'sum', 'B': 'mean'})
              .reset_index()
              .rename(columns={'A': 'Sum_A', 'B': 'Mean_B'}))
    print("\nMethod chaining result:")
    print(result)

    # Common pitfall: SettingWithCopyWarning
    # Incorrect way (may raise SettingWithCopyWarning):
    # df[df['A'] > 2]['E'] = [1, 2, 3]

    # Correct way:
    df.loc[df['A'] > 2, 'E'] = [1, 2, 3]
    print("\nCorrect way to set values:")
    print(df)

# Advanced Tips:
def advanced_pandas_tips():
    """Demonstrate advanced Pandas tips and techniques."""
    # 1. Using categorical data types
    df = pd.DataFrame({
        'id': range(1000000),
        'category': np.random.choice(['A', 'B', 'C', 'D'], 1000000)
    })
    df['category'] = df['category'].astype('category')
    print("Memory usage with categorical data:", df.memory_usage(deep=True).sum() / 1e6, "MB")

    # 2. Using applymap for element-wise operations
    df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
    df_formatted = df.applymap(lambda x: f"{x:.2f}")
    print("\nFormatted DataFrame:")
    print(df_formatted)

    # 3. MultiIndex for hierarchical indexing
    arrays = [
        ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
        ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
    ]
    df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
    print("\nMultiIndex DataFrame:")
    print(df)

    # 4. Using query for filtering
    df = pd.DataFrame({
        'A': range(1, 6),
        'B': range(10, 60, 10),
        'C': ['foo', 'bar', 'baz', 'qux', 'quux']
    })
    result = df.query("A > 2 and B < 50")
    print("\nFiltered DataFrame using query:")
    print(result)

# 4. Integration and Real-World Applications
# ------------------------------------------

def financial_analysis_example():
    """Demonstrate Pandas in financial analysis."""
    # Create sample stock data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')
    prices = np.random.randn(len(dates)).cumsum() + 100
    volumes = np.random.randint(1000000, 10000000, size=len(dates))
    df = pd.DataFrame({
        'Date': dates,
        'Price': prices,
        'Volume': volumes
    })
    df.set_index('Date', inplace=True)

    # Calculate daily returns
    df['Return'] = df['Price'].pct_change()

    # Calculate 20-day moving average
    df['MA20'] = df['Price'].rolling(window=20).mean()

    # Calculate trading signals
    df['Signal'] = np.where(df['Price'] > df['MA20'], 1, 0)

    # Calculate strategy returns
    df['Strategy_Return'] = df['Signal'].shift(1) * df['Return']

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Price'], label='Price')
    plt.plot(df.index, df['MA20'], label='20-day MA')
    plt.title('Stock Price and Moving Average')
    plt.legend()
    plt.show()

    print("Cumulative Strategy Return:", df['Strategy_Return'].cumsum().iloc[-1])

def machine_learning_example():
    """Demonstrate Pandas in a machine learning workflow."""
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report

    # Load sample dataset
    from sklearn.datasets import load_iris
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Split data into features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)

    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", accuracy)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def demonstrate_advanced_concepts():
    """Demonstrate advanced Pandas concepts and emerging trends."""
    # 1. Pandas Extension Arrays
    from pandas.api.extensions import register_extension_dtype, ExtensionArray, ExtensionDtype
    import json

    @register_extension_dtype
    class JSONDtype(ExtensionDtype):
        name = 'json'
        
        @classmethod
        def construct_array_type(cls):
            return JSONArray

    class JSONArray(ExtensionArray):
        def __init__(self, values):
            self._data = values
            self._dtype = JSONDtype()

        @classmethod
        def _from_sequence(cls, scalars, dtype=None, copy=False):
            return cls([json.loads(scalar) for scalar in scalars])

        def __getitem__(self, item):
            return self._data[item]

        def __len__(self):
            return len(self._data)

        @property
        def dtype(self):
            return self._dtype

        def isna(self):
            return pd.array([x is None for x in self._data])

        def take(self, indices, allow_fill=False, fill_value=None):
            taken = [self._data[i] for i in indices]
            return JSONArray(taken)

        def copy(self):
            return JSONArray(self._data.copy())

    # Using the custom JSONDtype
    df = pd.DataFrame({
        'id': range(3),
        'json_data': JSONArray([
            json.dumps({'a': 1, 'b': 2}),
            json.dumps({'c': 3, 'd': 4}),
            json.dumps({'e': 5, 'f': 6})
        ])
    })
    print("DataFrame with custom JSON dtype:")
    print(df)
    print(df.dtypes)

    # 2. Pandas Nullable Integer Dtype
    df = pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8]
    })
    df = df.astype('Int64')
    print("\nDataFrame with nullable integer dtype:")
    print(df)
    print(df.dtypes)

    # 3. Arrow-backed DataFrames (experimental)
    try:
        import pyarrow as pa
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        df_arrow = df.convert_dtypes(dtype_backend="pyarrow")
        print("\nArrow-backed DataFrame:")
        print(df_arrow)
        print(df_arrow.dtypes)
    except ImportError:
        print("\nPyArrow not installed. Skipping Arrow-backed DataFrame example.")

# 6. FAQs and Troubleshooting
# ---------------------------

def pandas_faqs():
    """Address common Pandas FAQs and provide troubleshooting tips."""
    print("Pandas FAQs and Troubleshooting:")
    
    # Q: How do I handle missing values in Pandas?
    print("\nQ: How do I handle missing values in Pandas?")
    print("A: Use methods like dropna(), fillna(), or interpolate():")
    df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
    print("Original DataFrame:")
    print(df)
    print("\nAfter dropping NaN values:")
    print(df.dropna())
    print("\nAfter filling NaN values with mean:")
    print(df.fillna(df.mean()))
    
    # Q: How do I merge two DataFrames?
    print("\nQ: How do I merge two DataFrames?")
    print("A: Use pd.merge() or DataFrame.merge():")
    df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
    df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    print("\nMerged DataFrame (inner join):")
    print(pd.merge(df1, df2, on='key'))
    
    # Q: How do I pivot a DataFrame?
    print("\nQ: How do I pivot a DataFrame?")
    print("A: Use pivot() or pivot_table():")
    df = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'variable': ['A', 'B', 'A', 'B'],
        'value': [1, 2, 3, 4]
    })
    print("Original DataFrame:")
    print(df)
    print("\nPivoted DataFrame:")
    print(df.pivot(index='date', columns='variable', values='value'))

def pandas_troubleshooting():
    """Provide troubleshooting tips for common Pandas issues."""
    print("Pandas Troubleshooting Tips:")
    
    # Issue: SettingWithCopyWarning
    print("\nIssue: SettingWithCopyWarning")
    print("Tip: Use .loc[] for setting values to avoid this warning:")
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("Original DataFrame:")
    print(df)
    print("\nCorrect way to set values:")
    df.loc[df['A'] > 1, 'B'] = 10
    print(df)
    
    # Issue: Memory usage with large DataFrames
    print("\nIssue: Memory usage with large DataFrames")
    print("Tip: Use appropriate dtypes and consider using chunks for large files:")
    df = pd.DataFrame({'A': np.random.randint(0, 100, 1000000)})
    print(f"Memory usage before optimization: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    df['A'] = df['A'].astype('int8')
    print(f"Memory usage after optimization: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    
    # Issue: Slow performance with apply()
    print("\nIssue: Slow performance with apply()")
    print("Tip: Use vectorized operations or numba for better performance:")
    df = pd.DataFrame({'A': range(1000000)})
    
    def slow_function(x):
        return x ** 2
    
    start = time.time()
    df['B'] = df['A'].apply(slow_function)
    print(f"Time with apply(): {time.time() - start:.4f} seconds")
    
    start = time.time()
    df['C'] = df['A'] ** 2
    print(f"Time with vectorized operation: {time.time() - start:.4f} seconds")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def pandas_resources():
    """Provide recommended tools, libraries, and resources for Pandas."""
    print("Recommended Tools, Libraries, and Resources for Pandas:")
    
    print("\nTools and Libraries:")
    print("1. NumPy: For numerical computing, often used alongside Pandas")
    print("2. Matplotlib and Seaborn: For data visualization")
    print("3. Scikit-learn: For machine learning tasks using Pandas DataFrames")
    print("4. Dask: For working with larger-than-memory datasets")
    print("5. Modin: For scaling Pandas workflows across multiple cores or machines")
    
    print("\nResources:")
    print("1. Pandas Official Documentation: https://pandas.pydata.org/docs/")
    print("2. 'Python for Data Analysis' by Wes McKinney (creator of Pandas)")
    print("3. 'Effective Pandas' by Matt Harrison")
    print("4. Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf")
    print("5. Real Python Pandas Tutorials: https://realpython.com/learning-paths/pandas-data-science/")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_pandas_operations(n: int = 1000000):
    """
    Benchmark various Pandas operations and compare with pure Python.
    
    Args:
        n (int): Number of rows in the DataFrame for benchmarking.
    """
    print(f"Benchmarking Pandas operations with {n} rows:")
    
    # Generate data
    df = pd.DataFrame({
        'A': np.random.rand(n),
        'B': np.random.rand(n),
        'C': np.random.choice(['X', 'Y', 'Z'], n)
    })
    
    # Benchmark groupby operation
    start_time = time.time()
    result = df.groupby('C')['A'].mean()
    pandas_time = time.time() - start_time
    
    start_time = time.time()
    py_result = {}
    for key, group in df.groupby('C'):
        py_result[key] = sum(group['A']) / len(group)
    python_time = time.time() - start_time
    
    print(f"\nGroupby operation:")
    print(f"Pandas time: {pandas_time:.6f} seconds")
    print(f"Python time: {python_time:.6f} seconds")
    print(f"Speedup: {python_time / pandas_time:.2f}x")
    
    # Benchmark merge operation
    df2 = pd.DataFrame({
        'C': np.random.choice(['X', 'Y', 'Z'], n // 10),
        'D': np.random.rand(n // 10)
    })
    
    start_time = time.time()
    result = pd.merge(df, df2, on='C')
    pandas_time = time.time() - start_time
    
    print(f"\nMerge operation:")
    print(f"Pandas time: {pandas_time:.6f} seconds")

def optimize_pandas_code():
    """Demonstrate optimization techniques for Pandas code."""
    print("Pandas Code Optimization Techniques:")
    
    # 1. Use vectorized operations
    print("\n1. Use vectorized operations:")
    df = pd.DataFrame({'A': range(1000000), 'B': range(1000000)})
    
    def slow_function(row):
        return row['A'] + row['B']
    
    start_time = time.time()
    df['C'] = df.apply(slow_function, axis=1)
    apply_time = time.time() - start_time
    
    start_time = time.time()
    df['D'] = df['A'] + df['B']
    vectorized_time = time.time() - start_time
    
    print(f"Apply time: {apply_time:.6f} seconds")
    print(f"Vectorized time: {vectorized_time:.6f} seconds")
    print(f"Speedup: {apply_time / vectorized_time:.2f}x")
    
    # 2. Use appropriate dtypes
    print("\n2. Use appropriate dtypes:")
    df = pd.DataFrame({'A': np.random.choice(['cat', 'dog', 'bird'], 1000000)})
    print(f"Memory usage before optimization: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    df['A'] = df['A'].astype('category')
    print(f"Memory usage after optimization: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    
    # 3. Use chained indexing carefully
    print("\n3. Use chained indexing carefully:")
    df = pd.DataFrame({'A': range(1000000), 'B': range(1000000)})
    
    start_time = time.time()
    df[df['A'] > 500000]['B'] = 0  # This creates a copy
    chained_time = time.time() - start_time
    
    start_time = time.time()
    df.loc[df['A'] > 500000, 'B'] = 0  # This modifies the original
    loc_time = time.time() - start_time
    
    print(f"Chained indexing time: {chained_time:.6f} seconds")
    print(f"Using .loc time: {loc_time:.6f} seconds")
    print(f"Speedup: {chained_time / loc_time:.2f}x")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    """Provide guidelines for contributing to this note sheet."""
    print("How to Contribute to this Pandas Note Sheet:")
    print("1. Fork the repository containing this file.")
    print("2. Make your changes or additions.")
    print("3. Ensure all code examples are correct and follow the established style.")
    print("4. Add comments explaining new concepts or functions.")
    print("5. Update the Table of Contents if necessary.")
    print("6. Submit a pull request with a clear description of your changes.")
    
    print("\nGuidelines for contributions:")
    print("- Maintain the current format and style.")
    print("- Provide working code examples for new concepts.")
    print("- Include performance considerations for new functions.")
    print("- Add relevant references or citations for advanced topics.")
    
    print("\nWhen adding new sections or expanding existing ones, consider the following:")
    print("- Relevance to the main topic of Pandas in data science and machine learning.")
    print("- Clarity and depth of explanations.")
    print("- Practical applicability of examples and tips.")
    print("- Up-to-date information on Pandas features and best practices.")

# Main function to demonstrate various concepts
def main():
    """
    Main function to demonstrate various concepts related to Pandas.
    """
    print("Pandas for Data Manipulation in Python")
    print("======================================")
    
    pandas_basics()
    pandas_advanced()
    
    # Create a sample DataFrame for data cleaning
    sample_df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, 20, 30, np.nan, 50],
        'C': ['foo', 'bar', 'baz', 'qux', 'foo'],
        'date_column': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    })
    cleaned_df = pandas_data_cleaning(sample_df)
    print("\nCleaned DataFrame:")
    print(cleaned_df)
    
    demonstrate_best_practices()
    advanced_pandas_tips()
    
    financial_analysis_example()
    machine_learning_example()
    
    demonstrate_advanced_concepts()
    
    pandas_faqs()
    pandas_troubleshooting()
    
    pandas_resources()
    
    benchmark_pandas_operations()
    optimize_pandas_code()
    
    how_to_contribute()

# Unit tests for Pandas functions
class TestPandasFunctions(unittest.TestCase):
    def test_pandas_basics(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': ['foo', 'bar', 'baz']
        })
        self.assertEqual(df.shape, (3, 3))
        self.assertEqual(df['A'].mean(), 2)
    
    def test_pandas_advanced(self):
        df = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=5),
            'Value': [1, 2, 3, 4, 5]
        })
        df.set_index('Date', inplace=True)
        resampled = df.resample('M').sum()
        self.assertEqual(resampled.shape[0], 1)
    
    def test_pandas_data_cleaning(self):
        df = pd.DataFrame({
            'A': [1, 2, np.nan, 4, 5],
            'B': [10, 20, 30, np.nan, 50],
            'C': ['foo', 'bar', 'baz', 'qux', 'foo'],
            'date_column': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
        })
        cleaned_df = pandas_data_cleaning(df)
        self.assertTrue(cleaned_df['date_column'].dtype == 'datetime64[ns]')
        self.assertEqual(cleaned_df.shape[0], 3)  # After removing rows with NaN values

if __name__ == "__main__":
    main()
    unittest.main(argv=[''], exit=False)