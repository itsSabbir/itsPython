#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Data Science and Visualization
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# In this section, we cover essential libraries commonly used in data science and visualization.
# These libraries provide powerful tools for data manipulation, analysis, and visualization.

# Importing necessary libraries
import numpy as np  # NumPy: A fundamental package for numerical computing in Python
# NumPy provides support for large multi-dimensional arrays and matrices, along with a collection 
# of mathematical functions to operate on these arrays. It's the backbone of scientific computing in Python.

import pandas as pd  # Pandas: A data analysis and manipulation library
# Pandas offers data structures like Series and DataFrames that allow for flexible data manipulation 
# and analysis, akin to working with spreadsheets or SQL tables. It's essential for data cleaning, 
# transformation, and exploratory data analysis.

import matplotlib.pyplot as plt  # Matplotlib: A plotting library for creating static, animated, and interactive visualizations
# Matplotlib provides a MATLAB-like interface for generating plots, histograms, bar charts, error charts, 
# scatter plots, etc. It's highly customizable and allows for extensive control over plot appearance.

import seaborn as sns  # Seaborn: A statistical data visualization library based on Matplotlib
# Seaborn simplifies the process of creating informative and attractive visualizations. 
# It integrates well with Pandas and provides a high-level interface for drawing attractive statistical graphics.

# Example 1: Using NumPy for numerical computations
# NumPy arrays are more efficient than Python lists for numerical operations.
arr = np.array([1, 2, 3, 4, 5])  # Creating a NumPy array
# NumPy supports element-wise operations, making it efficient for mathematical calculations.
print("NumPy Array:", arr)

# Example 2: Using Pandas for data manipulation
# Creating a simple DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)  # Constructing a DataFrame
print("Pandas DataFrame:\n", df)

# Example 3: Basic data analysis with Pandas
# Using the describe method to get a summary of the DataFrame
print("DataFrame Summary:\n", df.describe(include='all'))
# The describe method provides descriptive statistics, including count, mean, standard deviation, 
# and other metrics for numerical columns, as well as counts for categorical variables.

# Example 4: Visualization with Matplotlib
# Creating a simple line plot using Matplotlib
plt.plot(arr, label='Line Plot')  # Plotting the NumPy array
plt.title('Line Plot Example')  # Setting the title of the plot
plt.xlabel('X-axis')  # Labeling the X-axis
plt.ylabel('Y-axis')  # Labeling the Y-axis
plt.legend()  # Adding a legend
plt.show()  # Displaying the plot

# Example 5: Using Seaborn for enhanced visualizations
# Creating a bar plot with Seaborn
sns.barplot(x='Name', y='Age', data=df)  # Bar plot for age by name
plt.title('Bar Plot Example')  # Setting the title
plt.show()  # Displaying the plot

# Advanced tips:
# - Use NumPy arrays for efficient numerical operations when performance is critical.
# - When working with large datasets, consider using Pandas in conjunction with Dask or Vaex for out-of-core processing.
# - Leverage Seaborn's built-in themes to improve the aesthetics of your plots with a single command (sns.set_theme()).
# - Utilize Matplotlib's Object-Oriented interface for more complex visualizations, allowing for better customization and layout control.

# Potential pitfalls:
# - Be mindful of data types in Pandas; incorrect types can lead to unexpected results during operations.
# - When creating visualizations, ensure your data is clean and pre-processed to avoid misleading representations.
# - While Seaborn offers convenient plotting functions, always verify the underlying data, especially in aggregate plots.


#===============================================================================
# 1. NumPy
#===============================================================================

# NumPy is a powerful library in Python used for numerical computing. 
# It provides support for arrays, matrices, and many mathematical functions to operate on these data structures.

import numpy as np  # Import the NumPy library

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])  # Create a 1D array from a Python list
arr2 = np.arange(0, 10, 2)  # Create an array with values from 0 to 10, with a step of 2
# Result: [0, 2, 4, 6, 8]
arr3 = np.linspace(0, 1, 5)  # Create an array of 5 evenly spaced values between 0 and 1
# Result: [0., 0.25, 0.5, 0.75, 1.]

