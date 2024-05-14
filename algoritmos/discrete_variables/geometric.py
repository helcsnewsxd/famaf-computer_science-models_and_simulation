import random as rnd
import numpy as np

def geometric_distribution(p: float, sz: int = 1) -> list[int]:
    """
    Generate a random number from a geometric distribution.

    Parameters:
    p: float - Probability of success.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(p: float) -> int:
        U = rnd.random()
        return int(np.log(1 - U) / np.log(1 - p)) + 1

    return [generate(p) for _ in range(sz)]

if __name__ == "__main__":
    p = 0.3
    c = dict()
    for x in geometric_distribution(p, 10**6): c[x] = c.get(x, 0) + 1
    for k in sorted(c.keys()): 
        if k > 20: break
        print(k, c[k]/sum(c.values()))