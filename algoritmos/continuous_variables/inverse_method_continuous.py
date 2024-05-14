import random as rnd

def inverse_transform_method(G: callable) -> float:
    """
    Inverse Transform Method for generating random numbers from a given distribution.

    Parameters:
    G: callable
        The inverse of the cumulative distribution function of the distribution from which we want to generate random numbers.

    Returns:
    float
        A random number from the distribution.
    """
    U = rnd.random()
    return G(U)