# Tip: Use np.zeros, np.ones, or np.empty for quick array initialization
zeros = np.zeros((3, 3))  # Create a 3x3 array filled with zeros
ones = np.ones((2, 2))  # Create a 2x2 array filled with ones
empty = np.empty((2, 3))  # Create a 2x3 array with uninitialized values (contents are unpredictable)

# Reshaping arrays
arr = np.arange(12)  # Create a 1D array with values from 0 to 11
reshaped = arr.reshape((3, 4))  # Reshape the array into a 3x4 matrix
# Result: [[ 0  1  2  3]
#          [ 4  5  6  7]
#          [ 8  9 10 11]]
# Tip: Use -1 to automatically calculate the size of one dimension
auto_reshaped = arr.reshape((3, -1))  # Reshape the array into 3 rows, automatically determine the number of columns

# Array operations
a = np.array([1, 2, 3])  # Define a 1D array a
b = np.array([4, 5, 6])  # Define another 1D array b
print(a + b)  # Element-wise addition, Result: [5 7 9]
print(a * b)  # Element-wise multiplication, Result: [4 10 18]
print(np.dot(a, b))  # Dot product, Result: 32 (1*4 + 2*5 + 3*6)

# Broadcasting
# Broadcasting allows NumPy to work with arrays of different shapes during arithmetic operations.
a = np.array([[1, 2, 3], [4, 5, 6]])  # Create a 2D array a
b = np.array([10, 20, 30])  # Create a 1D array b
print(a + b)  # b is broadcast to match a's shape, Result: [[11 22 33]
#                                                              [14 25 36]]

# Indexing and slicing
arr = np.arange(10)  # Create a 1D array with values from 0 to 9
print(arr[2:5])  # Slice the array to get elements from index 2 to 4, Result: [2 3 4]
print(arr[::2])  # Slice the array with a step of 2, Result: [0 2 4 6 8]
# Tip: Use negative step for reverse order
print(arr[::-1])  # Reverse the array, Result: [9 8 7 6 5 4 3 2 1 0]

# Boolean indexing
arr = np.arange(12).reshape((3, 4))  # Create a 3x4 array
bool_idx = arr > 5  # Create a boolean index where values are greater than 5
print(arr[bool_idx])  # Select elements that are greater than 5, Result: [ 6  7  8  9 10 11]

# Tip: Use np.where for conditional selection
result = np.where(arr % 2 == 0, arr, -1)  # Replace even elements with their value, odd with -1
# Result: [[-1  0 -1  2]
#          [-1  4 -1  6]
#          [-1  8 -1 10]]

# Statistical operations
arr = np.random.randn(5, 4)  # Create a 5x4 array with random numbers from a normal distribution
print(arr.mean())  # Calculate mean of all elements
print(arr.std())  # Calculate standard deviation of all elements
print(arr.var())  # Calculate variance of all elements
# Tip: Specify axis for row-wise or column-wise operations
print(arr.sum(axis=0))  # Column-wise sum
# Result: Sum of each column
print(arr.max(axis=1))  # Row-wise maximum
# Result: Maximum value in each row

# Linear algebra operations
a = np.array([[1, 2], [3, 4]])  # Define a 2D array a
b = np.array([[5, 6], [7, 8]])  # Define another 2D array b
print(np.dot(a, b))  # Matrix multiplication, Result: [[19 22]
#                                                             [43 50]]
print(np.linalg.inv(a))  # Calculate the inverse of a, Result: [[-2.   1. ]
#                                                                  [ 1.5 -0.5]]

print(np.linalg.eig(a))  # Calculate eigenvalues and eigenvectors of a, Result: (eigenvalues, eigenvectors)

# Tip: Use @ operator for matrix multiplication (Python 3.5+)
print(a @ b)  # Same as np.dot(a, b), Result: [[19 22]
#                                                 [43 50]]

# In summary, NumPy provides powerful tools for numerical computation.
# By mastering these techniques, you can perform efficient array manipulations, 
# statistical analysis, and linear algebra operations, significantly enhancing your data analysis capabilities.


