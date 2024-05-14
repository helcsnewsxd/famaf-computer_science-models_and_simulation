def isPrime(n: int) -> bool:
    """
    Check if a number is prime
    """
    if n == 1: return False
    elif n % 2 == 0: return n == 2
    
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def factorize(n: int) -> dict:
    """
    Factorize a number into its prime factors
    """
    factors = dict()
    i = 2
    while i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    return factors

def isPrimitiveRoot_forPrime(n: int, m: int) -> bool:
    """
    Check if n is a primitive root of m (with m prime)
    """
    assert isPrime(m)
    primes = factorize(m-1)
    for p in primes:
        if pow(n, (m-1)//p, m) == 1: return False
    return True

if __name__ == "__main__":
    numbers = [2, 15, 12_345, 2**7-1, 2**13-1]
    # Test the isPrime function
    for n in numbers:
        print(f"{n} is prime: {isPrime(n)}")

    # Test the factorize function
    for n in numbers:
        print(f"Factors of {n}: {factorize(n)}")
    
    # Test the isPrimitiveRoot_forPrime function
    true_cases = [
        [2, [1]],
        [3, [2]],
        [5, [2, 3]],
        [7, [3, 5]],
        [11, [2, 6, 7, 8]],
        [13, [2, 6, 7, 11]],
    ]
    for m, roots in true_cases:
        for root in roots:
            assert isPrimitiveRoot_forPrime(root, m)

    false_cases = [
        [3, [1]],
        [5, [1, 4]],
        [7, [1, 2, 4, 6]],
        [11, [1, 3, 4, 5, 9, 10]],
        [13, [1, 3, 4, 5, 9, 10, 12]],
    ]
    for m, roots in false_cases:
        for root in roots:
            assert not isPrimitiveRoot_forPrime(root, m)