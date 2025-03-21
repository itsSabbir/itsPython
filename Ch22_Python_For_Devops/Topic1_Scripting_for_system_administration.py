# Python for DevOps - Scripting for system administration - in the Python Programming Language
# =========================================================================================

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

import os
import sys
import subprocess
import shutil
import logging
import paramiko
import asyncio
import aiofiles
from typing import List, Dict, Union, Any
import unittest
import time

# 1. Overview and Historical Context
# ----------------------------------
# Python has become a popular choice for DevOps and system administration tasks due to its
# simplicity, readability, and extensive library support. It provides powerful tools for
# automating routine tasks, managing systems, and integrating various components of the
# DevOps pipeline.

# Historical context:
# - Python was created by Guido van Rossum and first released in 1991.
# - Its use in system administration began to grow in the late 1990s and early 2000s.
# - The rise of DevOps practices in the 2010s further boosted Python's adoption in this domain.

# Significance:
# - Python's simplicity and readability make it ideal for writing maintainable scripts.
# - Its cross-platform nature allows for consistent scripting across different operating systems.
# - The extensive standard library and third-party packages provide tools for various system tasks.

# Common use cases:
# - Automating repetitive system administration tasks
# - Log parsing and analysis
# - Configuration management
# - Deployment automation
# - Monitoring and alerting systems

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def file_operations():
    """Demonstrate basic file operations."""
    # Creating a file
    with open('example.txt', 'w') as f:
        f.write('Hello, DevOps!')

    # Reading from a file
    with open('example.txt', 'r') as f:
        content = f.read()
        print(f"File content: {content}")

    # Appending to a file
    with open('example.txt', 'a') as f:
        f.write('\nPython for system administration.')

    # Listing directory contents
    print("\nDirectory contents:")
    for item in os.listdir('.'):
        print(item)

    # Remove the file
    os.remove('example.txt')

def process_management():
    """Demonstrate process management operations."""
    # Running a system command
    result = subprocess.run(['echo', 'Hello from subprocess'], capture_output=True, text=True)
    print(f"Command output: {result.stdout}")

    # Getting current process ID
    print(f"Current process ID: {os.getpid()}")

    # Listing all running processes (Unix-like systems)
    if sys.platform != 'win32':
        ps_output = subprocess.check_output(['ps', 'aux']).decode()
        print("\nRunning processes:")
        print(ps_output[:500])  # Print first 500 characters

def network_operations():
    """Demonstrate basic network operations."""
    # Ping a host
    try:
        ping_result = subprocess.run(['ping', '-c', '4', 'google.com'], capture_output=True, text=True)
        print("Ping result:")
        print(ping_result.stdout)
    except subprocess.CalledProcessError:
        print("Ping failed")

    # Get IP address (simplified)
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use virtual environments to manage dependencies
# 2. Implement proper error handling and logging
# 3. Write modular and reusable code
# 4. Use configuration files for environment-specific settings
# 5. Implement proper security measures (e.g., avoid hardcoding credentials)

# Common Pitfalls:
# 1. Neglecting error handling in system calls
# 2. Inadequate logging and monitoring
# 3. Not considering cross-platform compatibility
# 4. Inefficient handling of large datasets or long-running processes
# 5. Ignoring security best practices

def demonstrate_best_practices():
    """Demonstrate best practices in DevOps scripting."""
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Use environment variables for configuration
        log_dir = os.environ.get('LOG_DIR', '/tmp')
        
        # Create log directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)
        
        # Perform some operation
        logging.info(f"Performing operation in {log_dir}")
        with open(os.path.join(log_dir, 'test.log'), 'w') as f:
            f.write('Test log entry')
        
        logging.info("Operation completed successfully")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

# Advanced Tips:
def advanced_devops_tips():
    """Demonstrate advanced DevOps scripting techniques."""
    # Parallel execution of tasks
    async def async_task(name: str) -> str:
        await asyncio.sleep(1)  # Simulate I/O-bound task
        return f"Task {name} completed"

    async def run_parallel_tasks():
        tasks = [async_task(str(i)) for i in range(5)]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    # Run the async function
    asyncio.run(run_parallel_tasks())

    # Remote command execution using paramiko
    def run_remote_command(hostname: str, username: str, password: str, command: str) -> str:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname, username=username, password=password)
            stdin, stdout, stderr = client.exec_command(command)
            return stdout.read().decode('utf-8')
        finally:
            client.close()

    # Example usage (commented out to avoid actual execution)
    # result = run_remote_command('example.com', 'user', 'password', 'ls -l')
    # print(result)

