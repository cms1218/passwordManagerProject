import os.path
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open ("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key","rb") as key_file:
            read_key = key_file.read()
        return read_key
    else:
        print("There are no previously loaded keys. ")
        return None
    