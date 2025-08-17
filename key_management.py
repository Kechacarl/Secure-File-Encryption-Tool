import os
from cryptography.fernet import Fernet # Import Fernet to use its key generation function
import base64

def generate_key():
    """Generates a random 32-byte key, Base64 encodes it, and saves it to 'secret.key'."""
    # Fernet.generate_key() already produces a Base64-encoded key.
    # We can use it directly to ensure compatibility.
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("New key generated and saved to secret.key")

if __name__ == "__main__":
    generate_key()