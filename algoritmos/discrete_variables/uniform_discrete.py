import random as rnd

def uniform_discrete_distribution(a: int, b: int, sz: int = 1) -> list[int]:
    """
    Generate a random number from a uniform discrete distribution.

    Parameters:
    a: int - Lower bound.
    b: int - Upper bound.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(a: int, b: int) -> int:
        U = rnd.random()
        return a + int((b - a + 1) * U)
    
    return [generate(a, b) for _ in range(sz)]

if __name__ == "__main__":
    a, b = 1, 6
    c = [0]*(b-a+1)
    for i in uniform_discrete_distribution(a, b, 10**6): c[i-a] += 1
    print([c[i]/sum(c) for i in range(len(c))])