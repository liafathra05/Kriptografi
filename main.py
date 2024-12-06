from vigenere_cipher import vigenere_cipher
from playfair_cipher import playfair_cipher
from hill_cipher import hill_cipher

def main():
    print("Welcome to the Cipher Program")
    print("1. Vigenere Cipher")
    print("2. Playfair Cipher")
    print("3. Hill Cipher")
    choice = input("Choose an option (1/2/3): ")

    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if choice == "1":
        action = input("Encrypt or Decrypt (E/D): ").upper()
        result = vigenere_cipher(text, key, encrypt=(action == "E"))
    elif choice == "2":
        action = input("Encrypt or Decrypt (E/D): ").upper()
        result = playfair_cipher(text, key, encrypt=(action == "E"))
    elif choice == "3":
        action = input("Encrypt or Decrypt (E/D): ").upper()
        result = hill_cipher(text, key, encrypt=(action == "E"))
    else:
        print("Invalid choice!")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()