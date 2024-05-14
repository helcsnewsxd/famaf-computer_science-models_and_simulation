import random as rnd
import numpy as np
from uniform_discrete import uniform_discrete_distribution

def monte_carlo_sum(f: callable, n: int, m: int) -> float:
    """
    Estimate the summatory of a function using the Monte Carlo method.

    Parameters:
    f: callable - Function to estimate the summatory.
    n: int - Number of samples.
    m: int - Number of iterations.

    Returns:
    float - Estimated summatory of the function.
    """
    s = 0
    for r in uniform_discrete_distribution(1, n, m):
        s += f(r)
    return s / m * n

if __name__ == "__main__":
    f = lambda x: np.exp(1/x)
    n = 10_000
    m = 100
    print(monte_carlo_sum(f, n, m))