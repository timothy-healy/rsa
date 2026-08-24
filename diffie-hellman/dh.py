"""
Implement Diffie-Hellman Key Exchange
"""
import random

def generate_keys(g, p):
    """
    Generates the secret exponent and publicly exchanged key in Diffie-Hellman.
    Assumes p and g are already chosen correctly.

    Args:
        g: Chosen int as the base.
        p: Chosen large prime modulus.

    Returns:
        tuple:
            - int: The secret exponent.
            - int: The public key to exchange.
    """
    private_key = random.randint(2, p-2)
    public_key = pow(g, private_key, p)
    return private_key, public_key

def compute_secret(shared_public_key, private_key, p):
    """
    Computes the secret value in Diffie-Hellman.
    Assumes the keys have been properly generated.
    Assumes p is a suitable prime.

    Args:
        shared_public_key: The public key received from the other party.
        private_key: The secret exponent.
        p: Chosen large prime modulus.

    Returns:
        int: The secret value.

    """
    return pow(shared_public_key, private_key, p)

# # hard coded values for testing
# # comment out input() lines below to use
# p = 920751269651692836158027677369
# g = 33024526926708246434869388771

p = int(input("Agreed upon large prime p: "))
g = int(input("Agreed upon integer base g: "))

alice_private, alice_public = generate_keys(g, p)
bob_private, bob_public = generate_keys(g, p)

alice_secret = compute_secret(bob_public, alice_private, p)
bob_secret = compute_secret(alice_public, bob_private, p)

print("Resulting exchange:")
print(f"Alice's public key sent to Bob: {alice_public}")
print(f"Bob's public key sent to Alice: {bob_public}")
print(f"Alice calculates secret value as: {alice_secret}")
print(f"Bob calculates secret value as: {bob_secret}")
print(f"Calculated the same value: {alice_secret == bob_secret}")
