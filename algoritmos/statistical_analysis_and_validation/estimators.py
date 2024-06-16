import numpy as np
import random as rnd


def calculate_principal_estimators(generator: callable = rnd.random, n: int = 1, d: float = 0.1):
    """
    Calculate the principal estimators (mean and variance) of the given generator.

    Parameters:
    - generator (callable): A random number generator.
    - n (int): The number of samples to generate.
    - d (float): The limit for standard deviation.

    Returns:
    - mean (float): The mean of the samples.
    - variance (float): The variance of the samples.
    - n (int): The number of samples generated.
    """

    mean = generator()
    s2 = 0
    i = 1
    while i <= n or np.sqrt(s2/i) > d:
        i += 1
        X = generator()

        prev_mean = mean
        mean = mean + (X - mean) / i
        s2 = s2 * (1 - 1/(i-1)) + i * (mean - prev_mean)**2

    return mean, s2, i
