def caesar_cipher(message, shift):
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

message = input("Enter the message to be encrypted: ")
shift = int(input("Enter the shift value: "))

encrypted_message = caesar_cipher(message, shift)

print("Encrypted message:", encrypted_message)
