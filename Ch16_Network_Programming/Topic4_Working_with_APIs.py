# Network Programming - Working with APIs - in the Python Programming Language
# =============================================================================

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
import json
from typing import Dict, Any, List, Union
import time
import asyncio
import aiohttp
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import unittest
from unittest.mock import patch, Mock
import logging

# 1. Overview and Historical Context
# ----------------------------------
# APIs (Application Programming Interfaces) are sets of protocols and tools for
# building software applications. They specify how software components should
# interact, allowing different systems to communicate and share data.

# Historical context:
# - The concept of APIs dates back to the early days of computing.
# - Web APIs gained popularity with the rise of web services in the late 1990s and early 2000s.
# - RESTful APIs, introduced by Roy Fielding in 2000, became the dominant standard for web APIs.
# - More recent developments include GraphQL (2015) and gRPC (2016).

# Significance:
# - APIs enable software integration, allowing different systems to work together.
# - They promote modularity, reusability, and separation of concerns in software design.
# - APIs facilitate the development of complex, distributed systems and microservices architectures.

# Common use cases:
# - Retrieving data from remote servers (e.g., weather data, social media feeds)
# - Sending data to remote servers (e.g., updating user profiles, posting content)
# - Integrating third-party services into applications
# - Building microservices-based architectures

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def basic_api_request():
    """Demonstrate a basic API request using the requests library."""
    response = requests.get('https://api.github.com/users/octocat')
    if response.status_code == 200:
        data = response.json()
        print(f"Username: {data['login']}")
        print(f"Followers: {data['followers']}")
    else:
        print(f"Error: {response.status_code}")

def api_request_with_parameters():
    """Demonstrate an API request with query parameters."""
    params = {'q': 'python', 'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories', params=params)
    if response.status_code == 200:
        data = response.json()
        for repo in data['items'][:5]:
            print(f"Repo: {repo['name']}, Stars: {repo['stargazers_count']}")
    else:
        print(f"Error: {response.status_code}")

def api_request_with_headers():
    """Demonstrate an API request with custom headers."""
    headers = {'User-Agent': 'MyApp/1.0', 'Authorization': 'token YOUR_ACCESS_TOKEN'}
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Authenticated user: {data['login']}")
    else:
        print(f"Error: {response.status_code}")