#===============================================================================
# 2. Pandas
#===============================================================================

# Pandas is a powerful data manipulation and analysis library for Python. 
# It provides data structures like DataFrame and Series for handling structured data.
# Below are various operations and best practices for using Pandas effectively.

# Creating DataFrames
import pandas as pd  # Importing the pandas library for data manipulation
import numpy as np  # Importing numpy for numerical operations

# Creating a simple DataFrame from a dictionary.
# Each key corresponds to a column, and the values are lists representing rows.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df)

# Tip: Use pd.date_range for date indices.
# This creates a range of dates for use as an index, which is often helpful for time series data.
dates = pd.date_range('20230101', periods=6)  # Generate 6 dates starting from 2023-01-01
df_dates = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df_dates)

# Reading and writing data
# Pandas provides robust functions for reading and writing data to various file formats.

# Tip: Specify usecols to read only specific columns from CSV.
df_csv = pd.read_csv('file.csv', usecols=['A', 'B'])  # Read specific columns to save memory
df_excel = pd.read_excel('file.xlsx', sheet_name='Sheet1')  # Read from Excel file
# Writing DataFrames to files without including the index.
df.to_csv('output.csv', index=False)  # Save DataFrame to CSV
df.to_excel('output.xlsx', sheet_name='Sheet1')  # Save DataFrame to Excel

# Basic operations
# These methods are essential for understanding and exploring the data.

print(df.head())  # Displays the first 5 rows of the DataFrame.
print(df.tail())  # Displays the last 5 rows of the DataFrame.
print(df.info())  # Provides a summary of the DataFrame including data types and non-null counts.
print(df.describe())  # Returns statistical summary for numerical columns (count, mean, std, min, max).

# Selecting data
# Selecting specific rows and columns is crucial for data analysis.

print(df['A'])  # Selects and prints the entire 'A' column.
print(df[['A', 'B']])  # Selects and prints multiple columns.
print(df.loc[0])  # Selects a row by its label (index).
print(df.iloc[0])  # Selects a row by its integer index.
# Tip: Use .at and .iat for fast scalar value access.
print(df.at[0, 'A'])  # Access a single value by label (fast access).
print(df.iat[0, 0])  # Access a single value by integer position (fast access).

# Filtering
# Filtering data is essential to focus on specific subsets of your data.

print(df[df['A'] > 1])  # Selects rows where the 'A' column is greater than 1.
# Tip: Use the query method for cleaner string expressions.
print(df.query('A > 1 and B < 6'))  # Uses query to filter DataFrame using a string expression.

# Handling missing data
# Missing data can be managed through various methods in Pandas.

df_missing = df.copy()  # Create a copy of the original DataFrame to introduce missing values.
df_missing.loc[0, 'A'] = np.nan  # Introduce a NaN (missing value) in the 'A' column.
print(df_missing.dropna())  # Drops rows containing any NaN values.
print(df_missing.fillna(0))  # Fills NaN values with 0.
# Tip: Use different fill methods for flexibility.
print(df_missing.fillna(method='ffill'))  # Forward fill: replaces NaN with the last valid observation.

# Group operations
# Grouping data allows for aggregation based on categories.

df_grouped = df.groupby('A')  # Groups DataFrame by values in column 'A'.
print(df_grouped.mean())  # Calculates mean for each group.
# Tip: Use agg for multiple operations to provide more complex aggregations.
print(df_grouped.agg({'B': 'mean', 'C': ['min', 'max']}))  # Multiple aggregations on different columns.

# Merging and joining
# Combining DataFrames is a common operation in data analysis.

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})  # First DataFrame.
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})  # Second DataFrame.
print(pd.merge(df1, df2, on='key', how='outer'))  # Merges DataFrames on 'key' with an outer join.

# Pivot tables
# Pivot tables are useful for reorganizing data for analysis.

df_pivot = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],
                         'B': ['one', 'two', 'one', 'two'],
                         'C': [1, 2, 3, 4]})
print(df_pivot.pivot_table(values='C', index='A', columns='B', aggfunc='sum'))  # Creates a pivot table.

