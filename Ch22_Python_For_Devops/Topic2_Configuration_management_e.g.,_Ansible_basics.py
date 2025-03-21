"""
Python for DevOps - Configuration Management (Ansible Basics) - in the Python Programming Language
==================================================================================================

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
Configuration management is a critical aspect of DevOps, enabling the automation of infrastructure provisioning and application deployment. Ansible, written in Python, is a popular configuration management tool that allows for infrastructure as code (IaC) and automated configuration management.

Historical context:
- Ansible was created by Michael DeHaan in 2012.
- It was acquired by Red Hat in 2015, accelerating its adoption in enterprise environments.
- Ansible's design philosophy emphasizes simplicity, agentless architecture, and idempotency.

Significance:
- Ansible simplifies complex IT workflows and makes it easy to deploy multi-tier applications.
- It uses YAML for defining configurations, making it human-readable and easy to learn.
- Being agentless, Ansible only requires SSH access to manage nodes, reducing overhead.

Common use cases:
- Server provisioning and configuration
- Application deployment
- Continuous delivery
- Security compliance automation

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import ansible_runner
import yaml
from typing import Dict, List, Any

def run_ansible_playbook(playbook_path: str, inventory_path: str, extra_vars: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Run an Ansible playbook using ansible-runner.
    
    Args:
    - playbook_path (str): Path to the Ansible playbook YAML file.
    - inventory_path (str): Path to the inventory file.
    - extra_vars (Dict[str, Any], optional): Additional variables to pass to the playbook.
    
    Returns:
    - Dict[str, Any]: Result of the playbook execution.
    """
    r = ansible_runner.run(playbook=playbook_path, inventory=inventory_path, extravars=extra_vars)
    return {"status": r.status, "rc": r.rc, "events": r.events}

def create_ansible_playbook(tasks: List[Dict[str, Any]], hosts: str = "all") -> str:
    """
    Create a simple Ansible playbook from a list of tasks.
    
    Args:
    - tasks (List[Dict[str, Any]]): List of Ansible tasks.
    - hosts (str, optional): Target hosts for the playbook. Defaults to "all".
    
    Returns:
    - str: YAML representation of the Ansible playbook.
    """
    playbook = [{
        "name": "Generated Playbook",
        "hosts": hosts,
        "tasks": tasks
    }]
    return yaml.dump(playbook)

def demonstrate_ansible_basics():
    """Demonstrate basic Ansible concepts using Python."""
    
    # Example: Creating a simple Ansible playbook
    tasks = [
        {
            "name": "Ensure nginx is installed",
            "apt": {"name": "nginx", "state": "present"},
            "become": True
        },
        {
            "name": "Start nginx service",
            "service": {"name": "nginx", "state": "started"},
            "become": True
        }
    ]
    
    playbook_yaml = create_ansible_playbook(tasks)
    print("Generated Ansible Playbook:")
    print(playbook_yaml)
    
    # Example: Running an Ansible playbook
    # Note: This is a simulated run, as actual execution requires proper setup
    playbook_path = "/path/to/playbook.yml"
    inventory_path = "/path/to/inventory"
    extra_vars = {"env": "production"}
    
    print("\nSimulating Ansible Playbook Execution:")
    result = run_ansible_playbook(playbook_path, inventory_path, extra_vars)
    print(f"Execution Status: {result['status']}")
    print(f"Return Code: {result['rc']}")
    print(f"Number of Events: {len(result['events'])}")

def create_dynamic_inventory(hosts: List[Dict[str, Any]]) -> str:
    """
    Create a dynamic Ansible inventory in YAML format.
    
    Args:
    - hosts (List[Dict[str, Any]]): List of host configurations.
    
    Returns:
    - str: YAML representation of the Ansible inventory.
    """
    inventory = {"all": {"hosts": {}}}
    for host in hosts:
        inventory["all"]["hosts"][host["name"]] = host["vars"]
    return yaml.dump(inventory)

def demonstrate_dynamic_inventory():
    """Demonstrate creating and using a dynamic Ansible inventory."""
    
    hosts = [
        {"name": "web1.example.com", "vars": {"ansible_host": "192.168.1.101", "http_port": 80}},
        {"name": "db1.example.com", "vars": {"ansible_host": "192.168.1.102", "db_port": 5432}}
    ]
    
    inventory_yaml = create_dynamic_inventory(hosts)
    print("Generated Dynamic Inventory:")
    print(inventory_yaml)
    
    # In a real scenario, you would write this to a file and use it with Ansible
    # or pass it directly to ansible-runner

