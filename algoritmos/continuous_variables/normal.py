import random as rnd
import numpy as np

def normal_distribution(m: float, s: float, sz: int = 1, method: str = "rejection") -> list[float]:
    """
    Generates random numbers from a normal distribution.

    Parameters:
    m: float
        The mean of the normal distribution.
    s: float
        The standard deviation of the normal distribution.
    sz: int
        The number of random numbers to generate.
    method: str
        The method to use for generating random numbers. Can be "rejection", "polar", "box-muller" or "uniform_ratios".
        Default is "rejection".

    Returns:
    list[float]
        A list of random numbers from the normal distribution.
    """
    def rejection_method() -> float:
        while True:
            u, y = -np.log(rnd.random()), -np.log(rnd.random())
            if y >= (u - 1) ** 2 / 2: return (u if rnd.random() < 0.5 else -u)
    
    def polar_method() -> list[float]:
        r2 = -2 * np.log(1 - rnd.random())
        theta = 2 * np.pi * rnd.random()
        x, y = np.sqrt(r2) * np.cos(theta), np.sqrt(r2) * np.sin(theta)
        return [x, y]
    
    def box_muller_method() -> list[float]:
        while True:
            v1, v2 = 2 * rnd.random() - 1, 2 * rnd.random() - 1
            if v1 ** 2 + v2 ** 2 <= 1:
                s = v1 ** 2 + v2 ** 2
                x, y = v1 * np.sqrt(-2 * np.log(s) / s), v2 * np.sqrt(-2 * np.log(s) / s)
                return [x, y]
        
    def uniform_ratios_method() -> float:
        c = 4 * np.exp(-0.5) / np.sqrt(2.0)
        while True:
            u, y = rnd.random(), 1 - rnd.random()
            z = c * (u - 0.5) / y
            if z ** 2 / 4 <= -np.log(y): return z
    
    match method:
        case "polar":
            r = []
            while len(r) < sz: r += [m + x * s for x in polar_method()]
            return r[:sz]
        case "box-muller":
            r = []
            while len(r) < sz: r += [m + x * s for x in box_muller_method()]
            return r[:sz]
        case "uniform_ratios":
            return [m + uniform_ratios_method() * s for _ in range(sz)]
        case "rejection":
            return [m + rejection_method() * s for _ in range(sz)]
        case _:
            raise ValueError("Invalid method. Please use 'rejection', 'polar', 'box-muller' or 'uniform_ratios'.")
    
if __name__ == "__main__":
    # Check if the generated random numbers are from the normal distribution.
    m_list = [-2, 2, 5, 10]
    s_list = [1, 1, 2, 3]
    sz = 10**5

    for i in range(len(m_list)):
        m, s = m_list[i], s_list[i]

        # Case 1: Using polar method.
        random_numbers = normal_distribution(m, s, sz, "polar")
        print(f"Using Polar method:")
        print(f"    Expected mean: {m} and variance: {s ** 2}")
        print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")

        # Case 2: Using Box-Muller method.
        random_numbers = normal_distribution(m, s, sz, "box-muller")
        print(f"Using Box-Muller method:")
        print(f"    Expected mean: {m} and variance: {s ** 2}")
        print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")

        # Case 3: Using Uniform Ratios method.
        random_numbers = normal_distribution(m, s, sz, "uniform_ratios")
        print(f"Using Uniform Ratios method:")
        print(f"    Expected mean: {m} and variance: {s ** 2}")
        print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")

        # Case 4: Using Rejection method.
        random_numbers = normal_distribution(m, s, sz, "rejection")
        print(f"Using Rejection method:")
        print(f"    Expected mean: {m} and variance: {s ** 2}")
        print(f"    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}")

        print("\n")