import random as rnd
import numpy as np
from exponential import exponential_distribution

def rejection_method(Y: callable, p: callable, q: callable, c: float, sz: int = 1) -> list[float]:
    """
    Estimate the expected value of a function using the rejection method.

    Parameters:
    Y: callable - Function to simulate the random variable.
    p: callable - Probability function of the random variable of X.
    q: callable - Probability function of the random variable of Y.
    c: float - Constant such that p(x) <= c * q(x) for all x.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(Y: callable, p: callable, q: callable, c: float) -> float:
        while True:
            x = Y()
            U = rnd.random()
            if U < p(x) / (c * q(x)): return x
    
    return [generate(Y, p, q, c) for _ in range(sz)]

def transform_rejection_method(H: callable, Hd: callable, p: callable, c: float, sz: int = 1) -> list[float]:
    """
    Estimate the expected value of a function using the rejection method.

    Parameters:
    H: callable - Inverse of the cumulative distribution function of the random variable of Y.
    Hd: callable - Derivative of H.
    p: callable - Probability function of the random variable of X.
    c: float - Constant such that p(x) <= c * q(x) for all x.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(H: callable, Hd: callable, p: callable, c: float) -> float:
        while True:
            U = rnd.random(); V = rnd.random()
            HU = H(U); HdU = Hd(U)
            if V < p(HU) * HdU / c: return HU
    
    return [generate(H, Hd, p, c) for _ in range(sz)]

if __name__ == "__main__":
    # Check to generate Gamma(3/2, 1) with Y as exponential(2/3)
    a = 3/2; b = 1
    Y = lambda: exponential_distribution(2/3)[0]
    p = lambda x : 2/np.pi * x**(1/2) * np.exp(-x)
    q = lambda x : 2/3 * np.exp(-2/3 * x)

    sz = 10**5
    random_numbers = rejection_method(Y, p, q, 1.35, sz)
    print(f"Using Rejection Method:")
    print(f"    Expected mean: {a * b} and variance: {a * b ** 2}")
    print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")

    # Check to generate Gamma(3/2, 1) with Y as exponential(2/3)
    H = lambda x: -3/2 * np.log(1 - x)
    Hd = lambda x: 3/2 / (1 - x)
    c = 3 * np.sqrt(3/(2*np.pi*np.e))
    random_numbers = transform_rejection_method(H, Hd, p, c, sz)
    print(f"Using Transform Rejection Method:")
    print(f"    Expected mean: {a * b} and variance: {a * b ** 2}")
    print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")