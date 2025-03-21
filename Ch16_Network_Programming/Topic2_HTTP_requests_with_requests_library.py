# Network Programming - HTTP requests with requests library - in the Python Programming Language
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
import json
from typing import Dict, Any, List, Union
import time
import asyncio
import aiohttp
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# 1. Overview and Historical Context
# ----------------------------------
# The requests library is a popular HTTP client library for Python, known for its
# simplicity and user-friendly API. It abstracts the complexities of making HTTP
# requests, allowing developers to interact with web services and APIs easily.

# Historical context:
# - Created by Kenneth Reitz in 2011
# - Quickly gained popularity due to its intuitive design compared to urllib/urllib2
# - Became part of the Python Packaging Authority in 2014
# - Continues to be actively maintained and widely used in the Python ecosystem

# Significance:
# - Simplifies HTTP interactions in Python
# - Provides a consistent API for various HTTP methods (GET, POST, PUT, DELETE, etc.)
# - Handles complex scenarios like authentication, sessions, and cookies with ease
# - Supports both synchronous and asynchronous (with extensions) operations

# Common use cases:
# - Interacting with RESTful APIs
# - Web scraping
# - Automated testing of web applications
# - Sending data to web servers
# - Downloading files and resources from the internet

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def basic_request_examples():
    # Basic GET request
    response = requests.get('https://api.github.com')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text[:100]}...")  # Print first 100 characters

    # POST request with data
    data = {'key': 'value'}
    response = requests.post('https://httpbin.org/post', data=data)
    print(f"POST response: {response.json()}")

    # Request with headers
    headers = {'User-Agent': 'MyApp/1.0'}
    response = requests.get('https://api.github.com', headers=headers)
    print(f"Headers used: {response.request.headers}")

    # Handling authentication
    auth = ('username', 'password')
    response = requests.get('https://api.github.com/user', auth=auth)
    print(f"Authenticated request status: {response.status_code}")

def advanced_request_examples():
    # Session usage for performance
    session = requests.Session()
    session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    response = session.get('https://httpbin.org/cookies')
    print(f"Session cookies: {response.json()}")

    # Streaming response
    with requests.get('https://httpbin.org/stream/20', stream=True) as r:
        for line in r.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                print(f"Streaming data: {decoded_line[:50]}...")  # Print first 50 characters

    # File upload
    files = {'file': open('example.txt', 'rb')}
    response = requests.post('https://httpbin.org/post', files=files)
    print(f"File upload response: {response.json()}")

def error_handling_examples():
    try:
        response = requests.get('https://httpbin.org/status/404')
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error occurred: {err}")

    try:
        response = requests.get('https://nonexistentwebsite.com', timeout=3)
    except requests.exceptions.Timeout:
        print("The request timed out")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

def best_practices_example():
    # Use session for multiple requests to the same host
    session = requests.Session()
    
    # Set default timeout for all requests in this session
    session.request = lambda method, url, *args, **kwargs: super(requests.Session, session).request(method, url, *args, **{**kwargs, 'timeout': 10})
    
    # Use params for query string parameters
    params = {'q': 'python', 'sort': 'stars'}
    response = session.get('https://api.github.com/search/repositories', params=params)
    
    # Always close the session when done
    session.close()
    
    return response.json()

def common_pitfalls_example():
    # Pitfall: Not closing response body
    response = requests.get('https://api.github.com', stream=True)
    # ... do something with the response ...
    response.close()  # Always close the response when using stream=True

    # Pitfall: Not handling redirects properly
    response = requests.get('http://github.com', allow_redirects=False)
    if response.status_code == 301:
        print(f"Redirected to: {response.headers['Location']}")

def advanced_tips_example():
    # Tip: Use connection pooling for better performance
    session = requests.Session()
    adapter = HTTPAdapter(pool_connections=10, pool_maxsize=10)
    session.mount('https://', adapter)

    # Tip: Implement retry logic
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        response = session.get('https://api.github.com')
        print(f"Request successful after retries: {response.status_code}")
    except requests.exceptions.RetryError as e:
        print(f"All retries failed: {e}")

