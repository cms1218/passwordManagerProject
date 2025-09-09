from keyManager import load_key
from cryptography.fernet import Fernet
from os import path

# Function called in main.py
def decrypt_message():
    key = load_key()

    # Ensure user has previously generated key
    if key is None:
        print("Generate one First")
        return None
    
    # Create object to unlock and lock data
    f = Fernet(key)
    
    # Ensure a message has been stored
    if path.exists("secret.enc"):
        with open("secret.enc", "rb") as secret:
            encrypted_message = secret.read()
            decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message
    else:
        print("There is no message to decrypt. Please encrypt one first. ")
        return None
