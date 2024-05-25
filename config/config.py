# config.py

import os

class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_API_KEY = 'your_stripe_api_key_here'
    TWILIO_ACCOUNT_SID = 'your_twilio_account_sid_here'
    TWILIO_AUTH_TOKEN = 'your_twilio_auth_token_here'