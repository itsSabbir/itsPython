# Data Science and Machine Learning Basics - Scikit-learn for machine learning basics - in the Python Programming Language
# =======================================================================================================

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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, model_selection, preprocessing, metrics, pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from typing import List, Tuple, Dict, Union
import time
import unittest

# 1. Overview and Historical Context
# ----------------------------------
# Scikit-learn is a powerful and widely-used machine learning library for Python.
# It provides a comprehensive set of tools for data preprocessing, model selection,
# evaluation, and deployment of machine learning algorithms.

# Historical context:
# - Scikit-learn was initially developed by David Cournapeau in 2007 as a Google Summer of Code project.
# - The first public release (v0.1) was in 2010.
# - It quickly gained popularity and became an integral part of the Python scientific computing ecosystem.

# Significance:
# - Scikit-learn provides a consistent interface for a wide range of machine learning algorithms.
# - It offers robust implementations of many popular machine learning techniques.
# - The library is designed to interoperate well with NumPy and SciPy, making it a natural choice for data scientists using Python.

# Common use cases:
# - Classification and regression tasks
# - Clustering and dimensionality reduction
# - Model selection and evaluation
# - Feature extraction and preprocessing

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def scikit_learn_basics():
    """Demonstrate basic Scikit-learn operations."""
    # Load a dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Create and train a model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

    # Print classification report
    print("\nClassification Report:")
    print(metrics.classification_report(y_test, y_pred))

def preprocessing_example():
    """Demonstrate data preprocessing techniques."""
    # Create a sample dataset
    data = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000],
        'gender': ['M', 'F', 'M', 'F', 'M']
    })

    # One-hot encode categorical variables
    data_encoded = pd.get_dummies(data, columns=['gender'])

    # Scale numerical features
    scaler = preprocessing.StandardScaler()
    data_scaled = scaler.fit_transform(data_encoded[['age', 'income']])

    # Combine scaled numerical features with encoded categorical features
    data_preprocessed = np.hstack((data_scaled, data_encoded[['gender_F', 'gender_M']].values))

    print("Preprocessed data:")
    print(data_preprocessed)