# 4. Integration and Real-World Applications
# ------------------------------------------

def log_analysis_example():
    """Demonstrate a real-world log analysis script."""
    log_file = 'example.log'
    
    # Generate a sample log file
    with open(log_file, 'w') as f:
        f.write("2023-05-01 10:00:00 INFO User logged in\n")
        f.write("2023-05-01 10:05:00 ERROR Database connection failed\n")
        f.write("2023-05-01 10:10:00 INFO User logged out\n")
        f.write("2023-05-01 10:15:00 WARNING Disk space low\n")

    # Analyze the log file
    error_count = 0
    warning_count = 0

    with open(log_file, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                error_count += 1
            elif 'WARNING' in line:
                warning_count += 1

    print(f"Log Analysis Results:")
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}")

    # Clean up
    os.remove(log_file)

def deployment_automation_example():
    """Demonstrate a simplified deployment automation script."""
    def deploy_application(source_dir: str, target_dir: str):
        print(f"Deploying application from {source_dir} to {target_dir}")
        
        # Create target directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)
        
        # Copy files
        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(target_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        
        print("Deployment completed successfully")

    # Example usage
    source = './app'
    target = './deployed_app'
    
    # Create a sample application directory
    os.makedirs(source, exist_ok=True)
    with open(os.path.join(source, 'app.py'), 'w') as f:
        f.write('print("Hello, DevOps!")')
    
    # Deploy the application
    deploy_application(source, target)
    
    # Clean up
    shutil.rmtree(source)
    shutil.rmtree(target)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def demonstrate_advanced_concepts():
    """Demonstrate advanced DevOps concepts and emerging trends."""
    # Infrastructure as Code (IaC) example using Python
    def create_ec2_instance():
        # This is a simplified example and won't actually create an EC2 instance
        print("Creating EC2 instance...")
        print("Instance created successfully")

    create_ec2_instance()

    # Containerization example (Docker interaction)
    def run_docker_container(image_name: str, container_name: str):
        command = f"docker run -d --name {container_name} {image_name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Container {container_name} started successfully")
        else:
            print(f"Failed to start container: {result.stderr}")

    # Example usage (commented out to avoid actual execution)
    # run_docker_container('nginx:latest', 'my_nginx_container')

    # Serverless function example
    def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
        print("Executing Lambda function")
        return {
            'statusCode': 200,
            'body': 'Hello from Lambda!'
        }

    # Simulate Lambda invocation
    event = {}
    context = None
    result = lambda_handler(event, context)
    print(f"Lambda function result: {result}")

# 6. FAQs and Troubleshooting
# ---------------------------

def devops_faqs():
    """Address common DevOps FAQs."""
    print("DevOps FAQs:")
    
    # Q: How do I handle sensitive information in scripts?
    print("\nQ: How do I handle sensitive information in scripts?")
    print("A: Use environment variables or secure vaults. Never hardcode sensitive data.")
    print("Example:")
    print("import os")
    print("database_password = os.environ.get('DB_PASSWORD')")
    
    # Q: How can I ensure my scripts are portable across different systems?
    print("\nQ: How can I ensure my scripts are portable across different systems?")
    print("A: Use Python's os and sys modules to handle system-specific operations.")
    print("Example:")
    print("import os")
    print("config_path = os.path.join(os.path.expanduser('~'), '.config')")

