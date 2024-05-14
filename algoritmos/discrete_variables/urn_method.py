from uniform_discrete import uniform_discrete_distribution

def urn_method(n: int, p: list[float], x: list[int], sz: int = 1) -> list[int]:
    """
    Generate a random number from an urn method.

    Parameters:
    n: int - Number of balls.
    p: list[float] - List of probabilities.
    x: list[int] - List of values.
    sz: int - Number of random numbers to generate.

    Returns:
    list[int] - List of random numbers.
    """
    def simulate(A: list[int]) -> int:
        return A[uniform_discrete_distribution(0, len(A) - 1)[0]]

    A = []
    for i in range(len(p)): A.extend([x[i]] * int(p[i] * n))
    return [simulate(A) for _ in range(sz)]