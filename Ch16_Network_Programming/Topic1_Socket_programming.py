# Network Programming - Socket Programming - in the Python Programming Language
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

import socket
import threading
import select
import ssl
import time
import asyncio
import logging
from typing import List, Tuple, Optional

# 1. Overview and Historical Context
# ----------------------------------
# Socket programming is a fundamental technique for network communication,
# allowing applications to send and receive data over networks using sockets.

# Historical context:
# - Sockets were introduced in BSD UNIX in the early 1980s.
# - Python's socket module, based on BSD sockets, has been part of the standard library since its early versions.
# - The concept of sockets originates from ARPANET and early internet protocols.

# Significance:
# - Provides low-level network communication capabilities.
# - Forms the basis for higher-level network protocols and libraries.
# - Enables the development of client-server applications and distributed systems.

# Common use cases:
# - Web servers and clients
# - Chat applications
# - File transfer protocols
# - Network monitoring tools
# - Custom network protocols

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic TCP Server
def basic_tcp_server():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

# Basic TCP Client
def basic_tcp_client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello, server")
        data = s.recv(1024)
    print(f"Received {data!r}")

# UDP Server
def udp_server():
    host = '127.0.0.1'
    port = 65433

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP server listening on {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"Received message from {addr}: {data.decode()}")
            s.sendto(b"Message received", addr)

# UDP Client
def udp_client():
    host = '127.0.0.1'
    port = 65433

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hello, UDP server", (host, port))
        data, _ = s.recvfrom(1024)
    print(f"Received {data.decode()}")

# Multi-threaded TCP Server
class ThreadedTCPServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.handle_client, args=(client, address)).start()

    def handle_client(self, client: socket.socket, address: Tuple[str, int]):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    response = f"Server received: {data.decode()}"
                    client.send(response.encode())
                else:
                    raise ConnectionError('Client disconnected')
            except ConnectionError:
                client.close()
                return False

# Non-blocking I/O with select
def non_blocking_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind(('localhost', 50000))
    server.listen(5)
    inputs = [server]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = []
            else:
                data = s.recv(1024)
                if data:
                    message_queues[s].append(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]

        for s in writable:
            try:
                next_msg = message_queues[s].pop(0)
            except IndexError:
                outputs.remove(s)
            else:
                s.send(next_msg)

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]

