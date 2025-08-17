import sys
from encryptor import encrypt_file, decrypt_file
from key_management import generate_key

def print_help():
    print("Usage: python main.py [option] [file_path]")
    print("\nOptions:")
    print("  -e, --encrypt    Encrypt the specified file.")
    print("  -d, --decrypt    Decrypt the specified file.")
    print("  -k, --key        Generate a new secret key.")
    print("  -h, --help       Show this help message.")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
    elif sys.argv[1] in ("-e", "--encrypt"):
        if len(sys.argv) < 3:
            print("Error: Missing file path for encryption.")
            print_help()
        else:
            encrypt_file(sys.argv[2])
    elif sys.argv[1] in ("-d", "--decrypt"):
        if len(sys.argv) < 3:
            print("Error: Missing file path for decryption.")
            print_help()
        else:
            decrypt_file(sys.argv[2])
    elif sys.argv[1] in ("-k", "--key"):
        generate_key()
    else:
        print("Error: Invalid option.")
        print_help()