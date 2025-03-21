# Web Scraping and Automation - Automating Tasks with Python Scripts - in the Python Programming Language
# ==============================================================================================

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

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import asyncio
import aiohttp
from typing import List, Dict, Any
import logging
import unittest
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import wraps

# 1. Overview and Historical Context
# ----------------------------------
# Web scraping and task automation with Python scripts have become essential tools
# in modern data analysis, research, and software development workflows.

# Historical context:
# - Web scraping emerged in the late 1990s with the growth of the World Wide Web.
# - Python became popular for web scraping due to its simplicity and rich ecosystem.
# - Libraries like Beautiful Soup (2004) and Scrapy (2008) greatly simplified web scraping tasks.
# - Task automation with Python has roots in system administration and has evolved
#   to cover a wide range of applications.

# Significance:
# - Web scraping allows extraction of valuable data from websites for analysis and processing.
# - Task automation increases efficiency, reduces human error, and enables handling of repetitive tasks.
# - Python's extensive library ecosystem makes it ideal for both web scraping and general automation.

# Common use cases:
# - Data mining and market research
# - Price monitoring and comparison
# - Content aggregation
# - Automated testing of web applications
# - Social media monitoring and analysis
# - Process automation in various industries

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic Web Scraping Example
def basic_web_scraper(url: str) -> List[Dict[str, str]]:
    """
    A basic web scraper that extracts quotes from a website.
    
    Args:
        url (str): The URL of the website to scrape.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing quotes and authors.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quotes.append({'text': text, 'author': author})
    
    return quotes

# Asynchronous Web Scraping Example
async def async_web_scraper(urls: List[str]) -> List[Dict[str, str]]:
    """
    An asynchronous web scraper that extracts quotes from multiple websites concurrently.
    
    Args:
        urls (List[str]): A list of URLs to scrape.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing quotes and authors.
    """
    async def fetch(session: aiohttp.ClientSession, url: str) -> List[Dict[str, str]]:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            quotes = []
            for quote in soup.find_all('div', class_='quote'):
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                quotes.append({'text': text, 'author': author})
            return quotes

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    return [quote for sublist in results for quote in sublist]

# Task Automation Example: File Processing
def process_csv_to_json(input_file: str, output_file: str) -> None:
    """
    Automates the task of converting a CSV file to JSON format.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output JSON file.
    """
    data = []
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Respect websites' robots.txt and implement proper rate limiting
# 2. Use appropriate error handling and logging
# 3. Implement retries for failed requests
# 4. Use asynchronous programming for I/O-bound tasks
# 5. Modularize code for better maintainability

# Common Pitfalls:
# 1. Ignoring changes in website structure
# 2. Not handling network errors or timeouts
# 3. Overloading servers with too many requests
# 4. Failing to properly parse and validate extracted data
# 5. Neglecting to handle anti-scraping measures

# Advanced Web Scraper with Error Handling and Retries
def advanced_web_scraper(url: str, max_retries: int = 3, delay: float = 1.0) -> List[Dict[str, str]]:
    """
    An advanced web scraper with error handling, retries, and rate limiting.
    
    Args:
        url (str): The URL of the website to scrape.
        max_retries (int): Maximum number of retry attempts.
        delay (float): Delay between requests in seconds.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing quotes and authors.
    """
    def retry_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    if attempt == max_retries - 1:
                        logging.error(f"Failed to scrape {url}: {str(e)}")
                        raise
                    time.sleep(delay * (2 ** attempt))  # Exponential backoff
        return wrapper

    @retry_decorator
    def fetch_page(url: str) -> requests.Response:
        response = requests.get(url)
        response.raise_for_status()
        return response

    try:
        response = fetch_page(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            quotes.append({'text': text, 'author': author})
        return quotes
    except Exception as e:
        logging.error(f"Error processing {url}: {str(e)}")
        return []

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Automated Stock Price Tracker
@dataclass
class StockData:
    symbol: str
    price: float
    change: float
    volume: int

class StockTracker:
    def __init__(self, symbols: List[str]):
        self.symbols = symbols
    
    def fetch_stock_data(self, symbol: str) -> StockData:
        url = f"https://finance.yahoo.com/quote/{symbol}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        price = float(soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text)
        change = float(soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text.strip('()%'))
        volume = int(soup.find('fin-streamer', {'data-field': 'regularMarketVolume'}).text.replace(',', ''))
        
        return StockData(symbol, price, change, volume)
    
    def track_stocks(self) -> List[StockData]:
        with ThreadPoolExecutor() as executor:
            return list(executor.map(self.fetch_stock_data, self.symbols))

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Headless Browser Automation with Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_dynamic_content(url: str) -> List[Dict[str, str]]:
    """
    Scrapes dynamic content from a website using Selenium with a headless Chrome browser.
    
    Args:
        url (str): The URL of the website to scrape.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing scraped data.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dynamic-content"))
        )
        
        elements = driver.find_elements(By.CLASS_NAME, "dynamic-content")
        return [{"content": element.text} for element in elements]
    finally:
        driver.quit()

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: How can I handle websites that use JavaScript to load content?
# A: Use a headless browser like Selenium or Playwright to interact with dynamic content.

