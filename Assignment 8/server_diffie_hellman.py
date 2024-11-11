# p: 99991
# g: 6


import socket
import random
from sympy import isprime, primitive_root

def generate_private_key(p):
    """Generate a private key."""
    private_key = random.randint(2, p - 2)
    print(f"Generated Private Key: {private_key}")
    return private_key

def calculate_public_key(g, private_key, p):
    """Calculate the public key."""
    public_key = pow(g, private_key, p)
    print(f"Calculated Public Key: {public_key}")
    return public_key

def calculate_shared_secret(public_key, private_key, p):
    """Calculate the shared secret."""
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

def validate_prime_and_primitive_root(p, g):
    """Check if p is prime and g is a primitive root of p."""
    if not isprime(p):
        raise ValueError("p must be a prime number.")
    # Verify g is a primitive root of p
    if g != primitive_root(p):
        raise ValueError("g must be a primitive root of p.")
    print(f"p: {p} is prime and g: {g} is a valid primitive root.")

def start_server(host='localhost', port=5000):
    # Take p and g as user input
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root (g): "))

    # Validate p and g
    try:
        validate_prime_and_primitive_root(p, g)
    except ValueError as e:
        print(e)
        return

    # Generate server's private and public keys
    private_key = generate_private_key(p)
    public_key = calculate_public_key(g, private_key, p)

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started. Listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"\nConnected by {addr}")

    # Send the server's public key and p, g values to the client
    conn.sendall(f"{public_key},{p},{g}".encode())

    # Receive the client's public key
    client_public_key = int(conn.recv(1024).decode())
    print(f"\nReceived Client's Public Key: {client_public_key}")

    # Calculate the shared secret
    shared_secret = calculate_shared_secret(client_public_key, private_key, p)
    print(f"\nShared Secret (Server): {shared_secret}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