def post_api_request():
    """Demonstrate a POST API request."""
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
    if response.status_code == 201:
        print(f"Created post with id: {response.json()['id']}")
    else:
        print(f"Error: {response.status_code}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

def api_best_practices():
    """Demonstrate API best practices."""
    
    # Use sessions for multiple requests to the same host
    session = requests.Session()
    
    # Set default timeout for all requests in this session
    session.request = lambda method, url, *args, **kwargs: super(requests.Session, session).request(method, url, *args, **{**kwargs, 'timeout': 10})
    
    # Implement retry logic
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    try:
        response = session.get('https://api.github.com/users/octocat')
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        print(f"Username: {data['login']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def handle_rate_limiting():
    """Demonstrate handling of API rate limiting."""
    response = requests.get('https://api.github.com/rate_limit')
    if response.status_code == 200:
        data = response.json()
        remaining = data['resources']['core']['remaining']
        reset_time = data['resources']['core']['reset']
        if remaining == 0:
            wait_time = reset_time - int(time.time())
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
            time.sleep(wait_time)
        else:
            print(f"Remaining requests: {remaining}")
    else:
        print(f"Error: {response.status_code}")

# 4. Integration and Real-World Applications
# ------------------------------------------

class WeatherAPI:
    """A class to interact with a weather API."""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
    
    def get_current_weather(self, city: str) -> Dict[str, Any]:
        """Get the current weather for a city."""
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = self.session.get(f"{self.BASE_URL}/weather", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_forecast(self, city: str, days: int = 5) -> List[Dict[str, Any]]:
        """Get the weather forecast for a city."""
        params = {'q': city, 'appid': self.api_key, 'units': 'metric', 'cnt': days}
        response = self.session.get(f"{self.BASE_URL}/forecast", params=params)
        response.raise_for_status()
        return response.json()['list']

def weather_api_example():
    """Demonstrate usage of the WeatherAPI class."""
    api = WeatherAPI('YOUR_API_KEY')
    try:
        current_weather = api.get_current_weather('London')
        print(f"Current temperature in London: {current_weather['main']['temp']}°C")
        
        forecast = api.get_forecast('London', 3)
        for day in forecast:
            print(f"Forecast: {day['dt_txt']}, Temp: {day['main']['temp']}°C")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_api_request(url: str) -> Dict[str, Any]:
    """Perform an asynchronous API request."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_multiple_users(usernames: List[str]):
    """Fetch data for multiple users asynchronously."""
    tasks = [async_api_request(f'https://api.github.com/users/{username}') for username in usernames]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"Username: {result['login']}, Followers: {result['followers']}")

def demonstrate_async_requests():
    """Demonstrate asynchronous API requests."""
    usernames = ['octocat', 'torvalds', 'gvanrossum']
    asyncio.run(fetch_multiple_users(usernames))

# 6. FAQs and Troubleshooting
# ---------------------------

def handle_ssl_verification():
    """Demonstrate handling SSL verification issues."""
    try:
        response = requests.get('https://expired.badssl.com')
        response.raise_for_status()
    except requests.exceptions.SSLError:
        print("SSL certificate verification failed. Proceeding with caution...")
        response = requests.get('https://expired.badssl.com', verify=False)
        print(f"Response received: {response.status_code}")

def use_proxy():
    """Demonstrate using a proxy for API requests."""
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }
    try:
        response = requests.get('http://example.org', proxies=proxies)
        print(f"Response received through proxy: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - requests: HTTP library for Python
# - aiohttp: Asynchronous HTTP client/server framework
# - requests-oauthlib: OAuth support for requests
# - requests-cache: Persistent cache for requests

# Resources:
# - "Python for Data Analysis" by Wes McKinney
# - "Web Scraping with Python" by Ryan Mitchell
# - requests documentation: https://docs.python-requests.org/
# - aiohttp documentation: https://docs.aiohttp.org/
# - REST API Design Rulebook by Mark Masse

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_api_requests():
    """Benchmark synchronous vs asynchronous API requests."""
    urls = ['https://api.github.com/users/octocat' for _ in range(10)]
    
    start_time = time.time()
    for url in urls:
        requests.get(url)
    sync_time = time.time() - start_time
    print(f"Synchronous requests took {sync_time:.2f} seconds")
    
    async def async_benchmark():
        async with aiohttp.ClientSession() as session:
            tasks = [session.get(url) for url in urls]
            await asyncio.gather(*tasks)
    
    start_time = time.time()
    asyncio.run(async_benchmark())
    async_time = time.time() - start_time
    print(f"Asynchronous requests took {async_time:.2f} seconds")
    
    print(f"Asynchronous requests were {sync_time / async_time:.2f}x faster")

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
    print("Basic API Request Example:")
    basic_api_request()

    print("\nAPI Request with Parameters Example:")
    api_request_with_parameters()

    print("\nAPI Request with Headers Example:")
    api_request_with_headers()

    print("\nPOST API Request Example:")
    post_api_request()

    print("\nAPI Best Practices Example:")
    api_best_practices()

    print("\nHandle Rate Limiting Example:")
    handle_rate_limiting()

    print("\nWeather API Example:")
    weather_api_example()

    print("\nAsynchronous API Requests Example:")
    demonstrate_async_requests()

    print("\nSSL Verification Handling Example:")
    handle_ssl_verification()

    print("\nProxy Usage Example:")
    use_proxy()

    print("\nAPI Request Benchmarking:")
    benchmark_api_requests()

if __name__ == "__main__":
    main()