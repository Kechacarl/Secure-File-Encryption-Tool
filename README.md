# Secure-File-Encryption-Tool
Secure file encryption and decryption tool built in Python

# Project Title: Secure File Encryption Tool
Overview
This project is a simple yet secure file encryption and decryption tool built in Python. It uses industry-standard cryptographic algorithms to ensure data confidentiality and integrity. The application employs AES (Advanced Encryption Standard) in GCM (Galois/Counter Mode) for symmetric encryption, providing both data secrecy and authentication. A separate key management script demonstrates how to securely generate and store keys.

Features
Symmetric Encryption: Utilizes AES-256 for robust encryption of file contents.

Data Integrity: Implements GCM to verify that encrypted files have not been tampered with.

Key Management: Includes a script for generating a secure key, which is essential for cryptographic operations.

Command-Line Interface: Easy-to-use functions for encrypting and decrypting files from the terminal.

Requirements
To run this project, you need to have the cryptography library installed. You can install it using pip.

Implementation
The project consists of three main Python scripts: key_management.py, encryptor.py, and main.py.

1. Key Management (key_management.py)
This script handles the generation of a secure cryptographic key. It uses a cryptographically secure random number generator to create a 256-bit key, which is then saved to a file named secret.key. Keep this file secure, as anyone with access to it can decrypt your files.

2. Encryptor (encryptor.py)
This script contains the core encryption and decryption logic. The Fernet class from the cryptography library is a high-level wrapper that simplifies secure symmetric encryption using a key, providing built-in integrity checks and a secure mode of operation.

3. Main Script (main.py)
This is the user-facing script that provides a simple command-line interface for the encryption and decryption functions. It takes command-line arguments to determine whether to encrypt or decrypt a file.

Usage
1. Generate a key: Before any encryption, you must generate a key.

Bash
python main.py -k

2. Encrypt a file:

Bash
python main.py -e my_document.txt
This will create an encrypted file named my_document.txt.encrypted.

3. Decrypt a file:

Bash
python main.py -d my_document.txt.encrypted
This will restore the original my_document.txt file.

Note: Always ensure your secret.key file is backed up in a secure location. If you lose this key, you will permanently lose access to all files encrypted with it.







