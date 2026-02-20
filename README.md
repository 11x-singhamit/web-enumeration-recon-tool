# WEB ENUMERATION AND RECONNAISSANCE TOOL

## Overview

The Web Enumeration and Reconnaissance Tool is a Python-based cybersecurity application designed to perform application-level reconnaissance on web applications in a safe and controlled environment. The tool helps identify web application structure, technologies, accessible directories, and potential security weaknesses.

This project was developed as part of an Ethical Hacking and Cyber Security coursework. It demonstrates object-oriented programming, web crawling algorithms, GUI development, database storage, and unit testing.

The tool supports both Command Line Interface (CLI) and Graphical User Interface (GUI).

---

## Features

- Web crawling and URL enumeration  
- Technology fingerprinting (Server and CMS detection)  
- Directory and file enumeration  
- Safe vulnerability detection (SQL Injection and XSS indicators)  
- Real-time scan result display  
- Graphical User Interface (GUI) dashboard  
- Command Line Interface (CLI) support  
- Result storage in SQLite database  
- Result logging in text file  
- Modular object-oriented architecture  
- Unit testing using pytest  

---

## Technologies Used

**Programming Language**
- Python 3

**Libraries**
- requests
- beautifulsoup4
- tkinter
- sqlite3
- datetime
- urllib.parse

**Testing Framework**
- pytest

**Database**
- SQLite3

---

## Project Structure

```
web-enumeration-recon-tool/
│
├── main.py
│
├── src/
│   ├── crawler.py
│   ├── fingerprint.py
│   ├── dir_enum.py
│   ├── vuln_detect.py
│   ├── storage.py
│   ├── gui.py
│   └── __init__.py
│
├── data/
│   ├── results.db
│   └── results.txt
│
├── tests/
│   └── test_all.py
│
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/11x-singhamit/web-enumeration-recon-tool.git
cd web-enumeration-recon-tool
```

### Install dependencies

```bash
pip install requests beautifulsoup4 pytest
```

Tkinter and sqlite3 are included with Python by default.

---

## How to Run

Run the tool:

```bash
python3 main.py
```

You will see:

```
1. CLI
2. GUI
Choose:
```

Select:

- CLI → Terminal-based scanning  
- GUI → Graphical dashboard scanning  

---

## Result Storage

Results are saved automatically in:

Database:
```
data/results.db
```

Log file:
```
data/results.txt
```

---

## Unit Testing

Run unit tests:

```bash
pytest tests/test_all.py -v
```

Expected output:

```
6 passed in 0.46s
```

---

## GUI Features

The GUI provides:

- Real-time enumeration display  
- Technology fingerprinting tab  
- Directory enumeration tab  
- Vulnerability detection tab  
- Start and Stop scan buttons  

---

## Educational Purpose and Ethical Use

This tool is developed for:

- Cybersecurity education  
- Ethical hacking learning  
- Controlled penetration testing environments  

Do not use on unauthorized systems.

Recommended testing platforms:

- Local test servers  

---

## Author

Amit Singh  
Ethical Hacking and Cyber Security Student  

GitHub:  
https://github.com/11x-singhamit/web-enumeration-recon-tool

---

## License

This project is for educational purposes only.