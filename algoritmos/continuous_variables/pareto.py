import numpy as np
from inverse_method_continuous import inverse_transform_method

def pareto_distribution(a: float, sz: int = 1) -> list[float]:
    """
    Generates random numbers from a Pareto distribution with shape parameter `a`.

    Parameters:
    a: float
        Shape parameter of the Pareto distribution.
    sz: int, optional
        Number of random numbers to generate. Default is 1.

    Returns:
    list[float]
        Random numbers from a Pareto distribution.
    """    
    pareto_density_inverse = lambda p: (1 / (1 - p)) ** (1 / a)
    return [inverse_transform_method(pareto_density_inverse) for _ in range(sz)]

if __name__ == "__main__":
    # Check if the generated random numbers are from the gamma distribution.
    sz = 10**5
    a = 2
    random_numbers = pareto_distribution(a, sz)
    print(f"Expected mean: {a / (a - 1)}")
    print(f"Generated mean: {np.mean(random_numbers)}")