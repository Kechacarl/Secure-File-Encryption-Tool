from cryptography.fernet import Fernet

def load_key():
    """Loads the key from the current directory."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Error: 'secret.key' not found. Please run key_management.py first.")
        return None

def encrypt_file(file_path):
    """Encrypts a file and saves the encrypted content."""
    key = load_key()
    if not key:
        return

    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    
    print(f"File '{file_path}' successfully encrypted to '{file_path}.encrypted'")

def decrypt_file(file_path):
    """Decrypts a file and saves the decrypted content."""
    key = load_key()
    if not key:
        return
        
    fernet = Fernet(key)
    
    try:
        with open(file_path, "rb") as enc_file:
            encrypted_data = enc_file.read()
    except FileNotFoundError:
        print(f"Error: Encrypted file '{file_path}' not found.")
        return
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Save the decrypted file with the original name
    original_file_path = file_path.removesuffix(".encrypted")
    with open(original_file_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"File '{file_path}' successfully decrypted to '{original_file_path}'")