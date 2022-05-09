import math
import numpy as np


# sqrt(pow((a-b),2)
def metryka_euklidesowa(listaA, listaB):
    wynik = 0
    for i in range(len(listaA) - 1):
        wynik += (listaA[i] - listaB[i]) ** 2
    return math.sqrt(wynik)


def metryka_euklidesowa_wektory(a, b, z=False):
    if z:
        a = a[:-1]
        b = b[:-1]
    c = np.array(a) - np.array(b)
    return math.sqrt(np.dot(c, c))


print(metryka_euklidesowa([1, 2, 3], [3, 4, 6]))

print(metryka_euklidesowa_wektory([1, 2, 3], [3, 4, 6], True))