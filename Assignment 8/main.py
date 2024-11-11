from sympy import isprime, primerange
from sympy.ntheory import primitive_root

def check_prime_and_primitive_root(p, g):
    # Check if p is prime
    if not isprime(p):
        return f"{p} is not a prime number."
    
    # Check if g is a primitive root of p
    try:
        calculated_root = primitive_root(p)
        if calculated_root == g:
            return f"{g} is a primitive root of the prime {p}."
        else:
            return f"{g} is not a primitive root of {p}. The first primitive root is {calculated_root}."
    except ValueError:
        return f"No primitive root found for {p}."

# Example: Check if 99991 is prime and 6 is a primitive root
p = 99991
g = 6
result = check_prime_and_primitive_root(p, g)
print(result)
