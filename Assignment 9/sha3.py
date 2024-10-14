import hashlib

def sha3_hash(text):
    """Generate SHA-3 hash for the given text."""
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(text.encode('utf-8'))  # Encode the text to bytes
    return sha3_256.hexdigest()  # Return the hexadecimal representation of the hash

def main():
    while True:
        print("\nSHA-3 Hashing Menu")
        print("1. Hash a string using SHA-3")
        print("2. Exit")
        
        choice = input("Choose an option (1 or 2): ")
        
        if choice == '1':
            user_input = input("Enter the string to hash: ")
            hash_result = sha3_hash(user_input)
            print(f"SHA-3 Hash (SHA3-256): {hash_result}")
        
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
