def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    
    for char in message:
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            encrypted_message += new_char
        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            encrypted_message += new_char
        else:
            encrypted_message += char
    
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    decrypted_message = ""
    
    for char in message:
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('A'))
            decrypted_message += new_char
        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('a'))
            decrypted_message += new_char
        else:
            decrypted_message += char
    
    return decrypted_message

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = caesar_cipher_encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
