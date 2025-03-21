# Web Scraping and Automation - Scrapy Framework Basics - in the Python Programming Language
# =====================================================================================

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

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import DropItem
from scrapy.item import Item, Field
from typing import List, Dict, Any
import logging
import time
from urllib.parse import urlparse

# 1. Overview and Historical Context
# ----------------------------------
# Scrapy is a powerful and flexible web scraping framework for Python. It provides a complete
# set of tools for extracting data from websites efficiently and systematically.

# Historical context:
# - Scrapy was first released in 2008 by Insophia (now Scrapinghub).
# - It was inspired by earlier scraping libraries like Beautiful Soup but aimed to provide
#   a more comprehensive and scalable solution.
# - Scrapy has evolved to support both Python 2 and 3, with the latest versions focusing on Python 3.

# Significance:
# - Scrapy simplifies the process of building and scaling web crawlers.
# - It provides a robust architecture for handling concurrent requests, data extraction,
#   and data processing.
# - The framework includes built-in support for handling common web scraping challenges,
#   such as duplicate request filtering and user agent rotation.

# Common use cases:
# - E-commerce price monitoring
# - News aggregation
# - Data mining for research or business intelligence
# - Content archiving
# - SEO analysis and monitoring

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic Spider
class BasicSpider(scrapy.Spider):
    name = 'basic_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# Item Definition
class QuoteItem(Item):
    text = Field()
    author = Field()
    tags = Field()

# Spider with Item
class ItemSpider(scrapy.Spider):
    name = 'item_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield item

# CrawlSpider Example
class QuoteCrawlSpider(CrawlSpider):
    name = 'quote_crawler'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# Pipeline Example
class DuplicatesPipeline:
    def __init__(self):
        self.quotes_seen = set()

    def process_item(self, item, spider):
        if item['text'] in self.quotes_seen:
            raise DropItem(f"Duplicate quote found: {item}")
        else:
            self.quotes_seen.add(item['text'])
            return item

# Middleware Example
class CustomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Custom User Agent 1.0'

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Respect robots.txt and implement proper crawl delays
# 2. Use Items to structure scraped data
# 3. Implement error handling and logging
# 4. Use middlewares for request/response processing
# 5. Utilize pipelines for data cleaning and storage

# Common Pitfalls:
# 1. Ignoring website terms of service or robots.txt
# 2. Overloading servers with too many requests
# 3. Not handling network errors or timeouts
# 4. Failing to update selectors when website structure changes
# 5. Neglecting to clean and validate scraped data

# Advanced Spider with Error Handling and Logging
class AdvancedSpider(scrapy.Spider):
    name = 'advanced_spider'
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 1,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.setLevel(logging.INFO)

    def parse(self, response):
        try:
            for quote in response.css('div.quote'):
                yield {
                    'text': quote.css('span.text::text').get(),
                    'author': quote.css('small.author::text').get(),
                    'tags': quote.css('div.tags a.tag::text').getall(),
                }
            
            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)
        except Exception as e:
            self.logger.error(f"Error parsing {response.url}: {str(e)}")

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Price monitoring spider
class PriceMonitorSpider(CrawlSpider):
    name = 'price_monitor'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/products']

    rules = (
        Rule(LinkExtractor(allow=r'/product/'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'/category/'), follow=True),
    )

    def parse_product(self, response):
        yield {
            'url': response.url,
            'name': response.css('h1.product-name::text').get(),
            'price': response.css('span.price::text').re_first(r'\d+\.\d+'),
            'stock': response.css('span.stock::text').get(),
            'timestamp': time.time(),
        }

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Asynchronous Spider using coroutines
class AsyncSpider(scrapy.Spider):
    name = 'async_spider'
    start_urls = ['http://quotes.toscrape.com/']

    async def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: How do I handle JavaScript-rendered content?
# A: Use Scrapy with a JavaScript rendering service like Splash or Selenium.

# Q: How can I avoid getting blocked by websites?
# A: Implement proper delays, rotate user agents, and use proxy servers.

# Proxy Middleware Example
class RotatingProxyMiddleware:
    def __init__(self, proxies):
        self.proxies = proxies
        self.current_proxy = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('PROXY_POOL'))

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxies[self.current_proxy]
        self.current_proxy = (self.current_proxy + 1) % len(self.proxies)

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# - Scrapy-Splash: For handling JavaScript-rendered content
# - Scrapyd: For deploying and managing Scrapy spiders
# - Scrapy-UserAgents: For rotating user agents
# - Scrapy-Proxies: For using proxy servers

# Resources:
# - Scrapy Official Documentation: https://docs.scrapy.org/
# - "Web Scraping with Python" by Ryan Mitchell
# - "Learning Scrapy" by Dimitrios Kouzis-Loukas

# 8. Performance Analysis and Optimization
# ----------------------------------------

# Benchmarking function
def benchmark_spider(spider_class, url, num_pages=10):
    class LimitedSpider(spider_class):
        page_count = 0
        
        def parse(self, response):
            self.page_count += 1
            if self.page_count > num_pages:
                raise scrapy.exceptions.CloseSpider('reached page limit')
            yield from super().parse(response)

    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',
        'CLOSESPIDER_PAGECOUNT': num_pages,
    })

    start_time = time.time()
    process.crawl(LimitedSpider, start_urls=[url])
    process.start()
    end_time = time.time()

    return end_time - start_time

# Optimization example: Using CSS selectors instead of XPath
class OptimizedSpider(scrapy.Spider):
    name = 'optimized_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

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
    Main function to demonstrate various concepts related to Scrapy.
    """
    # Basic spider demonstration
    process = CrawlerProcess()
    process.crawl(BasicSpider)
    process.start()

    # Benchmark comparison
    basic_time = benchmark_spider(BasicSpider, 'http://quotes.toscrape.com/')
    optimized_time = benchmark_spider(OptimizedSpider, 'http://quotes.toscrape.com/')
    
    print(f"Basic spider time: {basic_time:.2f} seconds")
    print(f"Optimized spider time: {optimized_time:.2f} seconds")
    print(f"Improvement: {(basic_time - optimized_time) / basic_time * 100:.2f}%")

if __name__ == "__main__":
    main()