def model_comparison():
    """Compare multiple machine learning models."""
    # Load a dataset
    breast_cancer = datasets.load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target

    # Split the data
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Define models to compare
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'SVM': SVC(random_state=42),
        'KNN': KNeighborsClassifier()
    }

    # Train and evaluate each model
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = metrics.accuracy_score(y_test, y_pred)
        print(f"{name} Accuracy: {accuracy:.2f}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Always split your data into training and testing sets.
# 2. Use cross-validation for more robust model evaluation.
# 3. Scale your features when using distance-based algorithms.
# 4. Handle missing values and outliers appropriately.
# 5. Use pipelines to streamline your machine learning workflow.

# Common Pitfalls:
# 1. Data leakage: allowing test data to influence model training.
# 2. Overfitting: creating models that perform well on training data but poorly on new data.
# 3. Ignoring feature importance and correlation.
# 4. Not handling imbalanced datasets appropriately.
# 5. Neglecting to tune hyperparameters.

def demonstrate_best_practices():
    """Demonstrate best practices in using Scikit-learn."""
    # Load a dataset
    diabetes = datasets.load_diabetes()
    X, y = diabetes.data, diabetes.target

    # Create a pipeline
    pipe = pipeline.Pipeline([
        ('scaler', preprocessing.StandardScaler()),
        ('pca', PCA(n_components=5)),
        ('regressor', RandomForestRegressor(random_state=42))
    ])

    # Perform cross-validation
    cv_scores = model_selection.cross_val_score(pipe, X, y, cv=5)
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean CV score: {cv_scores.mean():.2f} (+/- {cv_scores.std() * 2:.2f})")

    # Train the model using the entire dataset
    pipe.fit(X, y)

    # Feature importance
    feature_importance = pipe.named_steps['regressor'].feature_importances_
    for i, importance in enumerate(feature_importance):
        print(f"Feature {i+1} importance: {importance:.4f}")

# Advanced Tips:
def advanced_scikit_learn_tips():
    """Demonstrate advanced Scikit-learn tips and techniques."""
    # Custom transformer
    class CustomScaler(preprocessing.BaseEstimator, preprocessing.TransformerMixin):
        def __init__(self, factor=1.0):
            self.factor = factor

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            return X * self.factor

    # Custom cross-validation splitter
    class CustomSplitter:
        def __init__(self, n_splits=5):
            self.n_splits = n_splits

        def split(self, X, y=None, groups=None):
            n_samples = X.shape[0]
            fold_size = n_samples // self.n_splits
            for i in range(self.n_splits):
                test_start = i * fold_size
                test_end = (i + 1) * fold_size if i < self.n_splits - 1 else n_samples
                test_indices = np.arange(test_start, test_end)
                train_indices = np.concatenate([np.arange(0, test_start), np.arange(test_end, n_samples)])
                yield train_indices, test_indices

    # Load a dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Create a pipeline with custom transformer
    pipe = pipeline.Pipeline([
        ('custom_scaler', CustomScaler(factor=2.0)),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # Use custom cross-validation splitter
    custom_cv = CustomSplitter(n_splits=5)
    cv_scores = model_selection.cross_val_score(pipe, X, y, cv=custom_cv)
    print(f"Custom CV scores: {cv_scores}")
    print(f"Mean custom CV score: {cv_scores.mean():.2f} (+/- {cv_scores.std() * 2:.2f})")

# 4. Integration and Real-World Applications
# ------------------------------------------

def sentiment_analysis_example():
    """Demonstrate a real-world sentiment analysis application."""
    from sklearn.feature_extraction.text import TfidfVectorizer

    # Sample dataset
    texts = [
        "I love this product! It's amazing.",
        "This is terrible. I hate it.",
        "The quality is okay, but it's overpriced.",
        "Absolutely fantastic! Highly recommended.",
        "Worst purchase ever. Don't buy it."
    ]
    labels = [1, 0, 0, 1, 0]  # 1 for positive, 0 for negative

    # Create a pipeline
    sentiment_pipe = pipeline.Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression(random_state=42))
    ])

    # Train the model
    sentiment_pipe.fit(texts, labels)

    # Make predictions
    new_texts = [
        "This is pretty good.",
        "I regret buying this."
    ]
    predictions = sentiment_pipe.predict(new_texts)
    
    print("Sentiment Analysis Results:")
    for text, sentiment in zip(new_texts, predictions):
        print(f"Text: '{text}'")
        print(f"Sentiment: {'Positive' if sentiment == 1 else 'Negative'}\n")

def customer_segmentation_example():
    """Demonstrate a real-world customer segmentation application."""
    # Generate sample customer data
    np.random.seed(42)
    n_customers = 1000
    age = np.random.randint(18, 70, n_customers)
    income = np.random.normal(50000, 15000, n_customers)
    spending_score = np.random.randint(1, 101, n_customers)

    # Create a dataframe
    customer_data = pd.DataFrame({
        'Age': age,
        'Income': income,
        'SpendingScore': spending_score
    })

    # Preprocess the data
    scaler = preprocessing.StandardScaler()
    customer_data_scaled = scaler.fit_transform(customer_data)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=5, random_state=42)
    customer_data['Cluster'] = kmeans.fit_predict(customer_data_scaled)

    # Visualize the results
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(customer_data['Income'], customer_data['SpendingScore'], 
                          c=customer_data['Cluster'], cmap='viridis')
    plt.colorbar(scatter)
    plt.xlabel('Income')
    plt.ylabel('Spending Score')
    plt.title('Customer Segments')
    plt.show()

    print("Customer Segmentation Results:")
    print(customer_data['Cluster'].value_counts())

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def demonstrate_advanced_concepts():
    """Demonstrate advanced Scikit-learn concepts and emerging trends."""
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.ensemble import GradientBoostingClassifier
    from scipy.stats import uniform, randint

    # Load a dataset
    breast_cancer = datasets.load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target

    # Define the model
    gb_clf = GradientBoostingClassifier(random_state=42)

    # Define the hyperparameter space
    param_distributions = {
        'n_estimators': randint(100, 1000),
        'learning_rate': uniform(0.01, 0.5),
        'max_depth': randint(3, 10),
        'min_samples_split': randint(2, 20),
        'min_samples_leaf': randint(1, 10)
    }

    # Perform randomized search
    random_search = RandomizedSearchCV(
        gb_clf, param_distributions, n_iter=100, cv=5, random_state=42, n_jobs=-1
    )
    random_search.fit(X, y)

    print("Best hyperparameters found:")
    print(random_search.best_params_)
    print(f"Best cross-validation score: {random_search.best_score_:.4f}")

