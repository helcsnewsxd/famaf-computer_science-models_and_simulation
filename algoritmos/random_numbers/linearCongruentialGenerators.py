import math
from primeUtility import isPrime, isPrimitiveRoot_forPrime, factorize

def congruentialGenerator(seed: int, a: int, c: int, m: int, n: int) -> list[int]:
    """
    Generate a list of n pseudo-random numbers using the congruential generator method.
    """
    numbers = []
    for i in range(n):
        numbers.append(seed)
        seed = (a * seed + c) % m
    return numbers

def periodBrute_congruentialGenerator(seed: int, a: int, c: int, m: int) -> int:
    """
    Calculate the period of the congruential generator method with brute force.
    """
    periods = []
    seeds = range(m) if seed is None else [seed]
    for seed in seeds:
        numbers = dict()
        while seed not in numbers:
            numbers[seed] = len(numbers)
            seed = (a * seed + c) % m
        periods.append(len(numbers) - numbers[seed])
    return max(periods)

def period_congruentialGenerator(seed: int, a: int, c: int, m: int) -> int:
    """
    Calculate the period of the congruential generator method.
    """
    # If the generator is mixed and has the biggest period
    if c != 0 and math.gcd(c, m) == 1 and (a % p == 1 for p in factorize(m).keys()) and (m % 4 == 0) == (a % 4 == 1):
        return m
    
    # If the generator is multiplicative and has the biggest period
    if c == 0 and isPrime(m) and isPrimitiveRoot_forPrime(a, m):
        return m-1
    
    # Otherwise, calculate the period with brute force
    return periodBrute_congruentialGenerator(seed, a, c, m)

if __name__ == "__main__":
    # Test the congruentialGenerator function
    test_cases = [
        [0, 5, 1, 16, 20],
        [1, 1, 11, 22, 20],
        [0, 1, 1, 15, 20],

        # Mixed generator with biggest period
        [0, 5, 3, 16, 20],
        [0, 1_103_515_245, 12_345, 2**32, 20], # ANSI C
        
        # Multiplicative generator with biggest period
        [1, 2, 0, 19, 20],
        [1, 2**5, 0, 19, 20],
        [1, 7**5, 0, 2**31-1, 20],
    ]

    for test in test_cases:
        print(f"seed, a, c, m, n = {test[:4]}, {test[4]}: {congruentialGenerator(*test)}")
    
    # Test the period_congruentialGenerator function
    for test in test_cases:
        print(f"seed, a, c, m = {test[:4]}: {period_congruentialGenerator(*test[:4])}")