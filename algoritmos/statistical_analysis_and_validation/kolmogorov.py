import random as rnd


def kolmogorov_estimator(sample: list[float], F: callable):
    """
    Calculates the Kolmogorov estimator of a list of numbers.

    Parameters:
    sample: list[float]
        The list of numbers.
    F: callable
        The cumulative distribution function.

    Returns:
    float
        The Kolmogorov estimator of the list of numbers.
    """

    n = len(sample)
    s_sample = sorted(sample)

    D = 0
    for i in range(n):
        D = max((i + 1) / n - F(s_sample[i]), F(s_sample[i]) - i / n, D)

    return D


def kolmogorov_p_value_sim(d: float, n_sim: int, n: int):
    """
    Calculates the p-value of the Kolmogorov estimator using simulation.

    Parameters:
    d: float
        The value of the Kolmogorov estimator.
    n_sim: int
        The number of simulations to run.
    n: int
        The size of the original sample.

    Returns:
    float
        The p-value of the Kolmogorov estimator.
    """
    p_value = 0
    for _ in range(n_sim):
        sample = [rnd.random() for _ in range(n)]
        D = kolmogorov_estimator(sample, lambda x: x)
        if D >= d:
            p_value += 1

    return p_value / n_sim