# 6. FAQs and Troubleshooting
# ---------------------------

def scikit_learn_faqs():
    """Address common Scikit-learn FAQs."""
    print("Scikit-learn FAQs:")
    
    # Q: How do I handle missing values?
    print("\nQ: How do I handle missing values?")
    print("A: Use SimpleImputer or more advanced imputation techniques:")
    print("from sklearn.impute import SimpleImputer")
    print("imputer = SimpleImputer(strategy='mean')")
    print("X_imputed = imputer.fit_transform(X)")
    
    # Q: How do I encode categorical variables?
    print("\nQ: How do I encode categorical variables?")
    print("A: Use OneHotEncoder or LabelEncoder:")
    print("from sklearn.preprocessing import OneHotEncoder")
    print("encoder = OneHotEncoder(sparse=False)")
    print("X_encoded = encoder.fit_transform(X)")
    
    # Q: How do I choose the right model?
    print("\nQ: How do I choose the right model?")
    print("A: Consider the problem type, dataset size, interpretability needs, and computational resources.")
    print("Use cross-validation to compare different models' performance.")

def scikit_learn_troubleshooting():
    """Provide troubleshooting tips for common Scikit-learn issues."""
    print("Scikit-learn Troubleshooting Tips:")
    
    # Issue: Overfitting
    print("\nIssue: Overfitting")
    print("Tip: Use regularization, increase training data, or reduce model complexity:")
    print("from sklearn.linear_model import Ridge")
    print("model = Ridge(alpha=1.0)")
    
    # Issue: Slow model training
    print("\nIssue: Slow model training")
    print("Tip: Use more efficient algorithms, reduce data dimensionality, or use partial_fit for large datasets:")
    print("from sklearn.decomposition import TruncatedSVD")
    print("svd = TruncatedSVD(n_components=100)")
    print("X_reduced = svd.fit_transform(X)")
    
    # Issue: Imbalanced datasets
    print("\nIssue: Imbalanced datasets")
    print("Tip: Use class_weight parameter, oversampling, or undersampling techniques:")
    print("from sklearn.utils.class_weight import compute_class_weight")
    print("class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)")
    print("model = RandomForestClassifier(class_weight=dict(enumerate(class_weights)))")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def scikit_learn_resources():
    """Provide recommended tools, libraries, and resources for Scikit-learn."""
    print("Recommended Tools, Libraries, and Resources for Scikit-learn:")
    
    print("\nTools and Libraries:")
    print("1. Pandas: For data manipulation and analysis")
    print("2. NumPy: For numerical computing")
    print("3. Matplotlib and Seaborn: For data visualization")
    print("4. Imbalanced-learn: For handling imbalanced datasets")
    print("5. Scikit-optimize: For hyperparameter optimization")
    
    print("\nResources:")
    print("1. Scikit-learn Official Documentation: https://scikit-learn.org/stable/documentation.html")
    print("2. 'Hands-On Machine Learning with Scikit-Learn and TensorFlow' by Aurélien Géron")
    print("3. 'Python Machine Learning' by Sebastian Raschka")
    print("4. Scikit-learn Tutorials: https://scikit-learn.org/stable/tutorial/index.html")
    print("5. Machine Learning Mastery blog: https://machinelearningmastery.com/category/python-machine-learning/")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_models(n_samples: int = 10000, n_features: int = 20):
    """
    Benchmark various machine learning models and compare their performance.
    
    Args:
        n_samples (int): Number of samples in the dataset.
        n_features (int): Number of features in the dataset.
    """
    print(f"Benchmarking models with {n_samples} samples and {n_features} features:")
    
    # Generate a random dataset
    X, y = datasets.make_classification(
        n_samples=n_samples, n_features=n_features, random_state=42
    )
    
    # Split the data
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Models to benchmark
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'SVM': SVC(random_state=42),
        'KNN': KNeighborsClassifier()
    }
    
    for name, model in models.items():
        start_time = time.time()
        model.fit(X_train, y_train)
        train_time = time.time() - start_time
        
        start_time = time.time()
        y_pred = model.predict(X_test)
        predict_time = time.time() - start_time
        
        accuracy = metrics.accuracy_score(y_test, y_pred)
        
        print(f"\n{name}:")
        print(f"Training time: {train_time:.4f} seconds")
        print(f"Prediction time: {predict_time:.4f} seconds")
        print(f"Accuracy: {accuracy:.4f}")

