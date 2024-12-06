def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    combined = key + "".join([ch for ch in alphabet if ch not in key])
    return [list(combined[i:i + 5]) for i in range(0, 25, 5)]

def prepare_playfair_text(text, encrypt):
    text = text.upper().replace("J", "I").replace(" ", "")
    if encrypt:
        processed = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "X"
            if a == b:
                processed.append(a)
                processed.append("X")
                i += 1
            else:
                processed.extend([a, b])
                i += 2
        if len(processed) % 2 != 0:
            processed.append("X")
        return processed
    return text

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)

def playfair_cipher(text, key, encrypt=True):
    matrix = generate_playfair_matrix(key)
    text = prepare_playfair_text(text, encrypt)
    result = []

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            result.append(matrix[row1][(col1 + (1 if encrypt else -1)) % 5])
            result.append(matrix[row2][(col2 + (1 if encrypt else -1)) % 5])
        elif col1 == col2:
            result.append(matrix[(row1 + (1 if encrypt else -1)) % 5][col1])
            result.append(matrix[(row2 + (1 if encrypt else -1)) % 5][col2])
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return ''.join(result)

if __name__ == "__main__":
    text = "HELLO WORLD"
    key = "PLAYFAIRKEY"
    encrypted = playfair_cipher(text, key, encrypt=True)
    print(f"Encrypted: {encrypted}")
    decrypted = playfair_cipher(encrypted, key, encrypt=False)
    print(f"Decrypted: {decrypted}")
