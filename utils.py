"""
Functions that support my implementation of the RSA cryptosystem.
"""
import secrets, random, time
def gcd(a, b):
    """
    Calculate the GCD of integers a and b.

    Args:
        a: First int.
        b: Second int.

    Returns:
        int: The GCD of the inputs.
    """
    if a < b:
        temp = b
        b = a
        a = temp

    r = a % b

    if r > 0:
        return gcd(b, r)
    else:
        return b

def ext_euclid(a, b):
    """
    Calculates the GCD and integers u and v such that
    au + bv = GCD(a,b).

    Args:
        a: First int.
        b: Second int.

    Returns:
        tuple:
            - int: GCD of a and b.
            - int: The integer u.
            - int: The integer v.
    """
    if a < b:
            temp = b
            b = a
            a = temp
    if b == 0:
        return (a, 1, 1)


    u =1
    g = a
    x = 0
    y = b

    while y!= 0:
        q = g // y
        t = g % y

        s = u - (q*x)
        u = x
        g = y
        x = s
        y = t

    v = (g - (a*u)) // b
    return (g, u, v)

def fast_power(x, y, n):
    """
    Computes modular exponentiation mod n with base x and exponent y.

    Args:
        x: Base, as int.
        y: Exponent, as int.
        n: Modulus, as int.

    Returns:
        int: The result of x^y mod n.
    """
    a = x
    b = 1

    while y > 0:
        if y % 2 == 1:
            b = (b*a) % n
        a = (a**2) % n
        y = y //2

    return b

def miller_rabin(n, a):
    """
    Performs the Miller-Rabin test for compositeness for n with witness a.

    Args:
        n: Number to test, as int.
        a: Potential witness, as int.

    Returns:
        bool: True if n is composite, False if undetermined.
    """
    if (n % 2 == 0) or (1 < gcd(a, n) and gcd(a, n) < n):
        return True

    k = 0
    k_can = 1
    while (n-1) % (2**(k_can)) == 0:
        q_can = (n-1) // (2**(k_can))
        if q_can % 2 != 0:
            k = k_can
            q = q_can
        k_can += 1
    assert (n-1 == (2**k)*q)

    x = fast_power(a, q, n)
    if x % n == 1:
        return False

    for i in range(k):
        if x % n == n-1:
            return False
        x = (x**2) % n

    return True
    
    
def test_primality(p):
    """
    Tests for primality of p.

    Args:
        p: Number to test, as int.

    Returns:
        bool: True if p is likely prime, False otherwise.
    """
    if (p % 2 == 0) or (p % 3 == 0) or (p % 5  == 0) or (p % 7 == 0) or (p % 11 == 0):
            return False

    for i in range(100):
        potential_witness = random.randint(2, p-2)
        composite = miller_rabin(p, potential_witness)
        if composite:
            return False

    return True

def key_gen():
    """
    Generates an RSA key pair.

    Returns:
        tuple:
            - tuple:
                - int: Public modulus n.
                - int: Public encryption exponent e.
            - tuple:
                - int: Private decryption exponent d.
                - int: Value of Euler's phi-function.
    """
    for i in range(2):
        p_can = secrets.randbits(1024)

        while not test_primality(p_can):
            p_can = secrets.randbits(1024)

        if i == 0:
            p = p_can
        else:
            q = p_can

    n = p*q

    phi = (p-1)*(q-1)

    e = 65537

    g, k, d = ext_euclid(e, phi)
    assert g == 1
    d = d%phi

    return ((n, e), (d, phi))

def encrypt(m, n, e):
    """
    Performs RSA encryption.

    Args:
        m: Plaintext to encrypt, as int.
        n: Public modulus, as int.
        e: Public encryption exponent, as int.

    Returns:
        int: Resulting ciphertext.
    """
    c = fast_power(m, e, n)
    return c

def decrypt(c, n, d):
    """
    Performs RSA decryption.

    Args:
        c: Ciphertext to decrypt, as int.
        n: Public modulus, as int.
        d: Private decryption exponent, as int.

    Returns:
        int: Resulting plaintext.
    """
    m = fast_power(c, d, n)
    return m
