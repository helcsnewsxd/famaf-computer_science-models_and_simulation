import numpy as np
import random as rnd
from inverse_method_continuous import inverse_transform_method

def cauchy_distribution(l: float, sz: int = 1, method: str = 'polar') -> list[float]:
    """
    Generates random numbers from a Cauchy distribution with parameter `l`.

    Parameters:
    l: float
        Parameter of the Cauchy distribution.
    sz: int
        Number of random numbers to generate.
        Default is 1.
    method: str
        Method to generate the random numbers.
        Options are 'polar' and 'inverse'.
        Default is 'polar'.

    Returns:
    list[float]
        Random numbers from a Cauchy distribution.
    """
    def cauchy_polar_method(l: float, sz: int) -> list[float]:
        def generate():
            while True:
                u, v = rnd.random() * 2 - 1, rnd.random() * 2 - 1
                if v**2 + u**2 <= 1:
                    return v / u
        return [l * generate() for _ in range(sz)]

    def cauchy_inverse_transform_method(l: float, sz: int) -> float:
        cauchy_inverse_cumulative = lambda p: l * np.tan(np.pi * (p - 1/2))
        return [inverse_transform_method(cauchy_inverse_cumulative) for _ in range(sz)]
    
    match method:
        case 'polar':
            return cauchy_polar_method(l, sz)
        case 'inverse':
            return cauchy_inverse_transform_method(l, sz)
        case _:
            raise ValueError('Invalid method. Options are "polar" and "inverse".')

if __name__ == '__main__':
    # Check if the random numbers are from a Cauchy distribution
    l_list = [1, 2.5, 0.3]
    method_list = ['polar', 'inverse']
    sz = 10**5

    for l in l_list:
        for method in method_list:
            print(f'Cauchy distribution with l = {l} and method = {method}')
            random_numbers = cauchy_distribution(l, sz, method)
            proportion = len([x for x in random_numbers if -l <= x <= l]) / sz
            print(f'    Actual mean: {np.mean(random_numbers)} and variance: {np.var(random_numbers)}')
            print(f'    Proportion of numbers between -l and l: {proportion} vs. real value: {1/2}\n')