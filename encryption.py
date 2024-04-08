import os
import sys
import time


# ASCII sanat
ascii_art = """
 _           _ _____        b r y a n t      _   
| |_ ___ ___| |  __ |___ ___ ___ ___ _ _ ___| |_ 
|  _| . | . | | |___| -_|   |  _|  _| | | . |  _|
|_| |___|___|_|_____|___|_|_|___|_| |_  |  _|_|  
                       gg/Uz2T7we6pV|___|_|                                                                 
"""

class CustomAlphabetCipher:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !?."
        self.key = "xRjNiKsQIeOhPwHbXVdYqAaFgBfJmCcDzGnWvLrMtEoZuS?pU!T. 3kyl09 17"
        self.encrypt_dict = dict(zip(self.alphabet, self.key))
        self.decrypt_dict = dict(zip(self.key, self.alphabet))

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char in self.encrypt_dict:
                encrypted_text += self.encrypt_dict[char]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char in self.decrypt_dict:
                decrypted_text += self.decrypt_dict[char]
            else:
                decrypted_text += char
        return decrypted_text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def gradient_text(text):
    colors = ['\033[96m', '\033[96m', '\033[96m', '\033[96m', '\033[96m', '\033[96m']
    reset = '\033[0m'
    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + char)
        sys.stdout.flush()
        time.sleep(0.005)  # Yavaşlatma için
    sys.stdout.write(reset)  # Renkleri sıfırla

def main():
    cipher = CustomAlphabetCipher()
    while True:
        clear_screen()
        gradient_text(ascii_art)
        print("")
        print("\033[96m1. Encrypt Text\033[0m")
        print("\033[96m2. Decrypt Text\033[0m")
        print("\033[96m3. Exit\033[0m")
        choice = input("\nSelect an option: ")

        if choice == '1':
            clear_screen()
            print("\033[96mEncrypt Text\033[0m")
            plaintext = input("\nEnter the text to encrypt: ")
            encrypted_text = cipher.encrypt(plaintext)
            print("\n\033[92mEncrypted Text:\033[0m " + encrypted_text)
            input("\n\033[93mPress Enter to continue...\033[0m")
            
        elif choice == '2':
            clear_screen()
            print("\033[96mDecrypt Text\033[0m")
            ciphertext = input("\nEnter the text to decrypt: ")
            decrypted_text = cipher.decrypt(ciphertext)
            print("\n\033[92mDecrypted Text:\033[0m " + decrypted_text)
            input("\n\033[93mPress Enter to continue...\033[0m")

        elif choice == '3':
            clear_screen()
            gradient_text("Exiting the program...")
            break

        else:
            print("\n\033[91mInvalid option! Please try again.\033[0m")
            input("\n\033[93mPress Enter to continue...\033[0m")

if __name__ == "__main__":
    main()
