def vonNeumann(seed: int, n: int) -> list[int]:
    """
    Generate a list of n pseudo-random numbers using the Von Neumann method.
    """
    numbers = []
    for i in range(n):
        numbers.append(seed)
        seed = (seed ** 2 // 100) % 10_000
    return numbers

# Test the function with the example values
if __name__ == "__main__":
    n = 10
    seed_list = [4010, 2100, 3792, 1234]
    for seed in seed_list:
        print(f"n, seed = {n}, {seed}: {vonNeumann(seed, n)}")