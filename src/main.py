import keyManager
import encryptor
import decryptor

from keyManager import generate_key
from encryptor import encrypt_message, save_encrypted_file
from decryptor import decrypt_message

def main():
    while True:
        print("\n=== Simple Cryptography CLI ===")
        print("1. Generate Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            generate_key()

        elif choice == "2":
            msg = input("Enter the message to encrypt: ")
            encrypted = encrypt_message(msg)  
            save_encrypted_file(encrypted)

        elif choice == "3":
            decrypted = decrypt_message()
            if decrypted:
                print("Decrypted message:", decrypted)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
