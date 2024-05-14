import random as rnd

def discrete_distribution(p: list[float], x: list[int], sz: int = 1) -> list[int]:
    """
    Generate a random number from a discrete distribution.

    Parameters:
    p: list[float] - List of probabilities.
    x: list[int] - List of values.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(p: list[float], x: list[int]) -> int:
        r = rnd.random()
        i = 0; prob = p[i]
        while r >= prob: i += 1; prob += p[i]
        return x[i]
    
    assert len(p) == len(x), "The probabilities and values lists must have the same length."
    return [generate(p, x) for _ in range(sz)]

def discrete_distribution_function(p: callable, sz: int = 1) -> list[int]:
    """
    Generate a random number from a discrete distribution.
    This considers the values from 0 to inf.

    Parameters:
    p: callable - Probability function.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(p: callable) -> int:
        r = rnd.random(); i = 0
        prob = p(i)
        while r >= prob: i += 1; prob += p(i)
        return i
    
    return [generate(p) for _ in range(sz)]

if __name__ == "__main__":
    p = [0.1, 0.2, 0.3, 0.4]
    x = [1, 2, 3, 4]
    c = [0]*len(x)
    for i in discrete_distribution(p, x, 10**6): c[i-1] += 1
    print([c[i]/sum(c) for i in range(len(c))])

    p = lambda x: x/10
    c = [0]*5
    for i in discrete_distribution_function(p, 10**6): c[i] += 1
    print([c[i]/sum(c) for i in range(len(c))])