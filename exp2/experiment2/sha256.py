import hashlib

def sha256_text (data: str):

    return hashlib.sha256(data.encode()).hexdigest()

text1 = input("Enter Orginal text: ").strip()

text2 = input("Enter tampered text: ").strip()

hash1 = sha256_text (text1)

hash2 = sha256_text (text2)

print(f"Original text: {text1}")
print(f"Tampered Text: {text2}")
print(f"Original hash: {hash1}")
print(f"Tampered hash: {hash2}")

if hash1 == hash2:

   print("\n Data Intgrity verified (no Tampering)")

else:

   print(" \n Data has been tampered (hashes differ)")

