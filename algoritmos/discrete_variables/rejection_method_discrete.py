import random as rnd

def rejection_method(Y: callable, p: callable, q: callable, c: float, sz: int = 1) -> list[int]:
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
    def generate(Y: callable, p: callable, q: callable, c: float) -> int:
        while True:
            x = Y()
            U = rnd.random()
            if U < p(x) / (c * q(x)): return x
    
    return [generate(Y, p, q, c) for _ in range(sz)]