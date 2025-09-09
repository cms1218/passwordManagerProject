from keyManager import load_key
from cryptography.fernet import Fernet



def encrypt_message(message: str) -> bytes:

    key = load_key()
    if key is None:
        print("Generate one first. ")
        return None
    
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def save_encrypted_file(encrypted_data: bytes): 
    if encrypted_data is None:
        print("No data to save.") 
        return 
    with open ("secret.enc", "wb") as message_file:
        message_file.write(encrypted_data)




