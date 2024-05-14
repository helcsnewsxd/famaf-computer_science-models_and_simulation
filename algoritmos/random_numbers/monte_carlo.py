import random as rnd

def monteCarlo(f: callable, a: float, b: float, n: int) -> float:
    """
    Estimate the integral of f from a to b using the Monte Carlo method.
    a, b: interval [a, b]
    b is inf. if b is None
    """
    def estimate(f: callable, a: float, b: float, n: int) -> float:
        """
        Do the estimation method for fixed interval [a, b]
        """
        r = 0
        for i in range(n):
            x = rnd.random()
            r += f(a + (b - a) * x)
        return (b - a) * r / n

    g = lambda x: f(1/x - 1) / x**2
    match b:
        case None: return estimate(g, 0, 1, n) + estimate(f, a, 0, n)
        case _: return estimate(f, a, b, n)

def monteCarlo_multiple(f: callable, I: list[tuple[float, float]], n: int) -> float:
    """
    Estimate the multiple integral of function f over intervals in I using the Monte Carlo method.
    I[i][0], I[i][1]: interval [a, b]
        b is inf. if b is None => a must be 0
    f: function to integrate, takes a list of variables
    """
    def estimate(f: callable, I: list[tuple[float, float]], n: int) -> float:
        """
        Do the estimation method for fixed intervals
        """
        r = 0
        for i in range(n):
            x = [rnd.random() for _ in range(len(I))]
            r += f(x, I)
        m = 1
        for i in range(len(I)): m *= I[i][1] - I[i][0] if I[i][1] is not None else 1
        return m * r / n

    def g(x: list[float], I: list[tuple[float, float]]) -> float:
        """
        Function to estimate with fixed intervals [a, b]
        """
        denominator = 1
        for i in range(len(I)):
            if I[i][1] is None:
                assert I[i][0] == 0
                denominator *= x[i]**2
                x[i] = 1/x[i] - 1
            else:
                x[i] = I[i][0] + (I[i][1] - I[i][0]) * x[i]
        return f(x) / denominator

    return estimate(g, I, n)