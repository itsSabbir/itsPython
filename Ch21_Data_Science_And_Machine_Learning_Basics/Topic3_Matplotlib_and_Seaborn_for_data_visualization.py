# Data Science and Machine Learning Basics - Matplotlib and Seaborn for data visualization - in the Python Programming Language
# =====================================================================================================

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

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Union
import time
import unittest

# 1. Overview and Historical Context
# ----------------------------------
# Matplotlib and Seaborn are powerful libraries for data visualization in Python.
# Matplotlib provides a MATLAB-like plotting interface, while Seaborn offers a
# high-level interface for creating statistical graphics.

# Historical context:
# - Matplotlib was created by John D. Hunter in 2003 as a MATLAB-like plotting interface for Python.
# - Seaborn was developed by Michael Waskom in 2012 as a statistical visualization library built on top of Matplotlib.

# Significance:
# - Matplotlib is the foundation for many Python plotting libraries and provides fine-grained control over plot elements.
# - Seaborn simplifies the creation of complex statistical visualizations and offers aesthetically pleasing default styles.

# Common use cases:
# - Creating publication-quality figures for scientific papers and presentations
# - Exploratory data analysis in data science and machine learning workflows
# - Visualizing results of statistical analyses and machine learning models
# - Creating interactive visualizations for web applications and dashboards

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def matplotlib_basics():
    """Demonstrate basic Matplotlib operations."""
    # Create a simple line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)')
    plt.title('Simple Line Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Create a scatter plot
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
    plt.title('Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.show()

    # Create a bar plot
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [3, 7, 2, 5, 8]
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values)
    plt.title('Bar Plot')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.show()

def seaborn_basics():
    """Demonstrate basic Seaborn operations."""
    # Set the Seaborn style
    sns.set_style("whitegrid")

    # Create a simple line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x, y=y)
    plt.title('Seaborn Line Plot')
    plt.show()

    # Create a scatter plot
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="total_bill", y="tip", hue="time", size="size", data=tips)
    plt.title('Seaborn Scatter Plot')
    plt.show()

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x="day", y="total_bill", data=tips)
    plt.title('Seaborn Bar Plot')
    plt.show()

def advanced_visualization():
    """Demonstrate advanced visualization techniques."""
    # Create a complex multi-panel figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Advanced Multi-Panel Visualization', fontsize=16)

    # Panel 1: Histogram with KDE
    data = np.random.normal(0, 1, 1000)
    sns.histplot(data, kde=True, ax=axes[0, 0])
    axes[0, 0].set_title('Histogram with KDE')

    # Panel 2: Box plot
    tips = sns.load_dataset("tips")
    sns.boxplot(x="day", y="total_bill", data=tips, ax=axes[0, 1])
    axes[0, 1].set_title('Box Plot')

    # Panel 3: Heatmap
    corr = tips.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1, 0])
    axes[1, 0].set_title('Correlation Heatmap')

    # Panel 4: Violin plot
    sns.violinplot(x="day", y="total_bill", data=tips, ax=axes[1, 1])
    axes[1, 1].set_title('Violin Plot')

    plt.tight_layout()
    plt.show()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use appropriate plot types for your data and message.
# 2. Label axes, add titles, and include legends when necessary.
# 3. Choose color schemes that are accessible to color-blind individuals.
# 4. Use consistent styling across related visualizations.
# 5. Optimize figure size and resolution for the intended display medium.

# Common Pitfalls:
# 1. Overcomplicating visualizations with unnecessary elements.
# 2. Using inappropriate scales or ranges that distort data representation.
# 3. Neglecting to handle missing or invalid data in visualizations.
# 4. Creating misleading visualizations through poor design choices.
# 5. Ignoring the limitations of certain plot types for specific data distributions.

def demonstrate_best_practices():
    """Demonstrate best practices in data visualization."""
    # Create a sample dataset
    np.random.seed(0)
    data = pd.DataFrame({
        'Group': np.repeat(['A', 'B', 'C', 'D'], 50),
        'Value': np.random.normal(10, 2, 200),
        'Category': np.random.choice(['X', 'Y', 'Z'], 200)
    })

    # Create a figure with multiple subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Best Practices in Data Visualization', fontsize=16)

    # Left subplot: Box plot with swarm plot overlay
    sns.boxplot(x='Group', y='Value', data=data, ax=ax1)
    sns.swarmplot(x='Group', y='Value', data=data, color=".25", size=3, ax=ax1)
    ax1.set_title('Distribution of Values by Group')
    ax1.set_xlabel('Group')
    ax1.set_ylabel('Value')

    # Right subplot: Grouped bar plot
    sns.barplot(x='Group', y='Value', hue='Category', data=data, ax=ax2)
    ax2.set_title('Average Values by Group and Category')
    ax2.set_xlabel('Group')
    ax2.set_ylabel('Average Value')
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

