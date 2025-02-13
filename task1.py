import string

def vigenere_encrypt(plaintext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            cipher_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            ciphertext += cipher_char
            key_index += 1
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            plain_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            plaintext += plain_char
            key_index += 1
        else:
            plaintext += char

    return plaintext

def columnar_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols
    if len(plaintext) % num_cols != 0:
        num_rows += 1

    grid = ['' for _ in range(num_cols)]
    for i in range(len(plaintext)):
        grid[i % num_cols] += plaintext[i]

    key_order = sorted(range(len(key)), key=lambda x: key[x])
    transposed_text = ''.join(grid[i] for i in key_order)
    
    return transposed_text

def columnar_transposition_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    grid = ['' for _ in range(num_cols)]
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    column_size = len(ciphertext) // num_cols
    for i, col in zip(key_order, range(num_cols)):
        start = i * column_size
        end = (i + 1) * column_size
        grid[i] = ciphertext[start:end]

    plaintext = ''
    for i in range(column_size):
        for j in range(num_cols):
            if i < len(grid[j]):
                plaintext += grid[j][i]

    return plaintext

def hybrid_encrypt(plaintext, vigenere_key, transposition_key):
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    final_ciphertext = columnar_transposition_encrypt(vigenere_ciphertext, transposition_key)
    return final_ciphertext

def hybrid_decrypt(ciphertext, vigenere_key, transposition_key):
    transposed_plaintext = columnar_transposition_decrypt(ciphertext, transposition_key)
    final_plaintext = vigenere_decrypt(transposed_plaintext, vigenere_key)
    return final_plaintext

plaintext = "HELLO WORLD"
vigenere_key = "SECRET"
transposition_key = "COLUMNAR"

encrypted_text = hybrid_encrypt(plaintext, vigenere_key, transposition_key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = hybrid_decrypt(encrypted_text, vigenere_key, transposition_key)
print(f"Decrypted Text: {decrypted_text}")