def devops_troubleshooting():
    """Provide troubleshooting tips for common DevOps issues."""
    print("DevOps Troubleshooting Tips:")
    
    # Issue: Script fails when run as a cron job
    print("\nIssue: Script fails when run as a cron job")
    print("Tip: Ensure full paths are used for all commands and files.")
    print("Use the following at the start of your script:")
    print("import os")
    print("os.chdir(os.path.dirname(os.path.abspath(__file__)))")
    
    # Issue: Permission denied errors
    print("\nIssue: Permission denied errors")
    print("Tip: Check file and directory permissions. Use sudo when necessary.")
    print("Example:")
    print("import os")
    print("os.chmod('file.txt', 0o644)  # Set read-write for owner, read for others")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def devops_resources():
    """Provide recommended tools, libraries, and resources for DevOps with Python."""
    print("Recommended Tools, Libraries, and Resources for DevOps with Python:")
    
    print("\nTools and Libraries:")
    print("1. Ansible: For configuration management and automation")
    print("2. Fabric: For streamlining SSH usage and remote execution")
    print("3. Docker SDK for Python: For interacting with Docker")
    print("4. Boto3: For AWS infrastructure management")
    print("5. Prometheus: For monitoring and alerting")
    
    print("\nResources:")
    print("1. 'Python for DevOps' by Noah Gift et al.")
    print("2. 'Effective DevOps with AWS' by Yogesh Raheja et al.")
    print("3. Python Official Documentation: https://docs.python.org/")
    print("4. Real Python's DevOps tutorials: https://realpython.com/tutorials/devops/")
    print("5. DevOps Roadmap: https://roadmap.sh/devops")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_operations():
    """Benchmark various system operations."""
    print("Benchmarking system operations:")
    
    # File I/O
    start_time = time.time()
    for _ in range(1000):
        with open('benchmark.txt', 'w') as f:
            f.write('Benchmark test')
    file_io_time = time.time() - start_time
    os.remove('benchmark.txt')
    
    print(f"File I/O time (1000 operations): {file_io_time:.4f} seconds")
    
    # Process creation
    start_time = time.time()
    for _ in range(100):
        subprocess.run(['echo', 'test'], capture_output=True)
    process_time = time.time() - start_time
    
    print(f"Process creation time (100 operations): {process_time:.4f} seconds")

def optimize_operations():
    """Demonstrate optimization techniques for DevOps scripts."""
    print("Optimization Techniques:")
    
    # 1. Use generators for memory efficiency
    print("\n1. Use generators for memory efficiency:")
    def process_large_file(filename: str):
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip().upper()
    
    # Example usage
    with open('large_file.txt', 'w') as f:
        f.writelines(f"Line {i}\n" for i in range(1000000))
    
    start_time = time.time()
    for line in process_large_file('large_file.txt'):
        pass  # Process the line
    print(f"Processing time: {time.time() - start_time:.4f} seconds")
    
    os.remove('large_file.txt')
    
    # 2. Use multiprocessing for CPU-bound tasks
    print("\n2. Use multiprocessing for CPU-bound tasks:")
    from multiprocessing import Pool

    def cpu_bound_task(n):
        return sum(i * i for i in range(n))

    def parallel_processing():
        with Pool() as pool:
            results = pool.map(cpu_bound_task, [10000000] * 4)
        return results

    start_time = time.time()
    parallel_processing()
    print(f"Parallel processing time: {time.time() - start_time:.4f} seconds")

    start_time = time.time()
    for _ in range(4):
        cpu_bound_task(10000000)
    print(f"Sequential processing time: {time.time() - start_time:.4f} seconds")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    """Provide guidelines for contributing to this note sheet."""
    print("How to Contribute to this Python for DevOps Note Sheet:")
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
    print("- Relevance to the main topic of Python in DevOps and system administration.")
    print("- Clarity and depth of explanations.")
    print("- Practical applicability of examples and tips.")
    print("- Up-to-date information on Python features and DevOps best practices.")

# Main function to demonstrate various concepts
def main():
    """
    Main function to demonstrate various concepts related to Python for DevOps.
    """
    print("Python for DevOps - Scripting for System Administration")
    print("======================================================")
    
    file_operations()
    process_management()
    network_operations()
    
    demonstrate_best_practices()
    advanced_devops_tips()
    
    log_analysis_example()
    deployment_automation_example()
    
    demonstrate_advanced_concepts()
    
    devops_faqs()
    devops_troubleshooting()
    
    devops_resources()
    
    benchmark_operations()
    optimize_operations()
    
    how_to_contribute()

# Unit tests for DevOps functions
class TestDevOpsFunctions(unittest.TestCase):
    def test_file_operations(self):
        file_operations()
        self.assertFalse(os.path.exists('example.txt'), "File should be deleted after operations")

    def test_process_management(self):
        try:
            process_management()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"process_management() raised {type(e).__name__} unexpectedly!")

    def test_network_operations(self):
        try:
            network_operations()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"network_operations() raised {type(e).__name__} unexpectedly!")

if __name__ == "__main__":
    main()
    unittest.main(argv=[''], exit=False)