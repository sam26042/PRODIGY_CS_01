import sys

#For colorful CLI output
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False

def print_colored(message, color=Fore.GREEN):
    if COLOR_ENABLED:
        print(color + message)
    else:
        print(message)

def shift_char(char, shift):
    """Shift a single character if it is a letter."""
    if char.isalpha():
        shift_base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - shift_base + shift) % 26 + shift_base)
    return char

def caesar_cipher_encrypt(text, shift):
    """Encrypt text using Caesar Cipher."""
    shift = shift % 26  # Normalize the shift
    return ''.join(shift_char(char, shift) for char in text)

def caesar_cipher_decrypt(text, shift):
    """Decrypt text using Caesar Cipher."""
    return caesar_cipher_encrypt(text, -shift)

def get_valid_shift():
    """Prompt user for a valid shift between 1 and 25."""
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 25.")

def run_tests():
    """Basic tests for Caesar Cipher logic."""
    assert caesar_cipher_encrypt("ABC", 1) == "BCD"
    assert caesar_cipher_decrypt("BCD", 1) == "ABC"
    assert caesar_cipher_encrypt("xyz", 3) == "abc"
    assert caesar_cipher_encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert caesar_cipher_decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
    print("All tests passed!")

def main():
    print("Welcome to the Caesar Cipher Program!")

    while True:
        choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Thank you for using the Caesar Cipher Program. Goodbye!")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ").strip()
            if not message:
                print("Message cannot be empty. Please try again.")
                continue
            shift = get_valid_shift()
            if choice == 'E':
                encrypted_message = caesar_cipher_encrypt(message, shift)
                print_colored(f"Encrypted Message: {encrypted_message}", Fore.GREEN)
            elif choice == 'D':
                decrypted_message = caesar_cipher_decrypt(message, shift)
                print_colored(f"Decrypted Message: {decrypted_message}", Fore.CYAN)
        else:
            print("Invalid choice. Please select E, D, or Q.")

if __name__ == "__main__":
    # run_tests()  # Uncomment to run tests
    main()
