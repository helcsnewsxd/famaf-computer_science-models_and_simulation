import numpy as np
import math
from inverse_method_continuous import inverse_transform_method

def weibull_distribution(a: float, b: float, sz: int = 1) -> list[float]:
    """
    Generates random numbers from a Weibull distribution with shape parameter `a` and scale parameter `b`.

    Parameters:
    a: float
        Shape parameter of the Weibull distribution.
    b: float
        Scale parameter of the Weibull distribution.
    sz: int
        Number of random numbers to generate.
        Default is 1.

    Returns:
    list[float]
        Random numbers from a Weibull distribution.
    """
    weibull_density_inverse = lambda p: b * (-np.log(1 - p)) ** (1 / a)
    return [inverse_transform_method(weibull_density_inverse) for _ in range(sz)]

if __name__ == "__main__":
    # Check if the generated random numbers are from the gamma distribution.
    sz = 10**5
    a = 2
    b = 1
    random_numbers = weibull_distribution(a, b, sz)
    print(f"Expected mean: {b / a * math.gamma(1 / a)}")
    print(f"Generated mean: {np.mean(random_numbers)}")