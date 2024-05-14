import random as rnd
import numpy as np

from inverse_method_continuous import inverse_transform_method
from gamma import gamma_distribution

def exponential_distribution(l: float, sz: int = 1, gamma_method: bool = True) -> list[float]:
    """
    Generates random numbers from an exponential distribution.

    Parameters:
    l: float
        The rate parameter of the exponential distribution.
    sz: int
        The number of random numbers to generate.
    gamma_method: bool
        If True, uses the gamma distribution method to generate random numbers. Otherwise, uses the inverse transform method.
        (The gamma method is more efficient for generating multiple random numbers but if the SZ is big, -log(u) can be very close to 0 and cause numerical issues.)

    Returns:
    list[float]
        A list of random numbers from the exponential distribution.
    """
    if sz == 1 or not gamma_method:
        return [inverse_transform_method(lambda u: -np.log(1 - u) / l) for _ in range(sz)]

    # Method using a Gamma distribution.
    t = gamma_distribution(sz, 1/l)[0]
    u = sorted([rnd.random() for _ in range(sz - 1)] + [0, 1])
    return [(u[i] - u[i-1]) * t for i in range(1, len(u))]


if __name__ == "__main__":
    # Check if the generated random numbers are from the exponential distribution.
    l = 2
    print(f"Expected mean: {1 / l} and variance: {1 / l ** 2}")
    
    print(f"With Gamma method:")
    sz = 600
    random_numbers = exponential_distribution(l, sz)
    print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")

    print(f"With Inverse Transform method:")
    sz = 10**4
    random_numbers = exponential_distribution(l, sz, gamma_method=False)
    print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")