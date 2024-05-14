import random as rnd
from geometric import geometric_distribution

def bernoulli_distribution(p: float, sz: int = 1) -> list[int]:
    """
    Generate a random number from a Bernoulli distribution.

    Parameters:
    p: float - Probability of success.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    if sz == 1:
        return [1 if rnd.random() < p else 0]
    
    # Using the geometric distribution
    r_list = [0] * sz
    j = geometric_distribution(p)[0] - 1
    while j < sz: r_list[j] = 1; j += geometric_distribution(p)[0]
    return r_list

if __name__ == "__main__":
    p = 0.3
    c = dict()
    for x in bernoulli_distribution(p, 10**6): c[x] = c.get(x, 0) + 1
    print(c[0]/sum(c.values()), c[1]/sum(c.values()))

    c.clear()
    for _ in range(10**6):
        x = bernoulli_distribution(p)[0]
        c[x] = c.get(x, 0) + 1
    print(c[0]/sum(c.values()), c[1]/sum(c.values()))