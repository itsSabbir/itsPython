# Python Cheat Sheet: Data Science and Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. NumPy

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
arr3 = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]

# Tip: Use np.zeros, np.ones, or np.empty for quick array initialization
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
empty = np.empty((2, 3))  # Uninitialized

# Reshaping arrays
arr = np.arange(12)
reshaped = arr.reshape((3, 4))
# Tip: Use -1 to automatically calculate the size of one dimension
auto_reshaped = arr.reshape((3, -1))

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication
print(np.dot(a, b))  # Dot product

# Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)  # b is broadcast to match a's shape

# Indexing and slicing
arr = np.arange(10)
print(arr[2:5])  # [2, 3, 4]
print(arr[::2])  # [0, 2, 4, 6, 8]
# Tip: Use negative step for reverse order
print(arr[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Boolean indexing
arr = np.arange(12).reshape((3, 4))
bool_idx = arr > 5
print(arr[bool_idx])  # [6, 7, 8, 9, 10, 11]

# Tip: Use np.where for conditional selection
result = np.where(arr % 2 == 0, arr, -1)

# Statistical operations
arr = np.random.randn(5, 4)
print(arr.mean())
print(arr.std())
print(arr.var())
# Tip: Specify axis for row-wise or column-wise operations
print(arr.sum(axis=0))  # Column-wise sum
print(arr.max(axis=1))  # Row-wise maximum

# Linear algebra operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
print(np.linalg.inv(a))  # Inverse
print(np.linalg.eig(a))  # Eigenvalues and eigenvectors

# Tip: Use @  operator for matrix multiplication (Python 3.5+)
print(a @ b)

# 2. Pandas

# Creating DataFrames
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# Tip: Use pd.date_range for date indices
dates = pd.date_range('20230101', periods=6)
df_dates = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# Reading and writing data
# Tip: Specify usecols to read only specific columns
df_csv = pd.read_csv('file.csv', usecols=['A', 'B'])
df_excel = pd.read_excel('file.xlsx', sheet_name='Sheet1')
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', sheet_name='Sheet1')

# Basic operations
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.info())  # Summary of DataFrame
print(df.describe())  # Statistical summary

# Selecting data
print(df['A'])  # Select column
print(df[['A', 'B']])  # Select multiple columns
print(df.loc[0])  # Select row by label
print(df.iloc[0])  # Select row by integer index
# Tip: Use .at and .iat for fast scalar value access
print(df.at[0, 'A'])
print(df.iat[0, 0])

# Filtering
print(df[df['A'] > 1])
# Tip: Use query method for string expressions
print(df.query('A > 1 and B < 6'))

# Handling missing data
df_missing = df.copy()
df_missing.loc[0, 'A'] = np.nan
print(df_missing.dropna())  # Drop rows with NaN
print(df_missing.fillna(0))  # Fill NaN with 0
# Tip: Use different fill methods
print(df_missing.fillna(method='ffill'))  # Forward fill

# Group operations
df_grouped = df.groupby('A')
print(df_grouped.mean())
# Tip: Use agg for multiple operations
print(df_grouped.agg({'B': 'mean', 'C': ['min', 'max']}))

# Merging and joining
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
print(pd.merge(df1, df2, on='key', how='outer'))

# Pivot tables
df_pivot = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],
                         'B': ['one', 'two', 'one', 'two'],
                         'C': [1, 2, 3, 4]})
print(df_pivot.pivot_table(values='C', index='A', columns='B', aggfunc='sum'))

# Time series operations
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(ts.resample('M').mean())  # Monthly resampling
print(ts.rolling(window=7).mean())  # 7-day rolling average

# 3. Matplotlib

# Basic line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
# Tip: Use tight_layout to adjust subplot params
plt.tight_layout()
plt.show()

# Multiple plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, np.sin(x))
ax1.set_title('Sine')
ax2.plot(x, np.cos(x))
ax2.set_title('Cosine')
# Tip: Use suptitle for a figure-level title
fig.suptitle('Trigonometric Functions')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.colorbar()
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
# Tip: Use density=True for probability density
plt.hist(data, bins=30, density=True, alpha=0.7)
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
plt.bar(categories, values)
# Tip: Use barh for horizontal bars
plt.barh(categories, values)
plt.show()

# Pie chart
sizes = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# Tip: Use explode to emphasize a slice
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()

# 3D plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
ax.scatter(x, y, z)
plt.show()

# Customization
plt.style.use('seaborn')  # Change style
plt.rcParams['font.size'] = 14  # Change default font size
# Tip: Use context manager for temporary style changes
with plt.style.context('dark_background'):
    plt.plot(x, y)
    plt.show()

# 4. Seaborn

# Set style and color palette
sns.set_style("whitegrid")
sns.set_palette("deep")

# Scatter plot with regression line
tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()

# Categorical plot
sns.catplot(x="day", y="total_bill", kind="box", data=tips)
plt.show()

# Distribution plot
sns.distplot(tips['total_bill'], kde=True, rug=True)
# Tip: Use histplot for more control over histograms
sns.histplot(tips['total_bill'], kde=True)
plt.show()

# Heatmap
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.show()

# Pair plot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()

# Violin plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

# Joint plot
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plt.show()

# FacetGrid for multi-plot grids
g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(plt.scatter, "total_bill", "tip")
plt.show()

# Tips and Tricks

# 1. Use vectorized operations in NumPy and Pandas for better performance
# Bad: for loop
# Good: df['new_col'] = df['col1'] + df['col2']

# 2. Use .loc for label-based indexing and .iloc for position-based indexing in Pandas
# df.loc['row_label', 'column_label']
# df.iloc[0, 1]

# 3. Chainning methods in Pandas
result = (df.groupby('category')
          .agg({'value': 'mean'})
          .sort_values('value', ascending=False)
          .reset_index())

# 4. Use query() for complex filtering in Pandas
df.query('(column1 > 5) & (column2 < 10) | (column3 == "value")')

# 5. Efficient memory usage with categories in Pandas
df['category_column'] = df['category_column'].astype('category')

# 6. Use plt.subplots() for creating figure and axes objects in Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)

# 7. Customize Seaborn plots with Matplotlib
g = sns.regplot(x="total_bill", y="tip", data=tips)
g.set(xlabel="Total Bill ($)", ylabel="Tip ($)")
g.set_title("Relationship between Bill and Tip")

# 8. Use sns.despine() to remove top and right spines in Seaborn plots
sns.despine()

# 9. Efficient data reading in Pandas
# Use chunksize for large files
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)

# 10. Use context managers for temporary style changes in Matplotlib and Seaborn
with sns.axes_style("darkgrid"):
    plt.plot(x, y)

# 11. Utilize multiprocessing for parallel computations in NumPy
from multiprocessing import Pool

def parallel_operation(chunk):
    return np.sum(chunk)

with Pool() as p:
    result = p.map(parallel_operation, np.array_split(large_array, 4))

# 12. Use generators for memory-efficient data processing
def data_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield process_line(line)

for processed_data in data_generator('large_file.txt'):
    analyze(processed_data)