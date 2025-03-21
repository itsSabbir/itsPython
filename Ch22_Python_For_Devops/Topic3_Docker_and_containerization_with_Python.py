"""
Python for DevOps - Docker and Containerization - in the Python Programming Language
====================================================================================

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization
9. How to Contribute

Author: Sabbir Hossain

1. Overview and Historical Context
----------------------------------
Docker and containerization have revolutionized the way applications are developed, deployed, and scaled in modern software development and DevOps practices. Containers provide a lightweight, portable, and consistent environment for running applications across different platforms and infrastructures.

Historical context:
- Docker was first released as an open-source project in 2013 by Solomon Hykes.
- It built upon existing Linux container technologies like LXC (Linux Containers).
- The concept of containerization itself dates back to the 1970s with Unix chroot.

Significance:
- Containers provide a consistent environment from development to production.
- They enable microservices architecture and facilitate scalable, distributed systems.
- Containers improve resource utilization compared to traditional virtual machines.

Common use cases:
- Microservices deployment
- Continuous Integration/Continuous Deployment (CI/CD) pipelines
- Scalable web applications
- Data processing and analytics pipelines

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import docker
import os
import json
from typing import Dict, List, Any

class DockerManager:
    def __init__(self):
        self.client = docker.from_env()
    
    def build_image(self, path: str, tag: str) -> docker.models.images.Image:
        """
        Build a Docker image from a Dockerfile.
        
        Args:
        - path (str): Path to the directory containing the Dockerfile.
        - tag (str): Tag for the new image.
        
        Returns:
        - docker.models.images.Image: The built Docker image.
        """
        return self.client.images.build(path=path, tag=tag)
    
    def run_container(self, image: str, command: str = None, ports: Dict[str, str] = None, 
                      volumes: Dict[str, Dict[str, str]] = None) -> docker.models.containers.Container:
        """
        Run a Docker container.
        
        Args:
        - image (str): Name of the Docker image to run.
        - command (str, optional): Command to run in the container.
        - ports (Dict[str, str], optional): Port mappings.
        - volumes (Dict[str, Dict[str, str]], optional): Volume mappings.
        
        Returns:
        - docker.models.containers.Container: The running Docker container.
        """
        return self.client.containers.run(image, command=command, ports=ports, volumes=volumes, detach=True)
    
    def list_containers(self) -> List[docker.models.containers.Container]:
        """
        List all running Docker containers.
        
        Returns:
        - List[docker.models.containers.Container]: List of running containers.
        """
        return self.client.containers.list()
    
    def stop_container(self, container_id: str) -> None:
        """
        Stop a running Docker container.
        
        Args:
        - container_id (str): ID of the container to stop.
        """
        container = self.client.containers.get(container_id)
        container.stop()
    
    def remove_container(self, container_id: str) -> None:
        """
        Remove a Docker container.
        
        Args:
        - container_id (str): ID of the container to remove.
        """
        container = self.client.containers.get(container_id)
        container.remove()
    
    def get_container_logs(self, container_id: str) -> str:
        """
        Get logs from a Docker container.
        
        Args:
        - container_id (str): ID of the container to get logs from.
        
        Returns:
        - str: Container logs.
        """
        container = self.client.containers.get(container_id)
        return container.logs().decode('utf-8')

def create_dockerfile(base_image: str, commands: List[str]) -> str:
    """
    Create a Dockerfile as a string.
    
    Args:
    - base_image (str): Base image for the Dockerfile.
    - commands (List[str]): List of commands to include in the Dockerfile.
    
    Returns:
    - str: Dockerfile contents as a string.
    """
    dockerfile = f"FROM {base_image}\n"
    for command in commands:
        dockerfile += f"{command}\n"
    return dockerfile

def write_dockerfile(path: str, content: str) -> None:
    """
    Write a Dockerfile to disk.
    
    Args:
    - path (str): Path to write the Dockerfile.
    - content (str): Content of the Dockerfile.
    """
    with open(os.path.join(path, 'Dockerfile'), 'w') as f:
        f.write(content)

def demonstrate_docker_basics():
    """Demonstrate basic Docker operations using Python."""
    docker_manager = DockerManager()
    
    # Create a simple Dockerfile
    dockerfile_content = create_dockerfile(
        "python:3.9-slim",
        [
            "WORKDIR /app",
            "COPY . /app",
            "RUN pip install -r requirements.txt",
            "CMD [\"python\", \"app.py\"]"
        ]
    )
    
    # Write Dockerfile to disk
    write_dockerfile("./my_app", dockerfile_content)
    
    # Build Docker image
    image, _ = docker_manager.build_image("./my_app", "my-python-app:v1")
    print(f"Built image: {image.tags}")
    
    # Run Docker container
    container = docker_manager.run_container("my-python-app:v1", ports={'5000/tcp': '5000'})
    print(f"Running container: {container.id}")
    
    # List containers
    containers = docker_manager.list_containers()
    print("Running containers:")
    for c in containers:
        print(f"- {c.id}: {c.name}")
    
    # Get container logs
    logs = docker_manager.get_container_logs(container.id)
    print(f"Container logs:\n{logs}")
    
    # Stop and remove container
    docker_manager.stop_container(container.id)
    docker_manager.remove_container(container.id)
    print(f"Stopped and removed container: {container.id}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use minimal base images to reduce image size and attack surface.
2. Leverage multi-stage builds to separate build and runtime environments.
3. Use .dockerignore to exclude unnecessary files from the build context.
4. Pin specific versions of base images and dependencies for reproducibility.
5. Run containers with least privileges and as non-root users when possible.

Common Pitfalls:
1. Ignoring security in container images and runtime environments.
2. Not properly managing secrets and sensitive data in Docker images.
3. Overlooking proper resource management and limits for containers.
4. Neglecting to clean up unused images and containers, leading to disk space issues.

Advanced Tips:
1. Implement health checks for robust container orchestration.
2. Use Docker Compose for managing multi-container applications during development.
3. Leverage Docker's BuildKit for faster and more efficient image builds.
4. Implement proper logging and monitoring solutions for containerized applications.
"""