# 4. Integration and Real-World Applications
# ------------------------------------------

class GithubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"token {token}"})

    def get_user_repos(self, username: str) -> List[Dict[str, Any]]:
        response = self.session.get(f"{self.BASE_URL}/users/{username}/repos")
        response.raise_for_status()
        return response.json()

    def create_gist(self, files: Dict[str, Dict[str, str]], description: str, public: bool = True) -> Dict[str, Any]:
        data = {
            "description": description,
            "public": public,
            "files": files
        }
        response = self.session.post(f"{self.BASE_URL}/gists", json=data)
        response.raise_for_status()
        return response.json()

def github_api_example():
    # Note: Replace with a valid GitHub token
    github = GithubAPI("your_github_token_here")
    
    # Get repositories for a user
    repos = github.get_user_repos("octocat")
    print(f"Octocat has {len(repos)} public repositories")

    # Create a gist
    files = {
        "example.py": {
            "content": "print('Hello, World!')"
        }
    }
    gist = github.create_gist(files, "Example Gist", public=True)
    print(f"Created gist with ID: {gist['id']}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_request(url: str) -> Dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def async_requests_example():
    urls = [
        'https://api.github.com/users/octocat',
        'https://api.github.com/users/torvalds',
        'https://api.github.com/users/gvanrossum'
    ]
    tasks = [async_request(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"User: {result['login']}, Followers: {result['followers']}")

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    # Q: How to handle SSL certificate verification?
    response = requests.get('https://expired.badssl.com', verify=False)
    # Warning: This disables SSL certificate verification and is not recommended for production use

    # Q: How to use a proxy?
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }
    response = requests.get('http://example.org', proxies=proxies)

    # Q: How to handle cookies?
    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    response = requests.get('http://httpbin.org/cookies', cookies=jar)

    return response.json()

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - requests-oauthlib: For OAuth support
# - requests-cache: For adding caching support to requests
# - requests-toolbelt: Collection of utilities for requests
# - pytest-requests: For testing requests in pytest

# Resources:
# - Requests documentation: https://docs.python-requests.org/
# - "Python for Data Analysis" by Wes McKinney
# - "Web Scraping with Python" by Ryan Mitchell
# - Real Python's guide on Python requests: https://realpython.com/python-requests/
# - PyVideo talks on requests: https://pyvideo.org/search.html?q=requests

# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis():
    session = requests.Session()
    adapter = HTTPAdapter(pool_connections=100, pool_maxsize=100)
    session.mount('https://', adapter)

    urls = ['https://api.github.com/users/octocat' for _ in range(10)]

    start_time = time.time()
    for url in urls:
        session.get(url)
    end_time = time.time()

    print(f"Sequential requests took {end_time - start_time:.2f} seconds")

    async def async_performance_test():
        async with aiohttp.ClientSession() as session:
            tasks = [session.get(url) for url in urls]
            await asyncio.gather(*tasks)

    start_time = time.time()
    asyncio.run(async_performance_test())
    end_time = time.time()

    print(f"Asynchronous requests took {end_time - start_time:.2f} seconds")

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
    print("Basic Request Examples:")
    basic_request_examples()

    print("\nAdvanced Request Examples:")
    advanced_request_examples()

    print("\nError Handling Examples:")
    error_handling_examples()

    print("\nBest Practices Example:")
    result = best_practices_example()
    print(f"Search result: {result['total_count']} repositories found")

    print("\nCommon Pitfalls Example:")
    common_pitfalls_example()

    print("\nAdvanced Tips Example:")
    advanced_tips_example()

    print("\nGitHub API Example:")
    github_api_example()

    print("\nAsynchronous Requests Example:")
    asyncio.run(async_requests_example())

    print("\nFAQ and Troubleshooting:")
    faq_result = faq_and_troubleshooting()
    print(f"Cookie handling result: {faq_result}")

    print("\nPerformance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()