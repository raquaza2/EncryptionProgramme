#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
 
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