def create_optimized_dockerfile() -> str:
    """
    Create an optimized Dockerfile with best practices.
    
    Returns:
    - str: Optimized Dockerfile contents.
    """
    return """
# Stage 1: Build environment
FROM python:3.9-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install Python dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime environment
FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files from builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Set PATH to include installed packages
ENV PATH=/root/.local/bin:$PATH

# Run as non-root user
RUN useradd -m myuser
USER myuser

# Set health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the application
CMD ["python", "app.py"]
"""

def demonstrate_advanced_docker_usage():
    """Demonstrate advanced Docker usage and best practices."""
    optimized_dockerfile = create_optimized_dockerfile()
    print("Optimized Dockerfile:")
    print(optimized_dockerfile)
    
    # In a real scenario, you would build and run this optimized Dockerfile

"""
4. Integration and Real-World Applications
------------------------------------------
Docker and containerization integrate with various DevOps tools and practices:

1. CI/CD: Docker containers are often used in CI/CD pipelines for consistent build and test environments.
2. Orchestration: Tools like Kubernetes manage container deployment, scaling, and networking in production.
3. Microservices: Containers enable efficient deployment and scaling of microservices architectures.
4. Serverless: Some serverless platforms use containers to run functions in isolated environments.

Real-world example: Deploying a Python web application with Docker
"""

def create_flask_app() -> str:
    """
    Create a simple Flask application for demonstration.
    
    Returns:
    - str: Flask application code.
    """
    return """
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, Docker!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
"""

def create_docker_compose_file() -> str:
    """
    Create a Docker Compose file for the Flask application.
    
    Returns:
    - str: Docker Compose file contents.
    """
    return """
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    restart: always
"""

def demonstrate_real_world_application():
    """Demonstrate a real-world application deployment using Docker."""
    # Create Flask app
    flask_app = create_flask_app()
    with open('app.py', 'w') as f:
        f.write(flask_app)
    
    # Create requirements.txt
    with open('requirements.txt', 'w') as f:
        f.write('Flask==2.0.1')
    
    # Create Dockerfile
    dockerfile = create_optimized_dockerfile()
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile)
    
    # Create Docker Compose file
    docker_compose = create_docker_compose_file()
    with open('docker-compose.yml', 'w') as f:
        f.write(docker_compose)
    
    print("Created Flask app, Dockerfile, and Docker Compose file.")
    print("To build and run the application, use:")
    print("docker-compose up --build")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Container Security: Advanced scanning tools and runtime security measures for containers.
