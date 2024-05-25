encryption/README.md
# Encryption Module

This module handles all encryption and decryption functionalities for the app to ensure user data security and anonymity.

## Files:
- `encryption.py`: Contains functions for encryption and decryption using bcrypt algorithm.

### Dependencies:
- `bcrypt`: 4.0.1

### Functions:
- `encrypt_data(data)`: Encrypts the input data using bcrypt algorithm and returns the encrypted data.
- `decrypt_data(encrypted_data)`: Decrypts the input encrypted data using bcrypt algorithm and returns the decrypted data.

### Usage:
- Import the `encrypt_data` and `decrypt_data` functions from `encryption.py` into the necessary modules where encryption or decryption is required.
- Call the functions with the appropriate data to encrypt or decrypt sensitive information.