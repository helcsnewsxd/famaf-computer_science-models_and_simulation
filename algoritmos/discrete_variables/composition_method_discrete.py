def composition_method(p: list[float], f: list[callable], sz: int = 1) -> list[int]:
    """
    Generates random numbers from a distribution using the composition method.

    Parameters:
    p: list[float]
        The probabilities of the distributions.
    f: list[callable]
        The functions that generate random numbers from the distributions.
    sz: int
        The number of random numbers to generate.

    Returns:
    list[int]
        A list of random numbers from the distribution.
    """
    def generate(p: list[float], f: list[callable]) -> float:
        U = rnd.random()
        i = 0
        while U > p[i]: U -= p[i]; i += 1
        return f[i]()
    
    return [generate(p, f) for _ in range(sz)]