2. Serverless Containers: Platforms like AWS Fargate and Google Cloud Run for running containers without managing infrastructure.
3. Service Mesh: Technologies like Istio for advanced networking, security, and observability in containerized environments.
4. WebAssembly: Potential future alternative to containers for portable, sandboxed execution environments.
"""

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I optimize Docker image size?
A: Use multi-stage builds, minimal base images, and clean up unnecessary files in each layer.

Q: How can I manage secrets in Docker containers?
A: Use Docker secrets for swarm mode or external secret management systems like HashiCorp Vault.

Q: What's the difference between Docker Compose and Kubernetes?
A: Docker Compose is for defining and running multi-container applications on a single host, while Kubernetes is for orchestrating containerized applications across multiple hosts.

Troubleshooting:
1. Container exits immediately: Check the CMD/ENTRYPOINT in Dockerfile and ensure the application doesn't exit.
2. Can't connect to container: Verify port mappings and network settings.
3. Out of disk space: Regularly prune unused images, containers, and volumes with `docker system prune`.
"""

def troubleshoot_container(container_id: str) -> Dict[str, Any]:
    """
    Troubleshoot a Docker container by gathering relevant information.
    
    Args:
    - container_id (str): ID of the container to troubleshoot.
    
    Returns:
    - Dict[str, Any]: Troubleshooting information.
    """
    docker_manager = DockerManager()
    container = docker_manager.client.containers.get(container_id)
    
    return {
        "status": container.status,
        "logs": container.logs().decode('utf-8'),
        "inspect": container.attrs,
        "stats": next(container.stats(stream=False))
    }

def demonstrate_troubleshooting():
    """Demonstrate container troubleshooting."""
    # This is a simulated troubleshooting scenario
    sample_container_id = "sample_container_123"
    troubleshooting_info = troubleshoot_container(sample_container_id)
    
    print("Container Troubleshooting Information:")
    print(json.dumps(troubleshooting_info, indent=2))

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. Docker SDK for Python: For programmatic interaction with Docker.
2. docker-compose: For defining and running multi-container Docker applications.
3. Dive: A tool for exploring Docker image layers.
4. Portainer: Web UI for managing Docker environments.

Resources:
- "Docker in Practice" by Ian Miell and Aidan Hobson Sayers
- "Using Docker" by Adrian Mouat
- Official Docker Documentation: https://docs.docker.com/
- Docker Best Practices Guide: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Docker Security Guide: https://docs.docker.com/engine/security/security/
"""

"""
8. Performance Analysis and Optimization
----------------------------------------
When working with Docker containers, performance optimization is crucial for efficient resource utilization and scalability.
"""

def analyze_container_performance(container_id: str, duration: int = 60) -> Dict[str, Any]:
    """
    Analyze the performance of a Docker container over a specified duration.
    
    Args:
    - container_id (str): ID of the container to analyze.
    - duration (int): Duration of analysis in seconds.
    
    Returns:
    - Dict[str, Any]: Performance metrics of the container.
    """
    docker_manager = DockerManager()
    container = docker_manager.client.containers.get(container_id)
    
    stats = list(container.stats(stream=True, decode=True))
    cpu_usage = []
    memory_usage = []
    
    for stat in stats[:duration]:
        cpu_percent = calculate_cpu_percent(stat)
        memory_usage_mb = stat['memory_stats']['usage'] / (1024 * 1024)
        
        cpu_usage.append(cpu_percent)
        memory_usage.append(memory_usage_mb)
    
    return {
        "avg_cpu_usage": sum(cpu_usage) / len(cpu_usage),
        "max_cpu_usage": max(cpu_usage),
        "avg_memory_usage_mb": sum(memory_usage) / len(memory_usage),
        "max_memory_usage_mb": max(memory_usage)
    }

def calculate_cpu_percent(stat: Dict[str, Any]) -> float:
    """
    Calculate CPU usage percentage from Docker stats.
    
    Args:
    - stat (Dict[str, Any]): Docker stats for a single time point.
    
    Returns:
    - float: CPU usage percentage.
    """
    cpu_delta = stat['cpu_stats']['cpu_usage']['total_usage'] - stat['precpu_stats']['cpu_usage']['total_usage']
    system_delta = stat['cpu_stats']['system_cpu_usage'] - stat['precpu_stats']['system_cpu_usage']
    num_cpus = stat['cpu_stats']['online_cpus']
    
    cpu_percent = (cpu_delta / system_delta) * num_cpus * 100.0
    return round(cpu_percent, 2)

def optimize_container_resource_usage(container_id: str, cpu_limit: str, memory_limit: str) -> None:
    """
    Optimize container resource usage by setting CPU and memory limits.
    
    Args:
    - container_id (str): ID of the container to optimize.
    - cpu_limit (str): CPU limit (e.g., '0.5' for 50% of a CPU core).
    - memory_limit (str): Memory limit (e.g., '512m' for 512 MB).
    """
    docker_manager = DockerManager()
    container = docker_manager.client.containers.get(container_id)
    
    container.update(cpu_quota=int(float(cpu_limit) * 100000), memory=memory_limit)
    print(f"Container {container_id} resource limits updated: CPU={cpu_limit}, Memory={memory_limit}")

def demonstrate_performance_optimization():
    """Demonstrate container performance analysis and optimization."""
    # This is a simulated performance optimization scenario
    sample_container_id = "sample_container_456"
    
    print("Analyzing container performance...")
    performance_metrics = analyze_container_performance(sample_container_id)
    print("Performance Metrics:")
    print(json.dumps(performance_metrics, indent=2))
    
    print("\nOptimizing container resource usage...")
    optimize_container_resource_usage(sample_container_id, cpu_limit="0.5", memory_limit="512m")
    
    print("\nRe-analyzing container performance after optimization...")
    optimized_metrics = analyze_container_performance(sample_container_id)
    print("Optimized Performance Metrics:")
    print(json.dumps(optimized_metrics, indent=2))

"""
Performance Considerations:
1. Use appropriate base images to minimize container size and startup time.
2. Optimize Dockerfile to reduce the number of layers and overall image size.
3. Implement proper resource limits to prevent container resource contention.
4. Use volume mounts for persistent data to improve I/O performance.
5. Consider using Docker's '--read-only' flag to improve security and potentially performance.

