# Web Scraping and Automation - Beautiful Soup and lxml - in the Python Programming Language
# ==========================================================================================

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
from lxml import etree
import time
import asyncio
import aiohttp
from typing import List, Dict, Any, Union
import re
import json
import csv
from concurrent.futures import ThreadPoolExecutor
import unittest
from unittest.mock import patch, Mock

# 1. Overview and Historical Context
# ----------------------------------
# Web scraping is the process of automatically extracting data from websites. Beautiful Soup and lxml
# are popular Python libraries used for parsing HTML and XML documents, making them essential tools for web scraping.

# Historical context:
# - Beautiful Soup was first released in 2004 by Leonard Richardson
# - lxml was initially released in 2005 by Stefan Behnel, Martijn Faassen, and contributors
# - Both libraries have evolved to support various XML and HTML standards and parsing methods

# Significance:
# - Enables automated data extraction from web pages
# - Provides powerful tools for navigating and searching parsed documents
# - Supports different parsing methods (e.g., html.parser, lxml, html5lib)
# - Facilitates web automation and testing

# Common use cases:
# - Data mining and research
# - Price monitoring and comparison
# - News aggregation
# - Social media analysis
# - Content migration

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def fetch_html(url: str) -> str:
    """Fetch HTML content from a given URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_with_beautiful_soup(html: str) -> BeautifulSoup:
    """Parse HTML content using Beautiful Soup."""
    return BeautifulSoup(html, 'html.parser')

def parse_with_lxml(html: str) -> etree._Element:
    """Parse HTML content using lxml."""
    return etree.HTML(html)

# Example 1: Basic usage of Beautiful Soup
def example_beautiful_soup():
    """Demonstrate basic usage of Beautiful Soup."""
    html = """
    <html>
        <body>
            <h1>Web Scraping Example</h1>
            <p class="content">This is a paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find elements
    title = soup.find('h1').text
    paragraph = soup.find('p', class_='content').text
    items = [li.text for li in soup.find_all('li')]
    
    print(f"Title: {title}")
    print(f"Paragraph: {paragraph}")
    print(f"Items: {items}")

# Example 2: Basic usage of lxml
def example_lxml():
    """Demonstrate basic usage of lxml."""
    html = """
    <html>
        <body>
            <h1>Web Scraping Example</h1>
            <p class="content">This is a paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </body>
    </html>
    """
    tree = etree.HTML(html)
    
    # Find elements using XPath
    title = tree.xpath('//h1/text()')[0]
    paragraph = tree.xpath('//p[@class="content"]/text()')[0]
    items = tree.xpath('//li/text()')
    
    print(f"Title: {title}")
    print(f"Paragraph: {paragraph}")
    print(f"Items: {items}")

# Example 3: Web scraping with Beautiful Soup
def scrape_quotes() -> List[Dict[str, str]]:
    """Scrape quotes from a sample website using Beautiful Soup."""
    url = "http://quotes.toscrape.com"
    html = fetch_html(url)
    soup = parse_with_beautiful_soup(html)
    
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })
    
    return quotes

# Example 4: Web scraping with lxml
def scrape_books() -> List[Dict[str, Union[str, float]]]:
    """Scrape books from a sample website using lxml."""
    url = "http://books.toscrape.com"
    html = fetch_html(url)
    tree = parse_with_lxml(html)
    
    books = []
    for book in tree.xpath('//article[@class="product_pod"]'):
        title = book.xpath('.//h3/a/@title')[0]
        price = float(book.xpath('.//p[@class="price_color"]/text()')[0][1:])
        availability = book.xpath('.//p[@class="instock availability"]/text()')[1].strip()
        books.append({
            'title': title,
            'price': price,
            'availability': availability
        })
    
    return books

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Respect robots.txt and website terms of service
# 2. Implement rate limiting to avoid overloading servers
# 3. Use appropriate CSS selectors or XPath expressions for reliable parsing
# 4. Handle exceptions and network errors gracefully
# 5. Cache results when appropriate to reduce unnecessary requests

