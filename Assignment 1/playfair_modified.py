def find_position(matrix, char):
    """
    Find the row and column of a character in the Playfair matrix.

    Parameters:
    matrix (list): The 5x5 matrix for the Playfair cipher.
    char (str): The character to find in the matrix.

    Returns:
    tuple: The row and column of the character in the matrix.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def generate_playfair_matrix(key):
    """
    Generate a 5x5 matrix for the Playfair cipher based on the provided key.
    """
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    # Step 1: Adding key characters to the matrix
    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)

    # Step 2: Adding remaining characters to the matrix
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            matrix.append(char)

    # Step 3: Presenting the matrix
    print("Generated Playfair Matrix:")
    for i in range(5):
        print(matrix[i*5:(i+1)*5])
    print()  # Adding a blank line for better readability

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def playfair_encrypt(text, key):
    """
    Encrypt the plain text using the Playfair cipher.
    """
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"

    matrix = generate_playfair_matrix(key)
    encrypted_text = ""

    # Step 4: Encrypting the text
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        print(f"Processing characters: {char1}, {char2}")

        if char1 == char2:
            char2 = 'X'  # Insert 'X' if both characters are the same
            print(f"Same characters found, modifying second character to: {char2}")

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
            print(f"Same row: {char1} -> {matrix[row1][(col1 + 1) % 5]}, {char2} -> {matrix[row2][(col2 + 1) % 5]}")
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
            print(f"Same column: {char1} -> {matrix[(row1 + 1) % 5][col1]}, {char2} -> {matrix[(row2 + 1) % 5][col2]}")
        else:
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]
            print(f"Rectangle: {char1} -> {matrix[row1][col2]}, {char2} -> {matrix[row2][col1]}")

    print(f"Encrypted Text: {encrypted_text}\n")  # Final encrypted text
    return encrypted_text


def playfair_decrypt(text, key):
    """
    Decrypt the encrypted text using the Playfair cipher.
    """
    text = text.upper().replace("J", "I").replace(" ", "")
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""

    # Step 5: Decrypting the text
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        print(f"Processing characters: {char1}, {char2}")

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
            print(f"Same row: {char1} -> {matrix[row1][(col1 - 1) % 5]}, {char2} -> {matrix[row2][(col2 - 1) % 5]}")
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
            print(f"Same column: {char1} -> {matrix[(row1 - 1) % 5][col1]}, {char2} -> {matrix[(row2 - 1) % 5][col2]}")
        else:
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]
            print(f"Rectangle: {char1} -> {matrix[row1][col2]}, {char2} -> {matrix[row2][col1]}")

    print(f"Decrypted Text: {decrypted_text}\n")  # Final decrypted text
    return decrypted_text


def main():
    """
    The main function to run the menu-driven program.
    """
    while True:
        print("\nPlayfair Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            plain_text = input("\nEnter the plain text: ")
            key = input("Enter the key: ")
            encrypted_text = playfair_encrypt(plain_text, key)
        elif choice == '2':
            encrypted_text = input("\nEnter the encrypted text: ")
            key = input("Enter the key: ")
            decrypted_text = playfair_decrypt(encrypted_text, key)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# Enter the plain text: MEETMEATNOON
# Enter the key: MONARCHY

