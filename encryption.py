def caesar_encrypt (text,shift):
 result= ""
 for char in text:
    if char.isalpha():
      shift_base = ord('A') if char.isupper() else ord('a')
      result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
    else:
      result += char
 return result



def caesar_decrypt(text,shift):
   result = ""
   for char in text:
      if char.isalpha():
        shift_base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
      else:
         result += char
   return result


text = input("Enter a text:")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(text,shift)
print("Encrypted:",encrypted)

decrypted = caesar_decrypt(encrypted,shift)
print("Decrypted:",decrypted)

