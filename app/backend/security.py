import base64
import hashlib
from cryptography.fernet import Fernet
from .auth import SECRET_KEY

# Derive a valid 32-byte key from SECRET_KEY using SHA-256 and base64 encoding
derived_key = base64.urlsafe_b64encode(hashlib.sha256(SECRET_KEY.encode()).digest())
cipher_suite = Fernet(derived_key)

def encrypt_data(data: str) -> str:
    """Encrypts string data using Fernet symmetric encryption."""
    if not data:
        return ""
    return cipher_suite.encrypt(data.encode("utf-8")).decode("utf-8")

def decrypt_data(token: str) -> str:
    """Decrypts string data back to plain text."""
    if not token:
        return ""
    return cipher_suite.decrypt(token.encode("utf-8")).decode("utf-8")
