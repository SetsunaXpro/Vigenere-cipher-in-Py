# Vigenere Cipher Program with Loop

def greet_user():
    print("\nWelcome to the Vigenère Cipher Program!")
    print("You can either encrypt or decrypt a message.")
    
def get_choice():
    choice = input("\nDo you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()
    while choice not in ['e', 'd']:
        choice = input("Invalid choice. Please type 'E' for encrypt or 'D' for decrypt: ").strip().lower()
    return choice

def get_message(choice):
    if choice == 'e':
        return input("Enter the sentence you want to encrypt: ").upper()
    else:
        return input("Enter the sentence you want to decrypt: ").upper()

def get_key():
    return input("Enter the key: ").upper()

def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key_length = len(key)
    key_nums = [ord(k) - ord('A') for k in key]  # Key converted to numbers
    text_nums = [ord(c) - ord('A') for c in text if c.isalpha()]  # Text converted to numbers

    for i, num in enumerate(text_nums):
        key_shift = key_nums[i % key_length]  # Cyclically use key characters
        
        if mode == 'encrypt':
            new_num = (num + key_shift) % 26  # Modular addition
        elif mode == 'decrypt':
            new_num = (num - key_shift + 26) % 26  # Modular subtraction
        
        result.append(chr(new_num + ord('A')))  # Convert back to letter
    
    # Combine the result, preserving non-alphabet characters (spaces, punctuation)
    final_result = []
    non_alpha_index = 0
    for c in text:
        if c.isalpha():
            final_result.append(result[non_alpha_index])
            non_alpha_index += 1
        else:
            final_result.append(c)
    
    return ''.join(final_result)

def main():
    while True:
        greet_user()
        choice = get_choice()
        message = get_message(choice)
        key = get_key()

        if choice == 'e':
            encrypted_message = vigenere_cipher(message, key, mode='encrypt')
            print("\nEncrypted message:", encrypted_message)
        else:
            decrypted_message = vigenere_cipher(message, key, mode='decrypt')
            print("\nDecrypted message:", decrypted_message)

        restart = input("\nDo you want to perform another operation? (Y/N): ").strip().lower()
        if restart != 'y':
            print("Thank you for using the Vigenère Cipher Program! Goodbye.")
            break

# Run the program
if __name__ == "__main__":
    main()