# Time series operations
# Time series analysis is a common use case for Pandas, especially for financial data.

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))  # Creates a time series.
print(ts.resample('M').mean())  # Resamples the time series to monthly frequency and calculates the mean.
print(ts.rolling(window=7).mean())  # Computes the 7-day rolling average for smoothing data.

#===============================================================================
# 3. Matplotlib
#===============================================================================

# Matplotlib is a powerful plotting library in Python used for creating static, animated, and interactive visualizations.
# Below are various examples demonstrating how to create different types of plots.

# Example 1: Basic line plot
import numpy as np
import matplotlib.pyplot as plt

# Create an array of 100 values linearly spaced between 0 and 10
x = np.linspace(0, 10, 100)
# Compute the sine of each value in x
y = np.sin(x)

# Create a new figure with a specified size
plt.figure(figsize=(10, 6))
# Plot y versus x as a line
plt.plot(x, y)
# Set the title and labels for the axes
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
# Add a grid for better readability
plt.grid(True)
# Tip: Use tight_layout to adjust subplot parameters for better fit
plt.tight_layout()
# Display the plot
plt.show()

# Example 2: Multiple plots
# Create a figure and a set of subplots in a 1x2 grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# Plot sine wave on the first subplot
ax1.plot(x, np.sin(x))
ax1.set_title('Sine')  # Set the title for the first subplot
# Plot cosine wave on the second subplot
ax2.plot(x, np.cos(x))
ax2.set_title('Cosine')  # Set the title for the second subplot
# Tip: Use suptitle for a figure-level title
fig.suptitle('Trigonometric Functions')
# Display the plot
plt.show()

# Example 3: Scatter plot
# Generate random x and y data points
x = np.random.rand(50)
y = np.random.rand(50)
# Generate random colors and sizes for the scatter points
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)  # Scale sizes for better visibility
# Create a scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)  # Alpha sets transparency
plt.colorbar()  # Add a color bar to indicate value scale
# Display the plot
plt.show()

# Example 4: Histogram
# Generate 1000 random data points from a normal distribution
data = np.random.randn(1000)
# Create a histogram with specified number of bins
plt.hist(data, bins=30, edgecolor='black')
# Tip: Use density=True to normalize the histogram to a probability density
plt.hist(data, bins=30, density=True, alpha=0.7)  # Alpha adjusts transparency
# Display the plot
plt.show()

# Example 5: Bar plot
# Define categories and corresponding values
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
# Create a vertical bar plot
plt.bar(categories, values)
# Tip: Use barh for horizontal bars
plt.barh(categories, values)  # Create horizontal bars
# Display the plot
plt.show()

# Example 6: Pie chart
# Define sizes and labels for the pie chart
sizes = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']
# Create a pie chart with percentage display
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# Tip: Use explode to emphasize a slice
explode = (0, 0.1, 0, 0)  # Slightly pull out the second slice
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
# Display the plot
plt.show()

# Example 7: 3D plot
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting capabilities

# Create a new figure for 3D plotting
fig = plt.figure()
# Add a 3D subplot to the figure
ax = fig.add_subplot(111, projection='3d')
# Generate random x, y, z data points for 3D scatter plot
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
# Create a 3D scatter plot
ax.scatter(x, y, z)
# Display the plot
plt.show()

# Example 8: Customization
# Change the plotting style to 'seaborn'
plt.style.use('seaborn')  
# Adjust the default font size for plots
plt.rcParams['font.size'] = 14  
# Tip: Use context manager for temporary style changes
with plt.style.context('dark_background'):
    plt.plot(x, y)  # Re-plot sine wave using the new style
    plt.show()  # Display the plot


#===============================================================================
# 4. Seaborn
#===============================================================================

# Seaborn is a powerful Python data visualization library built on top of Matplotlib.
# It provides a high-level interface for drawing attractive statistical graphics.
# In this section, we will explore various plotting techniques using Seaborn.

# Set style and color palette
# Seaborn allows customization of styles and color palettes for improved aesthetics.
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")  # Sets the background style of the plots to 'whitegrid'
sns.set_palette("deep")      # Defines the color palette to 'deep', which is suitable for qualitative data

