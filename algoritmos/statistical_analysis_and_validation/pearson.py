import numpy as np
import random as rnd
from scipy.stats import chi2


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
        c = p / (1 - p)
        prob = (1 - p)**n
        F = prob
        U = rnd.random()

        for j in range(1, int(n * p) + 1):
            prob *= c * (n - j + 1) / j
            F += prob
        if U >= F:
            j = int(n * p) + 1
            while U >= F:
                prob *= c * (n - j + 1) / j
                F += prob
                j += 1
            return j - 1
        else:
            j = int(n * p)
            while U < F:
                F -= prob
                prob *= j / (c * (n - j + 1))
                j -= 1
            return j + 1

    if p > 0.5:
        return [n - generate(n, 1 - p) for _ in range(sz)]
    else:
        return [generate(n, p) for _ in range(sz)]


def pearson_estimator(N: list[int], p: list[float]) -> float:
    """
    Calculates the Pearson estimator of a list of numbers.

    Parameters:
    N: list[int]
        The list of frequencies.
    p: list[float]
        The list of probabilities.

    Returns:
    float
        The Pearson estimator of the list of numbers.
    """
    assert len(N) == len(p)

    n = sum(N)
    return sum((N[i] - n * p[i]) ** 2 / (n * p[i]) for i in range(len(N)))


def pearson_p_value(t: float, df: int) -> float:
    """
    Calculates the p-value of the Pearson estimator.

    Parameters:
    t: float
        The value of the Pearson estimator.
    df: int
        The degrees of freedom.

    Returns:
    float
        The p-value of the Pearson estimator.
    """
    return 1.0 - chi2.cdf(t, df)


def pearson_p_value_sim(t: float, n_sim: int, p: list[float], n: int):
    """
    Calculates the p-value of the Pearson estimator using simulation.

    Parameters:
    t: float
        The value of the Pearson estimator.
    n_sim: int
        The number of simulations to run.
    p: list[float]
        The list of probabilities.
    n: int
        The size of the original sample.

    Returns:
    float
        The p-value of the Pearson estimator.
    """
    def create_observation_freq(n: int, p: list[float]):
        N = np.zeros(len(p))
        N[0] = binomial_distribution(n, p[0])[0]
        for i in range(1, len(p) - 1):
            N[i] = binomial_distribution(
                n - sum(N[:i]), p[i]/(1 - sum(p[:i])))[0]
        N[-1] = n - sum(N[:-1])
        return np.array(N, dtype=int)

    p_value = 0
    for _ in range(n_sim):
        N = create_observation_freq(n, p)
        t_sim = pearson_estimator(N, p)
        if t_sim >= t:
            p_value += 1
    return p_value / n_sim
