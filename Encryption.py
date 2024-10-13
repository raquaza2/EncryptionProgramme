#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
 
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""
 
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted text: {cipher_text}")
print(f"original text: {plain_text}")