def create_ansible_role_structure(role_name: str) -> None:
    """
    Create the directory structure for an Ansible role.
    
    Args:
    - role_name (str): Name of the Ansible role.
    """
    import os
    
    base_path = f"roles/{role_name}"
    directories = [
        "defaults", "files", "handlers", "meta", "tasks", "templates", "vars"
    ]
    
    for directory in directories:
        os.makedirs(f"{base_path}/{directory}", exist_ok=True)
    
    # Create a sample main.yml in tasks
    with open(f"{base_path}/tasks/main.yml", "w") as f:
        f.write("---\n# Tasks for role {role_name}\n")
    
    print(f"Ansible role structure created for '{role_name}'")

def demonstrate_ansible_role_creation():
    """Demonstrate creating an Ansible role structure."""
    
    create_ansible_role_structure("webserver")
    
    print("\nAnsible Role Structure:")
    print("roles/")
    print("└── webserver")
    print("    ├── defaults")
    print("    ├── files")
    print("    ├── handlers")
    print("    ├── meta")
    print("    ├── tasks")
    print("    │   └── main.yml")
    print("    ├── templates")
    print("    └── vars")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use version control for your Ansible playbooks and roles.
2. Keep playbooks and roles idempotent to ensure consistent results.
3. Use Ansible Vault for managing sensitive data.
4. Organize complex deployments using roles and include statements.
5. Use tags to selectively run parts of your playbooks.

Common Pitfalls:
1. Forgetting to quote variables that start with numbers.
2. Not handling errors properly in playbooks.
3. Overusing command and shell modules instead of dedicated modules.
4. Ignoring the importance of proper inventory management.

Advanced Tips:
1. Use Ansible Tower or AWX for centralized automation management.
2. Implement custom Ansible modules for specialized tasks.
3. Leverage dynamic inventories for cloud environments.
4. Use Ansible's async capabilities for long-running operations.
"""

def demonstrate_ansible_vault():
    """Demonstrate using Ansible Vault for encrypting sensitive data."""
    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    from ansible.parsing.vault import VaultLib, VaultSecret
    
    def encrypt_string(secret_string: str, vault_password: str) -> str:
        """Encrypt a string using Ansible Vault."""
        vault = VaultLib([(DEFAULT_VAULT_ID_MATCH, VaultSecret(vault_password.encode()))])
        return vault.encrypt(secret_string.encode()).decode()
    
    def decrypt_string(encrypted_string: str, vault_password: str) -> str:
        """Decrypt a string using Ansible Vault."""
        vault = VaultLib([(DEFAULT_VAULT_ID_MATCH, VaultSecret(vault_password.encode()))])
        return vault.decrypt(encrypted_string.encode()).decode()
    
    # Example usage
    secret = "my_secret_password"
    vault_password = "vault_password"
    
    encrypted = encrypt_string(secret, vault_password)
    print(f"Encrypted secret: {encrypted}")
    
    decrypted = decrypt_string(encrypted, vault_password)
    print(f"Decrypted secret: {decrypted}")

"""
4. Integration and Real-World Applications
------------------------------------------
Ansible integrates well with various DevOps tools and practices:

1. CI/CD Pipelines: Ansible can be used in Jenkins, GitLab CI, or GitHub Actions for automated deployments.
2. Cloud Providers: Ansible has modules for AWS, Azure, GCP, and others, allowing for cloud infrastructure management.
3. Container Orchestration: While Kubernetes is often used for container orchestration, Ansible can complement it for initial cluster setup and management.
4. Monitoring Tools: Ansible can be used to deploy and configure monitoring solutions like Prometheus and Grafana.

Real-world example: Automating a web application deployment
"""

def create_web_app_deployment_playbook() -> str:
    """Create an Ansible playbook for deploying a web application."""
    playbook = [
        {
            "name": "Deploy Web Application",
            "hosts": "webservers",
            "become": True,
            "vars": {
                "app_repo": "https://github.com/example/web-app.git",
                "app_version": "v1.2.3",
                "app_dir": "/var/www/myapp"
            },
            "tasks": [
                {
                    "name": "Ensure required packages are installed",
                    "apt": {
                        "name": ["nginx", "git", "python3", "python3-pip"],
                        "state": "present"
                    }
                },
                {
                    "name": "Clone application repository",
                    "git": {
                        "repo": "{{ app_repo }}",
                        "version": "{{ app_version }}",
                        "dest": "{{ app_dir }}"
                    }
                },
                {
                    "name": "Install Python dependencies",
                    "pip": {
                        "requirements": "{{ app_dir }}/requirements.txt"
                    }
                },
                {
                    "name": "Configure Nginx",
                    "template": {
                        "src": "nginx_config.j2",
                        "dest": "/etc/nginx/sites-available/myapp"
                    }
                },
                {
                    "name": "Enable Nginx configuration",
                    "file": {
                        "src": "/etc/nginx/sites-available/myapp",
                        "dest": "/etc/nginx/sites-enabled/myapp",
                        "state": "link"
                    }
                },
                {
                    "name": "Start Nginx",
                    "service": {
                        "name": "nginx",
                        "state": "restarted"
                    }
                }
            ]
        }
    ]
    return yaml.dump(playbook)

def demonstrate_web_app_deployment():
    """Demonstrate creating a web application deployment playbook."""
    playbook_yaml = create_web_app_deployment_playbook()
    print("Web Application Deployment Playbook:")
    print(playbook_yaml)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Ansible Collections: Distributable and shareable units of Ansible content.
2. Ansible Automation Platform: Red Hat's enterprise solution for scaling automation.
3. AnsibleFest: Annual conference showcasing Ansible developments and use cases.
4. Ansible and AI/ML: Emerging trends in using Ansible for ML model deployment and AI infrastructure management.
"""

