import nltk
from nltk.corpus import words

# Load English words from NLTK
nltk.download('words')
valid_words = set(words.words())

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = (ord(char) - ord('a') - shift) % 26 + ord('a') if char.islower() else (ord(char) - ord('A') - shift) % 26 + ord('A')
            plaintext += chr(shift_amount)
        else:
            plaintext += char  # Non-alphabetic characters remain unchanged
    return plaintext

def find_valid_words(plaintext):
    words_in_plaintext = plaintext.split()
    valid_found = set()
    for word in words_in_plaintext:
        if word.lower() in valid_words:
            valid_found.add(word.lower())
    return valid_found

def main():
    print("Welcome to the Caesar Cipher Cryptanalysis Tool!")
    ciphertext = input("Enter the ciphertext: ")
    
    for key in range(26):  # Try all 26 possible keys
        decrypted_text = caesar_decrypt(ciphertext, key)
        valid_found = find_valid_words(decrypted_text)
        
        if valid_found:
            print(f"Key {key}: Valid words found: {', '.join(valid_found)}")
        else:
            print(f"Key {key}: No valid words found.")

if __name__ == "__main__":
    main()
