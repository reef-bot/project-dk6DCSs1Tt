# encryption.py

import bcrypt

def encrypt_data(data):
    # Encrypt the data using bcrypt
    encrypted_data = bcrypt.hashpw(data.encode('utf-8'), bcrypt.gensalt())
    return encrypted_data

def decrypt_data(data, encrypted_data):
    # Check if the data matches the encrypted data
    if bcrypt.checkpw(data.encode('utf-8'), encrypted_data):
        return True
    else:
        return False