def demonstrate_ansible_collection():
    """Demonstrate the structure of an Ansible Collection."""
    collection_structure = {
        "ansible_collections/": {
            "mycompany/": {
                "myapp/": {
                    "roles/": {
                        "webserver/": {},
                        "database/": {}
                    },
                    "playbooks/": {
                        "site.yml": "# Main playbook"
                    },
                    "plugins/": {
                        "modules/": {
                            "custom_module.py": "# Custom module code"
                        },
                        "filter/": {
                            "custom_filter.py": "# Custom filter code"
                        }
                    },
                    "README.md": "# Collection documentation",
                    "galaxy.yml": "# Collection metadata"
                }
            }
        }
    }
    
    def print_structure(structure, indent=0):
        for key, value in structure.items():
            print("  " * indent + str(key))
            if isinstance(value, dict):
                print_structure(value, indent + 1)
            elif value:
                print("  " * (indent + 1) + value)
    
    print("Ansible Collection Structure:")
    print_structure(collection_structure)

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do I handle different environments (dev, staging, production) in Ansible?
A: Use inventory groups and group_vars to define environment-specific variables.

Q: What's the difference between `copy` and `template` modules?
A: `copy` transfers files as-is, while `template` processes Jinja2 templates before copying.

Q: How can I speed up Ansible playbook execution?
A: Use `async` tasks, optimize your inventory, and leverage fact caching.

Troubleshooting:
1. Use `ansible-playbook --check` for dry runs to catch issues before actual execution.
2. Increase verbosity with `-v`, `-vv`, or `-vvv` flags for detailed output.
3. Use `ansible-playbook --start-at-task` to resume playbook execution from a specific task.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. ansible-lint: For linting Ansible playbooks and roles.
2. Molecule: For testing Ansible roles.
3. ansible-runner: For programmatic execution of Ansible from Python.
4. AWX: Open-source version of Ansible Tower for web-based management.

Resources:
- "Ansible for DevOps" by Jeff Geerling
- "Ansible: Up and Running" by Lorin Hochstein and René Moser
- Official Ansible Documentation: https://docs.ansible.com/
- Ansible Galaxy: https://galaxy.ansible.com/ (for community roles and collections)
- AnsibleFest presentations: https://www.ansible.com/resources/videos

