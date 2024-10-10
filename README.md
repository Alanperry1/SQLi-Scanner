# SQL Injection Scanner

## Overview

The SQL Injection Scanner is a Python-based tool designed to identify SQL injection vulnerabilities in web applications. It analyzes the forms on a given URL and attempts to exploit them to determine their susceptibility to SQL injection attacks.

## Features

- **Form Detection**: Automatically detects all forms on a specified web page.
- **SQL Injection Testing**: Performs injection attempts on detected forms using various payloads.
- **Vulnerability Reporting**: Clearly indicates whether a vulnerability was found.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd sql-injection-scanner
   ```

2. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

Run the scanner with the following command:
```bash
python sql_injection_scanner.py
```
Follow the prompt to enter the URL you wish to scan.

## Contribution

Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on applications for which you have explicit permission to test.

