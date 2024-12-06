import numpy as np

def hill_cipher(text, key, encrypt=True):
    n = int(len(key)**0.5)
    key_matrix = np.array([ord(c.upper()) - 65 for c in key]).reshape((n, n))
    if not encrypt:
        determinant = round(np.linalg.det(key_matrix))
        if determinant == 0 or np.gcd(determinant, 26) != 1:
            raise ValueError("Invalid key matrix for decryption")
        key_matrix = np.linalg.inv(key_matrix).astype(int) * determinant % 26

    text_vector = [ord(c.upper()) - 65 for c in text if c.isalpha()]
    while len(text_vector) % n != 0:
        text_vector.append(23)  # Padding with 'X'

    text_matrix = np.array(text_vector).reshape((-1, n)).T
    result_matrix = np.dot(key_matrix, text_matrix) % 26
    return ''.join(chr(c + 65) for c in result_matrix.T.flatten())

if __name__ == "__main__":
    text = "HELLO"
    key = "GYBNQKURP"  # Example key for a 3x3 matrix
    encrypted = hill_cipher(text, key, encrypt=True)
    print(f"Encrypted: {encrypted}")
    decrypted = hill_cipher(encrypted, key, encrypt=False)
    print(f"Decrypted: {decrypted}")