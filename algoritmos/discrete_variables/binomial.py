import random as rnd

def binomial_distribution(n: int, p: float, sz: int = 1) -> list[int]:
    """
    Generate a random number from a binomial distribution.

    Parameters:
    n: int - Number of trials.
    p: float - Probability of success.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def generate(n: int, p: float) -> int:
        c = p / (1 - p); prob = (1 - p)**n
        F = prob; U = rnd.random()
        
        for j in range(1, int(n * p) + 1): prob *= c * (n - j + 1) / j; F += prob
        if U >= F:
            j = int(n * p) + 1
            while U >= F: prob *= c * (n - j + 1) / j; F += prob; j += 1
            return j - 1
        else:
            j = int(n * p)
            while U < F: F -= prob; prob *= j / (c * (n - j + 1)); j -= 1
            return j + 1

    if p > 0.5: return [n - generate(n, 1 - p) for _ in range(sz)]
    else: return [generate(n, p) for _ in range(sz)]

if __name__ == "__main__":
    n, p = 10, 0.3
    c = dict()
    for x in binomial_distribution(n, p, 10**6): c[x] = c.get(x, 0) + 1
    for k in sorted(c.keys()): print(k, c[k]/sum(c.values()))