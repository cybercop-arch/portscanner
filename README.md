# PortScanner

A lightweight Python-based TCP port scanning utility designed to identify open ports and accessible network services on target systems. This project demonstrates fundamental concepts of network reconnaissance, service enumeration, and socket programming commonly used in cybersecurity and penetration testing environments.

---

## Overview

PortScanner performs TCP connection scans across a specified range of ports to determine which services are reachable on a target host. The scanner supports both IP addresses and hostnames and provides fast and reliable results using Python's built-in socket library.

This project is useful for:

- Network Reconnaissance
- Service Discovery
- Penetration Testing Practice
- Cybersecurity Learning
- Network Troubleshooting

---

## Features

- TCP port scanning functionality
- Supports hostname and IP-based targets
- Fast scanning using configurable socket timeouts
- Automatic DNS resolution
- Scan timestamp logging
- Exception and error handling
- Cross-platform compatibility
- No third-party dependencies required

---

## Project Structure

```bash
port-scanner/
│
├── port_scanner.py      # Main scanning script
├── README.md            # Project documentation
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core Programming Language |
| Socket Module | TCP Network Communication |
| Datetime Module | Timestamp Logging |

---

## Requirements

- Python 3.x
- Linux, Windows, or macOS
- No external libraries required

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

---

## Usage

Run the scanner:

```bash
python3 port_scanner.py
```

Enter the target hostname or IP address when prompted:

```bash
Enter target IP or hostname: scanme.nmap.org
```

---

## Example Output

```bash
[+] Scanning Target: scanme.nmap.org
[+] Scan Started: 2025-05-21 14:12:33

[OPEN] Port 22
[OPEN] Port 80

[+] Scan Completed
```

---

## How It Works

The scanner performs the following steps:

1. Resolves the hostname into an IP address using:

```python
socket.gethostbyname(target)
```

2. Iterates through a specified port range

3. Attempts TCP connections using:

```python
socket.connect_ex()
```

4. Displays ports that respond successfully

---

## Customization

Modify the scanning range inside the script:

```python
for port in range(1, 1025):
```

You can increase or decrease the range depending on the required scan scope.

---

## Learning Objectives

This project helps demonstrate:

- TCP/IP Networking Fundamentals
- Socket Programming in Python
- Basic Reconnaissance Techniques
- Service Enumeration
- Ethical Security Testing Concepts

---

## Legal Disclaimer

This tool is intended strictly for educational purposes and authorized security testing only.

Do not scan systems, networks, or infrastructure without proper authorization. Unauthorized scanning may violate legal regulations and organizational security policies.

---

## Author

**Samiksha**  
Cybersecurity and Digital Forensics Student  
Ethical Hacking | Network Security | Penetration Testing

---

## Contributing

Contributions, improvements, and feature suggestions are welcome.

Fork the repository, submit pull requests, or open issues for enhancements and fixes.