# Scatter plot with regression line
# We load the 'tips' dataset that contains information about restaurant tips.
tips = sns.load_dataset("tips")  # Loads the tips dataset from Seaborn's in-built datasets

sns.regplot(x="total_bill", y="tip", data=tips)  # Creates a scatter plot with a regression line
plt.title("Scatter Plot of Total Bill vs. Tip")  # Adding a title for clarity
plt.show()  # Displays the plot

# Categorical plot
# Categorical plots are useful for visualizing the distribution of categorical data.
sns.catplot(x="day", y="total_bill", kind="box", data=tips)  # Box plot to show total bill distribution across days
plt.title("Box Plot of Total Bill by Day")  # Adding a title for clarity
plt.show()  # Displays the plot

# Distribution plot
# Distribution plots help visualize the distribution of a variable.
sns.distplot(tips['total_bill'], kde=True, rug=True)  # Density and rug plot for total bill
# Tip: Use histplot for more control over histograms, as distplot is being deprecated.
# The histplot function provides more options for customization of histograms.
sns.histplot(tips['total_bill'], kde=True)  # Creates a histogram with a density estimate
plt.title("Histogram of Total Bill with KDE")  # Adding a title for clarity
plt.show()  # Displays the plot

# Heatmap
# Heatmaps are useful for visualizing matrices or 2D data.
flights = sns.load_dataset("flights")  # Loads the flights dataset
# Pivot the data to get months as rows and years as columns, summarizing passenger counts
flights_pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")  # Creates a heatmap with annotations
plt.title("Heatmap of Passengers by Month and Year")  # Adding a title for clarity
plt.show()  # Displays the plot

# Pair plot
# Pair plots visualize pairwise relationships in a dataset.
iris = sns.load_dataset("iris")  # Loads the iris dataset
sns.pairplot(iris, hue="species")  # Creates a pair plot colored by species
plt.title("Pair Plot of Iris Dataset")  # Adding a title for clarity
plt.show()  # Displays the plot

# Violin plot
# Violin plots combine box plots and density plots for richer visualizations.
sns.violinplot(x="day", y="total_bill", data=tips)  # Shows the distribution of total bills across days
plt.title("Violin Plot of Total Bill by Day")  # Adding a title for clarity
plt.show()  # Displays the plot

# Joint plot
# Joint plots visualize the relationship between two variables, along with their marginal distributions.
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")  # Creates a hexbin joint plot
plt.title("Joint Plot of Total Bill vs. Tip")  # Adding a title for clarity
plt.show()  # Displays the plot

# FacetGrid for multi-plot grids
# FacetGrid allows for creating a grid of plots based on one or more categorical variables.
g = sns.FacetGrid(tips, col="time", row="smoker")  # Creates a grid based on 'time' and 'smoker' status
g.map(plt.scatter, "total_bill", "tip")  # Maps scatter plots onto the grid
plt.subplots_adjust(top=0.9)  # Adjusts the layout for better title visibility
g.fig.suptitle("FacetGrid of Total Bill vs. Tip by Time and Smoker Status")  # Adding a title for the grid
plt.show()  # Displays the plot

# In summary, Seaborn simplifies the process of creating informative and attractive visualizations.
# Leveraging its features can enhance the analysis and presentation of data significantly.
# Advanced tip: Always consider the context and audience for your visualizations, and customize accordingly for clarity.


#===============================================================================
# Tips and Tricks
#===============================================================================

# In this section, we provide tips and tricks for enhancing performance and usability 
# in data analysis and visualization using libraries such as NumPy, Pandas, and Matplotlib.

# 1. Use vectorized operations in NumPy and Pandas for better performance
# Vectorized operations leverage low-level optimizations and avoid the overhead of Python loops,
# leading to significant performance improvements, especially with large datasets.
# Bad: Using a for loop for element-wise operations
for i in range(len(df)):
    df['new_col'][i] = df['col1'][i] + df['col2'][i]  # Slower due to Python-level looping

# Good: Using vectorized operations directly on DataFrames
df['new_col'] = df['col1'] + df['col2']  # Much faster due to internal optimizations in Pandas