# Q: How do I avoid getting blocked while scraping?
# A: Implement proper delays, rotate user agents, and use proxy servers.

# Browser Fingerprint Randomization
import random

def get_random_user_agent() -> str:
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    return random.choice(user_agents)

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# - Beautiful Soup: For parsing HTML and XML documents
# - Scrapy: A comprehensive web scraping framework
# - Selenium: For browser automation and scraping dynamic content
# - Requests: For making HTTP requests
# - aiohttp: For asynchronous HTTP requests
# - PyAutoGUI: For GUI automation

# Resources:
# - "Web Scraping with Python" by Ryan Mitchell
# - "Automate the Boring Stuff with Python" by Al Sweigart
# - Python's official documentation: https://docs.python.org/3/
# - Beautiful Soup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# - Scrapy documentation: https://docs.scrapy.org/en/latest/

# 8. Performance Analysis and Optimization
# ----------------------------------------

# Benchmarking function
def benchmark_scraper(scraper_func, url: str, num_runs: int = 10) -> float:
    """
    Benchmarks a web scraper function.
    
    Args:
        scraper_func: The scraper function to benchmark.
        url (str): The URL to scrape.
        num_runs (int): Number of runs for averaging performance.
    
    Returns:
        float: Average execution time in seconds.
    """
    total_time = 0
    for _ in range(num_runs):
        start_time = time.time()
        scraper_func(url)
        total_time += time.time() - start_time
    return total_time / num_runs

# Optimization example: Caching
import functools

@functools.lru_cache(maxsize=100)
def cached_web_scraper(url: str) -> List[Dict[str, str]]:
    """
    A web scraper that caches results to avoid redundant requests.
    
    Args:
        url (str): The URL of the website to scrape.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing quotes and authors.
    """
    return basic_web_scraper(url)

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
    """
    Main function to demonstrate various concepts related to web scraping and automation.
    """
    # Basic web scraping example
    url = "http://quotes.toscrape.com/"
    quotes = basic_web_scraper(url)
    print(f"Scraped {len(quotes)} quotes.")

    # Asynchronous web scraping example
    urls = [url] * 3  # Scrape the same URL multiple times for demonstration
    asyncio.run(async_web_scraper(urls))

    # Task automation example
    process_csv_to_json("input.csv", "output.json")

    # Advanced web scraper with error handling
    advanced_quotes = advanced_web_scraper(url)
    print(f"Scraped {len(advanced_quotes)} quotes with advanced scraper.")

    # Real-world example: Stock tracker
    tracker = StockTracker(["AAPL", "GOOGL", "MSFT"])
    stock_data = tracker.track_stocks()
    for data in stock_data:
        print(f"{data.symbol}: ${data.price:.2f} ({data.change:.2f}%) - Volume: {data.volume}")

    # Headless browser automation
    dynamic_content = scrape_dynamic_content("https://example.com/dynamic-page")
    print(f"Scraped {len(dynamic_content)} elements of dynamic content.")

    # Benchmarking and optimization
    avg_time = benchmark_scraper(basic_web_scraper, url)
    print(f"Average execution time: {avg_time:.4f} seconds")

    cached_time = benchmark_scraper(cached_web_scraper, url)
    print(f"Average execution time with caching: {cached_time:.4f} seconds")

    # Demonstrating the impact of caching
    speedup = (avg_time - cached_time) / avg_time * 100
    print(f"Caching improved performance by {speedup:.2f}%")

# Unit Testing Example
class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.url = "http://quotes.toscrape.com/"

    def test_basic_web_scraper(self):
        quotes = basic_web_scraper(self.url)
        self.assertIsInstance(quotes, list)
        self.assertTrue(len(quotes) > 0)
        self.assertIn('text', quotes[0])
        self.assertIn('author', quotes[0])

    def test_advanced_web_scraper(self):
        quotes = advanced_web_scraper(self.url)
        self.assertIsInstance(quotes, list)
        self.assertTrue(len(quotes) > 0)
        self.assertIn('text', quotes[0])
        self.assertIn('author', quotes[0])

    @unittest.skip("Requires internet connection and may be slow")
    def test_async_web_scraper(self):
        urls = [self.url] * 3
        quotes = asyncio.run(async_web_scraper(urls))
        self.assertIsInstance(quotes, list)
        self.assertTrue(len(quotes) > 0)
        self.assertIn('text', quotes[0])
        self.assertIn('author', quotes[0])