# Common Pitfalls:
# 1. Ignoring dynamic content loaded by JavaScript
# 2. Not handling changes in website structure
# 3. Overlooking character encoding issues
# 4. Failing to handle pagination or infinite scrolling
# 5. Neglecting to clean and validate scraped data

# Advanced Tips:
# 1. Use asynchronous scraping for improved performance
# 2. Implement custom caching mechanisms for frequently accessed data
# 3. Utilize browser automation tools like Selenium for JavaScript-heavy sites
# 4. Employ proxies and user agent rotation to avoid IP blocks
# 5. Implement incremental scraping to handle large datasets efficiently

# Example: Asynchronous scraping with aiohttp and Beautiful Soup
async def fetch_async(url: str, session: aiohttp.ClientSession) -> str:
    """Fetch HTML content asynchronously."""
    async with session.get(url) as response:
        return await response.text()

async def scrape_quotes_async(urls: List[str]) -> List[Dict[str, Any]]:
    """Scrape quotes from multiple pages asynchronously."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(url, session) for url in urls]
        htmls = await asyncio.gather(*tasks)
    
    all_quotes = []
    for html in htmls:
        soup = parse_with_beautiful_soup(html)
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })
        all_quotes.extend(quotes)
    
    return all_quotes

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Price monitoring system
class PriceMonitor:
    def __init__(self, products: List[Dict[str, str]]):
        self.products = products
    
    def fetch_prices(self) -> List[Dict[str, Any]]:
        """Fetch current prices for all products."""
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(self._fetch_product_price, self.products))
        return results
    
    def _fetch_product_price(self, product: Dict[str, str]) -> Dict[str, Any]:
        """Fetch price for a single product."""
        html = fetch_html(product['url'])
        tree = parse_with_lxml(html)
        price_str = tree.xpath(product['price_xpath'])[0].strip()
        price = float(re.search(r'\d+\.\d+', price_str).group())
        return {
            'name': product['name'],
            'url': product['url'],
            'price': price
        }
    
    def save_prices(self, prices: List[Dict[str, Any]], filename: str):
        """Save fetched prices to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'url', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for price in prices:
                writer.writerow(price)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Example: Using Scrapy for large-scale web scraping