# SSL/TLS Socket Example
def ssl_client():
    hostname = 'www.python.org'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
            print(f"Cipher used: {secure_sock.cipher()}")
            secure_sock.send(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
            response = secure_sock.recv(1024)
            print(f"Response: {response.decode()}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Always use context managers (with statements) for sockets to ensure proper cleanup.
# 2. Set appropriate timeouts to prevent hanging connections.
# 3. Use non-blocking sockets and asynchronous I/O for scalable applications.
# 4. Implement proper error handling and logging for network operations.
# 5. Use SSL/TLS for secure communications when dealing with sensitive data.

# Common Pitfalls:
# 1. Not handling network errors and exceptions properly.
# 2. Blocking indefinitely on socket operations without timeouts.
# 3. Not considering platform-specific socket behaviors.
# 4. Failing to properly close sockets, leading to resource leaks.
# 5. Ignoring buffer sizes and potential data fragmentation.

# Advanced Tips:
# 1. Use socket options to fine-tune performance (e.g., TCP_NODELAY, SO_KEEPALIVE).
# 2. Implement custom protocols on top of raw sockets for specialized applications.
# 3. Utilize non-blocking I/O and event loops for high-performance servers.
# 4. Consider using higher-level libraries (e.g., asyncio) for complex networking tasks.
# 5. Implement proper connection pooling for client applications.

# Example: Custom Protocol Implementation
class CustomProtocol:
    def __init__(self, sock: socket.socket):
        self.sock = sock

    def send_message(self, message: str):
        # Prefix each message with a 4-byte length field
        length = len(message).to_bytes(4, byteorder='big')
        self.sock.sendall(length + message.encode())

    def receive_message(self) -> Optional[str]:
        # Read the 4-byte length field
        length_bytes = self.sock.recv(4)
        if not length_bytes:
            return None
        length = int.from_bytes(length_bytes, byteorder='big')
        # Read the actual message
        message = self.sock.recv(length).decode()
        return message

# 4. Integration and Real-World Applications
# ------------------------------------------
# Socket programming is fundamental in various network applications:

# 1. Web servers (e.g., Nginx, Apache)
# 2. Database servers (e.g., PostgreSQL, MySQL)
# 3. Chat applications and instant messaging protocols
# 4. Email servers and clients (SMTP, POP3, IMAP)
# 5. File transfer protocols (FTP, SFTP)

# Real-world example: Simple HTTP Server
def simple_http_server():
    host = 'localhost'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Serving on {host}:{port}")

    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        print(f"Received request from {client_address}:\n{request}")

        response = "HTTP/1.1 200 OK\n\nHello, World!"
        client_connection.sendall(response.encode())
        client_connection.close()

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Asynchronous I/O with asyncio for high-performance networking
# 2. QUIC protocol as a modern alternative to TCP+TLS+HTTP2
# 3. WebSockets for real-time, full-duplex communication
# 4. gRPC for efficient, cross-platform RPC
# 5. Network function virtualization (NFV) and software-defined networking (SDN)

# Example: Asynchronous Socket Server with asyncio
async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    message = f"Hello {addr}\n"
    writer.write(message.encode())
    await writer.drain()

    while True:
        data = await reader.readline()
        if not data:
            break
        message = data.decode().strip()
        writer.write(f"Echo: {message}\n".encode())
        await writer.drain()

    print(f"Closed connection from {addr}")
    writer.close()

async def async_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: How do I handle connection timeouts?
# A: Use socket.settimeout() or non-blocking sockets with select:

def timeout_example():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # 5 second timeout
    try:
        sock.connect(('example.com', 80))
    except socket.timeout:
        print("Connection timed out")

# Q: How can I implement a simple port scanner?
# A: Use a loop to attempt connections to different ports:

def port_scanner(host: str, start_port: int, end_port: int):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Q: How do I handle large amounts of data?
# A: Use a loop to send or receive data in chunks:

def send_large_data(sock: socket.socket, data: bytes):
    CHUNK_SIZE = 4096
    for i in range(0, len(data), CHUNK_SIZE):
        chunk = data[i:i+CHUNK_SIZE]
        sock.sendall(chunk)

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. Wireshark: Network protocol analyzer
# 2. tcpdump: Command-line packet analyzer
# 3. asyncio: Asynchronous I/O library in Python standard library
# 4. Twisted: Event-driven networking engine
# 5. Scapy: Packet manipulation library

# Resources:
# 1. "Unix Network Programming" by W. Richard Stevens
# 2. "Foundations of Python Network Programming" by Brandon Rhodes and John Goerzen
# 3. Python Socket Programming HOWTO: https://docs.python.org/3/howto/sockets.html
# 4. Beej's Guide to Network Programming: https://beej.us/guide/bgnet/
# 5. RFC 793 - Transmission Control Protocol: https://tools.ietf.org/html/rfc793

# 8. Performance Analysis and Optimization
# ----------------------------------------

def benchmark_socket_operations():
    def measure_time(func):
        start = time.time()
        func()
        end = time.time()
        return end - start

    def tcp_test():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('example.com', 80))
            s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
            s.recv(4096)

    def udp_test():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(b'Hello', ('example.com', 80))

    tcp_time = measure_time(tcp_test)
    udp_time = measure_time(udp_test)

    print(f"TCP operation time: {tcp_time:.6f} seconds")
    print(f"UDP operation time: {udp_time:.6f} seconds")

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
# - Add relevant # references or citations for advanced topics.

# When adding new sections or expanding existing ones, consider the following:
# - Relevance to the main topic of socket programming in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

def main():
    print("1. Basic TCP Server and Client")
    threading.Thread(target=basic_tcp_server).start()
    time.sleep(1)  # Give the server time to start
    basic_tcp_client()

    print("\n2. UDP Server and Client")
    threading.Thread(target=udp_server).start()
    time.sleep(1)  # Give the server time to start
    udp_client()

    print("\n3. Multi-threaded TCP Server")
    server = ThreadedTCPServer('localhost', 65434)
    server_thread = threading.Thread(target=server.listen)
    server_thread.start()
    time.sleep(1)  # Give the server time to start

    # Connect to the multi-threaded server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65434))
        s.sendall(b"Hello, multi-threaded server")
        data = s.recv(1024)
        print(f"Received from multi-threaded server: {data.decode()}")

    print("\n4. Non-blocking Server")
    threading.Thread(target=non_blocking_server).start()
    time.sleep(1)  # Give the server time to start

    # Connect to the non-blocking server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 50000))
        s.sendall(b"Hello, non-blocking server")
        data = s.recv(1024)
        print(f"Received from non-blocking server: {data.decode()}")

    print("\n5. SSL Client")
    ssl_client()

    print("\n6. Custom Protocol Example")
    # Create a server socket using the custom protocol
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('localhost', 65435))
    server_sock.listen(1)

    def custom_protocol_server():
        conn, addr = server_sock.accept()
        protocol = CustomProtocol(conn)
        message = protocol.receive_message()
        print(f"Server received: {message}")
        protocol.send_message("Hello from server")
        conn.close()

    server_thread = threading.Thread(target=custom_protocol_server)
    server_thread.start()
    time.sleep(1)  # Give the server time to start

    # Connect to the custom protocol server
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('localhost', 65435))
    client_protocol = CustomProtocol(client_sock)
    client_protocol.send_message("Hello from client")
    response = client_protocol.receive_message()
    print(f"Client received: {response}")
    client_sock.close()

    print("\n7. Simple HTTP Server")
    http_server_thread = threading.Thread(target=simple_http_server)
    http_server_thread.start()
    time.sleep(1)  # Give the server time to start

    # Send a request to the HTTP server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8080))
        s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = s.recv(1024)
        print(f"HTTP Response: {response.decode()}")

    print("\n8. Asynchronous Socket Server with asyncio")
    asyncio.run(async_server())

    print("\n9. Timeout Example")
    timeout_example()

    print("\n10. Port Scanner Example")
    port_scanner('localhost', 65430, 65440)

    print("\n11. Performance Benchmark")
    benchmark_socket_operations()

if __name__ == "__main__":
    main()