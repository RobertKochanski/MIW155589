import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv

# REGRESJA LINIOWA
x = np.array([2, 5, 7, 8]).reshape((4, 1))
y = np.array([1, 2, 3, 3]).reshape((4, 1))
X = np.array([
    [1, 2],
    [1, 5],
    [1, 7],
    [1, 8],
])


def regresja_liniowa(x, y, X):
    B = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.transpose(X)), y)  # ((XT * X) ** -1) * XT * y
    # B = inv(np.transpose(X) @ X) @ np.transpose(X) @ y   ######## @ - mnożenie macierzy
    B_0 = B[0][0]
    B_1 = B[1][0]
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=1)
    plt.plot(x, [(q * B_1) + B_0 for q in x], color='blue')
    plt.title('Regresja liniowa')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


regresja_liniowa(x, y, X)
