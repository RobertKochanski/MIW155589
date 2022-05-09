import numpy as np


def func(x):
    return x


def montecarlo(func, a, b, n):
    x = np.random.uniform(a, b, n)
    y = [func(val) for val in x]
    y_mean = np.sum(y) / n
    return (b - a) * y_mean


def rectangle(a, b, func, n):
    dx = (b - a) / n
    result = 0
    for x in range(n):
        x = x * dx + a
        result += func(x) * dx
    return result


print("Całka metodą Monte Carlo: ", montecarlo(func, 0, 1, 1000))
print("Całka metodą prostokątów: ", rectangle(0, 1, func, 1000))


