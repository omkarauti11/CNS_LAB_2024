import hashlib

def compute_sha512(input_string):
    """Compute the SHA-512 hash of the input string."""
    sha512_hash = hashlib.sha512(input_string.encode()).hexdigest()
    return sha512_hash

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n--- SHA-512 Hash Generator ---")
        print("1. Compute SHA-512 Hash")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_input = input("Enter a string to hash: ")
            hash_result = compute_sha512(user_input)
            print(f"SHA-512 Hash: {hash_result}")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
