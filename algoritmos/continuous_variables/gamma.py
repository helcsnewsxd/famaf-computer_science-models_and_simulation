import random as rnd
import numpy as np

def gamma_distribution(a: int, b: float, sz: int = 1) -> list[float]:
    """
    Generates random numbers from a gamma distribution with shape parameter ('a') as integer.

    Parameters:
    a: int
        The shape parameter of the gamma distribution.
    b: float
        The rate parameter of the gamma distribution.
    sz: int
        The number of random numbers to generate.

    Returns:
    list[float]
        A list of random numbers from the gamma distribution.
    """
    def generate_gamma(a: int, b: float) -> float:
        u = 1
        for _ in range(a): u *= 1 - rnd.random()
        assert u > 0, "Invalid value generated for u"
        return -np.log(u) * b

    return [generate_gamma(a, b) for _ in range(sz)]

if __name__ == "__main__":
    # Check if the generated random numbers are from the gamma distribution.
    a = 2; b = 2
    sz = 10**5
    random_numbers = gamma_distribution(a, b, sz)
    print(f"Expected mean: {a * b} and variance: {a * b ** 2}")
    print(f"Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")