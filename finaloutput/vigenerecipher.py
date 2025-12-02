def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
           shift_base = ord('A') if char.isupper() else ord('a')
           shift = ord(key[key_index % len(key)]) - ord('A')
           result += chr((ord(char) - shift_base - shift) % 26 +shift_base)
           key_index += 1
        else:
            result += char
    return result


# --- Main program ---

text = input("Enter text: ")
key = input("Enter key: ")

encrypted = vigenere_encrypt(text, key)
print("Encrypted text:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted text:", decrypted)
