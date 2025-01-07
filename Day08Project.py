def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

repeat = input("Would you like to start? (y/n) \n").lower()
while repeat == 'y':
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt/exit): ").lower()
    if choice == "encrypt":
        text = input("Enter the message you want to encrypt: ")
        shift = int(input("Enter the shift value for encryption: "))
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Encrypted message:", encrypted_text)
        
    elif choice == "decrypt":
        encrypted_text = input("Enter the encrypted message: ")
        shift = int(input("Enter the shift value for decryption: "))
        decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
        print("Decrypted message:", decrypted_text)
    elif choice == "exit":
        print("Exiting the program. Goodbye!")
        break  # Properly exit the loop
    else:
        print("Invalid choice. Please choose either 'encrypt', 'decrypt', or 'exit'.")
