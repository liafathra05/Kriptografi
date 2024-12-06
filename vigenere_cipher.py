def vigenere_cipher(text, key, encrypt=True):
    result = []
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text.upper()]

    for i, char in enumerate(text_as_int):
        if 65 <= char <= 90:  # A-Z
            shift = key_as_int[i % key_length] - 65
            if not encrypt:
                shift = -shift
            new_char = (char + shift - 65) % 26 + 65
            result.append(chr(new_char))
        else:
            result.append(chr(char))
    return ''.join(result)

if __name__ == "__main__":
    text = "HELLO WORLD"
    key = "SECRETKEYSECRET"
    encrypted = vigenere_cipher(text, key, encrypt=True)
    print(f"Encrypted: {encrypted}")
    decrypted = vigenere_cipher(encrypted, key, encrypt=False)
    print(f"Decrypted: {decrypted}")