# Advanced Tips:
def custom_style():
    """Demonstrate creating and using a custom style."""
    # Define a custom style
    custom_style = {
        'axes.facecolor': '#F0F0F0',
        'axes.edgecolor': '#333333',
        'axes.labelcolor': '#333333',
        'text.color': '#333333',
        'xtick.color': '#333333',
        'ytick.color': '#333333',
        'grid.color': '#FFFFFF',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.family': 'sans-serif'
    }

    # Use the custom style
    with plt.style.context(custom_style):
        plt.figure(figsize=(10, 6))
        x = np.linspace(0, 10, 100)
        plt.plot(x, np.sin(x), label='sin(x)')
        plt.plot(x, np.cos(x), label='cos(x)')
        plt.title('Custom Styled Plot')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

# 4. Integration and Real-World Applications
# ------------------------------------------

def financial_visualization():
    """Demonstrate a real-world financial visualization."""
    # Generate sample stock data
    dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
    price = 100 + np.cumsum(np.random.randn(len(dates)) * 0.5)
    volume = np.random.randint(1000000, 5000000, size=len(dates))
    data = pd.DataFrame({'Date': dates, 'Price': price, 'Volume': volume})
    data.set_index('Date', inplace=True)

    # Create the visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    fig.suptitle('Stock Price and Volume Analysis', fontsize=16)

    # Price plot
    ax1.plot(data.index, data['Price'], color='blue')
    ax1.set_ylabel('Price ($)')
    ax1.set_title('Stock Price')
    ax1.grid(True)

    # Volume plot
    ax2.bar(data.index, data['Volume'], color='green', alpha=0.5)
    ax2.set_ylabel('Volume')
    ax2.set_xlabel('Date')
    ax2.set_title('Trading Volume')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def machine_learning_visualization():
    """Demonstrate visualizations for machine learning results."""
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import confusion_matrix, roc_curve, auc

    # Generate sample data
    X, y = make_classification(n_samples=1000, n_classes=2, n_features=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train a random forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_pred_proba = clf.predict_proba(X_test)[:, 1]

    # Create visualizations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Machine Learning Model Evaluation', fontsize=16)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax1)
    ax1.set_title('Confusion Matrix')
    ax1.set_xlabel('Predicted Label')
    ax1.set_ylabel('True Label')

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    ax2.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    ax2.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.05])
    ax2.set_xlabel('False Positive Rate')
    ax2.set_ylabel('True Positive Rate')
    ax2.set_title('Receiver Operating Characteristic (ROC) Curve')
    ax2.legend(loc="lower right")

    plt.tight_layout()
    plt.show()

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def interactive_visualization():
    """Demonstrate an interactive visualization using Matplotlib."""
    from matplotlib.widgets import Slider, Button

    # Create initial plot
    fig, ax = plt.subplots(figsize=(10, 6))
    t = np.linspace(0, 10, 1000)
    a0, f0 = 5, 2
    s = a0 * np.sin(2 * np.pi * f0 * t)
    l, = plt.plot(t, s, lw=2)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Amplitude')
    ax.set_title('Interactive Sine Wave')

    # Add sliders for amplitude and frequency
    axamp = plt.axes([0.25, 0.02, 0.50, 0.03])
    axfreq = plt.axes([0.25, 0.07, 0.50, 0.03])
    samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
    sfreq = Slider(axfreq, 'Freq', 0.1, 10.0, valinit=f0)

    def update(val):
        amp = samp.val
        freq = sfreq.val
        l.set_ydata(amp * np.sin(2 * np.pi * freq * t))
        fig.canvas.draw_idle()

    samp.on_changed(update)
    sfreq.on_changed(update)

    # Add reset button
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')

    def reset(event):
        samp.reset()
        sfreq.reset()
    button.on_clicked(reset)

    plt.show()

# 6. FAQs and Troubleshooting
# ---------------------------

def matplotlib_seaborn_faqs():
    """Address common Matplotlib and Seaborn FAQs."""
    print("Matplotlib and Seaborn FAQs:")
    
    # Q: How do I save a figure to a file?
    print("\nQ: How do I save a figure to a file?")
    print("A: Use plt.savefig() function:")
    print("plt.savefig('filename.png', dpi=300, bbox_inches='tight')")
    
    # Q: How do I create subplots?
    print("\nQ: How do I create subplots?")
    print("A: Use plt.subplots() function:")
    print("fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))")
    
    # Q: How do I customize colors in Seaborn?
    print("\nQ: How do I customize colors in Seaborn?")
    print("A: Use Seaborn's color palettes or create custom ones:")
    print("sns.set_palette('deep')")
    print("custom_palette = sns.color_palette('husl', 8)")
    print("sns.set_palette(custom_palette)")