# Note: This is a simplified example and would typically be in a separate file
import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    """Provide answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: How do I handle websites that require authentication?":
        "A: Use the requests library to maintain a session and send login credentials. Then use the authenticated session for subsequent requests.",
        
        "Q: What should I do if a website blocks my scraping attempts?":
        "A: Implement rate limiting, rotate user agents and IP addresses (using proxies), and consider reaching out to the website owner for permission or API access.",
        
        "Q: How can I scrape data from a website that uses infinite scrolling?":
        "A: Analyze the AJAX requests made during scrolling and replicate them in your scraper, or use browser automation tools like Selenium to interact with the page.",
        
        "Q: What's the best way to handle large amounts of scraped data?":
        "A: Consider using a database to store the data, implement incremental scraping, and use data processing libraries like pandas for analysis.",
        
        "Q: How do I ensure my web scraper continues to work if the website's structure changes?":
        "A: Implement robust error handling, use flexible selectors, regularly monitor your scraper's output, and consider implementing automated tests to detect changes."
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    """Provide recommended tools, libraries, and resources for web scraping with Python."""
    resources = {
        "Libraries": [
            "Beautiful Soup - https://www.crummy.com/software/BeautifulSoup/",
            "lxml - https://lxml.de/",
            "Scrapy - https://scrapy.org/",
            "Selenium - https://www.selenium.dev/",
            "requests - https://docs.python-requests.org/",
            "aiohttp - https://docs.aiohttp.org/"
        ],
        "Tools": [
            "Scrapy Cloud - For deploying and running web scrapers",
            "ScrapingHub - Managed web scraping platform",
            "Portia - Visual scraping tool",
            "ParseHub - Web scraping tool with a visual interface"
        ],
        "Resources": [
            "Web Scraping with Python by Ryan Mitchell",
            "The Hitchhiker's Guide to Python's Web Scraping section - https://docs.python-guide.org/scenarios/scrape/",
            "Scrapy documentation - https://docs.scrapy.org/",
            "Mozilla Developer Network (MDN) Web Docs - For understanding web technologies",
            "W3Schools XPath Tutorial - https://www.w3schools.com/xml/xpath_intro.asp"
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

def compare_parsers():
    """Compare the performance of different HTML parsers."""
    html = fetch_html("http://quotes.toscrape.com")
    
    print("Parsing with html.parser:")
    benchmark(BeautifulSoup, html, 'html.parser')
    
    print("Parsing with lxml:")
    benchmark(BeautifulSoup, html, 'lxml')
    
    print("Parsing with html5lib:")
    benchmark(BeautifulSoup, html, 'html5lib')
    
    print("Parsing with lxml.etree:")
    benchmark(etree.HTML, html)

# 9. How to Contribute
# --------------------
# (The contribution guidelines would typically be placed here, but for brevity, they are omitted in this code example.)

# Example of a unit test for the scraping function
class TestWebScraping(unittest.TestCase):
    @patch('requests.get')
    def test_scrape_quotes(self, mock_get):
        with open('test_quotes.html', 'r') as f:
            mock_get.return_value.text = f.read()
        
        quotes = scrape_quotes()
        
        self.assertEqual(len(quotes), 10)
        self.assertEqual(quotes[0]['author'], 'Albert Einstein')
        self.assertIn('change', quotes[0]['tags'])




def main():
    """Main function to demonstrate various concepts related to web scraping with Beautiful Soup and lxml."""
    print("Demonstrating web scraping with Beautiful Soup and lxml")

    print("\n1. Basic usage of Beautiful Soup:")
    example_beautiful_soup()

    print("\n2. Basic usage of lxml:")
    example_lxml()

    print("\n3. Web scraping with Beautiful Soup:")
    quotes = benchmark(scrape_quotes)
    print(f"Scraped {len(quotes)} quotes")
    print(f"First quote: {quotes[0]['text'][:50]}...")

    print("\n4. Web scraping with lxml:")
    books = benchmark(scrape_books)
    print(f"Scraped {len(books)} books")
    print(f"First book: {books[0]['title']}, Price: ${books[0]['price']}")

    print("\n5. Asynchronous scraping:")
    urls = [f"http://quotes.toscrape.com/page/{i}/" for i in range(1, 6)]
    async_quotes = asyncio.run(scrape_quotes_async(urls))
    print(f"Scraped {len(async_quotes)} quotes asynchronously")

    print("\n6. Real-world application (Price monitoring):")
    products = [
        {
            'name': 'Example Product 1',
            'url': 'http://example.com/product1',
            'price_xpath': '//span[@class="price"]/text()'
        },
        {
            'name': 'Example Product 2',
            'url': 'http://example.com/product2',
            'price_xpath': '//span[@class="price"]/text()'
        }
    ]
    monitor = PriceMonitor(products)
    prices = monitor.fetch_prices()
    monitor.save_prices(prices, 'prices.csv')
    print(f"Fetched and saved prices for {len(prices)} products")

    print("\n7. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()

    print("\n8. Recommended Resources:")
    recommended_resources()

    print("\n9. Performance Analysis:")
    compare_parsers()

    print("\n10. Running unit tests:")
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()

# Additional content and advanced topics:

# Handling JavaScript-rendered content
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_dynamic_content(url: str) -> str:
    """Scrape content from a JavaScript-rendered page using Selenium."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    # Wait for dynamic content to load (you might need to adjust the wait time)
    time.sleep(5)
    
    page_source = driver.page_source
    driver.quit()
    
    return page_source

# Handling pagination
def scrape_paginated_content(base_url: str, max_pages: int) -> List[Dict[str, Any]]:
    """Scrape content from multiple pages."""
    all_items = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        html = fetch_html(url)
        soup = parse_with_beautiful_soup(html)
        
        items = soup.find_all('div', class_='item')
        for item in items:
            # Extract item data
            title = item.find('h2').text
            description = item.find('p', class_='description').text
            all_items.append({
                'title': title,
                'description': description
            })
        
        # Check if there's a next page
        next_button = soup.find('a', class_='next-page')
        if not next_button:
            break
    
    return all_items

