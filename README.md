Day 08: Caesar Cipher Encryption & Decryption Program

Welcome to **Day 08** of my **100 Days of Python Challenge**!  
Today, I implemented a **Caesar Cipher** program that can both **encrypt** and **decrypt** messages based on a shift value.


📝 Project Overview

The **Caesar Cipher** is a classic encryption technique where each letter in the text is shifted by a fixed number of positions in the alphabet.


🚀 Features:

1. **Encrypt Text**: Convert a plaintext message into an encrypted format using a specified shift value.
2. **Decrypt Text**: Convert an encrypted message back into plaintext by reversing the shift.
3. **Interactive Menu**: The user can choose to encrypt, decrypt, or exit the program.


💻 How It Works

1. Encrypting a Message
The encryption shifts each letter by the specified value:
- For uppercase letters, the formula is:
  chr((ord(char) + shift - 65) % 26 + 65)
- For lowercase letters, the formula is:
  chr((ord(char) + shift - 97) % 26 + 97)
  
2. Decrypting a Message
The decryption reverses the shift applied during encryption:
- For uppercase letters:
  chr((ord(char) - shift - 65) % 26 + 65)
- For lowercase letters:
  chr((ord(char) - shift - 97) % 26 + 97)

3. Handling Non-Alphabetic Characters
Non-alphabetic characters (like spaces, punctuation) remain unchanged in both encryption and decryption.


📚 Concepts Applied

String Manipulation: Used Python's ord() and chr() functions for character manipulation.
Loops: Iterated through user input for encryption and decryption.
Conditionals: Handled menu choices and character type checks.
Interactive Input: Created a dynamic program that responds to user actions.
