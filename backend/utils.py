# backend/utils.py

import os
import random
import string

def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def process_payment(amount):
    # Logic to process payment using Stripe API
    return True

def send_chat_message(message):
    # Logic to send chat message using Twilio API
    return True

def encrypt_data(data):
    # Logic to encrypt data using bcrypt
    return "Encrypted Data"

def decrypt_data(data):
    # Logic to decrypt data using bcrypt
    return "Decrypted Data"