# Web Scraping and Automation - Selenium for browser automation - in the Python Programming Language
# ================================================================================================

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

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from typing import List, Dict, Any, Union
import unittest
from unittest.mock import patch, Mock

# 1. Overview and Historical Context
# ----------------------------------
# Selenium is a powerful tool for controlling web browsers through programs and automating browser tasks.
# It is widely used for web scraping, automated testing of web applications, and web-based administration tasks.

# Historical context:
# - Selenium was created by Jason Huggins in 2004 as an internal tool at ThoughtWorks
# - Selenium WebDriver was introduced in 2006, providing a more powerful and flexible API
# - Selenium 2.0 was released in 2011, merging WebDriver and Selenium RC
# - Selenium 3.0 was released in 2016, focusing on W3C WebDriver standardization
# - Selenium 4.0 was released in 2021, with full W3C WebDriver protocol support and new features

# Significance:
# - Enables browser automation across multiple platforms and browsers
# - Supports multiple programming languages, including Python
# - Facilitates automated testing of web applications
# - Powerful tool for web scraping, especially for JavaScript-heavy websites

# Common use cases:
# - Automated web testing
# - Web scraping of dynamic content
# - Automated form filling and submission
# - Simulating user interactions for performance testing

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def setup_driver() -> webdriver.Chrome:
    """Set up and return a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    return webdriver.Chrome(options=options)

# Example 1: Basic usage of Selenium
def basic_selenium_usage():
    """Demonstrate basic usage of Selenium WebDriver."""
    driver = setup_driver()
    try:
        # Navigate to a website
        driver.get("https://www.python.org")
        
        # Find an element by ID and interact with it
        search_bar = driver.find_element(By.ID, "id-search-field")
        search_bar.send_keys("Selenium")
        search_bar.send_keys(Keys.RETURN)
        
        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
        )
        
        # Extract and print search results
        results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
        for result in results:
            print(result.text)
    finally:
        driver.quit()

# Example 2: Handling dynamic content
def handle_dynamic_content():
    """Demonstrate handling of dynamic content with Selenium."""
    driver = setup_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        
        # Click the start button
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        
        # Wait for the hidden element to become visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        
        print(f"Dynamic content: {element.text}")
    finally:
        driver.quit()

# Example 3: Handling alerts and pop-ups
def handle_alerts():
    """Demonstrate handling of JavaScript alerts with Selenium."""
    driver = setup_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        
        # Trigger an alert
        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
        
        # Switch to the alert and accept it
        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()
        
        # Verify the result
        result = driver.find_element(By.ID, "result").text
        print(f"Result: {result}")
    finally:
        driver.quit()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use explicit waits instead of time.sleep()
# 2. Implement proper exception handling
# 3. Use appropriate locator strategies (CSS selectors or XPath)
# 4. Minimize browser instance creation and destruction
# 5. Implement Page Object Model for better organization

# Common Pitfalls:
# 1. Not handling dynamic content properly
# 2. Overusing implicit waits
# 3. Not closing browser instances, leading to resource leaks
# 4. Using unstable locators that might change
# 5. Not considering cross-browser compatibility

# Advanced Tips:
# 1. Use Selenium Grid for parallel testing
# 2. Implement custom expected conditions for complex waits
# 3. Utilize JavaScript execution for complex interactions
# 4. Implement retry mechanisms for flaky tests
# 5. Use Selenium's built-in screenshot capabilities for debugging

# Example: Custom expected condition and JavaScript execution
from selenium.webdriver.support.wait import WebDriverWait

class element_has_css_class(object):
    """An expectation for checking that an element has a particular css class.

    locator - used to find the element
    css_class - the class to check for
    """
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css_class in element.get_attribute("class"):
            return element
        else:
            return False

def advanced_selenium_usage():
    """Demonstrate advanced Selenium usage with custom wait conditions and JavaScript execution."""
    driver = setup_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_classes")
        
        # Click the button to add a new class
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        
        # Wait for the button to have the 'success' class
        button = WebDriverWait(driver, 10).until(
            element_has_css_class((By.CSS_SELECTOR, ".btn"), "success")
        )
        
        print(f"Button classes: {button.get_attribute('class')}")
        
        # Execute JavaScript to modify the page
        driver.execute_script("arguments[0].innerHTML = 'Modified by JavaScript';", button)
        
        print(f"Modified button text: {button.text}")
    finally:
        driver.quit()

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Automated login and data extraction
class LinkedInScraper:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.driver = setup_driver()

    def login(self):
        """Log in to LinkedIn."""
        self.driver.get("https://www.linkedin.com/login")
        self.driver.find_element(By.ID, "username").send_keys(self.email)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Wait for login to complete
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "global-nav"))
        )

    def scrape_profile(self, profile_url: str) -> Dict[str, Any]:
        """Scrape information from a LinkedIn profile."""
        self.driver.get(profile_url)
        
        # Wait for the profile to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card"))
        )
        
        # Extract information
        name = self.driver.find_element(By.CSS_SELECTOR, "h1.text-heading-xlarge").text
        headline = self.driver.find_element(By.CSS_SELECTOR, "div.text-body-medium").text
        
        return {
            "name": name,
            "headline": headline
        }

    def close(self):
        """Close the browser."""
        self.driver.quit()

# Usage example (not executed to protect privacy):
# scraper = LinkedInScraper("your_email@example.com", "your_password")
# scraper.login()
# profile_data = scraper.scrape_profile("https://www.linkedin.com/in/example_profile")
# print(profile_data)
# scraper.close()

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Example: Using Selenium with a proxy
def setup_driver_with_proxy(proxy: str) -> webdriver.Chrome:
    """Set up a Chrome WebDriver instance with a proxy."""
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={proxy}')
    return webdriver.Chrome(options=options)

# Example: Handling shadow DOM
def handle_shadow_dom():
    """Demonstrate handling of shadow DOM elements with Selenium."""
    driver = setup_driver()
    try:
        driver.get("https://books-pwakit.appspot.com/")
        
        # Access shadow DOM
        shadow_host = driver.find_element(By.CSS_SELECTOR, "book-app")
        shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        
        # Find element within shadow DOM
        app_header = shadow_root.find_element(By.CSS_SELECTOR, "app-header")
        app_toolbar = app_header.find_element(By.CSS_SELECTOR, "app-toolbar.toolbar-bottom")
        book_input_decorator = app_toolbar.find_element(By.CSS_SELECTOR, "book-input-decorator")
        input_element = book_input_decorator.find_element(By.CSS_SELECTOR, "#input")
        
        # Interact with the element
        input_element.send_keys("Selenium WebDriver")
        input_element.send_keys(Keys.RETURN)
        
        print("Search performed in shadow DOM")
    finally:
        driver.quit()

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    """Provide answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: How do I handle 'element not interactable' exceptions?":
        "A: Ensure the element is visible and not obscured. Use explicit waits to wait for the element to be clickable.",
        
        "Q: How can I speed up my Selenium tests?":
        "A: Use headless mode, minimize browser instances, implement parallel testing, and optimize wait strategies.",
        
        "Q: How do I handle iframes with Selenium?":
        "A: Use driver.switch_to.frame() to switch to the iframe before interacting with its elements.",
        
        "Q: How can I handle file uploads with Selenium?":
        "A: Use send_keys() with the file path on the file input element. For non-input uploads, consider using AutoIt or Robot class.",
        
        "Q: How do I handle browser notifications?":
        "A: Use ChromeOptions to add preferences that disable notifications before creating the WebDriver instance."
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    """Provide recommended tools, libraries, and resources for Selenium automation in Python."""
    resources = {
        "Libraries": [
            "Selenium WebDriver - https://www.selenium.dev/documentation/en/",
            "webdriver_manager - For automatic management of driver binaries",
            "pytest - For writing and running tests",
            "Allure - For generating test reports"
        ],
        "Tools": [
            "Selenium IDE - For recording and exporting Selenium scripts",
            "BrowserStack - For cross-browser testing",
            "Sauce Labs - For cloud-based testing infrastructure"
        ],
        "Resources": [
            "Selenium with Python documentation - https://selenium-python.readthedocs.io/",
            "The Selenium Guidebook by Dave Haeffner",
            "Elemental Selenium - Free weekly Selenium tips newsletter",
            "Selenium WebDriver with Python 3.x - Udemy course by Rahul Shetty"
        ]
    }
    
    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"- {item}")
        print()

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark(func, *args, **kwargs):
    """Benchmark a function's execution time."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
    return result

def compare_locator_strategies():
    """Compare the performance of different locator strategies."""
    driver = setup_driver()
    try:
        driver.get("https://www.python.org")
        
        print("Finding search input by ID:")
        benchmark(driver.find_element, By.ID, "id-search-field")
        
        print("Finding search input by NAME:")
        benchmark(driver.find_element, By.NAME, "q")
        
        print("Finding search input by CSS_SELECTOR:")
        benchmark(driver.find_element, By.CSS_SELECTOR, "#id-search-field")
        
        print("Finding search input by XPATH:")
        benchmark(driver.find_element, By.XPATH, "//input[@id='id-search-field']")
    finally:
        driver.quit()

# 9. How to Contribute
# --------------------
# (The contribution guidelines would typically be placed here, but for brevity, they are omitted in this code example.)

# Example of a unit test for Selenium automation
class TestSeleniumAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = setup_driver()

    def tearDown(self):
        self.driver.quit()

    def test_python_org_search(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

def main():
    """Main function to demonstrate various concepts related to Selenium automation in Python."""
    print("Demonstrating Selenium automation concepts in Python")
    
    print("\n1. Basic Selenium usage:")
    basic_selenium_usage()
    
    print("\n2. Handling dynamic content:")
    handle_dynamic_content()
    
    print("\n3. Handling alerts and pop-ups:")
    handle_alerts()
    
    print("\n4. Advanced Selenium usage:")
    advanced_selenium_usage()
    
    print("\n5. Handling shadow DOM:")
    handle_shadow_dom()
    
    print("\n6. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()
    
    print("\n7. Recommended Resources:")
    recommended_resources()
    
    print("\n8. Performance Analysis:")
    compare_locator_strategies()
    
    print("\n9. Running unit tests:")
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()

# Additional content and advanced topics:

# Handling file downloads with Selenium
from selenium.webdriver.chrome.options import Options

def setup_driver_for_download(download_dir: str) -> webdriver.Chrome:
    """Set up a Chrome WebDriver instance configured for file downloads."""
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=chrome_options)

def download_file(url: str, download_dir: str):
    """Download a file using Selenium."""
    driver = setup_driver_for_download(download_dir)
    try:
        driver.get(url)
        # Trigger the download (this will depend on the specific website)
        download_button = driver.find_element(By.ID, "download_button")
        download_button.click()
        
        # Wait for the download to complete (you might need to implement a more robust wait mechanism)
        time.sleep(5)
    finally:
        driver.quit()

# Implementing a Page Object Model
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.CLASS_NAME, "welcome-message")

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text

def test_login():
    driver = setup_driver()
    try:
        driver.get("https://example.com/login")
        
        login_page = LoginPage(driver)
        login_page.enter_username("testuser")
        login_page.enter_password("password123")
        login_page.click_login()
        
        home_page = HomePage(driver)
        assert "Welcome" in home_page.get_welcome_message()
    finally:
        driver.quit()

# Handling CAPTCHA
def solve_captcha(driver):
    """
    Demonstrate a basic approach to handling CAPTCHA.
    Note: This is a simplified example and may not work for all CAPTCHAs.
    """
    # Locate the CAPTCHA image
    captcha_img = driver.find_element(By.ID, "captcha-image")
    
    # Get the image source
    img_src = captcha_img.get_attribute("src")
    
    # Download the image (implementation not shown)
    # image_path = download_image(img_src)
    
    # Use an OCR library to read the text from the image (implementation not shown)
    # captcha_text = ocr_read_image(image_path)
    
    # Enter the CAPTCHA text
    captcha_input = driver.find_element(By.ID, "captcha-input")
    captcha_input.send_keys(captcha_text)

# Implementing custom Selenium commands
from selenium.webdriver.remote.webdriver import WebDriver

def add_custom_command(driver):
    def get_element_by_javascript(self, js):
        return self.execute_script(f"return {js};")
    
    WebDriver.get_element_by_javascript = get_element_by_javascript

# Usage:
# add_custom_command(driver)
# element = driver.get_element_by_javascript("document.querySelector('#my-element')")

# Handling infinite scrolling
def scroll_to_bottom(driver):
    """Scroll to the bottom of a page with infinite scrolling."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Implementing a retry mechanism for flaky tests
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def flaky_function(driver):
    # Some potentially flaky Selenium operation
    element = driver.find_element(By.ID, "flaky-element")
    element.click()

# Implementing a custom wait condition
class element_has_attribute(object):
    def __init__(self, locator, attribute, value):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.get_attribute(self.attribute) == self.value:
            return element
        else:
            return False

# Usage:
# WebDriverWait(driver, 10).until(
#     element_has_attribute((By.ID, "my-element"), "data-loaded", "true")
# )

# Handling browser notifications
def setup_driver_with_notifications_disabled():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=chrome_options)

# Implementing a simple Selenium Grid setup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def setup_remote_driver(hub_url, browser):
    if browser.lower() == "chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
    elif browser.lower() == "firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    return webdriver.Remote(
        command_executor=hub_url,
        desired_capabilities=capabilities
    )

# Usage:
# driver = setup_remote_driver("http://localhost:4444/wd/hub", "chrome")

# This concludes the expert-level note sheet on Web Scraping and Automation - Selenium for browser automation in Python.
# The content covers a wide range of topics from basic usage to advanced techniques, providing a comprehensive
# resource for developers at all skill levels.