def matplotlib_seaborn_troubleshooting():
    """Provide troubleshooting tips for common Matplotlib and Seaborn issues."""
    print("Matplotlib and Seaborn Troubleshooting Tips:")
    
    # Issue: Figures not showing in Jupyter Notebook
    print("\nIssue: Figures not showing in Jupyter Notebook")
    print("Tip: Use %matplotlib inline magic command at the beginning of your notebook")
    print("or plt.show() at the end of your plotting code")
    
    # Issue: Overlapping labels in plots
    print("\nIssue: Overlapping labels in plots")
    print("Tip: Use plt.tight_layout() or adjust subplot parameters:")
    print("plt.subplots_adjust(hspace=0.4, wspace=0.4)")
    
    # Issue: Seaborn plots not updating style
    print("\nIssue: Seaborn plots not updating style")
    print("Tip: Set style at the beginning of your script or reset default style:")
    print("sns.set_style('whitegrid')")
    print("plt.rcParams.update(plt.rcParamsDefault)  # Reset to matplotlib defaults")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def visualization_resources():
    """Provide recommended tools, libraries, and resources for data visualization."""
    print("Recommended Tools, Libraries, and Resources for Data Visualization:")
    
    print("\nTools and Libraries:")
    print("1. Plotly: For interactive and web-based visualizations")
    print("2. Bokeh: Another library for interactive visualizations")
    print("3. Altair: Declarative statistical visualization library")
    print("4. HoloViews: For composable, declarative data visualization")
    print("5. Dash: For building analytical web applications")
    
    print("\nResources:")
    print("1. Matplotlib Documentation: https://matplotlib.org/stable/contents.html")
    print("2. Seaborn Documentation: https://seaborn.pydata.org/")
    print("3. 'Python for Data Analysis' by Wes McKinney")
    print("4. 'Fundamentals of Data Visualization' by Claus O. Wilke")
    print("5. Datacamp's Data Visualization with Python track")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_visualization(n_points: int = 10000):
    """
    Benchmark various visualization techniques and compare their performance.
    
    Args:
        n_points (int): Number of data points to use in benchmarking.
    """
    print(f"Benchmarking visualization techniques with {n_points} data points:")
    
    # Generate data
    x = np.random.rand(n_points)
    y = np.random.rand(n_points)
    
    # Matplotlib scatter plot
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.close()
    mpl_time = time.time() - start_time
    
    # Seaborn scatter plot
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y)
    plt.close()
    sns_time = time.time() - start_time
    
    print(f"\nScatter plot:")
    print(f"Matplotlib time: {mpl_time:.6f} seconds")
    print(f"Seaborn time: {sns_time:.6f} seconds")
    
    # Histogram
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.hist(x, bins=50)
    plt.close()
    hist_time = time.time() - start_time
    
    print(f"\nHistogram:")
    print(f"Matplotlib histogram time: {hist_time:.6f} seconds")

def optimize_visualization():
    """Demonstrate optimization techniques for data visualization."""
    print("Visualization Optimization Techniques:")
    
    # 1. Use appropriate data types
    print("\n1. Use appropriate data types:")
    x = np.arange(1000000)
    y = np.random.randn(1000000)
    
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.close()
    float64_time = time.time() - start_time
    
    y = y.astype(np.float32)
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.close()
    float32_time = time.time() - start_time
    
    print(f"Float64 time: {float64_time:.6f} seconds")
    print(f"Float32 time: {float32_time:.6f} seconds")
    
    # 2. Use downsampling for large datasets
    print("\n2. Use downsampling for large datasets:")
    def downsample(x, y, num_points):
        indices = np.linspace(0, len(x) - 1, num_points, dtype=int)
        return x[indices], y[indices]
    
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.close()
    full_time = time.time() - start_time
    
    x_down, y_down = downsample(x, y, 10000)
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.plot(x_down, y_down)
    plt.close()
    downsampled_time = time.time() - start_time
    
    print(f"Full dataset time: {full_time:.6f} seconds")
    print(f"Downsampled time: {downsampled_time:.6f} seconds")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    """Provide guidelines for contributing to this note sheet."""
    print("How to Contribute to this Matplotlib and Seaborn Note Sheet:")
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
    print("- Relevance to the main topic of Matplotlib and Seaborn in data science and machine learning.")
    print("- Clarity and depth of explanations.")
    print("- Practical applicability of examples and tips.")
    print("- Up-to-date information on Matplotlib and Seaborn features and best practices.")

# Main function to demonstrate various concepts
def main():
    """
    Main function to demonstrate various concepts related to Matplotlib and Seaborn.
    """
    print("Matplotlib and Seaborn for Data Visualization in Python")
    print("======================================================")
    
    matplotlib_basics()
    seaborn_basics()
    advanced_visualization()
    
    demonstrate_best_practices()
    custom_style()
    
    financial_visualization()
    machine_learning_visualization()
    
    interactive_visualization()
    
    matplotlib_seaborn_faqs()
    matplotlib_seaborn_troubleshooting()
    
    visualization_resources()
    
    benchmark_visualization()
    optimize_visualization()
    
    how_to_contribute()

# Unit tests for visualization functions
class TestVisualizationFunctions(unittest.TestCase):
    def test_matplotlib_basics(self):
        # Test if the function runs without errors
        try:
            matplotlib_basics()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"matplotlib_basics() raised {type(e).__name__} unexpectedly!")

    def test_seaborn_basics(self):
        # Test if the function runs without errors
        try:
            seaborn_basics()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"seaborn_basics() raised {type(e).__name__} unexpectedly!")

    def test_advanced_visualization(self):
        # Test if the function runs without errors
        try:
            advanced_visualization()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"advanced_visualization() raised {type(e).__name__} unexpectedly!")

if __name__ == "__main__":
    main()
    unittest.main(argv=[''], exit=False)