# Advanced Concepts: Custom Spider Implementation
class Spider:
    def __init__(self, start_url: str, max_depth: int = 2):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set()

    def crawl(self):
        self._crawl_recursive(self.start_url, 0)

    def _crawl_recursive(self, url: str, depth: int):
        if depth > self.max_depth or url in self.visited:
            return

        self.visited.add(url)
        content = self._fetch(url)
        self._process(url, content)

        for link in self._extract_links(content):
            self._crawl_recursive(link, depth + 1)

    def _fetch(self, url: str) -> str:
        response = requests.get(url)
        return response.text

    def _process(self, url: str, content: str):
        print(f"Processing {url}")

    def _extract_links(self, content: str) -> List[str]:
        soup = BeautifulSoup(content, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]

# Example of a custom spider for a specific website
class QuoteSpider(Spider):
    def _process(self, url: str, content: str):
        soup = BeautifulSoup(content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f"Quote: {text}\nAuthor: {author}\n")

# Advanced Concepts: Distributed Scraping with Celery
# Note: This is a conceptual example and requires Celery and a message broker to be set up
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def scrape_url(url: str) -> List[Dict[str, str]]:
    return basic_web_scraper(url)

def distributed_scraping(urls: List[str]):
    tasks = [scrape_url.delay(url) for url in urls]
    results = [task.get() for task in tasks]
    return [item for sublist in results for item in sublist]

# Advanced Error Handling and Logging
import logging
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='scraper.log'
    )

def robust_web_scraper(url: str) -> List[Dict[str, str]]:
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            quotes.append({'text': text, 'author': author})
        
        logger.info(f"Successfully scraped {len(quotes)} quotes from {url}")
        return quotes

    except HTTPError as e:
        logger.error(f"HTTP error occurred while scraping {url}: {str(e)}")
    except ConnectionError as e:
        logger.error(f"Connection error occurred while scraping {url}: {str(e)}")
    except Timeout as e:
        logger.error(f"Timeout occurred while scraping {url}: {str(e)}")
    except RequestException as e:
        logger.error(f"An error occurred while scraping {url}: {str(e)}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred while scraping {url}")

    return []

# Performance Optimization: Multiprocessing for CPU-bound tasks
import multiprocessing

def cpu_intensive_task(data: List[str]) -> List[str]:
    # Simulate a CPU-intensive task, e.g., complex data processing
    return [item.upper() for item in data]

def parallel_processing(data: List[str], num_processes: int = None) -> List[str]:
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(cpu_intensive_task, chunks)

    return [item for sublist in results for item in sublist]

# Advanced Concepts: Using APIs for data extraction
import requests

def fetch_github_repos(username: str) -> List[Dict[str, Any]]:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    
    repos = response.json()
    return [
        {
            'name': repo['name'],
            'stars': repo['stargazers_count'],
            'description': repo['description']
        }
        for repo in repos
    ]

# Ethical Considerations and Rate Limiting
class RateLimitedScraper:
    def __init__(self, requests_per_minute: int):
        self.delay = 60 / requests_per_minute
        self.last_request = 0

    def fetch(self, url: str) -> str:
        elapsed = time.time() - self.last_request
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        
        response = requests.get(url)
        self.last_request = time.time()
        return response.text

# Main function extension
if __name__ == "__main__":
    main()

    # Run unit tests
    unittest.main(argv=[''], exit=False)

    # Demonstrate custom spider
    quote_spider = QuoteSpider("http://quotes.toscrape.com/", max_depth=1)
    quote_spider.crawl()

    # Demonstrate distributed scraping (conceptual)
    # urls = ["http://quotes.toscrape.com/page/1/", "http://quotes.toscrape.com/page/2/"]
    # distributed_results = distributed_scraping(urls)

    # Demonstrate robust error handling and logging
    robust_web_scraper("http://quotes.toscrape.com/")

    # Demonstrate parallel processing for CPU-bound tasks
    data = ["item1", "item2", "item3", "item4", "item5"]
    processed_data = parallel_processing(data)
    print(f"Processed data: {processed_data}")

    # Demonstrate API usage
    github_username = "octocat"
    github_repos = fetch_github_repos(github_username)
    print(f"GitHub repositories for {github_username}:")
    for repo in github_repos:
        print(f"- {repo['name']} (Stars: {repo['stars']}): {repo['description']}")

    # Demonstrate ethical scraping with rate limiting
    ethical_scraper = RateLimitedScraper(requests_per_minute=10)
    content = ethical_scraper.fetch("http://quotes.toscrape.com/")
    print(f"Ethically scraped content length: {len(content)} characters")

# This concludes the expert-level note sheet on Web Scraping and Automation with Python scripts.
# It covers a wide range of topics from basic concepts to advanced techniques, providing a
# comprehensive resource for developers at all skill levels.

          