Optimization Strategies:
1. Implement multi-stage builds to separate build and runtime environments.
2. Use Docker's BuildKit for faster and more efficient image builds.
3. Leverage Docker layer caching to speed up builds and deployments.
4. Implement proper logging strategies to minimize I/O overhead.
5. Use Docker networks effectively to optimize inter-container communication.

Example of optimizing a Dockerfile for a Python application:
"""

def create_optimized_python_dockerfile() -> str:
    """
    Create an optimized Dockerfile for a Python application.
    
    Returns:
    - str: Optimized Dockerfile contents.
    """
    return """
# Stage 1: Build dependencies
FROM python:3.9-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install Python dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files from builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Set PATH to include installed packages
ENV PATH=/root/.local/bin:$PATH

# Run as non-root user
RUN useradd -m myuser
USER myuser

# Set environment variables
ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    PIP_NO_CACHE_DIR=off \\
    PIP_DISABLE_PIP_VERSION_CHECK=on \\
    PYTHONPATH=/app

# Expose port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
"""

def demonstrate_dockerfile_optimization():
    """Demonstrate Dockerfile optimization for a Python application."""
    optimized_dockerfile = create_optimized_python_dockerfile()
    print("Optimized Dockerfile for Python Application:")
    print(optimized_dockerfile)
    
    print("\nKey Optimization Points:")
    print("1. Multi-stage build to separate build and runtime environments.")
    print("2. Minimal base image (python:3.9-slim) to reduce image size.")
    print("3. Installation of only necessary build dependencies.")
    print("4. Copying only required files from the builder stage.")
    print("5. Running as a non-root user for improved security.")
    print("6. Setting environment variables to optimize Python behavior.")
    print("7. Using Gunicorn as a production-ready WSGI server.")

"""
9. How to Contribute
--------------------
To contribute to this note sheet:
1. Fork the repository containing this file.
2. Make your changes or additions.
3. Ensure all code examples are correct and follow the established style.
4. Add comments explaining new concepts or functions.
5. Update the Table of Contents if necessary.
6. Submit a pull request with a clear description of your changes.

Guidelines for contributions:
- Maintain the current format and style.
- Provide working code examples for new concepts.
- Include performance considerations for new functions.
- Add relevant references or citations for advanced topics.

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of Docker and containerization in Python for DevOps.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Docker features and best practices.

Your contributions help keep this resource valuable for DevOps engineers and developers working with Python and Docker. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to Docker and containerization in Python for DevOps.
    """
    print("Demonstrating Docker Basics:")
    demonstrate_docker_basics()
    
    print("\nDemonstrating Advanced Docker Usage:")
    demonstrate_advanced_docker_usage()
    
    print("\nDemonstrating Real-World Application Deployment:")
    demonstrate_real_world_application()
    
    print("\nDemonstrating Container Troubleshooting:")
    demonstrate_troubleshooting()
    
    print("\nDemonstrating Performance Optimization:")
    demonstrate_performance_optimization()
    
    print("\nDemonstrating Dockerfile Optimization:")
    demonstrate_dockerfile_optimization()

if __name__ == "__main__":
    main()