import random as rnd

def risk_rate_method(p: callable, sz: int = 1) -> list[int]:
    """
    Generate a random number from a risk rate method.

    Parameters:
    p: callable - Probability function.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(p: callable) -> int:
        prob = p(0); s = 0; i = 0
        while True:
            U = rnd.random()
            if U < prob / (1 - s): return i
            i += 1; s += prob; prob = p(i)

    return [generate(p) for _ in range(sz)]