from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(plain_text, key):
    """
    Encrypt the plain text using DES algorithm.
    
    Parameters:
    plain_text (str): The text to be encrypted.
    key (bytes): The encryption key (must be 8 bytes long).
    
    Returns:
    bytes: The encrypted cipher text.
    """
    print(f"\n[Encrypt] Plain Text: {plain_text}")
    
    # Initialize the DES cipher in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)
    print(f"[Encrypt] DES Cipher initialized with ECB mode and key: {key.hex()}")
    
    # Padding the plain text to match DES block size (8 bytes)
    padded_text = pad(plain_text.encode(), DES.block_size)
    print(f"[Encrypt] Padded Plain Text (in hexadecimal): {padded_text.hex()}")
    
    # Encrypting the padded text
    encrypted_text = cipher.encrypt(padded_text)
    print(f"[Encrypt] Encrypted Text (in hexadecimal): {encrypted_text.hex()}")
    
    return encrypted_text

def des_decrypt(cipher_text, key):
    """
    Decrypt the cipher text using DES algorithm.
    
    Parameters:
    cipher_text (bytes): The encrypted text to be decrypted.
    key (bytes): The decryption key (must be 8 bytes long).
    
    Returns:
    str: The decrypted plain text.
    """
    print(f"\n[Decrypt] Cipher Text to Decrypt (in hexadecimal): {cipher_text.hex()}")
    
    # Initialize the DES cipher in ECB mode for decryption
    cipher = DES.new(key, DES.MODE_ECB)
    print(f"[Decrypt] DES Cipher initialized with ECB mode and key: {key.hex()}")
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(cipher_text)
    print(f"[Decrypt] Decrypted Padded Text (in hexadecimal): {decrypted_padded_text.hex()}")
    
    # Unpad the decrypted text
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    print(f"[Decrypt] Decrypted Text (unpadded): {decrypted_text.decode()}")
    
    return decrypted_text.decode()

def main():
    """
    The main function to run the program.
    """
    print("\nDES Encryption and Decryption")
    
    # Generate a random 8-byte key for DES
    key = get_random_bytes(8)
    print(f"\nGenerated Key (in hexadecimal): {key.hex()}")
    
    # Input plaintext
    plain_text = input("Enter the plain text to encrypt: ")
    
    # Encrypt the plaintext
    encrypted_text = des_encrypt(plain_text, key)
    
    # Decrypt the ciphertext
    decrypted_text = des_decrypt(encrypted_text, key)
    
    # Final verification of decrypted text
    print(f"\nDecrypted Text matches Original Plain Text: {decrypted_text == plain_text}")

if __name__ == "__main__":
    main()
