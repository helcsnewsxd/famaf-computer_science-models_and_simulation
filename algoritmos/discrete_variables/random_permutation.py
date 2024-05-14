from uniform_discrete import uniform_discrete_distribution

def random_permutation(a: list) -> list:
    """
    Generate a random permutation of a list.

    Parameters:
    a: list - List to be permuted.

    Returns:
    list - Random permutation of the list.
    """
    b = a.copy()
    n = len(b)
    for j in range(n-1, 0, -1):
        i = uniform_discrete_distribution(0, j)[0]
        b[i], b[j] = b[j], b[i]
    return b

def random_sample(a: list, k: int, inv: bool = False) -> list:
    """
    Generate a random sample of k elements from a list.

    Parameters:
    a: list - List to be sampled.
    k: int - Number of elements to be sampled.
    inv: bool - If True, the sample will be the complement of the random sample.

    Returns:
    list - Random sample of k elements from the list.
    """
    n = len(a)
    if k > n/2: return random_sample(a, n-k, True)

    b = a.copy()
    for j in range(n-1, n-k-1, -1):
        i = uniform_discrete_distribution(0, j)[0]
        b[i], b[j] = b[j], b[i]
    return b[:n-k] if inv else b[n-k:]

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print(random_permutation(a))
    for i in range(6):
        print(random_sample(a, i))