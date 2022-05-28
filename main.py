# punkt w 14-wymiarowej przestrzeni
# w głowie mamy ograniczenie do 3 wymiarów, żyjemy w 4,
# przewstrzeń metryczna, potrzebna para zbiór i element
# d - odległość
# 1. d(a,b)= 0 => a=b
# 2. d(a,b) = d(b,a)
# 3. if d(a,b) + d(b,c) >= d(a,c) nierówność trókąta
# jeżeli coś spełnia te warunki to jest to metryka, a zbiór przestrzenią metryczną
# żeby obliczyć odległość dwóch pkt od siebie korzystamy z twierdzenia pitagorasa
# c = pierw(a^2 + b^2)
# (Ax - Bx)^2 + (Ay-By)^2 i im więcej wymiarów tym więcej nawiasów
# ^rzutowanie na oś x ^rzutowanie na OY

import copy
import math
import random
from collections import defaultdict
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


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
    [1, 1, 1],
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