# 2. Use .loc for label-based indexing and .iloc for position-based indexing in Pandas
# .loc allows for accessing rows and columns using labels, which is more intuitive 
# when dealing with named indexes and columns.
# Example of label-based indexing:
df.loc['row_label', 'column_label']  # Accessing specific row and column by their labels

# .iloc is used for positional indexing, allowing access to rows and columns by integer index.
df.iloc[0, 1]  # Accessing the first row and second column (zero-based indexing)

# 3. Chaining methods in Pandas
# Chaining methods helps create a clean, readable syntax for data manipulation and analysis.
result = (df.groupby('category')  # Grouping data by 'category'
          .agg({'value': 'mean'})  # Aggregating values to compute the mean
          .sort_values('value', ascending=False)  # Sorting results by the mean value in descending order
          .reset_index())  # Resetting the index for a clean DataFrame output

# 4. Use query() for complex filtering in Pandas
# The query method allows for intuitive filtering using a string expression,
# enhancing code readability, especially for complex conditions.
df.query('(column1 > 5) & (column2 < 10) | (column3 == "value")')  # Filtering based on multiple conditions

# 5. Efficient memory usage with categories in Pandas
# Converting string columns with a limited number of unique values to the 'category' dtype
# can significantly reduce memory usage and improve performance in operations.
df['category_column'] = df['category_column'].astype('category')  # Optimizing memory usage

# 6. Use plt.subplots() for creating figure and axes objects in Matplotlib
# This approach allows for more flexibility in plotting, enabling customizations for multiple plots.
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Creating a new figure and a set of axes
ax.plot(x, y)  # Plotting data on the axes

# 7. Customize Seaborn plots with Matplotlib
# Seaborn works on top of Matplotlib, allowing for easy customization of plots.
import seaborn as sns

g = sns.regplot(x="total_bill", y="tip", data=tips)  # Creating a regression plot
g.set(xlabel="Total Bill ($)", ylabel="Tip ($)")  # Setting labels for axes
g.set_title("Relationship between Bill and Tip")  # Adding a title to the plot

# 8. Use sns.despine() to remove top and right spines in Seaborn plots
# This can enhance the aesthetic of plots by simplifying the visual representation.
sns.despine()  # Removes the top and right spines from the current plot

# 9. Efficient data reading in Pandas
# Using chunksize allows for processing large files in manageable segments,
# reducing memory usage and enabling efficient data handling.
for chunk in pd.read_csv('large_file.csv', chunksize=10000):  # Reading in chunks of 10,000 rows
    process(chunk)  # Process each chunk individually to avoid memory overload

# 10. Use context managers for temporary style changes in Matplotlib and Seaborn
# Context managers provide a way to temporarily apply styles or settings,
# ensuring that changes do not affect subsequent plots.
with sns.axes_style("darkgrid"):  # Setting a specific style temporarily
    plt.plot(x, y)  # Plotting within the context of the style

# 11. Utilize multiprocessing for parallel computations in NumPy
# Parallel computing can significantly speed up operations on large datasets.
from multiprocessing import Pool
import numpy as np

def parallel_operation(chunk):
    return np.sum(chunk)  # Sum the values in a chunk of data

# Splitting the array into chunks and processing them in parallel
with Pool() as p:  # Using a pool of worker processes
    result = p.map(parallel_operation, np.array_split(large_array, 4))  # Parallel execution

# 12. Use generators for memory-efficient data processing
# Generators yield items one at a time and only when requested, 
# making them ideal for handling large datasets without consuming excessive memory.
def data_generator(file_path):
    with open(file_path, 'r') as file:  # Opening the file
        for line in file:  # Iterating over each line in the file
            yield process_line(line)  # Yielding processed lines one by one

# Consuming the generator to analyze processed data
for processed_data in data_generator('large_file.txt'):  # Iterating over processed data
    analyze(processed_data)  # Analyzing each piece of data as it is generated

# In summary, these tips and tricks aim to optimize performance, enhance code clarity, 
# and ensure efficient data handling and visualization practices in Python.
