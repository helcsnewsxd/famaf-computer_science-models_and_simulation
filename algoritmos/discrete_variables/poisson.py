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
    l = 3
    c = dict()
    for x in poisson_distribution(l, 10**6): c[x] = c.get(x, 0) + 1
    for k in sorted(c.keys()): print(k, c[k]/sum(c.values()))