import random as rnd
import numpy as np
from exponential import exponential_distribution

# HOMOGENEOUS POISSON PROCESS
def poisson_process_events(l: float, t: float) -> list[float]:
    """
    Generates the events of a Poisson process until a given time 't'.

    Parameters:
    l: float
        The rate parameter of the Poisson process.
    t: float
        The time until which the events are generated.

    Returns:
    list[float]
        A list of times at which the events occur.
    """
    x = 0; events = []
    while True:
        x += exponential_distribution(l)[0]
        if x > t: break
        events.append(x)
    return events

# NON-HOMOGENEOUS POISSON PROCESS
def poisson_no_homogeneous_process_events(fl: callable, l: float, t: float) -> list[float]:
    """
    Generates the events of a non-homogeneous Poisson process until a given time 't'.

    Parameters:
    fl: callable
        The function that returns the rate parameter at time 't'.
    l: float
        The upper bound of the rate parameter.
    t: float
        The time until which the events are generated.

    Returns:
    list[float]
        A list of times at which the events occur.
    """
    x = 0; events = []
    while True:
        x += exponential_distribution(l)[0]
        if x > t: break
        if rnd.random() < fl(x) / l: events.append(x)
    return events

def poisson_no_homogeneous_process_events_optimized(fl: callable, l: list[float], t: list[float]) -> list[float]:
    """
    Generates the events of a non-homogeneous Poisson process with time intervals until a given time 't[-1]'.

    Parameters:
    fl: callable
        The function that returns the rate parameter at time 't'.
    l: list[float]
        The upper bound of the rate parameter.
    t: list[float]
        The time until which the events are generated (intervals).
    
    Returns:
    list[float]
        A list of times at which the events occur.
    """
    x = 0; events = []; i = 0
    while True:
        x += exponential_distribution(l[i])[0]
        while i != len(t) - 1 and x > t[i]: x = t[i] + (x - t[i]) * l[i] / l[i+1]; i += 1
        if x > t[-1]: break
        if rnd.random() < fl(x) / l[i]: events.append(x)
    return events

if __name__ == "__main__":
    # Check if the generated events are from a Poisson process.
    print(f"Homogeneous Poisson Process:")
    l = 2
    t = 10
    sz = 10**4
    cnt_events = [len(poisson_process_events(l, t)) for _ in range(sz)]
    print(f"    Expected mean: {l * t}")
    print(f"    Actual mean: {np.mean(cnt_events)}")

    # Check if the generated events are from a non-homogeneous Poisson process.
    print(f"Non-Homogeneous Poisson Process:")
    fl = lambda x: 2 + np.sin(x)
    l = 3
    t = 10
    sz = 10**4
    cnt_events = [len(poisson_no_homogeneous_process_events(fl, l, t)) for _ in range(sz)]
    print(f"    Using the basic method:")
    print(f"        Expected mean: {t * np.mean([fl(x) for x in np.linspace(0, t, 1000)])}")
    print(f"        Actual mean: {np.mean(cnt_events)}")

    l = [2 + np.sin(x) for x in np.linspace(0, 10, 1000)]
    t = np.linspace(0, 10, 1000)
    cnt_events = [len(poisson_no_homogeneous_process_events_optimized(fl, l, t)) for _ in range(sz)]
    print(f"    Using the optimized method:")
    print(f"        Expected mean: {t[-1] * np.mean([fl(x) for x in np.linspace(0, t[-1], 1000)])}")
    print(f"        Actual mean: {np.mean(cnt_events)}")