8. Performance Analysis and Optimization
----------------------------------------
When working with Ansible, especially in large-scale deployments, performance becomes crucial.
"""

def analyze_ansible_performance(playbook_path: str, inventory_path: str) -> Dict[str, Any]:
    """
    Analyze the performance of an Ansible playbook execution.
    
    Args:
    - playbook_path (str): Path to the Ansible playbook.
    - inventory_path (str): Path to the inventory file.
    
    Returns:
    - Dict[str, Any]: Performance metrics of the playbook execution.
    """
    import time
    import ansible_runner
    
    start_time = time.time()
    r = ansible_runner.run(playbook=playbook_path, inventory=inventory_path, quiet=True)
    end_time = time.time()
    
    total_duration = end_time - start_time
    task_durations = [event['event_data'].get('duration', {}).get('total') for event in r.events if event['event'] == 'runner_on_ok']
    
    return {
        "total_duration": total_duration,
        "task_count": len(task_durations),
        "average_task_duration": sum(task_durations) / len(task_durations) if task_durations else 0,
        "slowest_task": max(task_durations) if task_durations else 0,
        "fastest_task": min(task_durations) if task_durations else 0
    }

def optimize_ansible_playbook(playbook_path: str) -> str:
    """
    Optimize an Ansible playbook for better performance.
    
    Args:
    - playbook_path (str): Path to the Ansible playbook.
    
    Returns:
    - str: Optimized version of the playbook.
    """
    with open(playbook_path, 'r') as f:
        playbook = yaml.safe_load(f)
    
    optimized_playbook = []
    for play in playbook:
        optimized_play = play.copy()
        optimized_tasks = []
        for task in play.get('tasks', []):
            # Example optimization: Use 'package' module instead of distribution-specific modules
            if 'apt' in task:
                task['package'] = task.pop('apt')
            elif 'yum' in task:
                task['package'] = task.pop('yum')
            
            # Example optimization: Add 'async' to long-running tasks
            if task.get('command') or task.get('shell'):
                task['async'] = 3600
                task['poll'] = 0
            
            optimized_tasks.append(task)
        
        optimized_play['tasks'] = optimized_tasks
        optimized_playbook.append(optimized_play)
    
    return yaml.dump(optimized_playbook)

def demonstrate_performance_optimization():
    """Demonstrate Ansible performance analysis and optimization."""
    playbook_path = "/path/to/sample_playbook.yml"
    inventory_path = "/path/to/inventory"
    
    print("Analyzing Ansible Playbook Performance:")
    performance_metrics = analyze_ansible_performance(playbook_path, inventory_path)
    print(f"Total Duration: {performance_metrics['total_duration']:.2f} seconds")
    print(f"Number of Tasks: {performance_metrics['task_count']}")
    print(f"Average Task Duration: {performance_metrics['average_task_duration']:.2f} seconds")
    print(f"Slowest Task Duration: {performance_metrics['slowest_task']:.2f} seconds")
    print(f"Fastest Task Duration: {performance_metrics['fastest_task']:.2f} seconds")
    
    print("\nOptimizing Ansible Playbook:")
    optimized_playbook = optimize_ansible_playbook(playbook_path)
    print(optimized_playbook)

"""
Performance Considerations:
1. Use `async` and `poll` for long-running tasks to run them in parallel.
2. Leverage `serial` to control the number of hosts being configured simultaneously.
3. Use the `free` strategy for tasks that don't depend on each other.
4. Optimize your inventory by using dynamic inventories and grouping hosts efficiently.
5. Use `gather_facts: false` when fact gathering is not necessary.

Optimization Strategies:
1. Use the appropriate Ansible modules instead of shell/command modules when possible.
2. Minimize the number of tasks by combining related operations.
3. Use roles to organize and reuse code efficiently.
4. Leverage Ansible's built-in caching mechanisms for fact caching.
5. Use `delegate_to` and `run_once` for tasks that only need to run on a single host.

Example of optimizing a frequently called task:
"""

def optimize_package_installation():
    """Demonstrate optimizing package installation in Ansible."""
    unoptimized_task = {
        "name": "Install packages",
        "apt": {
            "name": ["nginx", "postgresql", "redis-server"],
            "state": "present"
        },
        "become": True
    }
    
    optimized_task = {
        "name": "Install packages",
        "package": {
            "name": ["nginx", "postgresql", "redis-server"],
            "state": "present"
        },
        "become": True,
        "async": 3600,
        "poll": 0
    }
    
    print("Unoptimized Task:")
    print(yaml.dump(unoptimized_task))
    
    print("\nOptimized Task:")
    print(yaml.dump(optimized_task))
    
    print("\nOptimization Explanation:")
    print("1. Changed 'apt' to 'package' for better cross-platform compatibility.")
    print("2. Added 'async' and 'poll' to allow for parallel execution.")

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
- Relevance to the main topic of Python for DevOps and Ansible basics.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Ansible features and best practices.

Your contributions help keep this resource valuable for DevOps engineers and system administrators working with Python and Ansible. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to Python for DevOps and Ansible basics.
    """
    print("Demonstrating Ansible Basics:")
    demonstrate_ansible_basics()
    
    print("\nDemonstrating Dynamic Inventory:")
    demonstrate_dynamic_inventory()
    
    print("\nDemonstrating Ansible Role Creation:")
    demonstrate_ansible_role_creation()
    
    print("\nDemonstrating Ansible Vault Usage:")
    demonstrate_ansible_vault()
    
    print("\nDemonstrating Web Application Deployment:")
    demonstrate_web_app_deployment()
    
    print("\nDemonstrating Ansible Collection Structure:")
    demonstrate_ansible_collection()
    
    print("\nDemonstrating Performance Optimization:")
    demonstrate_performance_optimization()
    
    print("\nDemonstrating Package Installation Optimization:")
    optimize_package_installation()

if __name__ == "__main__":
    main()