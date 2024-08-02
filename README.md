# CyberAssist

Welcome to the CyberAssist (Security Tools Suite), a collection of web-based tools designed to enhance your security posture and provide essential insights into various security aspects. This suite includes tools for password strength assessment, keylogging, cryptographic operations, hash generation, IP geolocation, DNS lookup, SSL/TLS certificate checking, and phishing URL detection.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tools Overview](#tools-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Password Strength Checker:** Assess the robustness of your passwords.
- **Keylogger:** Monitor and record keyboard inputs.
- **Cryptographic Tool:** Encrypt and decrypt messages.
- **Hash Generator:** Generate possible hash values from plain text.
- **IP Geolocation Finder:** Locate the geographical position of an IP address.
- **DNS Lookup Tool:** Retrieve detailed DNS records for a domain.
- **SSL/TLS Certificate Checker:** Check the validity and security of SSL/TLS certificates.
- **Phishing URL Detector:** Identify potential phishing URLs.

## Installation

To get started with the Security Tools Suite, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ansari-khursaid7tr/CyberAssist.git
   cd CyberAssist
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` in your web browser to access the tools.

## Usage

Each tool in the suite can be accessed from the home page. Navigate to the specific tool you need and follow the instructions on the page to utilize its features.

## Tools Overview

### Security and Monitoring Tools

#### Password Strength Checker
- **Description**: Assess the robustness of your passwords to ensure they are strong and secure against potential threats.
- **Usage**: Enter a password and receive feedback on its strength.

#### Keylogger
- **Description**: Monitor and record keyboard inputs to detect unauthorized activity.
- **Usage**: Enable keylogging to start recording keystrokes.

#### Phishing URL Detector
- **Description**: A tool that checks URLs for phishing indicators to determine their safety.
- **Usage**: Enter a URL and receive a safety assessment.

### Cryptography and Hashing Tools

#### Cryptographic Tool
- **Description**: Encrypt and decrypt messages to secure sensitive information.
- **Usage**: Select an encryption algorithm, enter a key and a message to encrypt or decrypt.

#### Hash Generator
- **Description**: Attempt to generate all the possible hash values from the given plain text.
- **Usage**: Enter plain text and generate its hash values.

### Network and DNS Tools

#### IP Geolocation Finder
- **Description**: A tool that locates the geographical position of an IP address.
- **Usage**: Enter an IP address to find its geolocation.

#### DNS Lookup Tool
- **Description**: Quickly retrieves detailed DNS records for a specified domain name.
- **Usage**: Enter a domain name and retrieve its DNS records.

#### SSL/TLS Certificate Checker
- **Description**: Check the validity and security of an SSL/TLS certificate for any domain.
- **Usage**: Enter a domain name to check its SSL/TLS certificate.

## Contributing

We welcome contributions to improve the Security Tools Suite! Please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

---

Feel free to reach out if you have any questions or need further assistance. Happy securing!