# Handling authentication
def scrape_authenticated_content(login_url: str, protected_url: str, username: str, password: str) -> str:
    """Scrape content from a page that requires authentication."""
    session = requests.Session()
    
    # Perform login
    login_data = {
        'username': username,
        'password': password
    }
    session.post(login_url, data=login_data)
    
    # Access protected content
    response = session.get(protected_url)
    return response.text

# Implementing custom caching
import hashlib
import os
import pickle

class WebCache:
    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def get(self, url: str) -> Union[str, None]:
        """Retrieve cached content for a URL."""
        cache_file = self._get_cache_file(url)
        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        return None
    
    def set(self, url: str, content: str):
        """Cache content for a URL."""
        cache_file = self._get_cache_file(url)
        with open(cache_file, 'wb') as f:
            pickle.dump(content, f)
    
    def _get_cache_file(self, url: str) -> str:
        """Generate a unique cache file name for a URL."""
        return os.path.join(self.cache_dir, hashlib.md5(url.encode()).hexdigest())

# Usage example:
# cache = WebCache('web_cache')
# html = cache.get(url)
# if html is None:
#     html = fetch_html(url)
#     cache.set(url, html)

# Implementing a simple rate limiter
import time
from functools import wraps

def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)
    def decorate(func):
        last_time_called = [0.0]
        @wraps(func)
        def rate_limited_function(*args, **kwargs):
            elapsed = time.time() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_time_called[0] = time.time()
            return ret
        return rate_limited_function
    return decorate

# Usage example:
# @rate_limited(2)  # 2 calls per second at most
# def fetch_url(url):
#     return requests.get(url)

# Advanced error handling and retrying
from requests.exceptions import RequestException
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def fetch_with_retry(url: str) -> str:
    """Fetch HTML content with retry logic."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        print(f"Error fetching {url}: {e}")
        raise

# Cleaning and normalizing scraped data
import unicodedata

def clean_text(text: str) -> str:
    """Clean and normalize scraped text."""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Normalize Unicode characters
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    # Remove non-printable characters
    text = ''.join(char for char in text if char.isprintable())
    return text

# Example of using XPath with lxml for complex queries
def extract_table_data(html: str) -> List[Dict[str, str]]:
    """Extract data from an HTML table using complex XPath queries."""
    tree = etree.HTML(html)
    rows = tree.xpath('//table[@id="data-table"]/tr[position() > 1]')
    data = []
    for row in rows:
        cells = row.xpath('./td')
        if len(cells) >= 3:
            data.append({
                'name': cells[0].xpath('string()').strip(),
                'value': cells[1].xpath('string()').strip(),
                'date': cells[2].xpath('string()').strip()
            })
    return data

# Implementing a simple spider
class SimpleSpider:
    def __init__(self, start_url: str, allowed_domain: str):
        self.start_url = start_url
        self.allowed_domain = allowed_domain
        self.visited = set()
    
    def crawl(self, max_pages: int = 10):
        queue = [self.start_url]
        while queue and len(self.visited) < max_pages:
            url = queue.pop(0)
            if url in self.visited:
                continue
            
            print(f"Crawling: {url}")
            html = fetch_html(url)
            self.visited.add(url)
            
            # Process the page (e.g., extract data)
            self.process_page(url, html)
            
            # Find new links
            soup = parse_with_beautiful_soup(html)
            for link in soup.find_all('a', href=True):
                next_url = link['href']
                if next_url.startswith(self.allowed_domain) and next_url not in self.visited:
                    queue.append(next_url)
    
    def process_page(self, url: str, html: str):
        # Implement your data extraction logic here
        pass

# Usage example:
# spider = SimpleSpider('http://example.com', 'http://example.com')
# spider.crawl()

# This concludes the expert-level note sheet on Web Scraping and Automation with Beautiful Soup and lxml in Python.
# The content covers a wide range of topics from basic usage to advanced techniques, providing a comprehensive
# resource for developers at all skill levels.