# 🔎 PortScanner

A simple Python-based **TCP port scanner** that scans a target IP for open ports within a given range. This tool helps identify which services are accessible on a machine, useful for penetration testing, network troubleshooting, and ethical hacking practices.

---

## 📦 Features

- 🔧 Scans TCP ports (default: 21–79)
- ⚡ Fast connection attempts with timeouts
- 🧠 Resolves IP from hostname (or accepts IP directly)
- 🕒 Displays timestamps for scanning session
- 🔒 Graceful error handling for hostname or connection issues

---

## 📁 Project Structure

```

port-scanner/
│
├── port\scanner.py        # The main port scanner script
├── README.md              # Documentation

````

---

## 📋 Requirements

- Python 3.x  
- Works on Linux, Windows, and macOS
- No third-party libraries needed

---

## 🚀 Usage

### 🧪 Run the scanner

```bash
python3 port_scanner.py
````

You'll be prompted to enter a target IP or hostname:

```
enter the target ip address: scanme.nmap.org
```

### 🖥 Example Output

```
scanning the target scanme.nmap.org
time started:  2025-05-21 14:12:33.785509
Port 22: open
Port 80: open
```

---

## 🧠 How It Works

* `socket.gethostbyname(target)`: Resolves hostname to IP 
* Connects to each port in the specified range
* Uses `connect_ex()` to test if the port is open
* Prints out the open ports only

---

## 📌 Notes

* You can change the port range:

```python
for port in range(1, 1025):
```

* Scanning too many ports on external servers may get blocked or flagged. Use responsibly and only on systems you own or have permission to test.

---

## 🛡 Disclaimer

This tool is for **educational and ethical hacking purposes only**. Do not scan systems you do not own or have authorization to test.

---

## 🙋‍♀️ Author

**Samiksha**
Cybersecurity & Forensics Student | Developer | Ethical Hacking Enthusiast

---

## 🤝 Contributing

Feel free to fork, suggest enhancements, or submit a pull request 🚀
