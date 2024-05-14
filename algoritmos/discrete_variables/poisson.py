import random as rnd
import numpy as np

def poisson_distribution(l: float, sz: int = 1) -> list[int]:
    """
    Generate a random number from a Poisson distribution.

    Parameters:
    l: float - Rate of the Poisson distribution.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(l: float) -> int:
        p = np.exp(-l); F = p
        U = rnd.random()

        for j in range(1, int(l) + 1): p *= l / j; F += p
        if U >= F:
            j = int(l) + 1
            while U >= F: p *= l / j; F += p; j += 1
            return j - 1
        else:
            j = int(l)
            while U < F: F -= p; p *= j / l; j -= 1
            return j + 1

    return [generate(l) for _ in range(sz)]

if __name__ == "__main__":
    # Check if the generated random numbers are from the Poisson distribution.
    l = 2
    sz = 10**5
    random_numbers = poisson_distribution(l, sz)
    print(f"Expected mean: {l} and variance: {l}")
    print(f"Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")