def optimize_random_forest():
    """Demonstrate optimization techniques for a Random Forest model."""
    print("Random Forest Optimization Techniques:")
    
    # Generate a random dataset
    X, y = datasets.make_classification(
        n_samples=10000, n_features=20, random_state=42
    )
    
    # Split the data
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Baseline model
    rf_base = RandomForestClassifier(random_state=42)
    rf_base.fit(X_train, y_train)
    base_accuracy = rf_base.score(X_test, y_test)
    print(f"\nBaseline Random Forest Accuracy: {base_accuracy:.4f}")
    
    # Optimize number of trees
    n_estimators_range = [10, 50, 100, 200, 500]
    scores = []
    for n_estimators in n_estimators_range:
        rf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
        rf.fit(X_train, y_train)
        scores.append(rf.score(X_test, y_test))
    
    optimal_n_estimators = n_estimators_range[np.argmax(scores)]
    print(f"Optimal number of trees: {optimal_n_estimators}")
    
    # Optimize max depth
    max_depth_range = [5, 10, 20, 50, 100, None]
    scores = []
    for max_depth in max_depth_range:
        rf = RandomForestClassifier(n_estimators=optimal_n_estimators, max_depth=max_depth, random_state=42)
        rf.fit(X_train, y_train)
        scores.append(rf.score(X_test, y_test))
    
    optimal_max_depth = max_depth_range[np.argmax(scores)]
    print(f"Optimal max depth: {optimal_max_depth}")
    
    # Final optimized model
    rf_optimized = RandomForestClassifier(
        n_estimators=optimal_n_estimators,
        max_depth=optimal_max_depth,
        random_state=42
    )
    rf_optimized.fit(X_train, y_train)
    optimized_accuracy = rf_optimized.score(X_test, y_test)
    print(f"Optimized Random Forest Accuracy: {optimized_accuracy:.4f}")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    """Provide guidelines for contributing to this note sheet."""
    print("How to Contribute to this Scikit-learn Note Sheet:")
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
    print("- Relevance to the main topic of Scikit-learn in data science and machine learning.")
    print("- Clarity and depth of explanations.")
    print("- Practical applicability of examples and tips.")
    print("- Up-to-date information on Scikit-learn features and best practices.")

# Main function to demonstrate various concepts
def main():
    """
    Main function to demonstrate various concepts related to Scikit-learn.
    """
    print("Scikit-learn for Machine Learning Basics in Python")
    print("=================================================")
    
    scikit_learn_basics()
    preprocessing_example()
    model_comparison()
    
    demonstrate_best_practices()
    advanced_scikit_learn_tips()
    
    sentiment_analysis_example()
    customer_segmentation_example()
    
    demonstrate_advanced_concepts()
    
    scikit_learn_faqs()
    scikit_learn_troubleshooting()
    
    scikit_learn_resources()
    
    benchmark_models()
    optimize_random_forest()
    
    how_to_contribute()

# Unit tests for Scikit-learn functions
class TestScikitLearnFunctions(unittest.TestCase):
    def test_scikit_learn_basics(self):
        # Test if the function runs without errors
        try:
            scikit_learn_basics()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"scikit_learn_basics() raised {type(e).__name__} unexpectedly!")

    def test_preprocessing_example(self):
        # Test if the function runs without errors
        try:
            preprocessing_example()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"preprocessing_example() raised {type(e).__name__} unexpectedly!")

    def test_model_comparison(self):
        # Test if the function runs without errors
        try:
            model_comparison()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"model_comparison() raised {type(e).__name__} unexpectedly!")

if __name__ == "__main__":
    main()
    unittest.main(argv=[''], exit=False)