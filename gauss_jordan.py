import numpy as np


def gj(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    for i in range(n):
        if np.abs(a[i, i]) <= 0:
            for j in range(i+1, n):
                if np.abs(a[j, i]) > np.abs(a[i, i]):
                    for k in range(i, n):
                        a[i, k], a[j, k] = a[j, k], a[i, k]
                    b[i], b[j] = b[j], b[i]
                    break

        pivot = a[i, i]
        for j in range(i, n):
            if pivot == 0:
                break
            a[i, j] /= pivot
        if pivot != 0:
            b[i] /= pivot

        for j in range(n):
            if j == i or a[j, i] == 0: continue
            factor = a[j, i]
            for k in range(i, n):
                a[j, k] -= factor * a[i, k]
            b[j] -= factor * b[i]

    return a, b


a = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [0, 0, 1],
])
b = np.array([
    [6],
    [4],
    [2],
])

a, b = gj(a, b)

print(a)
print(b)
